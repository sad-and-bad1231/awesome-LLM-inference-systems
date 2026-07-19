# Lightweight Data Maintenance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Keep daily and weekly monitoring focused on recent conference acceptances and official industry work by moving old terminal candidates to deterministic cold archives and compacting local state.

**Architecture:** Add a focused `maintenance.py` module that owns candidate rotation, archive inspection, and state compaction. Existing record stores remain unchanged; the CLI exposes one idempotent `maintain` command and invokes it only at the end of a successful weekly sweep. Candidate Markdown receives archive metadata without loading archived record bodies.

**Tech Stack:** Python 3 standard library (`gzip`, `json`, `tempfile`, `datetime`, `pathlib`), `unittest`, existing argparse CLI.

---

### Task 1: Candidate hot/cold rotation

**Files:**
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/maintenance.py`
- Create: `tests/ai_infra_monitor/test_maintenance.py`

- [ ] Write failing tests proving that only old `drop/promote` records move, undated and active records stay hot, gzip output is deterministic, identities are deduplicated, and a second run changes nothing.
- [ ] Run `python -m unittest tests.ai_infra_monitor.test_maintenance -v` and confirm failures are caused by the missing module/API.
- [ ] Implement `archive_candidates(candidate_path, archive_dir, hot_window_days, today=None)` using original record dictionaries, stable identity ordering, deterministic `gzip.compress(..., mtime=0)`, temporary files, and atomic replacement.
- [ ] Re-run the maintenance tests and confirm they pass.

### Task 2: Compact local state

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/maintenance.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/state.py`
- Modify: `tests/ai_infra_monitor/test_maintenance.py`

- [ ] Add failing tests proving old terminal state rows lose only `title`, `url`, and `run_id`, while active/recent rows and deduplication fields remain unchanged.
- [ ] Run the focused test and confirm the expected failure.
- [ ] Implement `compact_state_data` and `maintain_data`; change `save_state` to compact deterministic JSON while retaining atomic replacement.
- [ ] Re-run focused tests and the existing discovery tests.

### Task 3: CLI and weekly integration

**Files:**
- Modify: `scripts/ai_infra_monitor/monitor.py`
- Modify: `ai-infra-sources.yaml`
- Modify: `tests/ai_infra_monitor/test_cli.py`

- [ ] Add failing CLI tests for the `maintain` command, compact one-line output, weekly-last-batch invocation, and no invocation for daily or intermediate weekly batches.
- [ ] Run the selected CLI tests and confirm behavioral failures.
- [ ] Add archive settings to path resolution, implement `command_maintain`, register the parser, and call it before final weekly rendering only after successful triage/queue/report.
- [ ] Re-run CLI tests and confirm the existing resumable sweep lifecycle remains valid.

### Task 4: Compact candidate view and documentation

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/records.py`
- Modify: `scripts/ai_infra_monitor/monitor.py`
- Modify: `tests/ai_infra_monitor/test_records.py`
- Modify: `docs/ai-infra-monitor-workflow.md`
- Modify: `scripts/ai_infra_monitor/README.md`

- [ ] Add a failing rendering test showing that cold archive counts and links appear while archived bodies are absent.
- [ ] Run the selected records test and confirm it fails for the missing archive summary.
- [ ] Extend `render_markdown_views` with optional archive metadata and render only hot records plus compact per-shard counts.
- [ ] Document `maintain`, weekly-only maintenance, hot/cold boundaries, and recovery behavior.
- [ ] Run records/publication/CLI tests.

### Task 5: Migration and verification

**Files:**
- Generated: `data/archive/candidates/*.jsonl.gz`
- Generated: `data/candidates.jsonl`
- Generated: `ai-infra-candidates.md`

- [ ] Record pre-migration candidate counts, active-status counts, and bytes.
- [ ] Run the full unit suite.
- [ ] Run `maintain`, `render`, `publish`, and `validate`.
- [ ] Repeat the four commands and verify no new diff.
- [ ] Compare hot plus cold identity counts and verify active counts are unchanged.
- [ ] Review `git diff --check`, `git status --short`, and affected-file diffs to ensure existing user changes were preserved.
