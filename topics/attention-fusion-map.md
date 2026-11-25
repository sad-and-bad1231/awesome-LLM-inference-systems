# Attention & Kernel Fusion — engineering reading map

[← Kernel topic](kernels-compilers.md) · [← Topics](README.md) · [Communities](../communities/README.md)

A discovery index for five principal inference ecosystems: model semantics → backend → library/custom op → physical kernel → serving step. Detailed Ascend source paths and version-specific engineering references are maintained in the [Ascend Inference Profile Map](https://github.com/sad-and-bad1231/Ascend-Inference-Profile-Map/blob/main/tracks/kernels-compilers.md).

## 1. Separate the execution layers

| Layer | What to distinguish |
|---|---|
| Model computation | Softmax attention with MHA/MQA/GQA or MLA; recurrent/token-mixing layers such as GDN and KDA; hybrid models compose different layer types. |
| Visibility and state | Dense/causal/windowed/learned sparse selection; explicit, paged or compressed KV; recurrent state has different update and rollback semantics. MLA does not imply sparse selection. |
| Physical kernel | Tiling, online softmax, split-K reduction, gather, precision, layout, pipeline and hardware mapping. FlashAttention is an algorithm/implementation family, not a model attention architecture. |
| Backend and compiler | Shape/dtype/layout guards, metadata/workspace, kernel selection, graph capture and pattern replacement. A backend may dispatch several kernels; a compiler pass still needs a compatible implementation. |
| Runtime and serving | Prefill, extend, decode, mixed batches and multi-token verification; scheduling, context parallelism and communication change the actual workload and dependencies. |

Treat semantic approximation, arithmetic precision and physical execution as separate axes. Exact Top-K selection is not equivalent to exact dense attention. Paging is not attention sparsity. GDN/KDA state is not ordinary KV compression.

## 2. First-party implementation paths

| Ecosystem | Discovery entry | What to follow |
|---|---|---|
| vLLM | [Attention backends](https://docs.vllm.ai/en/latest/design/attention_backends/) · [Fusion](https://docs.vllm.ai/en/latest/design/fusions/) | Backend compatibility, native extensions and compiler passes |
| vLLM-Ascend | [Attention](https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/attention) · [Native ops](https://github.com/vllm-project/vllm-ascend/tree/main/csrc) · [Graph mode](https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/graph_mode.html) | FIA/MLA/SFA, GDN/KDA, GMM/MoE/MC2, graph fusion |
| SGLang | [Backend implementations](https://github.com/sgl-project/sglang/tree/main/python/sglang/srt/layers/attention) · [SGL Kernel NPU](https://github.com/sgl-project/sgl-kernel-npu) | Phase-specific dispatch, recurrent kernels and specialized execution |
| DeepSeek | [DeepInfer](https://github.com/deepseek-ai/DeepInfer) · [organization library index](../organizations/DeepSeek.md#execution-and-communication-libraries) | Model-specialized attention, GEMM, EP and native integration |
| CANN | [Ascend C](https://asc.gitcode.com/guide/) · [ops-transformer](https://gitcode.com/cann/ops-transformer) · [CATLASS](https://gitcode.com/cann/catlass) · [graph-autofusion](https://gitcode.com/cann/graph-autofusion) | Native operators, matrix templates and fusion |

### vLLM

[Selector and backend contract](https://github.com/vllm-project/vllm/tree/main/vllm/v1/attention) → [native operators](https://github.com/vllm-project/vllm/tree/main/csrc) → [fusion passes](https://github.com/vllm-project/vllm/tree/main/vllm/compilation/passes/fusion). The selector checks shape, dtype, cache and feature compatibility; backend metadata and physical kernel blocks are distinct from cache allocation. Follow the [fusion tracker](https://github.com/vllm-project/vllm/issues/36066) and [releases](https://github.com/vllm-project/vllm/releases).

### vLLM-Ascend

[Attention backend](https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/attention) → [native custom ops](https://github.com/vllm-project/vllm-ascend/tree/main/csrc) → [compilation](https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/compilation). Distinguish TorchNPU/CANN kernels, plugin-native fused ops, graph rewrites and ACLGraph/SuperKernel. Follow the [support matrix](https://docs.vllm.ai/projects/ascend/en/main/user_guide/support_matrix/feature_matrix.html) and [releases](https://github.com/vllm-project/vllm-ascend/releases). Installed-stack source and operator-level qualification belong to the [Map](https://github.com/sad-and-bad1231/Ascend-Inference-Profile-Map/blob/main/docs/OPERATOR_OFFICIAL_SOURCES.md).

### SGLang

[Backend guide](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/docs/docs/advanced_features/attention_backend.mdx) · [SGL Kernel NPU](https://github.com/sgl-project/sgl-kernel-npu) · [NVIDIA Mega](https://github.com/sgl-project/sgl-nvidia-mega) · [AMD Mono](https://github.com/sgl-project/sgl-amd-mono). Phase-specific attention and model-specific fused execution are separate mechanisms. Follow [Monokernel RFC](https://github.com/sgl-project/sglang/issues/43949), [Low-Latency Mode](https://www.lmsys.org/blog/2026-10-18-sglang-low-latency-mode/) and [releases](https://github.com/sgl-project/sglang/releases).

### DeepInfer and DeepSeek's kernel stack

[DeepInfer](https://github.com/deepseek-ai/DeepInfer) uses [FlashMLA](https://github.com/deepseek-ai/FlashMLA), [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), [DeepEP](https://github.com/deepseek-ai/DeepEP), [DeepSelect](https://github.com/deepseek-ai/DeepSelect), [TileKernels](https://github.com/deepseek-ai/TileKernels) and [DeepJIT](https://github.com/deepseek-ai/DeepJIT). See the [DeepSeek profile](../organizations/DeepSeek.md) for platform/release scope and [deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) for public versus production coverage. For Ascend native code, tests and runtime dependencies, use the [Map](https://github.com/sad-and-bad1231/Ascend-Inference-Profile-Map/blob/main/docs/OPERATOR_OFFICIAL_SOURCES.md#23-deepseek-native-execution-inspect-implementation-and-tests).

### CANN / Ascend native ecosystem

[Huawei profile](../organizations/Huawei.md) · [CANN community](https://gitcode.com/cann/community) · [CANN learning hub](https://gitcode.com/cann/cann-learning-hub) · [CANNBot](https://gitcode.com/cann/cannbot). Follow the upstream projects for new operator, compiler and device-runtime mechanisms.

**Engineering handoff:** [Operators track](https://github.com/sad-and-bad1231/Ascend-Inference-Profile-Map/blob/main/tracks/kernels-compilers.md) → [Official source map](https://github.com/sad-and-bad1231/Ascend-Inference-Profile-Map/blob/main/docs/OPERATOR_OFFICIAL_SOURCES.md) → [Profiling toolchain](https://github.com/sad-and-bad1231/Ascend-Inference-Profile-Map/blob/main/docs/PROFILING_TOOLCHAIN.md) → [Experiment playbook](https://github.com/sad-and-bad1231/Ascend-Inference-Profile-Map/blob/main/docs/OPERATOR_EXPERIMENT_PLAYBOOK.md). These own native CANN libraries, PTO/DSL, specific implementation paths, version qualification and experiment methods; do not duplicate them here.

### Shared libraries and programming models

| Scope | Projects |
|---|---|
| Softmax attention and serving | [FlashAttention](https://github.com/Dao-AILab/flash-attention) · [FlashInfer](https://github.com/flashinfer-ai/flashinfer) |
| Recurrent attention | [FLA](https://github.com/fla-org/flash-linear-attention) · [FlashKDA](https://github.com/MoonshotAI/FlashKDA) · [FLA-NPU](https://github.com/flashserve/flash-linear-attention-npu) |
| Native and portable libraries | [FlashAttention NPU](https://github.com/MinghuasLab/flash-attention-npu) · [AITER](https://github.com/ROCm/aiter) · [HALOps](https://github.com/PaddlePaddle/HALOps) · [FlagGems](https://github.com/flagos-ai/FlagGems) · [FlagAttention](https://github.com/flagos-ai/FlagAttention) |
| Programming and compiler | [CUTLASS/CuTe](https://github.com/NVIDIA/cutlass) · [Triton](https://github.com/triton-lang/triton) · [Triton-Ascend](https://github.com/triton-lang/triton-ascend) · [TileLang](https://github.com/tile-ai/tilelang) · [PTO ISA](https://gitcode.com/cann/pto-isa) |

## 3. Read existing papers by technical question

These names point into existing canonical sections; they do not create new bibliography entries. The following two tables cover the 36 Attention & Sparse Kernels and 24 Fusion, Pipelines & Megakernels rows of the Nov 21 inventory, using each paper's existing mechanism description. Use these as problem-oriented reading routes; the complete paper descriptions and sources remain in the main Kernel topic.

### Attention kernel reading paths

| Question | Existing papers (36 total) |
|---|---|
| Exact attention dataflow, parallelism, reuse | FlashDecoding++, Hydragen, FastTree, LeanAttention, PAT, TyphoonMLA, PackInfer, FlashAttention-4, Reorienting the Vector Axis |
| Concurrent prefill/decode | POD-Attention |
| Sparse attention execution and routing | LightningMoBA (Accelerating Mixture of Block Attention), CompactAttention, FlashPrefill V2, FSA, BLASST, Accelerating Sparse Transformer Inference on GPU (STOF) |
| Indexer/scoring/selection | AttentionIndex, DTS, HISA, IndexCache, Guess-Verify-Refine, MISA, LiteTopK, DoSA |
| Low-precision or approximate attention execution | AscMLA, SageAttention, SageAttention2, TurboAttention, BitDecoding, TriAttention, FOSCAR |
| Composable attention programming | FlexAttention, Flashlight, SAS |
| Adjacent sparse matrix kernels (not token-selective attention) | GeneralSparse, SpInfer |

[Full paper records and sources](kernels-compilers.md#attention--sparse-kernels-36). Start with foundational FA/FA2/FA3 and FlashInfer in the [Kernel foundations](kernels-compilers.md#foundations). GeneralSparse and SpInfer concern SpMM/weight or matrix sparsity; their current placement is an adjacency issue, not evidence of a new attention algorithm. Defer canonical migration until the broader kernel catalog is reviewed.

### Fusion and execution-boundary reading paths

| Question | Existing papers (24 total) |
|---|---|
| Algebraic, epilogue and operator fusion | CODA, LightSeq, FuTransformer, ZipFusion |
| Larger fusion scope and dependency representation | ClusterFusion, FlashFuser, MonoMoE, MPK, Event Tensor, MeldKernel |
| Fine-grained scheduling, pipeline and overlap | PipeThreader, Twill, DynaFlow, KOSMOS, MegaOps, SubGPU |
| Graph/static execution and shape specialization | GraCE, LLMFolder, Taming Dynamic Diffusion LLM Inference through Virtual Static Execution, XY-Serve |
| Boundary selection, controls, alternative runtime and interference | One Megakernel is Not Enough, Understanding GPU Megakernels, BaseRT, MorphX |

[Full paper records and sources](kernels-compilers.md#fusion-pipelines--megakernels-24). Some entries concern general DNN execution, TTS, diffusion or training-heavy workloads; use their mechanism as context, not as proof of text-serving improvement.

Fusion can remove materialization, redundant reductions, launch/synchronization or idle gaps. It can also increase registers/UB pressure, reduce occupancy or create new dependencies. PDL and tile-level overlap can improve the critical path without combining launches. Do not infer a larger fusion scope is necessarily better.

### Cross-topic navigation

| If the question is about… | Canonical reading entry |
|---|---|
| Sparse token selection, quality and conditional compute | [Sparse Attention & Conditional Compute](moe-sparse-execution.md#sparse-attention--conditional-compute-27), e.g. MInference, Kascade, LServe |
| State residency, prefix reuse, sparse KV retrieval | [KV Cache & Context Memory](kv-cache-memory.md), e.g. Marconi, HYPIC and Sparse KV Retrieval |
| KV/recurrent-state precision and error | [Quantization & Compression](quantization-compression.md), KV Cache Quantization and Recurrent State Quantization |
| Attention parallelism and collective coordination | [Distributed Serving](distributed-serving.md#parallelism--scale-up-29), e.g. RingAttention, Context Parallelism, TPLA, SPLASH |
| Multi-token verification and recurrent-state semantics | [Decoding Acceleration](decoding-acceleration.md), Tree & Parallel Verification and Adaptive Speculation |
| Mixed prefill/decode scheduling | [Runtime & Scheduling](runtime-scheduling.md), with POD-Attention and XY-Serve as execution-layer links |

**Coverage gap:** the 36-row Attention & Sparse Kernels section has no clearly dedicated GDN/KDA kernel paper in its current mechanism summaries. Read [GDN](https://arxiv.org/abs/2412.06464) and [Kimi Linear/KDA](https://arxiv.org/abs/2510.26692) as architecture context, then the FLA/FlashKDA/FLA-NPU and engine implementations above. The recurrent-state quantization/cache topics are not substitutes for native operator coverage.

## 4. Recent PRs as mechanism probes (Nov 18–24)

Selected discussions checked against their upstream PR bodies and merge state on 2026-11-24. A merged PR is source integration, not necessarily an available package release or a universal performance gain.

| Upstream source | Mechanism and scope |
|---|---|
| [vLLM #69538](https://github.com/vllm-project/vllm/pull/69538) · open | Move sliding-window masking into V loads in Triton unified attention, reducing duplicate tile pressure at large head dimensions; A100 head-256 case, not a general FA optimization. |
| [vLLM #69218](https://github.com/vllm-project/vllm/pull/69218) · open | FA4 H512 on Hopper with 16-bit KV: split logical 128-token block into 64-token kernel blocks to select TMA path instead of cp.async. A cache/backend interface issue; no change to the model's semantics. |
| [vLLM #61428](https://github.com/vllm-project/vllm/pull/61428) · merged | AITER ROCm decode-only GDN: conv1d + delta rule + gated RMSNorm into one launch, with required library API version and unfused fallback. |
| [vLLM #69006](https://github.com/vllm-project/vllm/pull/69006) · open | Proposed FlashInfer DCP A2A + LSE reduction for MLA; depends on FlashInfer release and NCCL symmetric-memory workspace. |
| [Ascend #22573](https://github.com/vllm-project/vllm-ascend/pull/22573) · open | SFA Q projection: fold transposes into npu_transpose_batchmatmul so output is token-major contiguous, with dtype/dimension gates and bmm fallback. |
| [Ascend #22235](https://github.com/vllm-project/vllm-ascend/pull/22235) · merged · [CANN #15456](https://gitcode.com/cann/ops-transformer/pull/15456) | MsaIndexScore computes ordered block TopK after forced init/local block masking; MiniMax-M3 A5 consumes it directly, gated by aligned topk and hardware capability; fallback remains. |
| [Ascend #22720](https://github.com/vllm-project/vllm-ascend/pull/22720) · merged | A5 FP8 C8 indexer V2 metadata prepared once per compatible group; refresh values each build while preserving graph addresses and isolate draft buffers. Metadata reuse is not stale-value reuse. |
| [Ascend #22086](https://github.com/vllm-project/vllm-ascend/pull/22086) · merged | QSA preparation: fuse position gather/norm/rotation, compressed indexer-key preparation and cache writes, preserve raw-ring read-before-write; native V2 input preparation removes launches/intermediates. |
| [Ascend #21498](https://github.com/vllm-project/vllm-ascend/pull/21498) · merged | Layer-level BF16 GEMM+ReduceScatter for SP; owns the post-attention collective and returns the same shard on native and fallback paths. Model, hardware, token and inner-dimension gates; not the separate FX pass itself. |
| [Ascend issue #22898](https://github.com/vllm-project/vllm-ascend/issues/22898) · issue | SparseFlashMla standalone 910B3 gather/Cube pipeline proposal; a diagnostic signal, not a merged fix. |

**Keep following:** [vLLM fusion tracker](https://github.com/vllm-project/vllm/issues/36066), [SGLang monokernel RFC](https://github.com/sgl-project/sglang/issues/43949), [CANN community](https://gitcode.com/cann/community), and the [community daily-report website](https://lab.sage.org.ai/auto-research-report-website/) for merged-PR discovery. Add only cases that clarify a mechanism or a meaningful implementation boundary; replace superseded cases rather than accumulating a chronological feed.

For any implementation, ask: what workload/shape/precision activates it; what physical launch, copy, dependency or compute cost disappears; how are outputs/state preserved; and does the gain survive an engine-level comparison? Pin the software/hardware pair before measuring.
