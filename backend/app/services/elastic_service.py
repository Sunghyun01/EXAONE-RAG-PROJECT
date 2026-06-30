import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")


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