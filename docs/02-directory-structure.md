# 02. Directory Structure

## 1. Root Structure

```text
exaone-rag-project/
├─ README.md
├─ docker-compose.yml
├─ .env
├─ .gitignore
│
├─ backend/
├─ infra/
├─ data/
├─ notebooks/
└─ docs/
```

---

## 2. Full Directory Plan

```text
exaone-rag-project/
├─ README.md
├─ docker-compose.yml
├─ .env
├─ .gitignore
│
├─ backend/                         # Python 개발환경 / RAG API 서버
│  ├─ app/
│  │  ├─ main.py                    # FastAPI 진입점
│  │  │
│  │  ├─ api/                       # API 라우터
│  │  │  ├─ chat.py                 # 질문/답변 API
│  │  │  ├─ documents.py            # 문서 업로드/관리 API
│  │  │  └─ search.py               # Elasticsearch 검색 API
│  │  │
│  │  ├─ connectors/                # 업무 시스템 문서 수집 Connector
│  │  │  ├─ base_connector.py
│  │  │  ├─ local_file_connector.py
│  │  │  ├─ sharepoint_connector.py
│  │  │  ├─ google_drive_connector.py
│  │  │  ├─ confluence_connector.py
│  │  │  └─ db_connector.py
│  │  │
│  │  ├─ jobs/                      # 동기화 Job
│  │  │  ├─ sync_scheduler.py
│  │  │  ├─ full_sync_job.py
│  │  │  └─ incremental_sync_job.py
│  │  │
│  │  ├─ services/
│  │  │  ├─ ollama_service.py        # Ollama / EXAONE 호출
│  │  │  ├─ elastic_service.py       # Elasticsearch 색인/검색
│  │  │  ├─ document_sync_service.py # 문서 수집 통합 처리
│  │  │  ├─ permission_sync_service.py
│  │  │  ├─ parser_service.py        # 문서 파싱
│  │  │  ├─ chunk_service.py         # Chunk 분할
│  │  │  ├─ embedding_service.py     # Embedding 생성
│  │  │  └─ rag_service.py           # RAG 답변 생성 흐름
│  │  │
│  │  ├─ prompts/
│  │  │  └─ system_prompt.txt        # 시스템 프롬프트
│  │  │
│  │  ├─ schemas/                    # 요청/응답 DTO
│  │  └─ config/                     # 환경설정
│  │
│  ├─ tests/
│  ├─ requirements.txt
│  └─ Dockerfile
│
├─ infra/                            # Docker/인프라 설정
│  ├─ elasticsearch/
│  │  ├─ mappings/                   # Elasticsearch index mapping
│  │  └─ settings/                   # analyzer, index 설정
│  │
│  ├─ open-webui/
│  │  └─ config/
│  │
│  └─ scripts/                       # 초기화 스크립트
│
├─ data/
│  ├─ uploads/                       # 업로드 문서 원본
│  ├─ parsed/                        # 파싱된 텍스트
│  └─ samples/                       # 테스트용 샘플 문서
│
├─ notebooks/
│  └─ rag_test.ipynb
│
└─ docs/
   ├─ 01-architecture.md
   ├─ 02-directory-structure.md
   ├─ 03-rag-flow.md
   ├─ 04-enterprise-connector.md
   ├─ 05-permission-policy.md
   ├─ 06-version-roadmap.md
   └─ 07-development-plan.md
```

---

## 3. Directory Role Summary

```text
backend
→ Python 기반 RAG API 서버 영역

infra
→ Elasticsearch, Open WebUI, Docker 관련 설정 영역

data
→ 테스트용 문서 및 파싱 결과 저장 영역

notebooks
→ RAG 흐름, 검색 품질, Embedding 테스트용 실험 영역

docs
→ 설계 문서 및 프로젝트 문서화 영역
```
