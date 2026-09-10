---
name: airflow
description: 通过 gcloud 查询 GCP Cloud Composer (Airflow) 的调度信息：列出 DAG、查看 DAG 详情、列出某个 DAG 包含的所有任务并按层/模块分组统计、查看运行记录、手动执行 DAG 中的单个任务（airflow tasks test）。当用户询问某个 Airflow 调度/DAG 包含什么任务、DAG 结构、运行状态，或需要手动执行/重跑某个采集任务时调用。
---

# Airflow (Cloud Composer) 查询技能

通过 `gcloud composer environments run` 在 Cloud Composer 环境内执行 airflow CLI 命令，查询 DAG 与任务信息。

## 前置要求

- 已安装 gcloud 并认证（`gcloud auth login`，账号需有访问 Cloud Composer 环境的权限）
- 默认环境参数：项目 `hiccpet-481303`、区域 `asia-southeast1`、Composer 环境 `hicc`

## 常用参数

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| `--project` | GCP 项目 ID | `hiccpet-481303` |
| `--location` | 区域 | `asia-southeast1` |
| `--env` | Cloud Composer 环境名 | `hicc` |
| `--dag` | DAG ID（如 `hicc_etl_morning_full`） | 必填 |

脚本位置：`scripts/airflow_cli.py`（与 skill 同级目录，直接以 python 运行）。

> 💡 **全局选项 `--env` / `--project` / `--location` 可写在命令行任意位置**（脚本解析前会自动归位）。
> 无论放在子命令前（`--env hicc tasks list`）还是子命令后（`tasks list --env hicc`）均有效。
> 推荐放在子命令后、紧邻参数，如 `tasks --env hicc list --dag <DAG_ID>`。

## 命令

### 1. 列出 Cloud Composer 环境

```bash
python scripts/airflow_cli.py list-envs --project <PROJECT> --location <LOC>
```

### 2. 列出所有 DAG

```bash
python scripts/airflow_cli.py dags list --env <ENV>
```

### 3. 查看 DAG 详情（调度周期、所有者等）

```bash
python scripts/airflow_cli.py dags details --env <ENV> --dag <DAG_ID>
```

### 4. 列出某个 DAG 包含的所有任务

```bash
# 完整任务清单
python scripts/airflow_cli.py tasks list --env <ENV> --dag <DAG_ID>

# 按前缀分组统计（推荐：大 DAG 一眼看清各层/模块任务数）
python scripts/airflow_cli.py tasks list --env <ENV> --dag <DAG_ID> --summary
```

`--summary` 会对任务 ID 按 `前缀` 分组计数，例如：

- `collect_layer.tg_amazon 30` → 采集层领星 Amazon 共 30 个任务
- `sync_layer 42` → 数据同步层共 42 个任务
- `start / end` → 无前缀的控制节点单独成组

### 5. 查看 DAG 运行记录

```bash
python scripts/airflow_cli.py dags list-runs --env <ENV> --dag <DAG_ID> \
  [--start-date 2026-08-19] [--end-date YYYY-MM-DD] [--state success|failed|running|queued]
```

`--state` 可按状态过滤（成功 / 失败 / 运行中 / 排队），`--start-date` / `--end-date` 按执行日期过滤。

### 6. 手动执行 DAG 中的单个任务（临时验证用）

```bash
python scripts/airflow_cli.py tasks test --env <ENV> --dag <DAG_ID> \
  --task <TASK_ID> --date YYYY-MM-DD [--tries N]
```

只运行指定的任务实例，**不会触发其上下游任务**，用于临时验证某个采集/同步任务（如排查接口报错后重跑单个任务）。

- `--task`：完整任务 ID。TaskGroup 内任务用点分隔，例如 `collect_layer.tg_amazon.crawl_amazon_mp_shipping_list`
- `--date`：logical_date（Airflow 执行日期），如 `2026-08-24`
- `--tries`：可选，重试次数（默认使用 DAG 配置的 retries）

> ⚠️ 任务 ID 里的**数据源名**必须与 `crawl_sources.yaml` 的源关键字一致（如 `amazon`），
> 不是 URL 前缀（`lingxing_amazon` 只是 API 路径）。写错会导致 `TaskNotFound`。
> 可用 `tasks list` 先查到准确的任务 ID。

## 注意事项与常见坑

- **gcloud composer run 命令语法**：SUBCOMMAND（如 `tasks` / `dags`）必须作为位置参数放在 `--` **之前**，airflow 命令自身的位置参数放在 `--` 之后：
  `gcloud composer environments run <ENV> --location <LOC> --project <PROJ> tasks list -- <DAG_ID>`
  把 `tasks` 也放到 `--` 之后会报 `argument SUBCOMMAND: Must be specified`。脚本已按此规则封装。
- **输出干扰行**：gcloud 会先打印 `Executing the command: ...`、`Command has been started ...`、`Use ctrl-c ...`，脚本已自动过滤。
- **大 DAG 建议加 `--summary`**：如 `hicc_etl_morning_full` 共 275 个任务，完整列表很长，`--summary` 可先看整体结构。
- **命令是异步执行**：gcloud 启动后等待 airflow 命令输出返回，耗时可能较长，请耐心等待（脚本为阻塞调用）。
- 若需查看单个任务的历史运行状态，可用 `airflow tasks states`，本 skill 暂未封装。
