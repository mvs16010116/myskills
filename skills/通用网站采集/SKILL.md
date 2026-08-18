---
name: 通用网站采集
description: 通用网站采集技能
---

# 通用网站采集技能文档

## 1. 采集系统架构

### 1.1 系统概述
网站采集系统用于自动化从目标网站获取数据，并将数据存储到数据库中，以便后续分析和使用。系统采用模块化设计，便于扩展和维护。

### 1.2 核心组件

| 组件 | 功能 |
|------|------|
| API层 | 负责与目标网站进行交互，发送请求获取数据 |
| 数据处理层 | 负责解析和处理获取到的数据 |
| 数据库层 | 负责数据的存储和管理 |
| 主程序 | 负责协调各个组件，控制采集流程 |

## 2. 目录结构设计

### 2.1 标准目录结构

```
websites/
└── site_name/          # 网站名称，如yplexpress
    ├── __pycache__/    # Python编译缓存
    ├── api/            # API相关代码
    │   ├── __pycache__/
    │   └── site_name_api.py  # 网站API调用实现
    ├── db/             # 数据库相关代码
    │   ├── __pycache__/
    │   └── site_name_mysql_db.py  # 数据库操作实现
    ├── docs/           # 文档目录
    │   ├── 接口文档.md    # 目标网站接口文档
    │   └── 采集技能文档.md  # 采集系统文档
    ├── models/         # 数据模型目录
    ├── sql/            # SQL脚本目录
    └── main.py         # 主程序入口
```

### 2.2 目录说明

- **api/**：存放与目标网站API交互的代码，包括登录、数据获取等功能
- **db/**：存放数据库操作相关代码，包括表创建、数据插入、更新等功能
- **docs/**：存放文档，包括接口文档和采集系统文档
- **models/**：存放数据模型，定义数据结构
- **sql/**：存放SQL脚本，如建表语句等
- **main.py**：主程序入口，控制整个采集流程

## 3. 采集流程设计

### 3.1 基本采集流程

1. **初始化配置**：加载配置文件，获取网站URL、账号密码等配置信息
2. **登录验证**：使用配置的账号密码登录目标网站，获取认证信息（如token）
3. **获取订单列表**：调用订单列表API，获取所有符合条件的订单
4. **并行采集订单详情**：使用多线程并行采集每个订单的详细信息
5. **数据存储**：将采集到的数据存储到数据库中
6. **完成采集**：输出采集结果，包括成功和失败的订单数量

### 3.2 详细流程图

```
开始
  │
  ▼
初始化配置
  │
  ▼
登录目标网站
  │
  ├─成功───┐
  │        ▼
  └─失败───┘
获取订单列表
  │
  ├─成功───┐
  │        ▼
  └─失败───┘
并行采集订单详情
  │
  ▼
数据存储到数据库
  │
  ▼
输出采集结果
  │
  ▼
结束
```

## 4. API调用设计

### 4.1 核心API设计

#### 4.1.1 登录API

**功能**：登录目标网站（如果有，获取认证token）

**实现要点**：
- 使用session保持会话
- 处理登录失败的重试逻辑
- 保存认证信息（如token）到请求头

**示例代码**：
```python
def login(self, username, password):
    # 构造登录请求
    # 发送登录请求
    # 处理登录响应
    # 更新请求头，添加token
    # 返回登录结果
```

#### 4.1.2 订单列表API

**功能**：获取订单列表，支持分页和筛选

**实现要点**：
- 自动处理分页
- 支持按状态、时间等条件筛选
- 重试机制

**示例代码**：
```python
def get_order_list(self, status, page_size):
    # 初始化订单列表
    # 循环处理分页
    # 发送请求获取订单列表
    # 处理响应数据
    # 合并订单列表
    # 返回完整订单列表
```

#### 4.1.3 订单详情API

**功能**：获取单个订单的详细信息

**实现要点**：
- 根据订单ID获取详情
- 重试机制
- 数据解析和处理

**示例代码**：
```python
def get_order_detail(self, order_id):
    # 构造请求URL
    # 发送请求获取订单详情
    # 处理响应数据
    # 返回订单详情
```

### 4.2 API调用规范

1. **请求头设计**：包含认证信息、内容类型等
2. **请求参数处理**：根据API要求格式化请求参数
3. **响应处理**：检查响应状态码，解析响应数据
4. **重试机制**：对失败的请求进行重试
5. **请求频率控制**：添加适当的延迟，避免请求过于频繁

## 5. 数据库设计

### 5.1 设计原则

1. **数据完整性**：确保数据的准确性和完整性
2. **可扩展性**：便于后续添加新字段和表
3. **性能优化**：考虑查询效率，合理设计索引
4. **数据类型合理**：根据数据特点选择合适的数据类型

### 5.2 表结构设计

#### 5.2.1 订单列表表

**功能**：存储订单的基本信息

**设计要点**：
- 使用唯一标识符作为主键
- 包含订单的基本属性
- 合理设计数据类型

**示例表结构**：

```sql
CREATE TABLE IF NOT EXISTS site_name_order_list (
    waybill_id VARCHAR(255) PRIMARY KEY COMMENT '运单ID',
    waybill_number VARCHAR(255) DEFAULT '' COMMENT '运单号',
    order_no VARCHAR(255) DEFAULT '' COMMENT '订单号',
    receive_name VARCHAR(255) DEFAULT '' COMMENT '收件人',
    receive_country VARCHAR(255) DEFAULT '' COMMENT '收件国家',
    receive_postal_code VARCHAR(255) DEFAULT '' COMMENT '邮编',
    pcs INT DEFAULT 0 COMMENT '件数',
    freight DECIMAL(10,2) DEFAULT 0.00 COMMENT '运费',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='网站订单列表表';
```

#### 5.2.2 订单详情表

**功能**：存储订单的详细信息

**设计要点**：
- 对于复杂数据，使用JSON格式存储
- 包含订单的所有详细信息

**示例表结构**：

```sql
CREATE TABLE site_name_order_detail (
    waybill_id VARCHAR(255) PRIMARY KEY COMMENT '运单ID',
    waybill LONGTEXT COMMENT '运单信息',
    box_list LONGTEXT COMMENT '箱子列表',
    box_detail_list LONGTEXT COMMENT '箱子详情列表',
    waybill_fee_list LONGTEXT COMMENT '运单费用列表',
    waybill_route_list LONGTEXT COMMENT '运单路由列表',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '记录创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '记录更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='网站订单详情表';
```

## 6. 数据更新策略

### 6.1 全量更新

**适用场景**：
- 数据量较小
- 需要确保数据完整性
- 定期数据同步

**实现方式**：
1. 获取所有数据
2. 删除旧数据
3. 插入新数据

**示例代码**：
```python
def insert_order_list(self, order_list):
    # 准备数据
    # 批量删除旧数据
    # 批量插入新数据
    # 返回插入结果
```

### 6.2 增量更新

**适用场景**：
- 数据量较大
- 数据更新频繁
- 只需要更新变化的数据

**实现方式**：
1. 根据时间戳或版本号获取增量数据
2. 更新或插入数据

## 7. 错误处理机制

### 7.1 重试机制

**设计要点**：
- 对API调用失败进行重试
- 设置合理的重试次数（如3次）
- 重试前添加延迟（如5秒）

**示例代码**：
```python
def get_order_list(self):
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            # 发送请求获取数据
            return data
        except Exception as e:
            if attempt < max_retries:
                time.sleep(5)  # 重试前延迟5秒
    return None
```

### 7.2 异常处理

**设计要点**：
- 捕获和记录异常
- 对不同类型的异常进行不同的处理
- 确保系统不会因单个请求失败而崩溃

**示例代码**：
```python
def collect_order_details(self, order):
    try:
        # 采集订单详情
    except Exception as e:
        # 记录失败信息
        print(f"订单处理异常: {e}")
```

## 8. 性能优化

### 8.1 并行采集

**设计要点**：
- 使用多线程或多进程并行采集数据
- 设置合理的并发数，避免请求过于频繁
- 对并行任务进行管理和监控

**示例代码**：
```python
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(collect_order_details, order) for order in order_list]
    for future in concurrent.futures.as_completed(futures):
        future.result()
```

### 8.2 请求频率控制

**设计要点**：
- 在请求之间添加适当的延迟
- 遵循目标网站的robots.txt规则
- 避免对目标网站造成过大压力

**示例代码**：
```python
time.sleep(0.5)  # 为了避免请求过于频繁，添加适当的延迟
```

### 8.3 批量操作

**设计要点**：
- 批量获取数据
- 批量插入数据到数据库
- 减少数据库连接次数

**示例代码**：
```python
def execute_many(self, sql, data_list):
    # 批量执行SQL语句
    cursor = self.connection.cursor()
    cursor.executemany(sql, data_list)
    self.connection.commit()
    cursor.close()
    return True
```

## 9. 监控与日志

### 9.1 日志设计

**设计要点**：
- 记录关键操作和状态
- 记录异常信息
- 便于问题排查和分析

**示例代码**：
```python
print(f"✓ 运单 {waybill_id} 详情获取成功")
print(f"✗ 运单 {waybill_id} 详情获取失败")
print(f"✗ 运单 {waybill_id} 处理异常: {e}")
```

### 9.2 运行统计

**设计要点**：
- 统计采集时间
- 统计成功和失败的订单数量
- 统计数据量大小

**示例代码**：
```python
start_time = datetime.now()
# 采集过程
end_time = datetime.now()
run_time = end_time - start_time
print(f"运行时长: {run_time}")
print(f"成功采集运单详情: {success_count} 条")
print(f"处理失败运单: {failed_count} 个")
```

## 10. 扩展性设计

### 10.1 模块化设计

**设计要点**：
- 将不同功能封装到不同模块中
- 模块之间通过接口进行交互
- 便于添加新功能和修改现有功能

### 10.2 配置驱动

**设计要点**：
- 将配置信息（如URL、账号密码等）存储到配置文件中
- 通过配置文件控制采集行为
- 便于修改配置，无需修改代码

**示例配置**：
```json
{
    "base_url": "https://oms.yplogistics.com/server",
    "username": "HICCTECH",
    "password": "hicc1234",
    "page_size": 50,
    "max_workers": 5
}
```

## 11. 最佳实践

### 11.1 代码规范

- 遵循PEP 8代码规范
- 使用有意义的变量和函数名
- 添加适当的注释
- 保持代码简洁和可读性

### 11.2 安全性

- 保护敏感信息（如账号密码）
- 使用HTTPS协议
- 避免存储明文密码

### 11.3 可维护性

- 定期更新代码和依赖
- 保持代码结构清晰
- 编写文档和注释
- 进行代码审查

## 12. 总结

本文档介绍了通用网站采集系统的设计和实现，包括系统架构、目录结构、采集流程、API设计、数据库设计、数据更新策略、错误处理、性能优化、监控与日志、扩展性设计等方面。

通过遵循本文档的设计原则和最佳实践，可以构建一个高效、可靠、可扩展的网站采集系统，用于自动化从目标网站获取数据，并将数据存储到数据库中。

这个系统设计具有以下优点：

1. **模块化设计**：便于扩展和维护
2. **并行采集**：提高采集效率
3. **重试机制**：提高系统可靠性
4. **批量操作**：优化性能
5. **完整的错误处理**：确保系统稳定运行
6. **详细的日志和监控**：便于问题排查和分析
7. **配置驱动**：便于修改和扩展

通过不断优化和改进，可以进一步提高系统的性能和可靠性，满足不同场景下的采集需求。