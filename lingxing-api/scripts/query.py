#!/usr/bin/env python3
"""
领星 API 知识库查询工具

子命令：
  search <关键词>           模糊搜索 API（按标题、路径、描述关键词）
  by-path <路径关键词>       按 API 路径关键词查
  by-key <业务键>           按业务键查相关接口
  by-category <一级分类>     按分类查
  related <api_path>        查与某 API 相关的接口（基于业务键）
  get <api_path 或 标题>     查 API 精简详情
  detail <api_path 或 标题>  查 API 完整详情（含入参/出参/样例）
  list-keys                 列出所有已建索引的业务键
  list-categories           列出所有分类
  stats                     知识库统计
"""
import gzip
import json
import sys
import argparse
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent / "data"


def _load_data_file(stem: str):
    """按文件名主干加载 data 文件，透明支持 .json 与 .json.gz（打包体积优化）。

    返回解析后的对象；文件不存在返回 None。
    """
    for name in (f"{stem}.json", f"{stem}.json.gz"):
        p = DATA_DIR / name
        if p.exists():
            if name.endswith(".gz"):
                with gzip.open(p, "rt", encoding="utf-8") as f:
                    return json.load(f)
            return json.loads(p.read_text(encoding="utf-8"))
    return None


def load_data() -> dict[str, Any]:
    """加载所有索引数据（含详细数据，按需懒加载）"""
    out = {
        "apis": _load_data_file("apis_clean") or [],
        "biz_key": _load_data_file("biz_key_index") or {},
        "category": _load_data_file("category_index") or {},
        "path_prefix": _load_data_file("path_prefix_index") or {},
        "desc": _load_data_file("desc_index") or {},
        "_detailed_loaded": False,
    }
    return out


def ensure_detailed(data: dict) -> None:
    """按需加载详细数据（apis_detailed.json[.gz] + path 索引）。

    path 索引优先读预构建文件；缺失时从 apis_detailed 运行时构建（O(n)，n=611 很快）。
    """
    if data.get("_detailed_loaded"):
        return
    detailed = _load_data_file("apis_detailed")
    data["apis_detailed"] = detailed if detailed is not None else []
    path_index = _load_data_file("api_path_index")
    if path_index is None:
        path_index = {a.get("api_path", ""): a for a in data["apis_detailed"] if a.get("api_path")}
    data["api_path_index"] = path_index
    data["_detailed_loaded"] = True


def _endpoint(api_path: str) -> str:
    """取 API 路径的最后一段（endpoint 名），如 .../getXXX -> getXXX"""
    return api_path.rstrip("/").rsplit("/", 1)[-1].lower() if api_path else ""


def find_api_by_ref(apis, ref):
    """按引用定位 API，优先级：完整路径 > 标题 > endpoint > 子串包含。

    优先 endpoint 精确匹配，可避免单数/批量版（如 XXXDetail / XXXDetailList）
    这类互为子串的接口被错误命中。
    """
    r = ref.lower()
    for a in apis:
        if a.get("api_path", "").lower() == r or a.get("title", "").lower() == r:
            return a
    # endpoint 精确匹配（单数/批量版靠它区分）
    for a in apis:
        if _endpoint(a.get("api_path", "")) == r:
            return a
    # 最后才子串包含
    for a in apis:
        if r in a.get("api_path", "").lower() or r in a.get("title", "").lower():
            return a
    return None


def find_detailed_by_ref(data: dict, ref: str) -> dict | None:
    """按 api_path / 标题 / endpoint 查详细记录，优先级同 find_api_by_ref。"""
    ensure_detailed(data)
    index = data["api_path_index"]
    # 1) 完整 api_path / 标题精确匹配
    r = ref.lower()
    for ap, d in index.items():
        if ap.lower() == r or d.get("title", "").lower() == r:
            return d
    # 2) endpoint 精确匹配（区分单数/批量版）
    for ap, d in index.items():
        if _endpoint(ap) == r:
            return d
    # 3) 子串包含
    for ap, d in index.items():
        if r in ap.lower() or r in d.get("title", "").lower():
            return d
    return None


def fmt_api(a, verbose=False):
    if not a:
        return "(无)"
    line = f"{a.get('method', ''):5s}  {a.get('api_path', ''):60s}  [{a.get('category_l1','')}/{a.get('category_l2','') or '-'}]  {a.get('title','')}"
    if verbose:
        line += f"\n    doc: {a.get('doc_path', '')}"
    return line


def fmt_param(p: dict) -> str:
    req = "必填" if p.get("required") else "可选"
    type_ = p.get("type", "") or "-"
    name = p.get("name", "")
    path = p.get("path", name)
    desc = p.get("desc", "")
    example = p.get("example", "")
    line = f"  - {path} ({type_}, {req})"
    if desc:
        line += f"\n    说明: {desc}"
    if example:
        line += f"\n    示例: {example}"
    return line


def cmd_search(args, data):
    kw = args.keyword
    results = []
    seen = set()
    for a in data["apis"]:
        text = f"{a.get('title','')} {a.get('api_path','')}".lower()
        if kw.lower() in text:
            ap = a.get("api_path", "")
            if ap and ap not in seen:
                results.append(a)
                seen.add(ap)
    for ck, refs in data["desc"].items():
        if kw in ck:
            for r in refs:
                ap = r.get("api_path", "")
                if ap and ap not in seen:
                    results.append(r)
                    seen.add(ap)
    print(f"=== search '{kw}': {len(results)} matches ===")
    for a in results[: args.limit]:
        print(fmt_api(a))


def cmd_by_path(args, data):
    kw = args.keyword
    results = [a for a in data["apis"] if kw in a.get("api_path", "")]
    print(f"=== path contains '{kw}': {len(results)} matches ===")
    for a in results[: args.limit]:
        print(fmt_api(a))


def cmd_by_key(args, data):
    key = args.key
    if key in data["biz_key"]:
        biz = data["biz_key"][key]
    else:
        candidates = [k for k in data["biz_key"] if key in k or key.lower() in k.lower()]
        if not candidates:
            print(f"未找到业务键 '{key}'。已建索引的键：")
            for k in data["biz_key"]:
                print(f"  - {k}")
            return
        if len(candidates) == 1:
            key = candidates[0]
            biz = data["biz_key"][key]
            print(f"(匹配到 {key})")
        else:
            print(f"多个匹配业务键，请精确选择：")
            for k in candidates:
                print(f"  - {k}")
            return
    print(f"=== 业务键「{key}」相关接口 ===")
    print(f"\n[PRIMARY：必填入参] {len(biz['primary'])} 个")
    for r in biz["primary"][: args.limit]:
        print("  " + fmt_api(r))
    print(f"\n[RETURN：返回含此键] {len(biz['return'])} 个")
    for r in biz["return"][: args.limit]:
        print("  " + fmt_api(r))
    if biz.get("mention"):
        print(f"\n[MENTION：描述提及] {len(biz['mention'])} 个")
        for r in biz["mention"][: args.limit]:
            print("  " + fmt_api(r))


def cmd_by_category(args, data):
    cat = args.category
    if cat not in data["category"]:
        print(f"未找到分类 '{cat}'。已建索引的分类：")
        for k, v in data["category"].items():
            print(f"  - {k} ({len(v)})")
        return
    apis = data["category"][cat]
    print(f"=== 分类「{cat}」共 {len(apis)} 个 API ===")
    for a in apis[: args.limit]:
        print("  " + fmt_api(a))


def cmd_related(args, data):
    api = find_api_by_ref(data["apis"], args.api_ref)
    if not api:
        print(f"未找到 API '{args.api_ref}'")
        return
    print(f"=== {api.get('title')} ===")
    print(fmt_api(api))
    related_keys = set()
    for k, biz in data["biz_key"].items():
        for r in biz.get("primary", []) + biz.get("return", []):
            if r.get("api_path") == api.get("api_path"):
                related_keys.add(k)
    if not related_keys:
        print("(无业务键关联)")
        return
    print(f"\n涉及业务键：{', '.join(sorted(related_keys))}")
    for k in sorted(related_keys):
        biz = data["biz_key"][k]
        print(f"\n--- 与「{k}」关联的其它接口（排除自身）---")
        others = [r for r in biz["primary"] + biz["return"] if r.get("api_path") != api.get("api_path")]
        for r in others[: args.limit]:
            print("  " + fmt_api(r))


def cmd_get(args, data):
    api = find_api_by_ref(data["apis"], args.api_ref)
    if not api:
        print(f"未找到 API '{args.api_ref}'")
        return
    print(f"=== 详情 ===")
    for k, v in api.items():
        if isinstance(v, list):
            print(f"  {k}: {len(v)} 项")
        else:
            print(f"  {k}: {v}")


def cmd_detail(args, data):
    """显示 API 完整详情：入参/出参/请求示例/响应示例"""
    d = find_detailed_by_ref(data, args.api_ref)
    if not d:
        print(f"未找到 API '{args.api_ref}' 的详情")
        return
    print(f"=== {d.get('title')} ===")
    print(f"  API:   {d.get('method','')} {d.get('api_path','')}")
    print(f"  分类:  {d.get('category_l1','')} / {d.get('category_l2','') or '-'} / {d.get('category_l3','') or '-'}")
    print(f"  限流:  {d.get('rate_limit','')}")
    print(f"  文档:  {d.get('doc_path','')}")
    if d.get("business_fields"):
        print(f"  业务字段: {', '.join(d.get('business_fields', []))}")
    print()

    # 请求头
    headers_in = d.get("headers_in") or []
    if headers_in:
        print(f"## 请求头 ({len(headers_in)} 项)")
        for p in headers_in:
            print(fmt_param(p))
        print()

    # 请求参数
    in_params = d.get("in_params") or []
    print(f"## 请求参数 ({len(in_params)} 项)")
    if in_params:
        for p in in_params:
            print(fmt_param(p))
    else:
        print("  (无)")
    print()

    # 请求示例
    if d.get("request_example"):
        print("## 请求示例")
        print(d["request_example"])
        print()
    if d.get("request_curl_example"):
        print("## 请求 curl 示例")
        print(d["request_curl_example"])
        print()

    # 返回参数
    out_params = d.get("out_params") or []
    print(f"## 返回参数 ({len(out_params)} 项)")
    if out_params:
        # 按 depth + path 排序展示，更易读
        for p in out_params:
            print(fmt_param(p))
    else:
        print("  (无)")
    print()

    # 响应示例
    if d.get("response_success_example"):
        print("## 响应成功示例")
        print(d["response_success_example"])
        print()
    if d.get("response_failure_example"):
        print("## 响应失败示例")
        print(d["response_failure_example"])
        print()


def cmd_list_keys(args, data):
    print(f"=== 业务键 ({len(data['biz_key'])} 个) ===")
    for k, v in data["biz_key"].items():
        total = len(v.get("primary", [])) + len(v.get("return", [])) + len(v.get("mention", []))
        print(f"  {k:20s}  primary={len(v.get('primary',[])):3d}  return={len(v.get('return',[])):3d}  total={total}")


def cmd_list_categories(args, data):
    print(f"=== 一级分类 ({len(data['category'])} 个) ===")
    for k, v in sorted(data["category"].items(), key=lambda x: -len(x[1])):
        print(f"  {k:30s}  {len(v):3d} 个 API")


def cmd_stats(args, data):
    stats = _load_data_file("stats") or {}
    print("=== 知识库统计 ===")
    for k, v in stats.items():
        print(f"  {k}: {v}")


def main():
    parser = argparse.ArgumentParser(description="领星 API 知识库查询")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("search", help="模糊搜索（标题/路径/中文关键词）")
    p.add_argument("keyword")
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("by-path", help="按 API 路径片段查")
    p.add_argument("keyword")
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("by-key", help="按业务键查")
    p.add_argument("key")
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("by-category", help="按分类查")
    p.add_argument("category")
    p.add_argument("--limit", type=int, default=50)

    p = sub.add_parser("related", help="查与某 API 相关的接口")
    p.add_argument("api_ref")
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("get", help="查 API 精简详情")
    p.add_argument("api_ref")

    p = sub.add_parser("detail", help="查 API 完整详情（入参/出参/样例）")
    p.add_argument("api_ref")
    p.add_argument("--no-example", action="store_true", help="不打印示例")
    p.add_argument("--no-out-params", action="store_true", help="不打印出参列表")

    sub.add_parser("list-keys", help="列出所有业务键")
    sub.add_parser("list-categories", help="列出所有分类")
    sub.add_parser("stats", help="知识库统计")

    args = parser.parse_args()
    data = load_data()
    dispatch = {
        "search": cmd_search, "by-path": cmd_by_path, "by-key": cmd_by_key,
        "by-category": cmd_by_category, "related": cmd_related, "get": cmd_get,
        "detail": cmd_detail, "list-keys": cmd_list_keys, "list-categories": cmd_list_categories,
        "stats": cmd_stats,
    }
    dispatch[args.cmd](args, data)


if __name__ == "__main__":
    main()
