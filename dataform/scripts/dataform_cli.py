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
        """创建编译结果并返回错误列表（空列表表示编译通过）。

        注意：编译错误字段为 compilationErrors（不是 errors）。
        """
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
        return result.get("compilationErrors", [])

    def create_compilation(self):
        """创建编译结果并返回完整资源路径。"""
        url = f"{self.repo_url}/compilationResults"
        data = json.dumps({"workspace": self.ws_path}).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST", headers=self._headers)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))["name"]

    def query_compilation_actions(self, compilation):
        """查询编译结果的所有 actions，返回 [{target, filePath, compiledQuery|kind}]。"""
        url = f"{BASE}/{compilation}:query"
        req = urllib.request.Request(url, method="GET", headers=self._headers)
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:1500]
            raise SystemExit(f"[API 错误] query_compilation_actions HTTP {e.code}: {detail}")
        actions = []
        for a in data.get("compilationResultActions", []):
            entry = {
                "target": a.get("target", {}),
                "filePath": a.get("filePath", ""),
            }
            if "table" in a:
                entry["kind"] = a["table"].get("relationType", "table")
                entry["compiledQuery"] = a["table"].get("compiledQuery", "")
            elif "operations" in a:
                entry["kind"] = "operations"
                entry["compiledQuery"] = ""
            elif "notebook" in a:
                entry["kind"] = "notebook"
                entry["compiledQuery"] = ""
            actions.append(entry)
        return actions

    # ---------- Release Config ----------
    def list_release_configs(self):
        url = f"{self.repo_url}/releaseConfigs"
        req = urllib.request.Request(url, headers=self._headers)
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8")).get("releaseConfigs", [])

    def create_release_config(self, rc_id, compilation_name=None):
        """创建 release config。

        说明：ReleaseConfig 资源没有 workspace 字段（gitCommitish 为 Git 托管仓库专用）。
        对于内部托管仓库，只能通过 releaseCompilationResult 绑定已发布的编译结果。
        compilation_name 非空时配置 releaseCompilationResult 指向该编译结果。
        """
        url = f"{self.repo_url}/releaseConfigs?releaseConfigId={rc_id}"
        body = {}
        if compilation_name:
            body["releaseCompilationResult"] = compilation_name
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST", headers=self._headers)
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:1500]
            raise SystemExit(f"[API 错误] create_release_config HTTP {e.code}: {detail}")

    # ---------- Workflow Invocation ----------
    def invoke(self, compilation, service_account=None):
        """创建 workflow invocation 并等待完成，返回最终状态。

        service_account: 仓库启用 strict act-as checks 时必须指定，
        否则 API 返回 400 "Service account must be set..."。
        """
        url = f"{self.repo_url}/workflowInvocations"
        body = {"compilationResult": compilation}
        if service_account:
            body["invocationConfig"] = {"serviceAccount": service_account}
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST", headers=self._headers)
        try:
            with urllib.request.urlopen(req) as resp:
                name = json.loads(resp.read().decode("utf-8"))["name"]
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:1500]
            raise SystemExit(f"[API 错误] create workflow_invocation HTTP {e.code}: {detail}")
        import time
        state = None
        while True:
            time.sleep(3)
            get_req = urllib.request.Request(f"{BASE}/{name}", headers=self._headers)
            with urllib.request.urlopen(get_req) as resp:
                info = json.loads(resp.read().decode("utf-8"))
            state = info.get("state")
            print(f"[invoke] {state} ...", flush=True)
            if state in ("SUCCEEDED", "FAILED", "CANCELLED"):
                break
        return name, state, info


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

    p_rc = sub.add_parser("release-config", help="创建/列出 release config")
    p_rc.add_argument("--project", required=True)
    p_rc.add_argument("--location", required=True)
    p_rc.add_argument("--repo", required=True)
    p_rc.add_argument("--workspace", required=True)
    p_rc.add_argument("action", choices=["create", "list"], help="create=绑定当前工作区, list=列出已有")
    p_rc.add_argument("--id", default="default", help="release config ID，默认 default")
    p_rc.add_argument("--compilation", default=None, help="由该编译结果驱动的 releaseCompilationResult（完整资源路径）")

    p_inspect = sub.add_parser("inspect", help="创建编译结果并展示各 action 的目标表与生成 SQL")
    p_inspect.add_argument("--project", required=True)
    p_inspect.add_argument("--location", required=True)
    p_inspect.add_argument("--repo", required=True)
    p_inspect.add_argument("--workspace", required=True)
    p_inspect.add_argument("--compilation", default=None, help="使用已有编译结果（完整资源路径），缺省自动创建")
    p_inspect.add_argument("--sql", action="store_true", help="展示生成 SQL 前若干行")
    p_inspect.add_argument("--sql-lines", type=int, default=12, help="每个 action 展示 SQL 行数，默认 12")
    p_inspect.add_argument("--target", action="append", default=None, help="仅展示匹配的 target（可多次），如 dwd/dwd_inbound_shipment_info")

    p_invoke = sub.add_parser("invoke", help="创建 workflow invocation 执行编译结果并等待完成")
    p_invoke.add_argument("--project", required=True)
    p_invoke.add_argument("--location", required=True)
    p_invoke.add_argument("--repo", required=True)
    p_invoke.add_argument("--workspace", required=True)
    p_invoke.add_argument("--compilation", default=None, help="使用已有编译结果（完整资源路径），缺省自动创建")
    p_invoke.add_argument("--service-account", default=None,
                          help="strict act-as checks 模式下必须指定运行用 service account")

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
    elif args.command == "release-config":
        if args.action == "list":
            for rc in df.list_release_configs():
                name = rc.get("name", "")
                ws = rc.get("workspace", "-")
                rc_comp = (rc.get("releaseCompilationResult") or {}).get("compilationResult", "-")
                print(f"  {name}")
                print(f"     workspace: {ws}")
                print(f"     compilationResult: {rc_comp}")
        else:
            rc = df.create_release_config(args.id, args.compilation)
            print(f"已创建 release config: {rc.get('name')}")
    elif args.command == "inspect":
        compilation = args.compilation or df.create_compilation()
        print(f"编译结果: {compilation}")
        actions = df.query_compilation_actions(compilation)
        print(f"共 {len(actions)} 个 action:")
        for a in actions:
            tgt = a.get("target", {})
            schema = tgt.get("schema", "-")
            name = tgt.get("name", "-")
            kind = a.get("kind", "?")
            line = f"  [{kind}] {schema}.{name}"
            if a.get("filePath"):
                line += f"  <- {a['filePath']}"
            print(line)
            if args.sql and a.get("compiledQuery"):
                q = a["compiledQuery"]
                lines = [ln for ln in q.splitlines() if ln.strip()]
                preview = "\n".join(lines[: args.sql_lines])
                print(preview)
                print("  ...")
            elif args.sql and not a.get("compiledQuery"):
                print("    (operations/notebook，无 compiledQuery)")
    elif args.command == "invoke":
        compilation = args.compilation or df.create_compilation()
        print(f"使用编译结果: {compilation}")
        print("创建 workflow invocation 并等待完成...")
        name, state, info = df.invoke(compilation, args.service_account)
        print(f"结果: {name}")
        print(f"状态: {state}")
        if state != "SUCCEEDED":
            failure = info.get("failure")
            if failure:
                print("失败原因:", json.dumps(failure, ensure_ascii=False)[:2000])


if __name__ == "__main__":
    main()
