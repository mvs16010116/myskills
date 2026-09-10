# 库存/履约域 清洗逻辑与规则（05_inv + 04_ful）

> 分析范围：`hicc_data_platform/models/05_inv/`（dim 2 + dwd 59 + dws 3 = 64 个模型，含 13 张 `*_v2_snap` 表与 `dwd_inv_global_detail_v2_snap`）、`hicc_data_platform/models/04_ful/dwd/dwd_ful_amazon_shipment_di.sql`。
> 架构基调：DIM → DWD → DWS 分层；DWD 内部存在**双链路**——旧版 `snap/di` 加工链路（对齐旧库 `dwd.dwd_scm_*`）与新 v2 链路（`*_v2_snap` 干净 ODS + `dwd_inv_global_detail_v2_snap` 统一口径），DWS 层分别供不同消费方。

---

## 05_inv 库存域

### 通用清洗规则（多个表共用的模式）

1. **latest_synctime CTE（取最新批次）**：每个 v2_snap 表顶部先 `WITH latest_synctime AS (SELECT <聚合> AS synctime FROM ods.<源表>)`，再 `WHERE synctime = (SELECT synctime FROM latest_synctime)` 只保留最新一次采集批次（覆盖增量/多批次残留）。
   - 差异三种（见下表）：`COALESCE(MAX(synctime), MAX(updated_at))`（源有 updated_at，兜底）｜`COALESCE(MAX(synctime), CURRENT_TIMESTAMP())`（源无 updated_at，用当前时间兜底）｜`MAX(synctime)`（源无 updated_at，不兜底）。
2. **sync_date_p 分区列**：`DATE(synctime)`，所有 v2_snap 表 `partition_by sync_date_p (DATE)`；旧版 snap 表用 `fdate_p = CURRENT_DATE()` 分区；global_detail 用 `DATE(CURRENT_TIMESTAMP())`。
3. **跨平台映射列（决策 9 统一追加）**：每张 v2_snap 末尾追加 `dim_hicc_sku_code / dim_warehouse_code / dim_warehouse_name / dim_channel_code / dim_country_code / dim_shop_code / dim_shop_name / dim_data_source`，不破坏 ODS 原字段。
   - **SKU 归一核心维表**：`dim.dim_product_skus_warehouse`（仓×渠道SKU×HICC SKU 唯一核心），映射键因仓而异：
     - 按 `warehouse_sku_id`（fnsku/reference_code/sys_code/sku/barcode…）+ `warehouse_id`：FBA、TikTok、Walmart、Loho（`LIKE 'L%'`）、dbeehk、winit、maple、locad（`LENGTH(warehouse_sku_id)=6`）；
     - 按 `warehouse_sku_code`：locad、maple、winit 出库；
     - 按 `upc = barcode` 关联 `dim.dim_product_skus`：dbeehk；
     - 按 `sku_id` 关联 `dim.dim_prd_shipout_product`：shipout；
     - 汇总时按 `(warehouse_id, hicc_sku_code)` 用 `ANY_VALUE(purchased_cost_price/vine_or_not)` 补维。
   - 仓库维表关联统一 `SELECT warehouse_id, ANY_VALUE(warehouse_name/belong_to_channel_code/belong_to_country_code) ... GROUP BY warehouse_id`（防仓库行发散）。
4. **金额折算**：`SAFE_CAST(JSON_VALUE(...) AS NUMERIC/INT64)` 防脏数据；采购价 `cg_price`（FBA 源字段 / `pdt_ods.product_skus_purchase` 取 `MAX(cg_price)` / `dim_product_skus_warehouse.purchased_cost_price`）；`金额 = 数量 × unit_qty × 采购价`（global_detail 中 `stock_amt_cny`）；本域均为人民币采购价口径，未见汇率折算（汇率逻辑在其他域）。
5. **JSON 展开方式**：
   - **数组展开**：`CROSS JOIN/LEFT JOIN UNNEST(JSON_QUERY_ARRAY(col, '$'))`（loho_inbound 升 SKU 行粒度、shipout 双层展开、FBA item_list、tk planned_goods、winit merchandise_list、walmart nodes 等）；
   - **对象取值**：`JSON_EXTRACT_SCALAR` / `JSON_VALUE`（含 `COLLATE(col,'')` 防御非 JSON 脏串、`PARSE_JSON` 重解析、`$[0]` 取首元素、`$['0To90days']` 括号键）；
   - **保留策略**：原 JSON 列"清洗后不保留"（shipout/walmart v2）或"透传保留"（FBA fba_storage_quantity_list、winit sales_shops 暂不展开）。
6. **库存三态展开（长格式）**：`dwd_inv_global_detail_v2_snap` 用 `CROSS JOIN UNNEST(['available','in_transit','unavailable']) AS v` 把每仓拆成多行 `stock_status`，各平台只产出自己拥有的状态，`CASE v WHEN ...` 映射源字段，并在 WHERE 中过滤 `SAFE_CAST(...) IS NOT NULL`（零值行剔除）。
7. **去重/平摊**：多对一关联一律 `GROUP BY + MAX/ANY_VALUE` 收敛（SKU 映射、仓库维表）；`SELECT DISTINCT`（tk_fbt_stock_snap）；FIFO 累计扣减（shipout 两处）；`ROW_NUMBER/DENSE_RANK` 取最新（inbound_shipment_status 取运单 rn=1、tk 操作日志取 dr=1）。
8. **时间处理**：`SAFE.PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S', ...)`（loho/maple STRING→TIMESTAMP）；Unix 秒 `TIMESTAMP_SECONDS`（tk update_time、betterxpr SendInTime）；毫秒 `TIMESTAMP_MILLIS(..., "America/New_York")`（tk 时区）；`DATETIME(x, 'Asia/Shanghai')` 转东八区（locad last_synced_at）；出库 fdate 跨时区 `DATETIME(TIMESTAMP(date_finish,'Asia/Shanghai'),'America/Los_Angeles')`（winit 出库）；`etl_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', CURRENT_TIMESTAMP()+INTERVAL 8 HOUR)`（北京时间）。
9. **状态过滤/枚举归一**：
   - 在途筛选：dbeehk `status='待入倉'`；loho `status IN ('0','1','2','3')`；shipout `status IN ('2','4')`；maple 状态 0-7 中文映射（含剔除 5 已取消/7 驳回）；winit 状态码→中文（DR/OD/RE/IC/TS/PEWC/EWC/SHD/STOP）；winit 出库 `status IN ('DLC','OBC')`；locad 出库 `status <> 'CANCELLED' AND picked_date IS NOT NULL`；
   - 退货剔除：amazon_removal `removal_order_type='Return'`、`marketplace <> '美国'`（美国仓数据口径）、`out_stock_flag IS NULL`（未出库才算可售）。
10. **Vine 标记**：`LOWER(seller_sku) LIKE '%vine%' OR LOWER(seller_sku) LIKE '%-v%'` → `'vine'`，否则 NULL（FBA 链路，global_detail 中由 `dim_product_skus_warehouse.vine_or_not` COALESCE 补全）。
11. **不可售数量职责**：old DWD（snap/di）只产出 Available/In_transit 两态；**不可售（unavailable）只在 v2 链路（global_detail）落地**（FBA afn_unsellable、dbeehk amount_processing、locad unusable、loho damaged、maple lock、shipout broken、tk unfulfillable、walmart reserved、winit frozen）。
12. **旧链路 dim_data_source 沿用旧表表名**（如 `dwd_scm_lingxing_amazon_fba_inventory_partition`），便于研发按旧名排查；v2 链路用简短标识（`amazon_fba`/`dbeehk_stock`/`loho_inbound`…）。

---

### 各表清洗逻辑

#### A. dim 维表层

##### dim_inv_warehouse_attr（table，cluster_by warehouse_id）
- 目标表: dim.dim_inv_warehouse_attr（公共仓分类维表，全链路仓库分类唯一权威）
- 上游: ods.import_dim_warehouse（仓库主数据全集，10 渠道 JOIN）
- 清洗逻辑: `warehouse_type` 归一（Platform/OVERSEAS→OVERSEAS；Domestic→DOMESTIC；新值→NULL 防误判）；`supply_code` 服务商归属 CASE：channel_code p001→AMAZON / p002→WALMART / p009→TIKTOK；warehouse_id w018→SHOWROM（SG_value 飞书）、w016/w017→WINIT、w005/w006→LOCAD、w007→LOHO、w009→DBEEHK、w004→MAPPLE、w002/w003→SHIPOUT（Meta海外仓/SGR海外仓同一服务商）、w001→DOMESTIC（坪山工厂）、未知→NULL
- 关键规则: 主键 warehouse_id（每仓一行）；channel_code 是"仓库服务的销售渠道"，supply_code 是"服务商身份"，两者语义分离

##### dim_amazon_shop_mapping（table）
- 目标表: dim.dim_amazon_shop_mapping（FBA 多站点仓库→店铺映射配置表）
- 上游: 纯手工 SELECT union all 配置（无源表）
- 清洗逻辑: 当 FBA `seller_group_name` 含逗号（多站点合并账号）时按 `name`(仓库) 映射为单一 shop_name/shop_id；欧洲仓统一映射德国（东连-hicc欧洲仓→DE、HICCPet 沙特+阿联酋→取沙特、PetThem 欧洲→DE）；北美仓统一映射美国站点
- 关键规则: 匹配优先级 = `seller_group_name` 非 NULL 精确匹配 > NULL 通配；同类型内 `priority` 越小越高；注意 HICCPet 与 Hiccpet 大小写差异

---

#### B. Amazon FBA 链路

##### dwd_inv_amazon_fba_stock_v2_snap（v2 干净 ODS）
- 目标表: dwd.dwd_inv_amazon_fba_stock_v2_snap（FBA 库存，含库龄分桶明细）
- 上游: ods.lingxing_amazon_fba_inventory + dim_amazon_shop_mapping + ods.import_dim_shop + dim_warehouse_sku_mapping + dim_product_skus_warehouse
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))` 取最新批次；`fba_storage_quantity_list`（共享仓才有值）JSON 不展开原样透传；**店铺映射**：`seller_group_name LIKE '%,%'`（多站点）才查 dim_amazon_shop_mapping（exact 精确 + wildcard 通配双 LEFT JOIN），单站点直接用 seller_group_name，`COALESCE(exact, wildcard, 原值)` 关联 import_dim_shop 取 shop_id；**仓库代码**：`sid=0 → shop.shop_id，否则 CAST(sid AS STRING)`；**SKU 映射**：fnsku→dim_warehouse_sku_mapping（按 warehouse_sku_id+warehouse_code 分组 MAX(hicc_sku_code)）；仓库维表按 warehouse_id ANY_VALUE 补名称/渠道/国家；追加 10 个 dim_* 列
- 关键规则: 保留 ODS 原字段名与顺序（83 列）；`sync_date_p = DATE(synctime)`

##### dwd_inv_amazon_fba_stock_snap / dwd_inv_amazon_fba_stock_di（旧链路）
- 目标表: dwd.dwd_inv_amazon_fba_stock_snap（增量快照，insert_overwrite，fdate_p 分区）→ dwd_inv_amazon_fba_stock_di（table）
- 上游: ods.lingxing_amazon_fba_inventory → snap；di 再关联 ods.lingxing_amazon_product_info（按 sku 取 cg_price）、ods.import_dim_shop（内联 CASE 店铺映射，逻辑同 v2 但写死映射串）、dim_warehouse_sku_mapping（fnsku+warehouse_code）
- 清洗逻辑: snap 透传 ODS + `CURRENT_TIMESTAMP() AS business_time` + `current_date() AS fdate_p`；di 计算 `Available_Stock_qty = afn_fulfillable_quantity + reserved_fc_transfers + reserved_fc_processing`、`In_transit_Stock_qty = afn_inbound_shipped_quantity`、金额 = `cg_price × 数量`；vine 标记（%vine% / %-v%）
- 关键规则: 旧链路口径与 v2 一致（available 三字段求和）；dim_data_source 保留旧表名

##### dwd_inv_amazon_inbound_txn_di
- 目标表: dwd.dwd_inv_amazon_inbound_txn_di（FBA 入库事务）
- 上游: ods.lingxing_amazon_shipment_list（item_list + ship_to_address 双 JSON 展开）+ dim_product_skus_warehouse
- 清洗逻辑: `UNNEST(JSON_QUERY_ARRAY(item_list,'$'))` 逐 SKU 展开（sku/fnsku/msku/asin/quantity_shipped/init_quantity_shipped/quantity_received/quantity_shipped_local/quantity_in_case/release_date/expiration_date）；ship_to_address 取 country/state/city；`datetime(start_date) AS create_time`；`SAFE_CAST` 时间
- 关键规则: hicc_sku 按 `fnsku + CAST(sid AS STRING)=warehouse_id` 关联 dim_product_skus_warehouse

##### dwd_inv_amazon_removal_shipment_v2_snap（v2，手动编写）
- 目标表: dwd.dwd_inv_amazon_removal_shipment_v2_snap（退货移除订单，单号炸裂+数量分摊+仓库归属）
- 上游: ods.lingxing_amazon_removal_shipment_list + 5 张物流表（amazon_return_betterxpr / amazon_return_stglobal / amazon_return_stglobal_us / amazon_return_betterxpr_out_order / import_return_warehouse_records）+ dim_warehouse_sku_mapping + dim_product_skus_warehouse
- 清洗逻辑: ①过滤 `removal_order_type='Return'`；②tracking_number 逗号拆分 + `UPPER` + `TRIM` + DISTINCT 去重 + 剔除空值（空数组保留 `''` 行不丢数）；③`UNNEST(...) WITH OFFSET` 炸裂 + shipped_quantity 整数平摊（`FLOOR(qty/len) + IF(off<MOD(qty,len),1,0)`，如 10/3→4,3,3）；④LEFT JOIN 5 物流表（`STRPOS` 子串匹配，英国出库表 `Status NOT IN ('7')`）；⑤派生：`return_other_warehouse`（物流命中 w011/w012/w013 → sid=0 时解析 seller_name JSON 数组按 marketplace 美国>德国优先级取 sid → 兜底 CAST(sid)）、`out_stock_flag`（rbpx_GB_out/stglobal_out/import_return_warehouse/stglobal_out_us）、`inbound_date = COALESCE(DE listingDate, US ReceiptTime, UK TIMESTAMP_SECONDS(SendInTime))`；⑥SKU 映射 fnsku→dim_warehouse_sku_mapping（ANY_VALUE）；⑦仓库维表（w011/w012/w013 不在维表，硬编码名称+渠道 p001+国家 GB/DE/US）
- 关键规则: 退货仓归属优先级 英国>德国>美国；`dim_channel_code = COALESCE(wh, 'p001')`；`unit_type='Single item'、convert_rate=1`

##### dwd_inv_amazon_removal_shipment_snap / dwd_inv_amazon_removal_shipment_di（旧链路）
- 目标表: dwd.dwd_inv_amazon_removal_shipment_snap（增量快照，synctime 分区）→ di（table 透传）
- 上游: 同 v2（5 物流表），di 只透传 snap 不重 JOIN（保留历史快照语义）
- 清洗逻辑: 与 v2 完全同构（raw_split_data→exploded_and_distributed→joined_data），额外派生 `matched_warehouse_code / DE_account_ID / DE_warehouse_name`；snap 用 `business_time + fdate_p`；di 新增 `dim_data_source='lingxing_amazon_removal_shipment_list_partition'`
- 关键规则: di 表为 table 物化，直接透传 snap 派生字段，避免覆盖快照历史语义

---

#### C. 中国仓（国内工厂仓 w001）

##### dwd_inv_chinese_stock_v2_snap
- 目标表: dwd.dwd_inv_chinese_stock_v2_snap（国内仓库存，人工导入）
- 上游: ods.import_chinese_stock + dim_product_skus_warehouse
- 清洗逻辑: **synctime 用 `COALESCE(MAX(synctime), CURRENT_TIMESTAMP())`**（该表无 updated_at，等价 MAX(synctime) 兜底）；expiration_date 源含非 ISO 格式（如 10/9/2027）注释要求解析为标准 DATE（SQL 当前直接透传）；`dim_hicc_sku_code = sku 自身`（国内 SKU 即 HICC SKU）；`dim_warehouse_code 硬编码 'w001'`
- 关键规则: 追加维表仅补名称/渠道/国家；无 JSON 展开

##### dwd_inv_chinese_stock_snap / dwd_inv_chinese_stock_di（旧链路）
- 目标表: snap（增量）→ di（table 透传）
- 上游: ods.import_chinese_stock + pdt_ods.dim_country（country_code→country_id）
- 清洗逻辑: `CAST(channel_id AS INT64)`；关联 dim_country 取 country_id；di 纯透传

---

#### D. dbeehk 香港仓（w009）

##### dwd_inv_dbeehk_stock_v2_snap（批次库存）
- 目标表: dwd.dwd_inv_dbeehk_stock_v2_snap（批次级库存）
- 上游: ods.dbeehk_stock + dim_product_skus + dim_product_skus_warehouse
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；**SKU 映射按 `CAST(upc AS STRING)=CAST(barcode AS STRING)` 关联 dim_product_skus**（条码匹配）；'w009' 硬编码
- 关键规则: 批次字段（lot_*）透传保留，供 global_detail 算库龄

##### dwd_inv_dbeehk_inbound_v2_snap（入库明细）
- 目标表: dwd.dwd_inv_dbeehk_inbound_v2_snap（入库明细）
- 上游: ods.dbeehk_inbound_details + dim_product_skus + dim_product_skus_warehouse
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；upc=barcode 关联 dim_product_skus 取 sku_code；'w009' 硬编码
- 关键规则: forecast_quantity/confirmed_quantity 透传（global_detail 用它算在途=预报-确认）

##### dwd_inv_dbeehk_stock_snap / dwd_inv_dbeehk_available_stock_di（旧链路）
- 目标表: snap（增量，updated_at/created_at 分区）→ di（table）
- 上游: ods.dbeehk_stock → snap；di 关联 dim_product_skus（upc=barcode）
- 清洗逻辑: snap 类型强化（CAST INT64/FLOAT64）；di：`Available = lot_remaining_amount`，`Available_Stock_cny = lot_remaining_amount × dps.purchased_cost_price`，In_transit 硬编码 0，belong_to_channel_code='p016'、country='HK'
- 关键规则: 批次效期 `lot_expiry_date AS expiry_date`

##### dwd_inv_dbeehk_inbound_details_snap / dwd_inv_dbeehk_intransit_stock_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.dbeehk_inbound_details → snap；di 再关联 ods.dbeehk_product + dim_product_skus（upc=barcode 构造 sku_mapping）
- 清洗逻辑: **di 过滤 `WHERE status='待入倉'`（任务重点规则）**；`In_transit = forecast_quantity`，金额 = forecast_quantity × purchased_cost_price；Available 硬编码 0
- 关键规则: dbeehk_product 中 sku 作为 warehouse_sku_id、barcode 作为 channel 编码

##### dwd_inv_dbeehk_inbound_txn_di
- 目标表: dwd.dwd_inv_dbeehk_inbound_txn_di（入库事务）
- 上游: ods.dbeehk_inbound_details JOIN ods.dbeehk_inbound_list（stock_in_id）+ dim_product_skus_warehouse（w009）
- 清洗逻辑: `shipment_id=inbound_order_no`；`shipped_qty=forecast_quantity`、`rec_qty=confirmed_quantity`；closed_time=stock_in_arrival_date；barcode→warehouse_sku_code 关联映射
- 关键规则: join 用 `main.inbound_order_no = CAST(t1.stock_in_id AS STRING)`

---

#### E. locad 海外仓（w005 新加坡 / w006 马来西亚）

##### dwd_inv_locad_stock_v2_snap
- 目标表: dwd.dwd_inv_locad_stock_v2_snap（海外仓库存）
- 上游: ods.locad_stock + dim_product_skus_warehouse
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；`expired(tinyint)` 枚举归一（注释）；**仓库映射 `CASE brand_id WHEN 3125 THEN 'w006' WHEN 2545 THEN 'w005'`**；SKU 映射 `inventory_sku = warehouse_sku_code AND warehouse_id` 匹配，过滤 `LENGTH(warehouse_sku_id)=6`
- 关键规则: brand_id 即仓库标识；timezone/timezone_name/last_synced_at 透传

##### dwd_inv_locad_stock_snap / dwd_inv_locad_stock_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.locad_stock → snap；di 关联 dim_product_skus_warehouse（LENGTH=6）
- 清洗逻辑: snap 中 `batch` 置 NULL、`expired` 置 NULL、`DATETIME(last_synced_at,'Asia/Shanghai')`；di：brand_id 3125→w006(MY)/2545→w005(SG)，`Available = sellable_stock`，金额 = sellable_stock × purchased_cost_price，belong_to_country_code 按 brand_id 映射 MY/SG、channel='APAC'
- 关键规则: 用 sellable_stock（可售）而非 usable_stock 作可用

##### dwd_inv_locad_inbound_txn_di
- 目标表: dwd.dwd_inv_locad_inbound_txn_di（入库事务）
- 上游: ods.locad_inbound_details JOIN locad_inbound_list JOIN locad_inbound_product_list + dim_product_skus_warehouse（w005/w006）
- 清洗逻辑: 三表 JOIN（id 关联）；`JSON_VALUE(t2.brand,'$.id')` 取 brand；`datetime_add(datetime(created_at), interval 8 hour)` 补东八区（completed_at 签收 0 时区）；品牌 id→仓库映射（w005='2545'/w006='3125'）双条件关联
- 关键规则: shipped_qty=total_consignment_quantity、rec_qty=total_received_quantity

---

#### F. loho 百家海外仓_SG（w007）

##### dwd_inv_loho_stock_v2_snap
- 目标表: dwd.dwd_inv_loho_stock_v2_snap（库存）
- 上游: ods.loho_stock + dim_product_skus_warehouse（w007）
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；SKU 映射 `sys_code = warehouse_sku_id AND warehouse_id='w007' AND warehouse_sku_id LIKE 'L%'`
- 关键规则: 'w007' 硬编码

##### dwd_inv_loho_inbound_v2_snap（手动拍板：行粒度升 SKU）
- 目标表: dwd.dwd_inv_loho_inbound_v2_snap（入库单列表，SKU 行粒度）
- 上游: ods.loho_inbound_list + dim_product_skus_warehouse（w007）
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；**sku_items 数组 `LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(sku_items,'$'))` 展开为 item_* 平铺列，行粒度从入库单升为 SKU 行**；create_time/grounding_time/estimate_date/check_in_time `SAFE.PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S')` STRING→TIMESTAMP；`SAFE_CAST(num/abroadReceiveNum/damagedQty AS INT64)`；SKU 映射 sysCode→warehouse_sku_id（LIKE 'L%'）
- 关键规则: 展开用 JSON_EXTRACT_SCALAR；原 JSON 列 sku_items 保留

##### dwd_inv_loho_stock_snap / dwd_inv_loho_available_stock_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.loho_stock → snap；di 关联 dim_product_skus_warehouse（w007 + LIKE 'L%'）
- 清洗逻辑: di：`Available = available_num`，金额 = available_num × purchased_cost_price，channel='p015'、country='SG'
- 关键规则: sys_code 为渠道 SKU 编码（warehouse_sku_id）

##### dwd_inv_loho_inbound_list_snap / dwd_inv_loho_intransit_stock_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.loho_inbound_list → snap；di 展开 sku_items + 关联 wmapping（w007）
- 清洗逻辑: **di 过滤 `status IN ('0','1','2','3')`（待审核/审核通过/部分收货/全部出库）**；`net_qty = num - abroadReceiveNum`；In_transit = net_qty，金额 = net_qty × purchased_cost_price；Available=0；channel='p015'、country='US'
- 关键规则: 展开用 `UNNEST(JSON_QUERY_ARRAY(COLLATE(sku_items,'')))`

##### dwd_inv_loho_inbound_txn_di
- 目标表: dwd.dwd_inv_loho_inbound_txn_di（入库事务）
- 上游: ods.loho_inbound_list + dim_product_skus_warehouse（w007）
- 清洗逻辑: `LEFT JOIN UNNEST(JSON_QUERY_ARRAY(sku_items))`；`warehouse_sku_code = variationSku`；status 硬编码 `'待入库'`（过滤 status IN ('0','1','2','3')）；shipped_qty=num、rec_qty=abroadReceiveNum
- 关键规则: wmapping 按 warehouse_sku_code=variationSku 关联

---

#### G. maple 枫仓（w004，加拿大）

##### dwd_inv_maple_stock_v2_snap
- 目标表: dwd.dwd_inv_maple_stock_v2_snap（枫仓库存）
- 上游: ods.maple_stock + dim_product_skus_warehouse（w004）
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；operateTime `SAFE.PARSE_TIMESTAMP`；**productStockDtl/boxStockDtl/fbaReturnStockDtl 三个 JSON 对象各展开 lockAmount/availableAmount/transportAmount 平铺字段**；SKU 映射 `sku = warehouse_sku_code AND w004`
- 关键规则: 9 个 JSON 展开列；原 JSON 列保留

##### dwd_inv_maple_stock_snap / dwd_inv_maple_stock_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.maple_stock → snap；di 关联 dim_product_skus_warehouse（w004）
- 清洗逻辑: **di 过滤 `WHERE stockType = 0`（商品库存）**；`JSON_VALUE(COLLATE(productStockDtl,''),'$.availableAmount/transportAmount')`；`Available=availableAmount、In_transit=transportAmount`，金额 × purchased_cost_price；channel='p018'、country='CA'
- 关键规则: skuId 作 channel_sku_code；stockType 区分商品/箱/FBA退货库存

##### dwd_inv_maple_inbound_txn_di
- 目标表: dwd.dwd_inv_maple_inbound_txn_di（入库事务）
- 上游: ods.maple_inbound_order_detail（inboundSkuVOList 展开）+ ods.maple_inbound_order
- 清洗逻辑: **status 0-7 中文映射（0新建/1待入库/2收货中/3已收货/4已上架/5已取消/6待审核/7驳回/其他）**；shipped_qty=quantity、rec_qty=receivedQuantity；channel='p018'、country='CA'
- 关键规则: dim_hicc_sku_code 直接取 JSON `$.sku`（未走维表映射）

---

#### H. shipout（Meta 海外仓 w002 / SGR 海外仓 w003）

##### dwd_inv_shipout_inbound_v2_snap（手动编写，含 FIFO）
- 目标表: dwd.dwd_inv_shipout_inbound_v2_snap（入库库存，SKU×批次明细）
- 上游: ods.shipout_inbound_stock + dim_prd_shipout_product + dim_product_skus_warehouse
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；**父子明细**：`warehouse_stock_list[0]`（恒 1 仓）顶层透传 ava_qty/standard_qty/broken_qty/pkg_qty + 追加仓级列（warehouse_id/inbounding_qty/outbounding_qty/converted_qty，随批次行复制）；`sku_lot_info_list` 经 `LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(...,'$'))` 展开 lot_* 平铺；**保留规则**：有批次 或 有出入库在途（inbounding+outbounding>0）的行保留，纯零库存占位行（172 行）丢弃；**FIFO 计算**：按 sku_id+client_org_id 分组、lot_expired_time 升序（NULLS LAST）跑 `SUM(lot_standard_qty) OVER` 累计 + LAG prev_cumsum，`lot_available_qty = prev_cumsum>=outbounding ? 全留 : cumsum<=outbounding ? 0 : cumsum-outbounding`；SKU 映射 `dim_prd_shipout_product.sku_id` → dim_hicc_sku_code/dim_warehouse_id/unit_type/convert_rate；原 JSON 列 warehouse_stock_list/sku_lot_info_list 清洗后不保留
- 关键规则: 在途行无批次，lot_* 全 NULL；FIFO 只对 `dim_hicc_sku_code IS NOT NULL` 的行计算

##### dwd_inv_shipout_inbound_order_snap / dwd_inv_shipout_inbound_order_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.shipout_inbound_order → snap；di 展开 inbound_item_count + dim_prd_shipout_product + dim_product_skus_warehouse + dim_product_skus
- 清洗逻辑: **di 过滤 `status IN ('2','4')`（待入库/入库接收中，注释：1草稿 2待入库 4入库接收中 5取消 6完结 7删除）**；`net_qty = quantity - receivedQuantity`；**w002 强制 convert_rate=1**；dim_warehouse_id 从 dim_prd_shipout_product 取；`In_transit = net_qty × COALESCE(convert_rate,1)`，金额 × purchased_cost_price；warehouse_id 映射（1845645392399155201→w002、1643077612316672001→w003）
- 关键规则: `raw_qty = net_qty`（未乘换算率），unit_qty 用 CTE 输出字段（与旧代码一致）

##### dwd_inv_shipout_inbound_stock_snap / dwd_inv_shipout_inbound_stock_di（旧链路，FIFO 扣出库中）
- 目标表: snap（增量）→ di（table）
- 上游: ods.shipout_inbound_stock → snap；di 双层 UNNEST + dim_prd_shipout_product
- 清洗逻辑: **双层展开**：`warehouse_stock_list[0].stockWithBizLotList` → `skuLotInfoList`（无 COLLATE）；提取 lot_qty（分子）、total_outbound（待分摊）、total_qty（分母，验证用）；**FIFO 扣减**：按 fdate_p+warehouse+hicc_sku 分组、expiry_date 升序累计 lot_qty，`deducted_qty = prev_cumsum>=total_outbound ? 0 : cumsum<=total_outbound ? lot_qty : total_outbound-prev_cumsum`；`Available = (lot_qty - deducted_qty) × unit_qty`、`Outbound_Stock_qty = deducted_qty × unit_qty`，金额 × purchased_cost_price；**belong_to_channel_code 规则**：w002 按 oms_sku 判定（`%-UPC%` 或 `%Place%`→p017，否则 p010），w003→p017；w002 强制 unit_qty=1；country='US'
- 关键规则: 输出验证列（total_outbound_qty/sys_lot_qty/lot_qty/deducted_qty/raw_qty）；`In_transit 硬编码 0`

##### dwd_inv_shipout_inbound_txn_di
- 目标表: dwd.dwd_inv_shipout_inbound_txn_di（入库事务）
- 上游: ods.shipout_inbound_order（inbound_item_count 展开）+ dim_product_skus_warehouse + dim_prd_shipout_product
- 清洗逻辑: 状态中文映射（1草稿/2待入库/4入库接收中/5取消/6完结/7删除）；w002（1845645392399155201）强制 convert_rate=1；`shipped_qty = quantity × convert_rate`、`rec_qty = receivedQuantity × convert_rate`；closed_time 仅 status=6 取 last_receive_time
- 关键规则: warehouse_sku_code=omsSku（cast 匹配）

---

#### I. TikTok FBT（HKUSCBQLEL2M / w010）

##### dwd_inv_tk_fbt_stock_v2_snap
- 目标表: dwd.dwd_inv_tk_fbt_stock_v2_snap（FBT 库存）
- 上游: ods.tk_fbt_stock + dim_product_skus_warehouse
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；**on_hand_detail JSON 展开 4 平铺字段**（total/reserved/available/unfulfillable_quantity）；`update_time` Unix 秒 `TIMESTAMP_SECONDS` 转 TIMESTAMP；SKU 映射 `reference_code = warehouse_sku_id AND warehouse_id='HKUSCBQLEL2M'`；dim_warehouse_code=shop_code
- 关键规则: skus/on_hand_detail 原 JSON 列保留

##### dwd_inv_tk_fbt_stock_snap / dwd_inv_tk_fbt_stock_di（旧链路）
- 目标表: snap（增量，`SELECT DISTINCT` 全量快照）→ di（table）
- 上游: ods.tk_fbt_stock → snap；di 关联 dim_product_skus_warehouse + ods.import_dim_warehouse + pdt_ods.product_skus_purchase
- 清洗逻辑: **SKU 映射用 `warehouse_sku_code = reference_code` 而非 id**（注释：部分新品 warehouse_sku_id 是 TK 数字 ID，按 id 匹配会漏；code 匹配是 id 匹配的严格超集，且 (warehouse_id, warehouse_sku_code)→hicc_sku_code 唯一）；采购价 `product_skus_purchase` 按 reference_code 取 MAX(cg_price)；`Available=available_quantity`、`In_transit=in_transit_quantity`；channel='p009'，country 从 import_dim_warehouse
- 关键规则: 老链路用 code 匹配，v2 链路用 id 匹配——口径差异点

##### dwd_inv_tk_inbound_txn_di
- 目标表: dwd.dwd_inv_tk_inbound_txn_di（入库事务）
- 上游: ods.tk_inbound_orders（planned_goods/order_operation_logs/received_batches 三数组）+ dim_product_skus + ods.import_dim_shop
- 清洗逻辑: 过滤 `order_id LIKE 'IBR%'`；planned_goods 展开（sku_ids/reference_code/quantity）；**order_operation_logs 用 `DENSE_RANK() OVER (PARTITION BY shipment_id ORDER BY operate_time DESC) dr=1` 取最新状态**；received_batches 按 shipment_id SUM(total_quantity) 汇总收量；`create_time = datetime(timestamp_millis(create_time), "America/New_York")` 纽约时区；hicc_sku 按 seller_sku=sku_code 关联 dim_product_skus；closed_time 仅 RECEIVED 取 operate_time；channel='p009'
- 关键规则: warehouse JSON 取 fbt_warehouse_id/name

---

#### J. Walmart WFS（3509afb2 / 73b35e81）

##### dwd_inv_walmart_wfs_stock_v2_snap
- 目标表: dwd.dwd_inv_walmart_wfs_stock_v2_snap（节点明细平铺）
- 上游: ods.walmart_wfs_inventory + dim_product_skus_warehouse
- 清洗逻辑: `COALESCE(MAX(synctime), MAX(updated_at))`；**nodes 数组 `CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(nodes,'$'))` 展开 node_* 平铺（恒 1 节点）**：inventoryData（stockStatus/onhandUnits/availableUnits/reservedUnits/inboundUnits/firstInStockDate/publishingStatus/itemLifecycle/unavailableUnits.inventoryReviewUnits+inventoryMovementUnits）+ inventoryAge 括号键取值（`$['0To90days']/['91To180days']/['181To270days']/['271To365days']/['365To450days']/['450PlusDays']/['365PlusDays']`）+ inventoryInsights（daysOfSupply/surplusUnits/outOfStockDate/suggestedUnits/sellThroughRate/customerFavorite/salesForecastWeek1to4/5to8/9to12）；SKU 映射 `client_id=warehouse_id AND sku=warehouse_sku_id`（warehouse_id IN 两店）；原 nodes 列不保留
- 关键规则: 对账恒等式 onhandUnits = availableUnits + reservedUnits + unavailableUnits 全表成立

##### dwd_inv_walmart_wfs_stock_snap / dwd_inv_walmart_wfs_stock_di（旧链路）
- 目标表: snap（增量，全量快照）→ di（table）
- 上游: ods.walmart_wfs_inventory → snap；di 关联 pdt_ods.product_skus_purchase
- 清洗逻辑: **SKU 规范化 `COALESCE(REGEXP_EXTRACT(COLLATE(sku,''), r'^(?:WM-|W-M)(.+)-AY[A-Z0-9]+$'), sku)` 去 WM-/W-M 前缀与 -AY 变体后缀**（di 内 SKU 均用规范化值）；nodes[0] JSON 取值；采购价按规范化 SKU 取 MAX(cg_price)；dim_data_source='dwd_scm_walmart_wfs_inventory_partition'
- 关键规则: 可用=onhandUnits（DWS 层）、在途=inboundUnits

##### dwd_inv_walmart_inbound_txn_di
- 目标表: dwd.dwd_inv_walmart_inbound_txn_di（入库事务）
- 上游: ods.walmart_inbound_shipments + walmart_inbound_shipment_items + dim_product_skus_warehouse
- 清洗逻辑: shipment+items 按 shipment_id 关联；`t2.sku = warehouse_sku_id AND warehouse_id IN ('3509afb2','73b35e81')`；shipped_qty=item_qty、rec_qty=received_qty；closed_time 仅 `shipment_status='CLOSED'` 取 shipment_update_date
- 关键规则: 无 JSON 展开（源已平铺）

---

#### K. winit 万邑通（w016 美东 USKY5 / w017 美西 US0001）

##### dwd_inv_winit_stock_v2_snap（组织级库存）
- 目标表: dwd.dwd_inv_winit_stock_v2_snap
- 上游: ods.winit_inventory_by_organization + dim_product_skus_warehouse + dim_product_skus
- 清洗逻辑: **synctime 用 `MAX(synctime)`（注释：该表无 updated_at 字段，不兜底）**；`sales_shops`（店铺编码数组 JSON）暂不展开透传保留；**unit_type/unit_qty 由 dim_product_skus 判定**：`gtin_inner_box IS NOT NULL → 'Inner Case' / unit_inner_box`，否则 `'Single item'/1`；仓库映射 `warehouse_code：US0001→w017、USKY5→w016、ELSE→w017`；SKU 映射 warehouse_sku_id+warehouse_id 双条件
- 关键规则: 三态字段 usable_qty/on_order_qty/in_stock_qty/frozen_qty 透传

##### dwd_inv_winit_inventory_by_organization_snap / dwd_inv_winit_org_stock_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.winit_inventory_by_organization → snap；di 关联 dim_product_skus_warehouse + dim_product_skus
- 清洗逻辑: **snap 中 synctime 需显式 `CAST(FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', synctime) AS STRING)`**（ODS 源 TIMESTAMP→目标 STRING，与其他表不同）；di：`Available = usable_qty × COALESCE(unit_inner_box,1)`、`In_transit = on_order_qty × unit_inner_box`，金额 × purchased_cost_price；**belong_to_channel_code 按 sales_channel 映射：TOB→p017 / GTM→p021 / shopify→p010 / PUBLIC→p010，否则 NULL**；country='US'；输出 raw_qty（未乘换算率）
- 关键规则: `dim_product_skus` 按 `gtin_inner_box = warehouse_sku_code` 关联取 unit_inner_box

##### dwd_inv_winit_inventory_by_type_snap / dwd_inv_winit_type_stock_di（旧链路）
- 目标表: snap（增量）→ di（table）
- 上游: ods.winit_inventory_by_type → snap；di 关联 dim_product_skus_warehouse + dim_product_skus
- 清洗逻辑: snap 全字段透传（70+ 列）+ synctime 透传；di：**`merchandise_serno SPLIT '-', [OFFSET(0)]` 截取前段关联 warehouse_sku_id**（w017）；`expiry_date = DATE(JSON_EXTRACT_SCALAR(batch_info_vo,'$.batchDate'))`；`Available = qty_available × unit_inner_box`、`In_transit = qty_ordered × unit_inner_box`；channel='p010'
- 关键规则: 商品级库存（merchandise_serno）；dps 按 gtin_inner_box=merchandise_code

##### dwd_inv_winit_inbound_order_di / dwd_inv_winit_inbound_txn_di
- 目标表: dwd_inv_winit_inbound_order_di（table，明细宽表）→ dwd_inv_winit_inbound_txn_di（事务口径）
- 上游: ods.winit_inbound_order_details（merchandise_list 展开）+ ods.winit_inbound_orders + dim_product_skus_warehouse
- 清洗逻辑: **merchandise_list `LEFT JOIN UNNEST(JSON_EXTRACT_ARRAY(...))` 展开**；**status 中文映射：DR草稿/OD已下单/RE已收货/IC验货完成/TS运输中/PEWC部分到仓/EWC已到仓/SHD已上架/STOP终止**；仓库映射 US0001→w017、USKY5→w016、ELSE w017；shipped_qty=quantity、rec_qty=actualQuantity、unit_qty=standardPartsNum（`shipped_qty=shipped_unit×unit_qty`）；SKU 映射 `productBarcode=warehouse_sku_id AND 仓库双条件`；channel='p010'、country='US'；`etl_time` 北京时间；**txn_di 中 channel_sku_code 含 '-' 时 `substr 截断到 '-'` 前再关联 w017**
- 关键规则: order_no 作 shipment_id（WI 开头），seller_order_no 作 shipment_id2（WYT/OB 开头）

##### dwd_scm_winit_outbound_di（出库，归 05_inv）
- 目标表: dwd.dwd_scm_winit_outbound_di（table，包裹×商品粒度）
- 上游: ods.winit_outbound_orders + dim_product_skus_warehouse（w016/w017）+ dim_product_skus + ods.sps_commerce_orders
- 清洗逻辑: **sku 列按逗号 `CROSS JOIN UNNEST(SPLIT(sku,','))` 拆行，再按 `@@` 拆分**：`[0]`=winit_sku_code、`[1]`=出库数量、`[2]`=winit_sku_id（可带 `-60X/-120X` 乘数后缀）；**unit_type 判定：`gtin_inner_box 命中→'Inner Case'`、`正则 r'-(\d+)' 命中→'Master Case'`、否则 'Single item'**；unit_qty = unit_inner_box 或正则乘数或 1；`Outbound_Stock_qty = raw_qty × unit_qty`、金额 × purchased_cost_price（COALESCE 0）；**dim_outbound_order_type 按 seller_order_no 规则分类**（'US HICC Pet'→Shopify；57%/TK→Tiktok-代发；IBR→Tiktok-FBT；WFA/GDM→Walmart-WFS；walmart/WMT→Walmart-代发；PO-211→Temu；KOL→KOL；PetsB2BDirect/Vitacost/AAFES/Chewy/iHerb/Petco 各自映射；否则 ToB_US）；`fdate = CAST(DATETIME(TIMESTAMP(date_finish,'Asia/Shanghai'),'America/Los_Angeles') AS DATE)`（东八区→洛杉矶跨时区，fdate_cn 保留东八区）；sps.po_number 模糊匹配（seller_order_no LIKE %po%）
- 关键规则: SKU 映射按 `REGEXP_REPLACE([2], r'-.*$','')` 去后缀 = warehouse_sku_id + 仓库映射（US0001→w017 ELSE→w016）；本表被 dwd_inv_warehouse_outbound_di 引用（status DLC/OBC 派送完成）

---

#### L. 出库/汇总/其他

##### dwd_inv_warehouse_outbound_di
- 目标表: dwd.dwd_inv_warehouse_outbound_di（table，全仓出库汇总）
- 上游: 4 段 UNION ALL：① ods.dbeehk_outbound_list + dbeehk_outbound_order_detail（package_info.items JSON 炸开）；② ods.locad_outbound_list + dim_product_skus_warehouse；③ ref dwd_scm_shipout_outbound_txn_di（shipout 大货出库）；④ ref dwd_scm_winit_outbound_di（万邑通出库）
- 清洗逻辑: dbeehk 段：`deliver_status=50` 才计 fdate（create_time 取日）、出库量=total_quantity、`dim_outbound_order_type = 'HKTV mall' ? 平台 : 'offline ToB'`；locad 段：`status <> 'CANCELLED' AND picked_date IS NOT NULL`、brand_id→w005/w006、packed_qty；shipout 段透传；winit 段 `status IN ('DLC','OBC')` 派送完成；统一输出 fdate/fdate_cn/Outbound_Stock_qty/Outbound_Stock_cny/unit_type='Single item'/unit_qty=1/raw_qty + `etl_time` 北京时间
- 关键规则: 出库三态统一口径（quantity × purchased_cost_price）；data_source_name 带渠道表名标识

##### dwd_inv_feishu_warehouse_sg_value_snap
- 目标表: dwd.dwd_inv_feishu_warehouse_sg_value_snap（SG_value 飞书采集库存，增量）
- 上游: ods.import_feishu_warehouse_sg_value（飞书多维表格）
- 清洗逻辑: **过滤 `source_table = '每天早上8同步到大数据平台'`**；fld* 字段透传；is_incremental 只回溯 1 天；business_time/fdate_p
- 关键规则: 对应 supply_code='SHOWROM'（w018），纯透传不加工

##### dwd_inv_scm_undelivered_order_details_snap
- 目标表: dwd.dwd_inv_scm_undelivered_order_details_snap（SCM 未交付订单，增量）
- 上游: ods.import_scm_undelivered_order_details
- 清洗逻辑: `CAST(id AS INT64)`；`order_time 置 NULL`；透传合同/供应商/已交付/未交付/半成品/成品数量与各日期
- 关键规则: 采购未交付在途口径（undelivered_quantity）

##### dwd_inv_inbound_shipment_status_di
- 目标表: dwd.dwd_inv_inbound_shipment_status_di（table，入库在途+运单在途状态总览）
- 上游: ref dws_inv_inbound_shipment_info_di + ref dws_inv_global_stock_snap + ods.import_dim_shop + ods.import_dim_warehouse + static_dim.dim_scm_shipment_exclusive
- 清洗逻辑: **在途筛选按平台枚举**：amazon `inbound_status IN ('DELIVERED','CHECKED_IN','IN_TRANSIT','SHIPPED')`；tk `IN ('TO_BE_RECEIVED','ARRIVE_HUB','PARTIALLY_RECEIVED','RECEIVING')`；shipout `='待入库'`；locad `NOT IN ('COMPLETED','CANCELLED','STOCK_INBOUNDED','ASN_DRAFT','ASN_REJECTED')`；dbeehk `='待入倉'`；walmart `IN ('RECEIVING_IN_PROGRESS','AWAITING_DELIVERY','PENDING_SHIPMENT_DETAILS','PENDING_APPOINTMENT')`；winit `='TS'`；或运单在途（`NOT REGEXP_CONTAINS(?, '(?i)签收|已收货') AND LENGTH(shipment_id)>8 AND (predict_arrival_date>今天 OR NULL)`）；**rename_shipment_status 阶段重命名**（签收入库→已送达→清关→提柜→已抵港→已开船→已报关→已揽收，按日期字段优先级）；FULL OUTER JOIN global_stock_snap（shop_id+hicc_sku）补 available/in_transit；窗口求和 inbound_shipped_qty/missing_shipment_shipped_qty/missing_collect_shipped_qty（按 shop_id+hicc_sku）；最后排除 `KOL|XM1D` 与 dim_scm_shipment_exclusive 黑名单
- 关键规则: 该模型在 dws/schema.yml 登记（位于 05_inv/dws 目录但属 dwd 逻辑）；warehouse_name 对 walmart 店铺硬编码 'walmart'

##### dwd_inv_global_detail_v2_snap（13 张 v2_snap 汇总，核心统一口径）
- 目标表: dwd.dwd_inv_global_detail_v2_snap（统一口径长格式：stock_status + stock_qty）
- 上游: 全部 13 张 `dwd_inv_*_v2_snap` + dim_product_skus_warehouse
- 清洗逻辑: **14 段 UNION ALL（13 仓 + amazon_return 拆两段）**，每段统一输出 24 列（wh_platform/dim_*/wh_sku_id/wh_sku_code/asin/purchased_cost_price/vine_or_not/stock_status/stock_qty/age_bucket/granularity/inbound_date/expiry_date/batch_no/unit_type/unit_qty/synctime）：
  - amazon：available = afn_fulfillable + reserved_fc_transfers + reserved_fc_processing；in_transit = afn_inbound_shipped_quantity；unavailable = afn_unsellable_quantity；库龄分桶从源 inv_age_* 字段降序映射（仅 available）；成本=cg_price（SAFE_CAST NUMERIC）；vine 由 seller_sku 判定
  - chinese：available = stock_quantity；expiry_date 透传；无库龄
  - dbeehk 批次：available=lot_remaining_amount / unavailable=amount_processing；库龄由 stock_in_arrival_date 用 `DATE_DIFF(CURRENT_DATE(), ...)` 推算；granularity='inbound_batch'，带 inbound_date/batch_no
  - dbeehk 入库在途：in_transit = `GREATEST(forecast_quantity - confirmed_quantity, 0)`（预报-确认=真正在途，当前全为 '完成' 状态在途=0）
  - locad：available=sellable_stock / unavailable=unusable_stock
  - loho 可用：available=available_num
  - loho 入库：in_transit = item_num - item_abroad_receive_num - item_damaged_qty；unavailable = item_damaged_qty；库龄由 create_time
  - maple：available=productStockDtl_available_amount / in_transit=transport_amount / unavailable=lock_amount
  - shipout：available = lot_available_qty × COALESCE(convert_rate,1)（FIFO 后可用）；in_transit=inbounding_qty（仓级已在单件）；unavailable = lot_broken_qty × convert_rate；库龄由 lot_inbound_time（`SPLIT(...,'T')[SAFE_OFFSET(0)]` + SAFE.PARSE_DATE）；unit_type/unit_qty 透传
  - tk：available=on_hand_detail_available_quantity / in_transit=in_transit_quantity / unavailable=on_hand_detail_unfulfillable_quantity
  - walmart：available=node_available_units / in_transit=node_inbound_units / unavailable=node_reserved_units；库龄由 node_first_in_stock_date
  - winit：available=usable_qty×unit_qty / in_transit=on_order_qty×unit_qty / unavailable=frozen_qty×unit_qty；unit_type/unit_qty 透传
  - amazon_return 可用（w011/w012）：`WHERE return_other_warehouse IN ('w011','w012') AND out_stock_flag IS NULL AND marketplace <> '美国' AND shipped_quantity > 0`；库龄由 inbound_date
  - amazon_return 在途（w014 虚拟仓）：`return_other_warehouse NOT IN ('w011','w012','w013') AND marketplace <> '美国'`；dim_country_code 由 marketplace 映射 英国→GB/德国→DE/美国→US
  - 每段过滤 `... IS NOT NULL AND DATE(source.synctime) = CURRENT_DATE()`（只取当日批次）
  - **统一维表补维（with_wh）**：`CROSS JOIN latest_synctime`（CURRENT_TIMESTAMP() 统一 synctime，**覆盖各 v2_snap 透传的 source.synctime**，源 synctime 仅保留作参考）；LEFT JOIN dim_product_skus_warehouse（warehouse_id+hicc_sku_code 分组 ANY_VALUE）COALESCE 补 purchased_cost_price/vine_or_not；`stock_amt_cny = stock_qty × unit_qty × 成本`；`sync_date_p = DATE(CURRENT_TIMESTAMP())` 加工当日 UTC 日期
- 关键规则: **库存三态展开的核心实现**（UNNEST + CASE + WHERE IS NOT NULL）；各平台只产出自己拥有的状态；不可售数量在此层落地；age_bucket 统一分桶（0-90/91-180/181-270/271-365/365+）且来源两套：源字段直读（amazon）或 DATE_DIFF 推算（dbeehk/loho/shipout/walmart/amazon_return）

---

#### M. DWS 层

##### dws_inv_global_stock_snap（v1 链路 DWS，供 FineBI）
- 目标表: dws.dws_inv_global_stock_snap（全平台可用+在途汇总）
- 上游: 15 段 UNION ALL，全部引用 DWD **旧链路 _di 加工表**（fba/dbeehk 可用/dbeehk 在途/shipout 在途/shipout 可用/locad/loho 在途/loho 可用/winit org/maple/tk/国内货代/亚马逊退货在途/亚马逊退货可用/walmart）
- 清洗逻辑: 对齐旧表 `dwd_scm_warehouse_available_transit_detail` 业务逻辑：输出 unit_type/unit_qty/Available_Stock_raw_qty/In_transit_Stock_raw_qty；**shipout 在途强制 Available=0、shipout 可用强制 In_transit=0**；walmart 段可用=onhandUnits（非 availableUnits）、在途=inboundUnits；亚马逊退货可用 `return_other_warehouse IN ('w011','w012') AND out_stock_flag IS NULL AND marketplace<>'美国'`、在途 w014 排除 w011/12/13；国内货代 sku 即 hicc_sku；最后 LEFT JOIN pdt_ods.dim_channel/dim_country 补 belong_to_channel_id/belong_to_country_id（**p006/p007/APAC 硬编码 66**）
- 关键规则: **与 v2 链路（global_detail）并行**：global_detail 是"最新批次明细+三态长格式"，本表是"全历史分区+可用/在途宽口径"，两者供不同 FineBI 报表消费；dim_data_source 保留旧表名

##### dws_inv_global_inbound_txn_di
- 目标表: dws.dws_inv_global_inbound_txn_di（全平台入库事务统一口径）
- 上游: 7 段 UNION ALL（amazon/tk/shipout/locad/dbeehk/walmart/winit 各 txn_di）
- 清洗逻辑: 统一列（stock_platform_name/shop_id/shipment_id/shipment_id2/warehouse_id/hicc_sku/shipped_qty/rec_qty/status/create_time/closed_time/receiving_time/expiry_date/warehouse_sku_code/belong_*）；**winit 的 shipment_id=order_no（WI 开头统一）、shipment_id2 保留原始 WYT/OB**；CAST 类型收敛
- 关键规则: 各平台 status 原样透传（未归一），由下游 inbound_shipment_status 归一

##### dws_inv_inbound_shipment_info_di
- 目标表: dws.dws_inv_inbound_shipment_info_di（入库单×运单信息融合）
- 上游: ref dws_inv_global_inbound_txn_di FULL OUTER JOIN ref dwd_scm_shipment_order_extend_di（货代运单，`ROW_NUMBER() OVER (PARTITION BY shipment_id ORDER BY create_time DESC) rn=1` 去重）+ ref dws_scm_shipping_sla_percentile_snap（75 分位时效）+ ref dwd_scm_shipment_track_node_di（轨迹 STRING_AGG）+ static_dim.dim_scm_inbound_close_manual
- 清洗逻辑: **appointment_delivery_date 分五级推算**：已签收取 actual_delivery → expected_delivery（预约派送）→ devanning+7 天 → retrieval+7 天 → 75 分位可靠（is_reliable）用 start_count+ceil(p75_collect2deli_days) → 按运输方式默认时效兜底（普船60/快船35/空运15/铁路45/卡航35/快递10）；**predict_arrival_date 分九级**（actual+7 → expected+7 → ata+22 → atd+config+7/57 → eta+22 → 各运输方式）；actual_delivery/inbound_closed_time 用 dim_scm_inbound_close_manual 人工表 COALESCE 覆盖；track_info 轨迹聚合
- 关键规则: FULL OUTER JOIN 保入库单/运单两侧数据；`(t2.rn=1 OR t2.rn IS NULL)` 防运单重复

---

## 04_ful 履约域

##### dwd_ful_amazon_shipment_di
- 目标表: dwd.dwd_ful_amazon_shipment_di（Amazon 货件履约明细，table）
- 上游: ods.lingxing_amazon_shipment_list + pdt_ods.product_skus_sales
- 清洗逻辑: 全字段透传 + **item_list 数组 `LEFT JOIN UNNEST(JSON_QUERY_ARRAY(main.item_list))` 展开 line_item**：JSON_VALUE 取 msku/fnsku/quantity_shipped 等数值字段（`CAST(JSON_VALUE(...) AS INT64)`）、字符串字段直取（prep_details/prep_instruction/prep_owner/release_date/ware_house_storage_id/sku/asin/prep_labelowner/expiration）；**hicc_sku 子查询**：`product_skus_sales WHERE channel_code='p001' AND data_source IN ('系统自动匹配','手动录入') GROUP BY channel_sku_code 取 MAX(sku_code)`，按 `fnsku = channel_sku_code` 关联（fnsku→HICC SKU）；spu_code/spu_name_en/brand/spu_name_cn/spec_name_cn/spec_name_en 全部 NULL 占位；`etl_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', CURRENT_TIMESTAMP()+8H)` 北京时间
- 关键规则: shipment_plan_list 数组仅转字符串存储不展开（注释明确）；数据源过滤只取系统自动匹配/手动录入的高可信映射

---

## 附录：13 张 v2_snap 表 synctime 处理对照

| v2_snap 表 | synctime 取最新方式 | 备注 |
|---|---|---|
| dwd_inv_amazon_fba_stock_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | 有 updated_at 兜底 |
| dwd_inv_amazon_removal_shipment_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | 手动编写 |
| dwd_inv_chinese_stock_v2_snap | `COALESCE(MAX(synctime), CURRENT_TIMESTAMP())` | **无 updated_at，等价 MAX(synctime) 兜底当前时间** |
| dwd_inv_dbeehk_inbound_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_dbeehk_stock_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_locad_stock_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_loho_inbound_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_loho_stock_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_maple_stock_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_shipout_inbound_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | 手动编写 |
| dwd_inv_tk_fbt_stock_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_walmart_wfs_stock_v2_snap | `COALESCE(MAX(synctime), MAX(updated_at))` | |
| dwd_inv_winit_stock_v2_snap | `MAX(synctime)` | **无 updated_at 字段，仅 MAX(synctime) 不兜底** |
| dwd_inv_global_detail_v2_snap | `CURRENT_TIMESTAMP()`（latest_synctime 全覆盖） | 统一覆盖 13 张表透传的 synctime |

## 附录：链路关系小结
- **v2 链路**：ODS → 13×`*_v2_snap`（干净 ODS，最新批次 + 跨平台 dim_* 列）→ `dwd_inv_global_detail_v2_snap`（三态长格式统一口径 + 维表补价）→ 供 v2 侧 FineBI/明细消费。
- **v1 链路**：ODS → `*_snap`（增量分区快照）→ `*_di`（加工：SKU 映射+采购价+金额）→ `dws_inv_global_stock_snap`（可用/在途宽口径）→ 供 FineBI（旧报表）。
- **入库事务链路**：各平台 `*_inbound_txn_di` → `dws_inv_global_inbound_txn_di` → `dws_inv_inbound_shipment_info_di`（融合货代运单/时效/轨迹）→ `dwd_inv_inbound_shipment_status_di`（在途状态总览，反向挂在 dws 目录）。
