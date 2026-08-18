---
name: "数据校验"
description: "Multi-dimension data validation skill covering record count comparison, field integrity, range checks, logical consistency, and quality reporting. Invoke when user wants to validate data between source and target, compare CSV vs DB, or produce data quality reports."
---

# 数据校验 Skill

多维数据校验技能，覆盖记录数对比、字段有效性、数据质量检查，输出结构化校验报告。参照业界数据质量六大维度（完整性、准确性、一致性、及时性、唯一性、规范性）进行系统性校验。

---

## 一、校验流程总览

```
┌─────────────────────────────────────────────────────────────┐
│                   数据校验六步法                              │
├─────────────────────────────────────────────────────────────┤
│ Step 1: 数据概览         → 获取总量、日期范围、字段结构        │
│ Step 2: 记录数对比       → 按日期/维度分组，源vs目标逐日比对   │
│ Step 3: 字段完整性校验   → 空值检查、必填字段校验              │
│ Step 4: 数据准确性校验   → 数值边界、逻辑一致性、格式校验      │
│ Step 5: 高级校验         → 重复检测、分布分析、时区转换        │
│ Step 6: 报告输出         → 结构化Markdown报告                 │
└─────────────────────────────────────────────────────────────┘
```

---

## 二、校验维度矩阵

| 维度 | 定义 | 检查方法 | 优先级 |
|:----:|------|----------|:------:|
| **完整性** | 数据不缺失 | NULL检查、空字符串检查、必填字段校验 | P0 |
| **准确性** | 数据真实反映业务 | 数值边界、值域范围、负数检测 | P0 |
| **一致性** | 跨系统数据一致 | 记录数对比、聚合值对比、关键字段逐行比对 | P0 |
| **及时性** | 数据在预期时间内 | 日期范围检查、采集时间对比、时滞分析 | P1 |
| **唯一性** | 无重复记录 | 主键重复检测、业务唯一键重复检测 | P1 |
| **规范性** | 数据格式合规 | 类型格式校验、枚举值校验、模式匹配 | P2 |

---

## 三、各步骤详细规范

### Step 1: 数据概览

获取源和目标两侧的基本信息，为后续校验提供上下文。

**核心新增：自动识别业务日期，体现最早/最近业务日期的数据量级，保证历史数据完整性。**

#### 1.1 自动识别业务日期字段

> **注意**：`created_at` 及类似字段（`craw_created_at`、`created_at_timestamp`、`crawl_time` 等）默认为**采集日期**（RPA/爬虫入库时间），不代表业务发生时间。仅当表中无任何业务日期字段时，才降级使用采集日期作为参考。少数业务表可能直接用 `created_at` 作为业务创建时间，需人工确认。

按优先级自动识别数据中的业务日期字段：

| 优先级 | 类别 | 字段名模式 | 典型场景 |
|:------:|:----:|-----------|----------|
| **P0** | 业务日期 | `date`, `business_date`, `report_date` | 明确标识业务日期的字段 |
| **P1** | 业务日期 | `order_date`, `sale_date`, `transaction_date`, `order_day` | 交易/订单/销售日期 |
| **P2** | 业务日期 | `stat_date`, `dt`, `biz_date`, `data_date` | 统计日期、分区字段 |
| **采集日期** | 采集日期 | `created_at`, `crawl_created_at`, `created_at_timestamp`, `crawl_time` | **默认是采集时间，仅当无P0~P2字段时降级使用** |

**自动识别逻辑**：遍历字段名，按 P0 → P1 → P2 优先级匹配第一个存在的字段作为业务日期。如果仅匹配到采集日期字段，则在报告中标记 **"⚠️ 使用采集日期替代，需人工确认"**。

#### 1.2 历史数据完整性检查

| 检查项 | 说明 |
|--------|------|
| 最早业务日期 | 确定数据开始覆盖的时间点，判断是否满足业务回溯要求 |
| 最早日期数据量 | 检查开始日期的数据是否完整（首日不应显著偏少） |
| 最近业务日期 | 确定数据截止时间点，判断是否及时更新 |
| 最近日期数据量 | 检查最新日期的数据是否完整（最后一日不应显著偏少） |
| 覆盖天数 | 业务日期覆盖的总天数 |
| 空白区间 | 业务日期序列中是否存在缺失日期（历史数据断档） |
| 总量级评估 | 日均量 × 天数 vs 业务预期总量，评估整体量级合理性 |

**检查清单：**
- [ ] 源数据总记录数
- [ ] 目标数据总记录数
- [ ] 源数据业务日期字段自动识别
- [ ] 目标数据业务日期字段自动识别
- [ ] 源数据最早业务日期及其数据量
- [ ] 源数据最近业务日期及其数据量
- [ ] 目标数据最早业务日期及其数据量
- [ ] 目标数据最近业务日期及其数据量
- [ ] 两端日期范围是否对齐
- [ ] 两侧字段列表及类型

**SQL模板：**
```sql
-- 总记录数
SELECT COUNT(*) AS total FROM `{table}` WHERE {filter};

-- 业务日期范围及端点数据量（自动识别业务日期字段）
SELECT
  MIN(`{date_field}`) AS min_business_date,
  MAX(`{date_field}`) AS max_business_date,
  COUNT(DISTINCT `{date_field}`) AS covered_days,
  SUM(CASE WHEN `{date_field}` = (SELECT MIN(`{date_field}`) FROM `{table}` WHERE {filter}) THEN 1 ELSE 0 END) AS min_date_records,
  SUM(CASE WHEN `{date_field}` = (SELECT MAX(`{date_field}`) FROM `{table}` WHERE {filter}) THEN 1 ELSE 0 END) AS max_date_records
FROM `{table}` WHERE {filter};

-- 采集时间范围（如存在 created_at）
SELECT MIN(created_at) AS min_created, MAX(created_at) AS max_created
FROM `{table}` WHERE {filter};

-- 按业务日期分组统计（含端点标记）
SELECT
  `{date_field}`,
  COUNT(*) AS cnt,
  CASE
    WHEN `{date_field}` = (SELECT MIN(`{date_field}`) FROM `{table}` WHERE {filter}) THEN '最早'
    WHEN `{date_field}` = (SELECT MAX(`{date_field}`) FROM `{table}` WHERE {filter}) THEN '最近'
    ELSE ''
  END AS endpoint_tag
FROM `{table}` WHERE {filter}
GROUP BY `{date_field}` ORDER BY `{date_field}`;

-- 检查业务日期是否连续（识别数据断档）
WITH date_seq AS (
  SELECT `{date_field}`, COUNT(*) AS cnt
  FROM `{table}` WHERE {filter}
  GROUP BY `{date_field}`
)
SELECT
  a.`{date_field}` AS current_date,
  a.cnt AS current_cnt,
  b.`{date_field}` AS next_date,
  DATEDIFF(b.`{date_field}`, a.`{date_field}`) AS gap_days
FROM date_seq a
LEFT JOIN date_seq b ON b.`{date_field}` = DATE_ADD(a.`{date_field}`, INTERVAL 1 DAY)
WHERE b.`{date_field}` IS NULL
  AND a.`{date_field}` < (SELECT MAX(`{date_field}`) FROM date_seq)
ORDER BY a.`{date_field}`;
```

---

### Step 2: 记录数对比

按日期（或其他业务维度）将源和目标数据分组对比，定位差异日。

**检查清单：**
- [ ] 逐日记录数对比
- [ ] 标记源独有日期（目标无数据）
- [ ] 标记目标独有日期（源无数据）
- [ ] 统计完全匹配天数、差异天数
- [ ] 计算总差异率

**输出表格格式：**

| 日期 | 源 | 目标 | 差异 | 说明 |
|:---:|:--:|:----:|:----:|------|
| 06-01 | 100 | 100 | 0 | ✅ |
| 06-02 | 98 | 100 | -2 | 目标多2条 |
| **合计** | **N** | **M** | **D** | |

**异常判定规则：**
- `差异 > 0`：源多于目标，可能目标漏采
- `差异 < 0`：源少于目标，可能目标多采集或源导出不全
- `差异 = 0`：当日完全匹配

---

### Step 3: 字段完整性校验

检查所有字段的空值情况，评估数据完整度。

**检查清单：**
- [ ] 所有字段 NULL 计数
- [ ] 字符串字段空字符串计数
- [ ] 必填字段完整性（PK、业务关键字段必须100%）
- [ ] 可选字段完整性（低于阈值可接受，默认阈值为90%）
- [ ] 字段完整率排序

**SQL模板：**
```sql
SELECT
  COUNT(*) AS total,
  SUM(IF(`{field1}` IS NULL OR `{field1}` = '', 1, 0)) AS `{field1}_null`,
  SUM(IF(`{field2}` IS NULL, 1, 0)) AS `{field2}_null`,
  ...
FROM `{table}` WHERE {filter};
```

**空值率判定：**
- `0%`：完美 ✅
- `0% ~ 10%`：可接受 ⚠️
- `10% ~ 50%`：需关注 🔶
- `>50%`：严重 ❌

---

### Step 4: 数据准确性校验

检查数值边界、逻辑一致性、字段格式。

#### 4.1 数值边界检查

**检查清单：**
- [ ] 数值字段负值检测（如金额、数量不应为负）
- [ ] 百分比类字段范围检测（ctr、conversion_rate 应在[0,1]）
- [ ] 比率字段检测（ROAS 不应为负）
- [ ] 计数类字段检测（impressions、clicks 不应为负）
- [ ] 阈值越界检测（超出合理业务范围）

**SQL模板：**
```sql
SELECT
  SUM(IF(`{numeric_field}` < 0, 1, 0)) AS `{field}_negative`,
  SUM(IF(`{pct_field}` < 0 OR `{pct_field}` > 1, 1, 0)) AS `{field}_out_of_range`
FROM `{table}` WHERE {filter};
```

#### 4.2 逻辑一致性检查

**检查清单：**
- [ ] clicks ≤ impressions（点击不能超过曝光）
- [ ] orders ≤ units_sold（订单数不能超过销量）
- [ ] advertised_add_to_cart ≤ total_add_to_cart（广告加购不能超过总加购）
- [ ] 有销售额必须有销量（total_attributed_sales > 0 → units_sold > 0）
- [ ] 有销量必须有订单（units_sold > 0 → orders > 0）
- [ ] 有花费必须有曝光（ad_spend > 0 → impressions > 0）

**SQL模板：**
```sql
SELECT
  SUM(IF(clicks > impressions, 1, 0)) AS clicks_gt_impressions,
  SUM(IF(units_sold > 0 AND orders = 0, 1, 0)) AS sold_no_order,
  SUM(IF(total_attributed_sales > 0 AND units_sold = 0, 1, 0)) AS sales_no_sold
FROM `{table}` WHERE {filter};
```

#### 4.3 字段格式规范性检查

**检查清单：**
- [ ] 日期字段格式是否统一
- [ ] 枚举字段是否在预期值范围内
- [ ] 标识符字段（campaign_id、ad_group_id等）是否有非法值
- [ ] 数值字段是否存了非数值字符串

**SQL模板：**
```sql
-- 枚举值分布
SELECT `{enum_field}`, COUNT(*) AS cnt
FROM `{table}` WHERE {filter}
GROUP BY `{enum_field}` ORDER BY cnt DESC;

-- 异常值检测（如varchar中存了'N/A'等占位符）
SELECT `{field}`, COUNT(*) AS cnt
FROM `{table}` WHERE {filter}
  AND (`{field}` = 'N/A' OR `{field}` = 'NULL' OR `{field}` = '')
GROUP BY `{field}`;
```

---

### Step 5: 高级校验

#### 5.1 重复记录检测

**检查清单：**
- [ ] 主键唯一性（id 字段）
- [ ] 业务唯一键（date+campaign_id+ad_group_id+item_id 等组合）
- [ ] 重复记录采样

**SQL模板：**
```sql
-- 业务唯一键重复检测
SELECT `{field1}`, `{field2}`, `{field3}`, COUNT(*) AS dup_cnt
FROM `{table}` WHERE {filter}
GROUP BY `{field1}`, `{field2}`, `{field3}`
HAVING COUNT(*) > 1
ORDER BY dup_cnt DESC;
```

#### 5.2 聚合值对比（源 vs 目标）

当两侧都有数值时，除逐日记录数外，还应对比关键指标的聚合值。

**检查清单：**
- [ ] 总 impression 数对比
- [ ] 总 clicks 数对比
- [ ] 总 ad_spend 对比
- [ ] 总 sales 对比
- [ ] 均值、最大值对比

**SQL模板：**
```sql
SELECT
  COUNT(*) AS cnt,
  SUM(impressions) AS total_impressions,
  SUM(clicks) AS total_clicks,
  SUM(ad_spend) AS total_spend,
  SUM(total_attributed_sales) AS total_sales,
  AVG(ctr) AS avg_ctr,
  AVG(roas) AS avg_roas
FROM `{table}` WHERE {filter};
```

#### 5.3 时区转换校验（跨时区数据专用）

当数据涉及不同时区时，需验证时区转换逻辑的正确性。

**检查清单：**
- [ ] 原始时区标识（UTC/ET/PT/北京时间等）
- [ ] 转换后日期是否一致
- [ ] 转换前后记录数是否匹配
- [ ] 跨日边界记录的手动抽样验证

**SQL模板：**
```sql
-- 美国东部时间 vs 美国太平洋时间 转换
SELECT
  `{utc_date}`,
  DATE_SUB(`{utc_date}`, INTERVAL 4 HOUR) AS et_date,
  DATE_SUB(`{utc_date}`, INTERVAL 7 HOUR) AS pt_date
FROM `{table}` WHERE {filter};
```

#### 5.4 分布异常检测

**检查清单：**
- [ ] 数值字段分位数统计（发现离群值）
- [ ] 每日记录数是否存在突增/突降（环比异常）
- [ ] 枚举值分布是否合理

**SQL模板：**
```sql
-- 数值分布统计
SELECT
  MIN(`{field}`) AS min_val,
  MAX(`{field}`) AS max_val,
  AVG(`{field}`) AS avg_val,
  STD(`{field}`) AS std_val
FROM `{table}` WHERE {filter};

-- 每日记录数环比（检测突增突降）
WITH daily AS (
  SELECT `{date_field}`, COUNT(*) AS cnt
  FROM `{table}` WHERE {filter}
  GROUP BY `{date_field}`
)
SELECT
  a.`{date_field}`,
  a.cnt,
  LAG(a.cnt) OVER (ORDER BY a.`{date_field}`) AS prev_cnt,
  ROUND((a.cnt - LAG(a.cnt) OVER (ORDER BY a.`{date_field}`)) / LAG(a.cnt) OVER (ORDER BY a.`{date_field}`) * 100, 2) AS change_pct
FROM daily a
ORDER BY a.`{date_field}`;
```

---

### Step 6: 报告输出

校验完成后，输出结构化 Markdown 报告。

**报告模板：**

```markdown
# {报告标题}

> **日期**: {校验日期}
> **场景**: {数据场景描述}
> **对比口径**: {校验维度说明}
> **数据说明**: 源（{源描述}），目标（{目标描述}）
> **业务日期字段**: {自动识别的日期字段名} {⚠️ 采集日期/需人工确认}

---

## 一、数据概览

| 项目 | 源 | 目标 |
|------|:--:|:----:|
| 总记录数 | {N} | {M} |
| 业务日期范围 | {min} ~ {max} | {min} ~ {max} |
| 覆盖天数 | {N}天 | {M}天 |
| 最早日期数据量 | {date}: {N}条 | {date}: {M}条 |
| 最近日期数据量 | {date}: {N}条 | {date}: {M}条 |
| 日均数据量 | {N}条/天 | {M}条/天 |
| 数据断档天数 | {N}天 | {M}天 |

### 业务日期端点数据量对比

| 端点 | 源日期 | 源记录数 | 目标日期 | 目标记录数 | 差异 | 评估 |
|:----:|:------:|:--------:|:--------:|:----------:|:----:|:----:|
| 最早 | {date} | {N} | {date} | {M} | {D} | ✅/⚠️ |
| 最近 | {date} | {N} | {date} | {M} | {D} | ✅/⚠️ |

### 历史数据完整性评估

- **覆盖完整性**: ✅ 两端日期范围一致 / ⚠️ 源早于目标 / ⚠️ 目标早于源
- **数据连续性**: ✅ 无断档 / ⚠️ 存在{N}天空白区间（详见下方明细）
- **端点量级**: ✅ 首尾日均正常 / ⚠️ 端点数据量异常（首日/末日显著少于日均）

## 二、每日记录数对比

{对比表格}

| **合计** | **{N}** | **{M}** | **{D}** | |

## 三、字段完整性校验

| 字段 | 空值数 | 空值率 | 结果 |
|------|:------:|:------:|:----:|
| ... | ... | ... | ✅/⚠️/🔶/❌ |

## 四、数据准确性校验

### 4.1 数值边界

| 检查项 | 命中数 | 结果 |
|--------|:------:|:----:|
| ... | 0 | ✅ |

### 4.2 逻辑一致性

| 检查项 | 命中数 | 结果 |
|--------|:------:|:----:|

## 五、高级校验

{高级校验结果}

## 六、校验结论

| 维度 | 结果 | 说明 |
|:----:|:----:|------|
| 完整性 | ✅ | ... |
| 准确性 | ✅/⚠️ | ... |
| 一致性 | ✅ | ... |
| 唯一性 | ✅/❌ | ... |

---
*报告由数据校验Skill自动生成 | {日期}*
```

---

## 四、异常分级规则

所有校验项按以下三级标记：

| 等级 | 标记 | 定义 | 响应 |
|:----:|:----:|------|------|
| **P0** | ❌ | 关键数据错误，影响业务决策 | 必须修复，立即处理 |
| **P1** | ⚠️ | 数据质量隐患，需关注 | 需分析原因，安排修复 |
| **P2** | 🔶 | 数据规范性问题，可优化 | 记录在案，持续改进 |
| 通过 | ✅ | 校验通过 | 无需处理 |

---

## 五、校验流程示例（Python + MySQL）

### 5.1 数据库客户端

```python
# validator/db_client.py
class DbClient:
    def __init__(self):
        self.conn = None
    
    def execute(self, sql):
        # 执行SQL并返回结果
        pass
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        if self.conn:
            self.conn.close()
```

### 5.2 CSV 读取

```python
import csv
with open('{csv_path}', 'r', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
```

### 5.3 对比执行

```python
from validator.db_client import DbClient

# CSV统计
csv_counts = Counter(r['{date_field}'] for r in csv_rows)

# MySQL统计
db = DbClient()
with db:
    mysql_rows = db.execute('''
        SELECT `{date_field}`, COUNT(*) AS cnt
        FROM `{table}` WHERE {filter}
        GROUP BY `{date_field}` ORDER BY `{date_field}`
    ''')
    mysql_counts = {str(r[0]): r[1] for r in mysql_rows}

# 逐日对比
for d in sorted(set(list(csv_counts) + list(mysql_counts))):
    c = csv_counts.get(d, 0)
    m = mysql_counts.get(d, 0)
    # 记录结果
```

---

## 六、最佳实践 Checklist

### 校验前
- [ ] 确认两端业务日期字段一致（自动识别或手动指定）
- [ ] 确认两端数据范围一致（同日期/同分区）
- [ ] 确认两端数据过滤条件一致（是否都加了 WHERE 子句）
- [ ] 确认字段映射关系正确（字段名、类型、含义）
- [ ] 确认时区归属一致（UTC/ET/PT/北京时间）
- [ ] 明确业务预期历史数据回溯天数（如：需覆盖最近90天）

### 校验中
- [ ] 先总量对比，后逐日对比
- [ ] 先检查端点日期数据量（历史完整性），后中间日期
- [ ] 先字段完整性，后业务一致性
- [ ] 异常数据必须采样查看明细
- [ ] 同时对比记录数 + 聚合值（双层校验）
- [ ] 检查业务日期连续性和端点量级（首尾日均不应显著低于日均值）
- [ ] 分析差异原因（漏采/重复/时区/过滤条件差异/首尾日期不完整）

### 校验后
- [ ] 输出结构化报告，包含端点数据量对比和历史完整性评估
- [ ] 标记 P0/P1 问题，明确责任人
- [ ] 异常原因记录到报告
- [ ] 定期回归校验（每日/每周）

---

## 七、快速使用

```bash
# 1. 每日记录数对比
python -m validator.daily_check --source {csv_path} --table {table_name} --filter "{where_condition}"

# 2. 字段完整性检查
python -m validator.field_check --table {table_name} --filter "{where_condition}"

# 3. 全量校验（生成报告）
python -m validator.full_check --source {csv_path} --table {table_name} --filter "{where_condition}" --output docs/{report_name}.md
```