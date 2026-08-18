---
name: "bigquery-query"
description: "Execute Google BigQuery SQL queries via bq CLI. Invoke when user asks to query data, run SQL, check metrics, or inspect BigQuery tables in the hiccpet-481303 project."
---

# BigQuery Query Skill

This skill enables executing Google BigQuery SQL queries using the `bq` command-line tool, pre-configured for the HICC PET data warehouse project (`hiccpet-481303`).

## When to Invoke

- User asks to query data from BigQuery
- User asks for metrics, counts, sums, aggregations (sales, inventory, ad spend, etc.)
- User asks to check table data, structure, or sample rows
- User asks to verify ETL results or data freshness
- Any question that requires running SQL against BigQuery

## Prerequisites

- Google Cloud SDK (`gcloud`/`bq`) must be installed and authenticated
- Python is at `D:/Program_Files/miniconda/python.exe`
- Must set `CLOUDSDK_PYTHON` environment variable before running bq commands (Windows Git Bash environment)

## Query Execution

### Environment Setup

Always prefix bq commands with the Python path:

```bash
CLOUDSDK_PYTHON="D:/Program_Files/miniconda/python.exe" bq query --use_legacy_sql=false --format=pretty "<SQL>"
```

### Query Best Practices

1. **Always use Standard SQL**: `--use_legacy_sql=false`
2. **Format output**: Use `--format=pretty` for human-readable results
3. **Project ID**: Default project is `hiccpet-481303`; always use fully qualified table names: `` `project.dataset.table` ``
4. **Timezone**: The ETL uses Asia/Shanghai (UTC+8). `CURRENT_TIMESTAMP() + INTERVAL 8 HOUR` is used for etl_time.
5. **Currency**: Sales amounts in DWS layer are already in USD via `dim.dim_exchange_rates`.
6. **Date filters**: Use half-open intervals for date ranges: `fdate >= 'YYYY-MM-DD' AND fdate < 'YYYY-MM-DD'`

### Common Query Patterns

#### Count rows / check data freshness
```sql
SELECT MIN(fdate) AS min_date, MAX(fdate) AS max_date, COUNT(*) AS row_count
FROM `hiccpet-481303.<dataset>.<table>`
WHERE fdate >= 'YYYY-MM-DD'
```

#### Sum metrics (e.g., sales)
```sql
SELECT ROUND(SUM(amount_field), 2) AS total_usd, COUNT(*) AS rows
FROM `hiccpet-481303.<dataset>.<table>`
WHERE fdate >= 'YYYY-MM-DD' AND fdate < 'YYYY-MM-DD'
  AND <dimension filters>
```

#### Group by dimension
```sql
SELECT <dim_field>, ROUND(SUM(amount_field), 2) AS total_usd
FROM `hiccpet-481303.<dataset>.<table>`
WHERE fdate >= 'YYYY-MM-DD' AND fdate < 'YYYY-MM-DD'
GROUP BY <dim_field>
ORDER BY total_usd DESC
```

#### Check table structure (schema)
```bash
CLOUDSDK_PYTHON="D:/Program_Files/miniconda/python.exe" bq show --schema --format=pretty hiccpet-481303:<dataset>.<table>
```

#### Preview sample rows
```bash
CLOUDSDK_PYTHON="D:/Program_Files/miniconda/python.exe" bq head -n 10 --format=pretty hiccpet-481303:<dataset>.<table>
```

## Key Tables Reference (HICC PET DW)

Based on the hicc-dw knowledge base:

| Domain | Table | Description |
|--------|-------|-------------|
| Sales 2C | `dws.dws_ord_shop_channel_sku_orders` | 2C sales summary (all channels, USD) |
| Sales 2B | `dwd.dwd_sps_import_b2b_channel_import_po` | 2B PO summary (USD) |
| Ads | `dws.dws_ads_tot` | All-channel ad spend summary (USD) |
| SKU Mapping | `dim.dim_import_sku_mapping` | Channel SKU → HICC SKU mapping |
| Exchange Rates | `dim.dim_exchange_rates` | Monthly FX rates to USD |
| Inventory | `dws.dwd_scm_warehouse_available_transit_detail` | Available + in-transit inventory |

### Channel Codes (`dim_channel_code`)

| Code | Channel |
|------|---------|
| p001 | Amazon |
| p002 | Walmart |
| p006 | Lazada |
| p007 | Shopee |
| p008 | HKTVmall |
| p009 | TikTok Shop |
| p010 | Shopify |
| p012 | ShowRoom SG |
| p017 | Chewy |

## Important Data Conventions

1. **2C Sales cancellation rule**: An order line is canceled if `cancel_date IS NOT NULL AND cancel_date` falls within the reporting period. Filter: `(cancel_date IS NULL OR cancel_date >= <period_end>)`
2. **Amazon DWD quirk**: `dwd.dwd_ord_lingxing_amazon_api_order_detail_i` already filters out `order_status = 'Canceled'` at source, so cancel_date is always NULL for Amazon rows in DWS.
3. **Amounts in DWS**: Already converted to USD via `item_price_amount * to_usd_rate`. Do NOT apply FX again.
4. **Date fields**:
   - `fdate`: local date of the channel
   - `fdate_cn`: date in Asia/Shanghai timezone
   - Use `fdate` for standard reporting unless user specifies CN timezone

## Error Handling

- If `bq` reports `python3.12: command not found`, ensure `CLOUDSDK_PYTHON` is set to the miniconda path above.
- If authentication fails, suggest user run `gcloud auth application-default login` first.
- If query returns 0 rows, verify date range and table name; check data freshness first with a MIN/MAX date query.

## Example Workflow

When user asks "What is X metric for period Y?":
1. Identify the correct table using the hicc-dw skill (sales.md, ads.md, etc.)
2. Construct SQL with appropriate filters (date, channel, etc.)
3. Execute via RunCommand with `CLOUDSDK_PYTHON` prefix
4. Present results with clear metric labels, currency (USD), and data date range caveats
