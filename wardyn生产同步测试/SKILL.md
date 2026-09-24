---
name: "wardyn生产同步测试"
description: "将 wardyn 生产库 hiccpet_new_db 的商品主数据表全量覆盖同步到测试库（192.168.33.253，dev/test 共用）。用于让测试环境的公司 SKU、渠道变体、组合品、仓库映射与生产保持一致。Invoke when user asks to sync production data to test/dev, 生产同步到测试, 覆盖测试库数据, 让测试库与生产数据一致, 或本地下发计划/仓库库存页面数据与生产对不齐。"
---

# wardyn 生产 → 测试 数据同步

把生产库 `hiccpet_new_db` 指定表的数据「全量覆盖」到测试库，使 dev/test 环境的商品主数据与生产一致。

## 连接配置

```json
{
  "PROD": {"host": "47.84.91.117", "port": 3306, "user": "hiccpet-manage", "password": "HiccPet-mysql@2026"},
  "TEST": {"host": "192.168.33.253", "port": 3306, "user": "root", "password": "Hicc-mysql-2026"},
  "DB": "hiccpet_new_db"
}
```

连接参数支持环境变量覆盖：`PROD_MYSQL_HOST/PORT/USER/PASSWORD`、`TEST_MYSQL_HOST/PORT/USER/PASSWORD`、`SYNC_DB`。

## 同步策略

**全量覆盖**：先 `DELETE` 测试库整表，再批量 `INSERT` 生产数据（含主键 `id`），保证两库逐行一致。

- 只读生产库，绝不向生产写任何数据。
- 写入在单个事务内完成，任一步失败自动回滚。
- 执行前先校验两库列定义，测试库缺列则跳过并报错（避免结构漂移写坏数据）。

## 默认同步表

| 表 | 用途 |
|---|---|
| `product_skus` | 公司 SKU 主数据 |
| `product_skus_sales` | 渠道变体（下发主表） |
| `product_sku_bundles` | 组合品组件 |
| `product_skus_warehouse` | 仓库 SKU 映射 |

## 默认不同步的配置表（需要时用 `--tables` 显式指定）

| 表 | 不同步原因 |
|---|---|
| `sales_channel_shop` | 含 `api_config`（Shopify 凭据）与 `sync_enabled` 开关，覆盖会改动本地环境凭据/开关 |
| `mdm_bu_shops` | 店铺 → 经营单元码映射，属环境配置 |
| `warehouses` | 仓库定义，属环境配置 |

## 执行方式

脚本路径：`C:\Users\user\.agents\skills\wardyn生产同步测试\sync_prod_to_test.py`

### 1. 只读预览（默认，不修改任何数据）

```powershell
python C:\Users\user\.agents\skills\wardyn生产同步测试\sync_prod_to_test.py
```

### 2. 预览指定表

```powershell
python C:\Users\user\.agents\skills\wardyn生产同步测试\sync_prod_to_test.py --tables product_skus,product_skus_sales
```

### 3. 真正执行同步

```powershell
python C:\Users\user\.agents\skills\wardyn生产同步测试\sync_prod_to_test.py --execute
```

### 4. 一致性校验（只读，不修改数据）

比对生产与测试的「行数 + 全表内容 MD5」，逐表给出是否一致：

```powershell
python C:\Users\user\.agents\skills\wardyn生产同步测试\sync_prod_to_test.py --verify
```

### 5. 包含配置表（谨慎，会覆盖本地凭据/开关）

```powershell
python C:\Users\user\.agents\skills\wardyn生产同步测试\sync_prod_to_test.py --tables sales_channel_shop --execute
```

## 注意事项

1. **默认只读**：不加 `--execute` 不会写入，先预览确认行数无误再执行。
2. **生产只读**：脚本对生产库仅执行 `SELECT`，不存在误写生产的路径；执行前会校验生产与测试的 `@@hostname` 不同，解析到同一实例则直接中止。
3. **dev 与 test 共用同一个库**（`192.168.33.253`），同步会同时影响两者。
4. **同步会覆盖测试库的手工改动**（如手动补录的映射、手工编辑的 SKU），执行前请确认。
5. **同步结果 = 生产当前状态**：若生产侧有定时任务在改写这些表（如渠道同步任务），同步到的就是该任务运行后的最新快照，行数可能与历史预期不同。
6. 同步后如需让后端生效，重启本地后端进程即可（无缓存）。
7. 优先使用 `python` 命令，避免 Windows 上 `mysql` 客户端的认证插件问题。
