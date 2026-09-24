---
name: audit-hicc-dw
disable-model-invocation: false
description: >-
  Inspect 审计 dbt 模型/DDL 质量。Use when user asks to audit, review, check, validate, or
  score a data model. Also when user mentions model quality, Kimball compliance,
  anti-pattern detection, or wants a quality gate before deploy.
---

# audit-hicc-dw — `inspect` 模型质量审计

## Leading Word: `inspect`

> 施工完成后的最后关卡。`inspect` 是在 deploy 之前对模型做一次完整的工程质量检查——
> 就像竣工验收，检查清单逐项核对，不合格的打回重做。

## 审计前置条件

Before inspect a model, confirm the prerequisite artifacts exist:

- [ ] **`spec.md`** (from `to-spec-hicc-dw`) — needed for Kimball compliance check (grain, bus matrix, SCD strategy, surrogate key plan)
- [ ] **`tickets.md`** (from `to-ticket-hicc-dw`) — needed for DAG structure check
- [ ] **Model SQL** (dbt `.sql` file or equivalent) — the actual implementation
- [ ] **DDL SQL** (if a new table) — the physical schema statement
- [ ] **`run_results.json` or `dbt run --select {model}` output** (if available) — for runtime validation

If any artifact is missing, note it in the report as `uncheckable` for relevant dimensions.

## 1. Gather & Parse

Inspect the prerequisites to build an audit context:

```yaml
audit_context:
  model_name: dwd_trd_toc_order_item_di
  domain: 01_trd
  tier: dwd
  grain_from_spec: "one row per order_id × line_item"
  model_type: transaction_fact  # or dimension, periodic_snapshot, cumulative_snapshot
  has_spec: true
  has_ddl: true
```

**Completion criterion**: all present artifacts are parsed into structured fields. Missing artifacts are documented. Proceed with whatever is available — never abort due to missing artifacts; flag them and score from what exists.

## 2. Score Each Dimension

Score the model against 6 audit dimensions. Each dimension is scored **separately** (0-100) and given a **weight** for the composite score.

**Tier-aware scoring**: each dimension has tier-specific checks. The auditor **only applies checks relevant to `audit_context.tier`** (dim / dwd / dws / ods). Checks for other tiers are marked `N/A` and skipped.

### 2.1 Design Correctness (weight: 30%) — 分层特化

> 同一维度对 DIM/DWD/DWS 的衡量标准完全不同。DWS 的核心是「指标即交付」——如果 DWS 模型无法满足 spec Section 6 定义的指标需求，无论 SQL 多规范都是失败的。

#### 2.1a 通用检查（ALL tiers）

| Check | Pass | Fail |
|-------|------|------|
| Grain is declared in the model (`-- Grain:` comment) | +10 | 0 |
| Grain matches the spec's Grain Declaration (Section 3) | +20 | 0 |
| Bus Matrix position is consistent with spec | +10 | 0 |
| Naming follows HICC convention (tier + domain + entity + suffix) | +10 | 0 |

#### 2.1b DWD 特定检查

| Check | Pass | Fail |
|-------|------|------|
| Every FK is classified as `degenerate` or `conformed` | +10 | 0 |
| Degenerate dimensions have no surrogate key (correct by omission) | +5 | 0 |
| SCD2 dimensions have `{entity}_sk`, `effective_date`, `expiration_date`, `is_current` | +15 | 0 |
| Fact references SCD2 dimensions by surrogate key (`sku_sk`), not natural key (`sku_id`) | +10 | 0 |
| DWD granularity is atomic (not aggregated) | +10 | 0 |

#### 2.1c DWS 特定检查（核心：指标交付）

> 这是 DWS 审计最重要的部分。**如果 DWS 无法精准回答业务问题，整个模型就是失败的。**
> 在开始评分前，必须在 spec Section 6（Metric Definitions）中确认哪些指标是这个 DWS 模型负责交付的。

| Check | Pass | Fail |
|-------|------|------|
| All metrics from spec Section 6 designated for this model **exist as columns** | **+25** | 0 |
| Metric formulas match spec (SUM vs COUNT vs DISTINCT, filter conditions applied) | **+20** | 0 |
| Metric unit matches spec (USD vs HKD vs original currency) | +10 | 0 |
| Drill-through path exists (DWS → DWD via identifiable key or ID) | +10 | 0 |
| Time range coverage satisfies query requirements (at least as wide as DWD source) | +10 | 0 |
| Grain correctly supports intended drill-down dimensions (by channel / by seller / by date) | +15 | 0 |

**DWS 关键门槛**: 如果「指标覆盖率」为 0（spec 的指标在 DWS 中找不到），则本维度直接判为 0 分（🔴 Failing），不计算其余检查项。理由是：**数据模型的核心使命是服务业务指标，DWS 层没有这个能力的代价高于一切。**

#### 2.1d DIM 特定检查

| Check | Pass | Fail |
|-------|------|------|
| All key attributes from spec Section 4 are present in the DDL | +15 | 0 |
| SCD strategy declared in spec is correctly implemented | +15 | 0 |
| No overlapping SCD validity ranges (for SCD2 dimensions) | +10 | 0 |
| Surrogate key (`{entity}_sk`) exists for SCD2 dimensions | +15 | 0 |
| Attribute null rates are within spec Section 7 DQ thresholds | +10 | 0 |

**Score mapping per tier**:

| Tier | Available points | Example score | Grade |
|------|----------------|---------------|-------|
| DIM | 40 (通用) + 65 (DIM) = 105 | 85/105 = 81 | Good 🟡 |
| DWD | 40 (通用) + 50 (DWD) = 90 | 80/90 = 89 | Good 🟡 |
| DWS | 40 (通用) + 90 (DWS) = 130 | 120/130 = 92 | Excellent 🟢 |
| ODS | 40 (通用) — no tier-specific | 35/40 = 88 | Good 🟡 |

### 2.2 BigQuery Optimization (weight: 25%)

| Check | Pass | Fail |
|-------|------|------|
| Model has a partition column (`PARTITION BY`) | +20 | 0 |
| Partition column is `DATE` type (not TIMESTAMP — cheaper scans) | +15 | 0 |
| Partition column matches the model's grain (date dimension) | +10 | 0 |
| Cluster columns are specified (`CLUSTER BY`) | +15 | 0 |
| Cluster columns are **filter-appropriate** (high-cardinality filter columns first) | +10 | 0 |
| Column types are optimal (INT64 > STRING for IDs, DATE > TIMESTAMP for dates) | +15 | 0 |
| `partition_expiration_days` is set | +5 | 0 |
| DML uses partition filter (WHERE partition_date = ...) | +10 | 0 |

**BigQuery type optimization rules**:

```
ID/Key fields:
  INT64           ✅ preferred (faster JOIN, smaller storage)
  STRING          ✅ use when business key is alphanumeric
  FLOAT64         ❌ never for IDs — use INT64

Date/Time fields:
  DATE            ✅ for partition columns, date-only values
  TIMESTAMP       ✅ for event times (UTC)
  DATETIME        ❌ avoid — use TIMESTAMP or DATE
  STRING(date)    ❌ never — use proper DATE/TIMESTAMP

Numeric fields:
  NUMERIC(18,4)   ✅ for monetary amounts
  INT64           ✅ for counts, quantities
  FLOAT64         ❌ avoid for money — precision issues
  BIGNUMERIC      ⚠️ only when NUMERIC range is insufficient

String fields:
  STRING          ✅ general purpose
  BYTES           ❌ avoid unless binary data
```

### 2.3 HICC Architecture Consistency (weight: 20%)

**Tier-specific suffix conventions**:

| Tier | Suffix Convention | Examples | Valid |
|------|------------------|---------|-------|
| DIM | `dim_{domain}_{entity}` | `dim_channel`, `dim_product_skus_sales` | ✅ no suffix needed |
| DWD | `dwd_{domain}_{entity}_di` or `_snap` | `dwd_trd_toc_order_item_di`, `dwd_inv_global_detail_v2_snap` | ✅ `_di` / `_snap` |
| DWS | `dws_{domain}_{entity}_{granularity}` | `dws_trd_seller_daily`, `dws_fnc_profitability_monthly` | ✅ granularity suffix (daily/weekly/monthly) |
| ODS | `ods_{source}_{table}` | `ods_shopee_orders`, `ods_winit_inventory` | ✅ source prefix |

| Check | Pass | Fail |
|-------|------|------|
| Dataset matches tier (`dim`, `dwd`, `dws`, `ods`) | +10 | 0 |
| Model name follows `{domain}_{entity}_{suffix}` convention appropriate for its tier | +15 | 0 |
| Suffix follows HICC convention per tier table above | +10 | 0 |
| Domain prefix matches spec Section 1 (e.g. `dwd_trd_*` for trade domain) | +15 | 0 |
| All `{{ source() }}` references point to valid ODS tables | +10 | 0 |
| All `{{ ref() }}` references follow DIM→DWD→DWS direction (no reverse ref) | +15 | 0 |
| DWS references DWD (not ODS directly) — no layer-skipping | +10 | 0 |
| DQ SQL (if present) follows model naming: `val_{model_name}_*.sql` | +15 | 0 |

**Naming rule reference**: 3-tiers are `dwd`, `dws`, `dim`; 9 domains are `trd`, `ad`, `prd`, `scm`, `inv`, `voc`, `fnc`, `pur`, `mds`. See `hicc-dw` for full convention.

### 2.4 SQL Standards Compliance (weight: 10%)

| Check | Pass | Fail |
|-------|------|------|
| `SELECT` lists specific columns — no `SELECT *` | +20 | 0 |
| `WHERE` starts with `1=1` on the same line | +15 | 0 |
| Comma is placed **before** the field (comma-first style) | +15 | 0 |
| `LEFT JOIN` not `JOIN` — all joins are explicit directional | +15 | 0 |
| No implicit cross-join (no comma-separated FROM tables) | +10 | 0 |
| Business key fields allow NULL (no NOT NULL on business columns) | +10 | 0 |
| No ambiguous column references (all column names are prefix-qualified) | +15 | 0 |

### 2.5 Data Quality Readiness (weight: 10%) — 分层特化

> DQ 检查的重点因层而异：DWD 关注完整性和引用关系，DWS 关注指标漂移，DIM 关注属性和版本正确性。

#### 2.5a 通用 DQ 检查（ALL tiers）

| Check | Pass | Fail |
|-------|------|------|
| DQ SQL exists for this model (`val_{model_name}_*.sql` or equivalent) | +15 | 0 |
| DQ includes row count check | +15 | 0 |
| DQ includes null rate check on key columns (PK, business keys) | +15 | 0 |
| DQ thresholds are realistic (e.g. `null_rate < 5%`, not `null_rate = 0`) | +15 | 0 |
| DQ is executable (parameterized for any partition_date) | +10 | 0 |

#### 2.5b DWD/DIM 特定 DQ

| Check | Pass | Fail |
|-------|------|------|
| DQ includes uniqueness check on primary key | +15 | 0 |
| DQ includes referential integrity check (FK → parent table) | +15 | 0 |

#### 2.5c DWS 特定 DQ（核心：指标漂移+口径验证）

| Check | Pass | Fail |
|-------|------|------|
| DQ includes **metric drift detection** (today vs yesterday vs last week same day) | **+20** | 0 |
| DQ includes **max single-row metric value** check (catches outliers/errors) | +10 | 0 |
| DQ includes **ratio comparison** (GMV/order_count — if ratio 10→100 it's suspicious) | +15 | 0 |
| DQ includes **downstream reconciliation** (DWS total vs source DWD total on key metrics) | +15 | 0 |

### 2.6 Anti-Pattern Detection (weight: 5% — penalty-only dimension)

**通用反模式（ALL tiers）**:

| Check | Status | Penalty |
|-------|--------|---------|
| Cartesian join (no JOIN condition or CROSS JOIN without purpose) | Detected / Not detected | -30 |
| N+1 query pattern (dbt query inside a loop) | Detected / Not detected | -20 |
| Same column joined through different paths (ambiguous grain) | Detected / Not detected | -20 |
| SCD2 dimension without surrogate key | Detected / Not detected | -15 |
| Fact table without partition column | Detected / Not detected | -20 |

**跨层陷阱检测（DWD + DWS）**:

| Check | Status | Penalty |
|-------|--------|---------|
| Fan trap detected (N-to-1-to-N chain through same column) | Detected / Not detected | -20 |
| Chasm trap detected (two facts through same dim in one query) | Detected / Not detected | -20 |

**DWS 特定反模式**:

| Check | Status | Penalty |
|-------|--------|---------|
| Dimension over-mapping (aggregating by 10+ dimensions with no filter support) | Detected / Not detected | -15 |
| Metric ratio without both numerator and denominator present (e.g. conversion rate = converted/total — needs both columns) | Detected / Not detected | -15 |
| DWS is identical to DWD (no aggregation, just renamed — wasted layer) | Detected / Not detected | -25 |

**Anti-pattern base score**: 100. Subtract penalty per detected anti-pattern. Minimum: 0.

**Completion criterion**: every applicable check in all 6 dimensions is evaluated. Skipped checks (due to missing artifacts) are listed in the report. Proceed to scoring.

## 3. Compute Composite Score

The composite score uses **tier-specific weights**. DWS models emphasize metric delivery (Design Correctness + DQ Readiness have higher effective weight).

```yaml
# Example: DWS model audit
audit_context:
  tier: dws

dimension_scores:
  design_correctness:   92    weight: 0.30   contribution: 27.6
  bigquery_optimization: 88   weight: 0.25   contribution: 22.0
  hicc_architecture:    85    weight: 0.20   contribution: 17.0
  sql_standards:        95    weight: 0.10   contribution: 9.5
  dq_readiness:         80    weight: 0.10   contribution: 8.0
  anti_pattern:         100   weight: 0.05   contribution: 5.0
  total:                89.1  weight: 1.00

# What this means: DWS model is strong on metric delivery (92)
# and SQL quality (95), but DQ readiness (80) needs improvement
# — specifically metric drift detection is missing.
```

```yaml
# Example: DWD model audit
dimension_scores:
  design_correctness:   85    weight: 0.30   contribution: 25.5
  bigquery_optimization: 92   weight: 0.25   contribution: 23.0
  hicc_architecture:    90    weight: 0.20   contribution: 18.0
  sql_standards:        85    weight: 0.10   contribution: 8.5
  dq_readiness:         70    weight: 0.10   contribution: 7.0
  anti_pattern:         90    weight: 0.05   contribution: 4.5
  total:                86.5  weight: 1.00

# What this means: solid DWD, but missing referential integrity DQ check
```

**DQ readiness score mapping per tier**:

| Tier | Available points | Example score |
|------|----------------|---------------|
| DIM | 70 (通用) + 30 (DWD/DIM DQ) = 100 | 85/100 = 85 |
| DWD | 70 (通用) + 30 (DWD/DIM DQ) = 100 | 75/100 = 75 |
| DWS | 70 (通用) + 60 (DWS DQ) = 130 | 104/130 = 80 |
| ODS | 70 (通用) = 70 | 60/70 = 86 |

**Grade classification**:

| Score | Grade | Meaning | Action |
|-------|-------|---------|--------|
| 90-100 | 🟢 **Excellent** | Ready for deploy | No changes needed |
| 75-89 | 🟡 **Good** | Minor issues | Fix warnings before deploy |
| 60-74 | 🟠 **Needs Work** | Significant issues | Must fix medium+ issues before deploy |
| 0-59 | 🔴 **Failing** | Major redesign needed | Return to implement; major rework required |

**Pass threshold**: composite score ≥ 75 AND no 🔴 (failing) individual dimension. If any dimension scores < 60, the model fails regardless of composite score.

**Completion criterion**: composite score is computed. Each dimension's breakdown is documented. The model gets a pass/fail verdict with actionable next steps.

## 4. Generate Audit Report

Output the audit report in a structured format suitable for both human reading and action tracking.

### Report Template (tier-aware)

The template adapts its dimension names and issue types based on `audit_context.tier`. Below is a **DWS model** example.

```yaml
---
audit_report:
  model: dws_trd_seller_daily
  tier: dws
  auditor: implement-hicc-dw → audit-hicc-dw
  audited_at: "2026-09-11T10:00:00+08:00"
  grade: Good 🟡
  composite_score: 89.1
  pass: true

scores:
  design_correctness:
    score: 92
    weight: "30%"
    grade: Excellent 🟢
    applied_checks: "通用(4) + DWS(6)"
    detail: "6/6 metrics from spec present; 1 formula deviation found"
  bigquery_optimization:
    score: 88
    weight: "25%"
    grade: Good 🟡
    detail: "Missing partition_expiration_days"
  hicc_architecture:
    score: 85
    weight: "20%"
    grade: Good 🟡
    applied_checks: "8 (including DWS-specific layer-skipping check)"
    detail: "DWS correctly references DWD (no layer skip ✅)"
  sql_standards:
    score: 95
    weight: "10%"
    grade: Excellent 🟢
    detail: "All HICC SQL conventions followed"
  data_quality_readiness:
    score: 80
    weight: "10%"
    grade: Good 🟡
    applied_checks: "通用(5) + DWS(4)"
    detail: "Metric drift detection missing; ratio comparison missing"
  anti_pattern_detection:
    score: 100
    weight: "5%"
    grade: Excellent �
    applied_checks: "通用(5) + DWS(3)"
    detail: "No anti-patterns detected"

issues:
  - severity: error
    dimension: design_correctness
    check: "Metric formula matches spec"
    message: >-
      Metric `conversion_rate` is implemented as 
      `COUNT(DISTINCT order_id) / COUNT(session_id)`, 
      but spec says `COUNT(order_id) / COUNT(session_id)`.
      Using DISTINCT deflates the rate for multi-order sessions.
    suggestion: >-
      Change to: `SAFE_DIVIDE(COUNT(order_id), COUNT(session_id))`.
      Backfill: requires 30-day window per spec.

  - severity: warning
    dimension: data_quality_readiness
    check: "DQ includes metric drift detection (DWS)"
    message: "No metric drift detectin in DQ suite."
    suggestion: >-
      Add `val_dws_trd_seller_daily_drift.sql`:
      ```sql
      SELECT
        a.event_date_utc
        , a.gmv_usd
        , b.gmv_usd AS gmv_usd_yesterday
        , ROUND(SAFE_DIVIDE(a.gmv_usd - b.gmv_usd, b.gmv_usd) * 100, 2) AS gmv_drift_pct
      FROM {{ ref('dws_trd_seller_daily') }} a
      LEFT JOIN {{ ref('dws_trd_seller_daily') }} b
        ON a.event_date_utc = DATE_ADD(b.event_date_utc, INTERVAL 1 DAY)
      WHERE ABS(SAFE_DIVIDE(a.gmv_usd - b.gmv_usd, b.gmv_usd)) > 0.30
      ORDER BY a.event_date_utc DESC;
      ```

  - severity: info
    dimension: hicc_architecture
    check: "Suffix follows HICC convention per tier"
    message: >-
      Model name `dws_trd_seller_daily` is correct (dws prefix, daily granularity suffix).

recommendations:
  - priority: high
    action: "Fix conversion_rate formula to match spec"
    effort: "1 hour"
    impact: "Correct metric accuracy — affects all downstream reports"
  - priority: high
    action: "Add metric drift detection DQ check"
    effort: "30 min"
    impact: "Catches data quality regressions before analysts report issues"
  - priority: medium
    action: "Add ratio comparison DQ check"
    effort: "30 min"
    impact: "Detects logic errors in aggregate calculations"
  - priority: low
    action: "Add partition_expiration_days=365"
    effort: "5 min"
    impact: "Reduces storage cost"

summary: |
  Model passes audit with 89.1/100 (Good 🟡).
  Tier: DWS — metric delivery focus.
  1 error (formula deviation) and 1 warning (missing drift DQ) identified.
  2 minor recommendations.
  Fix the formula error before deploy; add drift DQ in the same sprint.
```

**Completion criterion**: the report is complete and actionable — every issue includes a concrete `suggestion`. The model either passes (≥75) with documented minor issues, or fails (<75 or any red dimension) with clear reasons and rework instructions.

## 5. Recommend Next Steps

Based on the audit outcome, provide the appropriate next action:

| Audit Result | Next Step |
|--------------|-----------|
| Pass (Excellent) 🟢 | Proceed to deploy. No changes needed. |
| Pass (Good) 🟡 | Fix warnings before merge. Create fix tickets or fix inline. |
| Fail (Needs Work) 🟠 | Return to `implement-hicc-dw` for the failing dimensions. Re-audit after fixes. |
| Fail (Failing) 🔴 | Return to `to-spec-hicc-dw` for the failing dimensions. Spec may need revision. Then `to-ticket-hicc-dw` → `implement-hicc-dw` → re-audit. |

**Completion criterion**: next steps are documented in the report. If the model failed, the recommended re-entry point (implement or to-spec) is stated. Inspect the report before closing the audit.

## 6. Deliverables

The audit produces two outputs:

```
output/
  ├── audit_{model_name}.yaml   # Machine-readable: scores, issues, verdict
  └── audit_{model_name}.md     # Human-readable: formatted report (this section's output)
```

**Completion criterion**: both files are written. The user can review the `.md` report and, once approved, proceed to deploy or rework.

## External Skill Dependencies

This skill depends on (and does NOT reproduce) the following skills:

- **`hicc-dw`**: HICC table structure, naming conventions, domain prefixes
- **`to-spec-hicc-dw`**: Spec reference (grain, bus matrix, SCD strategy, surrogate key plan)
- **`implement-hicc-dw`**: Implementation reference (SQL patterns, Column Manifest, DDL templates)
- **`bigquery-query`**: Run BigQuery INFORMATION_SCHEMA queries for physical checks (partition size, slot usage)

## Pipeline Position

```
grill → to-spec → to-ticket → implement → audit-hicc-dw → deploy
                                            ↑
                              Final quality gate before release.
                              If failed, return to implement or to-spec.
```