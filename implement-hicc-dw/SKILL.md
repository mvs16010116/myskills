---
name: "implement-hicc-dw"
description: "Generate dbt model SQL, BigQuery DDL, and data quality checks for HICC PET data warehouse. Invoke when implementing a ticket from tickets.md (DDL/DM/VAL/BACKFILL/REVIEW)."
---

# Implement — HICC Data Warehouse Chisel

Chisel precise data models from raw sources for the HICC PET data warehouse. This skill consumes a specific **ticket** from `tickets.md` (produced by `to-ticket-hicc-dw`) and produces the corresponding artifact: BigQuery DDL, dbt SQL + schema.yml, data quality SQL, backfill plan, or reconciliation queries.

**Chisel** is the leading word: carve away everything that isn't the model. The output is clean, structured, and deterministic — no extraneous columns, no ambiguous joins, no missing partitions. Every section below ends with a completion criterion: meet it before moving to the next chisel stroke.

Invoked as part of the `grill → to-spec → to-ticket → implement` pipeline. Each invocation handles **one ticket** from `tickets.md`. The pipeline executor dispatches independent tickets in parallel and blocking tickets sequentially.

## Ticket Dispatch

Read the active ticket from `tickets.md`. Determine its type and dispatch to the correct handler:

| Ticket Type | Handler | Output Artifact |
|-------------|---------|----------------|
| `DDL` | Section: DDL Handler | `CREATE TABLE` / `ALTER TABLE` DDL statements |
| `DM` | Sections 1-7: DM Handler | dbt model SQL + `schema.yml` |
| `VAL` | Section: VAL Handler | Data quality check SQL + results |
| `BACKFILL` | Section: BACKFILL Handler | Backfill SQL + execution plan |
| `REVIEW` | Section: REVIEW Handler | Reconciliation query SQL + results |

If no `tickets.md` exists (independent invocation), assume `DM` type and create from scratch using the spec.

## 1. Source Inventory

Before writing a single line of SQL, know what you are chiseling from.

1. **Identify source tables** — read the spec, list every upstream source (`{{ source('ods','table') }}` or `{{ ref('model') }}`)
2. **Read source schemas** — for each source table, get its column list via BigQuery `INFORMATION_SCHEMA.COLUMNS` or `hicc-dw` `lineage.md`
3. **Understand source data** — for each upstream field the spec references:
   - Sample values (`SELECT DISTINCT col FROM source LIMIT 10`)
   - Null ratio (`SELECT COUNTIF(col IS NULL)/COUNT(*) FROM source`)
   - Data type and range (`MIN/MAX`)
4. **Note source quirks** — the cleaning rules in `hicc-dw` (`cleaning-sales.md`, `cleaning-inventory.md`, etc.) document what upstream data needs fixing. Read the relevant file for each domain.
5. **Completion criterion**: every unique value of each source field the spec references has a documented null rate, data type, and quirk. If any field has >5% nulls, flag it in the model comment. Chisel stops here until sources are understood.

## 2. Grain Declaration

Chisel the grain first — it defines the shape of everything that follows. State the grain in one sentence at the top of every model. The grain is the "one row per X" contract.

| Pattern | Grain Declaration |
|---------|------------------|
| Transaction fact | `— Grain: one row per {order_id} × {line_item}` |
| Snapshot fact | `— Grain: one row per {sku} per {date}` |
| Dimension | `— Grain: one row per {dimension_key}` |
| Aggregate | `— Grain: one row per {channel} per {date}` |

Write this as a SQL comment on line 1 of the model file. If you can't write a single-line grain, the model is under-specified — go back to the spec and chisel the ambiguity.

**Completion criterion**: grain fits the model type (fact/snapshot/dim/aggregate) and is expressible in one sentence. If not, send the spec back for clarification.

## 3. Column Manifest

List every column the model outputs with its lineage. This is written as a SQL comment block at the top of the file, immediately after the grain:

```sql
-- Grain: one row per order_id × line_item
-- Columns:
--   order_id                ← src_orders.order_id
--   line_item_id            ← src_order_items.line_item_id
--   sku_id                  ← src_order_items.sku_id → dim_product_skus_sales.sku_id
--   order_date              ← src_orders.order_date
--   unit_price_usd          ← src_order_items.unit_price / COALESCE(dim_exchange_rates.to_usd_rate, 1)
--   quantity                ← src_order_items.quantity
--   total_amount_usd        ← unit_price_usd * quantity
--   etl_time                 = CURRENT_TIMESTAMP() + 8h  -- Beijing time
```

Every column maps to exactly one upstream source or is clearly marked as derived (`=` for computed, `←` for direct pass-through, `→` for lookup).

**Completion criterion**: every column in the target model's output is declared with lineage. No column appears in the SELECT without appearing in this manifest. Chisel the manifest until every column is accounted for.

## 4. SQL Generation — HICC Conventions

Every SQL line must follow these HICC conventions (these override any generic SQL style):

### 4.1 Comma-First Style

```sql
SELECT
      o.order_id
    , o.order_date
    , i.line_item_id
    , i.sku_id
    , i.quantity
FROM `source` o
JOIN `source2` i
    ON o.order_id = i.order_id
```

### 4.2 WHERE 1=1

```sql
WHERE 1=1
    AND o.order_date >= @start_date
    AND o.order_date < @end_date
```

### 4.3 Naming

| Element | Convention | Example |
|---------|-----------|---------|
| Model | `{layer}_{domain}_{business_object}_{suffix}` | `dwd_trd_toc_amazon_order_item_di` |
| Layer prefix | `dim_` / `dwd_` / `dws_` | `dws_trd_channel_daily_summary` |
| Suffix | `_di` = daily incremental, `_snap` = snapshot, `_v2` = version | `dwd_inv_global_detail_v2_snap` |
| Columns | snake_case | `unit_price_usd`, `order_date_utc` |
| CTEs | pascal-case acronym or full | `OrderItems`, `InventorySnap` |

### 4.4 BigQuery-Specific

- **Partitioning**: `PARTITION BY DATE(event_date_utc)` or `DATE(event_time_utc)` — prefer `_utc` suffixed timestamp columns. Default partition expiration: 365 days for DWD/DIM, 730 days for DWS.
- **Clustering**: order columns by cardinality descending. Typical: `channel_id`, `country_code`, `sku_id`, `event_date_utc`
- **Incremental models** (`_snap` suffix only): use `insert_overwrite` with `PARTITION BY` on the time column. Use `IF NOT EXISTS` guards.
- **Full-refresh models** (default `table`): use `CREATE OR REPLACE TABLE`
- **Disallow**: `SELECT *`, implicit cross-join, unqualified `INNER JOIN` without `ON` on same line
- **Business fields**: allow NULL (`INT64`, not `INT64 NOT NULL`)
- **Query cost**: when adding a column that requires a JOIN, note the table's byte estimate from `information_schema` — if >10GB scanned per run, flag for optimization

### 4.5 dbt Model Patterns

```sql
{{ config(
    materialized='table',
    partition_by={ 'field': 'event_date_utc', 'data_type': 'date' },
    cluster_by=['channel_id', 'country_code'],
    partition_expiration_days=365
) }}

-- Grain: one row per channel per date
-- Columns:
--   channel_id     ← src_orders.channel_id
--   event_date_utc ← src_orders.event_date_utc
--   total_sales_usd = SUM(unit_price_usd * quantity)

WITH Orders AS (
    SELECT
          channel_id
        , event_date_utc
        , unit_price_usd
        , quantity
    FROM {{ ref('dwd_trd_toc_order_item_di') }}
    WHERE 1=1
        {% if is_incremental() %}
            AND event_date_utc >= _dbt_max_partition
        {% endif %}
)

SELECT
      channel_id
    , event_date_utc
    , SUM(unit_price_usd * quantity) AS total_sales_usd
FROM Orders
GROUP BY 1, 2
```

### 4.6 Grain Integrity

- Every model **must have a primary key** (natural or surrogate). If no single column is unique, concatenate: `CONCAT(order_id, '_', line_item_id) AS order_item_key`
- For aggregate models, the grain IS the GROUP BY — verify that no GROUP BY produces fewer or more rows than the spec expects
- **Surrogate keys**: use `FARM_FINGERPRINT(CONCAT(col1, '_', col2))` for large tables, or direct concatenation for small dimensions

### 4.7 HICC Canonical Patterns

These patterns recur across the HICC data warehouse. Chisel them consistently.

**SKU dimension selection** — HICC has three SKU dimension tables; pick the right one:

| Context | Dimension Table | Key Field |
|---------|----------------|-----------|
| Sales (ToC/ToB revenue) | `{{ ref('dim_product_skus_sales') }}` | `sku_id` |
| Inventory (warehouse stock) | `{{ ref('dim_product_skus_warehouse') }}` | `sku_id` (unique by warehouse × channel × sku) |
| Unified mapping (L1→L2→L3) | `{{ ref('dim_hicc_sku_mapping_v2') }}` | `hicc_sku_id` |

**Exchange rate conversion** — always use `dim_exchange_rates.to_usd_rate`:
```sql
COALESCE(er.to_usd_rate, 1) AS to_usd_rate
```
Join on `er.month = DATE_TRUNC(src.event_date, MONTH)` — rates are monthly.

**Timestamp convention**:
- Event time (single source of truth): `event_time_utc` — UTC TIMESTAMP
- Partition field: `event_date_utc` — derived as `DATE(event_time_utc)`
- ETL time: `etl_time` = `CURRENT_TIMESTAMP() + INTERVAL 8 HOUR` — Beijing time

**Domain directory mapping** — model file goes into the domain directory matching the prefix:

| Prefix | Directory | Example |
|--------|-----------|---------|
| `dim_` or `dwd_trd_` | `01_trd/dim/` or `01_trd/dwd/` | `dwd_trd_toc_amazon_order_item_di.sql` → `models/01_trd/dwd/` |
| `dwd_mkt_` | `02_mkt/dwd/` | `dwd_mkt_amazon_sp_daily.sql` → `models/02_mkt/dwd/` |
| `dwd_prd_` | `03_prd/dwd/` | → `models/03_prd/dwd/` |
| `dwd_ful_` | `04_ful/dwd/` | → `models/04_ful/dwd/` |
| `dwd_inv_` | `05_inv/dwd/` | → `models/05_inv/dwd/` |
| `dwd_voc_` | `06_voc/dwd/` | → `models/06_voc/dwd/` |
| `dwd_fnc_` | `07_fnc/dwd/` | → `models/07_fnc/dwd/` |
| `dwd_scm_` | `08_scm/dwd/` | → `models/08_scm/dwd/` |
| `dim_*` (mdm) or `dwd_09_*` | `09_mdm/dim/` | → `models/09_mdm/dim/` |

**Completion criterion**: every field that needs SKU join, exchange rate, or timestamp follows the canonical pattern above. No inline `TO_USD_RATE` expressions — always join `dim_exchange_rates`.

## 5. Data Quality

After the model SQL, chisel the quality checks that prove the model is sound. Generate a companion quality-check block:

```sql
/*
DQ: dwd_trd_toc_order_item_di
  1. Row count.                  Expected: >1000.            Actual: <count>
  2. Null rate unit_price_usd.   Expected: <1%.             Actual: <rate>%
  3. Uniqueness order_item_key.  Expected: 100%.            Actual: <pct>%
  4. Referential integrity.
     - dim_product_skus_sales:   Expected: 100% match.      Actual: <pct>%
  5. Date range.                 Expected: yesterday only.   Actual: <min> ~ <max>
*/
```

Generate the actual SQL for each check — `SELECT COUNT(1)`, `SELECT COUNTIF(col IS NULL)/COUNT(*)`, etc.

**Minimum DQ coverage per model type**:

| Model Type | Required Checks |
|---|---|
| DIM | Uniqueness on key, Non-null on each column |
| DWD | Row count ±30% vs yesterday, Non-null on key columns, Referential integrity to referenced DIMs |
| DWS | Row count ±10% vs yesterday, Non-null on grain, Metric range reasonability |

**Completion criterion**: every check in the coverage matrix above has executable SQL generated. Run it against a representative date range to confirm the SQL is valid. Chisel stops here if any check returns unexpected results.

## 6. dbt Schema (YAML)

Generate a `schema.yml` entry for the model:

```yaml
version: 2

models:
  - name: dwd_trd_toc_order_item_di
    description: "ToC订单行项明细，每日增量"
    columns:
      - name: order_item_key
        description: "订单行项唯一键"
        tests:
          - unique
          - not_null
      - name: order_id
        description: "订单ID"
        tests:
          - not_null
      - name: unit_price_usd
        description: "单价(USD)"
        tests:
          - not_null
```

Cover:
- `unique` + `not_null` on the primary key
- `not_null` on each business key and metric
- `relationships` test on each foreign key referencing a DIM
- `accepted_values` on low-cardinality enum columns
- `dbt_expectations` tests for range (`expect_column_values_to_be_between`)

**Completion criterion**: every column has at least one test. Primary key has `unique` + `not_null`. Every foreign key has a `relationships` test. Chisel the YAML until every constraint from the spec is expressed as a test.

## 7. Backfill Strategy

Given the model's materialization type, declare the backfill plan:

| Materialization | Backfill SQL | Window |
|----------------|-------------|--------|
| `table` | `CREATE OR REPLACE TABLE ... AS SELECT ... WHERE event_date_utc BETWEEN @start AND @end` | Full scan |
| `incremental` (insert_overwrite) | dbt will re-materialize the affected partitions on next run | Affected partition range only |
| `view` | No backfill needed (always live) | N/A |

When the spec changes an existing model's logic:
1. **Rollback plan**: restore the previous version's SQL (`git checkout`) and run `dbt run --select model_name` — this is faster than DDL
2. **Backfill window**: `@start_date` defaults to model creation date; for logic changes, set it to 30 days before the change date
3. **Validation**: after backfill, run the DQ checks from Section 5 and compare row counts against the previous run

**Completion criterion**: the backfill plan specifically addresses the model's materialization type. For logic changes on existing models, both rollback SQL and backfill SQL are declared. Chisel the plan until a reviewer can execute it without asking questions.

---

## DDL Handler (Ticket Type: DDL)

For `DDL` tickets only. Generate the BigQuery DDL statements to create the table. The ticket's "Spec Reference" field points to spec Section 4 (Dimensional Model) for column definitions — map each column's logical type through the **Column type guidelines** below to produce BigQuery physical types.

### DDL Template

```sql
CREATE OR REPLACE TABLE `hiccpet-481303.{dataset}.{table_name}`
(
      {column1} {type} OPTIONS(description='{desc}')
    , {column2} {type} OPTIONS(description='{desc}')
    -- ... all columns from spec Section 4 (Dimensional Model)
)
PARTITION BY {partition_field}
CLUSTER BY {cluster_columns}
OPTIONS(
    partition_expiration_days={expiration_days}
    , description='{table_description}'
);
```

### Rules by Layer

| Layer | Dataset | Partition | Cluster | Expiration |
|-------|---------|-----------|---------|------------|
| DIM | `dim` | None (unless SCD2 with valid_from/valid_to) | Primary key or high-cardinality lookup column | 365 |
| DWD | `dwd` | `DATE(event_time_utc)` or `event_date_utc` | channel_id, country_code, sku_id | 365 |
| DWS | `dws` | `event_date_utc` | channel_id, country_code | 730 |
| ODS (if creating) | `ods_{domain}` | `_PARTITIONDATE` via ingestion time | Ingestion time only | None (raw data retained) |

### Column type guidelines

- **Keys & IDs**: `STRING` (not INT64), to accommodate mixed alphanumeric IDs from different marketplaces
- **Monetary amounts (USD)**: `NUMERIC(18,4)` — precise, not `FLOAT64`
- **Monetary amounts (local currency)**: `NUMERIC(18,2)`
- **Quantities, counts**: `INT64`
- **Ratios, percentages**: `NUMERIC(5,4)` — stored as decimal, not 0-100 percentage
- **Timestamps**: `TIMESTAMP` (not `DATETIME` or `STRING`) — event_time_utc always UTC
- **Dates**: `DATE` — event_date_utc
- **All business columns**: `NULLABLE` by default (do not add `NOT NULL` unless it's a system column like `etl_time`)

### Verification

After DDL execution:
1. Confirm table exists: `SELECT table_name, table_type FROM `region-asia-southeast1`.INFORMATION_SCHEMA.TABLES WHERE table_name = '{name}'`
2. Confirm column count matches spec
3. Confirm partition and cluster settings

**Completion criterion**: DDL script is generated with correct dataset, partition, cluster, and column types per the ticket's spec reference. Chisel the DDL until `CREATE TABLE` executes without error.

---

## VAL Handler (Ticket Type: VAL)

For `VAL` tickets only. Execute the data quality checks from the spec and report results.

### Execution

1. **Read the DQ criteria** from spec Section 7 (Data Quality & Acceptance Criteria)
2. **Generate and run** the SQL checks against BigQuery
3. **Report results** in the ticket output

### Report Format

```markdown
## VAL Results: {model_name}

**Ticket ref**: TICKET-NNN
**Run date**: 2026-09-10
**Environment**: hiccpet-481303

| Check | Expected | Actual | Status |
|-------|----------|--------|--------|
| Row count | >1000 | 1,234,567 | PASS |
| Null rate unit_price_usd | <1% | 0.02% | PASS |
| Uniqueness order_item_key | 100% | 100% | PASS |
| Ref integrity: dim_product_skus_sales | >95% | 99.8% | PASS |
| Date range | yesterday only | 2026-09-09 only | PASS |

**Verdict**: PASS (5/5 checks pass)
```

### Failure handling

- If any check FAILS, include a root cause analysis (e.g. "source ODS has 2% unmatched sku_codes because the ODS table missed yesterday's batch")
- FAIL verdict blocks downstream tickets; mark the blocking dependency in `tickets.md`

**Completion criterion**: every check from the ticket's DQ criteria is executed and reported. PASS → downstream tickets unblocked. FAIL → root cause documented and ticket sent back for rework. Chisel the validation until every check is accounted for.

---

## BACKFILL Handler (Ticket Type: BACKFILL)

For `BACKFILL` tickets only. Generate the backfill execution plan.

### Backfill SQL Generation

Determine the correct backfill SQL based on materialization type:

```sql
-- Full-refresh table
CREATE OR REPLACE TABLE `hiccpet-481303.dwd.{table_name}` AS
SELECT ... FROM {{ ref('upstream') }}
WHERE event_date_utc BETWEEN '{start_date}' AND '{end_date}';

-- Incremental (insert_overwrite)
-- dbt handles this automatically via materialized='incremental'
-- Run: dbt run --select {model_name} --full-refresh

-- Partition-precise incremental backfill
DECLARE target_partitions ARRAY<DATE>;
SET target_partitions = GENERATE_DATE_ARRAY('{start_date}', '{end_date}');
-- Airflow will iterate over partitions
```

### Window Determination

| Scenario | Window | Rationale |
|----------|--------|-----------|
| Greenfield model | `Start of source data` → `today` | Full history needed |
| Logic change (non-breaking) | `30 days before change` → `today` | Quick catch-up + forward consistency |
| Logic change (breaking) | `Start of source data` → `today` | Source data reinterpreted, full refresh required |
| Small model (<1M rows) | Full refresh | Cheaper than incremental logic |

### Validation: 1-Day Overlap Reconciliation

After backfill, run an overlap check to ensure old and new logic are consistent at the seam:

```sql
-- Compare 1-day overlap between old and new backfill boundary
WITH old_data AS (
    SELECT ... FROM `{old_table}`
    WHERE event_date_utc = '{boundary_date}'
), new_data AS (
    SELECT ... FROM `{new_table}`
    WHERE event_date_utc = '{boundary_date}'
)
SELECT
      'row_count' AS check_name
    , (SELECT COUNT(1) FROM old_data) AS old_value
    , (SELECT COUNT(1) FROM new_data) AS new_value
    , ABS((SELECT COUNT(1) FROM old_data) - (SELECT COUNT(1) FROM new_data)) AS diff
UNION ALL
SELECT
      'null_rate_key' AS check_name
    , (SELECT COUNTIF(key IS NULL)/COUNT(*) FROM old_data)
    , (SELECT COUNTIF(key IS NULL)/COUNT(*) FROM new_data)
    , ABS( (SELECT COUNTIF(key IS NULL)/COUNT(*) FROM old_data)
         - (SELECT COUNTIF(key IS NULL)/COUNT(*) FROM new_data) )
```

Pass if: row count diff < 5% AND no new NULLs on key columns (matching ticket acceptance criteria).

### Rollback Plan

Include a one-line rollback command:

```
# Rollback:
git checkout HEAD~1 -- models/{domain}/{model_name}.sql
dbt run --select {model_name}
```

**Completion criterion**: backfill SQL, window, and rollback are declared. The plan is safe to execute without impacting downstream consumers. Chisel the plan until a reviewer can execute it with a single command.

---

## REVIEW Handler (Ticket Type: REVIEW)

For `REVIEW` tickets only. Cross-model reconciliation between DWS and its source DWD.

### Reconciliation Query

Generate a reconciliation query that compares the DWS aggregate against the source DWD:

```sql
WITH dwd_agg AS (
    SELECT
          event_date_utc
        , channel_id
        , SUM(unit_price_usd * quantity) AS gmv_usd
        , COUNT(DISTINCT order_id) AS order_count
    FROM {{ ref('dwd_trd_toc_order_item_di') }}
    WHERE 1=1
        AND event_date_utc >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    GROUP BY 1, 2
)
, dws AS (
    SELECT
          event_date_utc
        , channel_id
        , gmv_usd
        , order_count
    FROM {{ ref('dws_trd_daily_channel_summary') }}
    WHERE event_date_utc >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
)
SELECT
      COALESCE(dwd_agg.event_date_utc, dws.event_date_utc) AS event_date_utc
    , COALESCE(dwd_agg.channel_id, dws.channel_id) AS channel_id
    , dwd_agg.gmv_usd AS dwd_gmv
    , dws.gmv_usd AS dws_gmv
    , ABS(dwd_agg.gmv_usd - dws.gmv_usd) AS gmv_diff
    , CASE WHEN dwd_agg.gmv_usd = 0 THEN NULL
           ELSE ABS(dwd_agg.gmv_usd - dws.gmv_usd) / dwd_agg.gmv_usd * 100
      END AS gmv_diff_pct
    , dwd_agg.order_count AS dwd_orders
    , dws.order_count AS dws_orders
FROM dwd_agg
FULL OUTER JOIN dws
    ON dwd_agg.event_date_utc = dws.event_date_utc
    AND dwd_agg.channel_id = dws.channel_id
ORDER BY 1, 2
```

### Reconciliation criteria

| Metric | Tolerance | Action if exceeded |
|--------|-----------|-------------------|
| GMV difference (per row) | < $0.01 per date×channel row | FAIL: reconciliation broken |
| Row count (date × channel) | 100% match | FAIL: missing rows |
| Max single-row percentage diff | < 5% | PASS; flag for manual review |

### Report format

```markdown
## REVIEW Results: DWS ↔ DWD reconciliation

**Ticket ref**: TICKET-009
**Models**: dws_trd_daily_channel_summary ← dwd_trd_toc_order_item_di
**Window**: last 7 days
**Run date**: 2026-09-10

**Summary**:
- Total rows matched: 35 / 35 (100%)
- GMV max diff: 0.03% (PASS)
- Orders max diff: 0.00% (PASS)

**Verdict**: PASS
```

**Completion criterion**: reconciliation query is generated and executed. Verdict is PASS or FAIL with specific discrepancies listed. Chisel the review until data integrity between layers is quantitatively verified.

---

## Reference Disclosure

When you encounter ambiguous domain-specific patterns or conventions that vary across the codebase, pull from these disclosed sources:

- `hicc-dw` skill (`references/architecture.md`, `cleaning-*.md`, `lineage.md`) — authoritative model registry, cleaning rules, and dependency graph
- `tickets.md` (from `to-ticket-hicc-dw`) — the ticket being implemented; the ticket's "Spec Reference" field points to the relevant sections in `spec.md`
- `spec.md` (from `to-spec-hicc-dw`) — the ultimate source of truth for the model design
- The user's system-level coding rules (top of conversation) — these are always in context and must never be contradicted