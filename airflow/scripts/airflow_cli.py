# -*- coding: utf-8 -*-
"""Airflow (Cloud Composer) 查询 CLI —— 通过 gcloud composer environments run 执行 airflow 命令。

用法：
  python airflow_cli.py list-envs --project <PROJECT> [--location <LOC>]
  python airflow_cli.py dags list --env <ENV> [--project <PROJECT>] [--location <LOC>]
  python airflow_cli.py dags details --env <ENV> --dag <DAG_ID>
  python airflow_cli.py dags list-runs --env <ENV> --dag <DAG_ID> [--start-date YYYY-MM-DD] [--end-date YYYY-MM-DD] [--state success|failed]
  python airflow_cli.py tasks list --env <ENV> --dag <DAG_ID> [--summary]
  python airflow_cli.py tasks test --env <ENV> --dag <DAG_ID> --task <TASK_ID> --date YYYY-MM-DD [--tries N]
"""
import argparse
import os
import shutil
import subprocess
import sys
from collections import Counter

# 默认值：hiccpet-481303 / asia-southeast1 / hicc（Cloud Composer 环境名）
DEFAULT_PROJECT = "hiccpet-481303"
DEFAULT_LOCATION = "asia-southeast1"
DEFAULT_ENV = "hicc"

# 全局选项：可在命令行的任意位置书写（脚本解析前会自动归位到子命令之前）
GLOBAL_OPTS = ("--env", "--project", "--location")


def _normalize_argv(argv):
    """把全局选项（--env/--project/--location）及其值提前到 argv 最前面。

    argparse 嵌套子解析器只识别定义在当前层级的选项：
    - --env 定义在 dags/tasks 层，放在孙级子命令（list/details/test）之后会报
      "unrecognized arguments: --env xxx"；
    - --project/--location 定义在根层，放在子命令之后同样不识别。

    本函数在 parse 前把这三个全局选项统一移到最前面，保证任意书写位置都能正确解析，
    无需用户记忆 --env 该放在 tasks 前还是后。
    """
    head, tail = [], []
    i, n = 0, len(argv)
    while i < n:
        arg = argv[i]
        if arg in GLOBAL_OPTS:
            head.append(arg)
            # 选项值（非 - 开头）一并前移
            if i + 1 < n and not argv[i + 1].startswith("-"):
                head.append(argv[i + 1])
                i += 2
            else:
                i += 1
        else:
            tail.append(arg)
            i += 1
    return head + tail


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


GCLOUD = find_gcloud()


def run_gcloud(args_list):
    """执行 gcloud 命令，返回 stdout。"""
    proc = subprocess.run([GCLOUD] + args_list, capture_output=True, text=True, encoding='utf-8')
    if proc.returncode != 0:
        print(proc.stdout, file=sys.stderr)
        print(proc.stderr, file=sys.stderr)
        sys.exit(proc.returncode)
    return proc.stdout


def gcloud_composer_run(env, project, location, subcommand, nested, cmd_args):
    """在 Composer 环境中执行 airflow 子命令。

    gcloud 语法要求 SUBCOMMAND 作为位置参数（`--` 之前），CMD_ARGS 放在 `--` 之后：
      run <ENV> --location <LOC> --project <PROJ> <subcommand> [<nested>] [-- <cmd_args>...]
    """
    cmd = [
        "composer", "environments", "run", env,
        "--location", location, "--project", project,
        subcommand,
    ]
    if nested:
        cmd.append(nested)
    if cmd_args:
        cmd += ["--"] + cmd_args
    return run_gcloud(cmd)


def cmd_list_envs(args):
    cmd = ["composer", "environments", "list",
           "--locations", args.location, "--project", args.project]
    print(run_gcloud(cmd))


def cmd_dags_list(args):
    out = gcloud_composer_run(args.env, args.project, args.location,
                              "dags", "list", [])
    print(out)


def cmd_dags_details(args):
    out = gcloud_composer_run(args.env, args.project, args.location,
                              "dags", "details", [args.dag])
    print(out)


def cmd_dags_list_runs(args):
    cmd_args = ["-d", args.dag]
    if args.start_date:
        cmd_args += ["-s", args.start_date]
    if args.end_date:
        cmd_args += ["-e", args.end_date]
    if args.state:
        cmd_args += ["--state", args.state]
    out = gcloud_composer_run(args.env, args.project, args.location,
                              "dags", "list-runs", cmd_args)
    print(out)


def cmd_tasks_list(args):
    """列出 DAG 的所有任务；--summary 时按前缀分组统计。"""
    out = gcloud_composer_run(args.env, args.project, args.location,
                              "tasks", "list", [args.dag])
    # 去掉 gcloud 输出的干扰行
    lines = [l.strip() for l in out.splitlines()
             if l.strip() and not l.startswith(("Executing", "Command has been started", "Use ctrl-c"))]
    if not args.summary:
        print("\n".join(lines))
        print(f"\n任务总数: {len(lines)}")
        return
    counter = Counter()
    for line in lines:
        parts = line.split(".")
        if len(parts) >= 3:
            counter[".".join(parts[:2])] += 1   # collect_layer.tg_amazon
        elif len(parts) == 2:
            counter[parts[0]] += 1              # start / end
        else:
            counter[line] += 1
    print(f"任务总数: {len(lines)}\n")
    for key in sorted(counter):
        print(f"{key:<42} {counter[key]}")


def cmd_tasks_test(args):
    """手动执行 DAG 中的单个任务（airflow tasks test）。

    仅运行指定的任务实例，不触发其上下游任务，用于临时验证某个采集/同步任务。
    gcloud 语法: run <ENV> ... tasks test -- <DAG_ID> <TASK_ID> <DATE> [--tries N]
    """
    cmd_args = [args.dag, args.task, args.date]
    if args.tries:
        cmd_args += ["--tries", str(args.tries)]
    out = gcloud_composer_run(args.env, args.project, args.location,
                              "tasks", "test", cmd_args)
    print(out)


def build_parser():
    parser = argparse.ArgumentParser(description="Airflow (Cloud Composer) 查询工具")
    parser.add_argument("--project", default=DEFAULT_PROJECT, help=f"GCP 项目 ID，默认 {DEFAULT_PROJECT}")
    parser.add_argument("--location", default=DEFAULT_LOCATION, help=f"区域，默认 {DEFAULT_LOCATION}")
    parser.add_argument("--env", default=DEFAULT_ENV, help=f"Composer 环境名，默认 {DEFAULT_ENV}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_envs = sub.add_parser("list-envs", help="列出 Cloud Composer 环境")
    p_envs.set_defaults(func=cmd_list_envs)

    p_dags = sub.add_parser("dags", help="DAG 相关命令")
    dag_sub = p_dags.add_subparsers(dest="dags_cmd", required=True)
    dag_sub.add_parser("list", help="列出所有 DAG").set_defaults(func=cmd_dags_list)
    p_details = dag_sub.add_parser("details", help="查看 DAG 详情")
    p_details.add_argument("--dag", required=True, help="DAG ID")
    p_details.set_defaults(func=cmd_dags_details)
    p_runs = dag_sub.add_parser("list-runs", help="查看 DAG 运行记录")
    p_runs.add_argument("--dag", required=True, help="DAG ID")
    p_runs.add_argument("--start-date", default=None, help="起始日期 YYYY-MM-DD")
    p_runs.add_argument("--end-date", default=None, help="结束日期 YYYY-MM-DD")
    p_runs.add_argument("--state", default=None, choices=["queued", "running", "success", "failed"],
                        help="按运行状态过滤")
    p_runs.set_defaults(func=cmd_dags_list_runs)

    p_tasks = sub.add_parser("tasks", help="任务相关命令")
    task_sub = p_tasks.add_subparsers(dest="tasks_cmd", required=True)
    p_list = task_sub.add_parser("list", help="列出 DAG 的所有任务")
    p_list.add_argument("--dag", required=True, help="DAG ID")
    p_list.add_argument("--summary", action="store_true", help="按前缀分组统计")
    p_list.set_defaults(func=cmd_tasks_list)

    p_test = task_sub.add_parser("test", help="手动执行 DAG 中的单个任务（不触发上下游）")
    p_test.add_argument("--dag", required=True, help="DAG ID（如 hicc_etl_morning_full）")
    p_test.add_argument("--task", required=True,
                        help="任务 ID（TaskGroup 用点分隔，如 collect_layer.tg_amazon.crawl_amazon_mp_shipping_list）")
    p_test.add_argument("--date", required=True, help="执行日期 YYYY-MM-DD（logical_date）")
    p_test.add_argument("--tries", type=int, default=None, help="重试次数（默认使用 DAG 配置）")
    p_test.set_defaults(func=cmd_tasks_test)
    return parser


if __name__ == "__main__":
    # 解析前归位全局选项，保证 --env/--project/--location 可写在任意位置
    args = build_parser().parse_args(_normalize_argv(sys.argv[1:]))
    args.func(args)
