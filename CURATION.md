# Curation policy

**Current policy (last reconciled 2026-11-10).** This file contains enduring selection and attribution rules; see [STRICT_REVIEW.md](STRICT_REVIEW.md) for operational G0–G5 gates, [topics/README.md](topics/README.md) for live counts and [archived historical intake waves](reviews/archive/CURATION_HISTORY_20261030.md) for dated acceptance/rejection accounting. Counts in archives describe past checkpoints only.

## Canonical bibliography invariant

The eight topic tables are the **one canonical bibliography**. Admissions may use **KEEP_PREPRINT_EXPLORE**, **KEEP_PREPRINT_EVIDENCED**, **KEEP_STRICT / KEEP_REFERENCE**, **KEEP_FOUNDATIONAL**, or a narrowly justified **KEEP_ADJACENT**. All accepted papers must have a reliable primary-paper identity, a distinct *inference execution/system* idea, and an honest evidence/proof boundary. **Acceptance means editorial reading/research value, not independently reproduced performance.**

A credible arXiv preprint **does not need** top-conference acceptance, end-to-end Serving Goodput, public code, an Ascend port, or local reproduction to enter the bibliography. However, a paper with merely a grand architecture diagram, ungrounded headline speedup, generic agent prompt, or no falsifiable mechanism stays **HOLD_STORY_ONLY** (or Frontier WATCH) until a meaningful technical check is available. Keep genuinely unresolved paper identities / aliases in **HOLD_IDENTITY**; a **non-material date/venue discrepancy** can be annotated rather than automatically disqualifying a stable arXiv ID + title + author + full text. Never invent the date.

## Two-speed publication review: arXiv discovery vs. conference references

| Review dimension | **arXiv discovery / frontier-first** | **Top-conference reference / mature systems work** |
|---|---|---|
| Editorial role | Fast intake of novel problems, specific executable mechanisms, early exploration, negative results and brand-new directions (e.g. **RSI on Inference Engines**, Agent-native Serving, Kernel Agents) | Study exemplary system research: mechanism attribution, baseline selection, complete evaluations, reproducibility and topic convergence |
| Novelty | Distinct, falsifiable execution/optimization contract or surprising technical counterexample; cannot be generic application-agent packaging | A well-developed, reusable systems abstraction with clear prior-art distinctions |
| **Minimum evidence** | **One inspectable technical anchor:** controlled pilot/microbenchmark, evaluated prototype, trace study, transparent simulator/analytical model with assumptions, or rigorous formal argument. Explain what it **does not** demonstrate; modest or negative evidence is valid | Prefer full-paper methods, matched strong baselines, ablations, workload variation, measured hardware and metrics appropriate to the claim. Venue name alone does not prove this |
| Artifact | Optional; add author repo/commit if available. Mechanism, assumptions and evaluation/proof must still be inspectable | Favor pinned artifact, environment and experiments, but lack of public code alone does not exclude an important historical paper |
| Performance claim | Label **PILOT / MICROBENCH / TRACE / SIM / FORMAL / REAL_GPU/NPU / E2E**, author-reported vs independently replicated; no simulated speedup advertised as real deployment | Same labels, with more complete comparison and scope scrutiny; no blanket presumption of correctness from acceptance |
| Evidence status | **KEEP_PREPRINT_EXPLORE** (mechanism + limited but inspectable support) or **KEEP_PREPRINT_EVIDENCED** (substantial primary-source experiment) | **KEEP_REFERENCE** or existing **KEEP_STRICT / KEEP_FOUNDATIONAL** |
| Disposition when only a story exists | **HOLD_STORY_ONLY / WATCH_FRONTIER**, with a concrete next experiment that would change the verdict | HOLD/REMOVE unless historically foundational and independently established |

**Both tracks share a hard floor:** valid paper identity; material LLM-inference-system relevance; identifiable bottleneck → mechanism → expected observable; explicitly attributed claims; model/precision/quality changes and simulator-vs-hardware separation; a reason why the reader should care. The **strength of the evidence**, not the prestige or recency of the venue, decides which tag applies. Frontier research papers can graduate from EXPLORE → EVIDENCED → REFERENCE as experiments and publication mature, **without creating duplicate rows**. Do not impose a target admission percentage or wait for 2027 conference lists to decide what to read.


## Intake cadence and upgrade path

- **arXiv:** browse recent papers often (daily/weekly when actively researching) across inference-related cs.DC/cs.OS/cs.PF/cs.AR and adjacent model/agent fields. Broaden discovery around brand-new topics rather than enforcing a low fixed acceptance quota. Admit **EXPLORE** quickly when the minimum technical anchor is real; record the *one experiment that would be most informative next*. Periodically re-check updated preprint versions.
- **Conferences:** scan authoritative proceedings/accepted lists when published; use a slower deep-reading cycle for **REFERENCE** examples of research problem formulation, strong experimental design, and convergence. **Do not invent future 2027 acceptances or delay arXiv admission until decisions.**
- **Progression:** source discovery → mechanism check → evidence-grade label → optional artifact/reproduction → later venue/final-version update. Upgrade the existing one-home row; keep provisional claims clearly marked. Negative/pilot studies remain valuable when falsifiable; speculative marketing without an inspectable anchor stays WATCH/HOLD.

## Goal

Maintain an approachable, **selectively edited Awesome bibliography**, not a paper database, monitoring platform, knowledge graph, ranking site or per-paper note repository. `README.md` is the editorial entrance; each topic or organization Markdown page is a directly maintained, human-reviewed list. No machine-generated parallel catalog. Updates should remain small and attributable to primary sources.

## Admission gate

A paper or survey is accepted when all baseline requirements are satisfied:

1. **Systems relevance:** targets a concrete LLM inference/serving bottleneck (runtime scheduling, memory/KV, P/D transfer, kernel/compiler, distributed systems, parallelism, speculation, production operations), or is a genuinely foundational prerequisite.
2. **Substantive contribution:** proposes an identifiable and reusable system mechanism or architecture, not merely a renamed heuristic, new prompt/task, or marginal parameter tuning.
3. **Evidence:** use the appropriate **preprint exploration vs. mature systems reference** threshold above: an inspectable, falsifiable pilot/model/proof suffices for exploratory preprints; strong measured baselines and full-system methods are preferred for conference exemplars. Never promote a hypothetical design into a measured runtime speedup.
4. **Reliable identity:** stable paper ID, title, authors, version/year and accessible full text; **arXiv is its own valid preprint identity** and needs no invented conference venue. Distinguish unverified metadata fields from genuine paper-identity conflicts.
5. **Research credibility:** author expertise, institutions, open-source adoption, and selective systems venues are positive supporting signals. **Institutional prestige alone is neither sufficient nor necessary.**

## Default exclusion

- Training-only or model-quality-only studies with no inference execution/system contribution.
- Unsupported simulation/proof/algorithm claims **without an inspectable execution mechanism, assumptions or systems implications**. Transparent models/formal analysis with testable inference consequences can enter as clearly labeled **PREPRINT_EXPLORE**, not as measured deployed acceleration.
- Derivative variants without an important new abstraction, measurable systems advantage, or materially different deployment context.
- General vector DB, security, generic cloud, and hardware papers not tightly connected to LLM inference.
- Duplicates, unpublished claims with unclear provenance, and venue/affiliation metadata that cannot be verified.

## Review workflow

1. Check current canonical paper titles, arXiv IDs, DOI/publisher URL aliases across all eight topic pages. If the original external JSONL is available, use it only as a discovery aid; never treat its `verified_legacy` or `core` tag as final admission evidence.
2. Verify using conference proceedings, publisher, official paper PDF, or author's artifact/project page.
3. Judge **problem → mechanism → evidence strength → next test / limitations**. A preprint need not already demonstrate end-to-end Serving; never suggest it does when evidence is narrower.
4. Add one Markdown table row under the correct sub-group with verified year/venue, primary source link and a **distinct mechanism plus a truthful evidence boundary** (models, hardware, metric, quality/model changes, artifact availability as applicable).
5. When uncertain, omit from public list and revisit in a later batch. Use GitHub issues/PRs for discussions; do not create a second shadow database.

## Rebuild provenance

Started 2026-10-08 from the user-supplied `papers.jsonl` (1,003 entries). First pass is selective identity-and-abstract-level screening, **not a complete reading of all papers or verification of each experimental claim**. The original 19-paper seed contained 18 entries from the upload and the missing FlashAttention paper. This follow-up adds 11 further historical/engineering papers and 6 complementary surveys. The initial 19-paper reset was merged into `main` in PR #7. Earlier data and automation can still be recovered from Git history. Later curation waves are independently checked and committed via reviewable changes; the original import and past scripts remain recoverable from Git history.

## Change discipline

No crawler, JSONL store, generated views, CI publication pipeline, deep research-note hierarchy, badges with hardcoded counts, or mandatory per-paper reading documents. Add complexity only when a concrete presentation need cannot be solved with Markdown.

## Adjacent-work and evidence-scope decisions

`KEEP_ADJACENT` is **not** an unconditional green label. Cross-domain papers (DiT/video, ASR, VLA, RL rollout, GPU OS, simulation) must have an identifiable execution mechanism and an explicit reason a modern LLM inference-systems reader would need the work. An adjacent paper can be valuable without belonging in the 8-topic canonical list. Strong academic venue or new model speed alone is insufficient for canonical LLM Serving admission.

If removing a row for editorial scope, preserve the primary proceedings source and precise reason in `reviews/`; do not delete the historical reading signal. If retaining a paper with changed models/semantics, record the non-equivalence and task/hardware boundaries. See the [2026-11-05 complete adjacent-scope triage](reviews/ADJACENT_FULL_SCOPE_REVIEW_20261105.md); this 75-row pass includes explicit `INDEXED_SOURCE` caveats and **does not** claim independent reproduction.

## Offline repository integrity check

Before submitting any Markdown curation PR, run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/check_catalog.py
```

The lightweight GitHub Actions check runs the **same commands** on relevant PRs. This is **not a publication pipeline**, crawler, generated bibliography, or automatic scientific reviewer. The script compares declared topic/subgroup totals, first-paper URL identities (including arXiv/DOI/OpenReview forms), foundation and organization/OSS index counts, and internal Markdown targets/anchors. Counts live in the visible Markdown indexes; no independent machine-managed catalog is introduced.

**Limitations:** identity aliases that mix DOI/arXiv/publisher pages can evade exact URL matching; Markdown link extraction is a practical linter rather than a full CommonMark parser; live external URL availability, publication claims, model correctness and reported speedups require manual primary-source review. Never use a passing structural check as evidence that G0–G5 scientific gates passed. When a legitimate source changes the catalog count, update the visible index and the paper row together; do not weaken the checker just to pass CI.

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

## Emerging frontiers: selective adjacent-inference exception (2026-10-12)

The eight canonical classes remain classified by **decisive systems mechanism**. The [frontier reading map](frontiers/README.md) is a cross-index, never a second paper database or quota. Start with one foundation/measurement anchor per field and admit only exceptional follow-ons; venue rank, novelty language and large-scale paper discovery alone do not qualify.

For the emerging World Model / Interactive Video / VLA boundary, admit an **explicitly labeled adjacent foundation-model inference** work only when it exposes a reusable inference-time bottleneck or mechanism (e.g. long-lived state, temporal cache, streaming execution, heterogeneous VLM/action pipelines) **and** reports credible measured real-device execution or end-to-end inference. Training-only improvements, video-quality-only innovations, generic robotics datasets, and unmeasured speedup projections remain excluded. The foundational KernelBench general-ML evaluation paper is a **narrow landmark exception**, not permission to add generic DNN benchmarks or GPU optimization papers without clear relevance to future inference-kernel engineering.

For agent-generated kernels, require real compiled/executed kernels and distinguish benchmark speedups from actual inference serving speedups; consider hidden-distribution correctness, baseline flags and resource overhead. Preprints remain preprints. Treat all performance gains as *author reported*, not reproduced. Each paper retains one canonical mechanism home.

## Bibliographic quality control (2026-10-08)

For every new row: verify the **final published title and venue** rather than assuming an arXiv title persisted into formal proceedings; use a publication-specific URL where possible (publisher, USENIX session, PMLR, NeurIPS/ICLR/MLSys conference page). The source note must distinguish arXiv versions, workshops, corporate reports and peer-reviewed papers. Mark papers with unresolved links/identity for later editorial work rather than upgrading their status. Canonical full rows must not duplicate between topic pages, migrated cohorts or the historical Foundation showcase.

## Expansion and limits (October 2026)

Large corpus discovery is not bulk admission. A historical source's `core`, `verified_legacy`, or `official_source` label is only a retrieval signal. Each public topic row needs a named technical mechanism and a publisher/conference source with evidence of implementation or technically meaningful measurement. Screening of publication abstracts is weaker than reading the evaluation section or reproducing the results, and should never be described as equivalent. Generic DNN, training-only and venue-title-only candidates remain outside the main eight topics. No quota overrides these rules.

## 2026 conference expansion discipline

For the 2026 large-volume request, **2026 must describe the accepted formal conference publication**, not merely a paper's preprint date. Verify a paper-specific proceedings page, DOI or publisher-endorsed conference schedule, not a scraped bibliography entry. Require concrete LLM inference relevance and distinctive evaluated system mechanisms. Record numerical shortfalls honestly rather than importing training papers, generic GPU benchmark papers or incomplete program-title-only entries to satisfy a fixed quota. The 2026 conference-only tranche adds 53 entries. The target of 300 *additional* entries remains unmet and should not be confused with the cumulative library count.


