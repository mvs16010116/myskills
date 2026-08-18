#!/usr/bin/env python3
"""
FineBI 指标数据查询模块
通过 API 接口查询指标数据，支持搜索指标/维度、查询数据、分页等
认证方式：HMAC-SHA256 摘要签名认证

使用示例：
    from query_indicator import IndicatorAPI, Secret

    api = IndicatorAPI(
        server_url="http://bi.hiccpet.net",
        secret=Secret(username="rank", secret_key="你的secret_key"),
    )

    # 1. 搜索指标
    indicators = api.search_indicators("销量")
    for ind in indicators:
        print(f"{ind['name']} (ID: {ind['id']})")

    # 2. 查询指标总数据（无维度）
    result = api.query_data(metrics=["指标ID"])
    print(f"总销量: {result['total']}")

    # 3. 按维度分组查询
    result = api.query_data(
        metrics=["指标ID"],
        dimensions=["维度ID"],
        page_size=100,
    )
    for row in result["rows"]:
        print(f"{row[0]} | {row[1]}")

    # 4. 按月汇总
    summary = api.query_data_summary(
        metrics=["指标ID"],
        dimensions=["日期维度ID"],
    )
    for month, total in summary["monthly"].items():
        print(f"{month}: {total:,.0f}")
"""

import hmac
import hashlib
import base64
import re
import uuid
import time
import json
import urllib.request
from dataclasses import dataclass
from typing import Optional
from collections import defaultdict


@dataclass
class Secret:
    """API 认证密钥"""
    username: str
    secret_key: str


class IndicatorAPI:
    """FineBI 指标中心 API 客户端"""

    # API 路径前缀
    BASE_PATH = "/decision/api/dc/v1"
    # 搜索端点
    SEARCH_URL = "/indicator/search"
    # 数据查询端点
    QUERY_URL = "/indicator/query/data"
    # 查询 SQL 端点
    SQL_URL = "/indicator/query/sql"

    def __init__(self, server_url: str, secret: Secret):
        """
        初始化 API 客户端

        Args:
            server_url: FineBI 服务器地址，如 "http://bi.hiccpet.net"
            secret: 认证密钥，包含 username 和 secret_key
        """
        self.server_url = server_url.rstrip("/")
        self.secret = secret

    # ------------------------------------------------------------------
    # 认证
    # ------------------------------------------------------------------

    def _build_auth_header(self) -> str:
        """生成 HMAC-SHA256 签名认证头"""
        nonce = str(uuid.uuid4())
        timestamp = str(int(time.time() * 1000))
        string_to_sign = self.secret.username + nonce + timestamp
        signature = base64.b64encode(
            hmac.new(
                self.secret.secret_key.encode(),
                string_to_sign.encode(),
                hashlib.sha256,
            ).digest()
        ).decode()
        return (
            f"HMAC-SHA256 signature={signature},"
            f"identity={self.secret.username},"
            f"nonce={nonce},"
            f"timestamp={timestamp}"
        )

    def _request(self, endpoint: str, body: dict) -> dict:
        """发送 POST 请求到 API"""
        url = f"{self.server_url}{self.BASE_PATH}{endpoint}"
        data = json.dumps(body).encode()
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Authorization": self._build_auth_header(),
                "Content-Type": "application/json",
            },
        )
        try:
            resp = urllib.request.urlopen(req, timeout=30)
            return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()
            try:
                return json.loads(error_body)
            except json.JSONDecodeError:
                return {"success": False, "errorCode": str(e.code), "errorMsg": error_body[:200]}
        except Exception as e:
            return {"success": False, "errorCode": "EXCEPTION", "errorMsg": str(e)}

    def _get_request(self, endpoint: str) -> dict:
        """发送 GET 请求到 API"""
        url = f"{self.server_url}{self.BASE_PATH}{endpoint}"
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": self._build_auth_header(),
                "Content-Type": "application/json",
            },
        )
        try:
            resp = urllib.request.urlopen(req, timeout=30)
            return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()
            try:
                return json.loads(error_body)
            except json.JSONDecodeError:
                return {"success": False, "errorCode": str(e.code), "errorMsg": error_body[:200]}
        except Exception as e:
            return {"success": False, "errorCode": "EXCEPTION", "errorMsg": str(e)}

    # ------------------------------------------------------------------
    # 搜索
    # ------------------------------------------------------------------

    def search_indicators(
        self,
        keyword: str,
        page_index: int = 1,
        page_size: int = 50,
        privilege: str = "view",
    ) -> list:
        """
        搜索指标

        Args:
            keyword: 搜索关键词，如 "销量"、"金额"
            page_index: 页码，从 1 开始
            page_size: 每页条数
            privilege: 权限类型，view(元数据) 或 use(使用权限)

        Returns:
            指标列表，每条包含 id, name, position, type, engineType 等字段
        """
        body = {
            "keyword": keyword,
            "pageIndex": page_index,
            "pageSize": page_size,
            "force": True,
            "privilege": privilege,
            "filter": {"itemTypes": [65]},  # 65 = 指标
        }
        result = self._request(self.SEARCH_URL, body)
        if result.get("success"):
            return result.get("data", {}).get("items", [])
        return []

    def search_dimensions(
        self,
        keyword: str,
        page_index: int = 1,
        page_size: int = 50,
        privilege: str = "view",
    ) -> list:
        """
        搜索维度

        Args:
            keyword: 搜索关键词，如 "日期"、"地区"
            page_index: 页码，从 1 开始
            page_size: 每页条数
            privilege: 权限类型

        Returns:
            维度列表，每条包含 id, name, position 等字段
        """
        body = {
            "keyword": keyword,
            "pageIndex": page_index,
            "pageSize": page_size,
            "force": True,
            "privilege": privilege,
            "filter": {"itemTypes": [66]},  # 66 = 维度
        }
        result = self._request(self.SEARCH_URL, body)
        if result.get("success"):
            return result.get("data", {}).get("items", [])
        return []

    # ------------------------------------------------------------------
    # 语义信息接口（查看指标/维度属性、血缘、关系）
    # ------------------------------------------------------------------

    def get_metric_info(self, metric_id: str) -> dict:
        """
        查看指标属性（含计算口径、公式、标签等）

        GET /api/dc/v1/indicator/metric/{metricId}/info

        Args:
            metric_id: 指标 ID

        Returns:
            {
                "success": bool,
                "data": {
                    "id": 指标ID,
                    "name": 指标名称,
                    "creator": 创建者,
                    "createTime": 创建时间,
                    "type": 数据类型(16=文本,32=数值,48=时间),
                    "caliber": {"formula": 公式, "fields": [...], ...},
                    "tags": [...],
                    "validStatus": "VALID"/"INVALID",
                    ...
                }
            }
        """
        result = self._get_request(f"/indicator/metric/{metric_id}/info")
        return {
            "success": result.get("success", False),
            "data": result.get("data"),
            "raw": result,
        }

    def get_metric_consanguinity(self, metric_id: str) -> dict:
        """
        查看指标血缘关系（上下游依赖树）

        GET /api/dc/v1/indicator/metric/{metricId}/consanguinity

        Args:
            metric_id: 指标 ID

        Returns:
            {
                "success": bool,
                "nodeInfo": {节点ID: 节点属性, ...},  # 所有节点属性
                "parentEdges": [{"parent": 父节点ID, "child": 子节点ID}, ...],  # 上游边
                "childEdges": [{"parent": 父节点ID, "child": 子节点ID}, ...],  # 下游边
            }
        """
        result = self._get_request(f"/indicator/metric/{metric_id}/consanguinity")
        if result.get("success"):
            data = result.get("data", {})
            # 将 nodeInfo 从 dict 转为列表，方便遍历
            node_info = data.get("nodeInfo", {})
            node_list = []
            for node_id, attrs in node_info.items():
                attrs["_id"] = node_id
                node_list.append(attrs)
            return {
                "success": True,
                "node_info": node_info,
                "node_list": node_list,
                "parent_edges": data.get("parentEdges", []),
                "child_edges": data.get("childEdges", []),
                "raw": result,
            }
        return {"success": False, "raw": result}

    def get_metric_relate_dimensions(self, metric_id: str) -> dict:
        """
        查看指标关联的维度（可用哪些维度分析该指标）

        GET /api/dc/v1/indicator/metric/{metricId}/relate/dimension

        Args:
            metric_id: 指标 ID

        Returns:
            {
                "success": bool,
                "dimensions": [
                    {"id": 维度ID, "name": 维度名, "type": 数据类型, "description": 描述},
                    ...
                ]
            }
        """
        result = self._get_request(f"/indicator/metric/{metric_id}/relate/dimension")
        if result.get("success"):
            return {
                "success": True,
                "dimensions": result.get("data", []),
                "raw": result,
            }
        return {"success": False, "dimensions": [], "raw": result}

    def get_dimension_info(self, dimension_id: str) -> dict:
        """
        查看维度属性

        GET /api/dc/v1/indicator/dimension/{dimensionId}/info

        Args:
            dimension_id: 维度 ID

        Returns:
            {
                "success": bool,
                "data": {
                    "id": 维度ID,
                    "name": 维度名称,
                    "description": 描述,
                    "creator": 创建者,
                    "type": 数据类型,
                    ...
                }
            }
        """
        result = self._get_request(f"/indicator/dimension/{dimension_id}/info")
        return {
            "success": result.get("success", False),
            "data": result.get("data"),
            "raw": result,
        }

    def get_dimension_consanguinity(self, dimension_id: str) -> dict:
        """
        查看维度血缘关系

        GET /api/dc/v1/indicator/dimension/{dimensionId}/consanguinity

        Args:
            dimension_id: 维度 ID

        Returns:
            {
                "success": bool,
                "node_info": {节点ID: 节点属性, ...},
                "node_list": [节点属性列表],
                "parent_edges": [...],
                "child_edges": [...],
            }
        """
        result = self._get_request(f"/indicator/dimension/{dimension_id}/consanguinity")
        if result.get("success"):
            data = result.get("data", {})
            node_info = data.get("nodeInfo", {})
            node_list = []
            for node_id, attrs in node_info.items():
                attrs["_id"] = node_id
                node_list.append(attrs)
            return {
                "success": True,
                "node_info": node_info,
                "node_list": node_list,
                "parent_edges": data.get("parentEdges", []),
                "child_edges": data.get("childEdges", []),
                "raw": result,
            }
        return {"success": False, "raw": result}

    def get_dimension_relate_metrics(self, dimension_id: str) -> dict:
        """
        查看维度关联的指标（该维度可用于分析哪些指标）

        GET /api/dc/v1/indicator/dimension/{dimensionId}/relate/metric

        Args:
            dimension_id: 维度 ID

        Returns:
            {
                "success": bool,
                "metrics": [
                    {"id": 指标ID, "name": 指标名, "type": 数据类型, "description": 描述},
                    ...
                ]
            }
        """
        result = self._get_request(f"/indicator/dimension/{dimension_id}/relate/metric")
        if result.get("success"):
            return {
                "success": True,
                "metrics": result.get("data", []),
                "raw": result,
            }
        return {"success": False, "metrics": [], "raw": result}

    def get_dimension_data(
        self,
        dimension_id: str,
        keyword: Optional[str] = None,
        page_index: int = 1,
        page_size: int = 100,
    ) -> dict:
        """
        查看维度值（维度字段的枚举值列表）

        POST /api/dc/v1/indicator/dimension/{dimensionId}/data

        Args:
            dimension_id: 维度 ID
            keyword: 搜索关键词（可选）
            page_index: 页码
            page_size: 每页条数

        Returns:
            {
                "success": bool,
                "dimension_name": 维度名,
                "type": 数据类型,
                "data": [维度值列表],
                "page_info": {"pageCount", "pageIndex", "rowCount"},
            }
        """
        body = {
            "keyword": keyword or "",
            "queryId": str(uuid.uuid4()),
            "limit": {
                "pageIndex": page_index,
                "pageSize": page_size,
            },
        }
        result = self._request(f"/indicator/dimension/{dimension_id}/data", body)
        if result.get("success"):
            data = result.get("data", {})
            return {
                "success": True,
                "dimension_name": data.get("dimensionName", ""),
                "type": data.get("type"),
                "data": data.get("data", []),
                "page_info": data.get("pageinfo", {}),
                "raw": result,
            }
        return {"success": False, "raw": result}

    # ------------------------------------------------------------------
    # 数据查询
    # ------------------------------------------------------------------

    # 字段类型映射（用于构造 source）
    FIELD_TYPE = {
        "indicator": 65,  # 指标
        "dimension": 66,  # 维度
    }

    def query_data(
        self,
        metrics: list,
        dimensions: Optional[list] = None,
        filters: Optional[list] = None,
        orders: Optional[list] = None,
        page_size: int = 100,
        page_index: int = 1,
        summary: Optional[dict] = None,
        group: Optional[dict] = None,
        field_names: Optional[dict] = None,
    ) -> dict:
        """
        查询指标数据

        Args:
            metrics: 指标 ID 列表，如 ["725ac8e3-..."]
            dimensions: 维度 ID 列表，如 ["de39d257-..."]
            filters: 过滤条件列表
            orders: 排序条件列表
            page_size: 每页条数
            page_index: 页码
            summary: 汇总方式，如 {"type": 3} (3=求和)
            group: 日期分组，如 {"type": 5} (5=年月日)
            field_names: 字段名称映射，如 {"指标ID": "销量"}，不传则自动从搜索结果获取

        Returns:
            {
                "success": bool,
                "fields": [{"id", "name", "type"}],  # 返回字段信息
                "rows": [["val1", "val2"], ...],       # 数据行
                "total": 数值,                          # 本页汇总
                "row_count": 数值,                      # 总记录数
                "page_info": {"pageSize", "pageIndex", "rowCount"},
                "raw": 原始响应,                         # 完整原始响应
            }
        """
        dimensions = dimensions or []
        filters = filters or []
        orders = orders or []
        field_names = field_names or {}

        # 自动获取字段名称（如果未提供）
        all_ids = metrics + dimensions
        source = {}
        for field_id in all_ids:
            name = field_names.get(field_id, field_id)
            resource_type = self.FIELD_TYPE["indicator"] if field_id in metrics else self.FIELD_TYPE["dimension"]
            source[field_id] = {
                "fieldId": field_id,
                "resourceType": resource_type,
                "name": name,
            }

        body = {
            "dimensions": dimensions,
            "metrics": metrics,
            "source": source,
            "filters": filters,
            "orders": orders,
            "limit": {
                "pageSize": str(page_size),
                "pageIndex": str(page_index),
                "rowCount": "0",
            },
        }
        if summary:
            body["summary"] = summary
        if group:
            body["group"] = group

        result = self._request(self.QUERY_URL, body)

        if not result.get("success"):
            return {
                "success": False,
                "error": result.get("errorMsg", "查询失败"),
                "errorCode": result.get("errorCode", ""),
                "raw": result,
            }

        data = result.get("data", {})
        fields = data.get("fields", [])
        rows = data.get("data", [])
        page_info = data.get("pageInfo", {})

        # 计算本页数值汇总（取最后一列数值）
        total = 0
        for row in rows:
            if len(row) > 0:
                try:
                    total += float(row[-1]) if row[-1] else 0
                except (ValueError, TypeError):
                    pass

        return {
            "success": True,
            "fields": fields,
            "rows": rows,
            "total": total,
            "row_count": len(rows),
            "page_info": page_info,
            "raw": result,
        }

    def query_all_pages(
        self,
        metrics: list,
        dimensions: Optional[list] = None,
        filters: Optional[list] = None,
        orders: Optional[list] = None,
        page_size: int = 200,
        field_names: Optional[dict] = None,
        max_pages: int = 10,
    ) -> dict:
        """
        查询所有页数据（自动分页聚合）

        Args:
            metrics: 指标 ID 列表
            dimensions: 维度 ID 列表
            filters: 过滤条件
            orders: 排序条件
            page_size: 每页条数（建议 200 以减少请求次数）
            field_names: 字段名称映射
            max_pages: 最大页数限制，防止无限循环

        Returns:
            {
                "success": bool,
                "fields": [...],
                "rows": [...],          # 所有页合并后的数据
                "total": 总数,           # 所有页汇总
                "total_rows": 总记录数,
                "page_count": 实际请求页数,
            }
        """
        all_rows = []
        grand_total = 0
        page_count = 0

        for page in range(1, max_pages + 1):
            result = self.query_data(
                metrics=metrics,
                dimensions=dimensions,
                filters=filters,
                orders=orders,
                page_size=page_size,
                page_index=page,
                field_names=field_names,
            )
            page_count += 1
            if not result["success"]:
                break
            rows = result["rows"]
            if not rows:
                break
            all_rows.extend(rows)
            grand_total += result["total"]
            if len(rows) < page_size:
                break

        return {
            "success": True,
            "fields": result.get("fields", []),
            "rows": all_rows,
            "total": grand_total,
            "total_rows": len(all_rows),
            "page_count": page_count,
        }

    def query_data_summary(
        self,
        metrics: list,
        dimensions: Optional[list] = None,
        date_dimension_id: Optional[str] = None,
        field_names: Optional[dict] = None,
        max_pages: int = 10,
    ) -> dict:
        """
        查询指标数据并按月汇总

        Args:
            metrics: 指标 ID 列表
            dimensions: 维度 ID 列表
            date_dimension_id: 日期维度 ID（用于按月分组）
            field_names: 字段名称映射
            max_pages: 最大页数

        Returns:
            {
                "success": bool,
                "fields": [...],
                "total": 总数值,
                "total_rows": 总记录数,
                "monthly": {"2025-01": 10000, ...},  # 按月汇总
                "rows": [...],                        # 原始数据行
            }
        """
        result = self.query_all_pages(
            metrics=metrics,
            dimensions=dimensions,
            page_size=200,
            field_names=field_names,
            max_pages=max_pages,
        )
        if not result["success"]:
            return result

        monthly = defaultdict(float)
        for row in result["rows"]:
            if len(row) >= 2:
                date_str = row[0] if date_dimension_id else (dimensions[0] if dimensions else None)
                val = float(row[-1]) if row[-1] else 0
                if date_str and str(date_str) != "None":
                    month = str(date_str)[:7]
                    monthly[month] += val
                else:
                    monthly["(未知日期)"] += val

        return {
            "success": True,
            "fields": result["fields"],
            "total": result["total"],
            "total_rows": result["total_rows"],
            "monthly": dict(sorted(monthly.items())),
            "rows": result["rows"],
        }

    # ------------------------------------------------------------------
    # 数据集查询（通过 /v5/api/ 接口，需要 Bearer Token 认证）
    # ------------------------------------------------------------------

    @staticmethod
    def _login_get_token(server_url: str, username: str = "rank", password: str = "rank") -> str:
        """
        登录 FineBI 获取 Bearer Token

        POST /decision/login

        Args:
            server_url: FineBI 服务器地址
            username: 登录用户名
            password: 登录密码

        Returns:
            access_token 字符串
        """
        import urllib.request
        login_url = f"{server_url.rstrip('/')}/decision/login"
        data = json.dumps({"username": username, "password": password}).encode()
        req = urllib.request.Request(
            login_url,
            data=data,
            headers={"Content-Type": "application/json"},
        )
        resp = urllib.request.urlopen(req, timeout=10)
        result = json.loads(resp.read())
        return result.get("data", {}).get("accessToken", "")

    @staticmethod
    def _parse_jsonp(text: str) -> dict:
        """
        解析 FineBI JSONP 响应（兼容 JSON 和 JSONP 格式）

        FineBI 的 /v5/api/table/{id}/get 等接口返回 JSONP 格式：
            callback({"success":true, ...})
        而 /v5/api/tables/fields/page 等接口返回纯 JSON

        Args:
            text: 响应文本

        Returns:
            解析后的 dict
        """
        text = text.strip()
        m = re.search(r'callback\((.+)\)', text)
        if m:
            return json.loads(m.group(1))
        return json.loads(text)

    def search_datasets(self, keyword: str = "", page_size: int = 50) -> list:
        """
        搜索数据集（公共数据表）

        通过 /decision/api/dc/v1/indicator/search 接口搜索，
        使用 itemTypes=[3] 过滤数据集类型。

        Args:
            keyword: 搜索关键词，如 "运单入库"、"库存"、"shipment"
            page_size: 每页条数

        Returns:
            数据集列表，每条包含：
            - name: 数据集 UUID（用于后续查询）
            - transferName: 显示名
            - position: 数据目录路径
            - fields: 字段名列表
            - connectionName: 数据连接名称
            - type: 2=SQL表, 其他=自助数据集
            - engineType: 引擎类型 (spider/...)
            - parentId: 父目录 ID
            - path: 目录路径树
            - id: 同 name (UUID)

        Example:
            >>> api = IndicatorAPI('http://bi.hiccpet.net', Secret('rank', 'key'))
            >>> datasets = api.search_datasets('运单入库')
            >>> for ds in datasets:
            ...     print(f"{ds['transferName']} (UUID: {ds['name']})")
            运单入库 | dwd_finebi_inbound_shipment_v (UUID: 1815b412...)
        """
        body = {
            "keyword": keyword,
            "pageIndex": 1,
            "pageSize": page_size,
            "force": True,
            "privilege": "view",
            "filter": {"itemTypes": [3]},  # 3 = 数据集
        }
        result = self._request(self.SEARCH_URL, body)
        if result.get("success"):
            return result.get("data", {}).get("items", [])
        return []

    def get_dataset_fields(
        self,
        uuid: str,
        login_username: str = "rank",
        login_password: str = "rank",
    ) -> list:
        """
        获取数据集字段列表

        通过 POST /v5/api/tables/fields/page 接口获取，
        需要 Bearer Token 认证（自动登录获取）。

        Args:
            uuid: 数据集 UUID（从 search_datasets 的 'name' 字段获取）
            login_username: FineBI 登录用户名
            login_password: FineBI 登录密码

        Returns:
            字段列表，每条包含：
            - name: 字段名
            - type: 数据类型 (16=文本, 32=数值, 48=时间)
            - id: 字段完整 ID
            - transferName: 显示名
            - enable: 是否启用

        Example:
            >>> api = IndicatorAPI('http://bi.hiccpet.net', Secret('rank', 'key'))
            >>> fields = api.get_dataset_fields('1815b412...')
            >>> for f in fields:
            ...     print(f"{f['name']} (type={f['type']})")
            shipment_main_flag (type=32)
            warehouse_name (type=16)
        """
        token = self._login_get_token(self.server_url, login_username, login_password)
        url = f"{self.server_url}/decision/v5/api/tables/fields/page"
        body = {"tableName": uuid, "pageIndex": "1", "pageSize": "200"}
        data = json.dumps(body).encode()
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )
        resp = urllib.request.urlopen(req, timeout=30)
        result = self._parse_jsonp(resp.read().decode())
        if result.get("success"):
            return result.get("data", {}).get("allFields", [])
        return []

    def get_dataset_data(
        self,
        uuid: str,
        page_size: int = 10,
        page_index: int = 1,
        login_username: str = "rank",
        login_password: str = "rank",
    ) -> dict:
        """
        获取数据集数据

        通过 POST /v5/api/tables/data/page 接口获取，
        需要 Bearer Token 认证（自动登录获取）。

        Args:
            uuid: 数据集 UUID（从 search_datasets 的 'name' 字段获取）
            page_size: 每页行数
            page_index: 页码（从 1 开始）
            login_username: FineBI 登录用户名
            login_password: FineBI 登录密码

        Returns:
            {
                "success": bool,
                "fields": [{"name": 字段名, "type": 数据类型, ...}],
                "data": [[值1, 值2, ...], ...],   # 二维数组，每行对应 fields 顺序
                "total_rows": 总行数,
                "page_info": {"totalRows", "pageSize", "pageIndex"},
                "error": 错误信息（失败时）,
            }

        Note:
            - 返回的 data 是一个二维列表，每行按 fields 的顺序排列
            - 字段类型: 16=文本, 32=数值, 48=时间
            - 数值字段的 None 值表示空值

        Example:
            >>> api = IndicatorAPI('http://bi.hiccpet.net', Secret('rank', 'key'))
            >>> result = api.get_dataset_data('1815b412...', page_size=5)
            >>> if result['success']:
            ...     fields = [f['name'] for f in result['fields']]
            ...     for row in result['data']:
            ...         print(dict(zip(fields, row)))
        """
        token = self._login_get_token(self.server_url, login_username, login_password)
        url = f"{self.server_url}/decision/v5/api/tables/data/page"
        body = {
            "tableName": uuid,
            "pageIndex": str(page_index),
            "pageSize": str(page_size),
        }
        data = json.dumps(body).encode()
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )
        resp = urllib.request.urlopen(req, timeout=30)
        result = self._parse_jsonp(resp.read().decode())
        if result.get("success"):
            resp_data = result.get("data", {})
            return {
                "success": True,
                "fields": resp_data.get("fields", []),
                "data": resp_data.get("data", []),
                "total_rows": resp_data.get("pageInfo", {}).get("totalRows", 0),
                "page_info": resp_data.get("pageInfo", {}),
            }
        return {
            "success": False,
            "error": result.get("errorMsg", "查询失败"),
            "fields": [],
            "data": [],
            "total_rows": 0,
            "page_info": {},
        }


# ======================================================================
# 快捷函数（命令行直接调用）
# ======================================================================

def quick_query(
    server_url: str,
    username: str,
    secret_key: str,
    keyword: str,
    dimension_keyword: Optional[str] = None,
    page_size: int = 200,
    max_pages: int = 10,
) -> dict:
    """
    快捷查询：搜索关键词指标 → 按日期维度分组查询 → 按月汇总

    Args:
        server_url: 服务器地址
        username: 用户名
        secret_key: 密钥
        keyword: 搜索关键词（如 "销量"）
        dimension_keyword: 维度关键词（如 "日期"），默认自动搜索 "日期"
        page_size: 每页条数
        max_pages: 最大页数

    Returns:
        {
            "success": bool,
            "indicator": {...},  # 找到的主要指标
            "dimension": {...},  # 找到的日期维度
            "data": {...},       # 查询结果
        }
    """
    api = IndicatorAPI(server_url, Secret(username=username, secret_key=secret_key))

    # 1. 搜索指标
    indicators = api.search_indicators(keyword)
    if not indicators:
        return {"success": False, "error": f"未找到包含「{keyword}」的指标"}

    # 取第一个匹配的指标
    indicator = indicators[0]

    # 2. 搜索维度
    dim_keyword = dimension_keyword or "日期"
    dimensions = api.search_dimensions(dim_keyword)
    dimension = None
    for dim in dimensions:
        if dim_keyword in dim.get("name", ""):
            dimension = dim
            break
    if not dimension and dimensions:
        dimension = dimensions[0]

    # 3. 查询数据
    metrics = [indicator["id"]]
    dims = [dimension["id"]] if dimension else []
    field_names = {indicator["id"]: indicator["name"]}
    if dimension:
        field_names[dimension["id"]] = dimension["name"]

    result = api.query_data_summary(
        metrics=metrics,
        dimensions=dims,
        date_dimension_id=dimension["id"] if dimension else None,
        field_names=field_names,
        max_pages=max_pages,
    )

    return {
        "success": result["success"],
        "indicator": indicator,
        "dimension": dimension,
        "data": result,
    }


def print_result(result: dict):
    """友好打印查询结果"""
    if not result.get("success"):
        print(f"查询失败: {result.get('error', '未知错误')}")
        return

    ind = result.get("indicator", {})
    dim = result.get("dimension", {})
    data = result.get("data", {})

    print(f"指标: {ind.get('name', '?')}  (ID: {ind.get('id', '?')})")
    print(f"路径: {ind.get('position', '?')}")
    if dim:
        print(f"维度: {dim.get('name', '?')}  (ID: {dim.get('id', '?')})")
    print()

    monthly = data.get("monthly", {})
    if monthly:
        print(f"{'月份':<12} | {'数值':>12}")
        print(f"{'-'*12}-|{'-'*13}")
        for month, val in monthly.items():
            print(f"{month:<12} | {val:>12,.0f}")
        print()
        print(f"{'合计':<12} | {data.get('total', 0):>12,.0f}")
        print(f"总记录数: {data.get('total_rows', 0)}")
    else:
        print(f"总数值: {data.get('total', 0):,.0f}")
        print(f"记录数: {data.get('total_rows', 0)}")
        print()
        for row in data.get("rows", [])[:20]:
            print("  " + " | ".join(str(v) for v in row))


# ======================================================================
# 命令行入口
# ======================================================================

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 4:
        print("用法: python query_indicator.py <server_url> <username> <secret_key> <keyword> [dimension_keyword]")
        print("示例: python query_indicator.py http://bi.hiccpet.net rank your_key 销量 日期")
        sys.exit(1)

    server_url = sys.argv[1]
    username = sys.argv[2]
    secret_key = sys.argv[3]
    keyword = sys.argv[4]
    dim_keyword = sys.argv[5] if len(sys.argv) > 5 else None

    result = quick_query(server_url, username, secret_key, keyword, dim_keyword)
    print_result(result)