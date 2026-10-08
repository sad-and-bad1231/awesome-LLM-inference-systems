# Curation policy

## Goal

Maintain an approachable **Awesome** list, not a paper database, monitoring platform, knowledge graph, ranking site, or per-paper note repository. `README.md` is the only public catalog and single source of truth. Updates are manual and small.

## Admission gate

A paper or survey is accepted when all baseline requirements are satisfied:

1. **Systems relevance:** targets a concrete LLM inference/serving bottleneck (runtime scheduling, memory/KV, P/D transfer, kernel/compiler, distributed systems, parallelism, speculation, production operations), or is a genuinely foundational prerequisite.
2. **Substantive contribution:** proposes an identifiable and reusable system mechanism or architecture, not merely a renamed heuristic, new prompt/task, or marginal parameter tuning.
3. **Evidence:** credible real hardware, end-to-end workloads, published evaluation or production deployment; baseline and trade-offs should be intelligible. Older landmark papers can be admitted for historic influence after their concrete contribution is verified.
4. **Reliable identity:** title, year, venue, and official primary source checked; unverified entries must not appear in the published list.
5. **Research credibility:** author expertise, institutions, open-source adoption, and selective systems venues are positive supporting signals. **Institutional prestige alone is neither sufficient nor necessary.**

## Default exclusion

- Training-only or model-quality-only studies with no inference execution/system contribution.
- Pure simulation/proof/algorithm papers lacking convincing systems evidence, except historically foundational techniques.
- Derivative variants without an important new abstraction, measurable systems advantage, or materially different deployment context.
- General vector DB, security, generic cloud, and hardware papers not tightly connected to LLM inference.
- Duplicates, unpublished claims with unclear provenance, and venue/affiliation metadata that cannot be verified.

## Review workflow

1. Search the candidate in the original JSONL, but do not trust `verified_legacy` or `core` as final admission evidence.
2. Verify using conference proceedings, publisher, official paper PDF, or author's artifact/project page.
3. Judge **problem → mechanism → end-to-end value / limitations**. Favor precision over coverage.
4. Add one Markdown table row under the correct year with primary link, venue, concise institutions, and mechanism.
5. When uncertain, omit from public list and revisit in a later batch. Use GitHub issues/PRs for discussions; do not create a second shadow database.

## Rebuild provenance

Started 2026-10-08 from the user-supplied `papers.jsonl` (1,003 entries). First pass is selective identity-and-abstract-level screening, **not a complete reading of all papers or verification of each experimental claim**. The seed includes 18 matching uploaded records and one independently verified missing historical prerequisite (FlashAttention, NeurIPS 2022). The old `main` branch and Git history preserve the original data/automation until a deliberate merge; this draft branch intentionally contains only these two Markdown files.

## Change discipline

No crawler, JSONL store, generated views, CI publication pipeline, deep research-note hierarchy, badges with hardcoded counts, or mandatory per-paper reading documents. Add complexity only when a concrete presentation need cannot be solved with Markdown.

## Survey-specific gate

Require a distinct systems lens (Serving architecture, hardware/compilers, KV cache, scheduling or distributed inference), credible primary source, meaningful taxonomy/synthesis and an honest coverage boundary. Prefer peer-reviewed surveys; strong lab-authored preprints must be clearly labeled. Reject near-duplicate overviews and survey titles without substantial system content.

## Historical prerequisites

Only a small set of pre-LLM papers belongs here, when its mechanism directly grounds modern inference (Transformer, blockwise verification, MQA). Label background architectures/algorithms separately from evaluated modern serving systems.
