# AI Infra Monitor Workflow

The JSONL stores are the fact sources. Markdown files are generated views and must not be edited by hand:

- `ai-infra-system-abstractions.md`: concise primary navigation view with counts and representative records.
- `data/papers.jsonl` -> `paper-list.md`: academic paper store and view.
- `data/industry.jsonl` -> `industrial-llm-inference-systems.md`: industry/project store and view.
- `data/candidates.jsonl` -> `ai-infra-candidates.md`: recent actionable staging and audit view.
- `data/archive/candidates/candidates-YYYY-MM.jsonl.gz`: immutable cold audit shards for old terminal candidates.
- `data/papers.jsonl` + `data/industry.jsonl` -> `README.md`, `papers/README.md`, `industry/README.md`: public Awesome-style views.

The retired long-COT side list is no longer part of the active workflow.

## Schema Policy

Every JSONL record must include `id`, `canonical_id`, `aliases`, `status_history`, `evidence`, `record_type`, `title`, `venue_or_channel`, `year`, `orgs`, `summary`, `source_tier`, `primary_url`, `artifact_url`, `source_ids`, `status`, `system_abstraction_primary`, `system_abstraction_secondary`, `technical_tags`, and `triage`. Records also receive deterministic `curation` metadata: `scope` (`core|adjacent|archive`) and `priority` (`foundation|frontier|supporting`). Every core record additionally has explicit `evidence.affiliation_status`, `evidence.artifact_status`, `evidence.metadata_checked_at`, and `evidence.metadata_sources`; legacy presence and unreviewed gaps are not equivalent to verification.

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

- Treat the JSONL stores as the complete fact layer. Generated reading views contain a guide-aligned mainline, a deterministic 180-day exploration window, and links to the retained archive.
- Organize both research and engineering views around seven themes: Attention/Kernel, KV Cache, Prefill-Decode transport, speculative decoding, MoE, Compiler/DSL, and Runtime/Scheduling.
- Collapse industry release streams to one row per project. Raw release notes remain in JSONL; generated summaries are HTML-free and capped at 240 characters.
- Keep at most 20 evidenced exploration entries per internal track and 15 per public track. Public mainline budgets are 8 papers and 5 aggregated industry projects per theme, plus 8 entries per company topic. The window is relative to the newest stored evidence date so rendering is reproducible.
- Use `python scripts/ai_infra_monitor/monitor.py audit` for a compact, summary-free view of evidence gaps, duplicates, theme coverage, long release notes, and projected public sizes.
- Keep `ai-infra-system-abstractions.md` short enough to scan. It should show entry points, coverage counts, SRE metrics, and representative items rather than every row.
- Keep full detail in `data/papers.jsonl` and `data/industry.jsonl`; the abstraction file is only a navigation index.
- Keep dropped candidates available for audit, but do not mix them into the active candidate table. `maintain` moves terminal candidates older than 180 days into deterministic monthly gzip shards; daily rendering reads only the hot store and archive counts.
- Keep `figs/ai-inference-systems-cover.png` and `figs/ai-inference-system-map.png` tracked with their SVG sources; public README links must remain local and stable.
- Do not add another top-level index file unless it replaces an existing view.

## Daily Automation

Goal: collect signals and queue high/normal-priority candidates without hand-editing generated Markdown. Reading attention is separate: only `core` records enter the main public views; `adjacent` and `archive` records are retained in `archive/README.md`.

Model policy: use GPT-5.6 Luna with medium reasoning. Daily work is mostly scripted discovery, triage, render, and validation, so the cheapest GPT-5.6 model is the default.

```powershell
python scripts/ai_infra_monitor/monitor.py discover --mode daily
python scripts/ai_infra_monitor/monitor.py triage --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py queue --run-id <run-id> --tiers A B C
python scripts/ai_infra_monitor/monitor.py curate
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
python scripts/ai_infra_monitor/monitor.py curate
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py report --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py maintain
python scripts/ai_infra_monitor/monitor.py finalize --run-id <run-id> --no-commit
```

Weekly automation runs Saturday at 22:00 Beijing time. The source pool is partitioned into bounded batches so one slow conference page cannot block the full sweep; each returned run ID is triaged and queued before rendering. Omit `--no-commit` only when a local commit is explicitly intended.

The equivalent single-command lifecycle is:

```powershell
python scripts/ai_infra_monitor/monitor.py sweep --mode weekly --source-batch-count 6 --report
```

`sweep` performs discovery, triage, queue, optional report, and finalize for every batch. A triage or queue failure stops the current batch before later lifecycle steps, while later bounded batches can still run and be resumed independently. Intermediate batches validate JSONL and update state without rebuilding the global Markdown/public views; the final successful weekly batch runs `maintain`, then performs the full render and Markdown validation. Daily sweeps do not run maintenance. This avoids repeating repository-wide work six times in a bounded sweep. It does not create a commit by default.

## Lightweight Data Maintenance

`maintain` keeps routine automation bounded without changing the paper or industry fact stores:

```powershell
python scripts/ai_infra_monitor/monitor.py maintain
```

Only `drop` and `promote` candidates are eligible for movement. Records older than `settings.candidate_hot_window_days` are archived, and the recent terminal set is additionally bounded by `settings.candidate_hot_terminal_limit` (default 500) so a large conference sweep cannot inflate the hot store. Active and undated candidates remain in `data/candidates.jsonl`; cold records are deduplicated by canonical identity and stored in deterministic monthly gzip shards. Old terminal rows in the ignored local state file lose redundant title, URL, and run ID fields but retain identity, fingerprint, source, status, and last-seen date. The command is idempotent and prints one compact JSON summary.

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

`curate` backfills or refreshes guide-based reading scope and priority without changing source facts. `finalize` runs in this order:

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
- If `maintain` encounters invalid hot JSONL or a damaged gzip shard, it exits without deleting source evidence. Repair or restore the affected file, then rerun the same command.
- Do not manually patch generated Markdown except as a temporary debugging step; the next render will overwrite it.
