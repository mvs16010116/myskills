# -*- coding: utf-8 -*-
"""
GCP Dataform 代码拉取 / 推送 / 编译校验 通用命令行工具（纯 REST API，不依赖 Git/GitHub）。

用法:
  # 拉取整个工作区到本地
  python dataform_cli.py pull --project <PROJECT> --location <LOC> --repo <REPO_ID> --workspace <WS> --out <本地目录>

  # 推送单个文件到工作区并提交
  python dataform_cli.py push --project <PROJECT> --location <LOC> --repo <REPO_ID> --workspace <WS> \
      --file "<本地路径>=<远端路径>" [--message "<提交说明>"]

  # 推送本地目录下所有文件到工作区并提交（远端路径 = 相对 --dir 的路径）
  python dataform_cli.py push --project <PROJECT> --location <LOC> --repo <REPO_ID> --workspace <WS> \
      --dir <本地目录> [--message "<提交说明>"]

  # 创建编译结果并校验无错误
  python dataform_cli.py compile --project <PROJECT> --location <LOC> --repo <REPO_ID> --workspace <WS>

  # 打印仓库提交历史
  python dataform_cli.py log --project <PROJECT> --location <LOC> --repo <REPO_ID> --workspace <WS> [--limit 20]

说明:
  - 认证走 gcloud application-default / access token，无需额外凭据
  - repo 传 Dataform 仓库 ID 或名称均可
"""
import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://dataform.googleapis.com/v1beta1"

# 拉取时无需保留的构建产物目录
SKIP_DIRS = {"node_modules", ".git", ".dataform"}


def find_gcloud():
    """定位 gcloud 可执行文件（Windows 下为 gcloud.cmd）。"""
    for name in ("gcloud", "gcloud.cmd", "gcloud.bat"):
        path = shutil.which(name)
        if path:
            return path
    fallbacks = [
        os.path.expanduser(r"~\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd"),
        r"C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd",
    ]
    for p in fallbacks:
        if os.path.exists(p):
            return p
    raise SystemExit("未找到 gcloud，请先安装 Google Cloud SDK 并完成认证")


def get_token(gcloud):
    """通过 gcloud 获取访问令牌。"""
    return subprocess.check_output([gcloud, "auth", "print-access-token"], text=True).strip()


class Dataform:
    """Dataform REST API 封装。"""

    def __init__(self, project, location, repo, workspace, token):
        repo_url = f"{BASE}/projects/{project}/locations/{location}/repositories/{repo}"
        self.ws_url = f"{repo_url}/workspaces/{workspace}"
        # API 要求相对路径（不含 BASE 前缀），如 projects/<project>/locations/<loc>/repositories/<repo>/workspaces/<ws>
        self.ws_path = f"projects/{project}/locations/{location}/repositories/{repo}/workspaces/{workspace}"
        self.url = self.ws_url
        self.repo_url = repo_url
        self.token = token
        self._headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    def _call(self, action, body=None):
        url = f"{self.url}:{action}"
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method="POST", headers=self._headers)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:1000]
            raise SystemExit(f"[API 错误] {action} HTTP {e.code}: {detail}")

    def _call_get(self, action, params):
        url = f"{self.url}:{action}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers=self._headers)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:1000]
            raise SystemExit(f"[API 错误] {action} HTTP {e.code}: {detail}")

    # ---------- 拉取 ----------
    def list_dir(self, path):
        """列出工作区某目录内容（path 为空表示根目录）。"""
        return self._call_get("queryDirectoryContents", {"path": path} if path else None).get(
            "directoryEntries", []
        )

    def read_file(self, path):
        """读取工作区某文件内容；空文件不返回 fileContents，视为空内容。"""
        resp = self._call_get("readFile", {"path": path})
        contents = resp.get("fileContents", "")
        return base64.b64decode(contents).decode("utf-8", errors="replace") if contents else ""

    def pull(self, out_dir):
        """递归拉取整个工作区到本地目录。"""
        os.makedirs(out_dir, exist_ok=True)
        count = self._walk("", out_dir)
        print(f"完成，共拉取 {count} 个文件到 {out_dir}")

    def _walk(self, path, out_dir):
        count = 0
        for entry in self.list_dir(path):
            if "file" in entry:
                fpath = entry["file"].lstrip("/")
                local = os.path.join(out_dir, fpath.replace("/", os.sep))
                os.makedirs(os.path.dirname(local), exist_ok=True)
                try:
                    with open(local, "w", encoding="utf-8") as f:
                        f.write(self.read_file(fpath))
                    print(f"  [文件] {fpath}")
                    count += 1
                except Exception as e:
                    print(f"  [跳过] {fpath}: {e}")
            elif "directory" in entry:
                dpath = entry["directory"]
                if dpath.split("/")[0] in SKIP_DIRS:
                    print(f"  [跳过目录] {dpath}")
                    continue
                count += self._walk(dpath, out_dir)
        return count

    # ---------- 推送 ----------
    def write_file(self, remote_path, local_path):
        """将本地文件写入工作区（contents 为 base64 编码）。"""
        with open(local_path, "rb") as f:
            contents = base64.b64encode(f.read()).decode("ascii")
        self._call("writeFile", {"path": remote_path, "contents": contents})
        print(f"  [写入] {remote_path}")

    def commit(self, message, author):
        """提交工作区改动。"""
        body = {
            "author": {"name": author, "emailAddress": author},
            "commitMessage": message,
        }
        self._call("commit", body)
        print(f"  已提交: {message}")

    # ---------- 提交历史 ----------
    def log(self, limit=20, all_commits=False):
        """拉取仓库提交历史（fetchHistory 挂在 repository 层级）。

        all_commits=True 时自动翻页直至取完所有提交；否则仅取 limit 条。
        """
        commits = []
        page_token = None
        while True:
            params = {"pageSize": 100}
            if page_token:
                params["pageToken"] = page_token
            url = f"{self.repo_url}:fetchHistory?" + urllib.parse.urlencode(params)
            req = urllib.request.Request(url, headers=self._headers)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            commits.extend(data.get("commits", []))
            next_token = data.get("nextPageToken")
            if not all_commits:
                return commits[:limit]
            if not next_token or len(commits) >= limit:
                break
            page_token = next_token
        return commits

    # ---------- 编译校验 ----------
    def compile(self):
        """创建编译结果并返回错误列表（空列表表示编译通过）。"""
        # 编译结果挂在 repository 层级，body 需传相对 workspace 路径
        url = f"{self.repo_url}/compilationResults"
        data = json.dumps({"workspace": self.ws_path}).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST", headers=self._headers)
        with urllib.request.urlopen(req) as resp:
            name = json.loads(resp.read().decode("utf-8"))["name"]
        # name 为完整资源路径，如 projects/.../compilationResults/<id>
        get_req = urllib.request.Request(f"{BASE}/{name}", headers=self._headers)
        with urllib.request.urlopen(get_req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        return result.get("errors", [])


def push_file_map(args):
    """解析 --file '本地=远端' 或 --dir 目录映射。"""
    files = []
    if args.file:
        for item in args.file:
            local, remote = item.split("=", 1)
            files.append((os.path.abspath(local), remote))
    if args.dir:
        root = os.path.abspath(args.dir)
        for cur, _, names in os.walk(root):
            for name in names:
                local = os.path.join(cur, name)
                rel = os.path.relpath(local, root).replace(os.sep, "/")
                files.append((local, rel))
    if not files:
        raise SystemExit("请通过 --file 或 --dir 指定要推送的文件")
    return files


def main():
    parser = argparse.ArgumentParser(description="GCP Dataform 代码拉取/推送/编译校验")
    sub = parser.add_subparsers(dest="command", required=True)

    p_pull = sub.add_parser("pull", help="拉取整个工作区到本地")
    p_pull.add_argument("--project", required=True)
    p_pull.add_argument("--location", required=True)
    p_pull.add_argument("--repo", required=True)
    p_pull.add_argument("--workspace", required=True)
    p_pull.add_argument("--out", required=True)

    p_push = sub.add_parser("push", help="推送文件到工作区并提交")
    p_push.add_argument("--project", required=True)
    p_push.add_argument("--location", required=True)
    p_push.add_argument("--repo", required=True)
    p_push.add_argument("--workspace", required=True)
    p_push.add_argument("--file", action="append", help="本地路径=远端路径")
    p_push.add_argument("--dir", help="本地目录，远端路径为相对该目录的路径")
    p_push.add_argument("--message", default="sync dataform workspace")
    p_push.add_argument("--author", default=None, help="提交人邮箱，默认取 gcloud 账号")

    p_compile = sub.add_parser("compile", help="创建编译结果并校验")
    p_compile.add_argument("--project", required=True)
    p_compile.add_argument("--location", required=True)
    p_compile.add_argument("--repo", required=True)
    p_compile.add_argument("--workspace", required=True)

    p_log = sub.add_parser("log", help="打印仓库提交历史")
    p_log.add_argument("--project", required=True)
    p_log.add_argument("--location", required=True)
    p_log.add_argument("--repo", required=True)
    p_log.add_argument("--workspace", required=True, help="fetchHistory 不限工作区，传任意已存在的工作区即可")
    p_log.add_argument("--limit", type=int, default=20, help="最多显示条数，默认 20")
    p_log.add_argument("--all", action="store_true", help="打印全部提交历史（自动翻页）")

    args = parser.parse_args()

    gcloud = find_gcloud()
    token = get_token(gcloud)
    df = Dataform(args.project, args.location, args.repo, args.workspace, token)

    if args.command == "pull":
        df.pull(os.path.abspath(args.out))
    elif args.command == "push":
        if not args.author:
            args.author = subprocess.check_output(
                [gcloud, "config", "get-value", "account"], text=True
            ).strip()
        for local, remote in push_file_map(args):
            df.write_file(remote, local)
        df.commit(args.message, args.author)
    elif args.command == "compile":
        errors = df.compile()
        if errors:
            for e in errors:
                print("  [编译错误]", e.get("message"))
            raise SystemExit(f"编译失败，共 {len(errors)} 个错误")
        print("编译通过，0 错误")
    elif args.command == "log":
        commits = df.log(args.limit, args.all)
        if not commits:
            print("暂无提交记录")
            return
        print(f"仓库最近 {len(commits)} 条提交:")
        for i, c in enumerate(commits, 1):
            author = c.get("author", {})
            email = author.get("emailAddress", "-")
            msg = c.get("commitMessage", "")
            commit_time = (c.get("commitTime") or "")[:19].replace("T", " ")
            print(f"  {i}. {msg}")
            print(f"     提交人: {email} | 提交时间: {commit_time}")


if __name__ == "__main__":
    main()
