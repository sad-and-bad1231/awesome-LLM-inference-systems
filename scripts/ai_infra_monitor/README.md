# AI Infra Monitor

Pure-standard-library discovery and bookkeeping for the research index.

Run commands from the workspace root:

```powershell
python scripts/ai_infra_monitor/monitor.py init
python scripts/ai_infra_monitor/monitor.py discover --mode daily
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py publish
```

`data/papers.jsonl` and `data/industry.jsonl` are the main fact sources; `data/candidates.jsonl` is discovery staging. Markdown files are generated views.
`paper-list.md` and `industrial-llm-inference-systems.md` are separate reading lists. `ai-infra-system-abstractions.md` is only a concise navigation index.
The public repository views also include `README.md`, `papers/README.md`, and `industry/README.md`, plus the local diagrams under `figs/`. Optional `presentation` metadata controls a small curated set of featured entries without changing the fact schema.

One-time migration of a legacy unified JSONL export:

```powershell
python scripts/ai_infra_monitor/monitor.py migrate --source <legacy-jsonl>
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
```

Daily automation:

```powershell
python scripts/ai_infra_monitor/monitor.py discover --mode daily
python scripts/ai_infra_monitor/monitor.py triage --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py queue --run-id <run-id> --tiers A B C
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py finalize --run-id <run-id> --no-commit
```

Weekly automation uses the same flow, with `--mode weekly`, followed by
`report` and `finalize` without `--no-commit` only when a commit is intended.
