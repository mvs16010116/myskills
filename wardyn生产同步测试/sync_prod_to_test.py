#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wardyn 生产 → 测试 数据同步脚本

将生产库 hiccpet_new_db 指定表的数据「全量覆盖」到测试库（dev/test 共用 192.168.33.253）。

写入策略：先 DELETE 测试库整表，再批量 INSERT 生产数据（含主键 id），保证两库数据完全一致。

安全约束：
  1. 默认 dry-run（只读预览），必须显式加 --execute 才会写入测试库。
  2. 只读生产库，绝不向生产库写入任何数据。
  3. 写入在单个事务内完成，失败自动回滚。

用法：
  # 预览（只读，不改数据）
  python sync_prod_to_test.py

  # 预览指定表
  python sync_prod_to_test.py --tables product_skus,product_skus_sales

  # 真正执行同步
  python sync_prod_to_test.py --execute
"""

import argparse
import hashlib
import os
import re
import sys

try:
    import pymysql
except ImportError:
    print("错误：未安装 pymysql，请先执行 pip install pymysql")
    sys.exit(1)

# 生产库连接配置（只读）
PROD_CONFIG = {
    "host": os.environ.get("PROD_MYSQL_HOST", "47.84.91.117"),
    "port": int(os.environ.get("PROD_MYSQL_PORT", 3306)),
    "user": os.environ.get("PROD_MYSQL_USER", "hiccpet-manage"),
    "password": os.environ.get("PROD_MYSQL_PASSWORD", "HiccPet-mysql@2026"),
}

# 测试库连接配置（可写，dev/test 共用）
TEST_CONFIG = {
    "host": os.environ.get("TEST_MYSQL_HOST", "192.168.33.253"),
    "port": int(os.environ.get("TEST_MYSQL_PORT", 3306)),
    "user": os.environ.get("TEST_MYSQL_USER", "root"),
    "password": os.environ.get("TEST_MYSQL_PASSWORD", "Hicc-mysql-2026"),
}

TARGET_DB = os.environ.get("SYNC_DB", "hiccpet_new_db")

# 默认同步表：Shopify 库存下发 / 仓库库存功能直接依赖的商品主数据表
DEFAULT_TABLES = [
    "product_skus",           # 公司 SKU 主数据
    "product_skus_sales",     # 渠道变体（下发主表）
    "product_sku_bundles",    # 组合品组件
    "product_skus_warehouse", # 仓库 SKU 映射
]

# 配置类表（含环境专属凭据或环境开关），默认不同步，需要时用 --tables 显式指定
CONFIG_TABLES = [
    "sales_channel_shop",  # 含 api_config（Shopify 凭据）与 sync_enabled 开关
    "mdm_bu_shops",        # 店铺 → 经营单元码映射
    "warehouses",          # 仓库定义
]

TABLE_NAME_PATTERN = re.compile(r"^[A-Za-z0-9_]+$")


def connect(config):
    """建立 MySQL 连接（自动提交关闭，便于事务控制）。"""
    return pymysql.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=TARGET_DB,
        charset="utf8mb4",
        autocommit=False,
        cursorclass=pymysql.cursors.Cursor,
    )


def get_columns(conn, table):
    """读取表的列名（按定义顺序）。"""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT COLUMN_NAME FROM information_schema.COLUMNS "
            "WHERE TABLE_SCHEMA=%s AND TABLE_NAME=%s ORDER BY ORDINAL_POSITION",
            (TARGET_DB, table),
        )
        return [row[0] for row in cur.fetchall()]


def count_rows(conn, table):
    """统计表行数。"""
    with conn.cursor() as cur:
        cur.execute(f"SELECT COUNT(*) FROM `{table}`")
        return cur.fetchone()[0]


def table_fingerprint(conn, table):
    """计算全表指纹：返回 (行数, 内容 MD5)。

    按主键排序后逐行拼接所有列值再 MD5，可同时检出「行数不一致」与「行内容不一致」。
    """
    cols = get_columns(conn, table)
    order_col = "id" if "id" in cols else cols[0]
    digest = hashlib.md5()
    count = 0
    with conn.cursor() as cur:
        cur.execute(f"SELECT `{'`, `'.join(cols)}` FROM `{table}` ORDER BY `{order_col}`")
        for row in cur:
            digest.update(repr(row).encode("utf-8"))
            count += 1
    return count, digest.hexdigest()


def sync_table(prod_conn, test_conn, table, execute, batch_size):
    """同步单张表，返回结果字典。"""
    result = {"table": table, "prod": 0, "test_before": 0, "test_after": 0,
              "deleted": 0, "inserted": 0, "skipped": False, "error": None}

    prod_cols = get_columns(prod_conn, table)
    if not prod_cols:
        result["error"] = f"生产库不存在该表或表无列定义"
        return result

    test_cols = get_columns(test_conn, table)
    if not test_cols:
        result["error"] = f"测试库不存在该表"
        return result

    missing = [c for c in prod_cols if c not in test_cols]
    if missing:
        result["error"] = f"测试库缺少列: {', '.join(missing)}（表结构不一致，需先对齐 DDL）"
        return result

    result["prod"] = count_rows(prod_conn, table)
    result["test_before"] = count_rows(test_conn, table)

    if not execute:
        result["skipped"] = True
        return result

    with prod_conn.cursor() as pcur:
        pcur.execute(f"SELECT `{'`, `'.join(prod_cols)}` FROM `{table}`")
        rows = pcur.fetchall()

    placeholders = ", ".join(["%s"] * len(prod_cols))
    insert_sql = (
        f"INSERT INTO `{table}` (`{'`, `'.join(prod_cols)}`) VALUES ({placeholders})"
    )

    try:
        test_conn.begin()
        with test_conn.cursor() as tcur:
            tcur.execute(f"DELETE FROM `{table}`")
            result["deleted"] = tcur.rowcount
            for i in range(0, len(rows), batch_size):
                tcur.executemany(insert_sql, rows[i:i + batch_size])
                result["inserted"] += len(rows[i:i + batch_size])
        test_conn.commit()
    except Exception as exc:  # noqa: BLE001 - 事务失败必须回滚后向上报错
        test_conn.rollback()
        result["error"] = f"写入失败已回滚: {exc}"
        return result

    result["test_after"] = count_rows(test_conn, table)
    return result


def main():
    parser = argparse.ArgumentParser(description="wardyn 生产 → 测试 数据同步工具")
    parser.add_argument(
        "--tables",
        default=",".join(DEFAULT_TABLES),
        help=f"待同步表名，逗号分隔（默认: {','.join(DEFAULT_TABLES)}）",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="真正执行写入（不加该参数为只读预览，不修改任何数据）",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="仅做一致性校验：比对生产与测试的行数与全表内容 MD5，不修改任何数据",
    )
    parser.add_argument("--batch-size", type=int, default=500, help="批量插入行数（默认 500）")
    args = parser.parse_args()

    tables = [t.strip() for t in args.tables.split(",") if t.strip()]
    for t in tables:
        if not TABLE_NAME_PATTERN.match(t):
            print(f"错误：非法表名 {t!r}")
            sys.exit(1)

    print(f"目标库: {TARGET_DB}")
    print(f"生产库: {PROD_CONFIG['host']}:{PROD_CONFIG['port']}（只读）")
    print(f"测试库: {TEST_CONFIG['host']}:{TEST_CONFIG['port']}（写入目标）")
    print(f"同步表: {', '.join(tables)}")
    if args.verify:
        mode = "一致性校验（只读）"
    elif args.execute:
        mode = "执行写入（全量覆盖）"
    else:
        mode = "只读预览（不修改数据）"
    print(f"模式  : {mode}")
    print("-" * 70)

    prod_conn = connect(PROD_CONFIG)
    test_conn = connect(TEST_CONFIG)
    try:
        # 安全护栏：确认生产与测试解析到不同 MySQL 实例，避免配置写错导致误写生产
        with prod_conn.cursor() as cur:
            cur.execute("SELECT @@hostname")
            prod_hostname = cur.fetchone()[0]
        with test_conn.cursor() as cur:
            cur.execute("SELECT @@hostname")
            test_hostname = cur.fetchone()[0]
        if prod_hostname == test_hostname:
            print(f"错误：生产与测试解析到同一 MySQL 实例（{prod_hostname}），已中止以防误写生产。")
            sys.exit(1)

        # 宽松 sql_mode，容忍生产数据中的零值日期等历史数据
        with test_conn.cursor() as cur:
            cur.execute("SET SESSION sql_mode=''")
            cur.execute("SET SESSION FOREIGN_KEY_CHECKS=0")

        if args.verify:
            mismatched = []
            for table in tables:
                pc, ph = table_fingerprint(prod_conn, table)
                tc, th = table_fingerprint(test_conn, table)
                if pc == tc and ph == th:
                    print(f"[一致] {table}: {pc} 行, md5={ph[:12]}")
                else:
                    mismatched.append(table)
                    print(f"[不一致] {table}: 生产 {pc} 行(md5={ph[:12]}) vs 测试 {tc} 行(md5={th[:12]})")
            print("-" * 70)
            if mismatched:
                print(f"存在 {len(mismatched)} 张表不一致: {', '.join(mismatched)}")
                sys.exit(1)
            print("全部表生产与测试完全一致。")
            return

        results = []
        for table in tables:
            res = sync_table(prod_conn, test_conn, table, args.execute, args.batch_size)
            results.append(res)
            if res["error"]:
                print(f"[失败] {table}: {res['error']}")
            elif res["skipped"]:
                print(f"[预览] {table}: 生产 {res['prod']} 行 → 测试 {res['test_before']} 行（待覆盖）")
            else:
                print(f"[完成] {table}: 删除 {res['deleted']} 行, 插入 {res['inserted']} 行, "
                      f"测试 {res['test_before']} → {res['test_after']} 行")

        print("-" * 70)
        failed = [r for r in results if r["error"]]
        if failed:
            print("存在失败项，请逐条处理：")
            for r in failed:
                print(f"  - {r['table']}: {r['error']}")
            sys.exit(1)

        if not args.execute:
            print("预览完成。确认无误后加 --execute 执行写入。")
        else:
            print("同步完成。")
    finally:
        prod_conn.close()
        test_conn.close()


if __name__ == "__main__":
    main()
