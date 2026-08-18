---
name: lazada接口数据采集技能
description: 在交互式命令提及该技能的时候触发
---

# Lazada数据采集技能使用说明

## 1. 功能概述

`LazadaCollector` 是一个统一的Lazada数据采集接口，用于采集Lazada平台的各种数据，包括：

- 订单列表数据
- 订单商品数据
- 广告组报告数据
- 广告活动列表数据
- 令牌刷新功能

## 2. 安装和配置

### 2.1 环境要求

- Python 3.6+
- 项目依赖已安装（通过 `pip install -r requirements.txt` 安装）

### 2.2 配置文件

确保以下配置文件已正确配置：

- `config/config.py`: 包含API密钥和国家配置
- `config/db_config.py`: 包含数据库连接配置

## 3. 使用方法

### 3.1 基本使用流程

1. 导入 `LazadaCollector` 类
2. 初始化采集器
3. 调用相应的采集方法

### 3.2 初始化采集器

```python
from lazada_collector import LazadaCollector

# 使用默认环境（test）
collector = LazadaCollector()

# 指定环境（test 或 prod）
collector = LazadaCollector(environment='prod')
```

### 3.3 采集订单和订单商品

```python
# 采集马来西亚最近7天的订单和商品信息
result = collector.collect_orders_and_items(
    country_code='my',
    days=7,
    limit=100,
    short_code='your_short_code'
)

print(f"订单采集结果: {result['order_result']}")
print(f"商品采集结果: {result['item_result']}")
```

### 3.4 仅采集订单列表

```python
# 仅采集订单列表
order_result = collector.collect_orders(
    country_code='my',
    days=7,
    limit=100,
    short_code='your_short_code'
)

print(f"订单采集结果: {order_result}")
```

### 3.5 仅采集订单商品

```python
# 仅采集订单商品
item_result = collector.collect_order_items(
    country_code='my',
    max_workers=20,
    short_code='your_short_code'
)

print(f"商品采集结果: {item_result}")
```

### 3.6 采集广告组报告

```python
# 采集广告组报告
ad_result = collector.collect_adgroup_report(
    country_code='my',
    start_date='2023-01-01',
    end_date='2023-01-07',
    short_code='your_short_code'
)

print(f"广告组报告采集结果: {ad_result}")
```

### 3.7 采集广告活动列表

```python
# 采集广告活动列表
campaign_result = collector.collect_campaign_list(
    country_code='my',
    short_code='your_short_code'
)

print(f"广告活动列表采集结果: {campaign_result}")
```

### 3.8 刷新令牌

```python
# 刷新所有国家的令牌
refreshed = collector.refresh_tokens(auto_refresh=True)
print(f"刷新结果: {refreshed}")

# 仅刷新指定国家的令牌
refreshed = collector.refresh_tokens(
    country_codes=['my', 'sg'],
    auto_refresh=True
)
print(f"刷新结果: {refreshed}")
```

## 4. 参数说明

### 4.1 公共参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `country_code` | str | 'my' | 国家代码 ('my', 'sg', 'th', 'vn', 'id', 'ph') |
| `short_code` | str | None | 短代码（必选） |
| `environment` | str | 'test' | 数据库环境 ('test' 或 'prod') |

### 4.2 订单采集参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `limit` | int | 100 | 每页订单数量限制 |
| `days` | int | 30 | 采集最近多少天的订单 |
| `update_after` | str | None | 更新时间起点（格式: YYYY-MM-DD） |
| `update_before` | str | None | 更新时间终点（格式: YYYY-MM-DD） |
| `created_after` | str | None | 创建时间起点（格式: YYYY-MM-DD） |
| `created_before` | str | None | 创建时间终点（格式: YYYY-MM-DD） |
| `status` | str | None | 订单状态 |

### 4.3 订单商品采集参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `order_ids` | list | None | 指定的订单ID列表，如果为None则从数据库获取 |
| `limit` | int | None | 从数据库获取的最大订单数 |
| `offset` | int | 0 | 从数据库获取的偏移量 |
| `max_workers` | int | 30 | 并行工作线程数 |

### 4.4 广告组报告采集参数

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `start_date` | str | 7天前 | 开始日期（格式: YYYY-MM-DD） |
| `end_date` | str | 今天 | 结束日期（格式: YYYY-MM-DD） |
| `campaign_ids` | list | None | 广告活动ID列表 |
| `adgroup_ids` | list | None | 广告组ID列表 |

## 5. 返回结果说明

### 5.1 订单采集返回结果

```python
{
    'api_total_count': int,  # API返回总记录数
    'mysql_total_count': int,  # 数据库保存记录数
    'is_consistent': bool,  # 数据是否一致
    'file_path': str  # 本地保存的文件路径
}
```

### 5.2 订单商品采集返回结果

```python
{
    'total_count': int,  # 总订单数
    'success_count': int,  # 成功采集的订单数
    'failed_count': int,  # 采集失败的订单数
    'item_count': int,  # 共获取商品数量
    'all_items': list,  # 所有商品数据
    'failed_orders': list  # 采集失败的订单列表
}
```

### 5.3 令牌刷新返回结果

```python
{
    'country_code1': 'refresh_token1',
    'country_code2': 'refresh_token2',
    # ...
}
```

## 6. 错误处理

所有方法在遇到错误时会抛出异常，建议使用try-except块进行捕获和处理：

```python
try:
    result = collector.collect_orders_and_items(
        country_code='my',
        days=7,
        short_code='your_short_code'
    )
    print("采集成功!")
except Exception as e:
    print(f"采集失败: {e}")
```

## 7. 最佳实践

1. **合理设置采集时间范围**：避免一次性采集过多数据，建议按天或周进行采集
2. **使用合适的并行线程数**：根据服务器性能和API限制，调整`max_workers`参数
3. **定期刷新令牌**：建议每天定时刷新令牌，确保采集任务正常执行
4. **监控采集结果**：定期检查采集结果的一致性，确保数据完整性
5. **使用测试环境进行调试**：在生产环境执行采集任务前，先在测试环境进行调试

## 8. 示例脚本

### 8.1 定期采集脚本

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
定期采集Lazada数据的脚本
"""

from lazada_collector import LazadaCollector
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename=f'lazada_collect_{datetime.now().strftime("%Y%m%d")}.log'
)
logger = logging.getLogger(__name__)

def main():
    logger.info("开始执行Lazada数据采集任务")
    
    try:
        # 初始化采集器
        collector = LazadaCollector(environment='prod')
        
        # 刷新令牌
        logger.info("开始刷新令牌")
        refreshed = collector.refresh_tokens(auto_refresh=True)
        logger.info(f"令牌刷新结果: {refreshed}")
        
        # 采集订单和商品数据
        logger.info("开始采集订单和商品数据")
        result = collector.collect_orders_and_items(
            country_code='my',
            days=1,  # 采集昨天的数据
            limit=100,
            short_code='your_short_code'
        )
        
        logger.info(f"订单采集结果: API={result['order_result']['api_total_count']}, DB={result['order_result']['mysql_total_count']}, 一致={result['order_result']['is_consistent']}")
        logger.info(f"商品采集结果: 总订单={result['item_result']['total_count']}, 成功={result['item_result']['success_count']}, 商品数={result['item_result']['item_count']}")
        
        logger.info("Lazada数据采集任务执行完成")
        
    except Exception as e:
        logger.error(f"Lazada数据采集任务执行失败: {e}", exc_info=True)

if __name__ == "__main__":
    main()
```

### 8.2 广告数据采集脚本

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
采集Lazada广告数据的脚本
"""

from lazada_collector import LazadaCollector
from datetime import datetime, timedelta

# 初始化采集器
collector = LazadaCollector(environment='prod')

# 设置日期范围（最近30天）
end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

# 采集广告活动列表
print("采集广告活动列表...")
campaign_result = collector.collect_campaign_list(
    country_code='my',
    short_code='your_short_code'
)
print(f"广告活动列表采集完成: {campaign_result}")

# 采集广告组报告
print("\n采集广告组报告...")
ad_result = collector.collect_adgroup_report(
    country_code='my',
    start_date=start_date,
    end_date=end_date,
    short_code='your_short_code'
)
print(f"广告组报告采集完成: {ad_result}")
```

## 9. 常见问题

### 9.1 令牌过期

**问题**：采集任务失败，提示"无法获取有效的访问令牌"

**解决方案**：
1. 检查令牌是否过期
2. 调用 `refresh_tokens()` 方法刷新令牌
3. 手动更新数据库中的令牌信息

### 9.2 数据不一致

**问题**：采集结果显示"数据不一致"

**解决方案**：
1. 检查数据库连接是否正常
2. 检查数据库表结构是否正确
3. 检查API返回数据是否完整
4. 查看日志文件，定位具体错误

### 9.3 采集速度慢

**解决方案**：
1. 增加并行线程数 `max_workers`
2. 减小每页数据量 `limit`
3. 缩短采集时间范围 `days`
4. 优化网络连接

## 10. 更新日志

### v1.0.0 (2026-03-06)

- 初始版本
- 支持订单和订单商品采集
- 支持广告组报告和广告活动列表采集
- 支持令牌刷新功能
- 提供统一的API接口

## 10. 表模型设计规则

Lazada采集系统的表模型设计遵循以下规则：

### 10.1 表名规则

- 采用 `lazada_` 前缀 + 功能描述的命名方式，例如：`lazada_orders_list`、`lazada_order_items`
- 使用复数形式表示表中存储多条记录
- 按功能模块分组命名，便于管理和维护

### 10.2 字段命名规则

- 采用下划线分隔的小写命名方式（snake_case）
- 字段名与API返回字段名保持一致，便于数据映射
- 关键字段使用语义化命名，清晰表达字段含义

### 10.3 数据类型选择

- **金额字段**：使用 `DECIMAL(10,2)` 类型，避免浮点精度问题
- **JSON数据**：使用 `JSON` 类型或 `TEXT` 类型存储复杂结构数据
- **时间字段**：
  - 原始API返回时间：使用 `VARCHAR` 类型存储，保留原始格式
  - 记录创建/更新时间：使用 `TIMESTAMP` 类型，自动管理时间戳
- **标识符**：使用 `VARCHAR` 类型，长度根据实际需要设置
- **文本数据**：
  - 短文本：使用 `VARCHAR` 类型，根据实际长度设置
  - 长文本：使用 `TEXT` 类型

### 10.4 索引设计

- 为常用查询字段创建索引，例如：`order_id`、`product_id`、`sku_id` 等
- 为主键创建自增ID
- 为关联字段创建索引，提高连接查询性能
- 为唯一性字段创建唯一索引

### 10.5 表结构组织

- 按功能模块分组创建表，例如：
  - 订单相关：`lazada_orders_list`、`lazada_order_items`
  - 广告相关：`lazada_adgroup_report`、`lazada_campaign_list`
  - 令牌相关：`lazada_access_token_responses`、`lazada_access_token_user_info`
- 关联表之间通过相同字段名建立关联
- 每个表包含 `created_at` 和 `updated_at` 字段，用于跟踪记录的创建和更新时间

### 10.6 注释规范

- 为每个表添加详细注释，说明表的用途和创建时间
- 为每个字段添加注释，说明字段的含义、数据来源和用途
- 为索引添加注释，说明索引的用途和优化目标

### 10.7 表模型示例

#### 订单表（lazada_orders_list）

| 字段类型 | 字段名 | 说明 |
|--------|------|------|
| VARCHAR(50) | order_id | 订单唯一标识符 |
| VARCHAR(50) | order_number | 订单编号 |
| VARCHAR(50) | created_at | 订单创建时间(字符串格式) |
| VARCHAR(50) | updated_at | 订单最后更新时间(字符串格式) |
| DECIMAL(10,2) | price | 订单价格 |
| JSON | recipient_info | 收件人信息(JSON对象) |
| JSON | statuses | 订单状态(JSON数组) |
| VARCHAR(50) | short_code | 入参short_code |
| TIMESTAMP | created_at_timestamp | 记录创建时间戳 |
| TIMESTAMP | updated_at_timestamp | 记录最后更新时间戳 |

#### 订单商品表（lazada_order_items）

| 字段类型 | 字段名 | 说明 |
|--------|------|------|
| VARCHAR(50) | order_id | 订单ID |
| VARCHAR(50) | order_item_id | 订单商品ID |
| VARCHAR(50) | product_id | 商品ID |
| VARCHAR(50) | sku_id | SKU ID |
| VARCHAR(255) | name | 商品名称 |
| DECIMAL(10,2) | item_price | 商品单价 |
| DECIMAL(10,2) | paid_price | 实际支付价格 |
| VARCHAR(50) | status | 订单商品状态 |
| VARCHAR(50) | short_code | 入参short_code |
| TIMESTAMP | created_timestamp | 记录创建时间 |
| TIMESTAMP | updated_timestamp | 记录更新时间 |

## 11. API数据结构与表模型映射关系

### 11.1 API接口与表的对应关系

| API接口 | 对应表名 | 描述 |
|--------|---------|------|
| /orders/get | lazada_orders_list | 订单列表数据 |
| /order/items/get | lazada_order_items | 订单商品详细信息 |
| /auth/token/refresh | lazada_access_token_responses | 访问令牌响应信息 |
| /auth/token/refresh | lazada_access_token_user_info | 访问令牌用户信息 |
| /adgroup/report/get | lazada_adgroup_report | 广告组报告数据 |
| /campaign/list/get | lazada_campaign_list | 广告活动列表数据 |

### 11.2 API响应数据映射规则

1. **直接映射**：API响应中的字段与表字段名一致时，直接映射保存
2. **类型转换**：根据表字段类型对API返回值进行转换
3. **JSON序列化**：复杂结构数据（如对象、数组）使用JSON序列化后保存到数据库
4. **默认值处理**：API返回值为空时，使用表字段的默认值
5. **额外字段添加**：
   - 添加`country_code`字段，标识数据所属国家
   - 添加`short_code`字段，标识数据来源
   - 添加记录创建/更新时间戳

### 11.3 订单API数据映射示例

#### API响应结构（简化）
```json
{
  "data": {
    "orders": [
      {
        "order_id": "212913540132422",
        "order_number": "212913540132422",
        "created_at": "2025-12-19T15:47:28+08:00",
        "updated_at": "2025-12-19T15:47:28+08:00",
        "price": 100.00,
        "voucher_platform": 10.00,
        "recipient_info": {
          "name": "John Doe",
          "phone": "1234567890"
        },
        "statuses": ["pending"]
      }
    ]
  }
}
```

#### 数据库表映射

| API字段 | 表字段 | 类型转换 |
|--------|--------|----------|
| order_id | order_id | 直接映射 |
| order_number | order_number | 直接映射 |
| created_at | created_at | 直接映射（字符串） |
| updated_at | updated_at | 直接映射（字符串） |
| price | price | 直接映射（DECIMAL） |
| voucher_platform | voucher_platform | 直接映射（DECIMAL） |
| recipient_info | recipient_info | JSON序列化 |
| statuses | statuses | JSON序列化 |
| - | country_code | 手动添加（如：'my'） |
| - | short_code | 手动添加（如：'MY4NA1T7CK'） |
| - | created_at_timestamp | 自动生成 |
| - | updated_at_timestamp | 自动生成 |

### 11.4 订单商品API数据映射示例

#### API响应结构（简化）
```json
{
  "data": [
    {
      "order_id": "212913540132422",
      "order_item_id": "212913540132422_01",
      "product_id": "300163725140",
      "sku_id": "30016372514001",
      "name": "Product Name",
      "item_price": 50.00,
      "paid_price": 45.00,
      "status": "pending",
      "shop_id": "123456"
    }
  ]
}
```

#### 数据库表映射

| API字段 | 表字段 | 类型转换 |
|--------|--------|----------|
| order_id | order_id | 直接映射 |
| order_item_id | order_item_id | 直接映射 |
| product_id | product_id | 直接映射 |
| sku_id | sku_id | 直接映射 |
| name | name | 直接映射 |
| item_price | item_price | 直接映射（DECIMAL） |
| paid_price | paid_price | 直接映射（DECIMAL） |
| status | status | 直接映射 |
| shop_id | shop_id | 直接映射 |
| - | country_code | 手动添加（如：'my'） |
| - | short_code | 手动添加（如：'MY4NA1T7CK'） |
| - | created_timestamp | 自动生成 |
| - | updated_timestamp | 自动生成 |

### 11.5 数据转换处理

1. **金额转换**：
   - API返回值：`100.0`（float类型）
   - 表字段类型：`DECIMAL(10,2)`
   - 转换方式：直接转换，保留两位小数

2. **JSON序列化**：
   - API返回值：`{"name": "John Doe"}`（对象类型）
   - 表字段类型：`JSON`或`TEXT`
   - 转换方式：`json.dumps()`序列化后保存

3. **布尔值处理**：
   - API返回值：`true`（布尔类型）
   - 表字段类型：`BOOLEAN`或`TINYINT`
   - 转换方式：直接映射，数据库自动处理

4. **时间处理**：
   - API返回值：`2025-12-19T15:47:28+08:00`（字符串类型）
   - 表字段类型：`VARCHAR`（原始时间）或`TIMESTAMP`（记录时间）
   - 转换方式：原始时间直接保存，记录时间自动生成

### 11.6 数据一致性保障

1. **批量操作**：使用批量插入/更新提高性能和一致性
2. **事务管理**：单个订单的相关操作（如删除旧记录、插入新记录）在同一事务中完成
3. **数据校验**：比较API返回记录数与数据库保存记录数，确保数据一致
4. **日志记录**：保存采集日志，便于问题追踪和数据恢复

## 12. 联系方式

如有问题或建议，请联系开发团队。