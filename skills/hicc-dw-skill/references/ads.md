# 广告域

## 模块结构

| 目录 | 层级 | BigQuery 数据集 | 说明 |
|------|------|----------------|------|
| 广告dwd | DWD | dwd | 广告投放明细 |
| 广告dws | DWS | dws | 广告汇总 |
| 广告dws_分摊 | DWS | dws | 广告费用分摊汇总 |

## 关键特性

- **多渠道广告**: 支持 SB 广告（Sponsored Brands）、领星 campaign 配置
- **费用分摊**: 独立广告费用分摊汇总层，将广告费用按一定规则分摊到 SKU/订单
- **账户维度**: 使用亚马逊 account_list 维度表关联广告账户
- **多店铺**: 支持 Walmart 多店铺广告数据（最新重构）

## 执行顺序

```
dim_维度 → 销售dwd_2C → 广告dwd → 广告dws_分摊 → 广告dws
```

广告域依赖销售dwd_2C先执行，因为广告费用分摊需要用到销售数据。

## 维度依赖

| 维度表 | 用途 |
|--------|------|
| dim.dim_campaign | 广告活动维度 |
| dim.dim_amazon_account | 亚马逊账户列表 |
| dim.dim_lingxing_sb_campaign | 领星 SB 广告配置 |

## 最近变更

- 2026-07-05: 重构广告报表查询以使用新的账户维度表
- 2026-06-29: 新增退货和广告数据表，优化现有SQL逻辑
- 2026-06-23: 支持多店铺Walmart数据，重构广告报表并新增退货表

## 代码文件

> 完整路径见 `references/file-index.md`

| 文件名 | GitHub 路径 |
|--------|-------------|
| dwd_ads_campaign_product_performance.sql | `广告dwd/dwd_ads_campaign_product_performance.sql` |
| dwd_ads_chewy_campaign_sidebar.sql | `广告dwd/dwd_ads_chewy_campaign_sidebar.sql` |
| dwd_ads_chewy_spend.sql | `广告dwd/dwd_ads_chewy_spend.sql` |
| dwd_ads_petco_spend.sql | `广告dwd/dwd_ads_petco_spend.sql` |
| dwd_ads_tk_product_item_group_reports.sql | `广告dwd/dwd_ads_tk_product_item_group_reports.sql` |
| dwd_ads_walmart_compaign_item_performance.sql | `广告dwd/dwd_ads_walmart_compaign_item_performance.sql` |
| dwd_lazada_adgroup_report_广告.sql | `广告dwd/dwd_lazada_adgroup_report_广告.sql` |
| dwd_shopee_campaign_daily_performance_广告.sql | `广告dwd/dwd_shopee_campaign_daily_performance_广告.sql` |
| shopify广告dwd_ads_shopify_ga4_ad_spend.sql | `广告dwd/shopify广告dwd_ads_shopify_ga4_ad_spend.sql` |
| 亚马逊订单dwd_lingxing_order_profit_msku.sql | `广告dwd/亚马逊订单dwd_lingxing_order_profit_msku.sql` |
| 关键词表现明细表dwd_ads_keyword_performance.sql | `广告dwd/关键词表现明细表dwd_ads_keyword_performance.sql` |
