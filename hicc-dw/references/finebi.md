# FineBI 定义目录分析报告：指标→模型→表→字段 引用关系

> 分析范围：`d:\PycharmProjects\dw\hicc_dw_script\finebi_dev\definitions\` 下全部 yaml 文件
> 文件类型：`metrics`（指标）、`models`（模型）、`tables`（数据表/视图）、`dimensions`（维度）
> 生成日期：2026-09-09

## 目录

1. [指标→表→字段映射表（按业务域分组）](#一指标表字段映射表按业务域分组)
2. [模型→表关联结构](#二模型表关联结构)
3. [重点业务域细表（05_库存与周转 / 01_交易与销售）](#三重点业务域细表)

---

## 一、指标→表→字段映射表（按业务域分组）

**说明**
- 表达式为 `表.字段` 形式 ⇒ 直接引用底层表字段；表达式为 `指标名` 运算 ⇒ 公式型指标（引用其他指标，需继续向下钻取到表字段）。
- "所属模型"列：指标 yaml 本身不声明模型，此处按"指标引用的表 ∈ 模型 tables 列表"推断（若指标引用的表未出现在任何模型 tables 中则标记为 `-`）。

### 00_未分类（6 个指标）

| 指标名称 | 表达式 | 聚合 | 口径描述 | 引用表.字段 | 所属模型(推断) |
|---|---|---|---|---|---|
| 净销售额 | `SUM_AGG(dwd_trd_toc_amazon_order_item_di.order_total_amount) - SUM_AGG(dwd_trd_toc_amazon_order_item_di.itemlist_tax_amount)` | true | 按订单维度汇总订单总金额并扣除订单明细税费后的净销售收入 | dwd_trd_toc_amazon_order_item_di.order_total_amount / itemlist_tax_amount | - |
| 净销v2.1 | `SUM_AGG(dwd_trd_toc_amazon_order_item_di.order_total_amount) - SUM_AGG(dwd_trd_toc_amazon_order_item_di.itemlist_tax_amount)` | true | 净销售额 v2.1 口径，按订单维度总金额扣除订单明细税费 | dwd_trd_toc_amazon_order_item_di.order_total_amount / itemlist_tax_amount | - |
| 总销售额 | `SUM_AGG(dwd_trd_toc_amazon_order_item_di.order_total_amount)` | true | 订单维度商品销售总额 GMV，未扣减税费与退款 | dwd_trd_toc_amazon_order_item_di.order_total_amount | - |
| 测试指标 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.paid_amount_usd)` | true | 测试指标，订单商品维度支付金额汇总 | dws_trd_channel_sku_sales_di_order.paid_amount_usd | 订单_ToC_商品_交易模型 |
| 测试_净销售额 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.paid_amount_usd) - SUM_AGG(dws_trd_channel_sku_sales_di_order.paid_amount_usd_cancel)` | true | 测试指标，订单商品支付金额扣除取消支付金额后的净销售额 | dws_trd_channel_sku_sales_di_order.paid_amount_usd / paid_amount_usd_cancel | 订单_ToC_商品_交易模型 |
| 测试_净销售额_v2 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.paid_amount_usd) - SUM_AGG(dws_trd_channel_sku_sales_di_order.paid_amount_usd_cancel)` | true | 测试指标 v2，订单商品支付金额扣除取消支付金额后的净销售额 | dws_trd_channel_sku_sales_di_order.paid_amount_usd / paid_amount_usd_cancel | 订单_ToC_商品_交易模型 |

### 01_交易与销售（17 个指标）

| 指标名称 | 表达式 | 聚合 | 口径描述 | 引用表.字段 | 所属模型(推断) |
|---|---|---|---|---|---|
| ToC销售额 | `ToC订单支付金额 - ToC取消订单销售额`（公式） | true | - | → ToC订单支付金额 / ToC取消订单销售额 | - |
| ToC订单支付金额 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.paid_amount_usd)` | true | GMV，包含退款订单金额，单位美元 | dws_trd_channel_sku_sales_di_order.paid_amount_usd | 订单_ToC_商品_交易模型 |
| ToC取消订单销售额 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.paid_amount_usd_cancel)` | true | 已支付订单中被取消订单的总金额，统计时间为取消时间 | dws_trd_channel_sku_sales_di_order.paid_amount_usd_cancel | 订单_ToC_商品_交易模型 |
| ToC销量 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.quantity_ordered) - SUM_AGG(dws_trd_channel_sku_sales_di_order.quantity_ordered_cancel)` | true | ToC 所有平台（Amazon/Tiktok/Shopee/Lazada/Shopify），默认 bundle 维度 | dws_trd_channel_sku_sales_di_order.quantity_ordered / quantity_ordered_cancel | 订单_ToC_商品_交易模型 |
| ToC取消订单销量 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.bundle_quantity_cancel)` | true | 已支付订单中被取消的订单商品总数量，统计时间为取消时间 | dws_trd_channel_sku_sales_di_order.bundle_quantity_cancel | 订单_ToC_商品_交易模型 |
| TOC单品销量 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.bundle_quantity) - SUM_AGG(dws_trd_channel_sku_sales_di_order.bundle_quantity_cancel)` | true | - | dws_trd_channel_sku_sales_di_order.bundle_quantity / bundle_quantity_cancel | 订单_ToC_商品_交易模型 |
| 单品销量 | `ToB销量 + SUM_AGG(dws_trd_channel_sku_sales_di_order.bundle_quantity) - SUM_AGG(dws_trd_channel_sku_sales_di_order.bundle_quantity_cancel)`（公式+表） | true | 订单销量一致，包含 ToB + ToC | dws_trd_channel_sku_sales_di_order.bundle_quantity / bundle_quantity_cancel；→ToB销量 | 订单_ToC_商品_交易模型 |
| 销量 | `SUM_AGG(dws_trd_channel_sku_sales_di_order.quantity_ordered) - SUM_AGG(dws_trd_channel_sku_sales_di_order.quantity_ordered_cancel) + SUM_AGG(dwd_scm_sps_po_detail_di_tob.Qty_Ordered)` | true | 总销量，含 ToB + ToC 所有平台；1 个 bundle 的销量 = 套装内部 N 个单品销量 | dws_trd_channel_sku_sales_di_order.quantity_ordered / quantity_ordered_cancel；dwd_scm_sps_po_detail_di_tob.Qty_Ordered | 订单_ToC_商品_交易模型 / 订单_ToB_商品_交易模型 |
| 销售额 | `ToB销售额 + ToC销售额`（公式） | true | 总销售额，包括 ToB、ToC 所有平台 | → ToB销售额 / ToC销售额 | - |
| ToB销售额 | `SUM_AGG(dwd_scm_sps_po_detail_di_tob.tot_amount)` | true | ToB 销售额（SPS 系统） | dwd_scm_sps_po_detail_di_tob.tot_amount | 订单_ToB_商品_交易模型 |
| ToB销量 | `SUM_AGG(dwd_scm_sps_po_detail_di_tob.Qty_Ordered)` | true | ToB 销量（SPS 系统） | dwd_scm_sps_po_detail_di_tob.Qty_Ordered | 订单_ToB_商品_交易模型 |
| 沃尔玛销售额 | `SUM_AGG(dwd_trd_toc_walmart_order_item_di_walmart.charge_amount)` | true | - | dwd_trd_toc_walmart_order_item_di_walmart.charge_amount | 沃尔玛订单明细 |
| 目标销售额 | `SUM_AGG(dim_sell_target.sales)` | true | 口径：目标销售额（销售目标表中的目标销售额） | dim_sell_target.sales | 销售目标表 |
| 近7天销量 | ``（空，报表端按时间窗口过滤） | true | 口径：近7天日销量（近7天销量总和，不含取消订单） | - | - |
| 近7天日均销量 | `近7天销量 / 7`（公式） | true | 口径：近7天平均销量（不含取消订单，合并 ToC 多渠道销量和 ToB 销量） | → 近7天销量 | - |
| ToC退货金额 | `SUM_AGG(dws_voc_global_return_di.return_amount)` | true | 口径：ToC退货金额（汇总 ToC 各平台退货金额） | dws_voc_global_return_di.return_amount | 退货汇总表 |
| ToC退货数量 | `SUM_AGG(dws_voc_global_return_di.return_quantity)` | true | 口径：ToC退货数量（汇总 ToC 各平台退货数量） | dws_voc_global_return_di.return_quantity | 退货汇总表 |

### 02_营销与流量（33 个指标）

| 指标名称 | 表达式 | 聚合 | 引用表.字段 | 所属模型(推断) |
|---|---|---|---|---|
| 广告花费 | `ToC广告花费 + ToB广告花费`（公式） | true | → ToC广告花费 / ToB广告花费 | - |
| ToC广告花费 | `SUM_AGG(dws_mkt_global_ad_spend_di.spend_usd)` | true | dws_mkt_global_ad_spend_di.spend_usd | 广告事实模型 |
| ToB广告花费 | `ToB广告花费_chewy + ToB广告话费_petco`（公式） | true | → 子指标 | - |
| ToB广告花费_chewy | `SUM_AGG(dwd_mkt_chewy_ad_spend_di.spend)` | true | dwd_mkt_chewy_ad_spend_di.spend | 广告事实模型 / 维度模型表 |
| ToB广告话费_petco | `SUM_AGG(dwd_mkt_petco_ad_spend_di.spend)` | true | dwd_mkt_petco_ad_spend_di.spend | 广告事实模型 / 维度模型表 |
| spend | `dwd_mkt_campaign_product_perf_di.spend` | false | dwd_mkt_campaign_product_perf_di.spend | campaign表现 |
| 广告直接销售额 | `dwd_mkt_campaign_product_perf_di.direct_sales` | false | dwd_mkt_campaign_product_perf_di.direct_sales | campaign表现 |
| 广告订单数 | `dwd_mkt_campaign_product_perf_di.total_orders` | false | dwd_mkt_campaign_product_perf_di.total_orders | campaign表现 |
| 曝光量 | `dwd_mkt_campaign_product_perf_di.impressions` | false | dwd_mkt_campaign_product_perf_di.impressions | campaign表现 |
| 点击量 | `dwd_mkt_campaign_product_perf_di.clicks` | false | dwd_mkt_campaign_product_perf_di.clicks | campaign表现 |
| 自动订阅数 | `dwd_mkt_campaign_product_perf_di.autoship_subscriptions` | false | dwd_mkt_campaign_product_perf_di.autoship_subscriptions | campaign表现 |
| 自动订阅累积销售额 | `dwd_mkt_campaign_product_perf_di.autoship_accrued_sales` | false | dwd_mkt_campaign_product_perf_di.autoship_accrued_sales | campaign表现 |
| 自动订阅累积订单数 | `dwd_mkt_campaign_product_perf_di.autoship_accrued_orders` | false | dwd_mkt_campaign_product_perf_di.autoship_accrued_orders | campaign表现 |
| 关键词广告花费 | `dwd_mkt_chewy_keyword_perf_di.spend` | false | dwd_mkt_chewy_keyword_perf_di.spend | 关键词表现 |
| 关键词广告订单数 | `dwd_mkt_chewy_keyword_perf_di.total_orders` | false | dwd_mkt_chewy_keyword_perf_di.total_orders | 关键词表现 |
| 关键词曝光量 | `dwd_mkt_chewy_keyword_perf_di.impressions` | false | dwd_mkt_chewy_keyword_perf_di.impressions | 关键词表现 |
| 关键词点击量 | `dwd_mkt_chewy_keyword_perf_di.clicks` | false | dwd_mkt_chewy_keyword_perf_di.clicks | 关键词表现 |
| 关键词直接销售额 | `dwd_mkt_chewy_keyword_perf_di.direct_sales` | false | dwd_mkt_chewy_keyword_perf_di.direct_sales | 关键词表现 |
| 关键词LTV销售额 | `dwd_mkt_chewy_keyword_perf_di.ltv_sales` | false | dwd_mkt_chewy_keyword_perf_di.ltv_sales | 关键词表现 |
| 关键词自动订阅数 | `dwd_mkt_chewy_keyword_perf_di.autoship_subscriptions` | false | dwd_mkt_chewy_keyword_perf_di.autoship_subscriptions | 关键词表现 |
| 关键词自动订阅销售额 | `dwd_mkt_chewy_keyword_perf_di.autoship_sales` | false | dwd_mkt_chewy_keyword_perf_di.autoship_sales | 关键词表现 |
| 关键词自动订阅累积订单数 | `dwd_mkt_chewy_keyword_perf_di.autoship_accrued_orders` | false | dwd_mkt_chewy_keyword_perf_di.autoship_accrued_orders | 关键词表现 |
| 新客数 | `dwd_mkt_chewy_keyword_perf_di.new_to_brand_customers` | false | dwd_mkt_chewy_keyword_perf_di.new_to_brand_customers | 关键词表现 |
| walmart-ad_spend | `walmart_compaign_item_performance_rpa.ad_spend` | false | walmart_compaign_item_performance_rpa.ad_spend | 沃尔玛campaign_item_performance |
| walmart-ad_orders | `walmart_compaign_item_performance_rpa.orders` | false | walmart_compaign_item_performance_rpa.orders | 沃尔玛campaign_item_performance |
| walmart-impressions | `walmart_compaign_item_performance_rpa.impressions` | false | walmart_compaign_item_performance_rpa.impressions | 沃尔玛campaign_item_performance |
| walmart-clicks | `walmart_compaign_item_performance_rpa.clicks` | false | walmart_compaign_item_performance_rpa.clicks | 沃尔玛campaign_item_performance |
| 归因销售额 | `walmart_compaign_item_performance_rpa.total_attributed_sales` | false | walmart_compaign_item_performance_rpa.total_attributed_sales | 沃尔玛campaign_item_performance |
| 广告加购数 | `walmart_compaign_item_performance_rpa.total_add_to_cart` | false | walmart_compaign_item_performance_rpa.total_add_to_cart | 沃尔玛campaign_item_performance |
| 广告其他加购数 | `walmart_compaign_item_performance_rpa.other_add_to_cart` | false | walmart_compaign_item_performance_rpa.other_add_to_cart | 沃尔玛campaign_item_performance |
| 广告曝光SKU销售额 | `SUM_AGG(walmart_compaign_item_performance_rpa.advertised_sku_sales)` | true | walmart_compaign_item_performance_rpa.advertised_sku_sales | 沃尔玛campaign_item_performance |
| 广告曝光SKU数 | `SUM_AGG(walmart_compaign_item_performance_rpa.advertised_sku_units)` | true | walmart_compaign_item_performance_rpa.advertised_sku_units | 沃尔玛campaign_item_performance |
| 目标广告费 | `SUM_AGG(dim_sell_target.ad_cost)` | true | 口径：目标广告费（销售目标表中的目标广告费）；dim_sell_target.ad_cost | 销售目标表 |

### 05_库存与周转（29 个指标）

| 指标名称 | 表达式 | 聚合 | 口径描述 | 引用表.字段 | 所属模型(推断) |
|---|---|---|---|---|---|
| 在库数量 | `dwd_inv_scm_undelivered_order_details_snap_1.Available_Stock_qty` | false | 口径：各仓库可用库存数量之和 | dwd_inv_scm_undelivered_order_details_snap_1.Available_Stock_qty | 可用库存在途库存汇总表 |
| 在库金额 | `dwd_inv_scm_undelivered_order_details_snap_1.Available_Stock_cny` | false | 口径：在库金额（采购成本价 × 可用库存数量） | dwd_inv_scm_undelivered_order_details_snap_1.Available_Stock_cny | 可用库存在途库存汇总表 |
| 在途数量 | `dwd_inv_scm_undelivered_order_details_snap_1.In_transit_Stock_qty` | false | 口径：各仓库在途库存数量之和 | dwd_inv_scm_undelivered_order_details_snap_1.In_transit_Stock_qty | 可用库存在途库存汇总表 |
| 在途金额 | `dwd_inv_scm_undelivered_order_details_snap_1.In_transit_Stock_cny` | false | 口径：在途金额（采购成本价 × 在途库存数量） | dwd_inv_scm_undelivered_order_details_snap_1.In_transit_Stock_cny | 可用库存在途库存汇总表 |
| 当前在库数量 | `SUM_AGG(dwd_inv_scm_undelivered_order_details_snap_inventory.Available_Stock_qty)` | true | 口径：当前在库数量（当前最新日期的可用库存数量） | dwd_inv_scm_undelivered_order_details_snap_inventory.Available_Stock_qty | F_库存_最新可用库存在途库存 |
| 当前在库金额 | `SUM_AGG(dwd_inv_scm_undelivered_order_details_snap_inventory.Available_Stock_cny)` | true | 口径：在库金额（采购成本价 × 当前可用库存数量） | dwd_inv_scm_undelivered_order_details_snap_inventory.Available_Stock_cny | F_库存_最新可用库存在途库存 |
| 当前在途数量 | `SUM_AGG(dwd_inv_scm_undelivered_order_details_snap_inventory.In_transit_Stock_qty)` | true | 口径：当前在途数量（当前最新日期的在途库存数量） | dwd_inv_scm_undelivered_order_details_snap_inventory.In_transit_Stock_qty | F_库存_最新可用库存在途库存 |
| 当前在途金额 | `SUM_AGG(dwd_inv_scm_undelivered_order_details_snap_inventory.In_transit_Stock_cny)` | true | 口径：当前在途金额（采购成本价 × 当前在途库存数量） | dwd_inv_scm_undelivered_order_details_snap_inventory.In_transit_Stock_cny | F_库存_最新可用库存在途库存 |
| 出库数量 | `dwd_inv_warehouse_outbound_di_1.Outbound_Stock_qty` | false | 口径：出库数量（各仓库出库数量之和） | dwd_inv_warehouse_outbound_di_1.Outbound_Stock_qty | 出库汇总表 |
| 出库金额 | `dwd_inv_warehouse_outbound_di_1.Outbound_Stock_cny` | false | 口径：出库金额（出库数量 × 采购成本价） | dwd_inv_warehouse_outbound_di_1.Outbound_Stock_cny | 出库汇总表 |
| 海外仓发货费 | `SUM_AGG(dwd_scm_shipout_billing_txn_di.shipping_amount) + SUM_AGG(dwd_fnc_ezzeship_postfee_di.ezzeship_warehouse_shipping_fee)` | true | - | dwd_scm_shipout_billing_txn_di.shipping_amount；dwd_fnc_ezzeship_postfee_di.ezzeship_warehouse_shipping_fee | shipout仓库账单 / ezeeship明细表 |
| shipout海外物流费 | `SUM_AGG(dwd_scm_shipout_billing_txn_di.shipping_amount)` | true | - | dwd_scm_shipout_billing_txn_di.shipping_amount | shipout仓库账单 |
| ezeeship海外物流费 | `SUM_AGG(dwd_fnc_ezzeship_postfee_di.ezzeship_warehouse_shipping_fee)` | true | - | dwd_fnc_ezzeship_postfee_di.ezzeship_warehouse_shipping_fee | ezeeship明细表 |
| 海外仓操作费 | `SUM_AGG(dwd_scm_shipout_billing_txn_di.status)` | true | 海外仓操作费（含上架、换标） | dwd_scm_shipout_billing_txn_di.status | shipout仓库账单 |
| 采购总数量 | `dwd_scm_amazon_po_order_di.quantity_real` | false | 口径：采购总数量（领星采购单中的采购订单总数量（PO下单数量）） | dwd_scm_amazon_po_order_di.quantity_real | 领星采购单 |
| 采购总金额 | `dwd_scm_amazon_po_order_di.quantity_real_cny` | false | 口径：采购总金额（PO总数量 × 采购成本价） | dwd_scm_amazon_po_order_di.quantity_real_cny | 领星采购单 |
| 采购到货数量 | `dwd_scm_amazon_po_order_di.quantity_entry` | false | 口径：采购到货数量（领星采购单中已到货成品数量） | dwd_scm_amazon_po_order_di.quantity_entry | 领星采购单 |
| 采购到货金额 | `dwd_scm_amazon_po_order_di.quantity_entry_cny` | false | 口径：采购到货金额（采购到货数量 × 采购成本价） | dwd_scm_amazon_po_order_di.quantity_entry_cny | 领星采购单 |
| 采购未到货数量 | `dwd_scm_amazon_po_order_di.quantity_receive` | false | 口径：采购未到货数量（领星采购单中未到货成品数量） | dwd_scm_amazon_po_order_di.quantity_receive | 领星采购单 |
| 采购未到货金额 | `dwd_scm_amazon_po_order_di.quantity_receive_cny` | false | 口径：采购未到货金额（采购未到货数量 × 采购成本价） | dwd_scm_amazon_po_order_di.quantity_receive_cny | 领星采购单 |
| 采购待生产数量 | `dwd_scm_amazon_po_order_di.pending_production_qty` | false | 口径：采购待生产数量（未到货数量中扣减已交付成品数量后的待生产数量） | dwd_scm_amazon_po_order_di.pending_production_qty | 领星采购单 |
| 采购待生产金额 | `dwd_scm_amazon_po_order_di.pending_production_cny` | false | 口径：采购待生产金额（采购待生产数量 × 采购成本价） | dwd_scm_amazon_po_order_di.pending_production_cny | 领星采购单 |
| 采购在库数量 | `dwd_scm_amazon_po_order_di.finished_quantity` | false | 口径：供应商填报的已交付成品库存数量（供应商处已完成生产、可供发货的库存） | dwd_scm_amazon_po_order_di.finished_quantity | 领星采购单 |
| 采购在库金额 | `dwd_scm_amazon_po_order_di.finished_quantity_cny` | false | 口径：采购在库金额（采购在库数量 × 采购成本价） | dwd_scm_amazon_po_order_di.finished_quantity_cny | 领星采购单 |
| 预测到库数量 | `SUM_AGG(dim_scm_shipment_exclusive.shipped_qty)` | true | 口径：预测到库数量 | dim_scm_shipment_exclusive.shipped_qty | 库存预测模型视图 |
| 在库库存数量_环比增长值 | ``（空） | true | - | - | - |
| 在库库存数量_环比增长率 | ``（空） | true | - | - | - |
| 在库库存数量_周同比增长值 | ``（空） | true | - | - | - |
| 在库库存数量_周同比增长率 | ``（空） | true | - | - | - |

### 07_财务与核算（10 个指标）

| 指标名称 | 表达式 | 聚合 | 引用表.字段 | 所属模型(推断) |
|---|---|---|---|---|
| 采购成本 | `SUM_AGG(dwd_scm_shipout_outbound_txn_di.purchase_cost_usd)` | true | dwd_scm_shipout_outbound_txn_di.purchase_cost_usd | shipout_出库明细 |
| 头程成本 | `SUM_AGG(dwd_scm_shipout_outbound_txn_di.first_leg_cost_usd)` | true | dwd_scm_shipout_outbound_txn_di.first_leg_cost_usd | shipout_出库明细 |
| 科目金额 | `SUM_AGG(dwd_fnc_chewy_rebate_di.rebate_amount)` | true | dwd_fnc_chewy_rebate_di.rebate_amount | chewy发票pdf |
| 填报科目费用 | `SUM_AGG(dwd_fnc_subject_records_di.amount)` | true | dwd_fnc_subject_records_di.amount | 科目费用填报 |
| 结算销量 | `SUM_AGG(dwd_fnc_quickbooks_invoice_allocated_di.type)` | true | dwd_fnc_quickbooks_invoice_allocated_di.type | quickbooks发票数据明细 |
| ToB销售退货量 | `SUM_AGG(dwd_fnc_quickbooks_invoice_allocated_di.type)` | true | dwd_fnc_quickbooks_invoice_allocated_di.type | quickbooks发票数据明细 |
| ToB销售退货金额 | `SUM_AGG(dwd_fnc_quickbooks_invoice_allocated_di.type)` | true | dwd_fnc_quickbooks_invoice_allocated_di.type | quickbooks发票数据明细 |
| ToB销售净收入 | `SUM_AGG(dwd_fnc_quickbooks_invoice_allocated_di.type)` | true | dwd_fnc_quickbooks_invoice_allocated_di.type | quickbooks发票数据明细 |
| ToB销售收入 | `ToB销售净收入 + ToB销售退货金额`（公式） | true | → 子指标 | - |
| 毛利润 | `ToB销售收入 - (采购成本 + 头程成本 + 海外仓发货费 + 海外仓操作费 + 科目金额 + 填报科目费用 + …)`（公式） | true | → ToB销售收入 / 采购成本 / 头程成本 / 海外仓发货费 / 海外仓操作费 / 科目金额 / 填报科目费用 | - |

---

## 二、模型→表关联结构

**说明**：`relations` 中的 `JOIN_2_0` 表示源表为主表、目标表被关联（1:N）；`LEFT_JOIN` 表示事实表 LEFT JOIN 维度表（N:1）；`JOIN_1_2` 表示 1:1 关联。同一模型内存在重复 relations 定义（FineBI 导出的正常现象，已去重展示）。

### 01_交易与销售（5 个模型）

| 模型名称 | base_table | 关联表列表 | 关联关系摘要 |
|---|---|---|---|
| 订单_ToC_商品_交易模型 | dws_trd_channel_sku_sales_di_order | dws_trd_channel_sku_sales_di_order、dim_import_sku_info_4、dim_shop、amazon_sku_mapping、dim_country、dim.dim_calendar_cn、dim.dim_calendar_local、dim_channel_kv、dim_import_sku_info_2 | 主表 dim_calendar_local(dim_calendar_cn)→fdate/fdate_cn；dim_channel_kv.channel_code→dim_channel_code；dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dim_country.country_code→dim_country_code；dim_shop.dim_shop_id→dim_shop_id；amazon_sku_mapping(seller_sku,sid)→(channel_sku_code,dim_shop_id)；dim_import_sku_info_4.sku_code→bundleinfo_bundle_code |
| 订单_ToB_商品_交易模型 | dwd_scm_sps_po_detail_di_tob | dwd_scm_sps_po_detail_di_tob、dim_import_sku_info_4、dim.dim_calendar_cn、dim.dim_calendar_local、to_b_vendor_info、dim_import_sku_info_2 | to_b_vendor_info.Vendor_code→Vendor_code；dim_calendar_local/cn.fdate→PO_Date；dim_import_sku_info_2/4.sku_code→dim_hicc_sku_code |
| 销售目标表 | dim_sell_target | dim_sell_target、dim_shop、dim_country、dim.dim_calendar_cn、dim.dim_calendar_local、dim_channel_kv、dim_import_sku_info_2 | dim_import_sku_info_2.sku_code→sub_asin；dim_calendar_local/cn.fdate→fmonth；dim_country.country_code→dim_country_code；dim_channel_kv.channel_code→dim_channel_code；dim_shop.dim_shop_id→shop |
| 退货汇总表 | dws_voc_global_return_di | dws_voc_global_return_di、dim_shop、dim_country、dim.dim_calendar_cn、dim.dim_calendar_local、dim_channel_kv、dim_import_sku_info_2 | dim_calendar_cn.fdate→fdate_cn；dim_calendar_local.fdate→fdate；dim_shop.dim_shop_id→dim_shop_id；dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dim_country.country_code→dim_country_code；dim_channel_kv.channel_code→dim_channel_code |
| 沃尔玛订单明细 | dwd_trd_toc_walmart_order_item_di_walmart | dwd_trd_toc_walmart_order_item_di_walmart、dwd_trd_toc_walmart_order_item_di_1、dim.dim_calendar_local、dim_import_sku_info_2 | dim_calendar_local.fdate→fdate；dwd_trd_toc_walmart_order_item_di_1.item_sku→item_sku（商品名）；dim_import_sku_info_2.sku_code→item_sku |

### 02_营销与流量（4 个模型）

| 模型名称 | base_table | 关联表列表 | 关联关系摘要 |
|---|---|---|---|
| 广告事实模型 | dws_mkt_global_ad_spend_di | dws_mkt_global_ad_spend_di、dwd_mkt_petco_ad_spend_di、dwd_mkt_chewy_ad_spend_di、dim_shop、dim_country、dim.dim_calendar_cn、dim.dim_calendar_local、dim_channel_kv、dim_import_sku_info_2 | 三张广告事实表各自关联：dim_calendar_local/cn（fdate/fdate_cn）、dim_country、dim_channel_kv、dim_import_sku_info_2(sku_code→dim_hicc_sku_code)、dim_shop(dim_shop_id) |
| 沃尔玛campaign_item_performance | walmart_compaign_item_performance_rpa | walmart_compaign_item_performance_rpa、dwd_trd_toc_walmart_order_item_di_1、dim.dim_calendar_local、dim_import_sku_info_2 | dim_calendar_local.fdate→date；dwd_trd_toc_walmart_order_item_di_1.item_sku→sku_id；dim_import_sku_info_2.sku_code→sku_id |
| 关键词表现 | dwd_mkt_chewy_keyword_perf_di | dwd_mkt_chewy_keyword_perf_di、dim.dim_calendar_local | dim_calendar_local.fdate→fdate |
| campaign表现 | dwd_mkt_campaign_product_perf_di | dwd_mkt_campaign_product_perf_di、dim.dim_calendar_local、dim_channel_kv、dim_import_sku_info_2 | dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dim_calendar_local.fdate→fdate；dim_channel_kv.channel_code→channel_id |

### 05_库存与周转（9 个模型）

| 模型名称 | base_table | 关联表列表 | 关联关系摘要 |
|---|---|---|---|
| F_库存_最新可用库存在途库存 | dwd_inv_scm_undelivered_order_details_snap_inventory | dwd_inv_scm_undelivered_order_details_snap_inventory、dim_import_sku_info_4、dim_view_expiry_labels、dim_business_channel、dim_warehouse、dim_import_sku_info_2 | dim_warehouse.warehouse_id→dim_warehouse_id；dim_view_expiry_labels.fdate→expiry_date；dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dim_business_channel.id→belong_to_channel_id；dim_import_sku_info_4.sku_code→dim_hicc_sku_code |
| 可用库存在途库存汇总表 | dwd_inv_scm_undelivered_order_details_snap_1 | dwd_inv_scm_undelivered_order_details_snap_1、dim_import_sku_info_4、amazon_sku_mapping、dim_view_expiry_labels、dim_business_channel、dim.dim_product_skus_warehouse、dim_warehouse、dim.dim_calendar_cn、dim.dim_calendar_local、dim_import_sku_info_2 | dim_calendar_local.fdate→fdate_p；dim_warehouse→dim_warehouse_id；dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dim_view_expiry_labels.fdate_str→expiry_date_str；amazon_sku_mapping(sid,fnsku)→(dim_warehouse_id,channel_sku_code)；dim_product_skus_warehouse(warehouse_code,warehouse_sku_id)→(dim_warehouse_id,channel_sku_code)；dim_business_channel.id→belong_to_channel_id；dim_calendar_cn.fdate→fdate_cn；dim_import_sku_info_4.sku_code→dim_hicc_sku_code_single |
| 出库汇总表 | dwd_inv_warehouse_outbound_di_1 | dwd_inv_warehouse_outbound_di_1、dwd_inv_warehouse_outbound_di、dim.dim_product_skus_warehouse、dim_warehouse、dim.dim_calendar_cn、dim.dim_calendar_local、dim_channel_kv、dim_import_sku_info_2 | dim_calendar_local.fdate→fdate；dim_warehouse→dim_warehouse_id；dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dwd_inv_warehouse_outbound_di.dim_outbound_order_type→dim_outbound_order_type；dim_product_skus_warehouse(warehouse_code,warehouse_sku_id)→(dim_warehouse_id,channel_sku_code)；dim_calendar_cn.fdate→fdate_cn；dim_channel_kv.channel_name→dim_outbound_order_type(1:1) |
| FBA明细数据 | dwd_inv_amazon_fba_stock_di | dwd_inv_amazon_fba_stock_di、dim.dim_product_skus_warehouse、dim_warehouse、dim.dim_calendar_local、dim_import_sku_info_2 | dim_product_skus_warehouse(warehouse_code,warehouse_channel_sku_code)→(dim_warehouse_id,channel_sku_code)；dim_calendar_local.fdate→fdate_p；dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dim_warehouse.warehouse_id→dim_warehouse_id |
| 领星采购单 | dwd_scm_amazon_po_order_di | dwd_scm_amazon_po_order_di、dim_country、dim_scm_supplier、dim.dim_calendar_local、dim_import_sku_info_2 | dim_calendar_local.fdate→fdate_p；dim_scm_supplier.supplier_id→supplier_id；dim_import_sku_info_2.sku_code→dim_hicc_sku_code；dim_country.country_code→dim_country_code |
| shipout仓库账单 | dwd_scm_shipout_billing_txn_di | dwd_scm_shipout_billing_txn_di、dim.dim_calendar_local | dim_calendar_local.fdate→count_date |
| shipout_出库明细dwd_scm_shipout_outbound_detail | dwd_scm_shipout_outbound_txn_di | dwd_scm_shipout_outbound_txn_di、dim_warehouse、dim.dim_calendar_local、dim_import_sku_info_2 | dim_calendar_local.fdate→fdate；dim_warehouse.warehouse_id→dim_warehouse_id；dim_import_sku_info_2.sku_code→dim_hicc_sku_code |
| ezeeship明细表 | dwd_fnc_ezzeship_postfee_di | dwd_fnc_ezzeship_postfee_di、dim.dim_calendar_local | dim_calendar_local.fdate→fdate |
| 库存预测模型视图 | dim_scm_shipment_exclusive | dim_scm_shipment_exclusive、dim.dim_calendar_local | dim_calendar_local.fdate→predict_arrival_date |

### 06_客户与体验（1 个模型）

| 模型名称 | base_table | 关联表列表 | 关联关系摘要 |
|---|---|---|---|
| 商品评论分析 | dim_import_sku_info_3 | dim_import_sku_info_3 | 无关联关系（relations 为空） |

### 07_财务与核算（3 个模型）

| 模型名称 | base_table | 关联表列表 | 关联关系摘要 |
|---|---|---|---|
| 科目费用填报dwd_fin_import_financial_subject_records | dwd_fnc_subject_records_di | dwd_fnc_subject_records_di、dim.dim_calendar_local | dim_calendar_local.fdate→record_date |
| quickbooks发票数据明细 | dwd_fnc_quickbooks_invoice_allocated_di | dwd_fnc_quickbooks_invoice_allocated_di、dim.dim_calendar_local | dim_calendar_local.fdate→list_txn_date |
| chewy发票pdfdwd_fin_sps_chewy_rebate | dwd_fnc_chewy_rebate_di | dwd_fnc_chewy_rebate_di、dim.dim_calendar_local | dim_calendar_local.fdate→fdate |

### 09_主数据与维度（1 个模型，跨域大宽表）

| 模型名称 | base_table | 关联表列表 | 关联关系摘要 |
|---|---|---|---|
| 维度模型表 | dim_view_expiry_labels | 37 张表：dim_view_expiry_labels、dim_scm_supplier、D_商品_bundle维度表、dim_warehouse、to_b_vendor_info、dim_import_sku_info_2、dim_import_sku_info_4、dim_shop、amazon_sku_mapping、dim_country、dim.dim_product_skus_warehouse、dim_business_channel、dim_region、dim_import_sku_info、dwd_trd_toc_walmart_order_item_di_1、dim.dim_calendar_cn、dim.dim_calendar_local、dim_channel_kv、walmart_compaign_item_performance_rpa、dwd_fnc_subject_records_di、dwd_scm_shipout_outbound_txn_di、dwd_mkt_chewy_keyword_perf_di、dwd_scm_sps_po_detail_di_tob、dim_scm_shipment_exclusive、dws_voc_global_return_di、dwd_scm_shipout_billing_txn_di、dwd_inv_amazon_fba_stock_di、dwd_trd_toc_walmart_order_item_di_walmart、dwd_inv_scm_undelivered_order_details_snap_inventory、dim_sell_target、dws_mkt_global_ad_spend_di、dwd_mkt_petco_ad_spend_di、dwd_inv_warehouse_outbound_di_1、dwd_mkt_campaign_product_perf_di、dwd_inv_warehouse_outbound_di、dwd_scm_amazon_po_order_di、dwd_mkt_chewy_ad_spend_di、dwd_fnc_quickbooks_invoice_allocated_di、dwd_inv_scm_undelivered_order_details_snap_1、dwd_fnc_chewy_rebate_di、dwd_fnc_ezzeship_postfee_di、dws_trd_channel_sku_sales_di_order | 以 dim_view_expiry_labels 为基表，将几乎所有域的明细/汇总表通过 SKU（dim_import_sku_info_2/4）、仓库（dim_warehouse）、国家（dim_country）、渠道（dim_channel_kv）、店铺（dim_shop）、日历（dim_calendar_local/cn）等维度统一串接；relations 数量庞大（每个事实表按 dim_hicc_sku_code / dim_warehouse_id / dim_country_code / dim_channel_code / fdate 等键 LEFT JOIN） |

### 汇总：模型与表数量

| 业务域 | 模型数 | 涉及的唯一表数 |
|---|---|---|
| 01_交易与销售 | 5 | 15 |
| 02_营销与流量 | 4 | 9 |
| 05_库存与周转 | 9 | 13 |
| 06_客户与体验 | 1 | 1 |
| 07_财务与核算 | 3 | 4 |
| 09_主数据与维度 | 1 | 37 |
| **合计** | **23** | - |

---

## 三、重点业务域细表

### 3.1 05_库存与周转（12 张表定义）

| 表名（FineBI） | 展示名 | 数据来源（SQL/连接） | 关键字段 |
|---|---|---|---|
| dwd_inv_scm_undelivered_order_details_snap_inventory | 最新可用库存在途库存-快照 | bigquery：`dws.dws_inv_global_stock_snap`（过滤 fdate_p = current_date） | channel_sku_code、dim_hicc_sku_code、dim_shop_id、expiry_date、**Available_Stock_qty/cny（可用库存数量/金额）**、**In_transit_Stock_qty/cny（在途库存数量/金额）**、dim_data_source、dim_warehouse_id、belong_to_channel_code/id、belong_to_country_code、vine_or_not、expiry_date_str |
| dwd_inv_scm_undelivered_order_details_snap_1 | 最新可用库存在途库存-快照（历史） | bigquery：`dws.dws_inv_global_stock_snap`（fdate_p >= '2026-05-05'） | fdate_p/fdate_cn、channel_sku_code、dim_hicc_sku_code(_single)、dim_shop_id、expiry_date、Available_Stock_qty/cny（别名：可用库存数量/金额）、In_transit_Stock_qty/cny（别名：在途库存数量/金额）、dim_data_source、dim_warehouse_id、belong_to_channel_code/id、belong_to_country_code、vine_or_not、expiry_date_str |
| dwd_inv_amazon_fba_stock_di | Amazon-FBA明细-日级 | bigquery：`dwd.dwd_inv_amazon_fba_stock_di` | fdate_p、dim_warehouse_id、channel_sku_code、dim_hicc_sku_code、dim_shop_id、expiry_date、Available/In_transit_Stock_qty/cny、asin、seller_sku、product_name、afn_fulfillable_quantity、afn_unsellable_quantity、afn_inbound_working_quantity、**库龄分段：inv_age_0_to_30 / 31_to_60 / 61_to_90 / 0_to_90 / 91_to_180 / 181_to_270 / 271_to_330 / 271_to_365 / 331_to_365 / 365_plus（_days/_price）**、recommended_action、sell_through、estimated_excess_quantity、estimated_storage_cost_next_month、historical_days_of_supply、cg_price、cg_transport_costs |
| dwd_inv_warehouse_outbound_di_1 | 出库数据-日级 | bigquery：`dwd.dwd_inv_warehouse_outbound_di`（fdate is not null） | fdate/fdate_cn、dim_hicc_sku_code、channel_sku_code、**Outbound_Stock_qty（出库数量）**、**Outbound_Stock_cny（出库金额）**、data_source_name、dim_warehouse_id、customer_id/name、dim_outbound_order_type |
| dwd_inv_warehouse_outbound_di | 出库单类型维度-日级 | bigquery：`dwd.dwd_inv_warehouse_outbound_di`（DISTINCT） | dim_outbound_order_type |
| dwd_inv_walmart_wfs_stock_di | Walmart-WFS库存快照-日级 | bigquery：`dwd.dwd_inv_walmart_wfs_stock_di` | fdate_p、sku、onhandUnits、stockStatus、inboundUnits、itemLifecycle、reservedUnits、availableUnits、firstInStockDate、publishingStatus、daysOfSupply、surplusUnits、outOfStockDate、suggestedUnits、sellThroughRate、client_id、purchased_cost_price、dim_data_source |
| dwd_inv_walmart_inbound_txn_di | walmart WFS货件单据名细 | bigquery：`dwd.dwd_inv_walmart_inbound_txn_di` | shipment_id、shop_id、warehouse_code/name、hicc_sku、shipped_qty、ship_node_name、shipment_create_time、expected_delivery_date、actual_delivery_date、total_qty、rec_qty、shipment_status、expiry_date、warehouse_sku_code、belong_to_country_code、belong_to_channel_code |
| dwd_finebi_inbound_shipment_v | 运单入库 | bigquery：`dwd.dwd_inv_inbound_shipment_status_di` | shipment_main_flag、inbound_main_flag、intransit_main_flag、stock_platform_name、shop_id/name、shipment_id、order_id、warehouse_id/name、warehouse_sku、hicc_sku、available_stock_qty、in_transit_stock_qty、inbound_shipped_qty、shipped_qty、inbound_status、platform_name、shipping_method、shipment_status、collect_cargos_date、start_count_date、cus_dec_date、atd/ata、expected_delivery、actual_delivery、predict_arrival_date、receiving_time、import_check_date、export_check_date |
| dws_shipment_abnormal_data | 揽收报关揽收开船异常 | bigquery：`dws.dws_scm_shipment_abnormal_data_di` | platform_name、fba_info、create_time、collect_cargos_date、cus_dec_date、atd、cus_dec_alert_flag、atd_alert_flag、collect2today_days、bad_weather_alert_flag、check_flag/date、appointment_delivery_date、collect_overdue_flag、alert_type、track_info |
| dim_warehouse | 仓库维度 | bigquery：`ods.import_dim_warehouse`（排除 w010） | warehouse_id、warehouse_name、country_code |
| ods.import_scm_first_leg_transit_time_standard | 头程物流时效配置表 | bigquery：`ods.import_scm_first_leg_transit_time_standard` | id、country_name/code、shipping_channel、region、factory_pickup_days、sailing_to_arrival_days、clearance_to_sign_days、total_transit_days、remark、create_time、update_time、synctime |
| first_leg_cost_unit_price | 头程成本单价 | bigquery：手工构造示例数据（cast '2026-01-01'） | fdate、country_code、sku、package_type、first_leg_cost、purchase_price |

### 3.2 01_交易与销售（15 张表定义）

| 表名（FineBI） | 展示名 | 数据来源（SQL/连接） | 关键字段 |
|---|---|---|---|
| dws_trd_channel_sku_sales_di_order | 订单商品-日级（销售事实核心表） | bigquery：`dws.dws_trd_channel_sku_sales_di` 正常订单 UNION ALL 取消订单（cancel_date 非空） | fdate/fdate_cn（当地时间/北京时间）、channel_sku_code、dim_country_code、dim_hicc_sku_code、bundleinfo_bundle_code、dim_channel_code、dim_shop_id、bundle_quantity（单品销量）、quantity_ordered（bundle销量）、paid_amount_usd（支付金额）、quantity_ordered_cancel、paid_amount_usd_cancel（取消销量/金额）、bundle_quantity_cancel |
| dws_trd_channel_sku_sales_di_toc | ToC单据-日级 | bigquery：`dws.dws_trd_channel_sku_sales_di`（select *） | fdate/fdate_cn、cancel_date/cancel_date_cn、dim_shop_id、dim_channel_code、dim_hicc_sku_code、quantity_ordered、bundle_quantity、item_price_amount(_usd)、dim_country_code、channel_sku_code、seller_sku_code、dim_channel_name、order_id、vine_or_not、bundleinfo_bundle_code、data_source_name、dim_hicc_sku_code_single |
| dws_trd_channel_sku_sales_di_tiktok | TikTok-周报-日级 | bigquery：`dws.dws_trd_channel_sku_sales_di`（p009）+ `dwd.dwd_mkt_tk_item_group_perf_di`（广告）按周（周五~周四）LEFT JOIN | week_start_friday、week_end_thursday、week_range、sku_code、total_qty、order_total_amount_usd、ads_spend_usd |
| dws_trd_channel_sku_sales_di_1 | ToC平台首销日期-日级 | bigquery：`dws.dws_trd_channel_sku_sales_di`（quantity_ordered>0 且 cancel_date is null，MIN(fdate)） | dim_channel_code、dim_country_code、channel_sku_code、seller_sku_code、first_sale_date |
| dwd_trd_toc_amazon_order_item_di | Amazon-订单明细-日级 | bigquery：`dwd.dwd_trd_toc_amazon_order_item_di` | amazon_order_id、order_status、order_total_amount、currency、purchase_date_local(_utc)、posted_date、payment_method、itemlist_*（sku/asin/title/profit/quantity_ordered/quantity_shipped/item_price_amount/commission_amount/promotion_amount/tax_amount/cg_price/cg_transport_costs 等明细）、fdate |
| dwd_trd_toc_walmart_order_item_di_walmart | Walmart订单明细-日级 | bigquery：`dwd.dwd_trd_toc_walmart_order_item_di` | purchase_order_id、customer_order_id、fdate、item_sku、item_product_name、order_line_quantity_amount、charge_amount、amount_currency、tax_amount、fulfillment_ship_method、order_status、status_date、ship_date_time、client_id、dim_hicc_sku_code |
| dwd_trd_toc_walmart_order_item_di_1 | Walmart-商品维度-日级 | bigquery：`dwd.dwd_trd_toc_walmart_order_item_di`（按 item_sku 去重取商品名） | item_sku、item_product_name |
| dwd_trd_toc_tk_order_item_di | TikTok订单明细-日级 | bigquery：`dwd.dwd_trd_toc_tk_order_item_di` | order_id、status、cancellation_initiator、cancel_reason、paid_time、fulfillment_type、paymentjson_*（sub_total/product_tax/shipping_fee/total_amount/currency 等）、lineitemsjson_*（sku_id/sku_name/sale_price/original_price/product_name/seller_sku 等）、shop_code(dim_shop_id)、etl_time |
| dwd_trd_toc_shopify_order_item_di | Shopify订单明细-日级 | bigquery：`dwd.dwd_trd_toc_shopify_order_item_di` LEFT JOIN `dim.dim_product_skus` | created_at、cancelled_at_date、shop_id、order_id、name、currency_code、net_payment_*_amount、total_price_*_amount、total_tax_*_amount、line_item_sku、line_item_quantity、line_item_discountedUnitPriceAfterAllDiscountsSet_shopMoney_amount、spu_name_en/cn、brand、spec_name_cn/en、category |
| dwd_trd_toc_shopee_order_item_di | Shopee订单明细-日级 | bigquery：`dwd.dwd_trd_toc_shopee_order_item_di` | order_sn、shop_id、order_status、cancel_reason、currency、total_amount、pay_time、ship_by_date、shipping_carrier、itemlist_*（item_sku/model_sku/item_name/model_original_price/model_discounted_price/model_quantity_purchased 等） |
| dwd_trd_toc_lazada_order_item_di | Lazada订单明细-日级 | bigquery：`dwd.dwd_trd_toc_lazada_order_item_di` | order_id、order_item_id、sku、shop_sku、name、status、country_code、item_price、paid_price、tax_amount、shipping_amount、voucher_*、wallet_credits、supply_price、created_at、etl_time |
| dwd_trd_tob_hktvmall_order_item_di | HKTVMall订单明细-日级 | bigquery：`dwd.dwd_trd_tob_hktvmall_order_item_di` | consignmentCode、trackingId、orderDate、consignmentStatus、orderId、deliveryDate、consignmentEntries_*（pk/brand/skuId/quantity/skuNameEn/skuNameZh/totalPrice）、dim_channel_sku_code、hicc_sku_code、totalPrice_usd、currency、is_return、refund_quantity、fdate/fdate_cn、to_usd_rate |
| dwd_scm_sps_po_detail_di_1 | SPS销售订单明细-日级 | bigquery：`dwd.dwd_scm_sps_po_detail_di` LEFT JOIN `dim.dim_product_skus` LEFT JOIN `dim.dim_sps_vendor` | po_number、po_line_number、po_date、requested_delivery_date、channel_sku、dim_hicc_sku_code、Unit_Price、Qty_Ordered、tot_amount、Unit_of_Measure、Vendor_code、vendor_name、dim_country_code、dim_channel_code、spu_name_en/cn、brand、spec_name_cn/en、category |
| to_b_hk_po_detail | ToB香港PO明细 | Mysql_DataCollect：`hicc.import_b2b_channel_hk_po` LEFT JOIN `import_sku_info` | SKU、Product_Name_English/Chinese、Unit、Order_QtyUnit、Total_Amount、MSRP_Unit、MAP_Unit、order_id、order_Date、channel_name/code、currency_code、spu_name_en/cn、brand、spec_name_cn/en、category |
| supply_sales_forecast | 供应链销售预测 | 商品主数据：`supply_and_sales.forecast_detail` + `forecast_main`（取最新 forecast_id） | forecast_id、sku_code、last_1m_day_avg_orders、last_3m_day_avg_orders、forecast_month_qty、forecast_month、country_code、channel_name |

---

## 附录

### A. 各域指标数量统计

| 业务域 | 指标数 | 直接引用表字段 | 公式型（引用其他指标） | 空表达式（报表端配置） |
|---|---|---|---|---|
| 00_未分类 | 6 | 6 | 0 | 0 |
| 01_交易与销售 | 17 | 11 | 4（ToC销售额、单品销量、销售额、近7天日均销量） | 1（近7天销量） |
| 02_营销与流量 | 33 | 29 | 3（广告花费、ToB广告花费、ToB销售收入不在此域） | 0 |
| 05_库存与周转 | 29 | 24 | 0 | 4（环比/周同比增长率与值） |
| 07_财务与核算 | 10 | 7 | 3（ToB销售收入、毛利润，其中采购成本等 2 个为公式引用） | 0 |
| **合计** | **95** | **77** | **10** | **5** |

### B. 指标/模型关联要点

- **最核心的事实表**：
  - 销售域：`dws_trd_channel_sku_sales_di_order`（12+ 个指标引用）、`dwd_scm_sps_po_detail_di_tob`（ToB 销量/销售额）
  - 库存域：`dwd_inv_scm_undelivered_order_details_snap_1` / `_snap_inventory`（在库/在途/当前系列 8 个指标）、`dwd_inv_warehouse_outbound_di_1`（出库数量/金额）、`dwd_scm_amazon_po_order_di`（采购系列 10 个指标）
  - 营销域：`walmart_compaign_item_performance_rpa`（9 个指标）、`dwd_mkt_chewy_keyword_perf_di`（9 个指标）、`dwd_mkt_campaign_product_perf_di`（7 个指标）、`dws_mkt_global_ad_spend_di`（ToC 广告花费）
  - 财务域：`dwd_fnc_quickbooks_invoice_allocated_di`（4 个指标，均取 type 字段，口径待完善）
- **通用关联维度**：dim_import_sku_info_2（SKU 主数据，绝大多数模型关联）、dim_import_sku_info_4（bundle/单品维度）、dim.dim_calendar_local / dim.dim_calendar_cn（日期维度，几乎所有模型都关联）、dim_country、dim_channel_kv、dim_shop、dim_warehouse。
- **注意**：`近7天销量`、`在库库存数量_*环比/周同比*` 4 个指标表达式为空（依赖报表端时间窗口/同环比配置）；`结算销量`、`ToB销售退货量/金额/净收入` 表达式均取 `dwd_fnc_quickbooks_invoice_allocated_di.type`，疑似口径待完善（占位）。
