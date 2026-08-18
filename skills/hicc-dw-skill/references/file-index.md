# 代码文件索引

> 仓库: HiccTech/hicc_dw_script | 分支: main | 更新时间: 2026-07-06
> GitHub 文件 URL 格式: `https://github.com/HiccTech/hicc_dw_script/blob/main/{目录}/{文件名}`

## 一、dim_维度 — 维度层 (16 个 SQL 文件)

| 序号 | 文件名 | GitHub 路径 |
|------|--------|-------------|
| 1 | dim_campaign.sql | `dim_维度/dim_campaign.sql` |
| 2 | dim_exchange_rate.sql | `dim_维度/dim_exchange_rate.sql` |
| 3 | dim_pur_lingxing_amazon_supplier.sql | `dim_维度/dim_pur_lingxing_amazon_supplier.sql` |
| 4 | dim_shipout_product.sql | `dim_维度/dim_shipout_product.sql` |
| 5 | dim_sku_mapping.sql | `dim_维度/dim_sku_mapping.sql` |
| 6 | dim_warehouse_sku_mapping.sql | `dim_维度/dim_warehouse_sku_mapping.sql` |
| 7 | mapping表销售_dim_import_sku_mapping.sql | `dim_维度/mapping表销售_dim_import_sku_mapping.sql` |
| 8 | 亚马逊account_list.sql | `dim_维度/亚马逊account_list.sql` |
| 9 | 手工表导入商品主数据import_sku_info.sql | `dim_维度/手工表导入商品主数据import_sku_info.sql` |
| 10 | 获取主数据mapping表库存_dim_product_skus_warehouse.sql | `dim_维度/获取主数据mapping表库存_dim_product_skus_warehouse.sql` |
| 11 | 获取主数据mapping表销售_dim_product_skus_sales.sql | `dim_维度/获取主数据mapping表销售_dim_product_skus_sales.sql` |
| 12 | 获取主数据商品信息表_dim_product_skus.sql | `dim_维度/获取主数据商品信息表_dim_product_skus.sql` |
| 13 | 获取主数据商品分类层级加工.sql | `dim_维度/获取主数据商品分类层级加工.sql` |
| 14 | 获取主数据商品采购信息dim_product_skus_purchase.sql | `dim_维度/获取主数据商品采购信息dim_product_skus_purchase.sql` |
| 15 | 领星sb_campaign配置.sql | `dim_维度/领星sb_campaign配置.sql` |
| 16 | 领星采购信息表dim_lingxing_amazon_product_info.sql | `dim_维度/领星采购信息表dim_lingxing_amazon_product_info.sql` |

## 二、销售域

### 销售dwd_2C — 2C销售明细层 (8 个 SQL 文件)

| 序号 | 文件名 | GitHub 路径 |
|------|--------|-------------|
| 1 | dwd_ord_hktvmall_order_details.sql | `销售dwd_2C/dwd_ord_hktvmall_order_details.sql` |
| 2 | dwd_ord_lazada_order_items.sql | `销售dwd_2C/dwd_ord_lazada_order_items.sql` |
| 3 | dwd_ord_lingxing_amazon_api_order_detail_i.sql | `销售dwd_2C/dwd_ord_lingxing_amazon_api_order_detail_i.sql` |
| 4 | dwd_ord_lingxing_amazon_shipment_list.sql | `销售dwd_2C/dwd_ord_lingxing_amazon_shipment_list.sql` |
| 5 | dwd_ord_shopee_order_detail.sql | `销售dwd_2C/dwd_ord_shopee_order_detail.sql` |
| 6 | dwd_ord_tk_order_details.sql | `销售dwd_2C/dwd_ord_tk_order_details.sql` |
| 7 | dwd_ord_walmart_order_detail.sql | `销售dwd_2C/dwd_ord_walmart_order_detail.sql` |
| 8 | 订单明细dwd_ord_shopify_order_line_items.sql | `销售dwd_2C/订单明细dwd_ord_shopify_order_line_items.sql` |

### 销售dwd_2B — 2B销售明细层 (2 个 SQL 文件)

| 序号 | 文件名 | GitHub 路径 |
|------|--------|-------------|
| 1 | dwd_sps_import_b2b_channel_import_po.sql | `销售dwd_2B/dwd_sps_import_b2b_channel_import_po.sql` |
| 2 | dwd_sps_order_detail.sql | `销售dwd_2B/dwd_sps_order_detail.sql` |

### 销售dws — 销售汇总层 (1 个 SQL 文件)

| 序号 | 文件名 | GitHub 路径 |
|------|--------|-------------|
| 1 | dws_ord_shop_channel_sku_orders.sql | `销售dws/dws_ord_shop_channel_sku_orders.sql` |

## 三、广告域

### 广告dwd — 广告明细层 (11 个 SQL 文件)

| 序号 | 文件名 | GitHub 路径 |
|------|--------|-------------|
| 1 | dwd_ads_campaign_product_performance.sql | `广告dwd/dwd_ads_campaign_product_performance.sql` |
| 2 | dwd_ads_chewy_campaign_sidebar.sql | `广告dwd/dwd_ads_chewy_campaign_sidebar.sql` |
| 3 | dwd_ads_chewy_spend.sql | `广告dwd/dwd_ads_chewy_spend.sql` |
| 4 | dwd_ads_petco_spend.sql | `广告dwd/dwd_ads_petco_spend.sql` |
| 5 | dwd_ads_tk_product_item_group_reports.sql | `广告dwd/dwd_ads_tk_product_item_group_reports.sql` |
| 6 | dwd_ads_walmart_compaign_item_performance.sql | `广告dwd/dwd_ads_walmart_compaign_item_performance.sql` |
| 7 | dwd_lazada_adgroup_report_广告.sql | `广告dwd/dwd_lazada_adgroup_report_广告.sql` |
| 8 | dwd_shopee_campaign_daily_performance_广告.sql | `广告dwd/dwd_shopee_campaign_daily_performance_广告.sql` |
| 9 | shopify广告dwd_ads_shopify_ga4_ad_spend.sql | `广告dwd/shopify广告dwd_ads_shopify_ga4_ad_spend.sql` |
| 10 | 亚马逊订单dwd_lingxing_order_profit_msku.sql | `广告dwd/亚马逊订单dwd_lingxing_order_profit_msku.sql` |
| 11 | 关键词表现明细表dwd_ads_keyword_performance.sql | `广告dwd/关键词表现明细表dwd_ads_keyword_performance.sql` |

### 广告dws / 广告dws_分摊

> 待补充完整文件列表（请在 GitHub 仓库中查看 `广告dws/` 和 `广告dws_分摊/` 目录）

## 四、库存域

### 库存dwd — 库存明细层 (7 个 SQL 文件)

| 序号 | 文件名 | GitHub 路径 |
|------|--------|-------------|
| 1 | dwd_lingxing_amazon_seller_sku_list_partition.sql | `库存dwd/dwd_lingxing_amazon_seller_sku_list_partition.sql` |
| 2 | dwd_stk_shipout_outbound_detail_shipout出库明细.sql | `库存dwd/dwd_stk_shipout_outbound_detail_shipout出库明细.sql` |
| 3 | dwd_stk_walmart_wfs_inventory_partition.sql | `库存dwd/dwd_stk_walmart_wfs_inventory_partition.sql` |
| 4 | shipout仓库账单.sql | `库存dwd/shipout仓库账单.sql` |
| 5 | shipout明细dwd_scm_shipout_inbound_stock_partition.sql | `库存dwd/shipout明细dwd_scm_shipout_inbound_stock_partition.sql` |
| 6 | 亚马逊fba库存_dwd_scm_lingxing_amazon_fba_inventory_partition.sql | `库存dwd/亚马逊fba库存_dwd_scm_lingxing_amazon_fba_inventory_partition.sql` |
| 7 | 新加坡手工库存dwd.sql | `库存dwd/新加坡手工库存dwd.sql` |

### 库存dwd_快照 / 库存dws / 库存预测dwd

> 待补充完整文件列表（请在 GitHub 仓库中查看对应目录）

## 五、财务域

### 财务dwd — 财务明细层 (5 个 SQL 文件)

| 序号 | 文件名 | GitHub 路径 |
|------|--------|-------------|
| 1 | dwd_fin_import_financial_subject_records.sql | `财务dwd/dwd_fin_import_financial_subject_records.sql` |
| 2 | dwd_fin_sps_chewy_rebate.sql | `财务dwd/dwd_fin_sps_chewy_rebate.sql` |
| 3 | dwd_sps_invoice_detail.sql | `财务dwd/dwd_sps_invoice_detail.sql` |
| 4 | ezzeship_postfee_deal_detail.sql | `财务dwd/ezzeship_postfee_deal_detail.sql` |
| 5 | quickbooks发票明细dwd_fin_quickbooks_invoice_allocated_list.sql | `财务dwd/quickbooks发票明细dwd_fin_quickbooks_invoice_allocated_list.sql` |

### 财务dws

> 待补充完整文件列表（请在 GitHub 仓库中查看 `财务dws/` 目录）

## 六、退货域

### 退货dwd / 退货dws

> 待补充完整文件列表（请在 GitHub 仓库中查看 `退货dwd/` 和 `退货dws/` 目录）

## 七、数据同步层

### 数据同步bq2wardyn / dw_endflag

> 待补充完整文件列表（请在 GitHub 仓库中查看对应目录）

## 八、根目录非 SQL 文件

| 文件名 | 说明 |
|--------|------|
| .gitignore | Git 忽略规则 |
| Dockerfile | 容器化部署镜像 |
| Makefile.prod | 生产环境 Makefile |
| README.md | 项目说明 |
| auto-update.sh | 自动拉取代码更新脚本 |
| docker-compose.yml | 容器编排配置 |
| hiccpet-481303-f7f2e4edc9ac.json | BigQuery 服务账号密钥 |
| requirements.txt | Python 依赖 |
| write_sync_log.py | 同步日志写入工具 |
| 数仓调度.py | 数据仓库调度主程序 |
| 数据采集和任务运行告警.py | 数据采集与告警 |