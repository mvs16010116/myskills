# 数据分层架构（dbt 项目：hicc_data_platform）

> 项目目录：`hicc_data_platform/` | dbt 项目名：`hicc_data_platform` | profile：`hicc_data_platform`
> 数据平台：Google BigQuery | 项目 ID：`hiccpet-481303`
> 依赖：Airflow 调度（DTS 同步 MySQL→ODS，dbt 构建 dim/dwd/dws）

## 分层与数据集（Dataset 路由）

dbt `dbt_project.yml` 将 9 大业务域的子目录路由到 BigQuery Dataset：

| 层 | Dataset | 说明 |
|----|---------|------|
| DIM 维度层 | `dim` | 主数据维表（09_mdm 全部 + 各域 dim/ 子目录） |
| DWD 明细层 | `dwd` | 明细事实/快照（各域 dwd/ 子目录） |
| DWS 汇总层 | `dws` | 汇总/集市（各域 dws/ 子目录，供 FineBI 建模） |

> 模型物化：全局默认 `table`；`_snap` 结尾模型为 `incremental`（insert_overwrite，按 fdate_p/synctime 分区）。

## 9 大业务域（models/ 目录结构）

| 域目录 | 业务域 | 层 | 说明 |
|--------|--------|-----|------|
| `01_trd` | 交易与销售 | dwd/dws | 2C(Amazon/Walmart/Shopify/Shopee/Lazada/TikTok/HKTVmall) + 2B(SPS) 订单行项明细 |
| `02_mkt` | 营销与广告 | dim/dwd/dws | Amazon(SB/SD/SP)、Chewy、Petco、Shopee、Lazada、TikTok、Walmart、Shopify GA4 广告花费/表现 |
| `03_prd` | 产品与商品 | dim/dwd | 平台商品主数据、亚马逊 Listing 表现 |
| `04_ful` | 履约与交付 | dwd | 亚马逊货件 |
| `05_inv` | 库存与周转 | dim/dwd/dws | FBA/中国仓/海外仓(dbcehk/locad/loho/maple/shipout/tk/walmart/winit) 库存快照，含 v2 快照链路 |
| `06_voc` | 客户与体验(退货) | dwd/dws | 各渠道退货明细 + 全局退货汇总 |
| `07_fnc` | 财务与核算 | dwd/dws | Chewy rebate、QuickBooks 发票、Ezzeship 物流费、科目费用 |
| `08_scm` | 采购与供应 | dim/dwd/dws | 领星采购单、SPS PO、发货/物流轨迹、Shipout 出库账单 |
| `09_mdm` | 主数据与维度 | dim | 商品 SKU 主数据、SKU 映射、汇率、日历、渠道/国家/店铺/仓库 |

## 数据源（sources.yml）

dbt source 声明（模型引用一律用 `{{ source() }}` / `{{ ref() }}`，禁止硬编码全限定表名）：

| source 名 | dataset | 说明 |
|-----------|---------|------|
| `ods` | `ods` | 原始业务表（DTS 从 MySQL 同步 + 采集 API），**默认 freshness 检查：warn 12h / error 24h** |
| `pdt_ods` | `pdt_ods` | 数仓侧主数据源表（product_skus*、dim_channel/country 等） |
| `static_dim` | `dim` | 静态维表（dim_date、petco creative mapping、shipment exclusive 等手工/静态配置） |

**freshness 排除项**：手工导入表（`import_*`）、静态表（`bundle_info`、`chewy_promoted_products` 等已停采表）配置 `freshness: null` 跳过检查。

## 执行链路（Airflow 调度）

```
DTS 同步 (MySQL → ODS)  →  dbt build:
  dim 维表 (09_mdm → 各域 dim)
  → dwd 明细 (依赖 dim + ods)
  → dws 汇总 (依赖 dwd)
  → 供 FineBI / WarDyn 使用
```

- **morning_full DAG**：全量执行 dim→dwd→dws
- **afternoon_partial DAG**：增量执行 high 频率源
- 完整链路与 DAG 编排见 Airflow 开发规范（`airflow/dags`）

## 关键设计约定

- **命名**：`{层}_{域缩写}_{业务对象}_{物化后缀}`，如 `dwd_trd_toc_amazon_order_item_di`（_di=日增量表，_snap=快照表）
- **SKU 归一**：`dim_product_skus_sales`（销售）、`dim_product_skus_warehouse`（库存，仓×渠道SKU×HICC SKU 唯一核心）、`dim_hicc_sku_mapping_v2`（新统一映射，L1 官方→L2 regex→L3 待治理）
- **汇率**：`dim_exchange_rates`（月度汇率，to_usd_rate，真实工作日 + 本月模拟）
- **时间**：UTC 基准（`event_time_utc` 唯一真相源，`event_date_utc` 推荐分区），`etl_time` = 北京时间 `CURRENT_TIMESTAMP()+8h`
- **dbt 规范**：`{{ source('ods','表名') }}` 引用 ODS，`{{ ref('模型名') }}` 引用 dim/dwd/dws 模型

## 参考文档导航

- 全模型血缘：`lineage.md`（153 个模型的上游/下游依赖）
- 各域清洗逻辑与规则：`cleaning-sales.md` / `cleaning-inventory.md` / `cleaning-marketing.md` / `cleaning-mdm.md`
- FineBI 指标→表→字段映射：`finebi.md`
- 模型代码文件索引：`file-index.md`
