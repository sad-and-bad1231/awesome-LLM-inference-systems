# AI Infra Monitor Workflow

The JSONL stores are the fact sources. Markdown files are generated views and must not be edited by hand:

- `ai-infra-system-abstractions.md`: concise primary navigation view with counts and representative records.
- `data/papers.jsonl` -> `paper-list.md`: academic paper store and view.
- `data/industry.jsonl` -> `industrial-llm-inference-systems.md`: industry/project store and view.
- `data/candidates.jsonl` -> `ai-infra-candidates.md`: discovery staging and audit view.
- `data/papers.jsonl` + `data/industry.jsonl` -> `README.md`, `papers/README.md`, `industry/README.md`: public Awesome-style views.

The retired long-COT side list is no longer part of the active workflow.

## Schema Policy

Every JSONL record must include `id`, `canonical_id`, `aliases`, `status_history`, `evidence`, `record_type`, `title`, `venue_or_channel`, `year`, `orgs`, `summary`, `source_tier`, `primary_url`, `artifact_url`, `source_ids`, `status`, `system_abstraction_primary`, `system_abstraction_secondary`, `technical_tags`, and `triage`.

`system_abstraction_primary` must be one of:

- `Memory Topology & Virtualization`
- `Disaggregated Interconnects`
- `State Compression & Signal Coding`
- `Execution Compilation & Kernel Fusion`
- `Program-Aware Scheduling`
- `SRE/Fault-Tolerance/Sparing`

`technical_tags` must contain `phase`, `hardware`, `optimization_layer`, `workload`, `framework_binding`, and `metrics`. The monitor uses these tags for views and for SRE metrics such as `TTFT under Drift`, `Generation Stall Rate`, and `Numerical Reproducibility`.

Records may include an optional `presentation` object with `featured`, non-negative integer `order`, and display-only `blurb` fields. It controls a small set of public entry points and never changes evidence or triage semantics.

## Initial Migration

Run from `D:\ResearchWork`:

```powershell
python scripts/ai_infra_monitor/monitor.py init
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
```

For a legacy unified JSONL export, run `monitor.py migrate --source <legacy-jsonl>` once. After migration, agents should append or update the matching JSONL store only, then regenerate Markdown with `render`. Papers and industry solutions must not be merged into one reading file.

## Display Policy

- Keep `ai-infra-system-abstractions.md` short enough to scan. It should show entry points, coverage counts, SRE metrics, and representative items rather than every row.
- Keep full detail in `data/papers.jsonl` and `data/industry.jsonl`; the abstraction file is only a navigation index.
- Keep dropped candidates available for audit, but do not mix them into the active candidate table.
- Keep `figs/ai-inference-systems-cover.png` and `figs/ai-inference-system-map.png` tracked with their SVG sources; public README links must remain local and stable.
- Do not add another top-level index file unless it replaces an existing view.

## Daily Automation

Goal: collect signals and queue high/normal-priority candidates without hand-editing generated Markdown.

Model policy: use GPT-5.6 Luna with medium reasoning. Daily work is mostly scripted discovery, triage, render, and validation, so the cheapest GPT-5.6 model is the default.

```powershell
python scripts/ai_infra_monitor/monitor.py discover --mode daily
python scripts/ai_infra_monitor/monitor.py triage --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py queue --run-id <run-id> --tiers A B C
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py finalize --run-id <run-id> --no-commit
```

Daily automation runs Sunday through Friday at 22:00 Beijing time. The daily cap is configured by `settings.daily_limit`; candidates are sorted by triage priority before the cap is applied.

## Weekly Automation

Goal: batch confirmation, reporting, and optional commit.

Model policy: use GPT-5.6 Terra with high reasoning. Weekly work includes more judgment-heavy confirmation and reporting, but still should not default to Sol unless explicitly requested for a deep review.

```powershell
0..5 | ForEach-Object {
  python scripts/ai_infra_monitor/monitor.py discover --mode weekly --source-batch-index $_ --source-batch-count 6
}
python scripts/ai_infra_monitor/monitor.py triage --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py queue --run-id <run-id> --tiers A B C
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py report --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py finalize --run-id <run-id> --no-commit
```

Weekly automation runs Saturday at 22:00 Beijing time. The source pool is partitioned into bounded batches so one slow conference page cannot block the full sweep; each returned run ID is triaged and queued before rendering. Omit `--no-commit` only when a local commit is explicitly intended.

The equivalent single-command lifecycle is:

```powershell
python scripts/ai_infra_monitor/monitor.py sweep --mode weekly --source-batch-count 6 --report
```

`sweep` performs discovery, triage, queue, optional report, and finalize for every batch. A triage or queue failure stops the current batch before later lifecycle steps, while later bounded batches can still run and be resumed independently. Intermediate batches validate JSONL and update state without rebuilding the global Markdown/public views; the final batch performs the full render and Markdown validation. This avoids repeating repository-wide rendering six times in a bounded sweep. It does not create a commit by default.

When a long sweep is interrupted, resume a range without repeating completed batches:

```powershell
python scripts/ai_infra_monitor/monitor.py sweep --mode weekly --source-batch-count 6 --start-batch-index 2 --end-batch-index 5 --report
```

## Triage Pipeline

The first version is deterministic and does not call an external LLM API.

- Metadata rules downrank algorithmic-only simulation/proof records when no hardware, kernel, runtime, serving, or framework signal appears.
- GitHub repo inspection records language and root-path signals where available. If the API is unavailable or rate-limited, the candidate is kept and `triage.repo_signals.unavailable` is written.
- Ecosystem bindings promote records mentioning vLLM, SGLang, TensorRT-LLM, KServe, llm-d, LMCache, Kubernetes, or Docker.
- Raw low-priority discoveries remain in the run manifest; triage only materializes `keep` records with `high` or `normal` priority into `data/candidates.jsonl`. The `compact` command converts legacy non-actionable candidate rows to `drop` without deleting their evidence.
- `triage.llm_review` is reserved for a future strict expert review step.

## Finalize Gate

`finalize` runs in this order:

1. Validate JSONL schema, duplicates, enums, URLs, and candidate/verified conflicts.
2. Render all internal Markdown views from JSONL.
3. Render the public Awesome-style README views.
4. Validate generated Markdown shape, links, and duplicate rows.
5. Update run state.
6. Optionally commit local changes.

Automations must never push. Runtime state, run manifests, reports, and temporary files remain local unless intentionally committed.

## Recovery

- Network and GitHub API errors stay in the run manifest or `triage.repo_signals`; do not delete state to hide the error.
- If `validate` fails, fix the relevant JSONL store or renderer and rerun `render` plus `validate`.
- Do not manually patch generated Markdown except as a temporary debugging step; the next render will overwrite it.
