---
name: lingxing-api
label: 领星API知识库
description: 领星 ERP 开放接口（apidoc.lingxing.com）全量知识库，611 个 API 接口的元信息、参数、业务键关联索引、详细入参/出参/样例。当用户问关于领星 API、某类数据怎么采集、某个业务单号（采购单 / 发货单 / 订单 / ASIN / MSKU / 店铺 / 仓库 等）相关接口、接口之间的关系、某个接口怎么调用、需要传什么参数、返回什么字段时触发。覆盖销售、FBA、采购、仓库、物流、广告、财务、统计、客服、目标管理、多平台、亚马逊源表等 20 个一级分类。
---

# 领星 API 知识库

基于领星 ERP 开放接口文档站（https://apidoc.lingxing.com/）全量爬取（611 个 API）构建的结构化知识库。

## 何时用

- 用户问"领星有哪些 API 能查 X" / "X 怎么采集"
- 用户问"采购单号 / 发货单号 / 订单号 / ASIN / MSKU / 店铺 ID 相关的接口有哪些"
- 用户问"两个接口之间是什么关系" / "用 A 接口返回的单号，怎么用 B 接口"
- 用户问"领星的 [模块名] 模块有哪些 API"
- 用户问某个具体接口的用法（**路径、参数、必填项、示例**）
- 用户问"这个接口要传什么 / 返回什么" / "请求示例怎么写"

**不适用**：领星 ERP 系统操作问题（不是 API）；非领星数据；非领星域的亚马逊 API。

## 知识库结构

- `data/apis_clean.json` —— 611 个 API 的精简元数据（标题、路径、方法、分类、限流、参数数量、业务键）
- **`data/apis_detailed.json`** —— 611 个 API 的**完整详情**：入参/出参/请求示例/响应示例/curl 示例（**主要用这个**）
- `data/api_path_index.json` —— api_path → 详细记录 的 O(1) 索引（可选；缺失时 query.py 会从 apis_detailed 运行时重建）
- `data/api_title_index.json` —— title → 详细记录 的索引（可选）
- `data/biz_key_index.json` —— 37 个业务键 → 接口索引（primary/return/mention 三级关联）
- `data/category_index.json` —— 20 个一级分类 → 接口列表
- `data/path_prefix_index.json` —— 70 个路径前缀 → 接口列表
- `data/desc_index.json` —— 51 个中文关键词 → 接口列表

> **打包格式说明**：为控制发布包体积，`apis_detailed.json` 在分发包中可能以 **`apis_detailed.json.gz`**（gzip 压缩，6.2MB→753KB）形式存在，`query.py` 对 `.json` 与 `.json.gz` **透明兼容**，无需手动解压；`api_path_index.json` / `api_title_index.json` 在分发包中省略（与详细数据冗余），由 query.py 运行时自动重建索引。

> **新增重点**：`apis_detailed.json` 含每个接口的入参（含必填/类型/说明/示例）、出参（嵌套路径/类型/说明/示例）、请求示例 JSON、响应成功/失败示例 JSON。**此前版本只存了元数据，现在补全了所有细节。**

## 查询工具

直接用 `scripts/query.py` 子命令查询（基于 data/ 下的索引 JSON），不要重新解析 md：

```bash
# ===== 关联 / 模糊查询（轻量索引） =====

# 业务键查询（最常用，用户的"X 相关接口"诉求）
python3 scripts/query.py by-key "采购单号"           # 15 primary + 52 return + 5 mention
python3 scripts/query.py by-key "ASIN"
python3 scripts/query.py by-key "店铺ID"

# 模糊搜索（标题、路径、中文关键词）
python3 scripts/query.py search "创建采购单"
python3 scripts/query.py search "FBA货件"

# 路径片段查询
python3 scripts/query.py by-path "purchase"

# 分类查询
python3 scripts/query.py by-category "采购"
python3 scripts/query.py by-category "FBA"

# 关联接口（基于业务键共享，自动展开）
python3 scripts/query.py related "getInboundShipmentListMwsDetail"

# ===== 详情查询（读 apis_detailed.json） =====

# 精简详情（仅元数据）
python3 scripts/query.py get "getInboundShipmentListMwsDetail"

# 完整详情：入参/出参/请求示例/响应示例/curl
python3 scripts/query.py detail "outboundgetOrders"        # 按 api_path 片段
python3 scripts/query.py detail "/erp/sc/routing/storage/outbound/getOrders"  # 完整路径
python3 scripts/query.py detail "查询出库单列表"            # 按 title
python3 scripts/query.py detail "outbound" --no-example   # 不打印示例

# ===== 元查询 =====

python3 scripts/query.py list-keys
python3 scripts/query.py list-categories
python3 scripts/query.py stats
```

每个子命令支持 `--limit N` 控制输出条数。

## 工作流

### 1. 识别用户问的是哪类问题

| 用户问法示例 | 问题类型 | 首选查询 |
|---|---|---|
| "采购单号相关的接口有哪些" / "X 相关接口" | 业务键关联 | `by-key` |
| "领星采购模块有哪些 API" / "FBA 模块" | 分类查询 | `by-category` |
| "怎么创建 X" / "如何查询 X" | 模糊搜索 + 筛选 | `search` + 看标题动词 |
| "A 接口和 B 接口什么关系" / "A 接口返回 X，X 怎么用" | 关联分析 | `related` + `by-key` |
| "getInboundShipmentListMwsDetail 怎么用" / "要传什么参数" | 完整详情 | `detail` |
| "A 接口请求示例怎么写" / "返回什么字段" | 完整详情 | `detail` |

### 2. 业务键查询的解读

`by-key` 输出三类结果，含义不同：

- **PRIMARY（必填入参）** —— 必须把此业务键作为入参传入的接口；这些是"操作 X"的接口（创建/更新/查询/作废等）。
- **RETURN（返回含此键）** —— 返回结果里包含此业务键的接口；这些是"产出 X"的接口（采集 X 的数据时可调用）。
- **MENTION（描述提及）** —— 标题或参数描述里间接提到此业务键；通常是上下游关联或单据流转相关。

回答用户时按这三类分组说，**别把数字简单相加**——三类意义不同。

### 3. 模糊搜索的解读

`search` 同时匹配：
- API 标题和路径
- 中文关键词索引（"采购单"、"发货单"、"ASIN" 等业务对象词）

如果用户问的是动作（"创建"、"修改"、"作废"），先 `search` 业务对象，再从结果里挑出标题含动作的接口。

### 4. 关联查询的解读

`related <api_path>` 自动找出此接口涉及的所有业务键，并展开每个键下的"其它接口"——这就是"接口之间联系"的标准答法。

### 5. 详情查询的解读

`detail <ref>` 输出三段：入参（含必填/类型/说明/示例）→ 请求示例 → 出参（含嵌套路径如 `data>>order_sn`）→ 响应示例。

- `ref` 支持三种形式：
  - 完整 `api_path`：`/erp/sc/routing/storage/outbound/getOrders`
  - 路径片段：`outboundgetOrders`（模糊匹配）
  - title 中文/英文：`查询出库单列表` / `outboundgetOrders`
- 嵌套出参用 `>>` 分隔路径层级（如 `data>>item_list>>sku`），`depth` 字段标识层级。
- 请求/响应示例是原始 JSON 字符串，可直接复制使用。

## 回答模板

- **业务键问题**（如"采购单号相关接口"）：按 primary / return / mention 三段列出，每段给出前 10-15 个 + 总数；附 1-2 句说明。
- **分类问题**（如"FBA 模块"）：直接列出全部接口，提示总数。
- **操作问题**（如"怎么创建采购单"）：先 `search` 业务对象，再筛选标题含"创建/生成/添加"的；通常只有 1-3 个。
- **关联问题**（如"A 和 B 的关系"）：用 `related` 找共同业务键，并说明"通过 X 关联"。
- **接口调用问题**（如"这个接口怎么调" / "请求示例"）：直接 `detail` 输出完整入参/出参/示例，必要时简化。

## 注意

- **数据时效**：2026-08-12 抓取，之后领星可能新增/调整接口。如用户反馈"找不到某个新接口"，建议重抓 `_sidebar.md` 和 `docs/` 下的 md。
- **不重复抓**：除非用户明确说"重新抓"，否则不要重跑抓取脚本。
- **路径权限**：领星文档站所有路径均可匿名访问（HTTP 200），无需密钥。`Authorization/` 路径直接返回 markdown 内容。
- **接口关系**是基于业务键（共享字段名）的**静态关联**——领星文档本身没有显式的接口依赖图。如果发现用户问的关联超出此范围（如"A 调 B 之后会自动调 C"），老老实实说"业务键层面有关联，但实际调用关系需查接口实现"。
- **数据覆盖**：611 个接口中，~97% 含入参、~99% 含出参、~95% 含请求示例、~88% 含响应成功示例。少数接口（2 个 AWD 标签类、1 个 PDF 文件类）没有结构化出参表，返回原始字节流。

## 进阶：手动解析新接口

如需给某个具体接口生成更详细的参数/返回值说明，从 `data/apis_detailed.json` 出发——它包含所有已知细节，**原始 markdown 在抓取产物** `crawl/docs_raw/docs/<path>.md` 或重新 `curl https://apidoc.lingxing.com/docs/<path>.md`。
