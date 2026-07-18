# Contributing

This repository tracks evidence-aware papers and industrial systems for LLM inference serving.

## Scope

Prioritize:

- Runtime and serving systems
- Prefill/decode disaggregation and KV transfer
- KV state, memory hierarchy, and cache management
- Kernels, compilers, and hardware backends
- Scheduling, agent serving, and multi-tenant systems
- Serving benchmarks, reliability, and production operations

Training-only methods, generic vector databases, security-only systems, and hardware-only work should be submitted only when they contain direct inference-serving evidence.

## Adding an Entry

Add one JSONL record to the matching fact source:

- `data/papers.jsonl` for academic papers
- `data/industry.jsonl` for companies, open-source projects, and engineering material
- `data/candidates.jsonl` only for unverified discovery items

Every record must pass the local schema validator and include a primary URL, evidence metadata, canonical identity, technical tags, and a concise factual summary. Do not edit generated `README.md`, `papers/README.md`, `industry/README.md`, or `archive/README.md` directly.

The deterministic curation layer adds `curation.scope` and `curation.priority` from `guide.md`. Core records are the public reading path; adjacent and archive records remain available in `archive/README.md` for audit. Run `curate` after changing the guide or curation rules, then render the views.

For a small number of high-value public entry points, an optional `presentation` object may contain `featured`, a non-negative `order`, and a short `blurb`. These fields control display only and must not replace evidence or factual metadata.

Public diagrams live under `figs/`. Keep the PNG files and their SVG source files in sync; the validator checks both required PNG assets and generated Markdown links.

## Public Presentation

The public layer follows a paper-figure visual language: a white canvas, restrained accent colors, explicit system stages, and short labels that remain readable when GitHub scales the image. Edit the SVG source first, then regenerate the cover PNG with:

The renderer uses a local Chrome or Edge headless runtime so SVG and PNG stay pixel-consistent:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/render_public_figures.ps1
```

Keep the README focused on navigation and evidence. Do not add a new visual panel merely to increase coverage; extend the taxonomy or collection pages when the information is more useful as text.

## Local Checks

```powershell
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py curate
python -m unittest discover -s tests -p "test_*.py"
```

Pull requests should explain the source, evidence level, canonical identity, and why the item belongs to the serving mainline.
