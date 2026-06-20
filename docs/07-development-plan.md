# 07. Development Plan

## 1. Development Direction

이 프로젝트는 단순히 Local LLM을 실행하는 데서 끝나는 것이 아니라, 실제 기업 환경에서 사용할 수 있는 문서 검색형 AI 시스템을 목표로 한다.

초기 버전에서는 백엔드 구조와 검색/색인 흐름을 우선 구축하고, 이후 Web UI와 사용자 편의성 개선을 통해 실제 사용 가능한 서비스 형태로 확장한다.

```text
개발자 중심 RAG API
→ 사용자 중심 Web UI
→ 기업형 문서 검색 AI 서비스
```

---

## 2. Recommended Development Order

초기에는 복잡한 외부 시스템부터 붙이지 말고, 로컬 폴더 기반 수집부터 구현하는 것이 좋다.

```text
1단계: Ollama + EXAONE 실행
2단계: Elasticsearch Docker 구성
3단계: Python Backend 기본 API 구성
4단계: local_file_connector 구현
5단계: 특정 폴더 내 문서 자동 색인
6단계: 질문 → Elasticsearch 검색 → EXAONE 답변 생성
7단계: Open WebUI 연동
8단계: Confluence / Google Drive / SharePoint Connector 확장
9단계: Incremental Sync 구현
10단계: 권한 기반 검색 필터 적용
```

---

## 3. MVP Scope

v1.0에서 우선 집중할 범위는 다음과 같다.

```text
- Ollama 기반 EXAONE 실행
- Elasticsearch 실행
- Python Backend 기본 구조 구성
- 로컬 폴더 기반 문서 수집
- 문서 파싱 및 Chunk 분할
- Embedding 생성
- Elasticsearch 색인
- 질문 기반 문서 검색
- 검색 결과 기반 EXAONE 답변 생성
```

---

## 4. Future Scope

이후 버전에서는 다음 항목을 확장한다.

```text
- Web UI 추가
- 사용자 편의성 UI/UX 개선
- 업무 시스템 Connector 확장
- 권한 기반 검색 필터 고도화
- 관리자 대시보드 추가
- 답변 로그 및 피드백 기능 추가
- 모델 교체 및 프롬프트 설정 관리
```

---

## 5. Project Positioning

```text
단순 문서 업로드 챗봇
→ 개인용 프로젝트 느낌

Connector 기반 문서 수집 + Elasticsearch RAG
→ 기업형 프로젝트 느낌
```

따라서 이 프로젝트는 단순히 AI에 파일을 올리는 방식이 아니라, 업무 시스템에 저장된 문서를 AI가 수집하고 색인하는 구조로 설계한다.

---

## 6. Core Keywords

```text
- Local LLM
- EXAONE
- Ollama
- Elasticsearch
- RAG
- Document Connector
- Incremental Sync
- Permission Filtering
- Open WebUI
- Python Backend
- Docker Container
- Web UI
- UI/UX
```
