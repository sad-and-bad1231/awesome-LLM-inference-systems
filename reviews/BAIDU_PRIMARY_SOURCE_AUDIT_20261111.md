# 2026-11-11 — Baidu primary-source deep audit (organization + frontier context)

**Scope:** restore a precise Baidu/PaddlePaddle technical map from original NLP papers through the 2026-11-11 model release, current inference engine, hardware kernels and automated research. Changes are intentionally limited to [Baidu](../organizations/Baidu.md), [organizations navigation](../organizations/README.md), [RSI-adjacent frontier](../frontiers/README.md) and this dated receipt.

**Decision:** **ENRICH_ORGANIZATION + ADD_FRONTIER_CROSSREFERENCE; 0 canonical paper admissions; 0 topic deletions; 0 new frontier headings; 0 hardware reproductions.** Canonical inventory remains **852**, with 8 mechanisms, 44 engineering tracks and 7 active frontiers. Do not infer a fully verified G0–G5 corpus from this source audit.

## Why the previous profile was inadequate

The earlier [Baidu page](../organizations/Baidu.md) contained a model catalog and two source entries (FastDeploy, PaddleNLP). It omitted (i) pre-ChatGPT ERNIE research lineage, (ii) the 2025 model–inference co-design report, (iii) independent attention kernel library FlashMask, (iv) 2026 hybrid sparse/compressed attention and draft mechanisms, (v) native XPU deployment, and (vi) the **November 9 ERNIE Evolve** production-inference optimization account. A model's chatbot ranking is not a valid substitute for an engineering-source audit.

## Primary-source evidence, evidence type and disposition

| Item | Verified source | Mechanism / current scope | Editorial disposition |
|---|---|---|---|
| PaddlePaddle | [Official framework repository](https://github.com/PaddlePaddle/Paddle) | Framework open source since 2016; present AI framework/deployment ecosystem | **ORG_HISTORY**; not a topic paper |
| ERNIE (2019) | [Original authors' paper](https://arxiv.org/abs/1904.09223) | Knowledge-driven phrase/entity masking in pretrained NLP | **ORG_HISTORY**, **REMOVE_SCOPE if proposed as inference paper** |
| ERNIE 2.0 (AAAI 2020) | [Publisher record](https://ojs.aaai.org/index.php/aaai/article/view/6428) | Incremental lexical/syntactic/semantic pretraining tasks | **ORG_HISTORY**; do not call Baidu the inventor of all NLP |
| ERNIE 3.0 / Titan (2021) | [3.0](https://arxiv.org/abs/2107.02137) · [Titan](https://arxiv.org/abs/2112.12731) | Knowledge-enhanced generative pretraining and reported 260B dense scale | **ORG_HISTORY**, not serving benchmark |
| JIZHI (2021) | [Original preprint](https://arxiv.org/abs/2106.01674) · [Paddle Serving](https://github.com/PaddlePaddle/Serving) | Asynchronous staged pipeline + storage hierarchy + resource allocation | **ORG_ADJACENT**; evaluated on search/recommendation web inference, **not LLM token decoding** |
| FlashMask (2024 / ICLR 2025) | [Paper](https://arxiv.org/abs/2410.01359) · [official code](https://github.com/PaddlePaddle/FlashMask) | O(N) column-mask representation + sparse kernels; fine-tuning/alignment evidence | **ORG_KERNEL_LINEAGE; CANONICAL HOLD_SCOPE** pending standalone autoregressive inference contribution & fair comparator |
| ERNIE 4.5 (2025) | [Official report entry](https://ernie.baidu.com/research/posts/ernie4.5/) · [official repository](https://github.com/PaddlePaddle/ERNIE) | Multimodal MoE routing, low-bit inference kernels, PD/EP co-design | **ORG_ARCHITECTURE + ORG_ENGINEERING**, distinct from independent E2E replication |
| FastDeploy 2.0+ | [Engineering report](https://ernie.baidu.com/research/posts/fastdeploy2.0/) · [official runtime](https://github.com/PaddlePaddle/FastDeploy) · [P/D docs](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/features/disaggregated.md) | Load-aware P/D router, KV handoff, EP, quantization, speculative/MTP, chunked prefill | **ORG_CODE**; code/docs available; all author performance comparisons are version/hardware/workload-specific |
| PLAS (2025) | [Official long-context inference report](https://ernie.baidu.com/research/posts/plas/) | Learned block-sparse retrofit for ERNIE 4.5 with FastDeploy | **ORG_ENGINEERING; APPROXIMATE_QUALITY_CHECKED (author)**, not exact unchanged-output inference |
| ERNIE 5.0 (2026) | [arXiv report](https://arxiv.org/abs/2602.04705) · [Baidu technical summary](https://ernie.baidu.com/research/posts/ernie5.0/) | Unified modalities, sparse MoE, elastic depth/width/top-k | **ORG_ARCHITECTURE**; elastic deployment implication is not proof of current runtime |
| ERNIE 5.5 Flash Base (2026-11-05) | [Original release](https://ernie.baidu.com/release/ernie-5-5-flash-base/) | 37 HCA + 6 MLA/DSA layers; 128-token compression; multi-router latent MoE; mHC, ECHO/speculative, FlashMask-4 training | **ORG_ARCHITECTURE**; weights available; released base has **no post-training**; no independent E2E claim |
| ERNIE 5.5 Flash Preview (2026-11-11) | [Official release](https://ernie.baidu.com/zh/release/ernie-5-5-flash-preview/) | First post-trained preview; API available; 1M context; future weights promised by Nov 25 | **ORG_RELEASE_ONLY**; weight promise **not** a present public checkpoint; vendor scores are not independent measurements |
| FlashMask-3 / -4 (2026) | [Official code and feature/compatibility tables](https://github.com/PaddlePaddle/FlashMask) · [FlashMask-3 preprint](https://arxiv.org/abs/2610.17901) | CP balance/overlap; CuTe-DSL large-head masked attention on SM90/SM100 | **ORG_KERNEL_LINEAGE; CANONICAL HOLD_EVIDENCE** for online AR serving; actual device support must be checked, no Ascend portability presumed |
| Kunlunxin XPU path | [FastDeploy versioned deployment example](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/usage/kunlunxin_xpu_deployment.md) | XPU runtime/backend, EP, RDMA/BKCL setup | **ORG_DEVICE_BACKEND**; XPU configuration is not Ascend CANN evidence |
| ERNIE Evolve (2026-11-09) | [First-party research/engineering report](https://ernie.baidu.com/research/posts/ernie-evolve/) | Agent-led optimization of P800 native kernels, deterministic GPU inference, speculative decode and MoE paths | **FRONTIER_CROSSREFERENCE; AUTHOR_ONLY_CLAIM**; blog and selective benchmark artifacts do not establish independently reproducible production outcome |

## G0–G5 boundary review on new candidates

- **G0 identity:** all selected model reports, papers, blogs and upstream code have first-party source links. Do not turn a blog into a peer-reviewed paper. The original FlashMask work is a 2024 preprint with ICLR 2025 paper lineage; FlashMask-3 is a distinct 2026 preprint; FlashMask-4 is implementation/release evidence, not the same publication.
- **G1 inference scope:** FastDeploy and PLAS directly address LLM inference; ERNIE 5.5 architecture has inference cost implications; ERNIE Evolve covers actual inference optimization. The classic ERNIE language-representation series, FlashMask original training experiments and JIZHI recommendation serving are **context**, not automatic LLM inference-topic admissions.
- **G2 mechanism and baseline:** HCA/MLA has an explicit KV compression vs token-level access tradeoff; ECHO changes speculative draft production; FastDeploy offers P/D and KV transfer; PLAS requires an approximate attention change. Do not call established sparse attention or PD separation a wholly new frontier.
- **G3 evidence:** public sources include selected author-reported speed/throughput, not matched independent vLLM/SGLang E2E reruns. ERNIE Evolve reports **623.6% of baseline speed** on Kunlunxin P800 low-latency path, plus **+33.7% throughput** for deterministic GPU inference and **+14.9% decode speed** in another GPU path. The P800 gain includes enabling previously unused optimizations. No claim transfers automatically to all hardware, models, contexts or SLO settings.
- **G4 traceability:** upstream Paddle, FastDeploy, FlashMask and ERNIE model code exist; release branches, configs, reproducible experiment artifacts, workload traces and evaluator policies need case-specific checking. ERNIE Evolve's first-party blog is not enough for independent production-replay verification.
- **G5 editorial value:** source map and frontier cross-reference are valuable; **topic admissions deferred** until a distinct inference-specific G1 mechanism, meaningful G3 comparison and G4 receipt support a single canonical row rather than vendor promotional evidence.

**Reproduction state for this audit:** `artifact_inspected` (GitHub README/documentation and source-boundary review); `not_attempted` for kernel/runtime execution. No NPU/GPU device tests, source checkout, runtime traces, or throughput benchmarks were performed.

## Special claim rejected pending evidence

**Baidu invented Looped Transformer / is the origin of another vendor's recurrent-depth frontier model — UNVERIFIED.** The reviewed sources do not establish a primary Baidu paper with clear priority and technical continuity into the other model. Similar mechanisms, temporal precedence, adoption and formal attribution are different propositions. Neither claim is included as a fact on the company page.

## Next evidence work (not completed here)

1. Trace pinned FastDeploy router → P/D KV allocation/transfer → decoder/EP/sparse attention for a single documented release; compare with vLLM/SGLang on equivalent model and workload.
2. Study ERNIE 5.5 HCA/MLA/ECHO implementation to derive per-layer KV bytes, indexer cost, acceptance rate and quality/latency tradeoff. Base weights are not the released Preview checkpoint.
3. Validate FlashMask-4 shape/device/precision coverage and isolate prefill/decode kernel microbenchmarks before any canonical kernels-paper decision.
4. Reproduce ERNIE Evolve on fixed model, precision, real accelerator, hidden request shapes and immutable oracle; compare fixed agent, inheritance and search-memory under equal LLM/accelerator budgets.
5. Independently verify any Baidu Looped Transformer priority or lineage claim against original papers before adding it as history.

**Audit outcome:** organization narrative substantially repaired; open research questions preserved; **no fabricated leaderboard comparison, no paper count churn and no implied hardware reproduction**.
