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

Discovery is intentionally resumable and low-cost: source pages are scanned first, while repository inspection and core-serving triage happen in the explicit `triage` step. Use repeatable `--source-id` arguments to sweep a large conference or ecosystem source incrementally. HTTP fetches use the configurable `max_parallel_fetches` worker pool, while parsing and state updates remain deterministic in source order. GitHub-backed triage uses the configurable `max_parallel_triage` worker pool and writes results back in input order. Candidates are retained with a verdict; only `high` and `normal` priority records are queued into the fact stores. The `max_candidates_per_source` setting prevents a single large DBLP or program page from monopolizing a run; high-priority overflow is deferred, while low-priority overflow is recorded as suppressed in the run manifest and does not force a repeated full fetch.

`html_program` sources handle conference programs whose paper titles are rendered as plain text blocks or event-modal anchors. `html_bold_program` handles accepted-paper lists rendered as bold titles inside table/list items or paragraphs. `html_heading_program` handles accepted lists using `h3` paper headings, `html_linklings_program` handles Linklings `ttip_object_info` presentation slots, `html_icdcs_program` extracts numbered paper rows from ICDCS-style program tables while ignoring session headers, `html_prefixed_program` extracts tagged entries such as `CLD_REG_113:` from cloud program pages, `html_paragraph_anchor_program` handles paper anchors nested in paragraph records, `html_author_paragraph_program` strips author prefixes from paragraph citations, `html_classed_title_program` extracts titles from a configured CSS class, `html_paper_id_list` extracts list entries marked with `paper-id` and `paper-authors` spans, `html_dblp_titles` extracts only DBLP publication entries, `html_paper_block_program` extracts strong titles from `paper` blocks, `html_table_title_program` extracts numbered title rows with a configurable title column, and `html_embedded_full_papers` extracts full-paper titles embedded as escaped HTML in Next.js pages. URL fragments are preserved for stable per-paper identity.

The public figures use `figs/*.svg` as editable sources and committed PNGs for GitHub rendering. A local Chrome or Edge installation is required for deterministic SVG-to-PNG export. Regenerate them on Windows with:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/render_public_figures.ps1
```

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

For a targeted or resumable weekly sweep:

```powershell
python scripts/ai_infra_monitor/monitor.py discover --mode weekly --source-id mlsys26-virtual --source-id icml26-virtual
python scripts/ai_infra_monitor/monitor.py triage --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py queue --run-id <run-id> --tiers A B C
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py validate
```

Weekly automation uses the same flow, with `--mode weekly`, followed by
`report` and `finalize` without `--no-commit` only when a commit is intended.
