# Attention & Kernel Fusion — engineering reading map

[← Topics](README.md) · [Kernel papers](kernels-compilers.md) · [Communities](../communities/README.md)

**Start with a model and a serving step, not with a kernel name.** This cross-index connects the existing bibliography to upstream implementations and recent engineering changes. A subtopic reading path within Kernels & Compilers. Source snapshot: 2026-11-24.

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

| Ecosystem | Read in this order | What to investigate |
|---|---|---|
| vLLM | [Attention backend matrix](https://docs.vllm.ai/en/latest/design/attention_backends/) → [backend code](https://github.com/vllm-project/vllm/tree/main/vllm/v1/attention) → [Fusion passes](https://docs.vllm.ai/en/latest/design/fusions/) → [vLLM FlashAttention fork](https://github.com/vllm-project/flash-attention) | Backend compatibility/priority, metadata and dispatch, compile-time pattern matching; default versus explicitly enabled passes. |
| vLLM-Ascend | [Attention](https://github.com/vllm-project/vllm-ascend/tree/main/vllm_ascend/attention) → [custom ops](https://github.com/vllm-project/vllm-ascend/tree/main/csrc) → [additional config](https://docs.vllm.ai/projects/ascend/en/main/user_guide/configuration/additional_config.html) → [FA3 feature](https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/flash_attention.html) | FIA/MLA/SFA, graph compatibility, layout and CANN dispatch; FA3 also addresses training/inference consistency. MLAPO means MLA preprocessing fusion, not generic model parallelism. |
| CANN | [ops-transformer](https://gitcode.com/cann/ops-transformer) · [SFA source](https://gitcode.com/cann/ops-transformer/tree/master/attention/sparse_flash_attention) · [CATLASS](https://gitcode.com/cann/catlass/tree/master) · [TorchNPU](https://github.com/Ascend/pytorch) | Native operator and template implementation, host/device tiling, Cube/Vector pipelines, framework dispatch. Match the actual device and toolkit tag. |
| SGLang | [Low-Latency Mode](https://www.lmsys.org/blog/2026-10-18-sglang-low-latency-mode/) → [NVIDIA Mega](https://github.com/sgl-project/sgl-nvidia-mega) · [AMD Mono](https://github.com/sgl-project/sgl-amd-mono) → [integration RFC](https://github.com/sgl-project/sglang/issues/43949) | Model-specific small-batch decode/verify, PDL, mailboxes, persistent layers, collectives and fallback to standard execution. Both packages are experimental; NVIDIA Mega uses chains of fused kernels, not necessarily one launch. |
| SGLang cases | [Muse Spark Open](https://www.lmsys.org/blog/2026-11-05-muse-spark-open-ultrafast/) · [Neuron](https://www.lmsys.org/blog/2026-11-12-sglang-neuron-v0.1.0) · [ERNIE 5.5 Flash](https://www.lmsys.org/blog/2026-11-23-ernie55-flash-low-latency) | Model dataflow changes, hardware-specific execution and speculation interaction; read the benchmark settings before comparing. |
| Attention libraries | [FlashAttention](https://github.com/Dao-AILab/flash-attention) · [FlashInfer](https://github.com/flashinfer-ai/flashinfer) · [FlashMLA](https://github.com/deepseek-ai/FlashMLA) · [DeepSelect](https://github.com/deepseek-ai/DeepSelect) | Exact attention implementations, serving primitives and planning, native sparse MLA, specialized Top-K. Current FlashMLA has a breaking format/model/hardware change (Sept 30); older models require a pinned version. |
| Recurrent kernels | [FLA](https://github.com/fla-org/flash-linear-attention) · [FlashKDA](https://github.com/MoonshotAI/FlashKDA) · [FLA-NPU](https://github.com/flashserve/flash-linear-attention-npu) | Chunked prefill, recurrent decode, state layout and fusion; FLA-NPU is Tianjin University-led, with GDN and KDA kernels. |
| Other native kernels | [FlashAttention NPU](https://github.com/MinghuasLab/flash-attention-npu) · [SGL Kernel NPU](https://github.com/sgl-project/sgl-kernel-npu) · [AITER](https://github.com/ROCm/aiter) · [HALOps](https://github.com/PaddlePaddle/HALOps) | Distinguish independent projects, engine-owned kernels and vendor libraries; CUDA/ROCm/Ascend implementations are not interchangeable. |

For kernel programming, see the [DSL/compiler and automation sections](kernels-compilers.md) and [kernel agents](kernels-compilers.md#kernel-agents-goal-only-vs-kda-vs-compiler-agent-co-design). Company-level paths: [DeepSeek](../organizations/DeepSeek.md), [Huawei](../organizations/Huawei.md), [Moonshot](../organizations/Moonshot-Kimi.md), [Baidu](../organizations/Baidu.md), [AMD](../organizations/AMD.md).

## 3. Read existing papers by technical question

These names point into existing canonical sections; they do not create new bibliography entries. The following two tables cover the 36 Attention & Sparse Kernels and 24 Fusion, Pipelines & Megakernels rows of the Nov 21 inventory, using each paper's existing mechanism description. This is a navigation audit, not a new full-text admission review.

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
| Graph/static execution and shape specialization | GraCE, LLMFolder, Prism (virtual static execution), XY-Serve |
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

**Coverage gap:** the 36-row Attention & Sparse Kernels section has no clearly dedicated GDN/KDA kernel paper in its current mechanism summaries. The recurrent-state quantization/cache topics are not substitutes for native recurrent operator coverage. Prioritize first-party FLA/FlashKDA/FLA-NPU and upstream recurrent kernel integrations; separately verify candidate research papers before adding them to the canonical inventory.

## 4. Recent PRs as mechanism probes (Nov 18–24)

| Question | Upstream example |
|---|---|
| Can layout and mask handling improve occupancy or avoid copies? | [vLLM #69538](https://github.com/vllm-project/vllm/pull/69538) V-load window masking; [#69218](https://github.com/vllm-project/vllm/pull/69218) FA4 kernel-block alignment; [Ascend #22573](https://github.com/vllm-project/vllm-ascend/pull/22573) SFA Q projection + layout. |
| Can a sparse indexer avoid intermediate work? | [Ascend #22235](https://github.com/vllm-project/vllm-ascend/pull/22235) MsaIndexScore + Block Top-K; [#22720](https://github.com/vllm-project/vllm-ascend/pull/22720) V2 FP8 indexer metadata reuse; [#22086](https://github.com/vllm-project/vllm-ascend/pull/22086) QSA preparation fusion. |
| Can recurrent decode fuse its state-update chain? | [vLLM #61428](https://github.com/vllm-project/vllm/pull/61428) AITER conv1d + delta rule + gated norm, decode-only. |
| Can communication or preprocessing disappear from the critical path? | [Ascend #21498](https://github.com/vllm-project/vllm-ascend/pull/21498) gated BF16 MM + ReduceScatter; [vLLM #69006](https://github.com/vllm-project/vllm/pull/69006) proposed FlashInfer DCP A2A + LSE merge. |
| Is native KV gather blocking Cube computation? | [Ascend issue #22898](https://github.com/vllm-project/vllm-ascend/issues/22898), 910B3 standalone SparseFlashMla profiling and proposed cross-core-group parallelism; proposal, not a validated speedup. |

The [community daily-report website](https://lab.sage.org.ai/auto-research-report-website/) and its [published index](https://github.com/intellistream/auto-research-report-website/blob/main/public/word-reports/flow-index.json) provide merged-PR discovery; open PRs and issues are research signals, not released features.

For each new source, record the model/operator semantics, workload shape, hardware/version, actual execution path, bottleneck removed, correctness contract, and evaluation level (operator, step or serving). The same optimization can behave differently under speculation, large batches or long context. Keep claims and original evidence in their canonical records and link them here instead of adding a dated feed.
