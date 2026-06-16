# AI Infra Monitor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local, scheduled AI infrastructure research monitor that discovers only new material, applies evidence policy, updates the knowledge base, validates it, and creates local Git commits.

**Architecture:** A dependency-free Python CLI handles deterministic discovery, state, deduplication, candidate manifests, Markdown validation and Git finalization. Two Codex cron jobs perform semantic verification and summaries using the compact manifests.

**Tech Stack:** Python 3 standard library, Markdown, JSON-compatible YAML, Git, Codex cron automations.

---

### Task 1: Repository and contracts

**Files:**
- Create: `.gitignore`
- Create: `ai-infra-sources.yaml`
- Create: `ai-infra-state.example.json`
- Create: `ai-infra-candidates.md`
- Create: `docs/ai-infra-monitor-workflow.md`

- [ ] Define evidence tiers, source records, query groups and daily/weekly limits.
- [ ] Document the exact discover, validate and finalize commands.
- [ ] Initialize Git and commit the approved design before implementation.

### Task 2: Core models and normalization

**Files:**
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/models.py`
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/identity.py`
- Test: `tests/ai_infra_monitor/test_identity.py`

- [ ] Write tests for DOI, arXiv, URL and normalized-title identities.
- [ ] Implement immutable candidate records and deterministic identity selection.
- [ ] Verify `python -m unittest tests.ai_infra_monitor.test_identity -v` passes.

### Task 3: Source fetchers and parsers

**Files:**
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/fetch.py`
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/parsers.py`
- Test: `tests/ai_infra_monitor/test_parsers.py`
- Create: `tests/ai_infra_monitor/fixtures/feed.xml`
- Create: `tests/ai_infra_monitor/fixtures/index.html`

- [ ] Test Atom/RSS and HTML link extraction from local fixtures.
- [ ] Implement conditional HTTP fetching with ETag and Last-Modified.
- [ ] Implement GitHub release, OpenReview note, feed and HTML-index adapters.
- [ ] Verify parser tests pass without network access.

### Task 4: State and discovery pipeline

**Files:**
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/state.py`
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/discovery.py`
- Test: `tests/ai_infra_monitor/test_discovery.py`

- [ ] Test pending-candidate persistence and second-run deduplication.
- [ ] Implement daily/weekly source selection, keyword matching and candidate caps.
- [ ] Write compact `runs/<id>/candidates.json` manifests.
- [ ] Record source errors without aborting the run.

### Task 5: Markdown quality gates

**Files:**
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/validation.py`
- Test: `tests/ai_infra_monitor/test_validation.py`

- [ ] Test malformed table rows, duplicate paper titles, duplicate solution names, empty links and conflict markers.
- [ ] Implement validation for both main documents and candidate pool.
- [ ] Return non-zero status with actionable file and line diagnostics.

### Task 6: Candidate pool, reports and Git finalization

**Files:**
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/output.py`
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/git_ops.py`
- Test: `tests/ai_infra_monitor/test_output.py`

- [ ] Test candidate Markdown generation and stable ordering.
- [ ] Implement weekly report scaffolding from run statistics.
- [ ] Implement scoped staging, local commits, no-op behavior and state finalization.

### Task 7: CLI and end-to-end tests

**Files:**
- Create: `scripts/ai_infra_monitor/monitor.py`
- Create: `scripts/ai_infra_monitor/README.md`
- Create: `tests/ai_infra_monitor/test_cli.py`

- [ ] Expose `init`, `discover`, `validate`, `report`, `finalize` and `status`.
- [ ] Run a fixture-only discovery twice and verify the second run emits no duplicate.
- [ ] Run the complete unittest suite.
- [ ] Run validation against the current 337-paper and 216-solution documents.

### Task 8: Scheduled automations

**Files:**
- Modify: Codex automation configuration through `automation_update`.

- [ ] Create daily local automation for Sunday-Friday at 22:00 Asia/Shanghai.
- [ ] Create weekly local automation for Saturday at 22:00 Asia/Shanghai.
- [ ] Include primary-source verification, candidate routing, validation and local commit instructions.
- [ ] View both automations and verify active status, workspace and schedule.
