import os
from datetime import datetime
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
DOCUMENT_INDEX_NAME = os.getenv("DOCUMENT_INDEX_NAME", "exaone-rag-documents")


def get_elasticsearch_client() -> Elasticsearch:
    return Elasticsearch(ELASTICSEARCH_URL)


def check_elasticsearch_health() -> dict:
    es = get_elasticsearch_client()

    if not es.ping():
        return {
            "status": "error",
            "message": "Elasticsearch connection failed",
            "url": ELASTICSEARCH_URL,
        }

    info = es.info()

    return {
        "status": "ok",
        "message": "Elasticsearch connected",
        "url": ELASTICSEARCH_URL,
        "cluster_name": info.get("cluster_name"),
        "version": info.get("version", {}).get("number"),
    }


def create_document_index_if_not_exists() -> dict:
    es = get_elasticsearch_client()

    if es.indices.exists(index=DOCUMENT_INDEX_NAME):
        return {
            "status": "exists",
            "index": DOCUMENT_INDEX_NAME,
        }

    mapping = {
        "mappings": {
            "properties": {
                "doc_id": {"type": "keyword"},
                "chunk_id": {"type": "keyword"},
                "title": {"type": "text"},
                "content": {"type": "text"},
                "source_path": {"type": "keyword"},
                "created_at": {"type": "date"},
            }
        }
    }

    es.indices.create(index=DOCUMENT_INDEX_NAME, **mapping)

    return {
        "status": "created",
        "index": DOCUMENT_INDEX_NAME,
    }


def index_document_chunk(
    doc_id: str,
    chunk_id: str,
    title: str,
    content: str,
    source_path: str,
) -> dict:
    es = get_elasticsearch_client()

    document = {
        "doc_id": doc_id,
        "chunk_id": chunk_id,
        "title": title,
        "content": content,
        "source_path": source_path,
        "created_at": datetime.utcnow().isoformat(),
    }

    result = es.index(
        index=DOCUMENT_INDEX_NAME,
        id=chunk_id,
        document=document,
    )

    return {
        "result": result.get("result"),
        "index": DOCUMENT_INDEX_NAME,
        "chunk_id": chunk_id,
    }


def refresh_document_index() -> None:
    es = get_elasticsearch_client()
    es.indices.refresh(index=DOCUMENT_INDEX_NAME)


def search_documents(query: str, size: int = 5) -> dict:
    es = get_elasticsearch_client()

    result = es.search(
        index=DOCUMENT_INDEX_NAME,
        query={
            "match": {
                "content": query
            }
        },
        size=size,
    )

    hits = result.get("hits", {}).get("hits", [])

    return {
        "query": query,
        "total": result.get("hits", {}).get("total", {}),
        "results": [
            {
                "score": hit.get("_score"),
                "doc_id": hit.get("_source", {}).get("doc_id"),
                "chunk_id": hit.get("_source", {}).get("chunk_id"),
                "title": hit.get("_source", {}).get("title"),
                "content": hit.get("_source", {}).get("content"),
                "source_path": hit.get("_source", {}).get("source_path"),
            }
            for hit in hits
        ],
    }