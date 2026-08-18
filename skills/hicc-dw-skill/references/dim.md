# 维度层 (dim_维度)

## 核心维度表详解

### 1. dim.dim_exchange_rates — 汇率维度表

**最重要维度表之一，所有跨币种金额计算的基础。**

**文件**: `dim_exchange_rate.sql` (138行, 3.36KB)

**表结构**:

| 字段 | 类型 | 说明 |
|------|------|------|
| fdate | DATE | 汇率月份（DATE_TRUNC到月，如 2026-06-01） |
| currency_cn | STRING | 货币中文名 |
| from_currency | STRING | 货币代码（USD/EUR/JPY/HKD/GBP/AUD/NZD/SGD/CHF/CAD） |
| to_usd_rate | FLOAT64 | 1单位外币 = ?美元（精度10位小数） |
| rate | FLOAT64 | 源表原始汇率 |
| data_source | STRING | 数据来源：'外汇官方数据' / '上周期外汇官方数据' |

**汇率计算逻辑**:

```
范围1（直接报价货币: USD/EUR/JPY/HKD/GBP/AUD/NZD/SGD/CHF/CAD）:
  to_usd_rate = ROUND(rate / usd_rate_value, 10)

范围2（间接报价货币，其他所有货币）:
  to_usd_rate = ROUND(10000.0 / (rate * usd_rate_value), 10)
```

**本月模拟机制**:
- 当本月无工作日汇率数据时，自动使用最近一个工作日的汇率模拟当月汇率
- 模拟数据标记为 `data_source = '上周期外汇官方数据'`
- 模拟数据 `is_first_work_date = 0`（非真实工作日）

**使用方式**:
```sql
-- 标准关联（月度汇率）
LEFT JOIN dim.dim_exchange_rates AS er
  ON er.from_currency = source.currency_code
  AND er.fdate = DATE_TRUNC(source.order_date, MONTH)
```

**支持的货币**: USD, EUR, JPY, HKD, GBP, AUD, NZD, SGD, CHF, CAD 及其他

### 2. dim.dim_product_skus — 商品SKU信息

**文件**: `获取主数据商品信息表_dim_product_skus.sql`

包含商品主数据信息，支持分类层级。是所有业务域关联商品信息的基础维度表。

### 3. dim.dim_sku_mapping — SKU映射表

**文件**: `dim_sku_mapping.sql`

SKU 编码映射关系，用于跨系统 SKU 对齐。

### 4. dim.dim_warehouse_sku_mapping — 仓库SKU映射

**文件**: `dim_warehouse_sku_mapping.sql`

仓库维度的 SKU 映射，用于库存域。

### 5. dim.dim_product_skus_sales — 销售产品SKU映射

**文件**: `获取主数据mapping表销售_dim_product_skus_sales.sql`

销售域专用的产品 SKU 映射表。

### 6. dim.dim_product_skus_warehouse — 库存产品SKU仓库映射

**文件**: `获取主数据mapping表库存_dim_product_skus_warehouse.sql`

库存域专用的产品 SKU 仓库映射表。

### 7. dim.dim_product_skus_purchase — 商品采购信息

**文件**: `获取主数据商品采购信息dim_product_skus_purchase.sql`

包含渠道和地区字段，用于采购分析。

### 8. dim.dim_product_category — 商品分类层级

**文件**: `获取主数据商品分类层级加工.sql`

商品分类层级加工，支持多级分类。

### 9. dim.dim_campaign — 广告活动维度

**文件**: `dim_campaign.sql`

广告活动（campaign）维度信息。

### 10. dim.dim_amazon_account — 亚马逊账户列表

**文件**: `亚马逊account_list.sql`（最新更新: 2026-07-05）

亚马逊账户维度表，用于广告报表账户关联。

### 11-16. 其他维度表

| 文件 | 说明 |
|------|------|
| dim_import_sku_mapping | 销售导入 SKU 映射 |
| dim_shipout_product | 发货产品维度 |
| dim_lingxing_amazon_product_info | 领星产品维度 |
| dim_pur_lingxing_amazon_supplier | 领星亚马逊供应商 |
| dim_lingxing_sb_campaign | 领星 SB 广告配置 |
| 手工表导入商品主数据import_sku_info | 手工导入商品主数据（含分类字段、来源优先级） |

## SKU 映射体系

存在三套 SKU 映射：
1. **销售映射**: dim_product_skus_sales — 销售域使用
2. **仓库映射**: dim_product_skus_warehouse — 库存域使用
3. **导入映射**: dim_import_sku_mapping — 数据导入时使用

## 多数据源

- **领星 (LingXing)**: 亚马逊供应商、产品、SB广告配置
- **手工导入**: 商品主数据（含分类字段）
- **主数据系统**: 商品SKU、分类层级、采购信息
- **外汇官方数据**: 汇率数据

## 代码文件

> 完整路径见 `references/file-index.md`

| 文件名 | GitHub 路径 |
|--------|-------------|
| dim_campaign.sql | `dim_维度/dim_campaign.sql` |
| dim_exchange_rate.sql | `dim_维度/dim_exchange_rate.sql` |
| dim_pur_lingxing_amazon_supplier.sql | `dim_维度/dim_pur_lingxing_amazon_supplier.sql` |
| dim_shipout_product.sql | `dim_维度/dim_shipout_product.sql` |
| dim_sku_mapping.sql | `dim_维度/dim_sku_mapping.sql` |
| dim_warehouse_sku_mapping.sql | `dim_维度/dim_warehouse_sku_mapping.sql` |
| mapping表销售_dim_import_sku_mapping.sql | `dim_维度/mapping表销售_dim_import_sku_mapping.sql` |
| 亚马逊account_list.sql | `dim_维度/亚马逊account_list.sql` |
| 手工表导入商品主数据import_sku_info.sql | `dim_维度/手工表导入商品主数据import_sku_info.sql` |
| 获取主数据mapping表库存_dim_product_skus_warehouse.sql | `dim_维度/获取主数据mapping表库存_dim_product_skus_warehouse.sql` |
| 获取主数据mapping表销售_dim_product_skus_sales.sql | `dim_维度/获取主数据mapping表销售_dim_product_skus_sales.sql` |
| 获取主数据商品信息表_dim_product_skus.sql | `dim_维度/获取主数据商品信息表_dim_product_skus.sql` |
| 获取主数据商品分类层级加工.sql | `dim_维度/获取主数据商品分类层级加工.sql` |
| 获取主数据商品采购信息dim_product_skus_purchase.sql | `dim_维度/获取主数据商品采购信息dim_product_skus_purchase.sql` |
| 领星sb_campaign配置.sql | `dim_维度/领星sb_campaign配置.sql` |
| 领星采购信息表dim_lingxing_amazon_product_info.sql | `dim_维度/领星采购信息表dim_lingxing_amazon_product_info.sql` |
