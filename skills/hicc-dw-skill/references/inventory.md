# 库存域

最复杂的业务域，包含明细、快照、汇总和预测四个层次。

## 模块结构

| 目录 | 层级 | 说明 |
|------|------|------|
| 库存dwd_快照 | DWD | 库存快照明细 — 执行顺序第一 |
| 库存dwd | DWD | 库存明细 — 依赖快照表 |
| 库存dws | DWS | 库存汇总 — 依赖明细表 |
| 库存预测dwd | DWD | 库存预测明细 — 独立链路 |

## 执行顺序

```
库存dwd_快照 → 库存dwd → 库存dws → 财务dwd → 财务dws
库存预测dwd（独立执行）
```

## 关键特性

- **快照机制**: 独立库存快照表，支持历史时间点追溯
- **FBA 物流**: 处理 FBA 物流方式在连接条件中的匹配问题（`fix(dwd)` 提交）
- **多店铺**: 支持 Walmart 多店铺库存数据
- **预测能力**: 独立的库存预测明细层，用于需求预测
- **SKU 维度**: 依赖 dim_product_skus_warehouse（仓库 SKU 映射）

## 维度依赖

| 维度表 | 用途 |
|--------|------|
| dim.dim_product_skus_warehouse | 库存产品 SKU 仓库映射 |
| dim.dim_warehouse_sku_mapping | 仓库 SKU 映射 |
| dim.dim_shipout_product | 发货产品维度 |

## 最近变更

- 2026-07-02: 库存dwd — Merge 多店铺Walmart + 清理冗余代码
- 2026-06-29: 库存预测dwd — 处理FBA物流方式连接条件匹配问题
- 2026-06-23: 库存dwd_快照 + 库存dws — 支持多店铺Walmart数据

## 代码文件

> 完整路径见 `references/file-index.md`

| 文件名 | GitHub 路径 |
|--------|-------------|
| dwd_lingxing_amazon_seller_sku_list_partition.sql | `库存dwd/dwd_lingxing_amazon_seller_sku_list_partition.sql` |
| dwd_stk_shipout_outbound_detail_shipout出库明细.sql | `库存dwd/dwd_stk_shipout_outbound_detail_shipout出库明细.sql` |
| dwd_stk_walmart_wfs_inventory_partition.sql | `库存dwd/dwd_stk_walmart_wfs_inventory_partition.sql` |
| shipout仓库账单.sql | `库存dwd/shipout仓库账单.sql` |
| shipout明细dwd_scm_shipout_inbound_stock_partition.sql | `库存dwd/shipout明细dwd_scm_shipout_inbound_stock_partition.sql` |
| 亚马逊fba库存_dwd_scm_lingxing_amazon_fba_inventory_partition.sql | `库存dwd/亚马逊fba库存_dwd_scm_lingxing_amazon_fba_inventory_partition.sql` |
| 新加坡手工库存dwd.sql | `库存dwd/新加坡手工库存dwd.sql` |
