from app.services.elastic_service import search_documents
from app.services.ollama_service import generate_answer


def build_rag_prompt(question: str, search_results: list[dict]) -> str:
    context_text = ""

    for idx, result in enumerate(search_results, start=1):
        context_text += f"""
[문서 {idx}]
제목: {result.get("title")}
출처: {result.get("source_path")}
내용:
{result.get("content")}
"""

    prompt = f"""
너는 기업 문서 기반 질의응답 AI Assistant다.

아래 참고 문서 내용만 기반으로 답변해라.
문서에 없는 내용은 추측하지 말고 "문서에서 확인되지 않습니다."라고 답해라.
답변은 한국어로 작성해라.

[참고 문서]
{context_text}

[사용자 질문]
{question}

[답변 형식]
1. 결론
2. 근거
3. 참고 문서
"""

    return prompt


def ask_rag(question: str, size: int = 5) -> dict:
    search_response = search_documents(query=question, size=size)
    search_results = search_response.get("results", [])

    if not search_results:
        return {
            "question": question,
            "answer": "관련 문서를 찾지 못했습니다.",
            "sources": [],
        }

    prompt = build_rag_prompt(question, search_results)
    llm_response = generate_answer(prompt)

    return {
        "question": question,
        "answer": llm_response.get("answer"),
        "model": llm_response.get("model"),
        "sources": [
            {
                "title": item.get("title"),
                "source_path": item.get("source_path"),
                "chunk_id": item.get("chunk_id"),
                "score": item.get("score"),
                "content": item.get("content"),
            }
            for item in search_results
        ],
    }