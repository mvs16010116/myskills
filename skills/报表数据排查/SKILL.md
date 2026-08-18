---
name: "报表数据排查"
description: "排查Excel报表指标与数据仓库的映射关系，验证报表数据准确性。当用户要求验证Excel报表/看板数据与数据库的一致性时调用。"
---

# 报表数据排查 Skill

排查 Excel 报表/看板指标与数据仓库（BigQuery）的映射关系，验证报表数据准确性。记录已验证的报表指标-库表字段映射关系和校验流程，用于快速排查报表数据问题。

---

## 一、适用场景

- 用户提供 Excel 报表（如库存看板、销售报表等），要求验证数据是否准确
- 需要排查报表中某个指标（如"在途库存数量"）对应数据库中哪个表、哪个字段
- 报表数据与数据库数据存在差异，需要定位差异原因
- 新报表上线前需要进行数据一致性校验

---

## 二、通用校验流程

```
Step 1: 理解报表结构     → 查看Sheet名称、列名、合计行
Step 2: 定位数据源        → 根据业务语义找到对应数据库表/字段
Step 3: 汇总值对比        → 按维度（日期、仓库、渠道等）对比总数
Step 4: 明细级对比        → 按SKU/商品维度逐行对比
Step 5: 关系验证          → 验证Sheet间勾稽关系（如 Sheet3 = Sheet1 + Sheet2）
Step 6: 输出报告          → 结构化报告，标注匹配/不匹配项及原因
```

---

## 三、库存报表指标映射关系（已验证）

以下为 `供应链库存数据看板.xlsx` 已验证的指标映射关系，核心数据源为 `dwd_scm_warehouse_available_transit_detail` 表。

### 3.1 数据源表

| 表名 | 说明 | 分区字段 |
|------|------|----------|
| `dwd.dwd_scm_warehouse_available_transit_detail` | 海外仓库存在途/在库明细表，按天分区 | `fdate_p`（格式：YYYY-MM-DD） |
| `dim.dim_product_skus_warehouse` | 仓库-SKU映射表，关联仓库名称 | `warehouse_id` |

### 3.2 核心字段映射

| Excel 报表指标 | BQ 字段 | 聚合方式 | 状态 |
|:---:|:---:|:---:|:---:|
| 在途库存数量 | `In_transit_Stock_qty` | `SUM()` | ✅ 已验证 |
| 在途库存金额 | `In_transit_Stock_cny` | `SUM()` | ✅ 已验证 |
| 在库库存数量 | `Available_Stock_qty` | `SUM()` | ✅ 已验证 |
| 在库库存金额 | `Available_Stock_cny` | `SUM()` | ✅ 已验证 |
| 总数量 | 在途+在库数量之和 | `SUM(In_transit_Stock_qty) + SUM(Available_Stock_qty)` | ✅ 已验证 |
| 总金额 | 在途+在库金额之和 | `SUM(In_transit_Stock_cny) + SUM(Available_Stock_cny)` | ✅ 已验证 |

### 3.3 过滤条件映射

| Excel Sheet | 筛选口径 | BQ 过滤条件 |
|:---:|:---|:---|
| 海外库存（效期维度） | 全部海外库存（排除绿标） | `(vine_or_not IS NULL OR vine_or_not != 'vine')` |
| 不含绿标以及临期库存 | 排除绿标 + 排除临期（效期≥3个月） | 上方条件 + `AND (expiry_date IS NULL OR expiry_date >= DATE_ADD(CURRENT_DATE(), INTERVAL 3 MONTH))` |
| 临期库存 | 效期<3个月或已过期 | `expiry_date IS NOT NULL AND expiry_date < DATE_ADD(CURRENT_DATE(), INTERVAL 3 MONTH)` |
| 仪表板-海外在途 | 汇总看板，数量单位K（千） | 同"效期维度"口径，金额/数量 × 1000 |
| 仪表板-海外在库 | 汇总看板，数量单位K（千） | 同"效期维度"口径，金额/数量 × 1000 |

### 3.4 仪表板汇总 Sheet 特殊说明

- **单位**：仪表板汇总 Sheet（海外在途/海外在库）的数据列名带 `(K)` 后缀，表示千单位
- **换算**：读取时需将数值 × 1000 得到实际值
- **已验证**：仪表板汇总数据与 BQ 完全匹配 ✅

### 3.5 仓库维度映射

| 仓库字段 | 关联表 | 关联字段 |
|:---:|:---:|:---:|
| `dim_warehouse_id` | `dim.dim_product_skus_warehouse` | `warehouse_id` |
| `warehouse_name` | `dim.dim_product_skus_warehouse` | `warehouse_name` |
| `belong_to_channel_code` | 直接字段（主表） | - |
| `belong_to_country_code` | 直接字段（主表） | - |

### 3.6 基础查询模板

```sql
-- 全部海外库存（排除绿标）
SELECT 
    ROUND(SUM(In_transit_Stock_qty), 0) AS transit_qty,
    ROUND(SUM(In_transit_Stock_cny), 2) AS transit_cny,
    ROUND(SUM(Available_Stock_qty), 0) AS avail_qty,
    ROUND(SUM(Available_Stock_cny), 2) AS avail_cny
FROM `hiccpet-481303.dwd.dwd_scm_warehouse_available_transit_detail`
WHERE fdate_p = '<数据日期 YYYY-MM-DD>'
  AND (vine_or_not IS NULL OR vine_or_not != 'vine');

-- 排除绿标 + 排除临期（效期 ≥ 3个月）
SELECT 
    ROUND(SUM(In_transit_Stock_qty), 0) AS transit_qty,
    ROUND(SUM(In_transit_Stock_cny), 2) AS transit_cny,
    ROUND(SUM(Available_Stock_qty), 0) AS avail_qty,
    ROUND(SUM(Available_Stock_cny), 2) AS avail_cny
FROM `hiccpet-481303.dwd.dwd_scm_warehouse_available_transit_detail`
WHERE fdate_p = '<数据日期 YYYY-MM-DD>'
  AND (vine_or_not IS NULL OR vine_or_not != 'vine')
  AND (expiry_date IS NULL OR expiry_date >= DATE_ADD('<数据日期 YYYY-MM-DD>', INTERVAL 3 MONTH));

-- 临期库存（效期 < 3个月）
SELECT 
    ROUND(SUM(Available_Stock_qty), 0) AS avail_qty,
    ROUND(SUM(Available_Stock_cny), 2) AS avail_cny
FROM `hiccpet-481303.dwd.dwd_scm_warehouse_available_transit_detail`
WHERE fdate_p = '<数据日期 YYYY-MM-DD>'
  AND expiry_date IS NOT NULL
  AND expiry_date < DATE_ADD('<数据日期 YYYY-MM-DD>', INTERVAL 3 MONTH);

-- 按仓库维度聚合对比
SELECT 
    t.dim_warehouse_id,
    w.warehouse_name,
    t.belong_to_channel_code,
    t.belong_to_country_code,
    ROUND(SUM(t.In_transit_Stock_qty), 0) AS transit_qty,
    ROUND(SUM(t.In_transit_Stock_cny), 2) AS transit_cny,
    ROUND(SUM(t.Available_Stock_qty), 0) AS avail_qty,
    ROUND(SUM(t.Available_Stock_cny), 2) AS avail_cny
FROM `hiccpet-481303.dwd.dwd_scm_warehouse_available_transit_detail` t
LEFT JOIN `hiccpet-481303.dim.dim_product_skus_warehouse` w
    ON t.dim_warehouse_id = w.warehouse_id
WHERE t.fdate_p = '<数据日期 YYYY-MM-DD>'
  AND (t.vine_or_not IS NULL OR t.vine_or_not != 'vine')
GROUP BY t.dim_warehouse_id, w.warehouse_name, t.belong_to_channel_code, t.belong_to_country_code
ORDER BY t.dim_warehouse_id;
```

---

## 四、Sheet 间勾稽关系验证

已验证的库存报表 Sheet 间关系：

```
Sheet3(效期维度) = Sheet1(不含绿标+临期) + Sheet2(临期) + 绿标
```

- 此关系在 Excel 中成立 ✅
- 每个 Sheet 的合计行（日期=合计）可直接用于验证

---

## 五、已知限制（不匹配项）

以下数据在 BQ 中无对应数据源，验证时需注意：

| 库存类型 | 来源 | 说明 |
|:---:|:---:|:---|
| PO未交付库存 | ERP 采购订单 | 未生产/未发货的采购订单，BQ 无此数据 |
| 国内货代库存 | 国内物流在途 | 国内仓库到港前的在途库存，BQ 无此数据 |
| 工厂库存（待产+成品） | ERP 生产计划 | 工厂侧的生产计划库存，BQ 无此数据 |
| 绿标库存 | 口径不一致 | BQ 的 `vine_or_not` 字段与 Excel 的"绿标"分类定义不同 |
| 临期库存（BQ侧） | 数据不完整 | BQ 中 `expiry_date` 字段覆盖率低，临期识别不完整 |

---

## 六、Python 校验脚本模板

```python
import pandas as pd
import json

EXCEL_PATH = 'data/供应链库存数据看板.xlsx'
REPORT_DATE = '2026-07-10'

# 1. 读取 Excel
xl = pd.ExcelFile(EXCEL_PATH)
sheet_names = xl.sheet_names

# 2. 读取指定 Sheet
df = pd.read_excel(EXCEL_PATH, sheet_name='海外库存（效期维度）-海外库存（效期维度）')
df_data = df[df['日期'] != '合计']  # 排除合计行
df_total = df[df['日期'] == '合计']  # 合计行

# 3. 汇总指标
transit_qty = float(df_data['在途库存数量'].sum())
avail_qty = float(df_data['在库库存数量'].sum())
total_amt = float(df_data['总金额'].sum())

# 4. 对比 BQ（通过 bq CLI 查询）
import subprocess
result = subprocess.run([
    'bq', 'query', '--use_legacy_sql=false', '--format=json',
    '''
    SELECT 
        ROUND(SUM(In_transit_Stock_qty), 0) AS transit_qty,
        ROUND(SUM(Available_Stock_qty), 0) AS avail_qty,
        ROUND(SUM(Available_Stock_cny), 2) AS avail_cny
    FROM `hiccpet-481303.dwd.dwd_scm_warehouse_available_transit_detail`
    WHERE fdate_p = '''' + REPORT_DATE + ''''
      AND (vine_or_not IS NULL OR vine_or_not != 'vine')
    '''
], capture_output=True, text=True)
bq_data = json.loads(result.stdout)[0]

# 5. 输出对比
print(f"在途库存: Excel={transit_qty:,.0f} vs BQ={float(bq_data['transit_qty']):,.0f}")
print(f"在库库存: Excel={avail_qty:,.0f} vs BQ={float(bq_data['avail_qty']):,.0f}")
```

---

## 七、校验报告结构

输出报告应包含以下章节：

1. **数据概况**：Excel 工作表列表、BQ 数据源概览
2. **汇总对比**：按维度（在途、在库、临期等）对比总数和金额
3. **明细级对比**：按仓库/ SKU 维度逐行对比
4. **关系验证**：验证 Sheet 间勾稽关系
5. **其他库存类型**：列出无法对比的库存类型及原因
6. **校验结论**：标注匹配/不匹配项及原因分析