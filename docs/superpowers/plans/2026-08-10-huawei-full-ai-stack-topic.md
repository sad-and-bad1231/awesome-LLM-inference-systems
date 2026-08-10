# Huawei Full AI Stack Topic Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the verified Huawei Ascend inference topic with bounded framework, cloud-platform, and Kunpeng infrastructure anchors.

**Architecture:** Add three declarative groups to the existing Huawei topic and four explicit primary-source facts. Keep broad platform records adjacent to the seven-theme mainline, while CloudMatrix384 remains a core production inference system; reuse all existing selectors, budgets, and renderers.

**Tech Stack:** Python 3, `unittest`, JSONL, Markdown render/publish pipeline.

---

### Task 1: Define the second-stage contract with RED tests

**Files:**
- Modify: `tests/ai_infra_monitor/test_reading.py`
- Modify: `tests/ai_infra_monitor/test_validation.py`

- [ ] Add Huawei fixtures for production, training, cloud, and CPU/heterogeneous groups; assert the rendered category order.
- [ ] Assert the Huawei configured groups exactly include the seven approved group keys.
- [ ] Run the two focused tests and confirm they fail because the three second-stage groups are absent.

### Task 2: Add configuration and facts

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/reading.py`
- Modify: `data/industry.jsonl`

- [ ] Append `training-frameworks`, `cloud-platform`, and `cpu-heterogeneous` to the Huawei topic configuration.
- [ ] Add official-source facts for CloudMatrix384, MindSpore, ModelArts, and Kunpeng BoostKit inference acceleration.
- [ ] Classify CloudMatrix384 as core production inference; classify the three broad-stack records as adjacent with no guide themes.
- [ ] Run focused reading and validation tests and confirm GREEN.

### Task 3: Regenerate and verify

**Files:**
- Modify: `docs/START-HERE.md`
- Regenerate: internal and public Markdown views selected by render/publish.

- [ ] Update the Huawei reading path with the second-stage framework/platform/infrastructure sequence.
- [ ] Run render, publish, all unit tests, validate, and audit.
- [ ] Run render and publish again and confirm generated-file hashes do not drift.
- [ ] Review `git diff --check`, commit the second stage, and leave the worktree clean.
