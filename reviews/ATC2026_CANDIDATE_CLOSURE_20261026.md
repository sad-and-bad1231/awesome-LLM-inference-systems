# ATC 2026 inference-candidate closure — 2026-10-26

## Scope and meaning of closure

This **closes the 2026-10-26 editorial pass** over the remaining ATC 2026 LLM/kernel/AI-infrastructure candidates, **not** their scientific merits and **not** an independent full-text replication. As of October 26, [ATC 2026](https://atc.sigops.org/2026/accepted.html) takes place **November 15–18, 2026**. Program acceptance (G0) is not an archival full-paper/Artifact audit (G2/G3/G4). The source links below are not placeholders in public canonical topic tables.

Policy: **one paper identity, one canonical topic row**; lack of enough G3 evaluation evidence, artifact or baseline clarity means the candidate must stay **outside** `topics/*.md`, with a decisive trigger for re-screening rather than a perpetual “quick admission.” A candidate can later become KEEP when new full-paper evidence appears; that is not a pending user task or implied background monitoring.

### Critical identity/quality corrections

1. **HACK remains HACK.** [ATC conference schedule](https://atc.sigops.org/2026/schedule.html) lists the accepted work under its exact published/early-[arXiv](https://arxiv.org/abs/2502.03589) name **“HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference”**, not “HKVQ.” The previous audit asserted an unverified HACK→HKVQ conference rename; **RETRACTED**. Existing single KV row corrected; no new count.
2. **TokenGate authors' code** is [token-gate-llms/TokenGate](https://github.com/token-gate-llms/TokenGate), **not** `tokengate-models/TokenGate`. Corrected both canonical row and first admission audit.
3. **R3 retraction of premature admissions (−3):** the earlier ATC tranche added **BMV**, **IgniteServe**, **HybridFaaS** from the conference program plus HUST lab/author summaries without an auditable final paper/experiment matrix or equivalent versioned artifact. We retract them from the canonical list and keep the historical decision below. This is an evidence-bound editorial correction, **not a claim that the research is invalid**.
4. No local GPU/NPU runs, no vLLM 0.23/Ascend code parity. Retain all older dated inventory figures **as dated snapshots**, with latest headline **766** (736 main + 33 initially added − 3 retracted). Do not quietly rewrite the historical ten-paper tranche as if it were always seven.

## Priority HOLD — real ATC identity, G3/G4 insufficient

These are **screened and OUTSIDE canonical**. The gate to reopen is precise; published venue alone cannot satisfy it.

| Work / primary identity | Mechanism with inference relevance | Current result | Decisive next evidence required |
|---|---|---|---|
| [DittoCache](https://atc.sigops.org/2026/accepted.html) (Jia He et al., USTC/Huawei) | GPU-centric KV Cache ownership/coordination; may remove host-side scheduling stalls | **HOLD_EVIDENCE** — no verifiable full method or physical integrated decode baseline located | Full PDF or source: exact CPU↔GPU operation/graph implementation, device/version, per-token control overhead, throughput + TPOT/Tail and cache correctness |
| [TensorBridge](https://soldierchen.github.io/publications/) (HKUST GZ) | Decode FP4 storage with FP8 Tensor Core execution | **HOLD_EVIDENCE** — author/venue identity confirmed, but quantified real-GPU improvement, dequant overhead, quality baseline not verified | Full kernel math, target GPU tensor-core path, error/PPL and serving goodput vs native FP8 or NVFP4 |
| [SptcAttn](https://kevinwu2017.github.io/) (SJTU/Enflame) | Map selected diagonal-stripe sparse Attention to 2:4 Sparse Tensor Cores; no loss of *selected* scores | **HOLD_EVIDENCE** — author mechanism confirmed, not enough inspectable kernels/measurements | Full hardware kernel and attention-only vs end-to-end numbers, mask selection cost, precision, NIAH/long-context model accuracy |
| [ATP](https://franchyi.github.io/) (USTC/NUS) | Workload-adaptive TP resource sizing under P/D disaggregation, optimize SLO-correct Goodput | **HOLD_EVIDENCE** — identity, stated objective verified; no dependable full experimental detail | Full paper with reconfiguration/resharding cost, arrival rates, TTFT/TPOT P95, static TP/PD and dynamic Strong Baselines |
| [JetFire](https://yaochen.site/) (NUS/HUST/ETH) | Approximate-then-correct Attention over CPU/GPU hybrid memory for long contexts | **HOLD_EVIDENCE** — venue/title/authors verified, mechanism unverified beyond title | Correctness proof and correction fallback rate, CPU→GPU I/O accounting, quality and real long-context TTFT/TPOT vs FlashAttention/offloading |
| [CacheSched](https://atc.sigops.org/2026/accepted.html) (PKU/UCLA/ZTE) | Cache-aware request scheduling | **HOLD_G2/G3** — conference title only; unclear material novelty over vLLM/SGLang cache affinity and existing cache routers | Full paper + strongest prefix-cache-aware schedulers, matched cache capacity/arrival trace and tail goodput, preferably executable patch |
| [Octopus](https://atc.sigops.org/2026/accepted.html) (Tsinghua) | SSD parallelism for sparse KV retrieval | **HOLD_EVIDENCE** — no inspectable SSD-vs-simulation split | Real SSD IOPS/queue-depth, token-level gather, retrieval precision, P95 E2E and hardware topology |
| [MoE-Lego](https://atc.sigops.org/2026/accepted.html) (SJTU/HKUST) | Plane-grained dynamic-precision expert-weight offloading | **HOLD_EVIDENCE** — model precision/quality and transfer scheduling unverified | Full paper and FP16/FP8 low-bit quality, expert residency, device-backed HBM/PCIe traces, strong MoE engine comparisons |
| [CacheFS](https://atc.sigops.org/2026/accepted.html) (Alibaba/ZJU) | P2P LLM model weight distribution and caching across fleet | **HOLD_G3/G4** — identity and scale claim unverified in accessible full paper | Production/download trace, cold-start/TTR and deployment/availability results, compare topology-aware peer distribution and model file cache |
| [Axon](https://cds-macau.github.io/publication/conference-paper/axon/) (Macau/Alibaba) | Asynchronous distributed KV-aware agent workflow routing | **HOLD_G2/G3** — author site says abstract TBD | Full algorithm, KV consistency and crossing, online agent session-level trace vs LLm-d/vLLM cache routers with SLO |
| [TwinCache](https://atc.sigops.org/2026/accepted.html) (BUPT) | Retrieval/reranking-aware RAG caching | **HOLD_EVIDENCE** — potentially relevant but query answer fidelity and measured serving cost unclear | Retrieval correctness and response quality, strong RAG cache baselines, model/embedding/index overhead and E2E cost |
| [DAG-KV](https://atc.sigops.org/2026/accepted.html) / [KVLite](https://atc.sigops.org/2026/accepted.html) | Structured agent task-state/KV reuse | **HOLD_IDENTITY/G2** — do not promote tentative shorthand names without full canonical paper identity | Full official paper title, method/novelty vs AKV/PBKV/Radix cache, operation-history correctness and task execution data |
| [Chorus](https://atc.sigops.org/2026/accepted.html) (HKUST/Alibaba) | CPU–GPU cooperative serving for decode length skew | **HOLD_EVIDENCE** — author result not yet traced to detailed full paper | Decode timeline and CPU offload overhead, length distribution, online SLO tail and comparison with continuous batching |
| [Mosaic (CPU–GPU block-sparse)](https://atc.sigops.org/2026/accepted.html) (BJUT/Microsoft) | CPU–GPU coordination for sparse long-context decode | **HOLD_IDENTITY/G3** — separate identity from [ICML diffusion Mosaic](https://proceedings.mlr.press/v306/zheng26o.html), do not count as one or invent new DOI | Full paper + execution offload cost, sparse mask quality and live long-context TTFT/TPOT |
| [A Novel AI-Native GPU Kernel Programming Language](https://atc.sigops.org/2026/accepted.html) (Enflame/SJTU) | Kernel DSL and autonomous tuner | **HOLD_G2/G3/G5** — no differentiated compiler IR and runtime artifact evidence | Compiler/codegen/IR details, correctness gate, comparison against TileLang/Triton/CuTe and Code Agent strong baselines |

## Retracted public admissions — retained here, not canonical

| Earlier admission | Why previous KEEP was premature | Re-entry |
|---|---|---|
| [BMV: Breaking Monolithic Verification](https://atc.sigops.org/2026/accepted.html) | Lab-summary numbers + ATC G0 do not certify proof of lossless sampling or matched latest EAGLE-3 benchmark | Full PDF/algorithm proof, artifact/precision/acceptance trace, actual target pass cost |
| [IgniteServe](https://atc.sigops.org/2026/accepted.html) | Claimed cold-start improvements lack independently auditable cold/warm weights/compilation/graph-capture breakdown | Full paper/cold-start artifact, reproducible hardware initialization measurements, vLLM version parity |
| [HybridFaaS](https://yuanchaoxu6.github.io/publications/) | Author summary and venue metadata establish topic but not strong comparison for very large tail-delay/cost claims | Full prototype artifacts and absolute P99/cost/model concurrency/baseline setup |

## Other screened outcomes

| Candidate | Result |
|---|---|
| [Rocks, Pebbles and Sand / RPS-Serve](https://arxiv.org/abs/2603.26498); [author code link](https://github.com/muse-research-lab/rps-serve/tree/main) | **REMOVE_G5_FROM_SELECTIVE_AT_PRESENT**. Source includes vLLM 0.8.4 multimodal experiments and strong author-reported TTFT gains, but its core priority-by-modality + aging policy is simpler and less general than many existing SLO/modalities schedulers; arXiv HTML body still uses older **TCM-Serve** nomenclature despite newer public title. Not a claim that results are invalid; retain URL here, do not occupy scarce canonical space without demonstrated baseline novelty. |
| [Rocks Pebbles Sand multimodal prior](https://arxiv.org/abs/2603.26498) versus [the diffusion Mosaic](https://proceedings.mlr.press/v306/zheng26o.html) | **DISTINCT**: no overlap of identity or mechanisms; do not reuse “Mosaic” citation for the CPU–GPU sparse paper. |
| [FlashCodec](https://atc.sigops.org/2026/accepted.html) (video decode MLLM) | **HOLD_ADJACENT**: video codec acceleration needs demonstrable LLM/VLM decode-serving end-to-end contribution, not standalone media decode speed |
| [RS-Infer](https://atc.sigops.org/2026/accepted.html), [STRIDE](https://atc.sigops.org/2026/accepted.html) | **HOLD_SCOPE**: secure/private inference meaningful but distinct from performance-first public LLM serving collection; add only if performance/correctness mechanism is substantial and verifiable |
| [PrefixFlow](https://atc.sigops.org/2026/accepted.html) | **REMOVE_SCOPE**: training-time KV for RL, not LLM inference serving |
| [Cloudless Tomorrow](https://atc.sigops.org/2026/accepted.html), [Make Graphs Great Again](https://atc.sigops.org/2026/accepted.html), [TraJudger](https://atc.sigops.org/2026/accepted.html) | **REMOVE_SCOPE/G5**: agent memory/program structures/failure diagnosis are not demonstrated inference runtime cost improvements under our present curation contract |
| [The GPU Changes Everything: Rethinking GPU I/O Stack at Massive Scale](https://atc.sigops.org/2026/accepted.html) | **HOLD_ADJACENT**: systems foundation relevant to KV transfers, requires a concrete LLM inference path to enter selective collection |
| [LiteCache / CLO](https://arxiv.org/abs/2511.14510) | **INDEPENDENT_IDENTITY UNRESOLVED** relative to DittoCache: some author overlap and GPU-centric KV concept do **not** license automatic aliasing. Keep independent source in this ledger; no duplicate canonical entry |
| [HYPIC](https://arxiv.org/abs/2607.25087), [InfiniLoRA](https://arxiv.org/abs/2604.07173), [gKSM](https://arxiv.org/abs/2610.25219), [ELDR](https://arxiv.org/abs/2607.00466), [Feather](https://arxiv.org/abs/2605.06046), [energy-aware shared GPU scheduling](https://arxiv.org/abs/2606.30391) | **EXISTING_CANONICAL / NO NEW ROW**. For future venue corrections edit canonical row rather than duplicate the source identity. |
| [SptcAttn source-side baseline diagnostics](https://github.com/microsoft/MInference/issues/199) | **DIAGNOSTIC_ONLY**: author reported preprint baseline OOM issues, **not** evidence of SptcAttn speedup. Do not use an open GitHub issue to claim GPU performance. |

## Definitive handoff

- There is **no active unresolved HOLD row in public topics**. This ledger is the sole current-turn review receipt for the above candidates; no second JSONL or TSV catalog is generated.
- All **high-signal unverified ATC records** have a targeted evidence trigger above; **none** was silently promoted on venue alone.
- **Most valuable future re-check if primary full paper appears:** DittoCache (host→GPU execution path), ATP (dynamic TP/PD), SptcAttn (sparse tensor-core mapping), JetFire (corrective hybrid I/O); next TensorBridge (FP4/FP8 interface), CacheFS (production weight distribution).
- **Not a promise of continuing background work.** As of October 26, the ATC conference has not yet happened. Final archival artifact changes should be judged once available.
- **Latest canonical proposed PR count: 766** = existing main **736** + earlier source-verified **23** + eligible later **7**; BMV/IgniteServe/HybridFaaS are explicitly excluded in this proposal. A paper's G3/G4 completeness may remain limited even for existing 766 and no universal independent numerical reproduction is claimed.
