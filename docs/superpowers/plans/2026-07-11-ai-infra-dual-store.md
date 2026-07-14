# AI Infra Dual-Store Knowledge Base Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Split the AI Infra knowledge base into paper and industry fact stores with canonical identity, evidence separation, serving-focused triage, and generated Markdown views.

**Architecture:** `data/papers.jsonl` and `data/industry.jsonl` are the main stores; `data/candidates.jsonl` is discovery staging. The monitor routes promotion by record kind, renders three separate Markdown views plus a compact abstraction index, and validates stores independently and across canonical IDs.

**Tech Stack:** Python 3 standard library, JSONL, YAML configuration, unittest, existing monitor CLI.

---

### Task 1: Lock the new data contract with tests

**Files:**
- Modify: `tests/ai_infra_monitor/test_records.py`
- Modify: `tests/ai_infra_monitor/test_cli.py`

- [ ] Add tests for canonical aliases (`Prism`, `Contextra`, `LLMFabric`), independent paper/industry/candidate stores, and queue routing.
- [ ] Run the focused tests and confirm failure because the new APIs do not exist.

### Task 2: Add canonical identity and evidence normalization

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/records.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/identity.py`

- [ ] Add `canonical_id`, `aliases`, `status_history`, and `evidence` to every normalized record.
- [ ] Merge the three approved title aliases without merging unrelated papers with the same short name.
- [ ] Add split-store migration helpers and cross-store canonical validation.
- [ ] Run record tests after each implementation slice.

### Task 3: Route discovery and queue through separate JSONL stores

**Files:**
- Modify: `scripts/ai_infra_monitor/monitor.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/output.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/records.py`
- Modify: `ai-infra-sources.yaml`

- [ ] Write discovered candidates to `data/candidates.jsonl`.
- [ ] Promote paper candidates to `data/papers.jsonl` and industry/project candidates to `data/industry.jsonl`.
- [ ] Mark promoted staging records and reject cross-store duplicates.
- [ ] Add serving-core scope configuration and keep existing source definitions intact.

### Task 4: Render and validate separate views

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/records.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/validation.py`
- Modify: `scripts/ai_infra_monitor/monitor.py`
- Modify: `docs/ai-infra-monitor-workflow.md`
- Modify: `scripts/ai_infra_monitor/README.md`

- [ ] Render paper, industry, candidate, and abstraction views from their respective stores.
- [ ] Validate schema, URL, enums, duplicate canonical IDs, and generated Markdown separately.
- [ ] Update daily, weekly, queue, finalize, and manual commands to use the three-store flow.

### Task 5: Migrate, retire side list, and verify

**Files:**
- Create: `data/papers.jsonl`
- Create: `data/industry.jsonl`
- Create: `data/candidates.jsonl`
- Delete: `data/infra-db.jsonl`
- Delete: `long-cot-kv-retention-literature.md`
- Regenerate: `paper-list.md`, `industrial-llm-inference-systems.md`, `ai-infra-candidates.md`, `ai-infra-system-abstractions.md`

- [ ] Migrate existing records with parity counts before canonical merges and report the intentional three-title merges.
- [ ] Render all generated views.
- [ ] Run the complete unittest suite and `monitor.py validate`.
- [ ] Confirm no command or generated file references `infra-db.jsonl` or the retired long-COT side list.
