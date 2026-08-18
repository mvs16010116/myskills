---
name: "api-collect-response"
description: "API采集接口返回内容标准化规范。定义数据采集route的统一JSON响应格式，包含status、message、data三层结构，data中强制包含success_count、failed_count、total_records、error_detail字段。适用于所有采集类、回填类、初始化类API接口的开发与改造。"
---

# API采集返回内容规范

## 概述

本 Skill 定义项目中所有**数据采集类 API Route** 的统一返回格式规范。所有采集、回填、初始化接口的 HTTP 响应必须遵循此规范，确保前后端协作一致、可观测性统一。

## 适用场景

在以下场景中**必须调用本 Skill**：
- 新增一个数据采集、回填、初始化的 API 路由
- 修改或重构现有的采集接口返回格式
- 审查代码时检查采集接口的响应格式是否符合规范
- 编写采集接口的文档说明

## 排除场景

以下接口**无需遵循**本规范（保持各自语义即可）：
- 健康检查 `/health`
- 状态查询 `/status`
- 非采集类的 CRUD 接口

## 统一响应结构

所有采集接口的 HTTP 响应必须是标准三层 JSON 结构：

```json
{
  "status": "success | error",
  "message": "人类可读的描述信息",
  "data": {
    "success_count": 0,
    "failed_count": 0,
    "total_records": 0,
    "error_detail": ""
  }
}
```

### 顶层字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `status` | string | 是 | 固定取值 `"success"` 或 `"error"`，表示本次采集整体是否成功。禁止使用自定义状态码（如 `"错误2"`、`"error20260324"` 等） |
| `message` | string | 是 | 人类可读的描述信息。成功时如 `"订单采集完成"`，失败时描述具体错误 |
| `data` | object | 是 | 采集结果数据，详见下方 data 规范 |

### data 字段规范

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `success_count` | int | 是 | 成功采集并写入数据库的记录数。默认 `0` |
| `failed_count` | int | 是 | 采集失败的记录数。默认 `0` |
| `total_records` | int | 是 | 总记录数，固定为 `success_count + failed_count`，不允许用其他公式 |
| `error_detail` | string | **按需** | 错误场景必填。描述具体失败原因，如 `"API调用失败: xxx"`、`"批量写入失败: xxx"`。成功场景可返回空字符串或省略该字段 |

### data 可选扩展字段

允许按业务需要增加额外字段，但**不得影响上述必填字段**。示例：

```json
{
  "data": {
    "success_count": 22,
    "failed_count": 0,
    "total_records": 22,
    "start_date": "2026-06-01",
    "end_date": "2026-06-02",
    "page": 1,
    "pageSize": 100,
    "backfill": false,
    "windows": 1
  }
}
```

## 各场景返回示例

### 场景一：完全成功（全部采集成功）

```json
{
  "status": "success",
  "message": "订单采集完成",
  "data": {
    "success_count": 1026,
    "failed_count": 0,
    "total_records": 1026,
    "start_date": "2026-03-25",
    "end_date": "2026-06-23"
  }
}
```

### 场景二：部分成功（部分失败）

```json
{
  "status": "success",
  "message": "商品采集完成",
  "data": {
    "success_count": 95,
    "failed_count": 5,
    "total_records": 100,
    "error_detail": "第3页有5条数据预处理失败"
  }
}
```

### 场景三：完全失败

```json
{
  "status": "error",
  "message": "API调用失败: Could not parse the provided public key.",
  "data": {
    "success_count": 0,
    "failed_count": 50,
    "total_records": 0,
    "error_detail": "API调用失败: Could not parse the provided public key."
  }
}
```

### 场景四：参数校验失败

```json
{
  "status": "error",
  "message": "日期范围不能超过90天",
  "data": {
    "success_count": 0,
    "failed_count": 0,
    "total_records": 0,
    "error_detail": "日期范围不能超过90天"
  }
}
```

## Route 异常处理规范

在 route 层的 `try/except` 中捕获到未预期异常时，必须返回标准格式：

```python
except Exception as e:
    error_msg = f"采集XX失败: {str(e)}"
    logger.error(error_msg)
    return jsonify({
        "status": "error",
        "message": error_msg,
        "data": {
            "success_count": 0,
            "failed_count": 0,
            "total_records": 0,
            "error_detail": error_msg
        }
    }), 500
```

## Route 日志规范

在 route 的 `rl.step()` 和 `rl.summary()` 中引用采集记录数时，**必须使用 `data.success_count` 字段**，避免使用不存在的字段名导致日志统计始终为 0：

```python
# ✅ 正确
rl.step(f"完成: status={result['status']}, collected={result.get('data', {}).get('success_count', 0)}")
rl.summary({
    "steps": [{"name": "...", "records": result.get('data', {}).get('success_count', 0), ...}],
    ...
})

# ❌ 错误（字段名不存在，日志 records 始终为 0）
rl.step(f"完成: collected={result.get('data', {}).get('collected_orders', 0)}")
```

## 实现模板

新增一个采集接口时的标准模板：

```python
@app.route('/hktvmall/api/v1/collect_xxx', methods=['GET'])
def api_collect_xxx():
    rl = get_route_logger()
    rl.banner("采集XXX", endpoint="/hktvmall/api/v1/collect_xxx")
    try:
        # 1. 参数解析
        param = request.args.get('param')

        # 2. 参数校验（立即返回，不进入采集逻辑）
        if invalid:
            return jsonify({
                "status": "error",
                "message": "参数错误: xxx",
                "data": {
                    "success_count": 0,
                    "failed_count": 0,
                    "total_records": 0,
                    "error_detail": "参数错误: xxx"
                }
            })

        # 3. 执行采集
        result = collector.collect_xxx(param)

        # 4. 日志记录（注意用 success_count，不要用错误的字段名）
        rl.step(f"完成: status={result['status']}, collected={result.get('data', {}).get('success_count', 0)}")
        rl.summary({
            "steps": [{"name": "collect_xxx", "records": result.get('data', {}).get('success_count', 0),
                       "status": "成功" if result['status'] == 'success' else "失败"}],
            "overall_success": result['status'] == 'success'
        })

        # 5. 返回结果（collector 内部已组装好标准格式）
        return jsonify(result)

    except Exception as e:
        rl.error("collect_xxx", str(e))
        rl.summary({
            "steps": [{"name": "collect_xxx", "records": 0, "status": "失败"}],
            "overall_success": False
        })
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": {
                "success_count": 0,
                "failed_count": 0,
                "total_records": 0,
                "error_detail": str(e)
            }
        }), 500
```

## Collector 方法返回值规范

负责业务逻辑的 `collect_xxx()` 方法必须在内部完成**成功/失败计数**，并返回标准格式的 dict，不要在 route 层再组装 data：

```python
def collect_xxx(self, ...):
    success_count = 0
    failed_count = 0
    error_detail = ""

    try:
        # ... 采集逻辑，遇到失败时：
        # failed_count += N
        # error_detail = "失败原因"

        if error_detail and success_count == 0:
            return {
                "status": "error",
                "message": error_detail,
                "data": {
                    "success_count": 0,
                    "failed_count": failed_count,
                    "total_records": 0,
                    "error_detail": error_detail
                }
            }

        return {
            "status": "success",
            "message": "XXX采集完成",
            "data": {
                "success_count": success_count,
                "failed_count": failed_count,
                "total_records": success_count + failed_count
            }
        }

    except Exception as e:
        error_msg = f"采集XXX失败: {str(e)}"
        return {
            "status": "error",
            "message": error_msg,
            "data": {
                "success_count": success_count,
                "failed_count": failed_count,
                "total_records": success_count + failed_count,
                "error_detail": error_msg
            }
        }
```

## 代码审查检查清单

在审查采集接口代码时，逐项检查：

- [ ] 返回 JSON 包含 `status`、`message`、`data` 三个顶层字段
- [ ] `status` 取值仅为 `"success"` 或 `"error"`，无自定义状态码
- [ ] `data` 包含 `success_count`（int）、`failed_count`（int）、`total_records`（int）
- [ ] `total_records` 严格等于 `success_count + failed_count`
- [ ] 错误场景 `data` 包含 `error_detail`（string）
- [ ] 所有 `total_records` 求和场景均使用 `success_count` 而非不存在的字段名
- [ ] Collector 内部的 `_xxx_window` 等辅助方法返回 `(collected, failed, error_detail)` 三元组
- [ ] Route 层 `except` 分支也返回标准格式（含 data），而非仅 `{"status": "error", "message": str(e)}`
- [ ] 日志中的 `records` 引用 `data.success_count`，而非 `data.collected_orders` 等错误字段名