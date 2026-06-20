# 01. System Architecture

## 1. Overview

EXAONE RAG Project는 로컬 LLM 기반의 기업형 문서 검색 AI 시스템을 목표로 한다.

기본 구조는 다음과 같다.

```text
[사용자]
   |
   v
[Open WebUI or Custom Chat UI]
   |
   v
[Python Backend / RAG API Server]
   |
   +----------------------------+
   |                            |
   v                            v
[Ollama + EXAONE]          [Elasticsearch]
- 답변 생성                  - 문서 Chunk 저장
- Embedding 생성             - Keyword 검색
                             - Vector 검색
                             - Metadata 검색
```

---

## 2. Main Components

### Ollama + EXAONE

```text
- 로컬 LLM 실행
- 사용자 질문에 대한 답변 생성
- Embedding 생성에 활용 가능
```

### Python Backend

```text
- 문서 파싱
- Chunk 분할
- Embedding 생성
- Elasticsearch 색인
- 사용자 질문 처리
- RAG 답변 생성
```

### Elasticsearch

```text
- 문서 Chunk 저장
- Keyword 검색
- Vector 검색
- Hybrid 검색
- Metadata 기반 필터링
```

### Open WebUI or Custom Web UI

```text
- 로컬 ChatGPT 형태의 UI
- Ollama 모델 연결
- 추후 Tool Server 또는 API 연동 가능
```

### Docker Container

```text
- Elasticsearch, Open WebUI, Backend 실행 환경 분리
- 로컬 환경 오염 최소화
- 서비스별 독립 실행 구조 구성
```

---

## 3. Recommended Runtime Structure

```text
Ollama
→ 로컬 PC에 설치하여 EXAONE 모델 실행

Elasticsearch
→ Docker Container로 실행

Python Backend
→ Python 개발환경에서 구현 후 Docker Container 적용

Open WebUI
→ 초기에는 선택 적용, 이후 Web UI 단계에서 확장
```
