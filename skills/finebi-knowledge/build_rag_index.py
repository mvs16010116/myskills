#!/usr/bin/env python3
"""
FineBI 知识库 RAG 索引构建器
读取本地 Markdown 文档，构建向量索引，支持语义检索
使用 ChromaDB 内置 ONNX 模型（all-MiniLM-L6-v2），无需联网下载
"""
import os
import re
import json
import hashlib
import logging
from datetime import datetime
from pathlib import Path

import chromadb
from chromadb.config import Settings
from chromadb.api.types import EmbeddingFunction, Documents, Embeddings

# ========== 配置 ==========
# 使用脚本所在目录作为基准，确保从任何位置调用都能正确找到数据
_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIRS = [
    os.path.join(_BASE_DIR, "data", "finebi_docs"),
    os.path.join(_BASE_DIR, "data", "finebi_docs_v7"),
]
CHROMA_DIR = os.path.join(_BASE_DIR, "data", "chroma_db")
COLLECTION_NAME = "finebi_docs"
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64
BATCH_SIZE = 128

LOG_DIR = os.path.join(_BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, f"rag_index_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"), encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class ChineseTextEmbeddingFunction(EmbeddingFunction):
    """中文文本嵌入函数，使用 text2vec-base-chinese 模型（768维，专为中文优化）"""

    _model = None  # 类级别缓存，避免重复加载模型

    def __init__(self, model_name: str = "shibing624/text2vec-base-chinese"):
        self._model_name = model_name
        if ChineseTextEmbeddingFunction._model is None:
            from sentence_transformers import SentenceTransformer
            ChineseTextEmbeddingFunction._model = SentenceTransformer(model_name)

    @property
    def model(self):
        return ChineseTextEmbeddingFunction._model

    def __call__(self, input: Documents) -> Embeddings:
        return self.model.encode(list(input), show_progress_bar=False).tolist()


def get_all_docs(docs_dirs):
    """递归获取所有 Markdown 文档"""
    docs = []
    for dd in docs_dirs:
        base = Path(dd)
        if not base.exists():
            logger.warning(f"目录不存在: {dd}")
            continue
        for md_file in sorted(base.rglob("*.md")):
            if md_file.is_file():
                docs.append((md_file, dd))
    return docs


def parse_doc_metadata(content):
    """解析文档 YAML 元数据头"""
    meta = {"title": "", "doc_id": "", "url": "", "source": "", "crawled_at": ""}
    content_str = content if isinstance(content, str) else content.decode("utf-8")

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content_str, re.DOTALL)
    if match:
        yaml_block = match.group(1)
        for line in yaml_block.split("\n"):
            for key in meta:
                if line.startswith(f"{key}:"):
                    meta[key] = line[len(key) + 1:].strip().strip('"').strip("'")
        content_str = content_str[match.end():]
    return meta, content_str


def clean_body(text):
    """清理文档正文，移除导航、反馈、版权等无关内容"""
    if not text:
        return ""

    # 移除所有图片引用和图片链接
    text = re.sub(r'!\[.*?\]\([^)]+\)', '', text)
    text = re.sub(r'\[.*?\]\(/core/style/lod\.png\)', '', text)
    text = re.sub(r'!\[.*?\]\(/core/style/lod\.png\)', '', text)

    # 移除"对此内容反馈"及后续反馈块
    text = re.sub(r'对此内容反馈\s*\n[\s\S]*?(?=\n#|\n##|\Z)', '', text)

    # 移除"产品级协助"及后续块
    text = re.sub(r'产品级协助_[\s\S]*?(?=\n#|\n##|\Z)', '', text)

    # 移除"附件列表"及后续的下载/导航信息
    text = re.sub(r'###?\s*附件列表[\s\S]*?(?=\n#|\n##|\Z)', '', text)

    # 移除语言切换和页脚
    text = re.sub(r'\[中文.*?\]\([^)]+\)\s*\[English.*?\]\([^)]+\)', '', text)
    text = re.sub(r'提交页面反馈[\s\S]*$', '', text)

    # 移除"有帮助/没帮助/只是浏览"
    text = re.sub(r'\* 有帮助\s*\n\* 没帮助\s*\n\* 只是浏览', '', text)

    # 移除"上一篇/下一篇"导航
    text = re.sub(r'\[[^]]*上一篇[^]]*\]\([^)]+\)\s*\[[^]]*下一篇[^]]*\]\([^)]+\)', '', text)

    # 移除"主题："行
    text = re.sub(r'\*\*主题：\*\*.*', '', text)

    # 移除多余空行
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


def split_into_chunks(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """使用滑动窗口将文本分割为 chunks，优先在段落边界处分割"""
    if not text.strip():
        return []

    # 先清理
    text = clean_body(text)
    if not text:
        return []

    MIN_CHUNK_SIZE = 50
    # 按段落分割
    paragraphs = re.split(r"\n\s*\n", text)
    # 过滤掉过短或纯符号的段落
    paragraphs = [
        p.strip() for p in paragraphs
        if p.strip() and len(p.strip()) >= 5
        and not re.match(r'^[\s\*\-_=\[\]()<>/\.]+$', p.strip())
    ]
    if not paragraphs:
        return []

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        # 如果段落本身就超过 chunk_size，单独作为 chunk
        if len(para) >= chunk_size:
            if current_chunk and len(current_chunk) >= MIN_CHUNK_SIZE:
                chunks.append(current_chunk.strip())
            current_chunk = ""
            # 长段落按滑动窗口切分
            for i in range(0, len(para), chunk_size - overlap):
                segment = para[i:i + chunk_size]
                if len(segment) >= MIN_CHUNK_SIZE:
                    chunks.append(segment.strip())
            continue

        # 如果加上当前段落会超过 chunk_size，先保存当前 chunk
        if current_chunk and len(current_chunk) + len(para) + 1 > chunk_size:
            if len(current_chunk) >= MIN_CHUNK_SIZE:
                chunks.append(current_chunk.strip())
            # 取 overlap 作为新 chunk 的起始
            if overlap > 0 and len(current_chunk) > overlap:
                current_chunk = current_chunk[-overlap:] + "\n\n" + para
            else:
                current_chunk = para
        else:
            current_chunk = (current_chunk + "\n\n" + para) if current_chunk else para

    # 最后一个 chunk
    if current_chunk and len(current_chunk) >= MIN_CHUNK_SIZE:
        chunks.append(current_chunk.strip())

    return chunks


def build_index():
    """构建向量索引"""
    logger.info("=" * 60)
    logger.info("FineBI RAG 索引构建器 - 启动")
    logger.info(f"文档目录: {DOCS_DIRS}")
    logger.info(f"索引目录: {CHROMA_DIR}")
    logger.info("=" * 60)

    # 1. 扫描文档
    logger.info("[1/4] 扫描文档...")
    docs = get_all_docs(DOCS_DIRS)
    logger.info(f"    找到 {len(docs)} 个文档")

    # 2. 分割文档为 chunks
    logger.info("[2/4] 分割文档为 chunks...")
    all_chunks = []
    all_metas = []
    all_ids = []

    for doc_path, base_dir in docs:
        try:
            with open(doc_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            logger.warning(f"    读取失败: {doc_path} - {e}")
            continue

        meta, body = parse_doc_metadata(content)
        rel_path = str(doc_path.relative_to(base_dir))
        # 确定版本
        version = "7.X" if "v7" in base_dir else "6.X"

        chunks = split_into_chunks(body)
        title = meta["title"]
        for i, chunk_text in enumerate(chunks):
            path_hash = hashlib.md5(str(rel_path).encode()).hexdigest()[:12]
            chunk_id = f"{version}_{path_hash}_{i:04d}"
            # 在 chunk 内容前加上标题，提升关键词匹配和语义检索效果
            enriched_text = f"# {title}\n\n{chunk_text}" if title else chunk_text
            all_chunks.append(enriched_text)
            all_metas.append({
                "title": meta["title"],
                "doc_id": meta["doc_id"],
                "url": meta["url"],
                "version": version,
                "source": meta["source"],
                "file_path": rel_path,
            })
            all_ids.append(chunk_id)

    logger.info(f"    共生成 {len(all_chunks)} 个 chunks")

    # 3. 创建 ChromaDB 集合（使用内置 ONNX 模型，无需联网）
    logger.info("[3/4] 创建 ChromaDB 集合...")
    os.makedirs(CHROMA_DIR, exist_ok=True)
    client = chromadb.PersistentClient(
        path=CHROMA_DIR,
        settings=Settings(anonymized_telemetry=False),
    )

    # 删除旧集合重建
    try:
        client.delete_collection(COLLECTION_NAME)
        logger.info("    已删除旧集合")
    except Exception:
        pass

    # 使用中文 Embedding 模型（text2vec-base-chinese，768维）
    embedding_func = ChineseTextEmbeddingFunction()
    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_func,
        metadata={
            "hnsw:space": "cosine",
            "description": "FineBI 知识库文档索引（中文 Embedding）",
            "built_at": datetime.now().isoformat(),
            "doc_count": str(len(docs)),
            "chunk_count": str(len(all_chunks)),
            "embedding_model": "shibing624/text2vec-base-chinese",
            "embedding_dim": "768",
        },
    )

    # 4. 预编码 + 批量写入
    logger.info(f"[4/4] 预编码所有 chunks（共 {len(all_chunks)} 条，使用 text2vec-base-chinese）...")
    embedding_func = ChineseTextEmbeddingFunction()
    model = embedding_func.model

    # 批量编码，显示进度条
    all_embeddings = model.encode(
        all_chunks,
        show_progress_bar=True,
        batch_size=64,
        normalize_embeddings=True,
    )

    logger.info(f"    编码完成，维度: {all_embeddings.shape[1]}")

    # 批量写入 ChromaDB
    logger.info("    写入 ChromaDB 索引...")
    batch_count = 0
    for start_idx in range(0, len(all_chunks), BATCH_SIZE):
        end_idx = min(start_idx + BATCH_SIZE, len(all_chunks))
        batch_chunks = all_chunks[start_idx:end_idx]
        batch_metas = all_metas[start_idx:end_idx]
        batch_ids = all_ids[start_idx:end_idx]
        batch_embs = all_embeddings[start_idx:end_idx].tolist()

        collection.add(
            embeddings=batch_embs,
            documents=batch_chunks,
            metadatas=batch_metas,
            ids=batch_ids,
        )
        batch_count += len(batch_chunks)
        logger.info(f"    已写入 {batch_count}/{len(all_chunks)}")

    logger.info("=" * 60)
    logger.info("索引构建完成!")
    logger.info(f"总计: {len(all_chunks)} 个 chunks | {len(docs)} 个文档")
    logger.info(f"集合: {COLLECTION_NAME}")
    logger.info(f"存储: {CHROMA_DIR}")
    logger.info("=" * 60)


def _extract_keywords(query):
    """使用 jieba 提取查询关键词"""
    import jieba
    # 添加 FineBI 专有词汇，确保被正确分词
    custom_words = [
        "数据集", "自助数据集", "仪表板", "数据连接", "数据权限",
        "数据预警", "权限管理", "用户管理", "系统管理",
        "SUM_AG", "DEF类", "同比", "环比", "占比",
        "过滤组件", "图表组件", "表格组件",
        "Excel导入", "数据库", "数据源",
    ]
    for w in custom_words:
        jieba.add_word(w)

    # 过滤停用词和单字
    stop_words = {"的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都",
                  "一", "一个", "上", "也", "很", "到", "说", "要", "去", "你",
                  "会", "着", "没有", "看", "好", "自己", "这", "如何", "怎么",
                  "什么", "怎样", "哪个", "哪些", "设置", "使用", "配置", "创建",
                  "编辑", "删除", "新增", "修改", "查询", "统计", "计算"}
    words = jieba.lcut(query)
    keywords = [w for w in words if len(w) >= 2 and w not in stop_words]
    return keywords


def _keyword_score(content, keywords):
    """计算关键词匹配得分（0-1 之间）"""
    if not keywords or not content:
        return 0.0
    content_lower = content.lower()
    matches = sum(1 for kw in keywords if kw.lower() in content_lower)
    return min(matches / len(keywords), 1.0)


def _calculate_keyword_weights(keywords, query=None):
    """
    根据关键词的特异性计算权重，使技术专有词获得更高权重。

    权重规则：
    - 基础权重：1.0
    - 包含大写字母或下划线的技术术语（如 SUM_AG, DEF, DEF类）：+3.0
    - 包含数字或英文的技术词（如 Excel, 7.X）：+2.0
    - 长度 >= 6 的较长关键词（更具体）：+1.0
    - FineBI 专有词汇额外加成：+2.0
    - 通用词（函数、设置、使用、配置、创建等）：-0.5（最低不低于 0.5）
    - 上下文感知：当通用词与 FineBI 专有词在查询中共同出现时，提升通用词权重
      （如"连接"与"数据库"共同出现时，"连接"被赋予更高权重，因为它是"数据连接"概念的一部分）
    """
    finebi_specific = {
        "SUM_AG", "SUM_AGG", "DEF类", "DEF", "DEF_ADD", "DEF子类",
        "同比", "环比", "占比", "累计值",
        "Excel", "KPI", "SQL",
         "数据预警", "仪表板", "数据集", "自助数据集", "数据连接",
        "数据权限", "权限管理", "格式刷",
        "图表", "图表组件", "表格组件", "过滤组件",
    }
    generic_words = {
        "函数", "如何", "怎么", "怎样", "设置", "使用", "配置",
        "创建", "编辑", "删除", "新增", "修改", "查询", "统计",
        "计算", "添加", "制作", "安装", "连接", "导入", "导出",
        "用法", "方法", "方式", "功能", "说明", "概述", "汇总",
    }
    # 上下文感知：当通用词与这些专有词共同出现时，提升通用词权重
    # 双向提升：当 A 与 B 共同出现时，A 和 B 都获得提升
    context_boost_map = {
        "连接": {"数据库", "数据", "数据源"},
        "过滤": {"条件", "组件"},
        "创建": {"数据集", "图表", "仪表板", "组件"},
        "添加": {"数据集", "图表", "组件", "数据"},
        "设置": {"权限", "预警", "条件"},
        "计算": {"同比", "环比", "占比", "累计值"},
    }
    # 反向上下文提升：当这些词共同出现时，所有相关词都获得提升
    bidir_context_map = {
        "数据库": {"连接"},  # "连接" + "数据库" → 两者都提升
        "数据源": {"连接"},
        "图表": {"添加", "制作", "创建"},  # "添加/制作/创建图表" → 两者都提升
    }

    weights = {}
    for kw in keywords:
        weight = 1.0

        # 技术术语（大写字母、下划线）：更具体
        if re.search(r'[A-Z_]', kw):
            weight += 3.0
        # 包含数字或英文
        if re.search(r'[a-zA-Z0-9]', kw):
            weight += 2.0
        # 较长关键词更具体
        if len(kw) >= 6:
            weight += 1.0
        # FineBI 专有词汇
        if kw in finebi_specific:
            weight += 2.0
        # 通用词降权
        if kw in generic_words:
            weight -= 0.5
        # 上下文感知：检查是否有需要提升的上下文
        if kw in context_boost_map and query:
            query_lower = query.lower()
            for trigger_word in context_boost_map[kw]:
                if trigger_word.lower() in query_lower:
                    weight += 1.5
                    break
        # 双向上下文提升：当两个词在查询中共同出现时，都获得提升
        if kw in bidir_context_map and query:
            query_lower = query.lower()
            for trigger_word in bidir_context_map[kw]:
                if trigger_word.lower() in query_lower:
                    weight += 1.5
                    break

        # 确保最低权重不低于 0.5
        weights[kw] = max(weight, 0.5)

    return weights


def _find_title_match_docs(collection, keywords, limit=2000):
    """
    通过获取所有文档元数据，在 Python 中按标题精确匹配关键词。
    避免 ChromaDB where_document 的 limit 限制导致遗漏。

    优化策略：
    1. 一次性获取所有文档的元数据（title, doc_id, url, version）
    2. 在 Python 中遍历所有文档，逐条检查标题是否包含关键词
    3. 对于匹配的文档，再按需获取其内容片段
    """
    title_match_docs = {}  # doc_id -> info

    # 获取所有文档元数据（仅metadatas，不包含documents，效率更高）
    try:
        all_meta = collection.get(include=["metadatas"])
    except Exception as e:
        logger.debug(f"获取文档元数据失败: {e}")
        return title_match_docs

    if not all_meta["ids"]:
        return title_match_docs

    # 在 Python 中遍历所有文档，按标题匹配关键词
    for i in range(len(all_meta["ids"])):
        title = all_meta["metadatas"][i].get("title", "")
        if not title:
            continue

        doc_id = all_meta["metadatas"][i].get("doc_id", "")
        if not doc_id:
            continue

        # 检查标题是否包含任何关键词
        matched_kws = set()
        for kw in keywords:
            if kw.lower() in title.lower():
                matched_kws.add(kw)

        if not matched_kws:
            continue

        if doc_id not in title_match_docs:
            title_match_docs[doc_id] = {
                "title": title,
                "doc_id": doc_id,
                "url": all_meta["metadatas"][i].get("url", ""),
                "version": all_meta["metadatas"][i].get("version", ""),
                "content": "",
                "matched_kws": matched_kws,
            }
        else:
            title_match_docs[doc_id]["matched_kws"].update(matched_kws)

    # 对匹配的文档，获取其内容片段（用于显示）
    # 批量获取第一个匹配文档的内容，避免多次查询
    matched_doc_ids = list(title_match_docs.keys())
    for doc_id in matched_doc_ids:
        try:
            # 获取该文档在 ChromaDB 中的第一个 chunk 作为内容片段
            doc_results = collection.get(
                where={"doc_id": {"$eq": doc_id}},
                limit=1,
                include=["documents"],
            )
            if doc_results["ids"] and doc_results["documents"]:
                title_match_docs[doc_id]["content"] = doc_results["documents"][0][:500]
        except Exception:
            pass

    return title_match_docs


def search(query, top_k=5, version_filter=None):
    """
    混合搜索：标题关键词匹配 + 语义搜索 + 重排序

    策略：
    1. Phase 1: 通过 where_document 找到标题包含关键词的文档（精确匹配）
    2. Phase 2: 语义搜索获取候选文档
    3. Phase 3: 合并结果，标题匹配的文档给予高权重
    """
    client = chromadb.PersistentClient(
        path=CHROMA_DIR,
        settings=Settings(anonymized_telemetry=False),
    )

    try:
        embedding_func = ChineseTextEmbeddingFunction()
        collection = client.get_collection(
            COLLECTION_NAME,
            embedding_function=embedding_func,
        )
    except Exception as e:
        logger.error(f"索引不存在: {e}")
        return []

    base_where = None
    if version_filter:
        base_where = {"version": {"$eq": version_filter}}

    # 提取关键词
    keywords = _extract_keywords(query)
    logger.info(f"搜索: '{query}' 关键词: {keywords}")

    # 计算关键词权重（技术专有词权重更高，支持上下文感知）
    kw_weights = _calculate_keyword_weights(keywords, query=query)
    total_weight = sum(kw_weights.values()) if kw_weights else 1.0

    # --- Phase 1: 标题关键词精确匹配 ---
    title_match_docs = _find_title_match_docs(collection, keywords)

    # --- Phase 2: 语义搜索（全量） ---
    semantic_results = collection.query(
        query_texts=[query],
        n_results=top_k * 10,
        where=base_where,
    )

    # --- Phase 3: 合并结果并重排序 ---
    scored = []
    seen_doc_ids = set()

    # 构建语义搜索排名索引：doc_id -> 首次出现的语义排名（用于同分文档的二级排序）
    semantic_rank = {}
    if semantic_results["ids"] and semantic_results["ids"][0]:
        for i in range(len(semantic_results["ids"][0])):
            doc_id = semantic_results["metadatas"][0][i].get("doc_id", "")
            if doc_id not in semantic_rank:
                semantic_rank[doc_id] = i

    # 先处理标题匹配的文档（给予高优先级，始终排在语义结果前面）
    title_scored = []
    for doc_id, r in title_match_docs.items():
        seen_doc_ids.add(doc_id)

        # 加权关键词得分：匹配的关键词权重之和 / 总权重
        matched_weight = sum(kw_weights.get(kw, 1.0) for kw in r["matched_kws"])
        kw_score = min(matched_weight / total_weight, 1.0)

        # 标题匹配文档：基础分 0.8 + 加权关键词匹配加分（最高 0.2）
        # 使用加权得分后，匹配了"SUM_AG"（权重高）的文档得分远高于只匹配了"函数"（权重低）的文档
        base_score = 0.8 + kw_score * 0.2

        # 语义排名作为二级排序键（同分文档中，语义排名越靠前越先展示）
        sem_pos = semantic_rank.get(doc_id, 9999)

        title_scored.append({
            "title": r["title"],
            "doc_id": doc_id,
            "url": r["url"],
            "version": r["version"],
            "content": r["content"][:500],
            "score": base_score,
            "keyword_score": kw_score,
            "semantic_rank": sem_pos,
        })

    # 按 kw_score 降序（主），semantic_rank 升序（次）排序
    title_scored.sort(key=lambda x: (-x["keyword_score"], x["semantic_rank"]))
    scored.extend(title_scored)

    # 再处理语义搜索结果（补充未被标题匹配覆盖的文档）
    if semantic_results["ids"] and semantic_results["ids"][0]:
        for i in range(len(semantic_results["ids"][0])):
            doc_id = semantic_results["metadatas"][0][i].get("doc_id", "")
            if doc_id in seen_doc_ids:
                continue
            seen_doc_ids.add(doc_id)

            semantic_score = 1 - semantic_results["distances"][0][i] if semantic_results.get("distances") else 0

            # 语义分数低于 0.5 的结果基本是噪声，跳过
            if semantic_score < 0.5:
                continue

            content = semantic_results["documents"][0][i]
            title = semantic_results["metadatas"][0][i].get("title", "")

            # 检查标题是否包含关键词（加权计算）
            title_kw_matches = [kw for kw in keywords if kw.lower() in title.lower()]
            matched_weight = sum(kw_weights.get(kw, 1.0) for kw in title_kw_matches)
            kw_score = min(matched_weight / total_weight, 1.0) if keywords else 0.0

            # 语义 70% + 加权关键词匹配 30%，但整体不超过 0.8（确保低于标题匹配文档）
            hybrid_score = min(semantic_score * 0.7 + kw_score * 0.3, 0.8)

            scored.append({
                "title": title,
                "doc_id": doc_id,
                "url": semantic_results["metadatas"][0][i].get("url", ""),
                "version": semantic_results["metadatas"][0][i].get("version", ""),
                "content": content[:500],
                "score": hybrid_score,
                "semantic_score": semantic_score,
                "keyword_score": kw_score,
            })

    # 按分数排序
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_k]


if __name__ == "__main__":
    build_index()