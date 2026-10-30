# 2026-10-30 taxonomy, lab and bibliographic hygiene audit

**Scope:** all eight canonical topic pages, current homepage/index/curation/strict gates, frontier navigation, research labs, organization landing page and four historical snapshots. **No new paper admission, reclassification, deletion, new frontier or new engineering direction.** This is a repository-wide **mechanical/structural audit plus four primary-publisher-evidence corrections**, **not** a full-text G3/G4 audit of all 813 papers, not a link-uptime crawl, not a benchmark reproduction.

## Live catalog inventory: zero structural count faults

| Engineering mechanism | Canonical paper rows | Engineering directions | Editorial risk needing deeper review |
|---|---:|---:|---|
| Kernels & Compilers | 114 | 6 | Kernel microseconds vs complete inference runtime; CUDA/Ascend portability; Agent-generated hidden-case correctness |
| KV Cache & Context Memory | 159 | 6 | Quality-changing eviction/reuse vs exact KV equivalence; prefill/transfer and device-memory budgets |
| Decoding Acceleration | 79 | 5 | Exact target distribution verification vs changed draft / trained recurrent models |
| Quantization & Compression | 43 | 6 | Accuracy/model change, dequantization overhead, quality-memory-latency tradeoffs |
| MoE & Sparse Execution | 70 | 4 | Expert communication topology, model-specific sparse wins, training/reweighting boundaries |
| Runtime & Scheduling | 142 | 6 | Trace vs live production, P95/P99 Goodput, request-distribution shifts and preemption overhead |
| Distributed & Disaggregated Serving | 132 | 5 | Real multi-node network vs modeled transport; load/source/switch assumptions |
| Benchmarking & Systems Analysis | 74 | 6 | Kernel-only vs end-to-end metrics, simulator calibration, baseline parity and device comparability |
| **Total** | **813** | **44** | |

Recomputed directly from the eight **year-leading Markdown paper table rows**, not the historic change ledger: **813 primary URLs, 813 normalized titles and 813 rows are unique**. Each file's `## Papers (N)` matches its physical row count, and each of the 44 `### ... (N)` subgroup headers matches row counts. Original main contained no obvious canonical `HOLD_...` admissions requiring mass removal. All 30 *distinct local Markdown targets* referenced by the rebuilt active/archived landing pages were checked to exist on this audit branch. Relative links were rebased inside archives. **This is not an external HTTP link-status check.**

## Documentation cleanup: move old status, preserve provenance

Before this review the navigation was dominated by contradictory-seeming, but actually **dated**, inventory progress: 669→796→745→722→736→766→793→803→813 in several high-visibility files. This is appropriate for a dated review receipt, **not** a live directory or a fixed admissions rule.

| File | Before / after (character count) | Treatment |
|---|---|---|
| `topics/README.md` | 42,203 → about 3,057 | Only 8-topic table, counts, use instructions, G0–G5 and provenance links remain; old admissions and screens moved to dated archive |
| `CURATION.md` | 76,536 → about 12,551 | Enduring policies retained; historical batch ledger moved, no new machine-generated source of truth |
| `README.md` | 20,396 → about 17,254 | One current snapshot, homepage foundations/surveys unchanged, recent/historical links moved out of introduction |
| `STRICT_REVIEW.md` | 24,168 → about 8,810 | Active G0–G5 gates remain; dated review snapshots archived |
| `communities/README.md` | 10,964 → about 5,714 | One research-group crosswalk, rather than duplicate Oct 25 and Oct 30 tables; upstream open-source systems preserved |

Historical text is preserved in `reviews/archive/{TOPIC_INDEX_HISTORY,CURATION_HISTORY,STATUS_SNAPSHOTS,LAB_SIGNALS}_20261030.md`, including date-specific discrepancies, limitations and original claims, with local link roots normalized. **Archive entries are not live inventories.**

## Four verifiable paper-row corrections — no new admissions

1. **BeaconKV** — official [ICML 2026 PMLR source](https://proceedings.mlr.press/v306/kim26af.html) confirms Beacon Query clustering / Thought Revisiting Tokens, four LRM evaluation and separately scoped up-to memory/throughput outcomes. Canonical description now states approximate KV behavior and author-reported extrema.
2. **Uncertainty-Aware Output Length Scheduling** — [ICML 2026 PMLR](https://proceedings.mlr.press/v306/zheng26ae.html) confirms log-t modeled output length and Tail Inflated Expectation (TIE), online per-token latency and distinct offline throughput comparison. No conflation of two metrics.
3. **THETA: Threshold-Based Exclusive Batching** — [ICML 2026 PMLR](https://proceedings.mlr.press/v306/zhang26eo.html) documents bandwidth- and mix-dependent MB/EB crossover (H200 vs RTX PRO 6000) and conditions where mixed batching still wins, not unconditional switching superiority.
4. **Breaking the Ice (vLLM startup)** — [MLSys 2026 official paper](https://proceedings.mlsys.org/paper_files/paper/2026/hash/29416b66c2149872b9d1415a3fd2c5e0-Abstract-Conference.html) and [author profiler artifacts](https://github.com/upb-cn/vllm-startup-profiler) establish six-phase, largely CPU-bound cold-start analysis **in measured environments**, not proved end-to-end service speedup in current vLLM.

**Limit of the row-level review:** other short rows (e.g., IndexMem, PatternKV, LouisKV, GyRot, Bullet, OptiKIT, MFS, Charon, and some MoE routing papers) still need individual paper-level G3/G4 annotation. A mechanically duplicate-free row with a primary link is **not** necessarily strong enough to claim its metric is reproducible or representative. No unsupported metric was added to these rows.

## Lab/source rigor

- Research groups and open-source runtimes stay separate; **one canonical topic row** per publication, never duplicated under lab name.
- **TOPIC** = indexed paper; **PREPRINT/ADJACENT** = venue or scope caveat; **BLOG/ENGINEERING** = first-party implementation/post, **not** an archival paper; **REVIEW/HOLD** = discovery source not admitted.
- [SyFI VibeSys](https://syfi.cs.washington.edu/blog/2026-10-08-qwen35-mi300a/) and [ServingStudio](https://syfi.cs.washington.edu/blog/2026-09-24-introducing-servingstudio/) are explicitly labeled first-party engineering blogs. [Berkeley Sky publication index](https://sky.cs.berkeley.edu/publications/) confirms CommBench/FreeToken entries; [CMU FlashRT paper](https://arxiv.org/abs/2607.18171), [MIT Quant VideoGen PMLR](https://proceedings.mlr.press/v306/xi26f.html), [Stanford NCM](https://arxiv.org/abs/2610.14162) are cross-links, not second bibliographic records.
- The group list is intentionally selective, **not** proof of exclusive institutional ownership in cross-lab work or completeness of a lab's 2026 papers.

## Verdict and remaining debt

**Structural hygiene: good after archival split. Bibliographic identity/duplication: clean at normalized-title/primary-link level. Rigor: source-based and uneven, NOT a full 813-paper scientific or experimental audit.**

Next highest-value work (separate PRs): **(1)** review 10+ terse canonical rows against method/evaluation sections, **(2)** sample G3 parity by category, especially simulation/model change and kernel-vs-end-to-end, **(3)** check external links and formal-venue aliases, **(4)** run independent reproduction only on strategically relevant and feasible kernels/runtime work. Never “greenwash” canonical entries merely by removing HOLD words or inventing evidence. A correct archive helps reader navigation but does not upgrade scientific evidence.
