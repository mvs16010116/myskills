# 财务域

## 模块结构

| 目录 | 层级 | 说明 |
|------|------|------|
| 财务dwd | DWD | 财务明细层 |
| 财务dws | DWS | 财务汇总层 |

## 执行顺序

```
库存dws → 财务dwd → 财务dws → 数据同步bq2wardyn
```

财务域依赖库存域先执行完成。

## 关键特性

- **汇率计算**: 汇率维度支持小数点后 10 位精度（`dim.dim_exchange_rates.to_usd_rate`）
- **状态标签**: DWS 层状态标签已从中文翻译为英文（`refactor(dws)` 提交）
- **数据映射**: 修复了数据映射问题，优化查询性能
- **多币种**: 支持多币种财务数据，通过汇率表统一换算为 USD

## 财务指标计算规范

所有财务金额通过 `dim.dim_exchange_rates` 关联换算：

```sql
LEFT JOIN dim.dim_exchange_rates AS er
  ON er.from_currency = source.currency_code
  AND er.fdate = DATE_TRUNC(source.date_field, MONTH)
```

汇率精度: **10位小数**（`ROUND(rate / usd_rate_value, 10)`）

## 最近变更

- 2026-07-02: 财务dws — 状态标签中译英
- 2026-06-22: 财务dwd — 修复数据映射问题，优化查询性能

## 代码文件

> 完整路径见 `references/file-index.md`

| 文件名 | GitHub 路径 |
|--------|-------------|
| dwd_fin_import_financial_subject_records.sql | `财务dwd/dwd_fin_import_financial_subject_records.sql` |
| dwd_fin_sps_chewy_rebate.sql | `财务dwd/dwd_fin_sps_chewy_rebate.sql` |
| dwd_sps_invoice_detail.sql | `财务dwd/dwd_sps_invoice_detail.sql` |
| ezzeship_postfee_deal_detail.sql | `财务dwd/ezzeship_postfee_deal_detail.sql` |
| quickbooks发票明细dwd_fin_quickbooks_invoice_allocated_list.sql | `财务dwd/quickbooks发票明细dwd_fin_quickbooks_invoice_allocated_list.sql` |
