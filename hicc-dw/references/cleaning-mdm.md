# 主数据维表 清洗逻辑与规则（09_mdm）

> 分析范围：`hicc_data_platform/models/09_mdm/dim/` 下全部 21 个 .sql 模型 + schema.yml
> 分层定位：09_mdm（主数据/维度层），供 DWD/DWS 各域关联使用；多数表为全量快照，每日 T+1（morning_full DAG）重建。

### 通用清洗规则

- **直通引用模式（static_dim 复用）**：`dim_date`、`dim_mkt_petco_creative_mapping`、`dim_prd_sps_vendor_style`、`dim_scm_shipping_time` 直接 `SELECT * FROM {{ source('static_dim', 'xxx') }}`，不加工，仅做模型化收编。
- **源主数据直通 + 派生列（ods 清洗源）**：`dim_business_channel_v2`、`dim_country_v2`、`dim_shop_v2` 等「_v2」系列直接读取 ods 主数据源表，在数仓侧只做**受治理的派生口径**（时区映射、TRIM 清洗），治理逻辑落维表、禁止散落到事实表。
- **多源 UNION ALL 合并 + 排他去重（NOT EXISTS）**：`dim_product_skus`（main 主数据 → manual 手工表 → bundle 组合品，逐级 NOT EXISTS 排他）、`dim_import_sku_mapping`（import_sku_mapping + import_amazon_sku_info）。
- **ROW_NUMBER 确定性去重**：以「数据源优先级/在售/键长度」等 ORDER BY 键分组取 rn=1：
  - `dim_product_skus_warehouse`：按 `data_source` 优先级（**手动录入 > 系统自动**）；
  - `dim_hicc_sku_mapping_v2`：已归一 > 官方映射 > 非 vine > 在售 > 短基础 SKU > seller_sku 字典序；
  - `dim_sku_mapping` / `dim_warehouse_sku_mapping`（amazon 分支）：按 `is_delete` 升序（在售优先）。
- **渠道 SKU → HICC SKU 归一体系（两代并存）**：
  - **旧体系** `dim_sku_mapping` / `dim_warehouse_sku_mapping`：以「正则规则链 + LEFT JOIN dim_product_skus 值域」逐条匹配，COALESCE 取第一个命中；Amazon 规则链 R1-R7（三字母前缀/AZ 中段/两字母前缀/W-M/EDF 原值/EDF 去首字母/去前两字符/原值）。
  - **新体系** `dim_hicc_sku_mapping_v2`：L1 官方映射 → L2 regex 兜底 → L3 待治理（禁止静默 NULL，含 governance_reason 归因），grain_key 唯一粒度。
- **vine 标记**：Amazon 渠道按 `LOWER(seller_sku) LIKE '%vine%' OR LIKE '%-v%'` 判定（`dim_product_skus_sales`/`dim_product_skus_warehouse`）；新体系 `dim_hicc_sku_mapping_v2` 修正为 `%vine%`（避免 `%-v%` 误伤 `-V3` 版本号后缀）。
- **JSON 展开（BigQuery UNNEST）**：账号（lingxing_account_list）、订单行（walmart/hktvmall）、商品列表（shopee/lazada/tiktok/shopify）均通过 `JSON_EXTRACT_ARRAY`/`json_query_array`/`json_value` 展平为行级。
- **regex 键规整**：W-M/WM 前缀剥离、`-`/`_` 尾段裁剪（`REGEXP_REPLACE(x, r'-[^-]*$', '')`）、T-K 前缀剥离、shopify variant id 取末段数字、hktvmall skuId 取下划线第 3 段。
- **月份级汇率**：真实工作日汇率 + 「本月无数据时」用最近工作日模拟，统一折算为 `to_usd_rate`（1 单位外币 = ? 美元），月粒度 `fdate = date_trunc(rate_date, month)`。
- **业务日历周**：`dim_calendar_cn`/`dim_calendar_local` 以 `DATE_ADD(fdate, 3 DAY)` 将「上周五~本周四」平移对齐到自然周，产出业务周区间字符串。

---

### 各表清洗逻辑

#### dim_business_channel_v2
- 目标表: dim_business_channel_v2（业务渠道维度表，ToB/ToC 全域统一，01_trd 战役新建）
- 上游: `{{ source('ods', 'import_dim_channel') }}`
- 清洗逻辑: 只读清洗源表全量值域，无变换；channel_type（ToC/ToB）为源系统维护的逻辑切分字段。
- 关键规则:
  - 值域含暂未启用渠道（Petco/Chewy/Temu/ShowRoom/GTM），事实表按需关联。
  - 渠道代码硬编码收敛：p001=Amazon / p002=Walmart / p006=Lazada / p007=Shopee / p008=HKTV Mall / p009=TikTok / p010=Shopify / p015-p018=ToB。
  - schema 测试：channel_code unique+not_null；channel_type accepted_values ['ToC','ToB']。

#### dim_calendar_cn
- 目标表: dim_calendar_cn（中国日期维度表，自然日粒度）
- 上游: `{{ ref('dim_date') }}`
- 清洗逻辑: 派生 `biz_offset3date = DATE_ADD(fdate, INTERVAL 3 DAY)`（把上周五~本周四平移成新的一周）；`week_date_range` 用 WEEK(MONDAY) 截断后回推 3 天得到「周五~下周四」区间字符串（`~` 连接）。
- 关键规则: 业务周口径 = 周五~下周四（区别于 ISO 周一~周日）；以 fdate 所在自然周对齐业务周。

#### dim_calendar_local
- 目标表: dim_calendar_local（本地业务日历维度表）
- 上游: `{{ ref('dim_date') }}`
- 清洗逻辑: 与 dim_calendar_cn 同构，仅输出 `biz_week_date_range`（fdate 所在周五~下周四区间，`~` 连接）。
- 关键规则: 业务周区间口径与 dim_calendar_cn 的 week_date_range 一致，为下游本地业务周聚合提供日历键。

#### dim_channel_lingxing_account
- 目标表: dim_channel_lingxing_account（Lingxing 亚马逊账号维度表）
- 上游: `{{ source('ods', 'lingxing_account_list') }}`
- 清洗逻辑: `CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(o.data, '$'))` 将 JSON 数组展开为行；逐字段 `JSON_EXTRACT_SCALAR` 提取 profile_id/sid/name/status/country_code/currency_code/email/vendor_code；status 转 INT64；过滤 `data IS NOT NULL AND data != '[]'`。
- 关键规则:
  - 主键 profile_id（Amazon Profile ID，唯一标识一个账号）；account_type 区分 seller/dsp。
  - etl_time 用 `CURRENT_TIMESTAMP() + INTERVAL 8 HOUR` 转北京时间格式化。

#### dim_country_v2
- 目标表: dim_country_v2（国家维度表，01_trd 战役新建）
- 上游: `{{ source('ods', 'import_dim_country') }}`
- 清洗逻辑: 直通源字段 + CASE 生成国家级 IANA 时区兜底（23 国硬编码映射）。
- 关键规则:
  - 国家代码沿业务惯例 `'UK'`（非 ISO 'GB'），Amazon 欧洲站映射需与 `.co.uk` 对齐。
  - 多时区大国（US/CA/AU）兜底取东部时区（US→America/New_York 等）；精确时区以 dim_shop_v2.iana_timezone 为准。
  - currency_code 为事实表币种兜底口径（事实表逐行携带币种，此处仅兜底）。
  - schema 测试：country_code unique+not_null；iana_timezone not_null。

#### dim_date
- 目标表: dim_date（日期维度表）
- 上游: `{{ source('static_dim', 'dim_date') }}`
- 清洗逻辑: 无，直接 `SELECT *` 直通 static 层日历表。
- 关键规则: 作为 dim_calendar_cn/dim_calendar_local 的基表。

#### dim_exchange_rates
- 目标表: dim_exchange_rates（汇率维度表，月粒度）
- 上游: `{{ source('ods', 'exchange_rates') }}`
- 清洗逻辑:
  1. real_rates：过滤 `is_first_work_date = 1`（仅真实工作日汇率）；
  2. usd_rate：取每个工作日 USD 汇率，同日 INNER JOIN 到各币种行；
  3. 折算：主流 10 币种（USD/EUR/JPY/HKD/GBP/AUD/NZD/SGD/CHF/CAD）`to_usd_rate = ROUND(rate / usd_rate_value, 10)`，其余小币种 `ROUND(10000.0 / (rate * usd_rate_value), 10)`（源表小币种为 1 外币=?10000 本币口径）；
  4. 模拟：`current_month_has_data` 判本月是否已有工作日数据；无则取 `rate_date < CURRENT_DATE()` 的最近工作日（latest_workday），将该日全币种复制为 `rate_date = CURRENT_DATE()`、`is_first_work_date = 0`、精度 6 位、data_source='上周期外汇官方数据'，仅当本月无数据且存在最近工作日时生成；
  5. 合并后统一 `date_trunc(rate_date, month)` 转月级，输出 fdate / currency_cn / from_currency / to_usd_rate / data_source。
- 关键规则:
  - 精度：真实汇率 10 位小数、模拟汇率 6 位小数；data_source 区分「外汇官方数据」/「上周期外汇官方数据」。
  - 模拟行 id=NULL、is_first_work_date=0，作为本月汇率兜底（防止月初无汇率导致折算丢失）。

#### dim_hicc_sku_mapping_v2
- 目标表: dim_hicc_sku_mapping_v2（HICC 统一 SKU 映射维度表，01_trd 战役新建）
- 粒度: platform_code × shop_id × channel_sku_code（grain_key = `platform_code|shop_id|channel_sku_code`）
- 上游: `pdt_ods.product_skus_sales`、`ods.import_product_skus_sales`（L1 官方映射）；`ods.lingxing_amazon_seller_sku_list`（Amazon）；`ods.walmart_orders`（Walmart）；`ods.shopee_model_list`（Shopee）；`ods.lazada_products_list`（Lazada）；`ods.tk_products`（TikTok）；`ods.shopify_products`（Shopify）；`ods.hktvmall_order_details`（HKTVMall）；`ods.bundle_info`（L5 bundle）；`ref('dim_product_skus')`（L2 值域门禁）；`ref('dim_shop_v2')`（国家关联）
- 清洗逻辑（三层归一架构 + 两遍清偿 + 确定性去重）:
  1. **L1 官方映射**：`pdt_ods.product_skus_sales` ∪ `ods.import_product_skus_sales`（过滤 deleted_at 非空、空 sku_code）以 (channel_code, shop_id, channel_sku_code)→sku_code；Amazon 键=ASIN，Walmart 键=剥 W-M/WM- 前缀后的干净 SKU，其余平台键=渠道技术键；
  2. **L1b 跨店铺 ASIN（Amazon）**：ASIN 全局唯一，同 ASIN 跨店铺=同商品（自家矩阵跟卖）；要求该 ASIN 全局 sku_code 唯一（HAVING count(*)=1）防歧义，MIN(sku_code) 取值；
  3. **L2 regex 兜底**：按平台规则链将 raw_sku_code 归一到 dim_product_skus 值域（457 个：main 264 + manual 140 + bundle 53），每步 `in (select sku_code from master)` 值域门禁；Amazon R1-R7 链（R1 三字母前缀 / R2 AZ 中段 / R3 两字母前缀 / R4 W-M 前缀 / R5a·R5b EDF 开头 / R7 vine 后缀剥离 / R6 去前两字符 / raw 原值）；Walmart=W-M|WM- 剥离后段或原值；Shopee/Lazada/TikTok/Shopify/HKTVMall=原值或 `^([^-]+)` 首段；
  4. **P3 combo 主成分**：raw 含 `+` 的组合 SKU 取主成分（Amazon `^AZ-([^+]+)`，其余 `+` 前段），受值域门禁；
  5. **P4 Amazon parent 继承**：同 (shop_id, parent_asin) 下已归一行的唯一 HICC SKU 继承（HAVING count(distinct)=1），vine 定案路径（vine 映射同款基础 SKU）；
  6. **L5 bundle 身份注册**：ods.bundle_info 中注册的平台销售端套装渠道键（Shopee KIT 系列/TK 套装）→ bundle_code，只做身份识别不做拆解，is_bundle=true；
  7. **确定性去重**：`ROW_NUMBER() PARTITION BY platform_code, shop_id, channel_sku_code`，ORDER BY 已归一 > l1_official > 非 vine > 在售(is_delete=0) > 短基础 SKU > seller_sku 字典序；
  8. **match_rule 归因**：l1_official / l1b_asin_cross_shop / R1-R7 / l2_regex / combo_primary_component / l4_parent_inherit / l5_bundle / unmatched。
- 关键规则:
  - 完整性硬门禁：`dim_hicc_sku_code NOT NULL`（100% 渠道键必须有 HICC SKU，禁止静默 NULL），未归一行 `is_governance_pending=true` + `governance_reason` 分类（unvariant_item_fallback / null_or_empty_sku / vine_program_sku / combo_sku / digit_placeholder / nonmaster_other），清偿归 09_mdm 主数据治理。
  - vine 判定 `%vine%`（%-v% 会误伤 -V3 版本号后缀）；Amazon 键唯一性实测 100%；L1+L2 覆盖 amazon 77.9% / walmart 100% / shopee 87.9% / lazada 89.9% / tiktok 85.6% / shopify 86.3% / hktvmall 99.0%。
  - Walmart ODS 无商品主数据表，映射源=订单行 sku（E26 实测唯一来源）；Shopee 无变体商品经 `COALESCE(model_id, item_id)` 产出 item_id 回退键。
  - schema 测试：grain_key unique+not_null；platform_code/dim_channel_code accepted_values；dim_hicc_sku_code not_null。

#### dim_import_sku_mapping
- 目标表: dim_import_sku_mapping（SKU 映射维度表，渠道 SKU→HICC SKU）
- 上游: `ods.import_sku_mapping`、`ods.import_amazon_sku_info`、`ods.import_dim_shop`
- 清洗逻辑: 两段 UNION ALL——非 p001 渠道直通 import_sku_mapping；p001（Amazon）用 import_amazon_sku_info 的 (sid, seller_sku)→hicc_sku，LEFT JOIN import_dim_shop 取 country/shop_name，`source_table` 字段标记来源（'import_sku_mapping'/'import_amazon_sku_info'）。
- 关键规则: p001 渠道仅取手工维护表（amazon 映射以手动录入优先）；channel != 'p001' 与 p001 两分支按渠道互斥。

#### dim_mkt_petco_creative_mapping
- 目标表: dim_mkt_petco_creative_mapping（Petco 广告创意映射表）
- 上游: `{{ source('static_dim', 'dim_mkt_petco_creative_mapping') }}`
- 清洗逻辑: 无，直通 static 层。
- 关键规则: 静态治理映射由 static_dim 层维护。

#### dim_prd_bundle_info
- 目标表: dim_prd_bundle_info（套餐 Bundle 主数据与拆分明细维度表）
- 粒度: 1 行 = 套餐 × 套餐内单品（无拆分则 bmap_* 为空）
- 上游: `ods.bundle_info`、`ods.bundle_item_mapping`
- 清洗逻辑: bundle_info 别名前缀 `bundleinfo_*`；LEFT JOIN bundle_item_mapping 别名前缀 `bmap_*`，关联键 `bmap_bundle_id = bundleinfo_id`（bundle_item_mapping.bundle_id 经 `REGEXP_REPLACE(r'\.0$','')` 去掉小数尾缀对齐字符串 ID）。
- 关键规则: bmap_percent 为金额/数量分摊系数；销售/广告 DWD/DWS 识别 bundle 后按 percent 分摊金额与数量（拆解发散在 DWD 层执行）。

#### dim_prd_sps_vendor_style
- 目标表: dim_prd_sps_vendor_style（SPS 供应商款式维度表）
- 上游: `{{ source('static_dim', 'dim_prd_sps_vendor_style') }}`
- 清洗逻辑: 无，直通 static 层。
- 关键规则: 静态供应商款式映射。

#### dim_product_categories
- 目标表: dim_product_categories（商品分类维度表，多级分类）
- 上游: `pdt_ods.product_categories`
- 清洗逻辑: 按 level=1/2/3 各取一次（id/name/parent_id 别名区分），三级逐级 LEFT JOIN 自关联（category1.id = category2.parent → category2.id = category3.parent），输出大类→子类→最小分类六级字段；`category_id_min = COALESCE(category_id3, category_id2, category_id1)`。
- 关键规则: 最小分类键 category_id_min 作为 dim_product_skus 关联分类的键；level 缺失/断链时 COALESCE 向上一级回退。

#### dim_product_skus
- 目标表: dim_product_skus（商品主数据维表，唯一商品维表）
- 上游: `pdt_ods.product_skus`、`pdt_ods.product_spus`、`pdt_ods.product_brands`、`ref('dim_product_categories')`、`ods.import_sku_info`、`ods.bundle_info`
- 清洗逻辑（三源合并，排他 NOT EXISTS）:
  1. **main 主数据**：product_skus LEFT JOIN product_spus（SPU 属性，sput_* 前缀）、LEFT JOIN product_brands（品牌）、LEFT JOIN dim_product_categories（按 `spu.backend_category_id = category_id_min` 关联三级分类）；extension_data JSON 展开 is_new / old_upc / inner_box_qty / gtin_inner_box / unit_inner_box / gtin_carton_box / unit_carton_box / purchased_cost_price；`sku_source='main'`、is_bundle=0；
  2. **manual 手工表**：ods.import_sku_info，仅主数据中不存在的 SKU（`NOT EXISTS`），字段空位 CAST(NULL)；sku_source='manual'；
  3. **bundle 组合品**：ods.bundle_info（bundle_code 作 sku_code），仅主数据/手工表均不存在，分类三级占位 'bundle'，brand_name='HICC PET'，is_bundle=1；sku_source='bundle'。
- 关键规则:
  - 标识列 sku_source（main/manual/bundle）+ is_bundle（1=组合品）标识行来源与组合属性。
  - is_new 从 extension_data JSON 提取（新品标签）；`is_delisting = product_labels LIKE '%"delisting"%'`（退市标记）。
  - 本表即 L2 归一的值域（HICC SKU 主数据），下游映射表以其为合法值域门禁。

#### dim_product_skus_purchase
- 目标表: dim_product_skus_purchase（采购 SKU 主数据维度表）
- 上游: `pdt_ods.product_skus_purchase`
- 清洗逻辑: 基本直通（采购视角字段：purchase_sku_code/cg_price/cg_box_pcs/装箱尺寸等），仅补充 `is_inner_box` 空串占位列。
- 关键规则: 采购价格 cg_price 供 dim_product_skus_warehouse 等下游取采购成本（MAX 聚合按 sku_code）；is_combo 标记组合商品。

#### dim_product_skus_sales
- 目标表: dim_product_skus_sales（销售 SKU 维度表，渠道 SKU→HICC SKU）
- 上游: `pdt_ods.product_skus_sales`、`ods.import_product_skus_sales`
- 清洗逻辑: 两段 UNION ALL（官方主数据 + 手工补充表），字段直通，id 转 STRING；派生 `vine_or_not`：仅 p001（Amazon）且 seller_sku_code LOWER LIKE '%vine%' OR '%-v%' → 'vine'，否则 NULL（手工表恒 NULL）。
- 关键规则: 该表的 (channel_code, shop_id, channel_sku_code)→sku_code 是 dim_hicc_sku_mapping_v2 的 L1 官方映射源；vine 标记供销售端识别 Vine 计划流量。

#### dim_product_skus_warehouse
- 目标表: dim_product_skus_warehouse（仓库 SKU 维度表，仓库 SKU→HICC SKU）
- 上游: `pdt_ods.product_skus_warehouse`、`pdt_ods.product_skus_purchase`（取采购成本 MAX(cg_price)）、`ods.import_dim_warehouse`（仓库国家/渠道）
- 清洗逻辑:
  1. **去重**：`ROW_NUMBER() PARTITION BY warehouse_code, warehouse_sku_code, warehouse_sku_id`，`ORDER BY CASE WHEN data_source='手动录入' THEN 1 ELSE 2 END`（手动录入优先），取 rn=1；
  2. LEFT JOIN product_skus_purchase 按 sku_code 取 `MAX(cg_price)`，`COALESCE(purchased_cost_price, 0)` 兜底；
  3. LEFT JOIN import_dim_warehouse 取 country_code/channel_code；
  4. **w002（Meta 海外仓）渠道特殊处理**：warehouse_sku_code LIKE '%-UPC%' 或 '%Place%' → p017（ToB_US），否则 p010（Shopify）；其余仓库直接取仓库表 channel_code；
  5. vine 标记：warehouse_name LIKE '%Amazon%' 且 sku LIKE '%vine%' OR '%-v%' → 'vine'。
- 关键规则: belong_to_channel_code 用于下游按仓库归属渠道归集；采购成本聚合取 MAX（同 sku 多采购价行取最大）；手动录入数据源优先级最高。

#### dim_scm_shipping_time
- 目标表: dim_scm_shipping_time（物流交期维度表）
- 上游: `{{ source('static_dim', 'dim_scm_shipping_time') }}`
- 清洗逻辑: 无，直通 static 层。
- 关键规则: 静态物流交期治理数据。

#### dim_shop_v2
- 目标表: dim_shop_v2（店铺维度表，01_trd 战役新建）
- 上游: `ods.import_dim_shop`、`ref('dim_country_v2')`
- 清洗逻辑:
  1. `TRIM(shop_id)` 归一（源侧实测回车污染 'B0975002\r'）；
  2. 派生 iana_timezone：**Amazon 站点实测覆盖优先**——channel_code='p001' 且 country IN ('US','CA') → America/Los_Angeles（实测 local=UTC-7/-8，DST 精确切换）；p001 且 BR → America/Manaus（实测 UTC-4）；其余取 dim_country_v2.iana_timezone 国家级默认。
- 关键规则:
  - 店铺级时区为 DWS event_date_local 派生依赖；Amazon US/CA 实测覆盖优先于国家级默认。
  - Known issues 保留原值不篡改：chewy1 挂 p019（import_dim_channel 无此渠道，孤儿外键）、petco1 挂 p017（ToB_US）——源数据治理问题。
  - schema 测试：shop_id unique+not_null；country_code relationships→dim_country_v2；iana_timezone not_null（不设 channel_code 硬关系测试因孤儿值）。

#### dim_sku_mapping
- 目标表: dim_sku_mapping（旧体系 SKU 映射维度表，供商品主数据使用）
- 上游: `ref('dim_prd_shopify_variants')`、`ref('dim_prd_tk_products')`、`ref('dim_prd_lazada_products')`、`ref('dim_prd_shopee_model')`、`ods.hktvmall_order_details`、`ods.walmart_orders`、`ods.lingxing_amazon_seller_sku_list`、`ods.import_dim_channel`、`ods.import_dim_shop`、`ref('dim_product_skus')`
- 清洗逻辑: 7 平台 UNION ALL：
  - Shopify（p010）：variant_id 作 channel_sku_code、variant_sku 作 seller/hicc；
  - TikTok（p009）：skus_ext_id → channel_sku，seller_sku 原值作 hicc；
  - Lazada（p006）：sku_id → channel_sku，`COLLATE(seller_sku,'')` 且 `REGEXP_EXTRACT(r'^([^-]+)')` 取首段作 hicc；country UPPER；
  - Shopee（p007）：model_ext_model_id → channel_sku，model_sku 首段作 hicc；
  - HKTVMall（p008）：consignmentEntries 展开，skuId 下划线第 3 段作 seller/hicc；
  - Walmart（p002）：`COALESCE(REGEXP_EXTRACT(r'^W-M(.*?)-'), 原值)` 剥离 W-M 前缀；order_lines JSON 安全解析展开；
  - Amazon（p001）：领星 listing，**regex 规则链匹配 dim_product_skus**（R1 三字母前缀 / R2 AZ 中段 / R3 两字母前缀 / R4 W-M / R5a EDF 原值 / R5b EDF 去首字母 / 去前两字符 / 原值），`ROW_NUMBER() PARTITION BY asin, sid, country ORDER BY is_delete asc` 取 rn=1（在售优先）；硬排除 `seller_sku='PESPL0110W-T1'`；
  - 全部 data_source='系统自动匹配'；最终 LEFT JOIN import_dim_channel/import_dim_shop 关联渠道名/店铺名。
- 关键规则: 旧体系「正则链匹配值域」模式；hicc_sku_code 为「取出横杠或处理后大部分需与公司 SKU 匹配」的近似映射，非官方映射。

#### dim_warehouse_sku_mapping
- 目标表: dim_warehouse_sku_mapping（仓库 SKU 映射维度表，旧体系）
- 上游: `ods.shipout_product`、`ods.locad_product_inventory`、`ods.dbeehk_product`、`ods.maple_product_sku_info`、`ods.loho_local_product`、`ods.lingxing_amazon_seller_sku_list`、`ref('dim_prd_tk_products')`、`ods.walmart_wfs_inventory`、`ods.winit_sku_list`、`ref('dim_product_skus')`、`ods.import_dim_warehouse`
- 清洗逻辑: 9 个仓库平台分支 UNION ALL：
  - shipout：org_id 映射仓库（55752→w003 / 52037→w002），oms_sku 关联 dim_product_skus.gtin_inner_box 或取 oms_sku，`REGEXP_REPLACE(r'-[^-]*$','')` 去尾段，GROUP BY 去重；
  - locad：brand_id 映射（3125→w006 / 2545→w005），sku 双重去尾（`-` 尾段 + `_` 尾段）；
  - dbeehk：固定 w009，barcode 关联 dim_product_skus.upc 得 sku_code；
  - maple：固定 w004，channel_sku_code 原值；
  - loho：固定 w007，sku 去 `-` 尾段；
  - amazon：领星 listing，**j1~j7+j_def 八条 LEFT JOIN 链**（三字母前缀/AZ 中段/两字母前缀/W-M/去前两字符/EDF 原值/EDF 去首字母/原值），`COALESCE(j1..j_def.sku_code)` 取第一个命中，`QUALIFY ROW_NUMBER() PARTITION BY fnsku, sid ORDER BY is_delete asc = 1`；
  - tk：`REGEXP_REPLACE(r'^T-K','')` 剥离前缀；
  - walmart：wfs_inventory，`^WM(.*?)-` 提取（双 W-M/WM 前缀口径）；
  - winit：w016/w017，sku_code 关联 gtin_inner_box 或取原值；
  - 最终 LEFT JOIN import_dim_warehouse 取仓库名。
- 关键规则: 各平台经不同归一手段产出「处理后的 HICC 公司 SKU」；warehouse_platform 字段标记数据来源平台（shipout/locad/dbeehk/maple/loho/amazon/tk/walmart/winit）；旧体系映射为近似匹配，后续由 dim_product_skus_warehouse 承接（其注释指明可改引本表）。

---

### 关键业务规则速查

| 规则 | 落点 | 内容 |
|------|------|------|
| 渠道代码收敛 | dim_business_channel_v2 | p001=Amazon…p010=Shopify，ToB p015-p018 |
| 国家级时区兜底 | dim_country_v2 | 23 国 CASE 硬编码；多时区大国取东部 |
| 店铺级时区 | dim_shop_v2 | Amazon US/CA→LA（实测覆盖），BR→Manaus，其余国家级默认 |
| 汇率折算 | dim_exchange_rates | 主流 10 币种 ÷USD，小币种 10000/(rate×usd)；月粒度；本月无数据用最近工作日模拟 |
| 业务周 | dim_calendar_cn/local | 周五~下周四业务周，+3 天对齐自然周 |
| 三源商品主数据 | dim_product_skus | main(主数据)>manual(手工)>bundle(组合)，NOT EXISTS 排他；is_bundle 标记 |
| SKU 归一（新） | dim_hicc_sku_mapping_v2 | L1 官方>L2 regex>L3 待治理；P3 combo 主成分；P4 parent 继承；L5 bundle 身份；grain_key 唯一 |
| SKU 归一（旧） | dim_sku_mapping / dim_warehouse_sku_mapping | 正则链 + 值域 LEFT JOIN，COALESCE 取首命中 |
| vine 标记 | dim_product_skus_sales / _warehouse | Amazon 渠道 '%vine%' / '%-v%'（v2 仅 %vine% 防误伤） |
| 去重优先级 | dim_product_skus_warehouse | 手动录入 > 系统自动 |
| 去重优先级 | dim_hicc_sku_mapping_v2 | 已归一>官方>非vine>在售>短SKU>字典序 |
| 采购成本 | dim_product_skus_warehouse | MAX(cg_price) by sku_code，0 兜底 |
| Meta 海外仓渠道 | dim_product_skus_warehouse | w002：-UPC/Place→p017，否则 p010 |
| 退市/新品 | dim_product_skus | is_delisting（product_labels）、is_new（extension_data） |

---

### 共性模式结论

1. **新旧两代 SKU 归一并存**：v2 系列（dim_hicc_sku_mapping_v2）采用「官方映射优先 + 待治理清单」替代旧「正则链近似匹配」（dim_sku_mapping/dim_warehouse_sku_mapping），后者仍被商品主数据链路引用，但注释已指向新表。
2. **治理口径集中在 09_mdm 维表**（时区映射、渠道代码、SKU 值域、bundle 身份），事实表只做外键关联，不散落口径。
3. **完整性硬门禁**：翻译层（dim_hicc_sku_mapping_v2.dim_hicc_sku_code）NOT NULL 100%，未归一进治理清单而非静默 NULL。
4. **确定性排序去重**是全库通用范式：优先数据源可信度，其次业务状态（在售/非 vine），再次键形态（短 SKU）。
