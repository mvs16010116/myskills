# 广告/财务/采购供应域 清洗逻辑与规则（02_mkt + 07_fnc + 08_scm）

> 分析对象：`hicc_data_platform/models/` 下 `02_mkt`（广告）、`07_fnc`（财务）、`08_scm`（采购供应）三个业务域的全部 dbt 模型（dim/dwd/dws 各层 SQL + schema.yml）。
> 数据平台：Google BigQuery。所有目标表均以 `_di`（日增量）/`_snap`（快照）结尾。

---

## 02_mkt 广告域

### 通用清洗规则

- **多源 UNION ALL 合并**：同一广告主多来源表合并（如亚马逊 SB/SD/SP 三源、Chewy onsite/offsite 双源），再对维度（日期×店铺×SKU×广告类型）做 `GROUP BY` 聚合；不同渠道在最终 DWS 层以固定 `dim_channel_code`（p001 亚马逊 / p002 Walmart / p003 / p004 Chewy / p006 Lazada / p007 Shopee / p009 TikTok / p010 Shopify）统一。
- **JSON 数组展开**：`UNNEST(JSON_EXTRACT_ARRAY(...))` / `UNNEST(JSON_QUERY_ARRAY(...))` 展开 campaigns / item_id_list / data / skus 等数组；Chewy 系列用 `SAFE.PARSE_JSON(value)` + `JSON_VALUE(camp, '$.kpis.XXX')` 取大写 KPI key。
- **SKU 映射补齐维度**：以 `import_dim_vendor_sku_mapping`（vendor SKU→hicc_sku）、`product_skus_sales`（pdt_ods）、`dim_product_skus_sales` / `dim_sku_mapping` 将渠道 SKU/ASIN 映射为内部 `dim_hicc_sku_code`；映射不到时为 NULL，后续分摊用兜底采购价。
- **金额折算（汇率）**：非 USD 渠道（Lazada、Shopee、B2B）通过 `ref('dim_exchange_rates')` 按 `DATE_TRUNC(fdate, MONTH) = e.fdate` + 币种匹配取 `to_usd_rate`，`spend * to_usd_rate` 折算为 USD；`dim_exchange_rates` 本身是"真实工作日汇率 + 本月无数据时用最近工作日模拟"的月级汇率维表。
- **广告费分摊（核心）**：两种模式——① 按采购价比例分摊（Lazada/Shopee DWS：`spend * purchased_cost_price / SUM(cost_price) OVER(PARTITION BY spu/广告组)`，无映射 SKU 兜底成本 0.01/0.001）；② 按 creative_id 映射分摊（Petco：item 级花费按 SKU 采购价比例摊到 creative×SKU）。
- **时间处理**：`fdate` 统一为业务日期；`etl_time` 统一用 `FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', CURRENT_TIMESTAMP() + INTERVAL 8 HOUR)`（北京时间）；Chewy onsite 爬虫日期 `MM/DD/YYYY` 字符串需 SPLIT 重组为 DATE。
- **无效花费过滤**：`spends > 0` / `cost > 0` / `expense > 0` / `ad_cost > 0`，剔除 0 花费行。
- **KPI 安全转换**：`SAFE_CAST` / `SAFE_DIVIDE` 防类型错误与除零（如 Petco CPC = SAFE_DIVIDE(spend, clicks)）。

### 各表清洗逻辑

#### dim_mkt_campaign
- 目标表: `dim.dim_mkt_campaign`（Shopee 活动-商品关联维表）
- 上游: `ods.shopee_campaign_setting_info`
- 清洗逻辑: `UNNEST(JSON_EXTRACT_ARRAY(item_id_list))` 将活动配置的 item JSON 数组展开为行；粒度 1 行 = campaign_id × item_id。
- 关键规则: 仅类型转换（campaign_id/item_id 转 STRING）+ 打 etl_time 时间戳。

#### dim_mkt_amazon_sb_campaign_config
- 目标表: `dim.dim_mkt_amazon_sb_campaign_config`（亚马逊 SB 活动配置维表）
- 上游: `ods.lingxing_amazon_api_sb_campaign_config`
- 清洗逻辑: `UNNEST(JSON_EXTRACT_ARRAY(t.data))` 展开 data 数组，`JSON_EXTRACT_SCALAR(d, '$.asin[0]')` 取 asin 数组首元素。
- 关键规则: `SELECT DISTINCT` 去重；粒度 1 行 = 店铺 × asin × campaign_id。

#### dwd_mkt_amazon_ad_perf_di
- 目标表: `dwd.dwd_mkt_amazon_ad_perf_di`（亚马逊广告花费 ASIN 级日明细）
- 上游: `ods.lingxing_amazon_sb_divide_asin_reports`（SB）、`ods.lingxing_amazon_api_sd_product_ad_reports_i`（SD）、`ods.lingxing_amazon_api_sp_product_ad_reports_i` / `_v`（SP）、`ref(dim_channel_lingxing_account)`、`pdt_ods.product_skus_sales`、`ods.import_dim_shop`
- 清洗逻辑: SB + SD + SP 三段 UNION ALL，各自 LEFT JOIN 店铺/国家/内部 SKU 映射后按 日期×店铺×ASIN×广告类型 GROUP BY 聚合 `SUM(spend_usd)`。
- 关键规则: ① SP 段双表合并——2026-07-01 前取 `_i` 表、之后取 `_v` 表（数据源切换）；② `ad_type` 打标 'sb'/'sd'/'sp'；③ 过滤 `spends/cost > 0`；④ 源数据已是 USD，不做汇率折算；⑤ 店铺维度通过 profile_id → lingxing account 映射。

#### dwd_mkt_campaign_product_perf_di
- 目标表: `dwd.dwd_mkt_campaign_product_perf_di`（广告商品粒度表现，Chewy+Walmart+Petco 四路 UNION）
- 上游: `ods.chew_campaign_product_performance_from_sidebar`（Chewy onsite）、`ods.import_dim_vendor_sku_mapping`、`ods.chewy_offsite_products_sidebar`（offsite）、`ods.walmart_compaign_item_performance_rpa`、`ref(dwd_mkt_petco_ad_spend_di)`、`ref(dim_prd_bundle_info)`
- 清洗逻辑: ① Chewy onsite：`SAFE.PARSE_JSON(value)` 后 `UNNEST(JSON_QUERY_ARRAY(LAX_JSON.campaigns))` 展开 campaign，KPI 取大写 key；② offsite：普通列直取；③ Walmart：`REGEXP_EXTRACT(sku_id, r'^(?:WM-|W-M)(.+)-AY[A-Z0-9]+$')` 提取内部 SKU；④ Petco：直接复用 `dwd_mkt_petco_ad_spend_di` 分摊后结果。
- 关键规则: ① channel_id 打标 p004(Chewy)/p002(Walmart)/p003(Petco)；② 套包分摊——关联 `dim_prd_bundle_info` 后 `spend * coalesce(bmap_percent, 1)`，有套包按比例拆分费用；③ 无归因渠道（Petco）direct_sales/total_orders 置 NULL，cpc 用 `SAFE_DIVIDE(spend, clicks)` 计算；④ 更新策略全量覆盖。

#### dwd_mkt_chewy_ad_spend_di
- 目标表: `dwd.dwd_mkt_chewy_ad_spend_di`（Chewy 广告花费明细，推广商品级）
- 上游: `ods.chewy_promoted_products`（onsite）、`ods.chewy_offsite_promoted_products`（offsite）、`ods.import_dim_vendor_sku_mapping`、`ods.import_dim_sps_vendor`
- 清洗逻辑: onsite 日期 `MM/DD/YYYY` 字符串按年-月-日重组为 DATE（空串置 NULL）；`REGEXP_REPLACE(spend, r'[^0-9.-]','')` 剥离货币符号后 CAST NUMERIC；offsite 直接取 data_date/cost。
- 关键规则: vendor 映射链路：sku → `channel_vendor_code` → `import_dim_sps_vendor` 补 vendor_name/country_code；`chewy_ad_type` 打标 onsite/offsite。

#### dwd_mkt_chewy_campaign_perf_di
- 目标表: `dwd.dwd_mkt_chewy_campaign_perf_di`（Chewy 广告活动表现汇总）
- 上游: `ref(dwd_mkt_chewy_onsite_campaign_perf_di)`、`ref(dwd_mkt_chewy_offsite_campaign_perf_di)`
- 清洗逻辑: 两个子模型 UNION ALL，前缀常量 `chewy_ad_type`（'onsite'/'offsite'），字段一一对齐。
- 关键规则: 纯合并层，无额外业务逻辑；列结构完全一致（含 autoship 专项指标、new_to_brand_customers 等）。

#### dwd_mkt_chewy_campaign_sidebar_di
- 目标表: `dwd.dwd_mkt_chewy_campaign_sidebar_di`（Chewy sidebar 商品×活动粒度）
- 上游: `ods.chew_campaign_product_performance_from_sidebar`（onsite）、`ods.chewy_offsite_products_sidebar`（offsite）、`ods.import_dim_vendor_sku_mapping`
- 清洗逻辑: 与 `dwd_mkt_campaign_product_perf_di` 的 Chewy 段同构——onsite 解析 `SAFE.PARSE_JSON(value)` + campaigns 数组展开 + KPI 大写 key；offsite 直取。
- 关键规则: channel_id 固定 'p017'；onsite 按 `skuid` + channel_code='p017' 映射 vendor_sku_mapping 补 hicc_sku；过滤 `value IS NOT NULL`。

#### dwd_mkt_chewy_keyword_perf_di
- 目标表: `dwd.dwd_mkt_chewy_keyword_perf_di`（Chewy 关键词广告表现）
- 上游: `ods.chew_campaign_keyword_performance`
- 清洗逻辑: `JSON_VALUE(value, '$.kpis.XXX')` 解析曝光/点击/花费/订单/销售额/新客/LTV/定期购指标。
- 关键规则: ① 计算类指标（CTR/CPC/CVR/ROAS/ACOS/LTV_ROAS）在源表已注释禁用，仅保留原始 KPI；② 一个笔误字段 `$.kpis_ACCRUED_ORD_ACCRUED_ORDERS` 取定期购累计订单；③ channel_code 置空格占位。

#### dwd_mkt_chewy_offsite_campaign_perf_di
- 目标表: `dwd.dwd_mkt_chewy_offsite_campaign_perf_di`（Chewy 站外活动表现）
- 上游: `ods.chewy_offsite_campaign_performance_from_sidebar`
- 清洗逻辑: `JSON_VALUE(value, '$.xxx')` 解析小写 key（campaign_id/status/budget/advertiser_cost/direct_sales/roas/ltv_roas 等）；`SAFE.PARSE_TIMESTAMP('%Y-%m-%d', effective_start_date)` 解析 start_date。
- 关键规则: 站外无 autoship 专项指标（置 NULL）、无 avg_position/products；过滤 `value IS NOT NULL`；etl_time 北京时。

#### dwd_mkt_chewy_onsite_campaign_perf_di
- 目标表: `dwd.dwd_mkt_chewy_onsite_campaign_perf_di`（Chewy 站内活动表现）
- 上游: `ods.chewy_onsite_campaign_performance_from_sidebar`
- 清洗逻辑: `JSON_VALUE(value, '$.kpis.XXX')` 解析大写 KPI（IMPRESSIONS/CLICKS/SPEND/DIRECT_SALES/CTR/DIRECT_ROAS/LTV_SALES/LTV_ROAS/AVG_POSITION/AUTOSHIP_* 等）；start_date 用 ISO8601 格式 `%Y-%m-%dT%H:%M:%E*SZ` 解析；products 用 `JSON_QUERY` 保留 JSON。
- 关键规则: 站内指标最全（含 autoship_conversion_rate、new_to_brand_customers、avg_position）；过滤 `value IS NOT NULL`。

#### dwd_mkt_lazada_adgroup_perf_di
- 目标表: `dwd.dwd_mkt_lazada_adgroup_perf_di`（Lazada 广告组花费明细）
- 上游: `ods.lazada_adgroup_report`、`ods.import_dim_country`、`ref(dim_exchange_rates)`
- 清洗逻辑: `spend * e.to_usd_rate AS spend_usd` 按月度汇率折算 USD；`DATE_TRUNC(stat_date, MONTH) = e.fdate` 关联汇率。
- 关键规则: 国家维度 `upper(t.country_code)` 关联 `import_dim_country` 取 currency_code，再由币种→汇率；`short_code` 作 dim_shop_id；保留原始 spend 与 exchange_rate_usd 供对账。

#### dwd_mkt_petco_ad_spend_di
- 目标表: `dwd.dwd_mkt_petco_ad_spend_di`（Petco 广告花费，creative×SKU 分摊）
- 上游: `ods.petco_ads_item_v`（item 金额）、`ods.petco_ads_creative_v`（creative 维度）、`ref(dim_mkt_petco_creative_mapping)`（手工映射）、`pdt_ods.product_skus_purchase`（采购价）、`ods.import_dim_sps_vendor`
- 清洗逻辑: item 表按 `ad_item_id+campaign_id+date` 关联 creative 表发散到 creative 级；再 join creative→SKU 映射；计算 `SUM(cost_price) OVER(PARTITION BY ad_item_id, fdate)` 与分摊比例 `cost_price/total_cost`，`raw_spend * allocation_ratio` 得分摊后花费。
- 关键规则: ① 无映射 SKU 时采购价兜底 `0.001`（保证 item 总金额被分摊完）；② 映射仅取 `LENGTH(hicc_sku) > 3` 的有效行；③ dim_vendor_code 固定 '169564'；④ dim_channel_code 固定 'p017'；⑤ 分摊比例在 total_cost<=0 时置 1。

#### dwd_mkt_shopee_campaign_perf_di
- 目标表: `dwd.dwd_mkt_shopee_campaign_perf_di`（Shopee 广告活动日花费）
- 上游: `ods.shopee_campaign_daily_performance`、`ods.import_dim_country`、`ref(dim_exchange_rates)`
- 清洗逻辑: `COALESCE(oer.to_usd_rate, 1) * expense AS expense_usd` 月度汇率折算（汇率缺失兜底 1）。
- 关键规则: 过滤 `expense > 0`；country 由 `region` 关联（a.region = dc.country_code）；dim_channel_code 固定 'p007'；保留 create_time/update_time。

#### dwd_mkt_shopify_ga4_spend_di
- 目标表: `dwd.dwd_mkt_shopify_ga4_spend_di`（Shopify GA4 广告花费）
- 上游: `ods.ga4_ad_spend`（花费）、`ods.ga4_channel_items`（商品表现）、`ref(dim_sku_mapping)`
- 清洗逻辑: 花费表按 `report_date + channel_group` 关联商品表现表；SKU 映射用 `SPLIT(item_id, '_')[OFFSET(3)]` 截取 item_id 第 4 段作 channel_sku_id 关联 `dim_sku_mapping`。
- 关键规则: 过滤 `ad_cost > 0`；dim_country_code 固定 'US'；保留 item_id/item_name/item_revenue/items_purchased 原始表现字段。

#### dwd_mkt_tk_item_group_perf_di
- 目标表: `dwd.dwd_mkt_tk_item_group_perf_di`（TikTok 商品组表现）
- 上游: `ods.tk_product_item_group_reports`、`ods.tk_products`、`ref(dim_product_skus_sales)`、`ods.tk_ads_store`
- 清洗逻辑: `substr(stat_time_day, 1, 10)` 截取日期；商品组→SKU：`tk_products.skus` JSON 数组取 `$[0].id` 作 channel_sku_code，再按 channel_code='p009' 映射 `dim_product_skus_sales` 补 hicc_sku；`JSON_EXTRACT_SCALAR(campaign_ids, '$[0]')` 取第一个 campaign_id。
- 关键规则: 过滤 `cost > 0`；dim_country_code 固定 'US'；store_code 作 dim_shop_id；保留 bid_type/product_status/report_type 等状态维度。

#### dwd_mkt_walmart_campaign_perf_di
- 目标表: `dwd.dwd_mkt_walmart_campaign_perf_di`（Walmart 广告活动×商品表现）
- 上游: `ods.walmart_compaign_item_performance_rpa`（RPA 采集）
- 清洗逻辑: 全字段 `SAFE_CAST`（NUMERIC/INT64/FLOAT64）标准化；id/campaign_id/ad_group_id/item_id 转 STRING。
- 关键规则: 完整保留归因字段——广告/非广告/总加购（add_to_cart）、详情页浏览、归因销售额、店内归因销售额/件数/订单、roas/omni_roas 等；etl_time 北京时。

#### dws_mkt_global_ad_spend_di
- 目标表: `dws.dws_mkt_global_ad_spend_di`（全渠道广告花费汇总）
- 上游: `ref(dwd_mkt_amazon_ad_perf_di)` / `ref(dws_mkt_shopee_campaign_perf_di)` / `ref(dws_mkt_lazada_adgroup_perf_di)` / `ref(dwd_mkt_tk_item_group_perf_di)` / `ref(dwd_mkt_walmart_campaign_perf_di)` / `ref(dwd_mkt_chewy_campaign_sidebar_di)` / `ref(dwd_mkt_petco_ad_spend_di)` / `ref(dwd_mkt_shopify_ga4_spend_di)`
- 清洗逻辑: 8 渠道 UNION ALL，各自按维度 GROUP BY 聚合 `SUM(spend_usd)`，输出统一列集（fdate/channel/country/sku/channel_sku/shop/ad_type/spend_usd）。
- 关键规则: ① 每段硬编码 `data_source_name` 溯源（如 'dwd_mkt_amazon_ad_perf_di'）；② 渠道归一：Shopee 取分摊后 `expense_allocated_usd`、Lazada 取 `spend_allocated_usd`；③ 无渠道 SKU 的渠道用占位 shop_id（Walmart '3509afb2'、Chewy 'chewy1'、Petco 'petco1'、Shopify 'shopify_US'）；④ Walmart/Petco/Shopify 国家硬编码 'US'。

#### dws_mkt_lazada_adgroup_perf_di
- 目标表: `dws.dws_mkt_lazada_adgroup_perf_di`（Lazada 广告花费 SKU 分摊）
- 上游: `ref(dwd_mkt_lazada_adgroup_perf_di)`、`ods.lazada_order_items`、`ref(dim_product_skus_sales)`、`ref(dim_product_skus)`
- 清洗逻辑: ① 广告组 itemId 经 `lazada_order_items`（product_id→sku 去重）关联卖家 SKU；② 按 channel_code='p006' 映射 hicc_sku（无映射 'UNKNOWN'）；③ 采购价兜底 `0.01`；④ `spend_usd * purchased_cost_price / SUM(purchased_cost_price) OVER(PARTITION BY fdate, campaign_id, spuid)` 分摊。
- 关键规则: 分摊维度是广告组×商品（spuid）；输出 allocated_ratio 与 total_cost 供审计。

#### dws_mkt_shopee_campaign_perf_di
- 目标表: `dws.dws_mkt_shopee_campaign_perf_di`（Shopee 广告花费 SPU→SKU 分摊）
- 上游: `ref(dwd_mkt_shopee_campaign_perf_di)`、`ref(dim_mkt_campaign)`、`ods.shopee_order_detail`、`ref(dim_product_skus_sales)`、`pdt_ods.product_skus_purchase`
- 清洗逻辑: ① `shopee_order_detail.item_list` JSON 展开，`model_id=0` 时用 item_id 否则用 model_id 作 channel_sku_code（SPU→SKU 口径）；② 映射 hicc_sku + 采购价（兜底 0.01）；③ 活动表关联 `dim_mkt_campaign` 得 item_id（spuid）；④ `expense_usd * SAFE_DIVIDE(sku_price, SUM(sku_price) OVER(PARTITION BY fdate, spuid))` 分摊。
- 关键规则: ① 只取 `pay_time IS NOT NULL` 的已支付订单；② 无 SKU 映射时（dim_hicc_sku_code IS NULL）费用全额挂到该 SPU 不分摊；③ `SAFE_DIVIDE` 防除零。

---

## 07_fnc 财务域

### 通用清洗规则

- **日期解析**：SPS 系文本日期 `MM/DD/YYYY` 统一 SPLIT 重组为 DATE（空串→NULL）；Chewy rebate 的 `%d/%m/%Y` 为日月年顺序，单独处理。
- **状态/字典映射**：`CASE WHEN` 将枚举码映射为业务名称（如 bill_status 1/2/3/4 → Not Billed/Partial Billed/Billed/Cancelled；carrier_service_id → FedEx/UPS 承运商名）。
- **JSON 解析**：QuickBooks 系从 header/traits/custom_fields/items JSON 抽取字段，自定义字段用"按 definition.name 过滤 + MAX 聚合 pivot"避免数据膨胀。
- **金额分摊**：QuickBooks 发票行金额按 `line_amount / SUM(line_amount) OVER(PARTITION BY invoice_id)` 比例分摊发票总额，行数与金额都对账。
- **多源对账打标**：SPS PO × Shipout 出库 × QuickBooks 发票三方关联，输出 SKU 级与 PO 级"发货状态 + 发票状态"标签。
- **费用科目名称标准化**：Chewy rebate 按名称长度与协议关键字映射出平台折扣费科目。

### 各表清洗逻辑

#### dwd_fnc_chewy_rebate_di
- 目标表: `dwd.dwd_fnc_chewy_rebate_di`（Chewy 返利/折扣科目）
- 上游: `ods.sps_chewy_rebate`
- 清洗逻辑: `PARSE_DATE('%d/%m/%Y', invoice_date)` 解析发票日期（日月年）；rebate_name 标准化。
- 关键规则: ① 费用科目映射——`length(rebate_name) <= 5` 且 `agreement_name like '%off%'` → 'platform_discount_fee'；`length(rebate_name) <= 5` 取 agreement_name；否则取 rebate_name；② 保留 rebate_name_origin/agreement_name_origin 原始值；③ rebate_amount 即科目费用。

#### dwd_fnc_ezzeship_postfee_di
- 目标表: `dwd.dwd_fnc_ezzeship_postfee_di`（Ezzeship 海外仓物流费）
- 上游: `ods.ezzeship_postfee_deal_detail`
- 清洗逻辑: `order_number` 关键词匹配映射平台（Chewy/Petco/iHerb/Vitacost/IBR/GPE/PSG/Woof Life/Petland/Sales Samples/等 14 个）；`date(created_time)` 取 fdate；`SPLIT(tracking_numbers, ',')[SAFE_OFFSET(0)]` 取首单号。
- 关键规则: ① bill_status 映射：'1'→Not Billed、'3'→Billed、'4'→Cancelled、'2'→Partial Billed；② 承运商映射：'34'→FedEx Home Delivery、'33'→FedEx Ground、'19'→UPS Worldwide Express Saver；③ 海外仓发货费计算——`bill_status='3'` 取 billed_amount、'1' 取 hold_amount、'2' 取 hold+billed 合计、其余 0（取消不计费）。

#### dwd_fnc_quickbooks_invoice_allocated_di
- 目标表: `dwd.dwd_fnc_quickbooks_invoice_allocated_di`（QuickBooks 发票金额分摊到行）
- 上游: `ref(dwd_fnc_quickbooks_invoice_item_di)`（行明细）、`ref(dwd_fnc_quickbooks_invoice_di)`（发票头）
- 清洗逻辑: 行明细按 `invoice_id` 关联发票头；`SAFE_DIVIDE(line_amount, SUM(line_amount) OVER(PARTITION BY invoice_id)) * list.amount` 将发票总额按行金额占比分摊。
- 关键规则: 输出 list_po_number / list_invoice_number / list_txn_date / list_amount 供对账；`SAFE_DIVIDE` 防除零。

#### dwd_fnc_quickbooks_invoice_di
- 目标表: `dwd.dwd_fnc_quickbooks_invoice_di`（QuickBooks 发票头）
- 上游: `ods.quickbooks_transactions`
- 清洗逻辑: `JSON_VALUE(header, '$.xxx')` 解析 transactionType/txnStatus/referenceNumber/txnDate/amount；嵌套 `$.contact.displayName`、`$.currencyInfo.currency/homeAmount`；`JSON_VALUE(traits, '$.balance.dueDate')` 等解析余额/到期/发货/税务。
- 关键规则: ① custom_fields 用**标量子查询**按 `definition.name`（udcf_1000000001/03/04）取值，避免行数膨胀；② amount 转 FLOAT64、due_date/ship_date 转 DATE。

#### dwd_fnc_quickbooks_invoice_item_di
- 目标表: `dwd.dwd_fnc_quickbooks_invoice_item_di`（QuickBooks 发票行明细）
- 上游: `ods.quickbooks_invoice_details`
- 清洗逻辑: `SAFE.PARSE_JSON(full_response)` 解析；`UNNEST(JSON_QUERY_ARRAY(json_data.data.node.lines.itemLines.edges))` 展开行项；customFields 先 pivot（按 `$.definition.schema.title` 过滤 + `MAX(CASE WHEN...)`）再 LEFT JOIN。
- 关键规则: ① 仅取 `status = 'active'` 的发票；② 行项字段 SKU/quantity/line_amount 用 JSON_VALUE + SAFE_CAST；③ 自定义字段 pivot 出 PO Number / requested delivery date / Ship notice number / PO Acknowledgement date / invoice number 五个业务字段。

#### dwd_fnc_sps_invoice_detail_di
- 目标表: `dwd.dwd_fnc_sps_invoice_detail_di`（SPS 发票明细）
- 上游: `ods.sps_invoice_detail_i`
- 清洗逻辑: 三个日期字段（Invoice_Date/PO_Date/Requested_Ship__Delivery_Date）`MM/DD/YYYY` SPLIT 重组为 DATE（空串→NULL）；其余字段直通。
- 关键规则: `WHERE Record_Type = 'H'` 只保留头记录；`SAFE_CAST(Invoice_Total AS FLOAT64)` 金额化；保留 allow_charge（津贴/收费）、payment_terms（账期）、tax 等完整商务字段。

#### dwd_fnc_subject_records_di
- 目标表: `dwd.dwd_fnc_subject_records_di`（科目费用记录）
- 上游: `ods.import_financial_subject_records`
- 清洗逻辑: 字段直通（id/record_date/subject_name/amount/created_at/updated_at）。
- 关键规则: 无加工，纯 DWD 直通层。

#### dws_fnc_sps_order_flag_di
- 目标表: `dws.dws_fnc_sps_order_flag_di`（SPS 采购订单发货/发票状态打标）
- 上游: `ref(dwd_scm_sps_po_detail_di)`、`ref(dwd_scm_shipout_outbound_txn_di)`、`ref(dwd_scm_winit_outbound_di)`、`ref(dwd_fnc_quickbooks_invoice_allocated_di)`
- 清洗逻辑: ① 出库汇总——shipout 与 winit 两个 DWD 层表 UNION ALL 后按 `sps_po_number + dim_hicc_sku_code` 聚合（MAX 发货日期、SUM 出库量、STRING_AGG 去重物流单号）；② 发票汇总——按 `list_po_number + sku` 聚合 quantity/line_amount/allocated 金额；③ PO 级汇总后二次打标。
- 关键规则: ① **SKU 级发货状态**：Qty_Ordered = 出库量 → 'Shipped'；出库为 NULL → 'Not Shipped'；大于 → 'Partially Shipped'；小于 → '!Over Shipped'；② **SKU 级发票状态**：tot_amount = 发票金额 → 'Invoiced'；NULL → 'Pending Invoice'；大于 → 'Partially Invoiced'；小于 → '!Over Invoiced'；③ PO 级状态同理基于 sps_order_qty/amount；④ winit 出库只取 `status IN ('DLC','OBC')`；⑤ 过滤 `po_date >= '2026-01-01'`。

---

## 08_scm 采购供应域

### 通用清洗规则

- **JSON 行项展开**：领星系（采购单/入库单/出库单）均 `LEFT JOIN UNNEST(JSON_QUERY_ARRAY(item_list))` 将子项展开为行，`JSON_VALUE(item, '$.xxx')` 取子项标量；物流系（德邦/滴答滴）展开 `logistics_list` / `trace_info` 数组。
- **金额计算（采购单价 × 数量）**：领星 PO 金额 = `quantity_xxx * COALESCE(cg_price, 0)`（CNY）；出库金额 = `Outbound_Stock_qty * purchased_cost_price`（CNY）。
- **汇率折算**：B2B HK/SG 币种按 `dim_exchange_rates` 月度 `to_usd_rate` 折 USD；shipout 头程/采购成本按 `(cost/rate)*100` 折 USD。
- **多平台轨迹统一（核心）**：佳成/凯奇/美琦/美通/极智佳/美易/商壹/世宽/滴答滴/德邦 10 个物流平台 ODS 各自解析轨迹文本（`regexp_contains` 关键词：'已收货'/'报关'/'已开船'/'已到港'/'已签收'/'提柜'/'拆柜'/'查验'/'放行'/天气等），聚合出 collect_cargos_date / cus_dec_date / ETD / ETA / ATD / ATA / expected_delivery / actual_delivery / bad_weather_date / retrieval_date / clearance_date / devanning_date / export(import)_check_date 等关键节点日期，再 UNION ALL 到统一 schema。
- **跨年校正**：ETD/ETA/预计派送从纯文本提取的日期若月份早于事件时间月份，`DATE_ADD(..., INTERVAL 1 YEAR)` 补一年（美易在 udf 内部 adjustYear 已校正，避免双倍叠加）；极智佳/美易用 `parse_date` 拼事件时间年份。
- **抽取 UDF**：`dwd.udf_extract_etd/eta/atd/ata/expected_delivery/actual_delivery/devanning_date/cus_dec_date` 等 BigQuery 注册函数解析文本中的日期。
- **货件号清洗**：shipment_id 多轮清洗（去 `E-`/`W-` 前缀、FBA 前缀补齐到 12 位、去 meta/sgr 营销号、按 `+`/`,` 拆分多货件号）；`dim_scm_shipment_mapping` 新旧货件号映射统一。
- **渠道/国家四层 fallback**：采购单渠道国家按 ①stockplan 精确匹配 plan_sn → ②STRPOS 模糊匹配 → ③产销协同 plan_remark（`$p001$CA` 格式解析）→ ④工厂未交货订单 contract_number 的顺序取数。
- **剔除规则**：`status_text NOT IN ('已作废')`；`status NOT IN ('DLC','OBC')` 反向过滤等。

### 各表清洗逻辑

#### dim_scm_inbound_close_manual
- 目标表: `dim.dim_scm_inbound_close_manual`（手工关闭入库单号）
- 上游: 无（手工维护）
- 清洗逻辑: `{{ config(enabled=false) }}` 模型禁用，实际数据为 INSERT 语句维护的 shipment_id 黑名单（手工关闭单号）。
- 关键规则: 用于下游排除已手工关闭的运单。

#### dim_scm_shipment_exclusive
- 目标表: `dim.dim_scm_shipment_exclusive`（排除运单号）
- 上游: 无（手工维护）
- 清洗逻辑: `enabled=false`；手工 INSERT 排除清单（已送达可忽略/小包订单忽略/样品订单）。
- 关键规则: `dws_scm_shipment_abnormal_data_di` 中 `t2.shipment_id is null` 排除这些运单。

#### dim_scm_shipment_mapping
- 目标表: `dim.dim_scm_shipment_mapping`（新旧货件号映射）
- 上游: 无（手工维护）
- 清洗逻辑: `enabled=false`；手工 INSERT old→new 货件号映射（如 IBR576621486 → FBA19DKR5D4X 等）。
- 关键规则: `dwd_scm_shipment_order_di` 中 `coalesce(t4.new_shipment_id, t1.shipment_id)` 归一货件号。

#### dim_scm_supplier
- 目标表: `dim.dim_scm_supplier`（供应商维表）
- 上游: `ods.lingxing_amazon_po_order_list`
- 清洗逻辑: `SELECT DISTINCT supplier_id(转 STRING), supplier_name`。
- 关键规则: 从采购单源表取供应商字典，去重。

#### dwd_scm_amazon_po_order_snap
- 目标表: `dwd.dwd_scm_amazon_po_order_snap`（领星 PO 增量快照）
- 上游: `ods.lingxing_amazon_po_order_list`
- 清洗逻辑: `main.* EXCEPT(synctime)` 剔除同步时间列；追加 `business_time` 与分区字段 `fdate_p = current_date()`。
- 关键规则: 增量物化 `insert_overwrite` + `fdate_p(date)` 分区；快照模型是 amazon_po_order_di 的底座。

#### dwd_scm_amazon_po_order_di
- 目标表: `dwd.dwd_scm_amazon_po_order_di`（领星亚马逊 PO 采购订单明细）
- 上游: `ref(dwd_scm_amazon_po_order_snap)`、`pdt_ods.product_skus_purchase`、`pdt_ods.stockplan_list`、`ods.lingxing_purchase_plan`、`ods.import_scm_undelivered_order_details`、`ods.lingxing_amazon_product_info`、`pdt_ods.dim_channel/dim_country`
- 清洗逻辑: ① snap 的 `item_list` JSON 展开为 SKU 行；② 金额 = `quantity_real/entry/receive × COALESCE(cg_price,0)`（CNY）；③ 渠道国家四层 fallback；④ `lingxing_purchase_plan` 补 ppg_sn。
- 关键规则: ① 剔除 `status_text = '已作废'`；② **pending_production_qty = quantity_receive**（待到货量替代原工厂手工待生产量）；③ 工厂手工填报字段（finished/delivered/undelivered/semi_finished_quantity 及金额）全部弃用置 0；④ `COALESCE(stockplan_exact, stockplan_fuzzy, purchase_plan_remark, uodp_channel_country)` 逐级取渠道/国家，且后级 join 均要求前级未命中（`xxx.plan_sn IS NULL`）；⑤ SKU 映射键为 `purchase_sku_code = item_list.sku`。

#### dwd_scm_b2b_po_import_di
- 目标表: `dwd.dwd_scm_b2b_po_import_di`（B2B 渠道 PO 导入：HK/SG）
- 上游: `ods.import_b2b_channel_hk_po_main`、`ods.import_b2b_channel_sg_po`、`ods.import_sps_hk_20260331_154520`、`ods.import_sps_hk_20260410_185955`、`ref(dim_exchange_rates)`、`ods.import_dim_sps_vendor`
- 清洗逻辑: HK（主表+2 张手工月表）+ SG 四段 UNION ALL；`total_amount_hkd * er.to_usd_rate AS tot_amt_usd` 月度汇率折算；`business_name = vendor.Vendor_name` 映射 vendor_code。
- 关键规则: ① 手工表按日期命名（2026-03-31/2026-04-10 导入），是临时补齐数据；② SG 段直接用 channel_code 作 vendor_code；③ 保留 currency_code 供追溯。

#### dwd_scm_lingxing_purchase_receipt_di
- 目标表: `dwd.dwd_scm_lingxing_purchase_receipt_di`（领星采购入库单明细）
- 上游: `ods.lingxing_purchase_receipt_order`、`pdt_ods.product_skus_purchase`
- 清洗逻辑: 订单头字段直通；`item_list` JSON 展开子项（sku/fnsku/notice_num_total/product_receive_num/quantity_qc_* 等）；`purchase_sku_code` 映射 hicc_sku。
- 关键规则: 状态字段保留原始值（status：10-待质检/40-已完成；qc_type：1-需质检；quality_examine_status：2-已质检）；`inbound_order_sns`/`qc_sn` 为 JSON 数组字段保留；etl_time 北京时。

#### dwd_scm_shipment_order_di
- 目标表: `dwd.dwd_scm_shipment_order_di`（多平台物流运单统一）
- 上游: `ods.jcex_orders`+`ods.jcex_order_tracking_info`（佳成）、`ods.kqgyl_orders`+`ods.kqgyl_order_tracking_v`（凯奇）、`ods.mqgj_workorder_list`+`_detail`+`mqgj_workorder_logistics_v`（美琦）、`ods.mt_order_list`+`mt_order_logistics`（美通）、`ods.ypl_order_list`+`ypl_order_detail_v`（极智佳）、`ods.mygj_order_list`+`mygj_order_track_v`（美易）、`ods.sygj_order_list`+`sygj_logistics`（商壹）、`ods.skgj_order_list`+`skgj_order_tracking`（世宽）、`ods.debang_order_list`+`debang_order_detail`（德邦）、`ods.didadi_order_list`+`didadi_order_trace`（滴答滴）、`dwd.dwd_lingxing_amazon_shipment_details_v`、`ref(dwd_inv_winit_inbound_txn_di)`、`static_dim.dim_scm_shipment_mapping`、`ods.shipping_cargo_arch`
- 清洗逻辑: 10 平台各自解析轨迹聚合关键节点日期（详见通用规则），UNION ALL 后统一 LEFT JOIN 仓库国家、目的国映射、新旧货件号映射、报关单信息。
- 关键规则: ① shipment_id 归一——`coalesce(t4.new_shipment_id, t1.shipment_id)` 且 join 时 `regexp_replace(shipment_id, r'(?i)^sgr-','')`；② 状态取最新轨迹（ROW_NUMBER 按 event_time DESC rn=1）；③ 各平台状态文本关键词映射统一为 collect/cus_dec/atd/ata 等节点；④ export_check_date 仅在早于实际离港时才取值（`< coalesce(atd, clearance_date, ..., '9999-12-31')`）；⑤ 报关单聚合按 platform+key（美易用 waybill_no，其余用 order_id）STRING_AGG 多单号；⑥ 滴答滴剔除 `jobno like '%-B%'` 补费订单；世宽剔除 '预报订单'。

#### dwd_scm_shipment_order_extend_di
- 目标表: `dwd.dwd_scm_shipment_order_extend_di`（运单扩展：时效与货件号清洗）
- 上游: `ref(dwd_scm_shipment_order_di)`、`ref(dim_scm_shipping_time)`、`ref(dwd_inv_tk_inbound_txn_di)`、`ref(dwd_inv_amazon_inbound_txn_di)`、`ods.shipping_cargo_arch`
- 清洗逻辑: ① shipment_id 多轮清洗（FBA 前缀补齐 `substr(concat('FBA',clean),1,12)`、去 meta/sgr 号、按 `+`/`,` 拆分展开）；② start_count_date 周对齐——以 collect_cargos_date 前 2 天所在周的周一为准（`date_sub(..., interval (dayofweek-4) day)`）；③ 各时效天数 `date_diff(actual_delivery, 节点, day)`（collect2deli/real_collect2deli/cus2deli/atd2deli/ata2deli/exp2deli）。
- 关键规则: ① `dim_scm_shipping_time` 匹配标准运输方式与配置时效天数（FBA 渠道跳过 cat 匹配）；② 剔除状态含 '取消'/'退' 的运单；③ 剔除清洗后 FBA 号不足 12 位的异常行；④ 剔除 raw 与 clean 均为 meta/sgr 开头的营销单；⑤ warehouse_id 用 `coalesce(t2(入库表), t1)` 补全。

#### dwd_scm_shipment_track_dates_di
- 目标表: `dwd.dwd_scm_shipment_track_dates_di`（各平台关键节点日期明细）
- 上游: `ods.jcex_dates_from_order_tracking_info`、`ods.kqgyl_order_tracking_v`、`ods.mqgj_workorder_logistics_v`、`ods.mt_order_logistics`、`ods.ypl_order_detail_v`、`ods.mygj_order_track_v`、`ods.sygj_logistics`
- 清洗逻辑: 7 平台 UNION ALL，各自按关键词/status_name/scan_code 提取 collect/cus_dec/etd/eta/atd/ata/expected/actual 八个节点日期。
- 关键规则: ① ETD/ETA 跨年校正（美通/美易/商壹：`extract(month from etd) < extract(month from event_time)` 时 +1 年）；② 极智佳/美易对 `MM/DD` 短日期用事件时间年份拼补；③ 过滤整行全 NULL 日期；④ 美通 etd/eta 从 content 正则提取两个 `YYYY-MM-DD` 分别取第 0/1 个。

#### dwd_scm_shipment_track_node_di
- 目标表: `dwd.dwd_scm_shipment_track_node_di`（物流轨迹节点明细）
- 上游: 10 平台轨迹 ODS（jcex/kqgyl/mqgj/mt/ypl/mygj/sygj/skgj/didadi 等）
- 清洗逻辑: 各平台字段统一映射为 platform_name/order_id/node_name/content/event_time；滴答滴 `UNNEST(json_extract_array(trace_info))` 展开 + `SAFE.PARSE_TIMESTAMP('%Y/%m/%d %H:%M', scanTime)`。
- 关键规则: 关联 `dwd_scm_shipment_order_extend_di` 补 shipment_id，供下游轨迹回溯。

#### dwd_scm_shipout_billing_txn_di
- 目标表: `dwd.dwd_scm_shipout_billing_txn_di`（Shipout 账单流水）
- 上游: `ods.shipout_transactions`
- 清洗逻辑: `UNNEST(JSON_EXTRACT_ARRAY(response, '$.data.records'))` 展开记录，再 `LEFT JOIN UNNEST(skuInfoList)` 展开 SKU 行；`total_amount / COALESCE(NULLIF(ARRAY_LENGTH(skuInfoList), 0), 1)` 按 SKU 行数均分金额。
- 关键规则: ① 物流费 `shipping_amount` 仅当 `feesBizType = '6'` 且 `status IN ('2','1')` 才计入，其余 0；② 状态 '3' 为取消不计费；③ 均分时 skuInfoList 为空/为 null 则除以 1（保留原金额）。

#### dwd_scm_shipout_outbound_txn_di
- 目标表: `dwd.dwd_scm_shipout_outbound_txn_di`（Shipout 出库流水：大货+小包）
- 上游: `ods.shipout_freight_order`（大货）、`ods.shipout_outbound_order`（小包）、`ref(dim_prd_shipout_product)`、`ref(dwd_scm_sps_po_detail_di)`、`ods.import_scm_sku_first_leg_cost_config`、`ref(dim_exchange_rates)`
- 清洗逻辑: 大货/小包两段 UNION ALL；items/sku_item_list JSON 展开；`Outbound_Stock_qty = qty × convert_rate`（mate 仓库换算率恒 1）；金额 = 数量 × 采购价（CNY）；头程/采购成本 USD = `(cost/rate)*100 × qty`。
- 关键规则: ① **时区转换**——fdate 按仓库时区：mate 仓(1845...201)→美西 `America/Los_Angeles`、sgr 仓(1643...001)→美东 `America/New_York`、fdate_cn 恒为 `Asia/Shanghai`；② 订单类型映射（大货）：destination_type=1→FBA、order_nos 含 WFA/GDM→Walmart-WFS、含 walmart/WMT→Walmart-代发、IBR→Tiktok-FBT、含 Tiktok/57→Tiktok-代发、Chewy/iHerb/Petco/Vitacost 关键词匹配，其余 'other'；小包另有 Shopify(#/103 开头)/Temu(PO-211)/KOL/PetsB2BDirect/AAFES 规则；③ 只取 `status IN (6,9)`（小包还要求 shipped_time 非空）；④ SPS PO 关联：`order_nos LIKE '%' || po_number || '%'` 模糊匹配；⑤ 成本配置按仓库与箱型选择（w002→不含内箱；w003+名称含 Inner box→含内箱）。

#### dwd_scm_sps_po_detail_di
- 目标表: `dwd.dwd_scm_sps_po_detail_di`（SPS PO 行明细 + B2B 渠道 UNION）
- 上游: `ods.sps_commerce_orders`（D 记录行 + H 记录头）、`ref(dim_prd_sps_vendor_style)`、`ods.import_dim_sps_vendor`、`ods.import_dim_channel`、`ref(dim_product_skus)`、`ref(dwd_scm_b2b_po_import_di)`
- 清洗逻辑: ① D 记录（行）关联 H 记录（头，按 po_number 聚合 MAX）透传 PO 头信息；② 日期 `MM/DD/YYYY` 重组；③ `tot_amount = unit_price × qty_ordered`；④ 箱规换算——`Unit_of_Measure != 'Each'` 时 `Qty_Ordered × unit_carton_box`；⑤ `ROW_NUMBER() OVER(PARTITION BY po_number, po_line_number)` 去重取 1。
- 关键规则: ① 剔除 `vendor_style like '%VPN%'` 及测试 SKU（'123456'/'456123'/'789546'/'987654'）；② 历史脏 SKU（如 ailan03）经 `dim_prd_sps_vendor_style` 映射 hicc_sku，映射不到则用 channel_sku 兜底；③ 供应商→渠道/国家经 import_dim_sps_vendor + import_dim_channel；④ B2B 段列对齐 NULL 填充后 UNION ALL（po_number 置 NULL，fdate 作 po_date）；⑤ Unit_Price 恒 NULL（源无单价）。

#### dws_scm_sps_po_detail_di
- 目标表: `dws.dws_scm_sps_po_detail_di`（SPS PO 明细汇总）
- 上游: `ref(dwd_scm_sps_po_detail_di)`
- 清洗逻辑: 全字段直通（维度+指标原样透出）。
- 关键规则: 无额外加工，供财务/运营直接消费。

#### dws_scm_shipment_abnormal_data_di
- 目标表: `dws.dws_scm_shipment_abnormal_data_di`（运单异常监控）
- 上游: `ref(dws_inv_inbound_shipment_info_di)`、`static_dim.dim_scm_shipment_exclusive`
- 清洗逻辑: 基于未送达运单计算 6 类告警 flag。
- 关键规则: ① **已揽货未报关**：cus_dec/ata/atd 全空且揽货超 7 天；② **已报关未开船**：atd/ata/devanning/clearance 全空且报关超 7 天；③ **超过预约送货日期**：未送达未收货且（预约日期已过 或 拆柜后 7 天）且创建 180 天内；④ **已下单未揽货**：下周二 14 点前未揽货（`datetime_trunc(create_time, week(monday)) + 8 天 + 14 小时`）；⑤ 查验预警/恶劣天气按最新轨迹首行关键词；⑥ 排除 `dim_scm_shipment_exclusive`、已入库关闭、已收货、非本年运单；⑦ 排除 '世宽' 平台；⑧ `alert_type` 按 flag 优先级归一类。

#### dws_scm_shipping_sla_percentile_snap
- 目标表: `dws.dws_scm_shipping_sla_percentile_snap`（运输时效 SLA 分位快照）
- 上游: `ref(dwd_scm_shipment_order_extend_di)`
- 清洗逻辑: 取近 90 天已送达样本（`real_collect2deli_days` 1~120 天、`ROW_NUMBER` 按 shipment_id 去重取最新），按 `shipping_method + warehouse_id` 分组算 `PERCENTILE_CONT(0.75)`。
- 关键规则: ① 样本量 `sample_count >= 10` 时 `is_reliable = true`（分位可用），否则需用默认时效兜底；② `stat_date = current_date()` 每日快照。

---

## 三域共通模式小结

| 模式 | 说明 | 典型模型 |
|------|------|---------|
| JSON 数组展开 | UNNEST 展开 item_list/campaigns/skus/trace_info 等 | dim_mkt_campaign、dwd_scm_amazon_po_order_di、dwd_fnc_quickbooks_invoice_item_di |
| 汇率折算 USD | dim_exchange_rates 月度 to_usd_rate | dwd_mkt_lazada_adgroup_perf_di、dwd_scm_b2b_po_import_di、dwd_scm_shipout_outbound_txn_di |
| UNION ALL 多源合并 | 同实体多来源（平台/爬虫/双表切换） | dwd_mkt_amazon_ad_perf_di、dws_mkt_global_ad_spend_di、dwd_scm_shipment_order_di |
| 金额按比例分摊 | 行/采购价/行数占比分摊 | dws_mkt_shopee_campaign_perf_di、dwd_fnc_quickbooks_invoice_allocated_di、dwd_scm_shipout_billing_txn_di |
| 状态标签 CASE | 枚举码/关键词 → 业务状态 | dwd_fnc_ezzeship_postfee_di、dws_fnc_sps_order_flag_di、dwd_scm_shipout_outbound_txn_di |
| 日期字符串重组 | MM/DD/YYYY、%d/%m/%Y 文本日期转 DATE | dwd_mkt_chewy_ad_spend_di、dwd_fnc_sps_invoice_detail_di、dwd_scm_sps_po_detail_di |
| SKU 映射 | 渠道 SKU → dim_hicc_sku_code（多张映射表） | dwd_mkt_chewy_ad_spend_di、dwd_scm_lingxing_purchase_receipt_di |
| 手工维表/黑名单 | enabled=false + INSERT 手工维护，下游排除/归一 | dim_scm_shipment_exclusive、dim_scm_shipment_mapping |
| 兜底值 | 映射缺失时 0.001/0.01 成本、to_usd_rate=1、'UNKNOWN' | dwd_mkt_petco_ad_spend_di、dws_mkt_lazada_adgroup_perf_di |
| etl_time 北京时间 | CURRENT_TIMESTAMP() + INTERVAL 8 HOUR | 全域通用 |
