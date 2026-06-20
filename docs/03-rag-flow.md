# 03. RAG Processing Flow

## 1. Document Indexing Flow

문서를 수집하고 검색 가능한 형태로 변환하는 흐름이다.

```text
문서 수집
→ 문서 파싱
→ Chunk 분할
→ Embedding 생성
→ Elasticsearch 저장
```

---

## 2. Document Processing Detail

### 1단계: 문서 수집

```text
- 로컬 폴더
- SharePoint
- Google Drive
- Confluence
- Jira
- 사내 게시판
- 사내 문서관리 시스템
- 업무 DB
```

### 2단계: 문서 파싱

```text
- PDF
- DOCX
- XLSX
- HTML
- Markdown
- TXT
```

### 3단계: Chunk 분할

```text
- 문서를 검색하기 좋은 단위로 분할
- Chunk 크기와 Overlap 정책 적용
- 문서 출처와 페이지 번호 Metadata 유지
```

### 4단계: Embedding 생성

```text
- Chunk 단위로 Embedding 생성
- Ollama Embedding Model 또는 별도 임베딩 모델 사용
```

### 5단계: Elasticsearch 저장

```text
- Chunk 본문 저장
- Embedding Vector 저장
- 문서 Metadata 저장
- 권한 정보 저장
```

---

## 3. Question Answering Flow

사용자 질문에 대해 검색 결과 기반으로 답변을 생성하는 흐름이다.

```text
사용자 질문
→ 질문 Embedding 생성
→ Elasticsearch 검색
→ 관련 Chunk 추출
→ RAG Prompt 생성
→ EXAONE 답변 생성
→ 출처 포함 응답 반환
```

---

## 4. Search Strategy

초기에는 Keyword Search와 Vector Search를 모두 고려한다.

```text
Keyword Search
→ 특정 용어, 시스템명, 문서명 검색에 유리

Vector Search
→ 의미 기반 검색에 유리

Hybrid Search
→ Keyword Search + Vector Search 결과를 조합
```

---

## 5. Answer Policy

LLM이 임의로 답변하지 않도록 문서 기반 답변 정책을 적용한다.

```text
- 검색된 문서 내용만 기반으로 답변
- 문서에 없는 내용은 추측하지 않음
- 답변에 출처 표시
- 근거 Chunk를 함께 제공
```
