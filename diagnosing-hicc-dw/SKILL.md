---
name: diagnosing-hicc-dw
label: HICC数据仓库排障专家
description: |
  数据仓库排障方法论，覆盖 DAG 任务失败、数据质量异常（多/少/错）、
  BigQuery 性能劣化和数据管道堵塞。
  6 阶段 forensic 排障框架，结合 HICC PET 数仓架构与 BigQuery 诊断工具。
  遇到 "数据对不上"、"DAG 报错"、"查询变慢"、"回刷失败" 时使用。
---

# HICC 数据仓库排障方法论

**Leading word: forensic** — 像法医一样检视数据，用证据而不是猜测定位问题。

## 使用前必读

1. **始终从故障的"现象"出发**，而不是从"假设"出发
2. 使用 `hicc-dw` skill 查表结构、血缘、口径作为排障上下文
3. 如涉及 Airflow DAG 状态查询，使用 `airflow` skill
4. 如涉及 BigQuery 查询，使用 `bigquery-query` skill
5. **HICC 分层定位思维**：故障从哪一层开始 → DTS/采集 → ODS → DIM → DWD → DWS → FineBI

## 排障框架总览

```
Phase 1: Forensic Find the Leak   →  验证"问题是否存在"，构建对账信号
Phase 2: Forensic Isolate Layer   →  定位问题发生在哪一层（DTS/ODS/DIM/DWD/DWS/BI）
Phase 3: Forensic Rank Causes     →  3-5 个可验证的假设
Phase 4: Forensic Dive Deeper     →  逐层探针，精准命中根因
Phase 5: Forensic Fix + Lock      →  修复 + 数据验证 + DQ 巡检
Phase 6: Forensic Verify+Cleanup  →  确认修复有效，清理临时资源
```

---

## Phase 1 — Forensic Find the Leak（构建对账信号）

> **无对账信号，不走 Phase 2。** 不先写对账 SQL 就去翻日志 = 撞大运。

### HICC 标准对账查询模板

#### 1a. 行数对账（最基础，先做这个）

```sql
-- 源 vs 目标：检查行数是否一致
-- 替换 {source_table}, {target_table}, {partition_date} 为实际值

WITH source AS (
  SELECT COUNT(1) AS row_count,
         COUNT(DISTINCT {pk_col}) AS unique_keys
  FROM `hiccpet-481303.{source_table}`
  WHERE {partition_date_col} = '{partition_date}'
),
target AS (
  SELECT COUNT(1) AS row_count,
         COUNT(DISTINCT {pk_col}) AS unique_keys
  FROM `hiccpet-481303.{target_table}`
  WHERE {partition_date_col} = '{partition_date}'
)
SELECT '{source_table}' AS side, row_count, unique_keys FROM source
UNION ALL
SELECT '{target_table}' AS side, row_count, unique_keys FROM target;
```

**判断标准**：
- row_count 差值 > 5% → 存在数据丢失或重复，进入 Phase 2
- unique_keys 不一致 → 主键完整性有问题

#### 1b. 日维度行数趋势（找到异常的第一天）

```sql
-- 按天检查行数曲线，找到数据断裂点
SELECT {partition_date_col} AS dt, COUNT(1) AS row_count
FROM `hiccpet-481303.{suspected_table}`
WHERE {partition_date_col} >= DATE_SUB(CURRENT_DATE(), INTERVAL 14 DAY)
GROUP BY dt
ORDER BY dt;
```

**异常模式**：
- 某天行数骤降为 0 → DTS 失败 或 ODS 增量缺失
- 某天行数突增 2× → 增量逻辑产生重复（没去重）
- 长时间连续下降 → 源数据本身在减少（正常业务）

#### 1c. 核心指标 SUM 对账（事实表专有）

```sql
-- 检查关键度量值是否一致
WITH source AS (
  SELECT COUNT(1) AS rows,
         COALESCE(ROUND(SUM({metric_col}), 2), 0) AS total_metric
  FROM `hiccpet-481303.{source_table}`
  WHERE {partition_date_col} = '{partition_date}'
),
target AS (
  SELECT COUNT(1) AS rows,
         COALESCE(ROUND(SUM({metric_col}), 2), 0) AS total_metric
  FROM `hiccpet-481303.{target_table}`
  WHERE {partition_date_col} = '{partition_date}'
)
SELECT s.rows AS src_rows, t.rows AS tgt_rows,
       s.total_metric AS src_metric, t.total_metric AS tgt_metric,
       ROUND(ABS(s.total_metric - t.total_metric) / NULLIF(GREATEST(s.total_metric, t.total_metric), 0) * 100, 4) AS pct_diff
FROM source s, target t;
```

**判断标准**：
- pct_diff < 0.1% → 可接受
- pct_diff >= 0.1% → 不可接受，进入 Phase 2

#### 1d. 增量对比（今天 vs 昨天 — 数据漂移检测）

```sql
-- 检查今天的数据相比昨天是否出现异常跳变
-- 用于发现增量逻辑异常、重复插入、缺失
WITH today AS (
  SELECT {partition_date_col} AS dt, COUNT(1) AS rows,
         COALESCE(ROUND(SUM({metric_col}), 2), 0) AS total_metric
  FROM `hiccpet-481303.{table}`
  WHERE {partition_date_col} = CURRENT_DATE()
  GROUP BY dt
),
yesterday AS (
  SELECT {partition_date_col} AS dt, COUNT(1) AS rows,
         COALESCE(ROUND(SUM({metric_col}), 2), 0) AS total_metric
  FROM `hiccpet-481303.{table}`
  WHERE {partition_date_col} = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
  GROUP BY dt
),
last_week AS (
  -- 同时对比上周同日，排除周末效应
  SELECT COUNT(1) AS rows,
         COALESCE(ROUND(SUM({metric_col}), 2), 0) AS total_metric
  FROM `hiccpet-481303.{table}`
  WHERE {partition_date_col} = DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
)
SELECT t.dt, t.rows AS today_rows, y.rows AS yesterday_rows,
       ROUND((t.rows - y.rows) / NULLIF(y.rows, 0) * 100, 2) AS row_pct_change,
       t.total_metric AS today_metric, y.total_metric AS yesterday_metric,
       ROUND((t.total_metric - y.total_metric) / NULLIF(y.total_metric, 0) * 100, 2) AS metric_pct_change
FROM today t, yesterday y, last_week lw;
```

**判断标准**：
- row_pct_change > ±30%（相比昨天）→ 需要关注
- metric_pct_change > ±30%（相比昨天）→ 可能口径变了

#### 1e. Airflow 任务失败快速确认（使用 `airflow` skill）

```
# 查某个 DAG 的近期失败记录
python scripts/airflow_cli.py dags list-runs --env hicc --dag {dag_id} --state failed --start-date {7天前}
```

### ✅ Phase 1 Completion Criterion

**必须完成以下至少一项才能进入 Phase 2：**
- [ ] 执行了一次行数对账 SQL，确认了源和目标的不一致
- [ ] 执行了日维度趋势查询，定位到了异常日期
- [ ] 执行了 Airflow list-runs，确认了任务失败及其时间点
- [ ] 执行了核心指标对账，确认了金额类偏差
- [ ] 执行了增量漂移检测，发现了行数或指标的跳变

---

## Phase 2 — Forensic Isolate Layer（定位故障层）

> HICC 数仓是 **4 层架构**（DTS → DIM/DWD → DWS → BI）。Forensic 定位：问题一定落在某一层。逐层检查，从最上层开始。

### 定位流程

```
用户反馈"数据不对"
    │
    ├─ 1. FineBI 报表层面
    │    检查 FineBI 的 SQL 定义 → 查报表 SQL 引用了哪张表/视图
    │    └─ 问题在 BI 层 → 修复 BI SQL
    │
    ├─ 2. DWS 汇总层
    │    对账 DWS vs DWD：行数+SUM 是否一致
    │    └─ 问题在 DWS → 修复 DWS 模型
    │
    ├─ 3. DWD 明细层
    │    对账 DWD vs ODS：行数+SUM 是否一致
    │    └─ 问题在 DWD → 修复 DWD 清洗逻辑
    │
    ├─ 4. DIM 维度层
    │    检查维度表是否完整（SKU 映射、汇率、渠道等）
    │    注意：DIM 问题往往表现为 DWD/DWS 数据异常
    │    └─ 问题在 DIM → 修复维度表
    │
    ├─ 5. ODS 存储层
    │    对账 ODS vs 源系统：行数是否一致
    │    └─ 问题在 ODS → DTS 同步失败/采集脚本异常
    │
    └─ 6. DTS/采集层
        查 DTS 任务运行状态、查采集脚本日志
        └─ 问题在采集 → 重跑 DTS / 修复采集代码
```

### Forensic 分层排查要点

| 层 | 典型故障 | 排查要点 |
|----|---------|---------|
| **DTS** | 传输配置错误、连接超时 | 查 DTS job 状态、源库连通性、权限变更 |
| **ODS** | 增量未到位、分区未创建 | `__TABLES_SUMMARY__` 查表大小和 last_modified_time |
| **DIM** | SCD2 历史记录异常 | `dim_product_skus_sales` 查 SKU 映射完整率 |
| **DWD** | 清洗逻辑变更未回刷、增量条件错误 | 查 dbt run_results，确认是否包含目标日期 |
| **DWS** | 汇总口径变化、分区未覆盖 | DWS vs DWD 对账 |
| **DIM** | 汇率缺失、SKU 映射不到 | `dim_exchange_rates` 查指定月的汇率覆盖情况 |
| **FineBI** | 指标定义引错字段、缓存超时 | 查 FineBI 数据定义与 dbt 模型字段是否一致 |

### ✅ Phase 2 Completion Criterion

- [ ] 明确了问题发生在哪一层（DTS/ODS/DIM/DWD/DWS/BI）
- [ ] 缩小了日期范围（精确到天）
- [ ] 缩小了维度范围（渠道/店铺/SKU 如果有）
- [ ] 如果是 DIM 层问题，确认是否影响了 DWD/DWS 一层还是多层

---

## Phase 3 — Forensic Rank Causes（生成可验证假设）

> 基于 Phase 2 确定的层，生成 3-5 个可验证的假设。**列出给用户确认**，用户可能有已经排除的候选。

### HICC 常见故障模式 → 假设模板

#### 故障模式 A：某天行数归零或骤降

| # | 假设 | 验证方法 |
|---|------|---------|
| 1 | DTS 传输在该日期失败，ODS 无新数据 | 查 DTS job 历史（`hicc-dts-{source}`），确认是否有 success entry |
| 2 | Airflow DAG 在该日期的 run 被跳过/失败 | 查 Airflow DAG runs（`list-runs --state failed`） |
| 3 | dbt 增量模型 where 条件排除了该日期 | 查 dbt model SQL 的 `is_incremental()` 条件，确认日期过滤逻辑 |
| 4 | 上游源表该日期确实没有数据 | 直接查 ODS 源表确认行数是否为 0 |

#### 故障模式 B：指标值偏差（金额对不上）

| # | 假设 | 验证方法 |
|---|------|---------|
| 1 | 汇率未更新或 JOIN 错误 | 查 `dim_exchange_rates` 中目标月的汇率记录数 |
| 2 | 口径变了（如含/不含退款、含/不含运费） | 对比 DWD SQL 与之前的版本，确认口径是否一致 |
| 3 | 增量回刷未覆盖该日期 | 查 backfill 记录，确认该日期是否在回刷范围内 |
| 4 | 源表数据在指定日期有重复（业务异常） | 查 ODS 对应表的主键去重检查 |

#### 故障模式 C：DAG/任务异常

| # | 假设 | 验证方法 |
|---|------|---------|
| 1 | Worker Pod 重启导致 dbt build 中断 | 查 scheduler log 中 "gcsfuse"、"celery@"、"ready." 的时间戳 |
| 2 | DTS 接口超时 | 查 DTS job 的 error 信息（"Public Key Retrieval"、"Access denied"） |
| 3 | 上游数据延迟，触发下游依赖失败 | 查任务依赖链，确认上游是否先失败 |
| 4 | Pool 资源不足，任务排队超时 | 查 `pool=hicc_sync_pool` 的 DAG log 是否出现 "No available slots" |

#### 故障模式 D：调度器未触发 / DAG 不启动

| # | 假设 | 验证方法 |
|---|------|---------|
| 1 | DAG 处于 paused 状态 | 查 `dags list` 确认 `is_paused` 是否为 False |
| 2 | max_active_runs 已达到上限 | 查 scheduler log 中 "max_active_runs" 或检查是否有 running run |
| 3 | 调度器追赶延迟 | 查 scheduler log 中 "is not having its next run scheduled" 或 "backfill" |
| 4 | 前一次运行未完成阻塞了后续调度 | 检查是否有一个 run 卡在 running 状态超过 24h |
| 5 | 调度周期（schedule_interval）未到达执行时间 | 确认 DAG 的 `schedule` 定义与当前时间的关系 |

### ✅ Phase 3 Completion Criterion

- [ ] 生成 3-5 个假设，每个有明确的验证方法
- [ ] 假设已按可能性排序
- [ ] 已告知用户，让用户排除已经排查过的假设

---

## Phase 4 — Forensic Dive Deeper（精准探针）

> 按 Phase 3 的假设逐一验证。**一次只验证一个假设。**

### HICC 探针工具箱

#### 探针 A：BigQuery INFORMATION_SCHEMA

```sql
-- A1. 查某张表的分区信息和数据量
SELECT table_name, partition_id, total_rows, total_logical_bytes
FROM `hiccpet-481303.INFORMATION_SCHEMA.PARTITIONS`
WHERE table_name = '{table_name}'
ORDER BY partition_id DESC
LIMIT 30;
```

```sql
-- A2. 查某天某个时间段内的 BigQuery 作业（找失败/慢的作业）
SELECT job_id, creation_time, end_time, state, error_result,
       ROUND(total_slot_ms / 1000, 1) AS slot_seconds,
       total_bytes_processed,
       query
FROM `region-asia-southeast1.INFORMATION_SCHEMA.JOBS_BY_PROJECT`
WHERE DATE(creation_time) = '{date}'
  AND state != 'PENDING'
ORDER BY creation_time DESC
LIMIT 50;
```

```sql
-- A3. 查指定表的元数据（最近更新时间）
SELECT table_name, table_type, table_type_name,
       TIMESTAMP_MILLIS(last_modified_time) AS last_modified,
       row_count, size_bytes
FROM `hiccpet-481303.{dataset}.__TABLES_SUMMARY__`
WHERE table_id = '{table_name}';
```

```sql
-- A4. 查 BigQuery slot 利用率（看是否接近资源上限）
SELECT
  TIMESTAMP_TRUNC(period_start, HOUR) AS usage_hour,
  ROUND(AVG(period_slot_ms) / 1000, 1) AS avg_slot_sec,
  MAX(period_slot_ms) / 1000 AS max_slot_sec,
  SUM(period_slot_ms) / 1000 AS total_slot_sec
FROM `region-asia-southeast1.INFORMATION_SCHEMA.JOBS_TIMELINE_BY_PROJECT`
WHERE DATE(job_creation_time) = '{date}'
  AND job_type = 'QUERY'
GROUP BY usage_hour
ORDER BY usage_hour;
```

#### 探针 B：Airflow 日志查询（`airflow` skill）

```
# 查某个任务在指定日期的日志
python scripts/airflow_cli.py tasks test --env hicc --dag {dag_id} \
  --task {task_id} --date {execution_date}

# 查 DAG 近期的所有运行记录（含各状态）
python scripts/airflow_cli.py dags list-runs --env hicc --dag {dag_id} --start-date {7天前}
```

#### 探针 C：DTS 任务状态查询

```
# 查 DTS 任务的运行历史（通过 gcloud）
gcloud transfers operations list \
  --job-names=projects/hiccpet-481303/locations/asia-southeast1/transferConfigs/{config_id} \
  --format="table(name,transferSpec,startTime,endTime,status)"
```

#### 探针 D：数据分布探查

```sql
-- D1. 按某维度分组统计，找异常分布
SELECT {dim_col}, COUNT(1) AS rows,
       ROUND(AVG({metric_col}), 2) AS avg_metric,
       ROUND(SUM({metric_col}), 2) AS total_metric,
       COUNT(DISTINCT {pk_col}) AS unique_keys
FROM `hiccpet-481303.{suspected_table}`
WHERE {partition_date_col} = '{suspected_date}'
GROUP BY {dim_col}
ORDER BY rows DESC
LIMIT 20;
```

```sql
-- D2. 查指定表的空值率（检查清洗逻辑是否产生大量 NULL）
SELECT
  COUNT(1) AS total_rows,
  COUNTIF({column_a} IS NULL) AS col_a_nulls,
  ROUND(COUNTIF({column_a} IS NULL) / COUNT(1) * 100, 2) AS col_a_null_pct,
  COUNTIF({column_b} IS NULL) AS col_b_nulls,
  ROUND(COUNTIF({column_b} IS NULL) / COUNT(1) * 100, 2) AS col_b_null_pct
FROM `hiccpet-481303.{suspected_table}`
WHERE {partition_date_col} = '{suspected_date}';
```

#### 探针 E：Worker Pod 状态与日志

```
# 查 Composer 环境的 GKE 集群
gcloud container clusters list --project hiccpet-481303 --region asia-southeast1

# 查 worker pod 重启事件（需要 kubectl 访问 Composer 集群）
kubectl get pods -n default | grep airflow-worker
kubectl describe pod airflow-worker-xxxxx | grep -A5 Events
```

#### 探针 F：Cloud Logging 脚本（最强利器 — 我们真实排障的主力武器）

当需要在 GCP Logging 中搜索 Airflow worker/scheduler 日志时，使用 Python SDK 而非 gcloud CLI（避免 Powershell 的 `--` 分隔符问题）。

**脚本模板：**

```python
# probe_{target}_logging.py — 从 Cloud Logging 搜索指定模式的日志
# 使用方法：python probe_{target}_logging.py

from google.cloud import logging_v2

client = logging_v2.Client(project='hiccpet-481303')

# ===== 配置区 =====
FILTER = (
    'logName:"airflow-worker" AND '
    '("Getting metadata" OR "metadata.internal" OR "503") '  # ← 换成你要搜的关键词
    'AND timestamp>="2026-08-25T00:00:00Z" '
    'AND timestamp<="2026-08-25T01:00:00Z"'
)
OUTPUT_FILE = "probe_result.txt"    # 输出文件路径
MAX_ENTRIES = 200                    # 最大返回条目数

# ===== 执行查询 =====
entries = list(client.list_entries(filter_=FILTER, max_results=MAX_ENTRIES))

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(f"Found {len(entries)} entries\n{'='*60}\n")
    for e in entries:
        ts = str(e.timestamp)[:19] if e.timestamp else "N/A"
        txt = (e.payload or "").strip()[:1000]
        f.write(f"--- {ts}\n{txt}\n\n")

print(f"Found {len(entries)} entries -> {OUTPUT_FILE}")
```

**常用过滤条件模板（替换 FILTER 中的关键词）：**

| 排障场景 | FILTER 关键词 |
|---------|---------------|
| metadata 503 | `"Getting metadata" OR "metadata.internal" OR "503"` |
| Worker 重启 | `"gcsfuse" OR "celery@" OR "Start gcsfuse" OR "ready."` |
| dbt build 失败 | `"dbt_producer_watcher" AND ("FAILED" OR "exception" OR "Error")` |
| Producer 任务失败 | `"dbt_producer_watcher" AND ("Marking task as FAILED" OR "TaskInstance Finished")` |
| 任务超时 | `"timeout" OR "Timeout" OR "Durations" AND ">="` |
| Worker OOM/驱逐 | `"OOM" OR "Out of memory" OR "evict" OR "Evict" OR "unhealthy"` |
| 调度器追赶 | `"scheduler" AND ("next run" OR "backfill" OR "max_active_runs")` |

#### 探针 G：dbt run_results.json 分析

当 dbt Producer 任务失败但看不到详细错误时，从 GCS 获取 `run_results.json`。

```python
# probe_dbt_run_results.py — 分析 dbt 构建结果，定位失败节点
# 使用方法：先找到 run_results.json 路径，下载后运行此脚本

import json

path = "run_results.json"       # 替换为实际路径
with open(path, encoding="utf-8") as f:
    data = json.load(f)

results = data.get("results", [])

failed_nodes = [r for r in results if r.get("status") in ("error", "fail")]
skipped_nodes = [r for r in results if r.get("status") == "skipped"]

print(f"Total nodes: {len(results)}")
print(f"Failed: {len(failed_nodes)}, Skipped: {len(skipped_nodes)}\n")

for n in failed_nodes:
    node_id = n.get("unique_id", "?")
    msg = n.get("message", "")
    err = n.get("failure", {})
    # 提取关键错误行
    lines = (msg or "").split("\n")
    error_lines = [l for l in lines if "Error" in l or "Failure" in l or "Compilation" in l]
    print(f"❌ FAILED: {node_id}")
    for el in error_lines[:3]:
        print(f"   {el[:300]}")
    if not error_lines:
        print(f"   {msg[:300]}")
    print()
```

**常用路径（从 GCS 获取 run_results.json）：**

```
# Composer 环境中 dbt 的默认输出路径
/home/airflow/gcs/data/dbt/{project}/target/run_results.json

# 或通过 DAG 任务日志中的路径定位
```

#### 探针 H：调度器健康检查

当怀疑 DAG 调度器未触发时使用：

```
# H1. 查 DAG 是否暂停
python scripts/airflow_cli.py dags list --env hicc | findstr {dag_id}

# H2. 查是否有正在运行的 run（可能阻塞后续调度）
python scripts/airflow_cli.py dags list-runs --env hicc --dag {dag_id} --state running

# H3. 查 scheduler 日志中是否有调度异常（使用探针 F 的脚本）
# Cloud Logging FILTER:
#   logName:"airflow-scheduler" AND "{dag_id}"
#   AND ("max_active_runs" OR "scheduling" OR "next run" OR "backfill")

# H4. 确认调度周期
# 查 DAG 的 schedule_interval 和 start_date
python scripts/airflow_cli.py dags details --env hicc --dag {dag_id}

# H5. 检查 DAG 的 next_dagrun 字段（通过 Airflow DB）
# 需要 airflow CLI 权限：
gcloud composer environments run hicc --location asia-southeast1 --project hiccpet-481303 \
  dags list-runs -- --dag-id {dag_id} -o table
```

#### 探针 I：FineBI 字段映射检查

当怀疑 FineBI 报表字段与 dbt 模型不一致时使用：

```
# 1. 用 hicc-dw skill 查 dbt 模型的字段定义
#    输入：dwd_trd_toc_order_item_di 有哪些字段

# 2. 对比 FineBI 中该指标的 SQL 定义，检查：
#    - 字段名是否一致（大小写敏感）
#    - 字段类型是否兼容（STRING vs INT64）
#    - 引用的表名是否准确（_snap vs _di vs _v）
#    - JOIN 条件是否正确

# 3. 常用检查 SQL：查出 FineBI 预期字段与实际表字段的差异
SELECT column_name, data_type, is_nullable
FROM `hiccpet-481303.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = '{table_name}'
ORDER BY ordinal_position;
```

### ✅ Phase 4 Completion Criterion

- [ ] 至少执行了 1 个探针来验证 Phase 3 中排第一的假设
- [ ] 如假设被证伪，用同样的方法验证下一个假设
- [ ] 找到了根因的具体证据（日志行 / SQL 结果 / 错误信息）

---

## Phase 5 — Forensic Fix + Lock（修复 + 数据验证）

> 修复方案取决于根因在哪一层。**Forensic 原则：不先验证就上线 = 没修复。**

### HICC 常见修复模式

#### 修复 A：DTS 失败 → 重跑 DTS

```bash
# 手动触发 DTS 重跑
gcloud transfer operations list \
  --job-names=projects/hiccpet-481303/locations/asia-southeast1/transferConfigs/{config_id} \
  --format="value(name)" | head -1
```

如果 DTS 配置问题（权限、JDBC 参数），先在 GCP Console 修复配置再重跑。

#### 修复 B：dbt 模型逻辑修复 → 增量回刷

```bash
# 1. 修复 dbt model SQL
# 2. 编译验证
dbt compile --select {model_name}

# 3. 用 implement-hicc-dw 的 BACKFILL Handler 生成回刷 SQL
# 4. 先回刷异常日期，与当前数据做 1 天重叠对账
```

**重叠对账验证 SQL：**

```sql
-- 对比旧逻辑（当前表）和新逻辑（临时表）在重叠日期的数据
WITH old_logic AS (
  SELECT {pk_col}, SUM({metric_col}) AS total
  FROM `hiccpet-481303.{production_table}`
  WHERE {partition_date_col} = '{overlap_date}'
  GROUP BY {pk_col}
),
new_logic AS (
  SELECT {pk_col}, SUM({metric_col}) AS total
  FROM `hiccpet-481303.{staging_table}`
  WHERE {partition_date_col} = '{overlap_date}'
  GROUP BY {pk_col}
)
SELECT COALESCE(o.{pk_col}, n.{pk_col}) AS key,
       o.total AS old_total, n.total AS new_total,
       ABS(o.total - n.total) AS diff
FROM old_logic o
FULL OUTER JOIN new_logic n USING ({pk_col})
WHERE o.total IS DISTINCT FROM n.total
ORDER BY diff DESC
LIMIT 20;
```

**验证通过标准**：Max diff per {pk_col} < $0.01（事实表）或 row count 100% 一致。

#### 修复 C：Worker 重启/超时 → 加重试+确认 Slot

1. 检查 DAG `default_args` 中的 `retries` 配置
2. 确认 `retry_delay` 和 `retry_exponential_backoff` 是否开启
3. 如果频繁出现，考虑增加 worker 资源或减少并发任务数

```python
# HICC 标准的重试配置
default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "retry_exponential_backoff": True,
    "max_retry_delay": timedelta(minutes=15),
}
```

#### 修复 D：增量逻辑异常 → 修复 merge/insert_overwrite 条件

```sql
-- HICC 标准增量模式：insert_overwrite + partition filter
{{
  config(
    materialized='incremental',
    partition_by={'field': 'event_date_utc', 'data_type': 'date'},
    incremental_strategy='insert_overwrite',
    on_schema_change='sync_all_columns',
  )
}}

-- 增量条件必须正确
{% if is_incremental() %}
  WHERE event_date_utc >= _dbt_max_partition
{% endif %}
```

#### 修复 E：维度数据缺失 → 补全维度

```sql
-- 检查维度匹配率
SELECT COUNTIF(t.{dim_fk} IS NULL) AS unmapped_rows,
       COUNT(1) AS total_rows,
       ROUND(COUNTIF(t.{dim_fk} IS NULL) / COUNT(1) * 100, 2) AS unmapped_pct
FROM `hiccpet-481303.{fact_table}` t
LEFT JOIN `hiccpet-481303.{dim_table}` d
  ON t.{dim_key} = d.{dim_key}
WHERE t.{partition_date_col} = '{target_date}';
```

如果 unmapped_pct > 5%，需要先补全维度表再回刷事实表。

#### 修复 F：调度器未触发 → 手动 Trigger DAG

```bash
# 手动触发 DAG 运行（重新调度）
python scripts/airflow_cli.py dags trigger --env hicc --dag {dag_id}

# 如果是因为前一次运行卡住，需要先清除卡住的 run
python scripts/airflow_cli.py dags clear --env hicc --dag {dag_id} --date {日期}
```

### ✅ Phase 5 Completion Criterion

- [ ] 根因已被修复
- [ ] 修复后的数据已通过对账验证（Phase 1 的对账信号变绿）
- [ ] 修复方案兼容现有数据（老数据不回滚）

---

## Phase 6 — Forensic Verify + Cleanup（验证 + 清理）

### 验证清单

- [ ] 重新运行 Phase 1 的对账信号，确认已变绿（问题消失）
- [ ] 如果涉及回刷，确认全部回刷日期均已覆盖
- [ ] 如果涉及 dbt SQL 修改，确认 schema.yml 测试没有新增失败
- [ ] 在 Airflow 上手动触发了修复后的 DAG run，且成功完成

### 清理清单

- [ ] 临时表已删除（`tmp_*`, `backup_*`）
- [ ] 临时探针脚本（`probe_*.py`）已清理
- [ ] 临时探针 SQL 已清理
- [ ] 如果涉及采集代码修复，确认线上已部署新代码
- [ ] 如果涉及 dbt 模型，确认变更已提交到 Git

### 反馈到建模 Pipeline（如果有）

如果排障后发现是**数据模型设计问题**（而非代码 Bug），而非单纯的逻辑 Bug：

- **模型粒度不对** → 需反馈到 `grill-hicc-dw` 重新挑战粒度设计
- **缺少维度表**（如发现某个关键维度不存在导致匹配不上）→ 走 `grill → to-spec → to-ticket → implement` 流程新建
- **口径定义不一致**（FineBI 口径与 dbt 模型不一致）→ 更新 `hicc-dw` 的指标口径文档

### 归档（可选）

如果这是一个值得记录的故障模式，可以补充到本文档的「常见故障模式」中，积累团队排障知识库。

---

## 附录 A：HICC 常见故障模式速查

| 故障现象 | 最可能的原因 | 优先排查的探针 | 修复方式 |
|---------|------------|--------------|---------|
| DAG 任务失败（500 Internal Server） | 后端采集接口报错 | 查采集脚本日志 | 修复采集代码 |
| sync_layer 任务失败（metadata 503） | GCE metadata server 瞬时不可用 | 探针 F：查 worker log 中 "Getting metadata" | 重跑，无需修代码 |
| dbt Consumer 失败、Producer 无输出 | Worker pod 重启（gcsfuse/celery） | 探针 F：查 scheduler log + worker event | 重跑，考虑加 retry |
| 某表行数归零 | DTS 失败 / 增量条件异常 | 探针 A1：行数趋势 SQL + 探针 C：DTS job 历史 | 重跑 DTS / 修复 SQL |
| 金额对不上 | 口径变更 / 汇率缺失 / 重复数据 | 探针 A3+探针 D2：SUM 对账 + 空值率检查 | 回刷 + 对齐口径 |
| 查询结果含 NULL | SCD2 维度匹配不到 / 源数据异常 | 探针 D2：维度匹配率 SQL | 补维度 / 加默认值 |
| DTS 报错 "Public Key Retrieval" | JDBC 连接未配置 SSL | 探针 C：查 DTS 配置的 TLS 模式 | 改 TLS 为 Encryption only |
| DTS 报错 "Access denied" | 源库用户权限限制 IP | 探针 C：查 MySQL user 表的 Host 字段 | 添加 IP 授权 |
| DAG 今日未触发 | 调度器未触发 / max_active_runs 阻塞 | 探针 H：查 scheduler log + running runs | 探针 F 修复：Trigger DAG |
| dbt Producer 失败无详细错误 | run_results.json 未准确分析 | 探针 G：分析 run_results.json | 修复 SQL + 回刷 |
| 报表数据与数据库不一致 | FineBI 字段映射错误 / 引错表 | 探针 I：COLUMNS 对比 dbt 定义 | 修复 FineBI 字段映射 |
| BigQuery 查询变慢 | Slot 不足 / 查询计划劣化 | 探针 A2+A4：查 slot 利用率 + 慢作业 | 优化 SQL / 加 slot |

## 附录 B：排障流程速览（一图流）

```
问题来了
  │
  ├─ Phase 1: F. Leak    → 写对账 SQL → 确认问题存在
  │
  ├─ Phase 2: F. Layer   → ODS→DIM→DWD→DWS→BI → 定位故障层
  │
  ├─ Phase 3: F. Causes  → 列出 3-5 个假设 → 给用户确认
  │
  ├─ Phase 4: F. Probe   → Logging / InfoSchema / dbt / DTS → 精准命中
  │    可用探针: A-InfoSchema, B-Airflow, C-DTS, D-DataDist, 
  │            E-Worker, F-CloudLoggingSDK, G-dbtRunResults, 
  │            H-Scheduler, I-FineBI
  │
  ├─ Phase 5: F. Fix     → Fix + 重叠对账 → 验证修复
  │
  └─ Phase 6: F. Verify  → 验证 + 清临时表 + 反馈Pipeline
```

## 附录 C：与相关技能的衔接

| 我在做什么 | 调什么 skill |
|-----------|-------------|
| 查某表结构、口径、血缘 | `hicc-dw` |
| 查 Airflow DAG 运行记录、任务列表 | `airflow` |
| 查询 BigQuery 数据 | `bigquery-query` |
| 生成 dbt 修复后的回刷 SQL | `implement-hicc-dw` → BACKFILL Handler |
| 未排障但需走建模流程 | `grill-hicc-dw` → `to-spec-hicc-dw` → `to-ticket-hicc-dw` |