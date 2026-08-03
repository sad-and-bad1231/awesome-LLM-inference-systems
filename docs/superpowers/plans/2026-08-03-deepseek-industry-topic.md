# DeepSeek Industry Topic Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate one compact DeepSeek AI systems topic in both industrial Markdown views from structured industry records.

**Architecture:** Records opt in through `presentation.topic = "deepseek-ai-systems"` and provide a fixed `presentation.topic_group`. A shared selector and renderer in `reading.py` produces deterministic, deduplicated rows; both internal and public renderers consume it.

**Tech Stack:** Python 3.11, JSONL, `unittest`, Markdown renderers.

---

### Task 1: Shared topic selection and rendering

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/reading.py`
- Test: `tests/ai_infra_monitor/test_reading.py`

- [ ] **Step 1: Write the failing selector test**

Create two tagged DeepSeek records, one duplicate project release, and one untagged third-party record. Assert that `select_industry_topic(records, "deepseek-ai-systems")` returns only the two official projects in the fixed group order.

- [ ] **Step 2: Run the test and verify RED**

Run:

```powershell
python -m unittest tests.ai_infra_monitor.test_reading.ReadingTests.test_industry_topic_is_explicit_deduplicated_and_group_sorted
```

Expected: import or attribute failure because the selector does not exist.

- [ ] **Step 3: Implement the minimal selector and Markdown renderer**

Add constants for the five group labels, `select_industry_topic(records, topic)`, and `render_industry_topic(records, topic, summary_max_chars=240)`. Select only explicit tags, deduplicate by project key/canonical identity, sort by group then title, and render a compact table with category, project, system role, and primary link.

- [ ] **Step 4: Run the focused test and verify GREEN**

Run the Step 2 command. Expected: `OK`.

### Task 2: Add the topic to both industrial views

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/records.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/publication.py`
- Test: `tests/ai_infra_monitor/test_records.py`
- Test: `tests/ai_infra_monitor/test_publication.py`

- [ ] **Step 1: Write failing renderer tests**

Add tagged DeepSeek and untagged third-party fixtures. Assert that both generated files contain `DeepSeek AI 系统专题`, contain the tagged project once, and omit the third-party item from the topic section.

- [ ] **Step 2: Run both focused tests and verify RED**

```powershell
python -m unittest tests.ai_infra_monitor.test_records tests.ai_infra_monitor.test_publication
```

Expected: assertions fail because neither view renders the topic.

- [ ] **Step 3: Call the shared renderer from both views**

Insert the rendered topic after the industrial observation/evidence section and before the normal seven-theme project list. Do not alter ordinary project aggregation or exploration.

- [ ] **Step 4: Run both focused test modules and verify GREEN**

Run the Step 2 command. Expected: all tests pass.

### Task 3: Populate facts and regenerate views

**Files:**
- Modify: `data/industry.jsonl`
- Regenerate: `industrial-llm-inference-systems.md`
- Regenerate: `industry/README.md`
- Regenerate as needed by existing commands: other generated Markdown views

- [ ] **Step 1: Tag existing official DeepSeek records**

Add `presentation.topic` and `presentation.topic_group` to existing MLA, FlashMLA, DeepGEMM/DeepEP, and DeepSeek architecture records that are backed by official or formal sources.

- [ ] **Step 2: Add missing compact official records**

Add separate project records for DeepEP, DeepGEMM, 3FS, DeepSpec, TileKernels, DeepSeek-OCR, DeepSeek-OCR-2, and the two official ecosystem collections when their official URLs resolve. Keep mutable star counts out of the facts.

- [ ] **Step 3: Render and validate**

```powershell
python scripts/ai_infra_monitor/monitor.py curate
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
python -m unittest discover -s tests -p "test_*.py"
```

Expected: validation passes and all tests pass.

- [ ] **Step 4: Verify deterministic output and scope**

Run `render` and `publish` again and compare hashes of generated views. Confirm the DeepSeek heading occurs once per industrial view, no raw HTML appears, and unrelated working-tree changes remain present.
