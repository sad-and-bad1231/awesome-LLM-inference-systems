# Curation policy

## Goal

Maintain an approachable, **selectively edited Awesome bibliography**, not a paper database, monitoring platform, knowledge graph, ranking site or per-paper note repository. `README.md` is the editorial entrance; each topic or organization Markdown page is a directly maintained, human-reviewed list. No machine-generated parallel catalog. Updates should remain small and attributable to primary sources.

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

Started 2026-10-08 from the user-supplied `papers.jsonl` (1,003 entries). First pass is selective identity-and-abstract-level screening, **not a complete reading of all papers or verification of each experimental claim**. The original 19-paper seed contained 18 entries from the upload and the missing FlashAttention paper. This follow-up adds 11 further historical/engineering papers and 6 complementary surveys. The initial 19-paper reset was merged into `main` in PR #7. Earlier data and automation can still be recovered from Git history. Later curation waves are independently checked and committed via reviewable changes; the original import and past scripts remain recoverable from Git history.

## Change discipline

No crawler, JSONL store, generated views, CI publication pipeline, deep research-note hierarchy, badges with hardcoded counts, or mandatory per-paper reading documents. Add complexity only when a concrete presentation need cannot be solved with Markdown.

## Survey-specific gate

Require a distinct systems lens (Serving architecture, hardware/compilers, KV cache, scheduling or distributed inference), credible primary source, meaningful taxonomy/synthesis and an honest coverage boundary. Prefer peer-reviewed surveys; strong lab-authored preprints must be clearly labeled. Reject near-duplicate overviews and survey titles without substantial system content.

## Historical prerequisites

Only a small set of pre-LLM papers belongs here, when its mechanism directly grounds modern inference (Transformer, blockwise verification, MQA). Label background architectures/algorithms separately from evaluated modern serving systems.

## Topic and organization pages

A **topic page** is a deliberately bounded, reproducible bibliography: one problem family, primary publication links, explicit year/venue, and a short *distinct mechanism* for each paper. Do not re-list established anchor entries from the home page to inflate coverage; link back instead. Paper counts are descriptive, never targets that override admission quality. When only an official conference program is available, label that weaker link provenance.

An **organization page** is a *small map of publicly documented work owned or clearly led by that organization*: model architecture with inference consequences, first-party software and technical reports, and public serving interfaces. Label the evidence type; never present an API feature as proof of an undisclosed implementation. **Do not catalog multi-institution collaborations merely because an organization coauthored a paper; place those in the topic bibliography instead.** Ownership of an open-source ecosystem component should be described precisely, without erasing external contributors. Prefer official repositories, publisher pages, and organization documentation. Verify version compatibility; do not exhaustively enumerate checkpoints, marketing releases, benchmarks or company news.

These are reader-facing Markdown pages, not a second structured database. Resist new pipelines and automatic admission.

## Eight mutually focused research classes (2026-10-08)

New primary paper admissions use **one** of: Kernels & Compilers; KV Cache & Context Memory; Decoding Acceleration; Quantization & Compression; MoE & Sparse Execution; Runtime & Scheduling; Distributed & Disaggregated Serving; Benchmarking & Systems Analysis. The classification follows the **decisive reusable mechanism** and its system boundary. Long-context, Agentic, Reasoning, Multimodal, GPU/NPU, model family and organization are workload/hardware contexts, **not top-level paper buckets**.

A publication may have multiple mechanisms, but each paper has only **one canonical full entry**. A short cross-reference to the home page's historical foundations is allowed. The legacy 50-entry Serving cohort was reviewed in the October 2026 migration: 49 assigned a canonical mechanism class, 1 (SkyServe) held out on LLM-specific scope grounds; the prior list is available from Git history. Reclassification does not independently reproduce measured results. The original user-provided JSONL and third-party awesome lists are discovery aids, not proof of admission. Publisher or formal conference pages determine publication status. For new entries, prefer a short technical mechanism rather than unverified benchmark speedup numbers.

## Bibliographic quality control (2026-10-08)

For every new row: verify the **final published title and venue** rather than assuming an arXiv title persisted into formal proceedings; use a publication-specific URL where possible (publisher, USENIX session, PMLR, NeurIPS/ICLR/MLSys conference page). The source note must distinguish arXiv versions, workshops, corporate reports and peer-reviewed papers. Mark papers with unresolved links/identity for later editorial work rather than upgrading their status. Canonical full rows must not duplicate between topic pages, migrated cohorts or the historical Foundation showcase.
