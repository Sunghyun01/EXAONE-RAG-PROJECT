# 06. Version History and Roadmap

## v1.0.0 - Initial Architecture

현재까지 정리한 Local EXAONE RAG Project의 초기 구성안을 v1.0으로 정의한다.

v1.0의 핵심 목표는 Local LLM 기반 RAG 시스템의 기본 아키텍처를 설계하고, Elasticsearch를 활용한 문서 검색 및 색인 구조를 구성하는 것이다.

### Main Scope

```text
- EXAONE 기반 Local LLM 사용
- Ollama를 통한 LLM 실행 환경 구성
- Docker Container 기반 실행 구조 설계
- Python Backend 개발환경 구성
- Elasticsearch 기반 Keyword / Vector Search 적용
- 문서 Chunking 및 Embedding 처리 구조 설계
- 업무 시스템 Connector 기반 문서 수집 구조 반영
- Full Sync / Incremental Sync 개념 적용
- 권한 기반 문서 검색 구조 설계
```

---

## v1.1.0 - Web UI Extension

이후 버전에서는 사용자 접근성을 높이기 위해 Web UI 기능을 추가한다.

### Planned Features

```text
- Web Chat UI 추가
- 문서 검색 화면 구성
- 질문/답변 이력 조회
- 답변 출처 표시 UI
- 문서별 검색 결과 확인
- Elasticsearch 검색 Score 확인 화면
- 사용자별 접근 가능 문서 필터링 화면
```

---

## v1.2.0 - UI/UX Improvement

Web UI 적용 이후에는 사용자 편의성을 높이기 위한 UI/UX 개선 작업을 진행한다.

### Planned Features

```text
- 직관적인 채팅 화면 구성
- 문서 출처 및 근거 문단 표시 개선
- 로딩 상태 및 답변 생성 상태 표시
- 검색 결과 하이라이팅
- 문서 업로드/동기화 상태 확인 화면
- 관리자용 문서 색인 현황 대시보드
- 사용자 피드백 기능 추가
```

---

## v1.3.0 - Enterprise Feature Enhancement

기업형 사용 환경을 고려하여 운영 및 관리 기능을 확장한다.

### Planned Features

```text
- 사용자 권한 기반 검색 필터 고도화
- 부서/그룹 단위 접근 제어
- Connector별 동기화 상태 관리
- 문서 변경 이력 관리
- 답변 로그 및 검색 로그 저장
- 관리자 설정 화면 추가
- 모델 변경 및 프롬프트 설정 관리
```

---

## Roadmap Summary

```text
v1.0
→ Local LLM + Ollama + Python Backend + Elasticsearch 기반 RAG 구조 설계

v1.1
→ Web UI 추가 및 기본 채팅/검색 화면 구성

v1.2
→ 사용자 편의성 중심 UI/UX 개선

v1.3
→ 기업형 권한 관리, 동기화 관리, 운영 기능 고도화
```
