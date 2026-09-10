# 销售/退货/商品域 清洗逻辑与规则（01_trd + 06_voc + 03_prd）

> 分析范围：`hicc_data_platform/models/01_trd`（销售域 dwd+dws）、`06_voc`（退货域 dwd+dws）、`03_prd`（商品域 dim+dwd），共 29 个模型 + 6 个 schema.yml。
> 技术栈：BigQuery + dbt。通用模式：JSON 行项展开、标准时间四字段（UTC 基准）、金额折算 USD、SKU 映射、多源合并。

---

## 01_trd 销售域

### 通用清洗规则（该域所有表共用）

- **标准时间四字段**：所有订单模型统一产出 `event_time_utc`（唯一真相源）/ `event_time_cn`（UTC+8）/ `event_date_utc` / `event_date_cn` 四字段；`fdate`（店铺本地时区，旧字段兼容）/ `fdate_cn`（北京时区）两个旧字段保留给下游。
  - 各渠道基准来源不同：Amazon=`purchase_date_local_utc` 字符串 PARSE；Shopify=`created_at` 已是真 UTC；Shopee/TK=`pay_time/paid_time` 秒级 Unix；Lazada/Walmart=`payment_time/order_date` 毫秒级 Unix；HKTVmall=`orderDate` 需做"北京时间→真实 UTC"时区修复。
- **JSON 行项展开**：订单主表 JSON 数组列经 `LEFT JOIN UNNEST(JSON_QUERY_ARRAY(...))` 展开为"一行一商品"（Shopee/TK 额外加 `COLLATE(...,'')` 规避 BigQuery 对陈旧 COERCION 的报错）；金额/数量字段用 `SAFE_CAST`/`CAST` 转 NUMERIC/INT64/FLOAT64。
- **SKU 归一/映射**：普遍通过 `{{ ref('dim_product_skus_sales') }}` 以「渠道 SKU + channel_code（p001/p002/p006/p007/p009/p010/p008）+ 店铺」多键关联得到 `hicc_sku_code`；Amazon 额外从该表带出 `vine_or_not`（Vine 计划标记）。
- **Canceled 剔除与 cancel_date 标记**：Amazon DWD 直接 `WHERE order_status <> 'Canceled'` 剔除；其余渠道保留订单但按状态标记 `cancel_date`（Canceled/CANCELLED/canceled/Cancelled/含 CANCEL 的 consignmentStatus），状态值随渠道拼写不同（Canceled / CANCELLED / canceled / Cancelled）。
- **金额折算 USD**：`{{ ref('dim_exchange_rates') }}` 按 `from_currency = 订单币种 AND fdate = DATE_TRUNC(业务日期, MONTH)` 月度汇率关联，`原币 × to_usd_rate` 得 USD 口径。
- **etl_time**：统一 `FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', CURRENT_TIMESTAMP() + INTERVAL 8 HOUR)`（北京时间）。
- **渠道编码体系**：p001=Amazon、p002=Walmart、p006=Lazada、p007=Shopee、p008=HKTVmall、p009=TK、p010=Shopify、p012=手工单；`biz_type` 区分 TOC（零售）/ TOB（B2B：HKTVmall、手工单）。
- **bundle 套装拆分**（仅 dwd_trd_channel_sku_sales_di）：关联 `dim_prd_bundle_info` 按「channel_sku_code + shop_code + channel_code」三键匹配，用 `bmap_percent` 系数把套餐销量/金额分摊到单品行。

### 各表清洗逻辑

#### dwd_trd_toc_amazon_order_item_di
- 目标表: dwd.dwd_trd_toc_amazon_order_item_di
- 上游: `{{ source('ods', 'lingxing_amazon_api_order_detail_i_v') }}` UNION ALL `{{ source('ods', 'lingxing_amazon_api_order_detail_i_static') }}`（静态历史表限 `purchase_date_local_utc < '2026-01-01'`）
- 清洗逻辑:
  - **双源合并**：增量视图 + 静态历史表（以 2026-01-01 为时间分界）。
  - **JSON 行项展开**：`LEFT JOIN UNNEST(JSON_QUERY_ARRAY(main.item_list)) AS itemlist`，行项字段全部 `JSON_VALUE(itemlist, '$.xxx')` 提取，金额用 `SAFE_CAST ... AS NUMERIC`、数量 `SAFE_CAST ... AS INT64`。
  - **实付金额加工**：`item_price_amount = item_price_amount − promotion_discount_amount − points_monetary_value_amount`（仅日本站有积分，与旧代码一致）。
  - **SKU 映射**：`dim_product_skus_sales`（`shop_id = itemlist.sid` + `channel_code='p001'` + `channel_sku_code = asin`），带出 `dim_hicc_sku_code` 与 `vine_or_not`；店铺信息 `import_dim_shop` 带出国家 `dim_country_code`。
  - **时间字段**：`PARSE_TIMESTAMP(purchase_date_local_utc)` → event_time_utc；+8h → event_time_cn；`fdate` 取 `purchase_date_local`（站点本地日期，领星已按站点转换，无法从 UTC 反推）。
  - **cancel_date**：仅当 `order_status='Canceled'` 时取 `last_update_date`（本地）/ `last_update_date_utc`（北京）。
- 关键规则: **Canceled 剔除**（`WHERE order_status <> 'Canceled'`）；**Vine 标记**透传；双源合并（视图+静态历史）。

#### dwd_trd_toc_shopify_order_item_di
- 目标表: dwd.dwd_trd_toc_shopify_order_item_di
- 上游: `{{ source('ods', 'shopify_orders') }}`、`{{ source('pdt_ods', 'product_skus_sales') }}`
- 清洗逻辑:
  - **JSON 行项展开**：`LEFT JOIN UNNEST(JSON_QUERY_ARRAY(mainorder.line_items)) AS line_item`（LEFT JOIN 防止无行项订单整单丢失）。
  - **渠道 SKU 归一**：`channel_sku_code = REGEXP_REPLACE(variant_id, r'.*/(\d+)', r'\1')`（`gid://shopify/ProductVariant/xxx` → 纯数字）。
  - **行项金额**：`item_price_amount = SAFE_CAST(originalUnitPriceSet.shopMoney.amount AS NUMERIC) × SAFE_CAST(quantity AS INT64)`（原始单价 × 下单数量，必须用 JSON 表达式不能引用别名）。
  - **SKU 映射**：`pdt_ods.product_skus_sales`（`channel_sku_code`=variant_id 数字部分 + `channel_code='p010'`）带出 `dim_hicc_sku_code`。
  - **时间字段**：`created_at` 已是真 UTC（GraphQL 返回 Z 时间，采集仅剥 Z）；`fdate` 按店铺国家切换本地时区（US→America/Los_Angeles、UK→Europe/London、SG→Asia/Singapore）；`fdate_cn` 北京；`cancel_date` 用 `cancelled_at` 按同样规则换算。
  - **字段对齐**：与旧代码 `dwd_ord_shopify_order_line_items` 完全对齐（`seller_sku_code`、`quantity_ordered`、`currency` 等旧字段名），另补 `line_item_*` 新字段。
- 关键规则: 金额区分 **shop（店铺币种）/ presentment（买家支付币种）两套体系**；variant_id gid 提取数字；按店铺国家分时区。

#### dwd_trd_toc_shopee_order_item_di
- 目标表: dwd.dwd_trd_toc_shopee_order_item_di
- 上游: `{{ source('ods', 'shopee_order_detail') }}`、`{{ ref('dim_product_skus_sales') }}`
- 清洗逻辑:
  - **JSON 行项展开**：`LEFT JOIN UNNEST(JSON_QUERY_ARRAY(COLLATE(main.item_list, ''))) AS itemlist`。
  - **渠道 SKU 归一**：`channel_sku_code = CASE WHEN SAFE_CAST(model_id AS INT64) = 0 THEN item_id ELSE model_id END`（model_id=0 时回退取 item_id）。
  - **行项金额**：`item_price_amount = model_discounted_price × model_quantity_purchased`（折扣价 × 数量）。
  - **时间字段**：`TIMESTAMP_SECONDS(pay_time)` → event_time_utc，+8h → cn；`fdate`/`fdate_cn` 均按 `Asia/Shanghai`（与旧代码一致）。
  - **cancel_date**：`order_status='CANCELLED'` 时取 `update_time` 转 Asia/Shanghai 日期。
  - **SKU 映射**：`dim_product_skus_sales`（`channel_sku_code`=归一后的 SKU + `channel_code='p007'`）。
- 关键规则: model_id=0 回退 item_id 的 **SKU 归一规则**；状态值拼写为 `CANCELLED`。

#### dwd_trd_toc_lazada_order_item_di
- 目标表: dwd.dwd_trd_toc_lazada_order_item_di
- 上游: `{{ source('ods', 'lazada_order_items') }}`、`{{ ref('dim_product_skus_sales') }}`
- 清洗逻辑:
  - **类型转换**：全部金额字段（item_price/paid_price/tax_amount/shipping_amount/voucher_*/wallet_credits/supply_price 等）`CAST AS NUMERIC`。
  - **时间字段**：`TIMESTAMP_MILLIS(CAST(payment_time AS INT64))`（毫秒级 Unix）→ event_time_utc，+8h → cn；`fdate`/`fdate_cn` 按 Asia/Shanghai。
  - **cancel_date**：`status='canceled'` 时 `SAFE_CAST(SUBSTR(updated_at,1,10) AS DATE)`。
  - **币种推导**：`country_code='sg'→SGD、'my'→MYR`；`country_code_up = UPPER(country_code)`。
  - **SKU 映射**：`dim_product_skus_sales`（`channel_sku_code=sku_id` + `channel_code='p006'`）。
  - 无 JSON 展开（ODS 已是行项级）。
- 关键规则: **币种从国家代码推导**；毫秒级时间戳转换；状态拼写 `canceled`（小写）。

#### dwd_trd_toc_tk_order_item_di
- 目标表: dwd.dwd_trd_toc_tk_order_item_di
- 上游: `{{ source('ods', 'tk_order_details') }}`、`{{ ref('dim_product_skus_sales') }}`
- 清洗逻辑:
  - **payment_json 解析**：`JSON_VALUE(payment_json, '$.xxx')` 展开税额/运费/折扣等（SAFE_CAST NUMERIC）。
  - **JSON 行项展开**：`LEFT JOIN UNNEST(JSON_QUERY_ARRAY(COLLATE(main.line_items_json, '')))`。
  - **时间字段**：`TIMESTAMP_SECONDS(paid_time)` → event_time_utc，+8h → cn；`fdate` 按 `America/New_York`（美国站）；`fdate_cn` 北京；`cancel_date` 用 `cancel_time` 按同样双时区。
  - **SKU 映射**：`dim_product_skus_sales`（`channel_sku_code = sku_id` + `channel_code='p009'`）。
  - **过滤**：`WHERE DATE(DATETIME(TIMESTAMP_SECONDS(paid_time), "America/New_York")) IS NOT NULL`（仅已支付订单）。
- 关键规则: **仅统计已支付订单**；`dim_country_code` 固定 'US'；fdate 用美东时区。

#### dwd_trd_toc_walmart_order_item_di
- 目标表: dwd.dwd_trd_toc_walmart_order_item_di
- 上游: `{{ source('ods', 'walmart_orders') }}`
- 清洗逻辑:
  - **双层 JSON 解析**：`SAFE.PARSE_JSON(order_lines)` 安全解析 → `JSON_EXTRACT_ARRAY(..., '$.orderLine')` 展开为行。
  - **SKU 归一**：`item_sku = COALESCE(REGEXP_EXTRACT(item.sku, r'^(?:WM-|W-M)(.+)-AY[A-Z0-9]+$'), item.sku)`（剥离 `WM-`/`W-M` 前缀与 `-AYxxx` 后缀），`dim_hicc_sku_code` 同规则。
  - **费用提取**：`charges.charge[0]`=商品总价/税（PRODUCT 类型）、`charge[1]`=运费（SHIPPING/FEE）；`incentive` 取 Walmart 补贴。
  - **时间字段**：`TIMESTAMP_MILLIS(CAST(order_date AS INT64))`（毫秒 epoch）→ event_time_utc，+8h → cn；`fdate` 按 `America/Los_Angeles`；`fdate_cn` 北京。
  - 状态取 `orderLineStatuses.orderLineStatus[0].status`（Created/Acknowledged/Shipped/Delivered/Cancelled/Refund）。
- 关键规则: **WM- 前缀/-AY 后缀 SKU 归一化**（订单与退货两处同规则）；注释标"补充 hiccsku"但当前 SQL 实际未完成关联。

#### dwd_trd_tob_hktvmall_order_item_di
- 目标表: dwd.dwd_trd_tob_hktvmall_order_item_di
- 上游: `{{ source('ods', 'hktvmall_order_details') }}`、`{{ ref('dim_product_skus_sales') }}`、`{{ ref('dim_exchange_rates') }}`、`{{ source('ods', 'hktvmall_3r_orders') }}`
- 清洗逻辑:
  - **JSON 行项展开**：`LEFT JOIN UNNEST(JSON_QUERY_ARRAY(COLLATE(main.consignmentEntries, '')))`，`JSON_VALUE` 提取 skuId/quantity/totalPrice 等，数量/金额 CAST 类型。
  - **时区修复**：MySQL DATETIME 同步到 BQ 后被误标为 UTC（实际是北京时间），用 `TIMESTAMP(DATETIME(orderDate), 'Asia/Shanghai')` 还原真实 UTC → event_time_utc；+8h → event_time_cn；`fdate = DATE(orderDate)`（北京日期）。
  - **SKU 映射**：`dim_product_skus_sales`（`channel_sku_code = skuId` + `shop_id = storecode`，**限制店铺维度避免跨店铺重复关联**）。
  - **金额折算**：`totalPrice_usd = er.to_usd_rate × totalPrice`（HKD→USD，月度汇率）。
  - **退货关联**：`hktvmall_3r_orders` 以 `orderid = SPLIT(orderId,'-')[0]` 关联（剥离运单后缀），`status LIKE '%ACCEPTED%'` → `is_return=1`、带出 `refund_quantity`。
- 关键规则: **"北京时间→真实 UTC"时区修复**（同步 rank 的 HKTVmall 修复）；订单号 SPLIT 剥离后缀关联退货单；店铺维度限制防跨店重复。

#### dwd_trd_channel_sku_sales_di
- 目标表: dwd.dwd_trd_channel_sku_sales_di
- 上游: 8 源 UNION ALL：`ref('dwd_trd_toc_amazon_order_item_di')`、`ref('dwd_trd_toc_shopify_order_item_di')`、`ref('dwd_trd_toc_shopee_order_item_di')`（WHERE `pay_time IS NOT NULL`）、`ref('dwd_trd_toc_lazada_order_item_di')`、`{{ source('ods', 'import_sales_manual_order') }}`、`ref('dwd_trd_toc_tk_order_item_di')`、`ref('dwd_trd_tob_hktvmall_order_item_di')`、`ref('dwd_trd_toc_walmart_order_item_di')`
- 清洗逻辑:
  - **全渠道 UNION 字段统一**：biz_type（TOC/TOB）、时间四字段、cancel_date/cancel_date_cn、dim_shop_id、dim_channel_code、channel_sku_code、seller_sku_code、quantity_ordered、item_price_amount、currency、country_code、order_id、hicc_sku_code、vine_or_not、data_source_name（记录来源模型名）。
  - **手工单（TOB）**：`import_sales_manual_order`，无精确时间按 `Sale_Date` 日期零点填充 event_time_*，币种固定 SGD、渠道 p012、国家 SG、`hicc_sku_code=NULL`。
  - **渠道名称**：`LEFT JOIN ods.import_dim_channel` 按 channel_code 带出 `dim_channel_name`。
  - **汇率折算**：`JOIN dim_exchange_rates`（`from_currency=currency` + `fdate=DATE_TRUNC(fdate, MONTH)`）→ `item_price_amount_usd = 原币 × to_usd_rate × bmap_percent`。
  - **bundle 套装拆分**：`LEFT JOIN dim_prd_bundle_info`（`bundleinfo_channel_sku_code=channel_sku_code AND bundleinfo_shop_code=dim_shop_id AND bundleinfo_channel_code=dim_channel_code` 三键匹配）：
    - `dim_hicc_sku_code = COALESCE(hicc_sku_code, bundleinfo_bundle_code)`（含 bundle 映射）；
    - `quantity_ordered = 原数量 × COALESCE(bmap_percent, 1)`（一行变 N 行，适合单品分析）；
    - `bundle_quantity = 原始数量`（套餐销量，bundle 会重复 N 行）；
    - `bundleinfo_bundle_code = dim_hicc_sku_code_single = COALESCE(hicc_sku_code, bmap_hicc_sku_code)`（单品口径）。
  - Amazon 源过滤 `itemlist_asin IS NOT NULL`；Shopee 源过滤 `pay_time IS NOT NULL`；Walmart 的 `Cancelled` 仅标记 cancel_date 不剔除。
- 关键规则: **bundle 拆分系数 bmap_percent 分摊**；多源字段口径统一（DWD 已对齐旧代码字段名）；数据血缘标记 `data_source_name`。

#### dws_trd_channel_sku_sales_di
- 目标表: dws.dws_trd_channel_sku_sales_di
- 上游: `ref('dwd_trd_channel_sku_sales_di')`
- 清洗逻辑: **纯透传**无加工，字段选择与注释补齐（biz_type、时间四字段、bundle 双口径数量、item_price_amount_usd 等），供 FineBI 直接出数。
- 关键规则: 无额外规则；口径说明见字段注释（含 bundle 与单品的差异）。

---

## 06_voc 退货域

### 通用清洗规则（该域所有表共用）

- **JSON 行项展开**：退货单主表 JSON 数组列 `CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(o.xxx, '$'))` 展开为"一行一商品退货"；Shopify 是**双层展开**（refunds → refundLineItems）。
- **空数组过滤**：统一 `WHERE 数组列 IS NOT NULL AND 数组列 != '[]'` 防空展开。
- **金额折算 USD**：`{{ ref('dim_exchange_rates') }}` 按月关联（`DATE_TRUNC(退货日期, MONTH)` + `from_currency=退款币种`），`refund_amount_usd = 原币 × to_usd_rate`。
- **SKU 映射**：统一走 `{{ ref('dim_product_skus_sales') }}` 以「渠道 SKU + channel_code（p001/p006/p007/p010）+ 店铺」关联 `dim_hicc_sku_code`；Amazon/Walmart 的 `dim_channel_sku_code` 为 asin / 渠道 SKU 原值。
- **业务时间**：`fdate/fdate_cn` 按"退货事件时间"（售后时间/退货创建时间/退款时间）取北京/本地日期；Walmart 美西、HKTVmall 用 reportDate。
- **状态过滤口径不一**：各渠道只保留"已受理/已退款"状态的退货单（Amazon 无状态过滤但要求 item_list 非空、Lazada `REFUND_SUCCESS`、Shopee `ACCEPTED`、Shopify `restockType='RETURN'`、Walmart `currentRefundStatus NOT IN ('CANCELLED')`）。
- **类型转换**：金额 `SAFE_CAST/CAST AS NUMERIC`、数量 `INT64/FLOAT64`、时间戳 `TIMESTAMP_SECONDS`（秒级）或 `SAFE.PARSE_TIMESTAMP`（ISO 格式）。

### 各表清洗逻辑

#### dwd_voc_amazon_return_di
- 目标表: dwd.dwd_voc_amazon_return_di
- 上游: `{{ source('ods', 'lingxing_amazon_after_sale_list') }}`、`ref('dim_product_skus_sales')`、`{{ source('ods', 'import_dim_shop') }}`、`{{ source('ods', 'import_dim_country') }}`、`ref('dim_exchange_rates')`
- 清洗逻辑:
  - **JSON 行项展开**：`CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(o.item_list, '$')) AS item`，`JSON_EXTRACT_SCALAR` 提取行项。
  - **售后类型三标记**：`after_type`（退货/退款/换货）→ `is_return` / `is_refund` / `is_exchange` 三列（1/0）。
  - **退款金额清洗**：`refund_amount_usd = SAFE_CAST(REGEXP_REPLACE(COLLATE(refund_amount,''), r'[^0-9.\-]', '') AS NUMERIC) × -1 × to_usd_rate`（剥离货币符号，**负号表示退款**）。
  - **汇率链路**：`import_dim_shop`（sid→country）→ `import_dim_country`（country→currency_code）→ `dim_exchange_rates`（按 after_time 月份匹配）。
  - **SKU 映射**：`dim_product_skus_sales`（`shop_id=sid` + `channel_sku_code=asin` + `channel_code='p001'`）。
  - **业务日期**：`fdate = CAST(SUBSTR(after_time,1,10) AS DATE)`（售后日期）。
- 关键规则: 售后类型三标记（退货/退款/换货）；**退款金额负数化**；汇率三级链路（店铺→国家→币种）。

#### dwd_voc_hktvmall_return_di
- 目标表: dwd.dwd_voc_hktvmall_return_di
- 上游: `{{ source('ods', 'hktvmall_3r_orders') }}`
- 清洗逻辑:
  - **直通透传**：ODS 已是行级退货记录，无 JSON 展开；仅做类型转换（`CAST(id AS STRING)`、`CAST(quantity AS INT64)`）。
  - **业务日期**：`fdate = fdate_cn = DATE(reportDate, 'Asia/Shanghai')`（退货报告日期）。
  - 状态过滤被注释（`-- where status like '%ACCEPTED%'`），全量保留。
- 关键规则: 无过滤全量入库；责任方字段（MERCHANT/HKTV）与退货原因代码保留。

#### dwd_voc_lazada_return_di
- 目标表: dwd.dwd_voc_lazada_return_di
- 上游: `{{ source('ods', 'lazada_reverse_orders_list') }}`、`{{ source('ods', 'import_dim_country') }}`、`ref('dim_exchange_rates')`、`ref('dim_product_skus_sales')`
- 清洗逻辑:
  - **JSON 行项展开**：`CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(o.reverse_order_lines, '$')) AS line`。
  - **金额分转元**：`refund_amount = SAFE_CAST(refund_amount AS NUMERIC) × 0.01`（Lazada 接口返回分为单位）；`refund_amount_usd = × 0.01 × to_usd_rate`。
  - **币种从国家映射**：`import_dim_country`（country_code → currency_code）。
  - **时间戳**：`TIMESTAMP_SECONDS(SAFE_CAST(... AS INT64))` 转 UTC（trade_order_gmt_create / return_order_line_gmt_create / modified）。
  - **业务日期**：`fdate` 取 `return_order_line_gmt_create` 转 Asia/Shanghai 日期。
  - **SKU 映射**：`dim_product_skus_sales`（`channel_sku_code = product.product_sku` + `channel_code='p006'`）。
  - **过滤**：`reverse_order_lines IS NOT NULL AND != '[]'`；`reverse_status = 'REFUND_SUCCESS'`（仅退款成功）。
- 关键规则: **金额 ×0.01 分转元**；**仅 REFUND_SUCCESS**；东南亚数据统一中国时区。

#### dwd_voc_shopee_return_di
- 目标表: dwd.dwd_voc_shopee_return_di
- 上游: `{{ source('ods', 'shopee_return_list') }}`、`ref('dim_product_skus_sales')`、`ref('dim_exchange_rates')`、`{{ source('ods', 'import_dim_shop') }}`
- 清洗逻辑:
  - **JSON 行项展开**：`CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(o.item)) AS item_json`。
  - **渠道 SKU**：`dim_channel_sku_code = CAST(model_id AS STRING)`；退款金额 `item_refund_amount_usd = item_refund_amount × to_usd_rate`。
  - **时间戳**：`TIMESTAMP_SECONDS(create_time/update_time/due_date/... )` 转 TIMESTAMP。
  - **业务日期**：`fdate = DATE(TIMESTAMP_SECONDS(create_time), 'Asia/Shanghai')`（退货创建日期）。
  - **SKU 映射**：`dim_product_skus_sales`（`model_id` + `channel_code='p007'`）；国家经 `import_dim_shop`（shop_id → country）。
  - **过滤**：`WHERE o.status = 'ACCEPTED'`（仅已受理退货单）。
- 关键规则: **仅 ACCEPTED 状态**；退货数量口径用 `item_amount`（行项数量）。

#### dwd_voc_shopify_return_di
- 目标表: dwd.dwd_voc_shopify_return_di
- 上游: `{{ source('ods', 'shopify_orders') }}`、`ref('dim_product_skus_sales')`、`ref('dim_exchange_rates')`
- 清洗逻辑:
  - **双层 JSON 展开**：`refunds` 数组（`CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(o.refunds,'$'))`）→ `refundLineItems` 数组（`CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(refund_obj,'$.refundLineItems'))`）。
  - **restock_type 判定实际退货**：`RETURN`=是；`CANCEL`=否（取消退款）；`NO_RESTOCK`=否（不要求寄回）；`is_return_desc` 中文描述。
  - **金额双币种 + USD**：shop（店铺币种）/ presentment（买家币种）两套；USD 折算 `× COALESCE(er.to_usd_rate, 1)`。
  - **SKU 映射**：`variant_id` 提取数字部分（`REGEXP_REPLACE r'.*/(\d+)'`）+ `channel_code='p010'`。
  - **业务日期**：`fdate` 按 `updated_at` + 店铺国家本地时区（US/UK/SG）；`fdate_cn` 经三段时区转换到北京日期。
  - **过滤**：`refunds IS NOT NULL AND != '[]'`；`restockType = 'RETURN'`（**仅实际退货**）。
  - 汇率关联键：`from_currency = currency_code` + `DATE_TRUNC(CAST(cancelled_at AS DATE), MONTH)`。
- 关键规则: **restockType='RETURN' 才计退货**；双币种（shop/presentment）金额体系与销售域一致；双层 JSON 展开。

#### dwd_voc_walmart_return_di
- 目标表: dwd.dwd_voc_walmart_return_di
- 上游: `{{ source('ods', 'walmart_returns') }}` UNION ALL（`{{ source('ods', 'walmart_returns_his') }}` LEFT JOIN `ref('dwd_trd_toc_walmart_order_item_di')`）
- 清洗逻辑:
  - **双源合并**：① 当前源 `walmart_returns`（raw_data 为完整退货 JSON，`LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(raw_data,'$.returnOrderLines'))` 展开）；② 历史源 `walmart_returns_his`（手工导入的历史退款单，补 NULL 字段对齐 UNION 列）。
  - **SKU 归一**：`dim_hicc_sku_code = COALESCE(REGEXP_EXTRACT(item.sku, r'^(?:WM-|W-M)(.+)-AY[A-Z0-9]+$'), item.sku)`（与销售域同规则）；`dim_channel_sku_code` 保留原值。
  - **金额清洗**：当前源 `CAST(totalRefundAmount.currencyAmount AS NUMERIC)`；历史源 `CAST(REPLACE(TOTAL_REFUND_AMOUNT,'$','') AS FLOAT64)`（剥 $ 符号）。
  - **chargeTotals 按索引提取**：固定顺序 `[0]=lineUnitPrice、[1]=lineProductTaxes、[2]=lineSubtotal、[3]=lineTotal、[4]=lineTaxesAndFees、[5]=lineTotalTaxes`。
  - **时间解析**：`SAFE.PARSE_TIMESTAMP('%Y-%m-%dT%H:%M:%E*SZ', ...)` 解析 ISO 时间；`fdate` 美西（America/Los_Angeles）、`fdate_cn` 北京。
  - **过滤**：当前源 `currentRefundStatus NOT IN ('CANCELLED')`；历史源 `CURRENT_STATUS LIKE '%Refunded%'` 且 `refunded_quantity=1`。
- 关键规则: **双源合并**（API 实时 + 手工历史导入）；排除 CANCELLED 状态；SKU 归一与销售域一致（WM- 前缀/-AY 后缀）；历史单按 `PO_NO` 关联销售订单。

#### dws_voc_global_return_di
- 目标表: dws.dws_voc_global_return_di
- 上游: 6 源 UNION ALL：`ref('dwd_voc_walmart_return_di')`、`ref('dwd_voc_amazon_return_di')`、`ref('dwd_voc_lazada_return_di')`、`ref('dwd_voc_shopee_return_di')`、`ref('dwd_trd_tob_hktvmall_order_item_di')`（**复用销售 DWD**，`WHERE is_return = 1`）、`ref('dwd_voc_shopify_return_di')`
- 清洗逻辑:
  - **统一维度**：fdate/fdate_cn/dim_shop_id/dim_channel_code/dim_hicc_sku_code/dim_country_code/dim_channel_sku_code 7 维 GROUP BY，`SUM(return_amount)` + `SUM(return_quantity)`。
  - **各渠道金额/数量口径**：
    - Walmart：`SUM(total_refund_amount)`（USD）+ `SUM(refunded_quantity)`，渠道 p002、国家固定 US；
    - Amazon：`SUM(CASE WHEN is_refund=1 THEN refund_amount_usd ELSE 0 END)` + `SUM(CASE WHEN is_return=1 THEN after_quantity ELSE 0 END)`（仅退款记金额、仅退货记数量），渠道 p001；
    - Lazada：`SUM(refund_amount_usd)` + `SUM(1)`（**每行计 1 件**），渠道 p006；
    - Shopee：`SUM(item_refund_amount_usd)` + `SUM(item_amount)`，渠道 p007；
    - HKTVmall：`SUM(totalPrice_usd)` + `SUM(refund_quantity)`，国家固定 HK、渠道 p008；
    - Shopify：`SUM(line_subtotal_shop_amount_usd)` + `SUM(refund_quantity)`，渠道 p010。
- 关键规则: 全渠道退货汇总统一 USD 口径；**退货数量口径各渠道不一致**（after_quantity / 固定1 / item_amount / refund_quantity）；HKTVmall 复用销售域 DWD 的 is_return 标记。

---

## 03_prd 商品域

### 通用清洗规则（该域所有表共用）

- **JSON 多层嵌套展开**：商品主表 JSON 列逐层 UNNEST 到目标粒度——Lazada 双层（products→skus）到 SKU、Shopee 单层（model）、Shopify 双层（variants.edges→node）、TK 单层（skus）；嵌套数组用 `JSON_QUERY_ARRAY`，嵌套对象用 `UNNEST([JSON_QUERY(...)])` 提取。
- **字段提取**：`JSON_VALUE/JSON_EXTRACT_SCALAR` 提取标量字段；金额 `SAFE_CAST/CAST` 转 NUMERIC/FLOAT64、数量转 INT64；**ID 类字段普遍 CAST 成 STRING**（防科学计数法/精度丢失、跨系统类型统一）。
- **gid 提取数字 ID**：Shopify 系列 `variant_id`/`product_id` 用 `REGEXP_REPLACE(..., r'.*/(\d+)', r'\1')` 从 `gid://shopify/xxx/123` 提取纯数字。
- **时间戳转换**：毫秒级用 `TIMESTAMP_MILLIS`、秒级 `TIMESTAMP_SECONDS`、ISO 字符串 `TIMESTAMP()`/`PARSE_TIMESTAMP`；etl_time 北京。
- **SKU 前缀解析**（dim_prd_lingxing_amazon_product）：按 SKU 前缀推导 HICC SKU、渠道、国家、地区。
- **归一关联主数据**：经 `dim_product_skus_warehouse`（warehouse_sku_id）或 `dim_product_skus`（sku_code）回链 HICC 主数据，产出 `dim_hicc_sku_code` 与采购成本。
- **配置/增量**：`dwd_prd_amazon_seller_sku_snap` 使用 `incremental + insert_overwrite` 按 `fdate_p` 分区。

### 各表清洗逻辑

#### dim_prd_lazada_products
- 目标表: dim.dim_prd_lazada_products
- 上游: `{{ source('ods', 'lazada_products_list') }}`
- 清洗逻辑:
  - **双层嵌套展开**：`UNNEST(JSON_QUERY_ARRAY(SAFE.PARSE_JSON(p.products),'$'))` 商品级 → `UNNEST(JSON_QUERY_ARRAY(product_json,'$.skus'))` SKU 级（最终 SKU 粒度宽表）。
  - **属性提取**：`JSON_VALUE` 提取商品属性（品牌/中英文名/动物类型/形态/成分等）与 SKU 规格（SkuId/SellerSku/ShopSku/model/Status）。
  - **价格库存**：`CAST AS FLOAT64/INT64`（吊牌价/折后价/总库存/可售库存/包裹尺寸）。
  - **时间**：13 位毫秒时间戳 `TIMESTAMP_MILLIS` 转标准 TIMESTAMP。
  - **过滤**：`products IS NOT NULL AND SAFE.PARSE_JSON(products) IS NOT NULL`（防解析失败）。
- 关键规则: 双层展开到 SKU 粒度；SellerSku 是内部 ERP 对接关键键。

#### dim_prd_lingxing_amazon_product
- 目标表: dim.dim_prd_lingxing_amazon_product
- 上游: `{{ source('ods', 'lingxing_amazon_product_info') }}`
- 清洗逻辑:
  - **SKU 前缀规则解析**（三套 CASE WHEN）：
    - `hicc_sku`：剥离前缀（AZ-→去4位、CAL-/UAE-→去5位、US-/CA-/SA-/JP-/SG-/W-M/T-K→去4位、DE/UK→去3位、E/D/F→去2位、KMY-→去5位等）；
    - `to_channel`：AZ-/CAL-/UAE-/DE/UK/SA-/JP-/E/D/F/CA→p001、W-M→p002、T-K→p009、SG-/KMY-→p015、US-→p017、CA-→p018；
    - `to_country`：AZ-/US-/W-M/T-K→US、CAL-/CA-/CA→CA、UAE-→AE、UK→UK、DE→/、SA-→SA、JP→JP、SG-/KMY-→SG、D→DE、F→FR；
    - `to_region`：DE→欧洲大陆、E→欧洲。
- 关键规则: **SKU 前缀→渠道/国家/地区映射规则**（渠道编码 p001/p002/p009/p015/p017/p018）。

#### dim_prd_shipout_product
- 目标表: dim.dim_prd_shipout_product
- 上游: `{{ source('ods', 'shipout_product') }}`、`ref('dim_product_skus_warehouse')`、`ref('dim_product_skus')`
- 清洗逻辑:
  - **主数据映射**：`dim_product_skus_warehouse`（`warehouse_sku_id=sku_id`）带出 `dim_hicc_sku_code` 与采购成本；再经 `dim_product_skus`（`sku_code=hicc_sku_code`）带出换算系数。
  - **换算系数 convert_rate 规则**：SKU 名含 'Inner box'→`unit_inner_box`；含 'PCS'→1；`org_id='52037'`（Meta 海外仓）→1（2026-08-20 修复补全分支）；否则 `unit_carton_box`。
  - **unit_type 判定**：PCS→'Single item'、org_id=52037→'Single item'、Inner box→'Inner Case'、否则 'Master Case'。
  - **仓库/渠道映射**：`org_id=55752→w003`、`52037→w002`；`belong_to_channel_code`：org_id=52037 时按 SKU 名含 '-UPC'/'Place'→p017 否则 p010，其他统一 p017。
- 关键规则: **换算系数分支规则**（Inner box/PCS/Meta 海外仓）；Meta 海外仓（52037）特殊渠道映射（LOGAN-HICCPET 提交）。

#### dim_prd_shopee_model
- 目标表: dim.dim_prd_shopee_model
- 上游: `{{ source('ods', 'shopee_model_list') }}`
- 清洗逻辑:
  - **JSON 数组展开**：`LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(model)) AS m`（变体模型一行一个）。
  - **类型统一**：ID/变体字段全部 `CAST AS STRING`（防科学计数法/精度丢失）。
  - **model_id 兜底**：`model_ext_model_id = COALESCE(model_id, item_id)`。
  - 保留 tier_variation / standardise_tier_variation 原始变体配置。
- 关键规则: 类型统一字符串化；model_id 空值回退 item_id。

#### dim_prd_shopify_variants
- 目标表: dim.dim_prd_shopify_variants
- 上游: `{{ source('ods', 'shopify_products') }}`
- 清洗逻辑:
  - **双层展开**：`UNNEST(JSON_QUERY_ARRAY(p.variants,'$.edges'))` → `UNNEST([JSON_QUERY(edge,'$.node')])`（对象解包简化后续 JSON_VALUE）。
  - **variant_id**：`REGEXP_REPLACE(node.id, r'.*/(\d+)', r'\1')`（gid 提取数字）。
  - **类型转换**：`variant_price SAFE_CAST NUMERIC`、`inventory_quantity SAFE_CAST INT64`、时间 `TIMESTAMP()`。
- 关键规则: gid 提取数字 ID；两层展开（edges→node）。

#### dim_prd_tk_products
- 目标表: dim.dim_prd_tk_products
- 上游: `{{ source('ods', 'tk_products') }}`
- 清洗逻辑:
  - **JSON 数组展开**：`UNNEST(JSON_QUERY_ARRAY(skus))`。
  - **行项提取**：`skus_ext_id`（sku.id）、`skus_ext_seller_sku`（seller_sku）CAST 成 STRING；`is_not_for_sale` CAST STRING。
  - `sales_regions` 取数组第 0 个元素 `JSON_EXTRACT_SCALAR(sales_regions,'$[0]')`。
- 关键规则: 简单 SKU 展开；销售区域取首个。

#### dwd_prd_amazon_product_perf_di
- 目标表: dwd.dwd_prd_amazon_product_perf_di
- 上游: `{{ source('ods', 'lingxing_amazon_product_performance') }}`（WHERE `start_date < '2026-07-01'`）UNION ALL `{{ source('ods', 'lingxing_amazon_product_performance_v') }}`
- 清洗逻辑: **双源合并**（静态历史 + 实时视图），字段透传 `SELECT *`。
- 关键规则: 双源合并，以 2026-07-01 为时间分界。

#### dwd_prd_amazon_seller_sku_snap
- 目标表: dwd.dwd_prd_amazon_seller_sku_snap
- 上游: `{{ source('ods', 'lingxing_amazon_seller_sku_list') }}`
- 清洗逻辑:
  - **增量物化**：`incremental + insert_overwrite`，分区字段 `fdate_p`（DATE，取 `current_date()`），`business_time = CURRENT_TIMESTAMP()`。
  - **small_rank 解析**：CTE `ranked_data` 将 `small_rank` JSON 数组按 `SAFE_CAST(rank AS INT64)` 升序取 **Top2**，生成 `rank_link_1/rank_value_1/rank_category_1/rank_link_2/rank_value_2/rank_category_2` 六个派生字段（`r.top_ranks[SAFE_OFFSET(0/1)]`）。
  - `main.* EXCEPT(synctime)` 透传原表字段。
- 关键规则: **BSR 排名 Top2 提取**（rank 升序 LIMIT 2）；增量按 synctime 分区；迁移自 ODS 分区表。

#### dwd_prd_amazon_seller_sku_di
- 目标表: dwd.dwd_prd_amazon_seller_sku_di
- 上游: `ref('dwd_prd_amazon_seller_sku_snap')`、`ref('dim_product_skus_sales')`
- 清洗逻辑:
  - **CTE 过滤**：`marketplace='美国' AND thirty_volume > 0`（仅美国站、30 日有销量）。
  - **LAG 窗口**：`daily_sales_chain_ratio = ROUND((yesterday_volume − COALESCE(prev,0)) / NULLIF(COALESCE(prev,0),0), 2)`（日销环比，`LAG(yesterday_volume,1) OVER(PARTITION BY listing_id ORDER BY fdate_p)`）。
  - **Pet Supplies BSR**：`CASE WHEN seller_category_new LIKE '%Pet Supplies%' THEN seller_rank`；`bsr_7day_avg` 用 `AVG(...) OVER(PARTITION BY listing_id ORDER BY fdate_p ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)`；`bsr_change_vs_yesterday` 用 LAG 差值。
  - **双类目排名**：`rank_change_1/2 = rank_value − COALESCE(prev_rank_value, rank_value)`（LAG 按 `listing_id, rank_category` 分区）；`rank_7day_avg_1/2` 7 日滚动均值。
  - **SKU 映射**：`dim_product_skus_sales`（`channel_sku_code=asin` + `channel_code='p001'` + `shop_id=CAST(sid AS STRING)`），带出 `sku_code/vine_or_not`。
- 关键规则: 窗口函数（LAG/AVG OVER）计算环比与 7 日滚动均值；仅美国站 & 30 日销量>0；Pet Supplies 类目专属 BSR。

---

## 附：域间共性模式小结

| 模式 | 销售域 01_trd | 退货域 06_voc | 商品域 03_prd |
|------|--------------|--------------|--------------|
| JSON 行项展开 | LEFT JOIN UNNEST | CROSS JOIN UNNEST（Shopify 双层） | 多层 UNNEST 到 SKU 粒度 |
| 时间四字段 | 全部模型统一 | fdate/fdate_cn 为主 | 仅 created/updated 时间 |
| 金额折算 USD | dim_exchange_rates 月汇率 | dim_exchange_rates 月汇率 | 采购成本直接带出 |
| SKU 映射 | dim_product_skus_sales | dim_product_skus_sales | dim_product_skus_warehouse / dim_product_skus |
| 双源合并 | Amazon（视图+静态）、全渠道 union | Walmart（API+历史导入） | Amazon product_perf（历史+视图） |
| 特殊清洗 | bundle 拆分系数、Vine 标记 | 金额分转元、退款负数化、restockType | SKU 前缀解析、gid 提取、BSR Top2 |
