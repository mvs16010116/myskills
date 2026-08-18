# 数据分层架构

## 全量表清单

### DIM 维度层 (dim 数据集)

| 表名 | 源文件 | 关键字段 | 说明 |
|------|--------|---------|------|
| dim.dim_exchange_rates | dim_exchange_rate.sql | fdate, from_currency, to_usd_rate, rate, data_source | 月度汇率，精度10位小数，含本月模拟 |
| dim.dim_campaign | dim_campaign.sql | — | 广告活动维度 |
| dim.dim_sku_mapping | dim_sku_mapping.sql | — | SKU 映射表 |
| dim.dim_warehouse_sku_mapping | dim_warehouse_sku_mapping.sql | — | 仓库 SKU 映射 |
| dim.dim_product_skus | 获取主数据商品信息表_dim_product_skus.sql | — | 商品 SKU 信息（含分类层级） |
| dim.dim_product_skus_warehouse | 获取主数据mapping表库存_dim_product_skus_warehouse.sql | — | 库存产品 SKU 仓库映射 |
| dim.dim_product_skus_sales | 获取主数据mapping表销售_dim_product_skus_sales.sql | — | 销售产品 SKU 映射 |
| dim.dim_product_skus_purchase | 获取主数据商品采购信息dim_product_skus_purchase.sql | — | 商品采购信息（渠道/地区） |
| dim.dim_product_category | 获取主数据商品分类层级加工.sql | — | 商品分类层级 |
| dim.dim_import_sku_mapping | mapping表销售_dim_import_sku_mapping.sql | — | 销售导入 SKU 映射 |
| dim.dim_shipout_product | dim_shipout_product.sql | — | 发货产品维度 |
| dim.dim_lingxing_amazon_product_info | 领星采购信息表dim_lingxing_amazon_product_info.sql | — | 领星产品维度 |
| dim.dim_pur_lingxing_amazon_supplier | dim_pur_lingxing_amazon_supplier.sql | — | 领星亚马逊供应商 |
| dim.dim_lingxing_sb_campaign | 领星sb_campaign配置.sql | — | 领星 SB 广告配置 |
| dim.dim_amazon_account | 亚马逊account_list.sql | — | 亚马逊账户列表 |
| — | 手工表导入商品主数据import_sku_info.sql | — | 商品主数据导入（含分类字段、来源优先级） |

### DWD 明细层 (dwd 数据集)

| 表名 | 目录 | 说明 |
|------|------|------|
| dwd.dwd_sps_order_detail | 销售dwd_2B | 2B 销售明细（SPS 渠道） |
| dwd.dwd_sps_import_b2b_channel_import_po | 销售dwd_2B | 2B B2B PO 汇总（HK+SG） |
| 多个 2C 渠道表 | 销售dwd_2C | Amazon/Walmart/Shopify/Shopee/Lazada/TikTok/HKTVmall/ShowRoom |
| — | 广告dwd | 广告投放明细 |
| — | 库存dwd | 库存明细 |
| — | 库存dwd_快照 | 库存快照明细（多店铺Walmart） |
| — | 库存预测dwd | 库存预测明细 |
| — | 财务dwd | 财务明细 |
| — | 退货dwd | 退货明细 |

### DWS 汇总层 (dws 数据集)

| 表名 | 目录 | 说明 |
|------|------|------|
| dws.dws_ord_shop_channel_sku_orders | 销售dws | 2C 销售汇总（8渠道 UNION ALL） |
| dwd.dwd_sps_import_b2b_channel_import_po | 销售dwd_2B | 2B 销售汇总（命名前缀为dwd但实际是汇总层） |
| — | 广告dws | 广告汇总 |
| — | 广告dws_分摊 | 广告费用分摊汇总 |
| — | 库存dws | 库存汇总 |
| — | 财务dws | 财务汇总 |
| — | 退货dws | 退货汇总 |

### 数据同步层

| 表名 | 目录 | 说明 |
|------|------|------|
| — | 数据同步bq2wardyn | BigQuery → WarDyn 同步 |
| — | dw_endflag | 数据仓库执行结束标志 |

## 执行链路（依赖顺序）

```
1. dim_维度（全部 16 个维度表）
2. 销售dwd_2C（依赖 dim_维度）
3. 广告dwd（依赖 dim_维度 + 销售dwd_2C）
4. 广告dws_分摊（依赖 广告dwd）
5. 广告dws（依赖 广告dws_分摊）
6. 销售dwd_2B（依赖 dim_维度）
7. 销售dws（依赖 销售dwd_2C + 销售dwd_2B）
8. 退货dwd（依赖 dim_维度）
9. 退货dws（依赖 退货dwd）
10. 库存dwd_快照（依赖 dim_维度）
11. 库存dwd（依赖 库存dwd_快照）
12. 库存dws（依赖 库存dwd）
13. 财务dwd（依赖 dim_维度）
14. 财务dws（依赖 财务dwd）
15. 数据同步bq2wardyn（依赖全部 DWS 层）
16. dw_endflag（依赖 数据同步bq2wardyn）
```

## 调度策略

- 完整运行链路按上述顺序串行执行
- 支持单独执行某个模块（简化链路）
- 通过 `dw_endflag` 表标记执行完成状态

## 数据源

- **ODS 层**: ods 数据集，包含原始业务数据
  - ods.exchange_rates: 外汇官方数据
  - ods.import_b2b_channel_hk_po_main: HK B2B PO 主表
  - ods.import_b2b_channel_sg_po: SG B2B PO
  - ods.import_sps_hk_*: HK SPS 手工导入数据
  - ods.import_dim_sps_vendor: SPS 供应商维度

## 代码文件

> 完整 SQL 文件清单见 `references/file-index.md`，包含所有 16 个目录的完整文件路径。
> GitHub 文件直链: `https://github.com/HiccTech/hicc_dw_script/blob/main/{目录}/{文件名}`
