---
name: hicc-dw
label: HICC数据仓库代码知识库
description: |
  HICC PET 数据仓库 SQL 代码知识库（GitHub: HiccTech/hicc_dw_script）。
  基于 Google BigQuery，覆盖销售、广告、库存、财务、退货五大业务域，
  遵循 DIM→DWD→DWS 分层架构。当用户询问数仓表结构、字段定义、
  指标口径、SQL 加工逻辑、ETL 链路、BigQuery 查询时使用此技能。
  本技能是数仓开发和指标开发的权威参考。
---

# HICC PET 数据仓库代码知识库

## 使用原则

1. **遇到表名、字段名、指标口径问题时，必须先查此技能**
2. 按问题域加载对应 reference 文件，跨域问题并行加载
3. 所有字段名、表名以本技能记录为准，不得凭记忆推断
4. 指标计算必须引用本技能中记录的计算公式，不得自行推导

## 快速导航

### 业务域参考

| 问题类型 | 读取文件 | 典型问法 |
|---------|---------|---------|
| 数据分层、执行链路、全量表清单 | references/architecture.md | "数仓有几层"、"执行顺序" |
| 维度表、SKU映射、汇率、商品主数据、分类 | references/dim.md | "SKU怎么映射"、"汇率表结构" |
| 销售数据、2C/2B、各渠道、销售额指标 | references/sales.md | "销售额怎么算"、"2C有哪些渠道" |
| 广告数据、投放、费用分摊、campaign | references/ads.md | "广告费怎么分摊" |
| 库存数据、快照、FBA物流、预测 | references/inventory.md | "库存表结构"、"FBA怎么处理" |
| 财务数据、汇率换算、状态标签 | references/finance.md | "财务汇总表"、"汇率精度" |
| 退货数据、金额修正、日期修正 | references/returns.md | "退货金额怎么修正" |

### 代码文件索引

| 问题类型 | 读取文件 | 典型问法 |
|---------|---------|---------|
| 查某个 SQL 文件的 GitHub 路径 | references/file-index.md | "dim_exchange_rate.sql 在哪" |
| 查某个目录下有哪些 SQL 文件 | references/file-index.md | "销售dwd_2C 目录有哪些文件" |
| 查看完整代码文件清单 | references/file-index.md | "列出所有 SQL 文件" |

> **GitHub 文件直链格式**: `https://github.com/HiccTech/hicc_dw_script/blob/main/{目录}/{文件名}`

## 项目概览

- **项目名称**: HICC PET 数据仓库 (hicc_dw_script)
- **数据平台**: Google BigQuery
- **项目ID**: hiccpet-481303
- **仓库**: HiccTech/hicc_dw_script (私有)
- **提交数**: 103 commits
- **语言**: Python 93.4%, Shell 4.4%, Dockerfile 2.2%
- **贡献者**: rankhicc, LOGAN-HICCPET, Dannyhiccpet

## 数据分层架构

```
┌─────────────────────────────────────────────────────────┐
│  DIM 维度层 (16 个 SQL 文件)                              │
│  dim.dim_exchange_rates, dim.dim_product_skus, ...       │
├─────────────────────────────────────────────────────────┤
│  DWD 明细层 (8 个目录)                                    │
│  销售dwd_2C │ 销售dwd_2B │ 广告dwd │ 库存dwd │ 库存dwd_快照 │
│  库存预测dwd │ 财务dwd │ 退货dwd                          │
├─────────────────────────────────────────────────────────┤
│  DWS 汇总层 (6 个目录)                                    │
│  销售dws │ 广告dws │ 广告dws_分摊 │ 库存dws │ 财务dws │ 退货dws │
└─────────────────────────────────────────────────────────┘
```

## 执行链路

```
dim_维度 → 销售dwd_2C → 广告dwd → 广告dws_分摊 → 广告dws
       → 销售dwd_2B → 销售dws → 退货dwd → 退货dws
       → 库存dwd_快照 → 库存dwd → 库存dws → 财务dwd → 财务dws
       → 数据同步bq2wardyn → dw_endflag
```

## 回答规范

1. 涉及表名时，使用完整 BigQuery 路径: `project.dataset.table`
2. 涉及金额时，注明币种（USD/HKD/原币）
3. 涉及日期时，注明字段名和时区假设
4. 涉及指标时，给出完整计算公式
5. 不确定的字段或逻辑，明确标注"待确认"并建议查验方式
