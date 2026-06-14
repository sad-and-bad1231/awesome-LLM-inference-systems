# AI Infra Monitor

Pure-standard-library discovery and bookkeeping for the research index.

Run commands from the workspace root:

```powershell
python scripts/ai_infra_monitor/monitor.py init
python scripts/ai_infra_monitor/monitor.py discover --mode daily
python scripts/ai_infra_monitor/monitor.py validate
```

Discovery is deterministic. Semantic verification and concise summaries are
performed by the scheduled Codex task from the generated run manifest.
