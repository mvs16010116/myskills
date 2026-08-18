# 销售域

## 核心指标

### 总销售额 (Total Sales)

```
总销售额 = 2C销售额 + 2B销售额
```

### 2C 销售额

```
2C销售额 = SUM(quantity_ordered × item_price_amount_usd)
         WHERE cancel_date IS NULL OR cancel_date >= 统计截止日期
```

**关键**: 需要排除已取消订单（`cancel_date` 在统计周期内的订单不计入）

### 2B 销售额

```
2B销售额 = SUM(tot_amt_usd)
```

## 表结构

### dws.dws_ord_shop_channel_sku_orders — 2C 销售汇总表

**DWS 汇总层，最重要的销售指标表。覆盖 8 个渠道。**

**文件**: `销售dws/dws_ord_shop_channel_sku_orders.sql`

**已知字段**:

| 字段 | 类型 | 说明 |
|------|------|------|
| fdate | DATE | 订单日期 |
| shop_channel | STRING | 店铺渠道（Amazon/Walmart/Shopify/Shopee/Lazada/TikTok/HKTVmall/ShowRoom） |
| channel_sku_code | STRING | 渠道 SKU 编码 |
| quantity_ordered | INT64 | 订购数量 |
| item_price_amount_usd | FLOAT64 | 单价（美元） |
| cancel_date | DATE | 取消日期（NULL=未取消） |

**2C 渠道覆盖**:
| 序号 | 渠道 | 平台 |
|------|------|------|
| 1 | Amazon | 亚马逊 |
| 2 | Walmart | 沃尔玛 |
| 3 | Shopify | Shopify独立站 |
| 4 | Shopee | Shopee |
| 5 | Lazada | Lazada |
| 6 | TikTok | TikTok Shop |
| 7 | HKTVmall | HKTVmall |
| 8 | ShowRoom | 展厅 |

### dwd.dwd_sps_import_b2b_channel_import_po — 2B 销售汇总表

**⚠️ 命名前缀为 dwd 但实际是汇总层，直接从 ODS 聚合。**

**文件**: `销售dwd_2B/dwd_sps_import_b2b_channel_import_po.sql` (64行, 1.89KB)

**表结构**:

| 字段 | 类型 | 说明 |
|------|------|------|
| fdate | DATE | 订单日期 |
| vendor_code | STRING | 供应商编码 |
| channel_sku_code | STRING | 渠道 SKU 编码 |
| purchase_quantity | INT64 | 采购数量 |
| tot_amt_usd | FLOAT64 | 总金额（美元，已换算） |
| currency_code | STRING | 原始币种 |

**数据来源（4路 UNION ALL）**:
1. **HK PO 主表**: `ods.import_b2b_channel_hk_po_main`
   - 金额换算: `total_amount_hkd × er.to_usd_rate`
   - 关联供应商: `ods.import_dim_sps_vendor`
2. **SG PO**: `ods.import_b2b_channel_sg_po`
   - 金额换算: `tot_amt × er.to_usd_rate`
3. **HK 2月手工数据**: `ods.import_sps_hk_20260331_154520`
4. **HK 3月手工数据**: `ods.import_sps_hk_20260410_185955`

**汇率关联**: 所有 PO 均通过 `dim.dim_exchange_rates` 按月关联汇率换算为 USD。

### dwd.dwd_sps_order_detail — 2B 销售明细表

**文件**: `销售dwd_2B/dwd_sps_order_detail.sql`

SPS 渠道的 2B 订单明细，包含特定 SKU 的数量计算逻辑修正。

## 销售域指标查询示例

### 月度总销售额

```sql
WITH sales_2c AS (
    SELECT SUM(quantity_ordered * item_price_amount_usd) AS total_sales_2c_usd
    FROM `hiccpet-481303.dws.dws_ord_shop_channel_sku_orders`
    WHERE fdate >= '2026-06-01' AND fdate < '2026-07-01'
      AND (cancel_date IS NULL OR cancel_date >= '2026-07-01')
),
sales_2b AS (
    SELECT SUM(tot_amt_usd) AS total_sales_2b_usd
    FROM `hiccpet-481303.dwd.dwd_sps_import_b2b_channel_import_po`
    WHERE fdate >= '2026-06-01' AND fdate < '2026-07-01'
)
SELECT
    ROUND(total_sales_2c_usd, 2) AS sales_2c_usd,
    ROUND(total_sales_2b_usd, 2) AS sales_2b_usd,
    ROUND(total_sales_2c_usd + total_sales_2b_usd, 2) AS sales_total_usd
FROM sales_2c, sales_2b;
```

### 按渠道销售额

```sql
SELECT
    shop_channel,
    ROUND(SUM(quantity_ordered * item_price_amount_usd), 2) AS sales_usd
FROM `hiccpet-481303.dws.dws_ord_shop_channel_sku_orders`
WHERE fdate >= '2026-06-01' AND fdate < '2026-07-01'
  AND (cancel_date IS NULL OR cancel_date >= '2026-07-01')
GROUP BY shop_channel
ORDER BY sales_usd DESC;
```

## 注意事项

1. **2C 取消订单**: `cancel_date` 在统计周期内的订单不计入销售
2. **2B 汇总表**: 2B 的 DWS 汇总表实际存储在 `dwd` 数据集下（命名历史原因）
3. **货币**: 所有金额字段均为 USD
4. **2B 手工数据**: HK 的 2月/3月数据使用手工导入的 ODS 表，非实时接口
5. **2B 的 `Qty_Ordered`**: SPS 明细表中此字段有特定 SKU 修正逻辑

## 代码文件

> 完整路径见 `references/file-index.md`

| 文件名 | GitHub 路径 |
|--------|-------------|
| dwd_ord_hktvmall_order_details.sql | `销售dwd_2C/dwd_ord_hktvmall_order_details.sql` |
| dwd_ord_lazada_order_items.sql | `销售dwd_2C/dwd_ord_lazada_order_items.sql` |
| dwd_ord_lingxing_amazon_api_order_detail_i.sql | `销售dwd_2C/dwd_ord_lingxing_amazon_api_order_detail_i.sql` |
| dwd_ord_lingxing_amazon_shipment_list.sql | `销售dwd_2C/dwd_ord_lingxing_amazon_shipment_list.sql` |
| dwd_ord_shopee_order_detail.sql | `销售dwd_2C/dwd_ord_shopee_order_detail.sql` |
| dwd_ord_tk_order_details.sql | `销售dwd_2C/dwd_ord_tk_order_details.sql` |
| dwd_ord_walmart_order_detail.sql | `销售dwd_2C/dwd_ord_walmart_order_detail.sql` |
| 订单明细dwd_ord_shopify_order_line_items.sql | `销售dwd_2C/订单明细dwd_ord_shopify_order_line_items.sql` |
| dwd_sps_import_b2b_channel_import_po.sql | `销售dwd_2B/dwd_sps_import_b2b_channel_import_po.sql` |
| dwd_sps_order_detail.sql | `销售dwd_2B/dwd_sps_order_detail.sql` |
| dws_ord_shop_channel_sku_orders.sql | `销售dws/dws_ord_shop_channel_sku_orders.sql` |
