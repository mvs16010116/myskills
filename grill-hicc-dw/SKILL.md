---
name: "grill-hicc-dw"
description: "Stress-test raw data warehouse requirements before spec creation. Invoke when user proposes a new data model, metric, or pipeline, before to-spec-hicc-dw. Runs through business need, data source, model design, cost, and scope challenges."
---

# Grill — HICC Data Warehouse Forge

Heat and hammer raw requirements until only what's solid remains. This is the first gate in the `grill → to-spec → to-ticket → implement` pipeline. Run this before any blueprint is drawn.

**Forge** is the leading word: raw requirements go into the forge. Heat, hammer, quench. Whatever survives is ready for the blueprint. Whatever cracks gets sent back for refinement.

Outcome: a `grill_conclusion.md` with verdict (`PASS` / `REWORK` / `BLOCKED`) and a summary of resolved concerns. If `PASS`, the pipeline proceeds to `to-spec-hicc-dw`.

## 1. Business Need Challenge

Before any data is modelled, challenge the business justification.

1. **Who needs this data?** — name the specific stakeholder, team, or FineBI report. "We might need it someday" is not a valid answer.
2. **What decision does this enable?** — every data model should enable a specific decision (pricing, inventory allocation, ad budget, etc.) If no decision changes, the model has no value.
3. **Why can't an existing model serve this?** — check `hicc-dw` `architecture.md` and `lineage.md` for overlapping models. If the data already exists in a different grain, can the spec just be a DWS aggregation on top of an existing DWD?
4. **How frequent is the query?** — daily dashboard / weekly analysis / one-time deep-dive. One-time queries don't need a new persistent model; a disposable SQL or FineBI dataset is cheaper.
5. **What's the SLA?** — T+0 real-time / T+1 daily / T+7 weekly. Higher SLA means higher cost — is the business case worth it?

**Forge questions** (ask these to the user):
- "这个数据需求对应的业务决策是什么？不做这个模型会有什么影响？"
- "现有的数仓模型（可在 `hicc-dw` architecture.md 中查看）能否满足？如果换个粒度聚合就行，那就只做一个 DWS，不用建 DWD。"
- "谁在什么场景下用这个数据？FineBI 看板还是临时分析？一次性查询不需要建持久表。"

**Completion criterion**: the business need is specific, justified, and cannot be met by an existing model. Forge the need until it's provably necessary.

## 2. Data Source Challenge

If the business need survives, challenge the upstream data.

1. **Source system** — which system provides this data? (Shopee / Lazada / Walmart / Winit / ERP / spreadsheet upload?)
2. **Source reliability** — has this source had data quality incidents in the past 6 months? Check `hicc-dw` `cleaning-*.md` for known issues.
3. **Source schema stability** — do fields change without notice? (common for marketplace APIs) If yes, build field-level schema drift detection into the DWD.
4. **Source availability** — is the data available in BigQuery ODS already? If not:
   - Can the DTS job be added to the existing schedule?
   - Is there a collector script (winit/petco/etc.) already running?
   - If entirely new source, estimate the time to onboard the raw data.
5. **Source completeness** — does the source data have historical depth? From what date is data available? If 0 days of history, no DWD can be backfilled.
6. **Data quality baseline** — pull a sample from the source ODS table:
   - Null rates on key columns
   - Duplicate rates if the grain is known
   - Date range (earliest/latest record)
   - Row count trend (stable / growing / decaying)
   - **Use `hicc-dw` to check existing DQ baselines**: invoke `hicc-dw` with queries like "查询{dim_name}的各字段空值率和行数趋势" to get real figures from BigQuery. Do not rely on guesswork — get the actual null rates and row counts.

**Forge questions**:
- "源数据在哪里？现在 BigQuery ODS 里已经有这张表了吗？调 `hicc-dw` 查一下。没有的话需要先建采集管道，那整个时间线拉长。"
- "源表有哪些已知的脏数据问题？调 `hicc-dw` 查 `cleaning-*.md`，再看具体字段的空值率。"
- "源数据最早可追溯到哪一天？调 `hicc-dw` 查该表的分区范围，如果只有 30 天历史，回刷计划就没意义了。"

**Completion criterion**: every upstream source is identified, available in BigQuery or has a documented onboarding plan, and has a data quality baseline. Forge the data until no unknown unknowns remain.

## 3. Model Design Challenge

With the data confirmed available, challenge the proposed model shape.

**Step 0 — Existing model audit (before grain challenge)**. **Use `hicc-dw` first** to check whether a similar model already exists:
   - `hicc-dw`: "查询{domain}域有哪些 dwd_ 和 dim_ 表"
   - `hicc-dw`: "查{domain}域的 lineage.md，有没有与{proposed_grain}类似的表"
   - If a model with the same grain already exists, the question becomes: "为什么不能复用已有的表？" rather than "怎么建新表？"

**Step 1 — Grain challenge**. The grain must be atomic and provable:
   - Can you produce one sample row from source data that matches this grain?
   - Is the grain truly atomic or is it already an aggregation? (an "order + line item" grain must explode 1 order with 3 line items into 3 rows)
   - Could the grain be coarser and still answer the business question? (Daily totals instead of per-order? Fewer dimensions?)
**Step 2 — SCD strategy challenge**. If this is a dimension:
   - Does the attribute change over time? (yes → SCD2, no → SCD1)
   - If SCD2, does the business need historical point-in-time lookups? (yes → keep SCD2, no → save cost with SCD1)

**Step 3 — Dimensional model challenge**. Is every measure truly additive?
   - Semi-additive measures (e.g. inventory snapshot at a point in time) need special handling — SUM across time doesn't work
   - Non-additive measures (e.g. ratios, percentages) need separate logic

**Step 4 — HICC convention check**. Does the proposed model follow existing naming conventions? (`dwd_{domain}_{entity}_{granularity}.sql`, `_di` for daily incremental, `_snap` for snapshot, `dim_` for dimensions)

**Forge questions**:
- "调 `hicc-dw` 查一下这个域有没有同类模型？如果有了为什么还要新建？"
- "这个粒度能直接从源数据还原吗？给我一条样例数据看看。"
- "这个维度用 SCD1 够吗？业务方真的需要查历史某个时间点的属性吗？调 `hicc-dw` 查类似维度表的 SCD 策略参考。SCD2 会翻倍行数。"
- "这个度量是加法度量还是半加法？库存快照用 SUM 是错的，需要特殊处理。"

**Completion criterion**: the grain is provable from source data, the SCD strategy is justified, and all measures are correctly categorized. Forge the model shape until no design ambiguity remains.

## 4. Cost & Performance Challenge

Data warehouse design is a cost trade-off. Challenge the model's cost impact.

1. **Storage cost** — estimate the storage cost:
   - `row_count * avg_row_bytes * 5 USD/TB/month`
   - For incremental models: multiply by retention days (365 for DWD, 730 for DWS)
   - **Use `hicc-dw` for real numbers**: invoke `hicc-dw` with "查询{similar_table}的 __TABLES__ 信息" to get actual row count, logical bytes, and partition range from BigQuery. Do not estimate from thin air — anchor on existing similar tables.
2. **Query cost** — estimate the query cost for the top 3 query patterns:
   - `bytes_processed * 5 USD/TB` per query
   - If the model supports FineBI dashboard queries scanned daily, multiply by query frequency
3. **Partition vs no partition** — if the model is <100GB and queried infrequently, skip partitioning entirely (table scans are cheaper than partition management overhead for small tables)
4. **Cluster vs no cluster** — cluster only if >1GB/partition or queries filter on specific columns. Clustering on low-cardinality columns (e.g. `is_deleted: 0/1`) has negligible benefit.
5. **Cost vs benefit** — is the business value of this model worth the estimated cost? If not, can the model be:
   - Aggregated to a coarser grain (fewer rows)?
   - Filtered to only the last N days?
   - Replaced by a view over the source ODS (zero storage cost)?

**Forge questions**:
- "这个模型一年大概存多少钱？每个月查询扫描多少 GB？调 `hicc-dw` 查一下同类表的大小做参考。算过吗？"
- "如果用户只想看近 7 天的数据，有没有必要存 365 天？"
- "这个模型小于 100GB 的话，不分区直接全表扫描可能更便宜。"
- "这个查询需求能不能直接用 FineBI 查 ODS 源表代替？零存储成本。"

**Completion criterion**: every model has an estimated storage and query cost. The cost is justified by the business value. If cost > value, forge a cheaper alternative. If no cheaper alternative exists, document the cost as known and accepted.

## 5. Scope & Timeline Challenge

Once the model is designed, challenge the delivery scope.

1. **Minimum viable model** — what's the smallest subset of this model that delivers business value?
   - Fewer columns? (drop any column not used in a known query)
   - Fewer historical data? (start with 90 days, extend later)
   - Partial dimensions? (use surrogate 0 for unmatched, defer dimension cleanup)
2. **Blocking dependencies** — what must exist before this model can be built?
   - ODS tables populated? (if no, the collector/DTS ticket is the true P0)
   - DIM tables built? (if yes, they must be built first — check topological order)
3. **Backfill scope** — if this is a modification:
   - How much history needs backfill?
   - Can the backfill run incrementally (1 day at a time) or must it be a single full refresh?
   - What's the expected row count and estimated BigQuery slot wall-clock time?
4. **Rollback plan** — before building, define the exit criteria:
   - If this model causes upstream failures, what's the rollback? (disable dbt model, delete table, restore git)
   - How long to recovery? (git revert + dbt run)

**Forge questions**:
- "第一个版本能不能只做 10 个核心字段？剩下 5 个字段之后再补。"
- "这个模型需要哪些上游表先建好？我们的 DIM 就绪了吗？"
- "如果做完了发现数据不对，回滚要多久？"

**Completion criterion**: the scope has a clear MVP boundary, blocking dependencies are identified and scheduled, and a rollback plan exists. Forge the scope until it's deliverable within a known timeframe.

## 6. Potential Pitfalls Challenge

Surface known failure modes for this type of model.

| Pitfall | Check |
|---------|-------|
| `JSONDecodeError` from third-party API | Is the collector already reliable for this source? |
| Schema drift | Does the upstream API add/remove fields without notice? |
| Late-arriving data | Can source data arrive with a 2-day delay? Does the model handle reprocessing? |
| Duplicate records | Does the source have known duplicates at the proposed grain? |
| Currency fluctuation | If this model uses exchange rates, does a rate change mid-month break batch consistency? |
| Marketplace ID change | If a Shopee shop changes its marketplace, does the model break historical continuity? |
| Timezone ambiguity | Does the source use UTC, local time, store time, or a mix? |

Check each against `hicc-dw` `lineage.md` and Airflow DAG history (known failure patterns).

**Forge questions**:
- "这个上游在过去有没有出现过数据延迟或格式变化？查一下 cleaning-*.md。"
- "如果今天的数据后天早上才到齐，这个模型会怎样？业务方能接受吗？"
- "同一个粒度的记录有可能重复吗？去重逻辑是什么？"

**Completion criterion**: every pitfall relevant to the proposed model is assessed and documented. Acceptable pitfalls are noted as known risks. Unacceptable pitfalls must be resolved before proceeding.

## 7. Forge Verdict

Summarize the grill outcome in a single verdict:

```markdown
## Grill Conclusion

**Verdict**: PASS / REWORK / BLOCKED

**Metadata**:
- Domain: 01_trd
- Proposed model(s): dwd_trd_toc_order_item_di, dws_trd_daily_channel_summary
- Estimated rows: ~1M/day
- Estimated storage cost: ~$3/month
- Estimated query cost/month: ~$1
- Grill date: 2026-09-10

**Resolved Concerns**:
1. (PASS) Business need: confirmed by operations team, for daily channel P&L tracking
2. (PASS) Data source: ODS shopee_orders available since 2024-01, null rate <0.1% on key columns
3. (PASS) Grain: one row per order_id × line_item, provable from source
4. (PASS) Cost: $4/month total, justified by daily executive dashboard usage

**Open Risks**:
1. (ACCEPTED) Source schema may drift on product category restructuring — last occurred 2025-08
2. (MITIGATED) Late-arriving data: model runs at T+4, covers 99.9% of data arrival

**Next Step**: proceed to `to-spec-hicc-dw`
```

Verdict options:
- **PASS** — all concerns are resolved or accepted. Proceed to `to-spec-hicc-dw`.
- **REWORK** — requirements need clarification or scope needs adjustment. List what must be reworked before next grill.
- **BLOCKED** — a hard dependency is missing (upstream data not available, no collector, key decision pending). Blocked items must be resolved before re-grilling.

**Completion criterion**: the verdict is delivered with supporting evidence. If PASS, the pipeline continues to `to-spec-hicc-dw`. If REWORK or BLOCKED, the user receives actionable feedback. Forge the requirements until the verdict is PASS or the user agrees to abort.

## Reference Disclosure

- `hicc-dw` skill (`architecture.md`, `cleaning-*.md`, `lineage.md`, `finebi.md`) — authoritative references for existing models, known data quality issues, and query patterns
- `to-spec-hicc-dw` — the downstream consumer; grill findings flow into the spec as constraints and accepted decisions
- Previous grill conclusions in this repo (if any) — avoid re-grilling settled questions