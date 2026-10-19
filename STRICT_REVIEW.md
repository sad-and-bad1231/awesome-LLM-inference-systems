# Strict Review: evidence-first curation

> **Current status (2026-10-18, after merged PRs #45–#48):** the eight-category catalog contains **784 canonical topic entries** (86 Kernels; 172 KV; 83 Decoding; 40 Quantization; 82 MoE; 135 Runtime; 128 Distributed; 58 Benchmarking). The previous broad intake had reached **678**: 486 baseline + 6 stricter + 186 provisional, followed by **15 strict-audit removals** and **6 net new distinct paper identities**; moving BitDecoding from KV to Kernels does not change the total. This is **not** a claim that 669 papers have all passed individual G0–G5 review or independent reproduction. A **first-pass taxonomy and screening sweep on the same date** regrouped all eight pages into **69 industry-grounded sub-groups** and appended an inline screening tag to **176 rows**; the initial sweep removed no rows and corrected exactly one venue cell. The 69 sub-groups were then simplified into **43 industry-facing engineering tracks**, with five sparse-attention papers moved from Decoding to MoE and one Tree-of-Thought scheduling work moved to Runtime; total rows and citations remain unchanged. The sub-group structure is a **reading map, not a G0–G5 verdict** — a `KEEP_*` or `HOLD_*` tag records an explicit, disclosed caveat (evidence not auditable as written, non-output-preserving speedup, adjacent scope) and never substitutes for the gates below. The original 1,003-row historical ledger remains a separate denominator, with 762 directional dispositions and 241 evidence-pending source records as of its last supplied version; it has **not been silently rewritten**.

This document is the **entry point for the second, strict audit**. [Topic index](topics/README.md) remains the sole public canonical bibliography; the external 1,003-row JSONL is a private evidence and identity tracking source, **not a second public catalog**. Do not edit it without receiving the actual latest user file.

## Non-negotiable audit gates

| Gate | Question | What passes | What fails / stays on hold |
|---|---|---|---|
| **G0 Identity** | Is this one real, correctly cited work? | Publisher full-paper DOI/proceedings or traceable author PDF; correct *final* title, year and track; cross-check aliases and existing row | Program listing, DBLP metadata or arXiv **alone** cannot certify a final full paper; mismatched identity → HOLD |
| **G1 Inference scope** | Does it change executed LLM inference or a genuinely foundational dependency? | A specific, inspectable effect on KV, attention, kernels, decoding, P/D, batching, MoE, serving, distributed execution, reliability or production diagnosis | Training-only, generic agent memory, unrelated cloud/security, model-only quality change; adjacent GPU/DiT/VLM needs explicit exceptional rationale |
| **G2 Distinctive mechanism** | What is the technical abstraction and why do strong existing methods fail? | State the bottleneck, decisive implementation, and **closest prior/strong baseline**, with material difference | Same heuristic relabeled, tiny parameter change, no identifiable system novelty → REMOVE |
| **G3 Evidence validity** | Does the experiment actually establish the claimed systems outcome? | Exact model/requests/context/batch/hardware and relevant TTFT, TPOT, P95/P99, throughput/goodput, peak memory, energy or cost; compare quality/exactness; distinguish kernel-only from end-to-end | Simulated accelerator described as fabricated, attention-only speed claimed as serving speed, missing baseline parity, ignored accuracy/SLO → HOLD or REMOVE |
| **G4 Traceability & reproduction** | Can a reader reproduce or at least audit the claim? | Author code/artifact/version where available; workload/model setup, dependency/hardware requirements, negative results and measurement boundaries documented | Inaccessible/irreconcilable benchmark source → HOLD; missing code **alone** does not disqualify a seminal historical systems paper |
| **G5 Editorial value** | Is this worth finite reading time in a selective list? | Seminal systems concept, reusable engineering design, production relevance or unusually strong real-device evidence; not subsumed by closer superior work | Superficial, crowded incremental variant or weak generalizability → REMOVE even with top venue |

### Review decision codes

- **KEEP_STRICT:** G0–G3 and G5 pass; note G4 outcome and any non-reproduction. May remain without public code if historically foundational and well evidenced.
- **KEEP_FOUNDATIONAL / KEEP_ADJACENT:** rare exceptions with **explicit** reason and honest scope labeling, never silently presented as text-LLM serving speedup.
- **HOLD_IDENTITY / HOLD_EVIDENCE:** insufficient full publication, material contradictory claims, simulator/real-hardware uncertainty or unavailable evaluation. Keep out of new public admissions; for already-published rapid entries, **remove or clearly mark provisional while pending**.
- **REMOVE_SCOPE / REMOVE_INCREMENTAL / REMOVE_EVIDENCE / DUPLICATE_ALIAS:** delete the canonical row (or retain only the correct original), preserve the reason and primary source in review receipts.

## Mandatory evidence receipt for each examined paper

Record at least: `source_index` (if historical) or canonical URL; current category/title/DOI/venue/year/**track**; publisher PDF and author artifact URLs; exact problem and claimed novelty; closest **three** related systems or strong baselines; models, tokens, workloads, hardware, toolchain, real-vs-simulated label; metrics including quality/semantic regressions; measured-vs-modeled claims; audit verdict and one concrete reason; evaluator/date and reproduction state (`not_attempted`, `artifact_inspected`, `run_failed`, `replicated`, `not_possible`). A result copied from the paper **must** be attributed as author-reported.

Do not create a machine-generated JSONL/CSV source of truth in this repository. Use small GitHub PR diffs for accepted/deleted Markdown rows, plus audit notes in the PR discussion; keep any full record-level working ledger outside the published repo.

## Order of work

1. **R0 — identity and scope cleanup (fast, 20–30 entries/PR).** Revisit all rapid entries supported by conference program/DBLP-only identity, incorrect year/title, generic ML tooling, image/video/VLM adjacency and obvious aliases. Prioritize hard rejections; do not ask for hardware before resolving G0.
2. **R1 — primary-paper and method audit (10–20 entries/PR).** Target first: high-density **KV (144)**, **Runtime (119)**, **Distributed (121)**, **Decoding (71)**, and **MoE (59)**, plus kernel/tooling exceptions. Check baseline equality and any changes to model weights, outputs, prompts or arrival process.
3. **R2 — reproducibility probes (only highest-value survivors).** Prefer existing vLLM/SGLang/Ascend paths when technically applicable; verify artifact commit/model/hardware/driver, run correctness first, then performance. A paper's CUDA artifact is not presumed Ascend-compatible.
4. **R3 — editorial pruning and freeze.** For each batch: PR with precise additions/deletions, summary of KEEP/HOLD/REMOVE/aliases, synchronized eight topic headings/index/homepage count, no duplicate normalized titles or publication URLs; reviewer approval then merge.

### Strong baseline checklist

Fair versions, identical model/tokenizer/checkpoint, context distribution, output lengths, batch/concurrency, precision, quality requirements, budget and hardware. When needed: modern vLLM/SGLang, FlashAttention/FlashInfer, static/continuous batching, prefix-cache policies, optimized speculative drafter or standard MoE expert placement. Report *both* throughput and SLO-correct goodput; TTFT/TPOT (including tail), memory/energy and approximation error when relevant. Never infer one metric from another.

### Hardware and model-change labels

**REAL_GPU/NPU/CPU/FPGA** (specific board), **RTL_EMU**, **PERF_SIM**, **TRACE_SIM**, **ANALYTIC_MODEL**, **AUTHOR_ONLY_CLAIM**; apply more than one label if needed, and attribute exactly what was physically tested. Likewise: **LOSSLESS_OUTPUT**, **APPROXIMATE_QUALITY_CHECKED**, **REQUIRES_FINETUNING**, **MODEL_CHANGED**. This prevents simulator, distillation or expert re-routing effects being advertised as drop-in speedups.

## Known provenance/identity hazards to resolve early

- **#933 NovaServe vs Select-N:** apparently overlapping ICS 2026 title/DOI but conflicting offload mechanism and author speedup figures; inspect final camera-ready before any admission.
- **#215 RAGBoost and #288 DefensiveKV:** prior source records lack sufficiently reconciled archival/evaluation evidence; external ledger still marks both unresolved.
- **Program-index-only rapid admits:** **42** original historical ledger records specifically have `admitted_fast_provisional_program_index`; these should be the first G0 full-publication re-verification queue, not labeled fully verified.
- **Euro-Par 2026 papers:** meeting year 2026 and some Springer book metadata imprint 2027; disclose both, do not overwrite one with the other.
- **Generic GPU OS, toolchain, and adjacent video/image generation:** assess the rare 'foundational/adjacent' exception paper-by-paper; drop weak connections to text LLM inference.

## Completion criterion

Strict screening is complete **only when every current canonical entry has a documented G0–G5 verdict**, rejected or merged duplicates are removed, the full 241-record evidence-hold list has a fresh source-specific disposition or explicit continuing hold, all counts are recomputed from Markdown, and no unchecked paper is presented as fully verified. A first-pass 100% screening rate does **not** mean strict acceptance is finished.

Related: [Curation policy](CURATION.md), [Topic index](topics/README.md), and the repository's October 2026 PR review history. New chats need the **actual** latest 1,003-row ledger attached; GitHub Markdown alone cannot reconstruct all historical source_index decisions.
