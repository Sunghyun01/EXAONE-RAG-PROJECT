# 04. Enterprise Connector Design

## 1. Concept

기업에서는 사용자가 AI에 문서를 직접 업로드하기보다, 각 업무 영역에 맞는 시스템에 문서를 업로드한다.

따라서 AI 시스템은 문서를 직접 받는 구조가 아니라, 업무 시스템에 저장된 문서를 수집하고 색인하는 구조로 설계한다.

```text
업무 시스템
→ Document Connector
→ Parser & Chunker
→ Embedding
→ Elasticsearch
→ RAG API
```

---

## 2. Target Systems

```text
- SharePoint
- Google Drive
- Confluence
- Jira
- Notion
- 사내 게시판
- 사내 문서관리 시스템
- S3/Object Storage
- 업무 DB
```

---

## 3. Collection Flow

```text
[업무 시스템]
SharePoint / Google Drive / Confluence / Jira / S3 / 사내 게시판 / DB
        |
        | API / Webhook / Batch / Scheduler
        v
[Document Connector]
        |
        | 문서 다운로드 / 변경분 확인 / 권한 정보 수집
        v
[Parser & Chunker]
        |
        | PDF, DOCX, XLSX, HTML, Markdown 파싱
        v
[Embedding 생성]
        |
        | Ollama Embedding Model
        v
[Elasticsearch]
        |
        | Keyword + Vector Index
        v
[Python RAG API]
        |
        | 질문 → Elasticsearch 검색 → EXAONE 답변 생성
        v
[Open WebUI or Custom Chat UI]
```

---

## 4. Pull 방식

AI 수집 서버가 주기적으로 업무 시스템 API를 호출해서 신규/수정/삭제 문서를 가져오는 방식이다.

```text
매 10분마다 업무 시스템 확인
→ 신규 문서 확인
→ 수정 문서 확인
→ 삭제 문서 확인
→ 변경된 문서만 Elasticsearch 재색인
```

### 장점

```text
- 업무 시스템 수정이 적어도 됨
- 배치 기반으로 구현하기 쉬움
- 초기 프로젝트에 적합
```

### 단점

```text
- 실시간성이 낮음
- 주기 설정에 따라 반영 지연 발생 가능
```

---

## 5. Push 방식

업무 시스템에서 문서가 등록/수정/삭제될 때 AI 수집 서버로 이벤트를 보내는 방식이다.

```text
문서 등록
→ 업무 시스템에서 Webhook 호출
→ AI 수집 서버가 해당 문서만 수집
→ Elasticsearch 업데이트
```

### 장점

```text
- 실시간 반영 가능
- 불필요한 전체 조회 감소
```

### 단점

```text
- 업무 시스템에서 Webhook/API 연동을 지원해야 함
- 시스템별 구현 난이도가 다름
```

---

## 6. Full Sync / Incremental Sync

### Full Sync

전체 문서를 다시 수집해서 색인하는 방식이다.

```text
전체 문서 조회
→ 전체 문서 다운로드
→ 전체 문서 파싱
→ 전체 Chunk 생성
→ Elasticsearch 재색인
```

사용 시점:

```text
- 최초 구축 시
- 인덱스 구조 변경 시
- 대량 재색인이 필요할 때
```

### Incremental Sync

변경된 문서만 수집해서 색인하는 방식이다.

```text
마지막 동기화 시간 확인
→ 신규/수정/삭제 문서만 조회
→ 변경된 문서만 처리
→ Elasticsearch 업데이트
```

사용 시점:

```text
- 운영 중 주기적 동기화
- 문서 변경분 반영
- 성능 최적화
```
