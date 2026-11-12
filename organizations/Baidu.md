# Baidu / PaddlePaddle

**Research lineage → model architecture → inference runtime → device kernels → automated engine optimization.** Baidu should not be characterized only by ERNIE's current leaderboard position. Its public record includes early Chinese NLP/pretraining research, a domestic deep-learning framework, executable LLM serving infrastructure, and recent low-level inference optimization. Conversely, historical influence, current model quality, and independently validated serving performance are **different claims**.

[← Organizations](README.md) · [← Home](../README.md) · [Autonomous engine evolution](../frontiers/README.md#autonomous-inference-engine-evolution-separate-engine-evolution-from-rsi) · [2026-11-11 source audit](../reviews/BAIDU_PRIMARY_SOURCE_AUDIT_20261111.md) · [Mechanism and code deep dive](../reviews/BAIDU_MECHANISM_CODE_AUDIT_20261111.md)

## 1. Research lineage: important, but not a claim to have invented NLP

| Year | First-party / published milestone | What it actually contributed | Boundary |
|---|---|---|---|
| 2016 | [PaddlePaddle framework](https://github.com/PaddlePaddle/Paddle) | China-origin open-source deep-learning framework and software ecosystem | Framework history, not evidence of a present-day serving speedup |
| 2019 | [ERNIE: Enhanced Representation through Knowledge Integration](https://arxiv.org/abs/1904.09223) | Entity- and phrase-level knowledge masking for language representation, beyond ordinary token masking | Builds on the BERT pretraining paradigm; not the origin of NLP or Transformers |
| 2019 / AAAI 2020 | [ERNIE 2.0: Continual Pre-Training](https://ojs.aaai.org/index.php/aaai/article/view/6428) | Incrementally introduces lexical, syntactic and semantic pretraining tasks | Pretraining methodology, not an LLM serving mechanism |
| 2021 | [ERNIE 3.0](https://arxiv.org/abs/2107.02137) and [ERNIE 3.0 Titan](https://arxiv.org/abs/2112.12731) | Knowledge-enhanced understanding/generation at larger scale; Titan reports 260B-parameter dense pretraining on PaddlePaddle | Primarily model/training evidence |
| 2021 | [JIZHI: web-scale model-as-a-service](https://arxiv.org/abs/2106.01674) | Staged asynchronous inference pipeline, hierarchical storage and adaptive resource allocation | **Recommendation/search model serving**, not autoregressive LLM serving; a useful systems antecedent |
| 2024 / ICLR 2025 | [FlashMask](https://arxiv.org/abs/2410.01359) ([code](https://github.com/PaddlePaddle/FlashMask)) | Column-wise sparse mask representation with O(N) mask storage and mask-aware kernels | Original evaluations focus on LLM fine-tuning/alignment; do not quote as an online decode gain |
| 2025 | [ERNIE 4.5 technical report](https://ernie.baidu.com/research/posts/ernie4.5/) and [official ERNIE code](https://github.com/PaddlePaddle/ERNIE) | Heterogeneous multimodal MoE, routing, low-bit quantization and P/D infrastructure | Distinguish model report and executable FastDeploy stack |
| 2026 | [ERNIE 5.0 technical report](https://arxiv.org/abs/2602.04705) ([overview](https://ernie.baidu.com/research/posts/ernie5.0/)) | Unified multimodal autoregression, ultra-sparse MoE, elastic depth/width/sparsity | Model/training mechanism with deployment implications, not an independently validated runtime |
| 2026-10 | [DCore controlled speculative-decoding study](https://arxiv.org/abs/2610.24993) · [code/26 drafter checkpoints](https://github.com/ernie-research/DCore) | Shared training/data/runtime and throughput evaluation of multiple speculative drafters; strong cost-accounting evidence | A real **SGLang/Qwen3 benchmarking artifact**, not a Baidu-owned universal inference engine |
| 2026-11 | [ERNIE 5.5 Flash Base](https://ernie.baidu.com/release/ernie-5-5-flash-base/) and [ERNIE Evolve](https://ernie.baidu.com/research/posts/ernie-evolve/) | Hybrid compressed/sparse attention, latent MoE, built-in draft decoding; agent-assisted optimization of real inference paths | Base weights available; Evolve performance is author-reported |

**Identity caution:** evidence reviewed here does **not** establish that Baidu invented Looped Transformer/recurrent-depth inference, nor that an unpublished third-party frontier model adopted a Baidu mechanism. The separately published Universal Transformer/parameter-sharing research cannot be reassigned to Baidu by resemblance. Keep this claim **UNVERIFIED**, not a historical milestone.

## 2. Official ERNIE model families and inference-relevant architecture

**Primary catalog:** [Baidu model overview](https://cloud.baidu.com/product/model.html), [Qianfan](https://cloud.baidu.com/product/wenxinworkshop.html) and [ERNIE research/releases](https://ernie.baidu.com/research/). Hosted third-party models on Qianfan are **not** Baidu-owned. A family name, API preview and downloadable checkpoint are not the same artifact.

| Owned family / status | Architecture / inference consequence | Primary source |
|---|---|---|
| **ERNIE 5.5 Flash Base** (2026-11-05, **open base weights**) | 280B total / 14B active; 43 layers; hybrid HCA/MLA sparse attention; multi-router latent MoE; mHC; ECHO-backed speculative decoding. Base checkpoint precedes mid/post-training. | [Detailed release, architecture, model-card links and license](https://ernie.baidu.com/release/ernie-5-5-flash-base/) |
| **ERNIE 5.5 Flash Preview** (2026-11-11, **API preview**) | First post-trained preview from the Flash Base; 1M-token context as advertised. **Weights not yet published as of Nov 11**; Baidu says release by Nov 25. | [First-party announcement](https://ernie.baidu.com/zh/release/ernie-5-5-flash-preview/) |
| **ERNIE 5.1** | Subsequent foundation/model-service family; catalog only unless a separate technical mechanism is documented. | [Official model catalog](https://cloud.baidu.com/product/model.html) |
| **ERNIE 5.0 / 5.0-Thinking** | 2.4T-parameter unified multimodal architecture; next-group-of-tokens, modality-agnostic MoE routing, elastic configurations. | [Technical overview](https://ernie.baidu.com/research/posts/ernie5.0/) · [report](https://arxiv.org/abs/2602.04705) |
| **ERNIE 4.5 / Turbo / VL / small models** | Dense and MoE variants with heterogeneous modality routing, low-bit kernels and FastDeploy deployment paths. | [Official model/code family](https://github.com/PaddlePaddle/ERNIE) |
| **ERNIE X1 / X1 Turbo / X1.1** | Reasoning-oriented releases; model-service capability does not itself imply a novel scheduler. | [Qianfan](https://cloud.baidu.com/product/wenxinworkshop.html) |
| **PaddleOCR-VL / PP-Structure, speech and media models** | Document, vision, speech and generation workloads; distinct runtime/state contracts. | [Model catalog](https://cloud.baidu.com/product/model.html) |

### ERNIE 5.5 Flash: architecture-to-execution mapping

| Mechanism | Concrete disclosed design | Systems question / measurement |
|---|---|---|
| **HCA + MLA/DSA hybrid attention** | 37 of 43 layers use HCA, compressing 128 historical tokens into one cached entry plus a recent raw-token window; six MLA layers retain token-level access, with sparse top-k selection for long context. | Per-layer KV bytes, compressed-state construction, indexer/selection overhead, prefill vs decode latency, effective long-context quality; compression is **not** exact KV equivalence |
| **Head-size asymmetry / VHA / low-rank gates** | 512-dimensional heads in cheaper HCA layers vs 256-dimensional MLA heads; low-rank gating and lightweight cross-head mixing; first-party report claims VHA can be fused into attention. | Actual kernel shapes, fusions and register/shared-memory tradeoffs; no assumed CUDA → Ascend portability |
| **Multi-Router Latent MoE** | 512 routed experts (top-10) plus one shared expert; 4096→2048 latent projection reduces dispatch/combine width; multi-router scoring changes expert selection. | EP all-to-all bytes, imbalance/tail expert occupancy, dispatch/combine cost; compare at equal activated compute and quality |
| **mHC residual streams** | Four residual streams mixed through constrained matrices. | Extra memory/materialization and kernel fusion across residual + quantization boundaries |
| **ECHO instead of a standalone MTP module** | Reuses a backbone layer for future-token prediction and drafting during speculative decoding. | Draft cost, acceptance rate, verification cost, net TPOT/throughput under matched workload; **not** guaranteed lossless speedup without the serving algorithm and oracle; the model card reports **0.36B additional ECHO parameters** outside the base model count |
| **FlashMask-4 for training large head dims** | SM90/SM100 CuTe-DSL kernels with flexible mask representation; large dimensions up to QK 576 / V 512 on SM100. | Original report's kernel comparisons are **not** end-to-end ERNIE serving results; hardware paths differ from XPU/Ascend |

Source: [ERNIE 5.5 Flash Base architecture and training system](https://ernie.baidu.com/release/ernie-5-5-flash-base/), [FlashMask source](https://github.com/PaddlePaddle/FlashMask).

## 3. Execution stack: read code, not merely model cards

| Layer | First-party artifact | Mechanism worth tracing | Verification boundary |
|---|---|---|---|
| **Framework** | [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) | Tensor execution, operator integration, compilation/distributed execution | Framework ownership does not make every hosted model or kernel Baidu-authored |
| **Model / development** | [PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP) · [ERNIE / ERNIEKit](https://github.com/PaddlePaddle/ERNIE) | Model implementations, distributed training, compression, prediction and export | Much is training infrastructure rather than inference-only |
| **LLM serving runtime** | [FastDeploy](https://github.com/PaddlePaddle/FastDeploy) · [P/D documentation](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/features/disaggregated.md) | P/D role separation, load-aware router, layerwise KV transfer, prefix caching, EP, quantization, speculative/MTP, chunked prefill, graph capture | Features are release/model/hardware dependent; self-reported throughput is not a neutral vLLM benchmark |
| **Sparse attention retrofit** | [PLAS on ERNIE 4.5](https://ernie.baidu.com/research/posts/plas/) | Pluggable learned block-sparse attention for long context in FastDeploy; author reports quality/performance tradeoff | **Approximate/model-path change**, not bitwise-exact replacement; report model/context/hardware |
| **Attention kernel** | [FlashMask / FlashMask-3 / FlashMask-4](https://github.com/PaddlePaddle/FlashMask) | Sparse mask representation; CP load balance/communication overlap; SM90/SM100 CuTe kernels | Separate **training CP** from online autoregressive inference. FlashMask-4 large-head implementations are GPU-specific, not confirmed on Ascend 910B2 |
| **Device/backend** | [Kunlunxin XPU deployment](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/usage/kunlunxin_xpu_deployment.md) | XPU-native kernels, parallelism, BKCL/RDMA settings, model-specific execution | Hardware and version matrix must be pinned; portability to CANN is not implied |
| **Legacy model serving** | [Paddle Serving](https://github.com/PaddlePaddle/Serving) · [JIZHI paper](https://arxiv.org/abs/2106.01674) | Historical asynchronous pipeline, tiered state and resource-control design | Recommendation inference antecedent, not an equivalent modern LLM decoder |

**Useful execution trace:** arrival/router → prefill replica → KV block allocation & transfer → decode replica → speculative draft/verify → MoE dispatch/collectives → attention kernel → host synchronization and output. Compare exact FastDeploy release/configuration against equivalent vLLM/SGLang functions; their public API compatibility is **not** evidence of internal architectural identity.

## 4. ERNIE Evolve (2026-11-09): inference-engine optimization, not proven model RSI

[First-party technical article](https://ernie.baidu.com/research/posts/ernie-evolve/) describes **Director → Selector → Executor → independent Evaluator/Reviewer**, a version tree and remembered experiment outcomes. It includes *real inference engineering tasks*, not only an abstract kernel agent:

| Task | Mechanisms described | Reported outcome / caveat |
|---|---|---|
| **Kunlunxin P800 low-latency decoding** | Enable native mHC fusion and speculative path; reduce Python/temporary tensor/host sync overhead; select native attention; repair DeepEP low-latency dispatch | Final generation speed **623.6% of the starting baseline** on the specified workload, **author-reported**; large gain includes enabling previously unused optimized paths, not a universal 6× algorithm |
| **GPU deterministic inference** | Triton deterministic sampling, sparse attention, small-M GEMM, mHC partitioning; enforce bitwise batch-invariant tokens/logprobs | **+33.7% throughput**, **−26% TPOT**, **−12% TTFT** claimed for the tested setup; full workload/harness parity not independently checked |
| **GPU peak single-request decoding** | MoE mapping, FP8 fusion, Small-M matmul reformulation, draft verification/sampling/communication fusion | **+14.9% decode speed** claimed after an already optimized baseline; vendor evidence only |

**Research significance:** a credible first-party **industry signal for agent-led cross-layer inference optimization** and feedback-driven hypothesis selection. **Limit:** the publicly described process, selective released benchmark results and vendor performance claims do **not** establish held-out generalization, reproducible production speedups or a recursively self-improving model/agent. Compare the [RSI-adjacent frontier](../frontiers/README.md#autonomous-inference-engine-evolution-separate-engine-evolution-from-rsi) under matched optimizer budget and hidden correctness tests.

## 4.5. Critical mechanism assessment and DCore admission

**Original work vs adopted techniques.** The ERNIE 5.5 architecture is a carefully engineered *combination*. [Virtual Head Attention](https://arxiv.org/abs/2610.17959), [Multi-View Latent MoE](https://arxiv.org/abs/2610.40577) (ERNIE uses its **Multi-Router** component) and [ECHO](https://arxiv.org/abs/2610.24766) are relevant first-party 2026 research; MLA, DSA, mHC and Muon also have prior literature and must not all be credited as Baidu inventions. ECHO's 'self-recursion' in future-token drafting is **not** evidence of the Looped Transformer / recurrent-depth architecture.

**Do not misread the optimizations:**

- **HCA compresses memory in 37 layers; it does not reduce all system KV storage 128×.** Six MLA layers retain per-token history, and DSA selection removes computation rather than automatically deleting stored state. Use [the layerwise cost model](../reviews/BAIDU_MECHANISM_CODE_AUDIT_20261111.md#2-ernie-55-flash-decompose-model-innovation-into-runtime-costs) before claiming savings.
- **MoE latent width halves activation traffic *per dispatched representation*, not necessarily MoE wall time.** Router, projections, expert imbalance, kernel launch and collectives still matter.
- **ECHO has future-token prediction capability, but acceptance is not TPS.** Count proposal, verification, fallback and batch overhead at equal quality.
- **FlashMask-3's published 128-GPU benefits are long-context *training* benefits.** SM100 CuTe overlap and CPB source availability have separate caveats; there is no verified Ascend 910B2 kernel here.

**Source-code entrypoints inspected:** [Go Router policies](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/online_serving/router.md) → [core resource manager](https://github.com/PaddlePaddle/FastDeploy/blob/develop/fastdeploy/engine/sched/resource_manager_v1.py) → [KV transfer manager](https://github.com/PaddlePaddle/FastDeploy/blob/develop/fastdeploy/cache_manager/cache_transfer_manager.py). In the code overview, older top-level scheduler modules are being deprecated: router instance selection, in-engine request preemption and KV transfer are **distinct control/data paths**. See [code trace and unknowns](../reviews/BAIDU_MECHANISM_CODE_AUDIT_20261111.md#3-fastdeploy-actual-code-path-and-controldata-boundaries).

**New strict admission:** [When Does Better Acceptance Pay? A Controlled Study of Speculative Decoding](https://arxiv.org/abs/2610.24993) (**2026 preprint**) / [DCore source](https://github.com/ernie-research/DCore) is now indexed **once** under [Benchmarking & Systems Analysis](../topics/benchmarking-analysis.md#performance--efficiency-studies-27), not duplicated under Decoding. It compares seven methods, shared SGLang setup, Qwen3-4B/8B, 10 benchmarks, budgets 8/16, concurrency and matching training data; source release includes 26 draft checkpoints. **Author-reported, not independently replicated.** Its transferable result is a controlled evaluation discipline, not a universal draft ranking.

**ERNIE Evolve's key negative signals:** general-purpose communication **regressed 14%** in one P800 test; a MoE communication flag alone was noise-level; already-optimized GPU communication near NVLink latency floor and kernel gaps at 2–4% did **not** justify further focus. The project does release [public benchmark solutions/logs](https://github.com/ernie-research/ERNIE-Evolve-Results), but **not** full production-inference replay artifacts. This is evidence for hypothesis-driven engineering, not proof of recursive improvement of the underlying model.

## 4.6. Pinned FastDeploy ↔ vLLM ↔ SGLang execution comparison (closeout)

**[Read the final source-level contract comparison](../reviews/BAIDU_NATIVE_EXECUTION_CLOSEOUT_20261111.md)** before assuming that similar public feature names imply equivalent runtime behavior. At frozen SHAs: FastDeploy `d923caf`, vLLM `0fc695f`, SGLang `23a45fd` and the associated vLLM-Ascend plugin `5cb98ca` (plugin native call-chain **not** audited here).

The verified, useful distinction: FastDeploy's Go Router performs **instance/pair selection** (with distinct cache-aware and load policies), `resource_manager_v1` performs **engine request, token, block and preemption** decisions, and `CacheTransferManager` handles **data movement**. vLLM V1's `num_computed_tokens` scheduler, SGLang's RadixCache/Disaggregation queues and vLLM KVConnector API represent different boundaries; this is a **mechanism comparison, not a benchmark or superiority claim**. Note especially the separate router-prefix estimate vs engine-owned physical KV, prefill/decode block reservation and unvalidated activation of V1 in any particular commercial configuration.

**Closeout decision:** evidence from 2019 ERNIE through ERNIE 5.5, FastDeploy and Evolve has been mapped to original sources; the DCore paper has one G0–G5 admission; remaining candidate/model/kernel lines retain bounded labels. **No more NPU work justified by this audit alone.**

## 5. Suggested reading and replication path

1. **Historical understanding:** ERNIE (2019) → ERNIE 2.0 (AAAI 2020) → ERNIE 3.0/Titan; study the ideas, **do not** place training-only NLP papers into inference topics.
2. **Architecture:** ERNIE 4.5 report → ERNIE 5.0 report → ERNIE 5.5 Flash Base architecture; derive attention-state, MoE-communication and draft/verify costs.
3. **Runtime/code:** FastDeploy P/D router/KV transfer → EP/quantization → sparse attention PLAS; inspect actual deployed branch before measurements.
4. **Kernel/source:** FlashMask repo (original → -3 CP → -4 CuTe) and XPU deployment; distinguish CUDA/SM100, XPU P800 and Ascend paths.
5. **Research frontier:** ERNIE Evolve → SEIS / Together Compiler; test what transfers across task distribution, hardware and verification constraints.

**Open questions:** (a) How much HCA saves in *total* KV memory once local windows, MLA state and indexers are included? (b) Which FastDeploy policies and kernels remain useful under real dynamic serving SLOs? (c) Can ERNIE Evolve's gains survive held-out models/request shapes/equal accelerator-hour budgets? (d) Which mechanisms are truly native to Kunlunxin, rather than generic CUDA kernels or imported third-party libraries?

**Editorial status (2026-11-11, completed source audit + pinned source-level closeout):** organization profile plus independent mechanism/code audit; **one** controlled DCore preprint admitted to Benchmarking & Systems Analysis (**852 → 853 corpus entries**), **no** new frontier count and **no** benchmark reproduced. [First source audit](../reviews/BAIDU_PRIMARY_SOURCE_AUDIT_20261111.md) is a dated 852-entry snapshot; [second G0–G5 mechanism audit](../reviews/BAIDU_MECHANISM_CODE_AUDIT_20261111.md) supersedes that intake count; [source comparison closeout](../reviews/BAIDU_NATIVE_EXECUTION_CLOSEOUT_20261111.md) adds **no further canonical entry**.
