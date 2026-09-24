---
name: "windows-sh部署dbt"
description: "部署 HICCPET 数仓 Airflow（Windows 原生 Python 版 deploy_all.py，位于本 skill 目录）。当用户要在 Windows 部署 dags/dbt/DTS、或原 deploy_all.sh 报 pipefail/CRLF/匿名401 等错误时调用。"
---

# HICCPET 数仓 Airflow 部署（Windows 原生 Python）

## 一句话结论

- **Windows 用户**：用 Python 版 `deploy_all.py`（就在本 skill 目录），Windows 原生直接跑
- **Mac/Linux 用户**：继续用 bash 版 `airflow/deploy/deploy_all.sh`（已保留，团队其他人仍在用）
- 两版功能完全一致，**共存不冲突**

## 为什么 Windows 用 Python 版

bash 版 `airflow/deploy/deploy_all.sh`（1004 行）是 Mac 环境产物，在 Windows 上有一堆兼容性坑：
- PowerShell 裸 `bash` 指向旧版 WSL sh，不支持 `set -o pipefail`
- msys bash 需 `MSYSTEM` 环境变量，非 tty 输出会被管道吞掉
- `command -v timeout` 命中 `C:\Windows\System32\timeout.exe`（语法是 `TIMEOUT /T`）

**不是所有人都有 msys2**，所以 Windows 部署统一走 Python：`python deploy_all.py` 直接调 gsutil/dbt/python，天然跨平台。bash 版继续保留给 Mac/Linux 用户，不要删除。

## 脚本位置与运行方式

```powershell
# 脚本在本 skill 目录，Python 原生运行（任意 cwd 均可，自动探测项目根）
python .trae/skills/windows-sh部署dbt/deploy_all.py --module dags --dry-run
```

常用参数（完整示例见脚本内 `main()` 顶部注释）：

| 命令 | 说明 |
|------|------|
| `python deploy_all.py` | 全量发布（所有模块） |
| `python deploy_all.py --module dags` | 只发布 DAG（含 hicc_utils/、config/） |
| `python deploy_all.py --module dags,dbt` | 组合模块 |
| `python deploy_all.py --module dts` | 只同步 DTS（不发布文件） |
| `python deploy_all.py --dry-run` | 只预览，不实际执行（务必先跑） |
| `python deploy_all.py --file 某文件` | 单文件发布（自动识别归属模块） |
| `python deploy_all.py --file airflow/dags/config/crawl_sources.yaml` | 发 crawl_sources.yaml → 自动 DTS 同步 |
| `python deploy_all.py --module dags --skip-dts` | 紧急发布，跳过 DTS 变更 |
| `python deploy_all.py --file xxx` | 单文件发布（部署后自动 MD5 校验） |

## 安全执行模板（PowerShell）

```powershell
# 1. 先 dry-run 预览（不会真部署）
python .trae/skills/windows-sh部署dbt/deploy_all.py --module dags --dry-run

# 2. 确认输出无误后，去掉 --dry-run 正式执行
python .trae/skills/windows-sh部署dbt/deploy_all.py --module dags
```

### 认证（脚本自动处理，无需手动）

- **gsutil**：脚本自动检测服务账号 key `hiccpet-481303-f7f2e4edc9ac.json`，未设 `BOTO_CONFIG` 时自动生成 boto 配置注入（解决匿名 401）。也可手动：`$env:BOTO_CONFIG="$env:TEMP\hicc_gs_boto.cfg"`
- **gcloud ADC**：需已执行过 `gcloud auth application-default login`（BigQuery 客户端已配置）
- **DTS 密码**：仅在 `crawl_sources.yaml` 有变更且发布 dags 时才需要。优先 `$env:DTS_MYSQL_PASSWORD='xxx'`，否则交互输入

## 历史踩坑（已由 Python 版解决，仅供参考）

| 坑 | sh 版表现 | Python 版处理 |
|----|-----------|---------------|
| pipefail 不支持 | `bash deploy_all.sh` 报 `set: pipefail: invalid option name` | 无需 bash，无此问题 |
| msys 输出被吞 | Start-Process 重定向才可见 | subprocess 直接透传 UTF-8 |
| timeout 冲突 | 命中 Windows `timeout.exe` | Python `subprocess.run(timeout=300)` |
| 匿名 401 | 需手动配 boto | `ensure_gsutil_auth()` 自动注入 |
| CRLF 乱码 | 需 `sed -i 's/\r$//'` | Python 文件读写不受影响 |

## 部署后文件校验（默认自动执行，必须通过）

**所有部署（`--file` 或 `--module`）完成后，脚本自动逐文件对比本地与 GCS 的 MD5**，
保证文件确实部署成功，避免"上传成功但内容不对 / 未同步 / 传错版本"的隐患。
任一文件 FAIL 立即以**非零退出码**中止部署。

- 校验方式：本地文件 Python 计算 base64 MD5，GCS 对象读取 `md5Hash` 对比
- `--file` 场景：校验本次发布的所有文件；含 dbt 源文件时自动追加校验 `manifest.json`
- `--module` 场景：校验整个模块目录（dbt 模块为全部源文件 + manifest.json）
- `--dry-run` 时不校验（未实际部署，无意义）
- `--verify` 参数已默认开启，保留仅为向后兼容，无需手动加

```powershell
# 部署（无论哪种方式，最后都会自动输出逐文件 [PASS]/[FAIL] 校验结果）
python .trae/skills/windows-sh部署dbt/deploy_all.py --module dbt

# 输出示例（全部 PASS 才算部署成功）
#   [OK] 182 个文件均与 GCS 一致 ✅
#   [PASS] gs://.../data/hicc_data_platform/target/manifest.json
```

### 单独校验已部署文件（不重新部署）

```powershell
# 用 gcloud storage（gcloud ADC 认证）
gcloud storage cp gs://asia-southeast1-hicc-e1a70e20-bucket/data/hicc_data_platform/models/08_scm/dws/dws_scm_shipment_abnormal_data_di.sql test\tmp_check.sql
(Get-FileHash test\tmp_check.sql -Algorithm MD5).Hash   # 与本地 Get-FileHash 结果对比
```

## 部署后验证

```powershell
# 1. 确认 gsutil 可访问 bucket
gsutil ls gs://asia-southeast1-hicc-e1a70e20-bucket

# 2. 部署时已自动执行 MD5 校验，确认最后输出 [OK] 全部 PASS 即可

# 3. 等待 Composer 同步（约 2-5 分钟）
# 4. 在 Airflow UI 检查 DAG 是否加载成功；如有需要 Unpause 对应 DAG
```
