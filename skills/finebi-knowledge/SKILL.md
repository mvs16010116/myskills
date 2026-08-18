---
name: "finebi-knowledge"
description: "FineBI知识库技能。当用户询问FineBI相关问题（功能使用、数据源配置、图表制作、权限管理、函数公式、部署集成等）时调用此技能，从本地知识库通过RAG语义检索回答。内置指标查询和数据集查询API，支持实时查询指标数据、按表名搜索数据集、获取字段、分页查询数据。"
---

# FineBI 知识库技能

## 概述

基于帆软 FineBI 6.X（1370篇）和 7.X（1262篇）完整帮助文档构建，总计 2632 篇文档，覆盖 FineBI 全部功能模块。使用 RAG 语义检索，支持中英文混合查询。

本技能的核心能力围绕 **口径**（指标的计算规则）展开——用户问"XX指标怎么算的"即是在问口径。技能支持通过 API 实时查询指标的**口径公式**、**血缘关系**和**数据值**，也支持按表名搜索数据集并查询数据。

---

## 前置代码

以下所有示例均基于 `query_indicator.py` 模块。初始化方式：

```python
import sys; sys.path.insert(0, r'C:\Users\user\.trae-cn\skills\finebi-knowledge')
from query_indicator import IndicatorAPI, Secret
api = IndicatorAPI('http://bi.hiccpet.net', Secret(username='rank', secret_key='你的密钥'))
```

后续示例中假设 `api` 已按上述方式初始化。

---

## 分支：RAG 文档检索

使用语义检索代替关键词搜索，支持按版本过滤。前置代码使用 `build_rag_index` 模块：

```python
import sys; sys.path.insert(0, r'C:\Users\user\.trae-cn\skills\finebi-knowledge')
from build_rag_index import search
```

### 通用检索

```python
results = search('你的问题', top_k=5)
for r in results:
    print(f'[{r["version"]}] {r["title"]} (score: {r["score"]:.2f})')
    print(f'  预览: {r["content"][:200]}...')
```

### 按版本过滤

```python
results = search('你的问题', top_k=5, version_filter='6.X')
```

### 检索结果字段

| 字段 | 说明 |
|------|------|
| `score` | 相似度分数（0~1，越高越相关） |
| `version` | 文档版本（6.X / 7.X） |
| `title` | 文档标题 |
| `url` | 原始文档链接 |
| `content` | 匹配内容预览 |

### 索引维护

```bash
cd "C:\Users\user\.trae-cn\skills\finebi-knowledge"

# 重建索引（文档更新后执行）
python build_rag_index.py

# 增量更新检测（检测文档变化，有变化时自动重建）
python update_knowledge.py
```

---

## 分支：指标数据查询

通过 API 实时查询指标，认证方式为 **HMAC-SHA256 摘要签名认证**，需提供用户名和密钥。

### 快速查询（一键查询）

搜索指标 → 按日期分组 → 按月汇总，一步完成：

```python
from query_indicator import quick_query, print_result
result = quick_query(
    server_url='http://bi.hiccpet.net',
    username='你的用户名',
    secret_key='你的密钥',
    keyword='销量',            # 搜索关键词
    dimension_keyword='日期',  # 维度关键词（可选，默认"日期"）
)
print_result(result)
```

### 搜索指标/维度

```python
# 搜索指标
api.search_indicators('销量')
# 返回: [{"id": "...", "name": "指标名", "position": "路径"}, ...]

# 搜索维度
api.search_dimensions('日期')
# 返回: [{"id": "...", "name": "维度名", "position": "路径"}, ...]
```

### 语义信息接口（口径、血缘、关系）

查看指标/维度的属性、口径公式、血缘关系、相互关联关系。

```python
# 1. 查看指标属性（含计算口径公式）
r = api.get_metric_info('指标ID')
print(r['data'].get('caliber', {}).get('formula', ''))  # 口径公式

# 2. 查看指标关联的维度
r = api.get_metric_relate_dimensions('指标ID')
# 返回: ["维度名1", "维度名2", ...]

# 3. 查看维度关联的指标
r = api.get_dimension_relate_metrics('维度ID')
# 返回: ["指标名1", "指标名2", ...]

# 4. 查看指标血缘关系（上下游依赖树）
r = api.get_metric_consanguinity('指标ID')
# r['node_list'] 为所有节点，r['parent_edges'] / r['child_edges'] 为上下游边

# 5. 查看维度属性
r = api.get_dimension_info('维度ID')
# 返回: {"name": "维度名", "description": "描述"}

# 6. 查看维度值（枚举值列表）
r = api.get_dimension_data('维度ID', page_size=10)
# 返回: {"data": ["值1", "值2", ...], "page_info": {...}}
```

### 查询指标数据

```python
# 查询总数据（无维度）
result = api.query_data(metrics=['指标ID'], field_names={'指标ID': '指标名称'})
# result['total'] 为汇总值，result['row_count'] 为记录数

# 按维度分组查询
result = api.query_data(
    metrics=['指标ID'], dimensions=['维度ID'],
    field_names={'指标ID': '销量', '维度ID': '日期'},
    page_size=30,
)
# result['rows'] 为 [["维度值", "指标值"], ...]

# 查询所有页（自动分页聚合）
result = api.query_all_pages(
    metrics=['指标ID'], dimensions=['维度ID'],
    page_size=200, field_names={'指标ID': '销量', '维度ID': '日期'},
)
# 返回: {"total_rows": N, "total": 汇总值, "page_count": N, "rows": [...]}

# 按月汇总
result = api.query_data_summary(
    metrics=['指标ID'], dimensions=['维度ID'],
    field_names={'指标ID': '销量', '维度ID': '日期'},
)
# result['monthly'] 为 {"2026-01": 值, "2026-02": 值, ...}
```

### 命令行快捷使用

```bash
cd "C:\Users\user\.trae-cn\skills\finebi-knowledge"
python query_indicator.py http://bi.hiccpet.net 你的用户名 你的密钥 销量 日期
```

### 查询结果字段

| 字段 | 说明 |
|------|------|
| `success` | 是否成功 |
| `fields` | 返回字段信息（名称、类型） |
| `rows` | 数据行 |
| `total` | 数值汇总 |
| `total_rows` | 总记录数 |
| `monthly` | 按月汇总（仅 `query_data_summary`） |
| `page_info` | 分页信息 |

---

## 分支：数据集查询（按表名查数据）

支持通过表名搜索数据集、获取字段、查询数据。

### 关键原理

1. **搜索数据集**：通过 `/decision/api/dc/v1/indicator/search` 接口，使用 `itemTypes=[3]`（3=数据集类型）过滤
2. **获取 UUID**：搜索结果中的 `name` 字段是数据集 UUID，而非显示名
3. **查字段/数据**：通过 `/v5/api/tables/fields/page` 和 `/v5/api/tables/data/page` 接口，使用 UUID 查询，需要 Bearer Token 认证（自动登录获取）

### 搜索数据集

```python
# 按表名搜索（模糊匹配）
datasets = api.search_datasets('运单入库')
# 返回: [{"name": "UUID", "transferName": "显示名", "position": "路径", "fields": [...], ...}, ...]

# 不传 keyword 列出所有数据集
api.search_datasets()
```

### 查询字段和数据

```python
# 获取字段列表
fields = api.get_dataset_fields('数据集UUID')
# 返回: [{"name": "字段名", "type": 16(文本)/32(数值)/48(时间)}, ...]

# 分页查询数据
result = api.get_dataset_data('数据集UUID', page_size=5)
# result['fields'] 为字段元数据，result['data'] 为二维数组，result['total_rows'] 为总行数
```

### 完整流程：表名 → 数据

```python
# 1. 搜索表名获取 UUID
datasets = api.search_datasets('运单入库')
uuid = datasets[0]['name']   # 注意：不是 transferName

# 2. 获取字段
fields = api.get_dataset_fields(uuid)
print(f'字段数: {len(fields)}')

# 3. 查询数据
result = api.get_dataset_data(uuid, page_size=5)
fnames = [f['name'] for f in result['fields']]
for row in result['data']:
    print(dict(zip(fnames, row)))
```

### 方法说明

| 方法 | 说明 | 认证方式 |
|------|------|---------|
| `search_datasets(keyword)` | 按显示名搜索数据集，返回 UUID | HMAC-SHA256 |
| `get_dataset_fields(uuid)` | 获取数据集字段列表 | Bearer Token（自动登录） |
| `get_dataset_data(uuid, page_size, page_index)` | 分页查询数据集数据 | Bearer Token（自动登录） |

### 注意事项

1. `search_datasets` 返回的 `name` 字段才是 UUID，非显示名 `transferName`
2. `get_dataset_fields` 和 `get_dataset_data` 自动调用 `/decision/login` 获取 Bearer Token
3. 默认使用 `rank/rank` 账号登录，如需其他账号传 `login_username` / `login_password` 参数
4. 数据返回格式为二维数组，每行按 fields 顺序排列
5. 字段类型：16=文本, 32=数值, 48=时间