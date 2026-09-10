---
name: hicc-dw
label: HICC数据仓库代码知识库
description: |
  HICC PET 数据仓库（dbt 项目 hicc_data_platform + FineBI 定义 finebi_dev）权威参考。
  基于 Google BigQuery，9 大业务域（交易/广告/商品/履约/库存/退货/财务/采购/主数据），
  遵循 DIM→DWD→DWS 分层架构。当用户询问数仓表结构、字段定义、指标口径、
  数据血缘（某表的上游/下游）、清洗逻辑与清洗规则、SQL 加工逻辑、ETL 链路、
  BigQuery 查询，或询问 FineBI 中某个指标用了什么表什么字段时使用此技能。
  本技能是数仓开发和指标开发的权威参考。
---

# HICC PET 数据仓库代码知识库

## 使用原则

1. **遇到表名、字段名、指标口径、血缘、清洗逻辑问题时，必须先查此技能**
2. 按问题域加载对应 reference 文件，跨域问题并行加载
3. 所有字段名、表名、血缘关系以本技能记录为准，不得凭记忆推断
4. 指标计算必须引用本技能中记录的计算公式/字段引用，不得自行推导
5. 物理表名 = dbt 模型名，位于 `hiccpet-481303.{dim|dwd|dws}.{模型名}`

## 快速导航

### ① 数据血缘（上游/下游）

| 问题类型 | 读取文件 | 典型问法 |
|---------|---------|---------|
| 某模型的上游来源、下游被谁引用 | references/lineage.md | "dwd_inv_global_detail_v2_snap 的上游是哪些表"、"谁引用了 dim_exchange_rates" |
| 全量表清单、执行链路 | references/architecture.md | "数仓有几层"、"执行顺序" |

> `lineage.md` 覆盖全部 153 个模型（含 165 个 source 节点），按 9 大域分层分组，每条含目标表/物化方式/上游/下游/说明。

### ② 清洗逻辑与清洗规则（按业务域）

| 业务域 | 读取文件 | 典型问法 |
|--------|---------|---------|
| 销售(01_trd) + 退货(06_voc) + 商品(03_prd) | references/cleaning-sales.md | "销售额怎么算"、"Amazon 订单怎么清洗"、"退货金额怎么修正" |
| 库存(05_inv) + 履约(04_ful) | references/cleaning-inventory.md | "库存表怎么清洗"、"v2_snap 怎么取 synctime"、"FBA怎么处理" |
| 广告(02_mkt) + 财务(07_fnc) + 采购(08_scm) | references/cleaning-marketing.md | "广告费怎么分摊"、"采购单怎么算金额"、"物流轨迹怎么解析" |
| 主数据维表(09_mdm) | references/cleaning-mdm.md | "SKU怎么映射"、"汇率表结构"、"维表怎么去重" |

> 每个文件含：**通用清洗规则**（该域所有表共用的模式）+ **各表清洗逻辑**（目标表/上游/清洗逻辑/关键规则 四要素）。

### ③ FineBI 指标 → 表 → 字段映射

| 问题类型 | 读取文件 | 典型问法 |
|---------|---------|---------|
| 某个 FineBI 指标用了什么表、什么字段 | references/finebi.md | "采购待生产数量用了哪个表哪个字段"、"ToC销售额怎么定义的" |
| 某个模型关联了哪些维度表 | references/finebi.md | "领星采购单模型关联了哪些维表" |
| FineBI 表与物理表对应关系 | references/finebi.md | "FBA明细数据对应哪张物理表" |

> `finebi.md` 覆盖 95 个指标：每个指标含表达式（表.字段）、聚合方式、口径描述（口径/单位/数据来源）、所属模型；另有 23 个模型的 base_table + 关联维表结构。

### ④ 代码文件索引

| 问题类型 | 读取文件 | 典型问法 |
|---------|---------|---------|
| 查某个模型 SQL 文件路径 | references/file-index.md | "dwd_inv_amazon_fba_stock_v2_snap.sql 在哪" |
| 查某个域目录有哪些模型 | references/file-index.md | "05_inv 有哪些 dwd 模型" |
| 查看完整模型清单 | references/file-index.md | "列出所有模型" |

> GitHub 文件直链格式: `https://github.com/HiccTech/hicc_dw_script/blob/main/hicc_data_platform/models/{目录}/{文件名}`

## 项目概览

- **项目名称**: HICC PET 数据仓库 (hicc_dw_script)
- **数仓工程**: `hicc_data_platform/`（dbt，9 大域 153 模型）
- **BI 语义层**: `finebi_dev/`（FineBI 7.0 BI-as-Code，95 指标定义）
- **数据平台**: Google BigQuery | **项目ID**: hiccpet-481303
- **仓库**: HiccTech/hicc_dw_script (私有)

## 数据分层架构

```
┌───────────────────────────────────────────────────────────────┐
│  DIM 维度层 (dim dataset, 09_mdm 主数据 + 各域 dim 维表)       │
│  dim_product_skus_warehouse, dim_exchange_rates, ...          │
├───────────────────────────────────────────────────────────────┤
│  DWD 明细层 (dwd dataset, 9 域 dwd 子目录)                     │
│  01_trd 02_mkt 03_prd 04_ful 05_inv 06_voc 07_fnc 08_scm      │
├───────────────────────────────────────────────────────────────┤
│  DWS 汇总层 (dws dataset, 各域 dws 子目录, 供 FineBI 建模)     │
└───────────────────────────────────────────────────────────────┘
```

## 执行链路

```
DTS 同步 (MySQL → ods) → dbt build: dim 维表 → dwd 明细 → dws 汇总 → FineBI/WarDyn
```

## 回答规范

1. 涉及表名时，使用完整 BigQuery 路径: `project.dataset.table`（或 dbt 模型名）
2. 涉及金额时，注明币种（USD/CNY/HKD/原币）
3. 涉及日期时，注明字段名和时区假设（UTC 基准 / 北京时间 +8h）
4. 涉及指标时，给出完整计算公式或字段引用，并注明 FineBI 定义来源
5. 涉及清洗时，先给该域通用清洗规则，再给目标表的具体清洗逻辑
6. 涉及血缘时，给出上游来源（ods source / ref 模型）与下游引用者
7. 不确定的字段或逻辑，明确标注"待确认"并建议查验方式
