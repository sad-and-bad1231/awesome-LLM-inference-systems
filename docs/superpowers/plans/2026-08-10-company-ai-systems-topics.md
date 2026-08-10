# Company AI Systems Topics Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add deterministic Kimi, MiniMax, GLM, StepFun, and ByteDance AI-system topic views beside the existing DeepSeek topic.

**Architecture:** Replace the single hard-coded DeepSeek renderer metadata with an ordered topic registry while retaining explicit record tags and project-level deduplication. Add only screenshot-derived records confirmed by official organization pages, official repositories, or formal paper pages, then render all configured topics through one shared entry point.

**Tech Stack:** Python 3 standard library, JSONL facts, Markdown renderers, `unittest`.

---

### Task 1: Configurable topic renderer

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/reading.py`
- Test: `tests/ai_infra_monitor/test_reading.py`

- [ ] **Step 1: Write the failing tests**

Add tests that construct records tagged `moonshot-ai-systems` and `minimax-ai-systems`, call `render_industry_topic` and a new `render_industry_topics`, and assert configured titles, fixed group order, explicit-tag isolation, and project deduplication.

- [ ] **Step 2: Run tests to verify RED**

Run: `python -m unittest tests.ai_infra_monitor.test_reading`

Expected: failure because the renderer still hard-codes the DeepSeek heading and `render_industry_topics` does not exist.

- [ ] **Step 3: Implement the ordered registry**

Define `INDUSTRY_TOPICS` with keys in this order:

```python
(
    "deepseek-ai-systems",
    "moonshot-ai-systems",
    "minimax-ai-systems",
    "zhipu-ai-systems",
    "stepfun-ai-systems",
    "bytedance-ai-systems",
)
```

Each entry supplies `title`, `description`, and ordered `(group_key, label)` pairs. Preserve DeepSeek's existing labels; use compact company-specific labels for model architecture, inference systems, training/data, multimodal/agents, and tools/ecosystem. Make `render_industry_topic` read the registry and return empty text for an unknown or empty topic. Add `render_industry_topics(records, summary_max_chars=240)` that joins all non-empty configured sections.

- [ ] **Step 4: Run tests to verify GREEN**

Run: `python -m unittest tests.ai_infra_monitor.test_reading`

Expected: all reading tests pass.

### Task 2: Shared rendering in both industry views

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/records.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/publication.py`
- Test: `tests/ai_infra_monitor/test_records.py`
- Test: `tests/ai_infra_monitor/test_publication.py`

- [ ] **Step 1: Write the failing tests**

Add one tagged Moonshot record and one tagged MiniMax record to each existing industry fixture. Assert both headings occur exactly once and that untagged third-party records remain outside the topic section.

- [ ] **Step 2: Run tests to verify RED**

Run: `python -m unittest tests.ai_infra_monitor.test_records tests.ai_infra_monitor.test_publication`

Expected: the new company headings are absent.

- [ ] **Step 3: Use the batch renderer**

Replace the two single-topic calls with `render_industry_topics(industry_source, summary_max_chars=display_summary_max_chars)`. Keep placement before the main resource list unchanged.

- [ ] **Step 4: Run tests to verify GREEN**

Run: `python -m unittest tests.ai_infra_monitor.test_records tests.ai_infra_monitor.test_publication`

Expected: all renderer tests pass.

### Task 3: Verified company records

**Files:**
- Modify: `data/industry.jsonl`
- Test: `tests/ai_infra_monitor/test_validation.py`

- [ ] **Step 1: Write a failing data-contract test**

Load `data/industry.jsonl`, collect `presentation.topic`, and assert the six configured topics are present. For the five new topics assert every tagged row has a non-empty official/formal URL, `evidence.verification_level == "official_source"`, and an allowed `topic_group` from the registry.

- [ ] **Step 2: Run the test to verify RED**

Run: `python -m unittest tests.ai_infra_monitor.test_validation`

Expected: the five new topics are absent.

- [ ] **Step 3: Tag existing verified rows and add a bounded official set**

Tag the existing Mooncake and ShadowKV rows. Add official rows for: Kimi-K3, Kimi-K2.5, Kimi-K2, Kimi-Linear, FlashKDA, checkpoint-engine, kimi-code; MiniMax-M2.7, MiniMax-M3, cli, MiniMax-MCP, OpenRoom, Mini-Agent, VTP; GLM-5, GLM-V, GLM-Image, Synapse; Step-3.7-Flash, Step-3.5-Flash, SteptronOss, Step-Audio2, Step-Realtime-CLI, Step1X-Edit, gelab-zero; Seed-1.8, ShadowKV, VeOmni, and CCCL only when its ByteDance affiliation is explicit on the formal source. Use `verified_at: 2026-08-10`, source tier A, neutral summaries, and no mutable popularity counts.

- [ ] **Step 4: Run curation and the contract test**

Run: `python scripts/ai_infra_monitor/monitor.py curate`

Run: `python -m unittest tests.ai_infra_monitor.test_validation`

Expected: curation completes and the data-contract test passes without changing raw summaries.

### Task 4: Regenerate and verify

**Files:**
- Regenerate: `industrial-llm-inference-systems.md`
- Regenerate: `industry/README.md`

- [ ] **Step 1: Run the full suite**

Run: `python -m unittest discover -s tests -p "test_*.py"`

Expected: all tests pass.

- [ ] **Step 2: Render, publish, and validate**

Run: `python scripts/ai_infra_monitor/monitor.py render`

Run: `python scripts/ai_infra_monitor/monitor.py publish`

Run: `python scripts/ai_infra_monitor/monitor.py validate`

Expected: both views contain each non-empty topic once and validation passes.

- [ ] **Step 3: Verify idempotence and content hygiene**

Hash generated views, rerun `render` and `publish`, and compare hashes. Search both views for raw release HTML and duplicate topic headings.

Expected: hashes are unchanged, every configured heading count is one, and no release HTML is present.

- [ ] **Step 4: Review the final diff**

Run: `git diff --check`

Run: `git status --short`

Expected: no whitespace errors; unrelated user files remain untouched and untracked assets remain present.
