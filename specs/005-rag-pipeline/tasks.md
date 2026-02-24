# Implementation Tasks: RAG Pipeline

**Feature Branch**: `005-rag-pipeline`

## Phase 1: Foundation Models

- [ ] Create `src/vindicta_oracle/models/rag.py`
  - [ ] Implement `RulesSegment` model extending `VindictaModel` (include embedding vector, URL, hash, timestamp, version id).
  - [ ] Implement `AgentQuery` model extending `VindictaModel`.
  - [ ] Update `src/vindicta_oracle/models/__init__.py` to export the new models.
- [ ] Ensure strict type hinting (`mypy`) is applied to new models.

## Phase 2: Ingest & Scraping Pipeline (`scraper.py`)

- [ ] Create `src/vindicta_oracle/rag_pipeline/scraper.py`.
- [ ] Integrate `crawl4ai` to scrape dynamic JS-rendered websites (FR-001).
- [ ] Implement DOM element extraction to clean markdown optimized for LLMs (FR-002).
- [ ] Implement SHA-256 chunk hashing to identify unique content changes.
- [ ] Ensure the ingest pipeline ignores completely duplicate/unchanged content (FR-003, SC-003).
- [ ] Write unit tests in `tests/unit/test_scraper.py` covering DOM extraction and hashing.

## Phase 3: Storage Layer (`storage.py`)

- [ ] Create `src/vindicta_oracle/rag_pipeline/storage.py`.
- [ ] Initialize embedded ChromaDB local database with SQLite metadata persistence (FR-004).
- [ ] Integrate local `ollama` client for generating text embeddings.
- [ ] Implement save/upsert logic for `RulesSegment` ensuring newest chunks shadow or version older segments (FR-006).
- [ ] Write unit tests in `tests/unit/test_storage.py` covering chunk saving and querying.

## Phase 4: MCP Server (`server.py`)

- [ ] Create `src/vindicta_oracle/mcp_server/server.py`.
- [ ] Implement the standard Model Context Protocol (MCP) server interface (FR-005).
- [ ] Expose `search_40k_rules` tool to allow Vindicta agents to query rules.
- [ ] Connect the MCP tool to `storage.py` querying logic for retrieving relevant markdown rules excerpts.
- [ ] Write integration test `tests/integration/test_mcp_server.py` verifying end-to-end local latency expectations (< 1.5 seconds) and context retrieval (SC-001, SC-002).

## Phase 5: CI & Validation

- [ ] Validate 90% test coverage using `uv run pytest`.
- [ ] Run `ruff check .` and `ruff format --check .` to ensure compliance.
- [ ] Run `mypy` strict type checking across the entire `vindicta_oracle` module.
