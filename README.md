# EXAONE RAG Project

Local LLM 기반의 기업형 RAG 문서 검색 시스템 구축 프로젝트입니다.

EXAONE 모델을 Ollama로 실행하고, Python Backend와 Elasticsearch를 활용하여 문서 검색, 벡터 검색, 권한 기반 검색 구조를 설계합니다.

---

## Project Summary

```text
LLM Model      : EXAONE
LLM Framework  : Ollama
Backend        : Python
Search Engine  : Elasticsearch
Runtime        : Docker Container
UI             : Open WebUI or Custom Web UI
Architecture   : Enterprise RAG Search System
```

---

## Table of Contents

### 1. Architecture

- [System Architecture](./docs/01-architecture.md)
- [RAG Processing Flow](./docs/03-rag-flow.md)

### 2. Project Structure

- [Directory Structure](./docs/02-directory-structure.md)

### 3. Enterprise Document Collection

- [Enterprise Connector Design](./docs/04-enterprise-connector.md)
- [Permission Based Search Policy](./docs/05-permission-policy.md)

### 4. Version & Roadmap

- [Version History and Roadmap](./docs/06-version-roadmap.md)
- [Development Plan](./docs/07-development-plan.md)

---

## Core Concept

이 프로젝트는 단순히 AI에 문서를 직접 업로드하는 챗봇이 아니라, 기업 내 업무 시스템에 저장된 문서를 수집하고 색인하여 검색 기반 답변을 제공하는 구조를 목표로 합니다.

```text
업무 시스템 문서
→ Document Connector
→ Parser & Chunker
→ Embedding
→ Elasticsearch
→ RAG API
→ EXAONE 답변 생성
```

---

## Version

현재 구성안은 `v1.0.0` 기준입니다.

```text
v1.0.0
→ Local LLM + Ollama + Python Backend + Elasticsearch 기반 RAG 구조 설계

v1.1.0
→ Web UI 추가

v1.2.0
→ 사용자 편의성 중심 UI/UX 개선

v1.3.0
→ 기업형 권한 관리 및 운영 기능 고도화
```
