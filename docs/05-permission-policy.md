# 05. Permission Based Search Policy

## 1. Concept

기업형 RAG에서 가장 중요한 부분은 권한 처리다.

사용자가 볼 수 없는 문서는 AI 답변에도 사용되면 안 된다.

---

## 2. Permission Example

```text
문서 A → 인사팀만 조회 가능
문서 B → 전사 조회 가능
문서 C → 운영팀만 조회 가능
문서 D → 특정 사용자만 조회 가능
```

---

## 3. Metadata Design

문서 Chunk를 저장할 때 단순히 본문만 저장하지 않고, 출처와 권한 Metadata를 함께 저장한다.

```text
doc_id
chunk_id
source_system
source_url
title
content
embedding
last_modified_at
indexed_at
owner
department
allowed_users
allowed_groups
security_level
document_type
page_no
```

---

## 4. Search Filtering Flow

검색 시 사용자의 권한 정보를 기준으로 Elasticsearch Query Filter를 적용한다.

```text
사용자 질문
→ 사용자 ID / 부서 / 그룹 확인
→ Elasticsearch 검색 시 allowed_users, allowed_groups 조건 적용
→ 사용자가 접근 가능한 Chunk만 검색
→ EXAONE 답변 생성
```

---

## 5. Permission Policy Direction

```text
- 사용자가 접근 가능한 문서만 검색 대상에 포함
- 검색 결과 Chunk에도 권한 필터 적용
- LLM Prompt에는 권한 통과 문서만 전달
- 답변 출처도 사용자가 볼 수 있는 문서만 표시
```

---

## 6. Future Enhancement

```text
- 사용자별 권한 캐시 적용
- 부서/직무/직책 기반 권한 확장
- 문서 보안등급 기반 필터링
- 관리자용 권한 검증 화면 추가
- 답변 로그에 사용된 문서 출처 기록
```
