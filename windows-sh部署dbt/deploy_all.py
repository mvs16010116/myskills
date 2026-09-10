#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HICCPET 数仓 Airflow 部署脚本（Python 版，Windows 原生可运行）。

功能与 airflow/deploy/deploy_all.sh 完全一致（1004 行 bash 的等价实现）：
  1. 发布 DAG 文件到 Composer GCS /dags/
  2. 发布 dbt 工程到 Composer GCS /data/hicc_data_platform/
  3. 发布 dbt profiles.yml 到 Composer GCS /data/
  4. 发布下游消费脚本到 Composer GCS /data/{shipment_model,monitor,feishu_sync}/
  5. 自动同步 DTS transfer configs（crawl_sources.yaml 变更时）

为什么用 Python：
  Windows 上运行 Mac/Linux 生成的 bash 脚本有一堆兼容性坑：
  - PowerShell 裸 `bash` 指向旧版 WSL sh，不支持 `set -o pipefail`
  - msys bash 需 MSYSTEM 环境变量，非 tty 输出还会被管道吞
  - `command -v timeout` 命中 C:\\Windows\\System32\\timeout.exe（语法 TIMEOUT /T）
  本脚本直接调用 gsutil/dbt/python，天然跨平台。

使用方式（PowerShell 直接跑）：
  python airflow/deploy/deploy_all.py                       # 全量
  python airflow/deploy/deploy_all.py --module dags         # 只发布 DAG
  python airflow/deploy/deploy_all.py --module dags --dry-run
  python airflow/deploy/deploy_all.py --file some/file.py
  python airflow/deploy/deploy_all.py --module dts          # 单独同步 DTS
  python airflow/deploy/deploy_all.py --module dags --skip-dts   # 紧急跳过 DTS

Windows 注意：
  gsutil 认证：脚本会自动检测 BOTO_CONFIG，未设置且存在服务账号 key 时，
  自动生成 boto 配置指向 hiccpet-481303-f7f2e4edc9ac.json（本机无 gcloud
  auth login 用户凭证，只有服务账号可用）。
  也可手动：$env:BOTO_CONFIG="$env:TEMP\\hicc_gs_boto.cfg"
  DTS 密码：export DTS_MYSQL_PASSWORD=xxx（或交互输入）
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# ============================================================================
# 配置
# ============================================================================

BUCKET = "asia-southeast1-hicc-e1a70e20-bucket"


def _find_project_root(start: Path) -> Path:
    """从脚本所在位置向上探测项目根（含 hicc_data_platform/dbt_project.yml 的目录）。

    脚本可放在任意位置（本 skill 目录 / airflow/deploy/ 等），不再依赖固定层级。
    """
    for p in (start, *start.parents):
        if (p / "hicc_data_platform" / "dbt_project.yml").exists():
            return p
    raise RuntimeError("找不到项目根（未发现 hicc_data_platform/dbt_project.yml）")


PROJECT_ROOT = _find_project_root(Path.cwd())
DAGS_DIR = PROJECT_ROOT / "airflow" / "dags"
DEPLOY_DIR = PROJECT_ROOT / "airflow" / "deploy"

CRAWL_SOURCES_YAML_REL = "airflow/dags/config/crawl_sources.yaml"
DTS_CONFIGS_YAML_REL = "airflow/dags/config/dts_transfer_configs.yaml"

# 模块与发布顺序（dts 是"单独同步 DTS"的特殊模块，不发布文件）
MODULE_ORDER = ["dags", "dbt", "profiles", "monitor", "shipment", "feishu"]


# ============================================================================
# 工具函数
# ============================================================================

def _which(name: str) -> str | None:
    """跨平台查找可执行文件（Windows 下自动补 .exe/.cmd/.bat 扩展名）。"""
    return shutil.which(name)


def _wrap_windows_cmd(cmd: list[str]) -> list[str]:
    """Windows 下 .cmd/.bat 需经 cmd /c 执行（subprocess 无法直接 CreateProcess .cmd）。"""
    if os.name != "nt":
        return cmd
    full = shutil.which(cmd[0])
    if full and full.lower().endswith((".cmd", ".bat")):
        return ["cmd", "/c"] + [full] + cmd[1:]
    return cmd


def run(cmd: list[str], cwd: Path | None = None, check: bool = False,
        timeout: float | None = None) -> int:
    """执行命令，返回退出码（stderr 透传，Windows 下 UTF-8 解码容错）。"""
    proc = subprocess.run(
        _wrap_windows_cmd(cmd),
        cwd=str(cwd) if cwd else None,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and proc.returncode != 0:
        raise RuntimeError(f"命令失败 ({proc.returncode}): {' '.join(cmd)}")
    return proc.returncode


# ============================================================================
# gsutil 执行（dry-run 只打印 + 超时 + 重试 3 次指数退避）
# ============================================================================

def ensure_gsutil_auth() -> None:
    """保证 gsutil 有可用凭据。

    Windows 本机只有服务账号 key（供 BigQuery 客户端用），没有
    `gcloud auth login` 的用户凭证 → gsutil 匿名 401。
    解决：自动生成 boto 配置指向服务账号 key（不改全局 gcloud 状态）。
    若用户已设置 BOTO_CONFIG 或已有用户凭证，则跳过。
    """
    if os.environ.get("BOTO_CONFIG") and os.environ.get("CLOUDSDK_CONFIG"):
        return
    sa_key = PROJECT_ROOT / "hiccpet-481303-f7f2e4edc9ac.json"
    if not sa_key.exists():
        return
    # 隔离 gcloud 配置目录：避免与用户账号（gcloud auth login）的多凭据冲突
    iso_dir = Path(tempfile.gettempdir()) / "hicc_gcloud_iso"
    iso_dir.mkdir(parents=True, exist_ok=True)
    os.environ["CLOUDSDK_CONFIG"] = str(iso_dir)
    # 服务账号 key 作为 ADC（供 gcloud / BigQuery 客户端 / gsutil 统一使用）
    adc = iso_dir / "application_default_credentials.json"
    if not adc.exists():
        adc.write_text(sa_key.read_text(encoding="utf-8"), encoding="utf-8")
    # boto 配置：仅指向服务账号 key
    boto = Path(tempfile.gettempdir()) / "hicc_gs_boto.cfg"
    if not boto.exists():
        boto.write_text(
            f"[Credentials]\ngs_service_key_file = {sa_key.as_posix()}\n",
            encoding="ascii",
        )
    os.environ["BOTO_CONFIG"] = str(boto)
    print(f"  [auth] 自动注入 gsutil boto 认证 → {sa_key.name}（CLOUDSDK_CONFIG 隔离）")


def _find_gsutil() -> str:
    exe = _which("gsutil")
    if not exe:
        raise RuntimeError("找不到 gsutil，请安装 Google Cloud SDK")
    return exe


def run_gsutil(cmd_str: str, dry_run: bool = False) -> int:
    """执行 gsutil 命令（注入 -o GSUtil:parallel_process_count=1、超时、重试）。

    与 deploy_all.sh 的 run_gsutil 行为一致：
      - dry-run 只打印
      - 注入 -o GSUtil:parallel_process_count=1（避免 Windows/macOS 凭据锁冲突）
      - 300s 超时（subprocess timeout）
      - 失败重试 3 次（指数退避 5s/10s）
    """
    if dry_run:
        print(f"    [DRY-RUN] {cmd_str}")
        return 0

    gsutil = _find_gsutil()
    # 在 "gsutil" 之后注入并行进程数=1 参数
    assert cmd_str.startswith("gsutil"), f"仅支持 gsutil 命令，收到: {cmd_str}"
    rest = cmd_str[len("gsutil"):].strip()
    base_cmd = _wrap_windows_cmd([gsutil, "-o", "GSUtil:parallel_process_count=1"] + rest.split())

    last_exit = -1
    for attempt in range(1, 4):
        try:
            proc = subprocess.run(
                base_cmd, text=True, encoding="utf-8", errors="replace",
                timeout=300,
            )
            last_exit = proc.returncode
        except subprocess.TimeoutExpired:
            last_exit = 124
            print(f"    ⏰ gsutil 超时 (300s)，attempt {attempt}/3", file=sys.stderr)
            continue
        except FileNotFoundError:
            raise RuntimeError(f"gsutil 不存在: {gsutil}")

        if last_exit == 0:
            return 0
        print(f"    ⚠️  gsutil 失败 (attempt {attempt}/3, exit={last_exit})",
              file=sys.stderr)
        if attempt < 3:
            sleep_sec = attempt * 5
            print(f"    ⏳ {sleep_sec}s 后重试...", file=sys.stderr)
            time.sleep(sleep_sec)

    print(f"    ❌ gsutil 重试 3 次仍失败", file=sys.stderr)
    print(f"    命令: {cmd_str}", file=sys.stderr)
    return last_exit


# ============================================================================
# 前置检查
# ============================================================================

def preflight_auth() -> None:
    if run(["gcloud", "auth", "application-default", "print-access-token"]) != 0:
        print("❌ gcloud ADC 认证失败，请先执行:", file=sys.stderr)
        print("   gcloud auth application-default login", file=sys.stderr)
        sys.exit(1)


def preflight_bucket() -> None:
    ensure_gsutil_auth()
    if run_gsutil(f"gsutil ls gs://{BUCKET}") != 0:
        print(f"❌ 无法访问 bucket: gs://{BUCKET}", file=sys.stderr)
        print("   请检查认证账号权限和 bucket 名称", file=sys.stderr)
        sys.exit(1)


# ============================================================================
# DTS transfer configs 管理
# ============================================================================

def is_crawl_sources_file(rel_path: str) -> bool:
    return rel_path == CRAWL_SOURCES_YAML_REL


def sync_dts_configs(dry_run: bool = False) -> int:
    """调用 setup_dts_transfers.py 同步 DTS transfer configs（本地 diff，零 API 调用优先）。"""
    script = DEPLOY_DIR / "setup_dts_transfers.py"
    if not script.exists():
        print(f"  ❌ setup_dts_transfers.py 不存在: {script}", file=sys.stderr)
        return 1

    print("[dts] 同步 DTS transfer configs...")
    py = sys.executable

    if dry_run:
        print("  [DRY-RUN] DTS_MYSQL_PASSWORD=*** python setup_dts_transfers.py --dry-run")
        env = dict(os.environ)
        env.setdefault("DTS_MYSQL_PASSWORD", "dry-run-placeholder")
        proc = subprocess.run(
            [py, str(script), "--dry-run"], text=True, encoding="utf-8",
            errors="replace", env=env,
        )
        if proc.returncode != 0:
            print("  ⚠️  DTS dry-run 预览失败（不影响后续部署）", file=sys.stderr)
        return 0

    # 轻量级预检（无需密码）：判断是否真的需要远程操作
    check = subprocess.run([py, str(script), "--check-only"],
                           text=True, encoding="utf-8", errors="replace")
    if check.returncode == 0:
        print("  [OK] DTS 配置已是最新，无需同步（跳过密码输入）")
        return 0

    if not os.environ.get("DTS_MYSQL_PASSWORD"):
        print("  ⚠️  DTS 配置有变更，需要 MySQL 密码...")
        print("     推荐用法：$env:DTS_MYSQL_PASSWORD='xxx'; python airflow/deploy/deploy_all.py ...")

    proc = subprocess.run([py, str(script)], text=True, encoding="utf-8",
                          errors="replace")
    if proc.returncode != 0:
        print("  ❌ DTS 同步失败（crawl_sources.yaml 与 DTS 服务状态不一致）",
              file=sys.stderr)
        print(f"     可手动排查：python {script} --dry-run", file=sys.stderr)
        return 1

    dts_yaml = PROJECT_ROOT / DTS_CONFIGS_YAML_REL
    if not dts_yaml.exists():
        print(f"  ❌ DTS 配置文件未生成: {dts_yaml}", file=sys.stderr)
        print(f"     请手动运行：python {script}", file=sys.stderr)
        return 1

    print("  [OK] DTS transfer configs 已同步（dts_transfer_configs.yaml 已更新）")
    return 0


# ============================================================================
# dbt manifest 管理
# ============================================================================

def is_dbt_source_file(rel_path: str) -> bool:
    """是否 dbt 源文件（修改后需重新 dbt parse）。与 deploy_all.sh 的 case 一致。"""
    rel = rel_path.replace("\\", "/")
    return (
        rel in ("hicc_data_platform/dbt_project.yml", "hicc_data_platform/packages.yml")
        or rel.startswith("hicc_data_platform/models/")
        or rel.startswith("hicc_data_platform/macros/")
    )


def parse_dbt_and_upload_manifest(dry_run: bool = False) -> int:
    """重新 dbt parse 生成 manifest.json 并上传 GCS（Cosmos DbtTaskGroup 依赖）。"""
    src = PROJECT_ROOT / "hicc_data_platform"
    dst = f"gs://{BUCKET}/data/hicc_data_platform"
    manifest = src / "target" / "manifest.json"

    if dry_run:
        print(f"    [DRY-RUN] dbt parse + gsutil cp {manifest} {dst}/target/manifest.json")
        return 0

    print("  [parse] 运行 dbt parse...")
    dbt = _which("dbt")
    if not dbt:
        print("  ❌ 找不到 dbt，请确认已安装", file=sys.stderr)
        return 1
    proc = subprocess.run(
        _wrap_windows_cmd([dbt, "parse", "--quiet"]), cwd=str(src),
        text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        print("  ❌ dbt parse 失败！请手动运行 cd hicc_data_platform && dbt parse 检查错误",
              file=sys.stderr)
        return 1
    print("  [parse] manifest.json 已重新生成")

    if run_gsutil(f"gsutil cp {manifest} {dst}/target/manifest.json") != 0:
        print("  ❌ manifest.json 上传失败", file=sys.stderr)
        return 1
    print("  [parse] manifest.json 已上传到 GCS")
    return 0


# ============================================================================
# 模块发布
# ============================================================================

def deploy_dags(dry_run: bool) -> int:
    print("[dags] 发布 DAG 文件...")
    src = DAGS_DIR
    dst = f"gs://{BUCKET}/dags"

    # 本地 glob 展开 .py（gsutil 对 Windows 反斜杠路径的通配符不友好）
    py_files = [str(p) for p in src.glob("*.py")]
    if py_files:
        run_gsutil(f"gsutil -m cp {' '.join(py_files)} {dst}/", dry_run)
    run_gsutil(f"gsutil -m rsync -r -d -x \"__pycache__/*\" {src / 'hicc_utils'}/ {dst}/hicc_utils/", dry_run)
    run_gsutil(f"gsutil -m rsync -r -d -x \"__pycache__/*\" {src / 'config'}/ {dst}/config/", dry_run)
    print("  [OK] DAG 文件已发布（含 hicc_utils/、config/）")
    return 0


def deploy_dbt(dry_run: bool) -> int:
    print("[dbt] 发布 dbt 工程...")
    src = PROJECT_ROOT / "hicc_data_platform"
    dst = f"gs://{BUCKET}/data/hicc_data_platform"
    manifest = src / "target" / "manifest.json"

    if dry_run:
        run_gsutil(f"gsutil -m rsync -r -d -x \"target/.*|logs/.*|dbt_packages/.*|\\.dbt/.*\" {src}/ {dst}/", dry_run)
        run_gsutil(f"gsutil cp {manifest} {dst}/target/manifest.json", dry_run)
        run_gsutil(f"gsutil -m rm {dst}/target/partial_parse.msgpack {dst}/target/graph.gpickle {dst}/target/run_results.json 2>nul || exit /b 0", dry_run)
        print("  [OK] dbt 工程已发布（含 manifest.json，Cosmos DbtTaskGroup 依赖）")
        return 0

    # 上传顺序：源代码 → manifest → 清理旧缓存（避免 Worker 读旧代码）
    print("  [upload] 上传 dbt 源代码...")
    if run_gsutil(f"gsutil -m rsync -r -d -x \"target/.*|logs/.*|dbt_packages/.*|\\.dbt/.*\" {src}/ {dst}/") != 0:
        return 1
    print("  [upload] 上传 manifest.json...")
    if run_gsutil(f"gsutil cp {manifest} {dst}/target/manifest.json") != 0:
        return 1
    print("  [clean] 清理 target/ 下的旧编译缓存...")
    run_gsutil(f"gsutil -m rm {dst}/target/partial_parse.msgpack {dst}/target/graph.gpickle {dst}/target/run_results.json 2>nul || exit /b 0")
    print("  [OK] ✅ 源代码 + manifest 已上传，旧缓存已清理")
    print("  [OK] dbt 工程已发布（含 manifest.json，Cosmos DbtTaskGroup 依赖）")
    return 0


def deploy_profiles(dry_run: bool) -> int:
    print("[profiles] 发布 dbt profiles.yml...")
    src = DEPLOY_DIR / "profiles_composer.yml"
    dst = f"gs://{BUCKET}/data/profiles.yml"
    run_gsutil(f"gsutil cp {src} {dst}", dry_run)
    print("  [OK] profiles.yml 已发布")
    return 0


def _rsync_dir(module: str, rel_dir: str, dry_run: bool) -> int:
    print(f"[{module}] 发布{module}模块脚本...")
    src = PROJECT_ROOT / rel_dir
    dst = f"gs://{BUCKET}/data/{module}"
    if not src.is_dir():
        print(f"  [SKIP] {module} 脚本目录不存在")
        return 0
    run_gsutil(f"gsutil -m rsync -r -d {src}/ {dst}/", dry_run)
    print(f"  [OK] {module} 脚本已发布")
    return 0


def deploy_monitor(dry_run: bool) -> int:
    return _rsync_dir("monitor", "airflow/data/monitor", dry_run)


def deploy_shipment(dry_run: bool) -> int:
    return _rsync_dir("shipment", "airflow/data/shipment_model", dry_run)


def deploy_feishu(dry_run: bool) -> int:
    return _rsync_dir("feishu", "airflow/data/feishu_sync", dry_run)


# ============================================================================
# 指定文件发布
# ============================================================================

def resolve_gcs_path(rel_path: str) -> str | None:
    """计算单个文件的 GCS 目标路径（与 deploy_all.sh 的 case 一一对应）。"""
    rel = rel_path.replace("\\", "/")
    if rel.startswith("airflow/dags/hicc_utils/"):
        return f"gs://{BUCKET}/dags/hicc_utils/{Path(rel).name}"
    if rel.startswith("airflow/dags/config/"):
        return f"gs://{BUCKET}/dags/config/{Path(rel).name}"
    if rel.startswith("airflow/dags/") and rel.endswith(".py"):
        return f"gs://{BUCKET}/dags/{Path(rel).name}"
    if rel.startswith("hicc_data_platform/"):
        rel_to_dbt = rel[len("hicc_data_platform/"):]
        return f"gs://{BUCKET}/data/hicc_data_platform/{rel_to_dbt}"
    if rel.startswith("airflow/data/monitor/"):
        return f"gs://{BUCKET}/data/monitor/{Path(rel).name}"
    if rel.startswith("airflow/data/shipment_model/"):
        return f"gs://{BUCKET}/data/shipment_model/{Path(rel).name}"
    if rel.startswith("airflow/data/feishu_sync/"):
        return f"gs://{BUCKET}/data/feishu_sync/{Path(rel).name}"
    if rel == "airflow/deploy/profiles_composer.yml":
        return f"gs://{BUCKET}/data/profiles.yml"
    print(f"  ⚠️ 无法识别文件归属模块: {rel_path}", file=sys.stderr)
    return None


def deploy_files_batch(files: list[str], dry_run: bool) -> int:
    """批量发布（按 GCS 目标目录分组，每组一次 gsutil -m cp）。"""
    if not files:
        return 0

    pairs: list[tuple[str, str]] = []  # (abs_path, gcs_path)
    failed = 0
    for rel_path in files:
        rel = rel_path.replace("\\", "/")
        abs_path = PROJECT_ROOT / rel
        if not abs_path.exists() or not abs_path.is_file():
            print(f"  ❌ 文件不存在: {rel_path}")
            failed += 1
            continue
        gcs_path = resolve_gcs_path(rel)
        if gcs_path is None:
            failed += 1
            continue
        pairs.append((str(abs_path), gcs_path))
        print(f"[file] {rel_path} → {gcs_path}")

    if not pairs:
        print("  ❌ 没有有效文件可发布")
        return 1

    # 按目标目录分组
    from collections import OrderedDict
    by_dir: "OrderedDict[str, list[str]]" = OrderedDict()
    for abs_path, gcs_path in pairs:
        gcs_dir = gcs_path.rsplit("/", 1)[0]
        by_dir.setdefault(gcs_dir, []).append(abs_path)

    for gcs_dir, srcs in by_dir.items():
        print(f"  [batch] → {gcs_dir}/")
        if run_gsutil(f"gsutil -m cp {' '.join(srcs)} {gcs_dir}/", dry_run) != 0:
            print(f"  ❌ 批量发布失败: {gcs_dir}", file=sys.stderr)
            failed += 1
        else:
            print("  [OK] 批量发布完成")
    return 1 if failed else 0


# ============================================================================
# 部署后文件校验（--verify：本地 MD5 vs GCS md5Hash）
# ============================================================================

_MD5_RE = re.compile(r"(?:md5|Hash \(md5\))[:\s]*([A-Za-z0-9+/=]{20,})")


def get_local_md5_base64(abs_path: Path) -> str:
    """计算本地文件 base64 编码的 MD5（与 GCS md5Hash 同格式）。"""
    h = hashlib.md5()
    with abs_path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return base64.b64encode(h.digest()).decode("ascii")


def get_gcs_md5_base64(gcs_path: str) -> str | None:
    """查询 GCS 对象的 md5Hash（base64）。失败返回 None。"""
    ensure_gsutil_auth()
    proc = subprocess.run(
        _wrap_windows_cmd([_find_gsutil(), "ls", "-L", gcs_path]),
        text=True, encoding="utf-8", errors="replace",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        print(f"    ⚠️  无法读取 GCS 对象: {gcs_path}", file=sys.stderr)
        return None
    m = _MD5_RE.search(proc.stdout)
    return m.group(1) if m else None


def verify_file_md5(abs_path: Path, gcs_path: str) -> bool:
    """校验单个文件：本地 MD5 与 GCS md5Hash 一致则 PASS。"""
    local = get_local_md5_base64(abs_path)
    remote = get_gcs_md5_base64(gcs_path)
    ok = remote is not None and local == remote
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {gcs_path}")
    if not ok:
        print(f"       本地 MD5: {local}")
        print(f"       GCS  MD5: {remote}")
    return ok


def verify_uploaded_files(files: list[str], has_dbt_source: bool,
                          dry_run: bool) -> int:
    """部署完成后校验本次发布的所有文件（--file 指定 + dbt 源文件时的 manifest.json）。

    Returns:
        0 全部一致；1 存在不一致或无法校验。
    """
    if dry_run:
        print("  [DRY-RUN] 跳过校验（未实际部署，无意义）")
        return 0

    targets: list[tuple[Path, str]] = []
    for rel_path in files:
        rel = rel_path.replace("\\", "/")
        gcs_path = resolve_gcs_path(rel)
        if gcs_path is None:
            continue
        targets.append((PROJECT_ROOT / rel, gcs_path))

    if has_dbt_source:
        manifest = PROJECT_ROOT / "hicc_data_platform" / "target" / "manifest.json"
        targets.append((
            manifest,
            f"gs://{BUCKET}/data/hicc_data_platform/target/manifest.json",
        ))

    if not targets:
        print("  ⚠️  没有可校验的文件", file=sys.stderr)
        return 1

    print(f"校验 {len(targets)} 个文件（本地 MD5 vs GCS md5Hash）...")
    results = [verify_file_md5(p, g) for p, g in targets]
    failed = sum(1 for ok in results if not ok)

    if failed:
        print(f"\n  ❌ {failed}/{len(targets)} 个文件不一致，请检查上传！")
        return 1
    print(f"\n  [OK] {len(targets)} 个文件均与本地一致 ✅")
    return 0


# ============================================================================
# 主流程
# ============================================================================

def main() -> None:
    # ════════════════════════════════════════════════════════════════════
    # 参数用法示例（PowerShell 直接运行，Windows 原生）
    # ════════════════════════════════════════════════════════════════════
    #   python airflow/deploy/deploy_all.py                          # 全量发布（所有模块）
    #   python airflow/deploy/deploy_all.py --module dags            # 只发布 DAG（含 hicc_utils/、config/）
    #   python airflow/deploy/deploy_all.py --module dags,dbt        # 发布 DAG + dbt 工程（逗号组合）
    #   python airflow/deploy/deploy_all.py --module dts             # 只同步 DTS 配置（不发布文件）
    #   python airflow/deploy/deploy_all.py --module dags --dry-run  # 预览，不实际执行
    #   python airflow/deploy/deploy_all.py --file airflow/dags/hicc_utils/dbt_tasks.py
    #                                # 只发布单个文件（--file 可多次使用，自动识别归属模块）
    #   python airflow/deploy/deploy_all.py --file airflow/dags/config/crawl_sources.yaml
    #                                # 发布 crawl_sources.yaml → 自动触发 DTS 同步 + 追加新快照
    #   python airflow/deploy/deploy_all.py --module dags --skip-dts # 紧急发布，跳过 DTS 变更
    #   python airflow/deploy/deploy_all.py --module dags --sync-variables
    #                                # 发布 + 同步 Airflow Variables（幂等）
    #   组合示例：先预览再真发
    #     python airflow/deploy/deploy_all.py --module dags --dry-run      # 1. 预览
    #     python airflow/deploy/deploy_all.py --module dags                 # 2. 确认后真发
    # ════════════════════════════════════════════════════════════════════

    parser = argparse.ArgumentParser(
        description="HICCPET 数仓 Airflow 部署（Python 版，Windows 原生可运行）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    # --module：要发布的模块，逗号分隔。可选: dags,dbt,profiles,monitor,shipment,feishu,dts,all
    #   all = 全量（默认，不带任何参数时）；dts 是"只同步 DTS 不发布文件"的特殊模块
    parser.add_argument("--module", default="",
                        help="指定要发布的模块（逗号分隔）: dags,dbt,profiles,monitor,shipment,feishu,dts,all")
    # --file：指定要发布的单个文件（相对项目根目录），可重复使用
    #   发布 crawl_sources.yaml 或 dbt 源文件时，会自动触发 DTS 同步 / dbt parse
    parser.add_argument("--file", action="append", default=[],
                        help="指定要发布的文件（相对项目根目录，可多次使用）")
    # --dry-run：只打印将要执行的操作，不实际调用 gsutil / 不部署
    parser.add_argument("--dry-run", action="store_true",
                        help="只预览将要发布的文件，不实际执行")
    # --sync-variables：发布完成后同步 Airflow Variables（幂等，只同步 Variables 跳过 Connections/Pools）
    parser.add_argument("--sync-variables", action="store_true",
                        help="部署完成后同步 Airflow Variables（幂等）")
    # --skip-dts：跳过自动 DTS 变更（紧急发布用，仅确认 crawl_sources.yaml 无变更时使用）
    parser.add_argument("--skip-dts", action="store_true",
                        help="跳过自动 DTS 变更（紧急发布时用）")
    # --verify：部署完成后校验 GCS 文件与本地内容一致（MD5 对比）
    parser.add_argument("--verify", action="store_true",
                        help="部署完成后校验 GCS 文件与本地 MD5 一致（--file/dbt 源文件场景）")
    args = parser.parse_args()

    modules = args.module
    files = args.file
    dry_run = args.dry_run
    skip_dts = args.skip_dts

    if not modules and not files:
        modules = "all"

    # preflight
    ensure_gsutil_auth()
    preflight_auth()
    preflight_bucket()

    def should_deploy_module(m: str) -> bool:
        if modules == "all":
            return True
        return m in [x.strip() for x in modules.split(",")]

    print("=" * 60)
    print("HICCPET 数仓 Airflow 部署")
    print("=" * 60)
    print(f"GCS Bucket: gs://{BUCKET}")
    print(f"项目根目录: {PROJECT_ROOT}")
    if dry_run:
        print("⚠️  DRY-RUN 模式：只预览不实际执行")
    print()

    # ── 发布指定文件 ──
    if files:
        print("═" * 60)
        print(f"发布指定文件 ({len(files)} 个)")
        print("═" * 60)

        has_dbt_source = any(is_dbt_source_file(f) for f in files)
        has_crawl_sources = any(is_crawl_sources_file(f.replace("\\", "/"))
                                for f in files)

        # crawl_sources.yaml 变更 → 先同步 DTS
        if has_crawl_sources and not skip_dts:
            print("─" * 60)
            print("检测到 crawl_sources.yaml 变更，触发 DTS transfer configs 同步")
            print("─" * 60)
            if sync_dts_configs(dry_run) != 0:
                print("❌ DTS 同步失败，部署中止", file=sys.stderr)
                sys.exit(1)

            # 追加新生成的 dts_transfer_configs.yaml 到上传列表
            if DTS_CONFIGS_YAML_REL not in files:
                files.append(DTS_CONFIGS_YAML_REL)
                print(f"  [auto] 追加上传 {DTS_CONFIGS_YAML_REL}（DTS 同步后生成的新快照）")

        deploy_files_batch(files, dry_run)

        if has_dbt_source:
            print("─" * 60)
            print("检测到 dbt 源文件变更，触发 dbt parse + 上传 manifest.json")
            print("─" * 60)
            if parse_dbt_and_upload_manifest(dry_run) != 0:
                print("❌ dbt parse 或 manifest 上传失败，部署中止", file=sys.stderr)
                sys.exit(1)

        # 部署后文件校验（--verify）
        if args.verify:
            print("─" * 60)
            print("部署后文件校验（--verify）")
            print("─" * 60)
            if verify_uploaded_files(files, has_dbt_source, dry_run) != 0:
                print("❌ 文件校验未通过，请检查 GCS 上传结果", file=sys.stderr)
                sys.exit(1)
        print()

    # ── 发布指定模块 ──
    if modules:
        print("═" * 60)
        print(f"发布模块: {modules}")
        print("═" * 60)

        # dts 独立模块：单独同步 DTS（不发布文件）
        if should_deploy_module("dts") and not should_deploy_module("dags"):
            if sync_dts_configs(dry_run) != 0:
                print("❌ DTS 同步失败，部署中止", file=sys.stderr)
                sys.exit(1)
            print()

        # dags 模块：先同步 DTS 再发布
        if should_deploy_module("dags"):
            if not skip_dts:
                print("─" * 60)
                print("dags 模块：发布前先触发 DTS 同步（避免上传过期的 dts_transfer_configs.yaml）")
                print("─" * 60)
                if sync_dts_configs(dry_run) != 0:
                    print("❌ DTS 同步失败，部署中止", file=sys.stderr)
                    sys.exit(1)
                print()
            else:
                print("⚠️  已用 --skip-dts 跳过 DTS 同步，将直接上传现有 dts_transfer_configs.yaml",
                      file=sys.stderr)
                print("    仅在确认 crawl_sources.yaml 无变更时使用此选项", file=sys.stderr)
            deploy_dags(dry_run)
            print()

        for m in MODULE_ORDER:
            if m == "dags":
                continue
            if should_deploy_module(m):
                fn = {"dbt": deploy_dbt, "profiles": deploy_profiles,
                      "monitor": deploy_monitor, "shipment": deploy_shipment,
                      "feishu": deploy_feishu}[m]
                fn(dry_run)
                print()

    # ── 同步 Airflow Variables（可选）──
    if args.sync_variables:
        print("═" * 60)
        print("同步 Airflow Variables（--sync-variables）")
        print("═" * 60)
        script = DEPLOY_DIR / "setup_airflow_connections.py"
        if dry_run:
            print(f"  [DRY-RUN] python {script} --skip-connections --skip-pools")
        else:
            run([
                sys.executable, str(script),
                "--env", os.environ.get("COMPOSER_ENV", "hicc"),
                "--location", os.environ.get("COMPOSER_LOCATION", "asia-southeast1"),
                "--skip-connections", "--skip-pools",
            ])
        print()

    print("=" * 60)
    print("部署完成")
    print("=" * 60)
    print()
    if dry_run:
        print("💡 这是 dry-run 预览，去掉 --dry-run 参数实际执行")
    else:
        print("下一步：")
        print("  1. 等待 Composer 同步（约 2-5 分钟）")
        print("  2. 在 Airflow UI 检查 DAG 是否加载成功")
        print("  3. 如有需要，Unpause 对应的 DAG")
    print()


if __name__ == "__main__":
    main()
