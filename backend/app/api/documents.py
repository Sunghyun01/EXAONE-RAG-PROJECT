from fastapi import APIRouter, Query
from app.services.document_service import read_text_file, split_text_to_chunks
from app.services.elastic_service import (
    create_document_index_if_not_exists,
    index_document_chunk,
    refresh_document_index,
    search_documents,
)

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/index-sample")
def index_sample_document():
    sample_path = "data/samples/sample.txt"
    title = "sample.txt"
    doc_id = "sample-doc-001"

    create_document_index_if_not_exists()

    text = read_text_file(sample_path)
    chunks = split_text_to_chunks(text)

    indexed_chunks = []

    for idx, chunk in enumerate(chunks):
        chunk_id = f"{doc_id}-{idx + 1}"

        result = index_document_chunk(
            doc_id=doc_id,
            chunk_id=chunk_id,
            title=title,
            content=chunk,
            source_path=sample_path,
        )

        indexed_chunks.append(result)

    refresh_document_index()

    return {
        "status": "ok",
        "message": "Sample document indexed",
        "doc_id": doc_id,
        "chunk_count": len(indexed_chunks),
        "chunks": indexed_chunks,
    }


@router.get("/search")
def search_document_chunks(
    q: str = Query(..., description="Search keyword"),
    size: int = Query(5, description="Search result size"),
):
    return search_documents(query=q, size=size)