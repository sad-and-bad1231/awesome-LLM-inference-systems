# Huawei Ascend AI Systems Topic Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a verified Huawei Ascend inference-systems company topic to both industrial reading views while preserving the seven-theme classification and raw fact stores.

**Architecture:** Extend the existing declarative `INDUSTRY_TOPICS` registry with one explicitly tagged topic. Reuse the shared selector and renderer, add only primary-source project anchors missing from `data/industry.jsonl`, and verify ordering, evidence, bounded output, and deterministic generation through existing tests and CLI commands.

**Tech Stack:** Python 3, `unittest`, JSONL fact stores, Markdown render/publish pipeline.

---

### Task 1: Lock the topic contract with failing tests

**Files:**
- Modify: `tests/ai_infra_monitor/test_reading.py`
- Modify: `tests/ai_infra_monitor/test_validation.py`

- [ ] **Step 1: Add a renderer ordering test**

Extend `test_configured_industry_topics_render_in_fixed_order` with an explicitly tagged `huawei-ascend-ai-systems` MindIE record and assert that its heading follows the ByteDance heading, includes MindIE, and excludes an untagged third-party Ascend record.

- [ ] **Step 2: Add a fact-store evidence assertion**

Extend the company-topic validation so the expected configured topic set includes Huawei Ascend and every Huawei record uses one of `hardware-toolchain`, `inference-runtime`, `serving-kv`, or `production-systems`.

- [ ] **Step 3: Run the focused tests and verify RED**

Run: `python -m unittest tests.ai_infra_monitor.test_reading.ReadingTests.test_configured_industry_topics_render_in_fixed_order tests.ai_infra_monitor.test_validation.ValidationTests.test_company_topic_records_have_official_evidence_and_valid_groups`

Expected: FAIL because `huawei-ascend-ai-systems` is not yet configured or present in the fact store.

### Task 2: Add the declarative topic and verified facts

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/reading.py`
- Modify: `data/industry.jsonl`

- [ ] **Step 1: Add the topic configuration**

Append `huawei-ascend-ai-systems` to `INDUSTRY_TOPICS` with the four fixed groups from the design. Keep it after `bytedance-ai-systems` so all generated views use the same order.

- [ ] **Step 2: Tag existing verified records**

Add explicit presentation metadata to P/D-Serve, Ascend-vLLM prefix caching/KV offload, MindIE, CachedAttention, and other directly relevant records only when the existing source is official or a formal paper/program.

- [ ] **Step 3: Add missing official anchors**

Add compact project facts for the official CANN/Ascend C documentation and `vllm-project/vllm-ascend` repository. Use stable project keys, neutral summaries, official URLs, `verified` status, and `official_source` evidence; do not copy release notes.

- [ ] **Step 4: Run the focused tests and verify GREEN**

Run: `python -m unittest tests.ai_infra_monitor.test_reading tests.ai_infra_monitor.test_validation`

Expected: PASS.

### Task 3: Update navigation and regenerate views

**Files:**
- Modify: `docs/START-HERE.md`
- Regenerate: `industrial-llm-inference-systems.md`
- Regenerate: `industry/README.md`
- Regenerate: other renderer-owned Markdown and derived curation metadata as selected by the CLI

- [ ] **Step 1: Update the human reading guide**

Add the Huawei Ascend topic to the company-topic list and describe the first-stage reading order as toolchain → runtime → Serving/KV. State that MindSpore, ModelArts, Kunpeng, and broader platform ecology are reserved for the second stage.

- [ ] **Step 2: Regenerate all views**

Run: `python scripts/ai_infra_monitor/monitor.py render` and `python scripts/ai_infra_monitor/monitor.py publish`.

- [ ] **Step 3: Run full verification**

Run: `python -m unittest discover -s tests -p "test_*.py"`, then `python scripts/ai_infra_monitor/monitor.py validate`.

Expected: all tests pass and validation reports no errors.

- [ ] **Step 4: Verify deterministic generation**

Record hashes for generated views, run render and publish a second time, and confirm hashes and `git diff` do not change.

### Task 4: Commit the completed first stage

**Files:**
- Stage only the design, plan, tests, topic configuration, verified fact additions, reading guide, and generated views changed by this feature.

- [ ] **Step 1: Review the diff**

Run: `git status --short` and `git diff --check`.

Expected: no whitespace errors and no unrelated files.

- [ ] **Step 2: Commit**

Run: `git commit -m "feat: add Huawei Ascend AI systems topic"` after staging the reviewed files.

