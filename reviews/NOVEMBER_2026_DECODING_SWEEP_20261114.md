# November 14, 2026 · Decoding Acceleration source sweep

**Scope:** Reconcile the latest `main` (930 canonical / Decoding 91), not a restart of the entire catalog. **Decision:** eight nonduplicate source-level admissions to one home in `topics/decoding-acceleration.md` (Decoding 99 / overall 938). No model, kernel, NPU, or author benchmark was executed locally; every number below is **author-reported**.

## Mechanism-level G0–G5 triage

| Work / arXiv | Decision | Distinct mechanism & real evidence anchor | Boundary / decisive next check |
|---|---|---|---|
| ForeSpark [2611.13442](https://arxiv.org/abs/2611.13442) · [code](https://github.com/facebookresearch/ForeSpark) | KEEP_PREPRINT_EVIDENCED | Joint pre-Draft + post-Draft Verification budget for block-parallel drafting; author vLLM TP8 H100/B200, DSpark/AR baselines, matched user rate and SLO workload | Needs trained estimator / modified engine; paired Load × K measures before any Ascend transplant |
| DForkTree [2611.12356](https://arxiv.org/abs/2611.12356) · [code](https://github.com/Perseus037/DForkTree) | KEEP_PREPRINT_EVIDENCED | N-gram PMI re-anchors fork-conditioned block marginal trees; matched DFlash/DDTree drafter + verifier Qwen3.5 tests | Only Tree construction is training-free; quantify host/GPU cost and per-branch gain |
| D3Tree [2611.11371](https://arxiv.org/abs/2611.11371) | KEEP_PREPRINT_EVIDENCED | Trained node survival prediction + GPU batch node-budget scheduling; author 6 VLMs/72 load settings | VLM workload and learned head; repeat under text-only Target before generalizing |
| HybridSpec [2611.04055](https://arxiv.org/abs/2611.04055) | KEEP_PREPRINT_EVIDENCED | GDN/MoE Verification Cost model + first-router decision + parallel state reconstruction; measured Hybrid Target greedy baseline | Specific to hybrid recurrent attention, not frozen dense Qwen2.5; concurrency and sampling not established |
| Twig [2608.01651](https://arxiv.org/abs/2608.01651) | KEEP_PREPRINT_EVIDENCED | Tree-factored recurrent state and accepted-path reconstruction; author SGLang integration + offline and online cases; HPCA 2027 author notice | v1 Aug 3, v2 Nov 5 (**not a new November submission**); separate kernel, offline and online denominators |
| REAL Loss [2611.14399](https://arxiv.org/abs/2611.14399) · [code](https://github.com/King-ty/speculators/tree/real-loss) | KEEP_PREPRINT_EXPLORE | Actual EAL path-weight training objective; compared 5 loss variants on Qwen3.6/9 subsets/5 seeds | **Loss-level acceptance only**; no matching model / same runtime E2E serving improvement demonstrated |
| Phrase-Level [2611.12464](https://arxiv.org/abs/2611.12464) | KEEP_PREPRINT_EXPLORE | Separate phrase draft vocabulary expanded to target tokens; trained small MLP head; single A5000/Qwen3-4B/HF benchmark | Greedy identity, not general temperature distribution; HF baseline not optimized online serving |
| Olifant [2611.16714](https://arxiv.org/abs/2611.16714) | KEEP_PREPRINT_EXPLORE | CPU memory-based predictor vs neural draft, with/without KV-cached verifier; throughput + energy experiments | Non-KV 2.43× and cached 1.25× are **different regimes**; must measure true CPU sync and Verifier costs in target engine |

**G0 identity:** all eight have stable original arXiv IDs and accessible abstract/manuscript pages; Twig's original August submission and November revision are distinguished. **G1/G2:** each changes executed Draft/Verify/Speculation or a direct acceptance objective (not a generic application). **G3:** real GPU/consumer studies or controlled model/loss experiments are reported, with the stated limits. **G4:** code links are given only where checked; no independent runtime results. **G5:** each fills a missing implementation or measurement question relative to the 91-paper baseline. Other seven mechanisms were scanned for exact arXiv/title duplication.

## Existing entries; WATCH vs admission

- **Already KEEP:** [Weights That Stay 2611.00506](https://arxiv.org/abs/2611.00506) is already a full Decoding row, with serial-head-only scope, H100/B200 head 11.6× separated from SGLang E2E +12.3%; **do not duplicate**. Existing ChainFlow, Domino, SpecPilot, JetSpec, DFlash and TableTune remain canonical.
- **WATCH_SOURCE:** [EAGLE-4 official repository and standalone manuscript](https://github.com/eagle-hq/EAGLE-4) include `eagle-harness` and dynamic cost-based speculation, but an independent arXiv/publisher identity and fair cross-engine comparator should be reconciled before making a formal canonical preprint row. It is a current **implementation lead**, not a confirmed 2026 conference paper.
- **WATCH_BENCHMARKING:** [Beyond Parallel Blindness 2608.27339](https://arxiv.org/abs/2608.27339) separates missing-conditioning information floor from trainable drafter model gap; valuable prior for DFlash/DSpark, but its primary output is **diagnostic/analysis**, better reconsidered under Benchmarking & Analysis rather than double-listed in Decoding.
- **No new Track taxonomy:** five engineering directions remain sufficient; distinguish Draft/Acceptance, Tree/State, and Joint Scheduling *within* the rows instead of growing subdirectories.

## Relevance to the 910B2 stable pair

The first NPU receipt exercises CPU `ngram` Draft → full Target Verify and demonstrates greedy identity, **not** a proven per-step overhead decomposition or throughput improvement. **Do not infer** that ForeSpark/DSpark/Weights That Stay or any B200/H100 result exists in the pinned vLLM `0fc695fc` + Ascend `5cb98caa`. First isolate a paired Critical-path term on this pair; only then select an optimization mechanism. Reusable theory stays in Profile-Map, raw measurements there and in the BeyondOneToken run; Awesome remains one-row-per-paper bibliography.

**Review source protocol:** arXiv original HTML/abstracts, authors' linked public artifacts where specified; not an independent reproduction or a claim that the November sweep is exhaustive. For updates, replace evidence/venue in the same row rather than adding aliases.
