---
name: "采集日志规范"
description: "数据采集系统日志模板规范。提供标准化的三阶段日志输出（Banner、Process、Summary），包含TeeLogger双写、print_banner、print_summary等完整实现。当需要编写数据采集系统日志输出、或复用日志格式规范时调用。"
---

# 数据采集系统日志模板规范

> 通用日志规范，可复用于任何数据采集平台。

---

## 一、日志整体结构

一个完整的采集日志分为 **3 个阶段**：

```
1. 启动横幅（Banner）       — 系统信息、版本、启动时间
2. 采集过程（Process）       — 步骤日志、API 调用、写入结果
3. 结果汇总（Summary）       — 表格统计、总体状态、耗时
```

---

## 二、标准日志格式

### 2.1 时间戳格式

| 层级 | 格式 | 示例 | 说明 |
|------|------|------|------|
| 行级前缀 | `YYYY-MM-DD HH:MM:SS \| ` | `2026-06-05 14:30:03 \|` | TeeLogger 自动添加，每条日志行前缀 |
| 过程内时间戳 | `[HH:MM:SS]` | `[14:30:03]` | 采集过程中的日志函数，相对时间便于阅读 |

### 2.2 代码实现

```python
class TeeLogger:
    """日志双写：同时输出到终端和文件"""

    def __init__(self, log_file: str):
        self.terminal = sys.stdout
        self.log_file = open(log_file, "a", encoding="utf-8")

    def write(self, message):
        if message.strip():
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"{ts} | {message}"
            self.terminal.write(line)
            self.log_file.write(line)
            self.log_file.flush()
        else:
            self.terminal.write(message)
            self.log_file.write(message)
            self.log_file.flush()

    def flush(self):
        self.terminal.flush()
        self.log_file.flush()


def log(msg):
    """采集过程中的日志函数，使用 [HH:MM:SS] 格式"""
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")
```

---

## 三、第 1 阶段：启动横幅（Banner）

**输出示例**：
```
================================================================================
                       万邑通(Winit) API 数据采集系统
================================================================================
采集程序版本: 1.0.0
工作目录: D:\PycharmProjects\datacollect\hicc_winit_api
启动时间: 2026-06-05 14:30:02
================================================================================
```

**代码实现**：
```python
def print_banner(system_name: str, version: str = "1.0.0"):
    sep = "=" * 78
    print(sep)
    print(f"{system_name:^78}")
    print(sep)
    print(f"采集程序版本: {version}")
    print(f"工作目录: {Path(__file__).resolve().parent}")
    print(f"启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(sep)
```

---

## 四、第 2 阶段：采集过程日志

### 阶段分隔
```
=== 开始采集 (滚动30天: 2026-05-06 ~ 2026-06-05) ===
--- Phase 1: 并行采集主数据 ---
```
- 开始标记：`=== {描述} ===`
- 阶段标记：`--- {阶段名} ---`

### API 调用日志
```
采集: winit.wh.pms.getWinitProducts (全量刷新)
采集: queryOutboundOrderList (2026-05-06 ~ 2026-06-05)
```
格式：`采集: {API名称} ({附加信息})`

### 分页/分批进度日志
```
  第1页: 42 条
  类型 OW0101: 21 条
  进度: 10/12
```
- 翻页：`{缩进}第{page_no}页: {count} 条`
- 按类型：`{缩进}类型 {type}: {count} 条`
- 进度：`{缩进}进度: {current}/{total}`

### 数据写入日志
```
  => 写入 51 条 (至 winit_products)
  => 写入 130 条 (至 winit_transaction_charges)
```
格式：`{缩进}=> 写入 {count} 条 (至 {table_name})`

### 错误日志
```
  商品列表 失败: (1364, "Field 'id' doesn't have a default value")
```
格式：`{缩进}{步骤名} 失败: {错误信息}`

### 采集完成汇总
```
=== 采集完成 ===
  winit_products                          : 51 条 (成功)
  winit_sku_list                          : 42 条 (成功)
  耗时: 31.3秒
  整体状态: 成功
```

### 缩进约定

| 层级 | 缩进 | 用途 |
|------|------|------|
| 0 | 无 | 阶段分隔、API 采集开始 |
| 1 | 2 空格 | 分页/分类/进度/写入/错误 |

---

## 五、第 3 阶段：结果汇总（Summary）

**输出示例**：
```
================================================================================
                               采集结果汇总
--------------------------------------------------------------------------------
表名                                              记录数               状态
--------------------------------------------------------------------------------
winit_products                                   51               成功
winit_sku_list                                   42               成功
--------------------------------------------------------------------------------
步骤总计
   成功步骤                          : 8
   失败步骤                          : 0
   总记录数                          : 291
   采集时间范围                        : 2026-05-06 ~ 2026-06-05
   开始时间                          : 2026-06-05 14:30:03
   结束时间                          : 2026-06-05 14:30:35
   总耗时                           : 31.3 秒
================================================================================
                             整体采集: 成功 ✓
================================================================================
日志文件: D:\PycharmProjects\datacollect\hicc_winit_api\output.log
```

**代码实现**：
```python
def print_summary(result: dict):
    sep = "=" * 78
    sep2 = "-" * 78
    print(sep)
    print("                               采集结果汇总")
    print(sep2)
    print(f"{'表名':50s}{'记录数':>10s}{'状态':>15s}")
    print(sep2)
    for step in result["steps"]:
        print(f"{step['table']:50s}{step['records']:>10d}{step['status']:>15s}")
    print(sep2)
    print("步骤总计")
    success_count = sum(1 for s in result["steps"] if s["status"] == "成功")
    fail_count = sum(1 for s in result["steps"] if s["status"] != "成功")
    total_records = sum(s["records"] for s in result["steps"])
    print(f"   成功步骤                          : {success_count}")
    print(f"   失败步骤                          : {fail_count}")
    print(f"   总记录数                          : {total_records}")
    print(f"   采集时间范围                        : {result['start_date']} ~ {result['end_date']}")
    print(f"   开始时间                          : {result['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   结束时间                          : {result['end_time'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   总耗时                           : {result['duration']:.1f} 秒")
    print(sep)
    status_text = "成功" if result["overall_success"] else "失败"
    status_icon = "✓" if result["overall_success"] else "✗"
    print(f"                             整体采集: {status_text} {status_icon}")
    print(sep)
```

### 分隔线规范

| 用途 | 字符 | 长度 | 代码 |
|------|------|------|------|
| 主分隔 | `=` | 78 | `"=" * 78` |
| 次分隔 | `-` | 78 | `"-" * 78` |

---

## 六、数据采集步骤编排模式

### 步骤包装器

```python
def _run_step(step_name: str, table_name: str, func: callable, *args) -> tuple:
    try:
        data = func(*args)
        count = len(data) if isinstance(data, (list, tuple)) else 0
        return data, {"name": step_name, "table": table_name, "records": count, "status": "成功"}
    except Exception as e:
        log(f"  {step_name} 失败: {e}")
        return [], {"name": step_name, "table": table_name, "records": 0, "status": f"失败: {e}"}
```

### 结果汇总结构

```python
result = {
    "start_time": datetime,
    "end_time": datetime,
    "duration": float,
    "start_date": str,
    "end_date": str,
    "steps": [{"name": str, "table": str, "records": int, "status": str}],
    "overall_success": bool,
    "errors": list[str],
}
```

---

## 七、日志文件管理

### 输出方式

```python
def main():
    log_file = Path(__file__).resolve().parent / "output.log"
    sys.stdout = TeeLogger(log_file)
    # ... 执行采集 ...
    sys.stdout.log_file.close()
    sys.stdout = sys.stdout.terminal
```

### 文件命名

| 场景 | 命名规则 | 示例 |
|------|---------|------|
| 固定日志 | `output.log` | `output.log` |
| 按日期轮转 | `output_{YYYYMMDD}.log` | `output_20260605.log` |
| 按时间轮转 | `output_{YYYYMMDD_HHMMSS}.log` | `output_20260605_143002.log` |

### 日志文件尾部

采集完成后输出日志文件路径，方便回溯：
```
================================================================================
日志文件: D:\PycharmProjects\datacollect\hicc_winit_api\output.log
```

---

## 八、跨平台复用清单

| 文件 | 需修改内容 |
|------|-----------|
| `main.py` | `print_banner()` 中的系统名称和 Client 类 |
| `collect_*.py` | API 名称、参数、分页逻辑 |
| `TeeLogger` | 无需修改，直接复用 |
| `_run_step` | 无需修改，直接复用 |
| `print_summary` | 无需修改，直接复用 |