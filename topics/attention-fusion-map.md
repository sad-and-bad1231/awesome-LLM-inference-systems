# Attention & Kernel Fusion — engineering reading map

[← Kernel topic](kernels-compilers.md) · [← Topics](README.md) · [Communities](../communities/README.md)

A source map for the five principal inference ecosystems. Follow **model semantics → backend → library/custom op → physical kernel → serving step**, then read the relevant optimization. Code links pin the inspected GitHub snapshots where practical; moving docs and GitCode references are current source entrances, not a guarantee of a release or local hardware support. Source review: 2026-11-24.

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

| Ecosystem | Backend contract | Physical operator layer | Fusion / execution boundary |
|---|---|---|---|
| vLLM | Selector + backend/metadata classes | FlashAttention, FlashInfer, Triton, AITER, native extensions | Inductor pattern passes, graph replay, library fused ops |
| vLLM-Ascend | Platform plugin + Ascend metadata/implementations | TorchNPU → CANN ACLNN, plugin Ascend C/Triton custom ops | Native fused ops, FX passes, Npugraph_ex, ACLGraph/SuperKernel |
| SGLang | Registry + forward metadata; phase-specific choices | FlashInfer, FlashAttention, Triton, SGL kernels and NPU extension | Native fusion, model-specific NVIDIA Mega/AMD Mono plugins |
| DeepInfer | Model-specific sparse-attention entry points | FlashMLA, DeepGEMM, DeepEP, DeepSelect, TileKernels | Direct dataflow/weight-layout co-design and native fused library calls |
| CANN | Operator and runtime platform, not a serving engine | Ascend C, ACLNN, CATLASS, device libraries | AutoFuse codegen, SuperKernel binary fusion, explicit PyPTO/CANNBot-DSL |

### vLLM

**Read in order:** [backend guide](https://docs.vllm.ai/en/latest/design/attention_backends/) → [selector.py](https://github.com/vllm-project/vllm/blob/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/v1/attention/selector.py) → [backend.py](https://github.com/vllm-project/vllm/blob/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/v1/attention/backend.py) → [backend implementations](https://github.com/vllm-project/vllm/tree/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/v1/attention/backends).

- The selector builds a compatibility request from head size, compute/KV dtype, cache block size and model/serving features; the platform resolves the backend. The backend interface owns the implementation class, metadata builder and supported kernel block sizes. A logical cache block need not equal a kernel tile. Inspect [FlashAttention](https://github.com/vllm-project/vllm/blob/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/v1/attention/backends/flash_attn.py) and [FlashInfer](https://github.com/vllm-project/vllm/blob/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/v1/attention/backends/flashinfer.py) as concrete implementations; MLA has a [separate backend family](https://github.com/vllm-project/vllm/tree/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/v1/attention/backends/mla) and a prefill selector.
- [Native operators](https://github.com/vllm-project/vllm/tree/b09bc99f40951f8984a6c64cecfed47036bc6016/csrc) and [Python custom-op bindings](https://github.com/vllm-project/vllm/blob/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/_custom_ops.py) bridge model code to C++/CUDA. The [vLLM FlashAttention fork](https://github.com/vllm-project/flash-attention) is a separate dependency, not interchangeable with every release of Dao-AILab's library.
- [Fusion guide](https://docs.vllm.ai/en/latest/design/fusions/) · [QK Norm + RoPE pass](https://github.com/vllm-project/vllm/blob/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/compilation/passes/fusion/qk_norm_rope_fusion.py) · [pass directory](https://github.com/vllm-project/vllm/tree/b09bc99f40951f8984a6c64cecfed47036bc6016/vllm/compilation/passes/fusion). The QK pass matches split/reshape/RMSNorm/rotation and substitutes a fused native op; the inspected code restricts head dimensions to supported dispatch choices. Other patterns include AllReduce+RMSNorm, Attention+Quant, RoPE+KV write and SiLU+Mul+Quant. Check optimization level, backend, shape, precision and full-graph requirements, not just pass existence.
- Follow [fusion tracking issue #36066](https://github.com/vllm-project/vllm/issues/36066), [releases](https://github.com/vllm-project/vllm/releases), and the [PR cases below](#4-recent-prs-as-mechanism-probes-nov-1824).

### vLLM-Ascend

**Read in order:** [platform selection](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/platform.py) → [attention directory](https://github.com/vllm-project/vllm-ascend/tree/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/attention) → [custom operators](https://github.com/vllm-project/vllm-ascend/tree/6301aaf2196dfeb107b48159d89c9703c0667320/csrc) → vendor implementation. This plugin has its own compatibility decisions and metadata, not merely a GPU backend renamed NPU.

| Path | Concrete implementation / question |
|---|---|
| Dense MHA/GQA | [attention_v1.py](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/attention/attention_v1.py): metadata builder, FIA/FIA-v2, paged-attention and encoder paths. The inspected code calls TorchNPU fused infer attention operators; determine the phase and graph path before measuring. |
| MLA | [mla_v1.py](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/attention/mla_v1.py): prefill/decode metadata, KV RMSNorm/RoPE/cache, weight packing and native MLA prolog. MLAPO means preprocessing fusion, not generic model parallelism. |
| DSA / sparse | [sfa_v1.py](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/attention/sfa_v1.py) · [dsa_v41.py](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/attention/dsa_v41.py): index metadata, Q projection, sparse gather/attention and dtype/layout-specific paths. SFA calls both TorchNPU and plugin custom ops depending on path. |
| Recurrent GDN/KDA | [gdn.py](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/attention/gdn.py) · [kda.py](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/ops/kda.py) · [ChunkKdaFwd design](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/csrc/attention/chunk_kda_fwd/docs/design.md). GDN has native chunk/recurrent paths with eligibility checks and Triton fallback. The KDA design stages gate accumulation, preparation, state update and finalization; a single public op may submit multiple physical kernels. |
| Training/inference consistency | [FA3 guide](https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/flash_attention.html): distinct from default FIA; use the documented conditions rather than assuming FA3 universally replaces FIA. |
| Plugin-native fusion | [fused scatter/copy + SFA](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/csrc/attention/fused_scatter_copy_sparse_flash_attention/README.md): for GLM sparse KV offload on Atlas A2/A3, combines DRAM-to-HBM missing-KV movement and attention with device-side path selection. Not a generic cache-offload or A5 implementation. |

**Graph and layer fusion:** [GraphFusionPassManager](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/compilation/graph_fusion_pass_manager.py) selects configured Norm+Quant, QKNorm+RoPE and other passes; [MatmulReduceScatter pass](https://github.com/vllm-project/vllm-ascend/blob/6301aaf2196dfeb107b48159d89c9703c0667320/vllm_ascend/compilation/passes/mm_reduce_scatter_fusion_pass.py) matches GEMM/optional padding followed by a compatible ReduceScatter and replaces it with a native MMRS operator. Separately, the [graph-mode guide](https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/graph_mode.html) distinguishes FX optimization (Npugraph_ex), ACLGraph replay, optional static-kernel compilation and SuperKernel binary fusion during capture. Static kernel is disabled by default in that guide; SuperKernel depends on it. Profile actual coverage, not just the enabled flag.

Use [additional configuration](https://docs.vllm.ai/projects/ascend/en/main/user_guide/configuration/additional_config.html), [feature matrix](https://docs.vllm.ai/projects/ascend/en/main/user_guide/support_matrix/feature_matrix.html), and [releases](https://github.com/vllm-project/vllm-ascend/releases) for exact model/device/toolkit combinations. For an older environment, read its release-specific docs (e.g. [v0.23 graph mode](https://docs.vllm.ai/projects/ascend/en/v0.23.0/user_guide/feature_guide/graph_mode.html)).

### SGLang

**Read in order:** [attention backend guide](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/docs/docs/advanced_features/attention_backend.mdx) → [registry](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/python/sglang/srt/layers/attention/attention_registry.py) → [base contract](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/python/sglang/srt/layers/attention/base_attn_backend.py) → [implementations](https://github.com/sgl-project/sglang/tree/72c9f47614978e7e5d031636bef734d46f10c249/python/sglang/srt/layers/attention).

- Registry factories select a backend according to engine/model configuration. The guide exposes independent prefill/decode backend choices (experimental hybrid attention), with compatibility constraints for speculative verification and paged KV. The base class separates forward metadata outside and inside graph capture. Read FlashInfer/FlashAttention/FlashMLA and DSA implementations in the attention directory.
- [GDN backend](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/python/sglang/srt/layers/attention/linear/gdn_backend.py) has a kernel dispatcher for decode, extend and verify, with separate Triton/FlashInfer and hardware-specific choices. [Linear kernel implementations](https://github.com/sgl-project/sglang/tree/72c9f47614978e7e5d031636bef734d46f10c249/python/sglang/srt/layers/attention/linear/kernels) include GDN and KDA variants. Do not conflate recurrent-state kernels with softmax attention.
- [SGLang GPU kernel source](https://github.com/sgl-project/sglang/tree/72c9f47614978e7e5d031636bef734d46f10c249/python/sglang/kernels) and [SGL Kernel NPU](https://github.com/sgl-project/sgl-kernel-npu) expose operator-level implementation. The [NPU operator guide](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/docs/docs/hardware-platforms/ascend-npus/development/operator_development.mdx) explains Ascend C host/device sources registered through PyTorch and Triton Python kernels. Its [performance guide](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/docs/docs/hardware-platforms/ascend-npus/development/operator_performance_optimizing.mdx) provides the next entry for tuning. SGL Kernel NPU's DeepEP-Ascend component has its own A2/A3/A5 CI matrix, distinct from DeepSeek's 950-oriented library.
- **Beyond individual operators:** [NVIDIA Mega](https://github.com/sgl-project/sgl-nvidia-mega) runs selected small-batch decode/verify as fused kernel chains communicating via mailboxes and programmatic dependent launch (PDL); the [V4.1 model page](https://github.com/sgl-project/sgl-nvidia-mega/blob/main/docs/models/deepseek_v41.md) exposes slot-specific row limits, GEMM/collective/norm boundaries, and stock fallback. [AMD Mono](https://github.com/sgl-project/sgl-amd-mono) instead uses persistent layer kernels, often one or two launches; exact coverage varies by model and row count. Both are experimental plugins. [V4 Mega attention backend](https://github.com/sgl-project/sglang/blob/72c9f47614978e7e5d031636bef734d46f10c249/python/sglang/srt/layers/attention/deepseek_v4_mega_backend.py) separately calls FlashMLA mega prefill/decode: do not assume the whole step is one kernel.

Follow [Monokernel RFC #43949](https://github.com/sgl-project/sglang/issues/43949), [Low-Latency Mode](https://www.lmsys.org/blog/2026-10-18-sglang-low-latency-mode/), [Muse Spark](https://www.lmsys.org/blog/2026-11-05-muse-spark-open-ultrafast/), [Neuron backend](https://www.lmsys.org/blog/2026-11-12-sglang-neuron-v0.1.0), [ERNIE 5.5 Flash](https://www.lmsys.org/blog/2026-11-23-ernie55-flash-low-latency), and [releases](https://github.com/sgl-project/sglang/releases). Model/hardware-specific cases are more useful than a generic fusion flag comparison.

### DeepInfer and DeepSeek's kernel stack

**Read in order:** [DeepInfer README](https://github.com/deepseek-ai/DeepInfer/blob/a679bb86ce36e883a98a97733492b686e5b9a08e/README.md) → [attention_backend.py](https://github.com/deepseek-ai/DeepInfer/blob/a679bb86ce36e883a98a97733492b686e5b9a08e/deepinfer/model_executor/layers/attention_backend.py) → [FlashMLA](https://github.com/deepseek-ai/FlashMLA) → [deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/a679bb86ce36e883a98a97733492b686e5b9a08e/doc/inference_deployment_qa.md). Unlike a general-purpose backend registry, this open release directly specializes V4.1-Flash. It supports SM100 and Ascend 950/CANN 9.2 offline inference; KV storage, full E/P/D service and DP-replica load balancing are not included.

The attention adapter has two main paths: BF16 sparse varlen prefill with selected KV indices, and sparse decode with paged quantized KV and schedule metadata. It pads unsupported Q head counts to 64/128 and slices the result back. An optional fused path calls FlashMLA's norm/RoPE/attention/RoPE/FP8-cast interface instead of materializing each preparation/epilogue. It requires pre-permuted projection weights and returns quantized output/scales. **FlashMLA documents this particular fused path as CUDA-only**, although its standalone sparse attention kernels support Ascend 950. The public engine must not be treated as proof of every fusion on both platforms.

| Library | Engineering reading |
|---|---|
| [FlashMLA](https://github.com/deepseek-ai/FlashMLA) | [Ascend sparse prefill deep dive](https://github.com/deepseek-ai/FlashMLA/blob/main/docs/20260930-ascend-prefill-deep-dive.md): online softmax with skip-rescale, sparse gather, Q-head/core work partition and Cube/Vector accumulator placement. This is a hardware-specific operator design, not a universal engine speedup. The September 30 release changed KV format and dropped older Hopper/model support; use [legacy commit](https://github.com/deepseek-ai/FlashMLA/tree/ba89a3466e9470ad08ab39738d4e7bb66989e1e7) for earlier formats. |
| [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) · [Ascend port](https://github.com/deepseek-ai/DeepGEMM-Ascend) | BF16/FP8/FP4 matrix kernels, MQA logits and MegaMoE. Ascend port abstracts MAD/layout and uses sparse loading/coroutine pipelines; scale-factor representation differs from CUDA. Validated on 950/CANN 9.2, not 910B2. |
| [DeepEP](https://github.com/deepseek-ai/DeepEP) · [Ascend port](https://github.com/deepseek-ai/DeepEP-Ascend) | EP token dispatch/combine and communication/computation coordination. Backend, interconnect and topology matter. |
| [DeepSelect](https://github.com/deepseek-ai/DeepSelect) · [TileKernels](https://github.com/deepseek-ai/TileKernels) | Indexer/sampler TopK and reusable MoE routing, quantization, Engram and mHC operators. TileKernels uses TileLang with distinct CUDA and 950/CANN 9.2 paths. |
| [DeepJIT](https://github.com/deepseek-ai/DeepJIT) | Compilation, loading, caching and launch infrastructure behind native extensions, not a serving scheduler. |

Use this stack to study co-design: model's sparse index and weight layouts determine native kernels; parallelism determines GEMM shapes and collective costs. The deployment Q&A explains production choices separately from public executable coverage. [DeepSeek profile](../organizations/DeepSeek.md) owns the wider company/model chronology.

### CANN / Ascend native ecosystem

**Read in order:** [Ascend C learning path](https://www.hiascend.com/en-sg/document/detail/en/CANNCommunityEdition/910/programug/Ascendcopdevg/docs/en/guide/getting_started/ascend_c_overview_and_learning_path.md) → [asc-devkit](https://gitcode.com/cann/asc-devkit) → [ops-transformer](https://gitcode.com/cann/ops-transformer) → [CATLASS](https://gitcode.com/cann/catlass) → integration and profiling.

| Layer | Source / purpose |
|---|---|
| Device programming | [Ascend C guide](https://asc.gitcode.com/guide/) · [operator implementation guide](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/programug/Ascendcopdevg/docs/en/guide/operator_practice/simd_operator_impl/overview.md): host tiling/validation and device computation, Cube/Vector units, on-chip buffers, DMA, synchronization. |
| Native attention | [FusedInferAttentionScore](https://gitcode.com/cann/ops-transformer/tree/master/attention/fused_infer_attention_score) · [SparseFlashAttention](https://gitcode.com/cann/ops-transformer/tree/master/attention/sparse_flash_attention) · [quantized SFA kernel directory](https://gitcode.com/cann/ops-transformer/tree/master/attention/kv_quant_sparse_flash_attention/op_kernel). Follow ACLNN API → host tiling → device kernel and tests. TorchNPU is the framework binding ([source](https://github.com/Ascend/pytorch)), not the implementation of every device op. |
| Matrix templates | [CATLASS basic Matmul](https://gitcode.com/cann/catlass/tree/master/examples/00_basic_matmul) · [documentation](https://gitcode.com/cann/catlass/tree/master/docs/zh): learn reusable matrix scheduling before custom fused epilogues or attention. |
| Automatic fusion | [graph-autofusion](https://gitcode.com/cann/graph-autofusion) separates SuperKernel (compiled binary/task fusion) from [AutoFuse](https://gitcode.com/cann/graph-autofusion/blob/master/autofuse/README_en.md) (codegen/JIT). SuperKernel can reduce task scheduling gaps; do not assume it removes all intermediate memory traffic. See the vLLM-Ascend graph integration above. |
| Explicit larger operators | [PyPTO examples](https://gitcode.com/cann/pypto/blob/master/examples/README_en.md) · [PyPTO-Gym](https://gitcode.com/cann/pypto-gym/blob/master/README.md) · [CANNBot-DSL](https://cannbot-dsl.gitcode.com/getting-started/) · [DSL source](https://gitcode.com/cann/cannbot-dsl). These are programming/optimization paths for constructing operator dataflow, not aliases for automatic binary fusion. |
| Model integration | [CANN inference recipes](https://gitcode.com/cann/cann-recipes-infer) · [PyPTO integration examples](https://gitcode.com/cann/cann-recipes-infer/blob/master/ops/pypto/README.md): bridge native ops and model-specific execution; check hardware and framework versions. |
| Operator agents | [CANNBot](https://gitcode.com/cann/cannbot), [skills](https://gitcode.com/cann/cannbot-skills), [CANNBench](https://cannbench.com/leaderboard): distinct harness, reusable engineering skills and real-device evaluation. Compare with the [kernel-agent reading route](kernels-compilers.md#kernel-agents-goal-only-vs-kda-vs-compiler-agent-co-design). |

**Community discussions:** [CANN learning hub](https://gitcode.com/cann/cann-learning-hub/tree/master) indexes native tutorials and production cases, including AutoFuse/TorchInductor, SuperKernel and DSA. [Meetup index](https://gitcode.com/cann/community/tree/master/events/meetup) and [Nov 10 event](https://cann.csdn.net/activelist) describe DeepSeek-V4.1 L20/L24 indexer/attention MegaKernel work with CANNBot-DSL; [Nov 21 meetup recap](https://gitcode.csdn.net/6b03a34840858c2d881d4289.html) separates DSL, CANNBench, MegaKernel and agent experience. These confirm community work and its direction; they do not establish a released, reproducible model-level implementation. The public CANNBot-DSL project and samples are independently available; the exact three Nov 10 kernels and integration commit were not established in this audit. Also follow [FlashAttention NPU discussion #292](https://gitcode.com/org/cann/discussions/292) and [Nov 19 GDN/KDA session](https://cann.csdn.net/6afd551340858c2d881c625e.html).

**Version discipline:** CANN master is not the installed toolkit. The [PyPTO 9.1 README](https://gitcode.com/cann/pypto/blob/9.1.0/README.md) explicitly recommends matching tags. [CANN 9.2 release notice](https://www.hiascend.com/productbulletins/detail/830) focuses on Ascend 950. Do not transfer 950/9.2 measurements or source compatibility to 910B2/9.1. GitCode source-directory/README access was partial in this review; links above distinguish source entrances and documented mechanisms from a line-by-line native-kernel audit.

### Shared libraries and programming models

| Source | Read for |
|---|---|
| [FlashAttention](https://github.com/Dao-AILab/flash-attention) | FA1/2 exact tiling/work partition, FA3 Hopper async/FP8, FA4 CuTe DSL on Hopper/Blackwell; read supported dtype/mask/shape. |
| [FlashInfer](https://github.com/flashinfer-ai/flashinfer) · [docs](https://docs.flashinfer.ai/) | Serving primitives: paged/ragged prefill/decode, cascade/prefix, POD, MLA, GEMM/MoE and backend dispatch. It is a library with multiple implementations, not an engine. |
| [FLA](https://github.com/fla-org/flash-linear-attention) · [FlashKDA](https://github.com/MoonshotAI/FlashKDA) · [FLA-NPU](https://github.com/flashserve/flash-linear-attention-npu) | Recurrent linear attention: chunked prefill, decode-state layout/update, rollback and fusion. FLA-NPU is a distinct Tianjin University-led project. |
| [FlashAttention NPU](https://github.com/MinghuasLab/flash-attention-npu) · [AITER](https://github.com/ROCm/aiter) · [HALOps](https://github.com/PaddlePaddle/HALOps) | Native platform/library examples; compare actual hardware target, implementation and integration rather than assuming backend parity. |
| [Triton](https://github.com/triton-lang/triton) · [CUTLASS/CuTe](https://github.com/NVIDIA/cutlass) · [TileLang](https://github.com/tile-ai/tilelang) | Different abstractions for tile-level computation/layout and scheduling. [TileLang pipeline guide](https://github.com/tile-ai/tilelang/blob/92458c19c378934889711ab4796cef8aaa535f5a/docs/programming_guides/software_pipeline.md) distinguishes inferred stages from explicit stage/order constraints. |
| [TileLang Ascend examples](https://github.com/tile-ai/tilelang/blob/92458c19c378934889711ab4796cef8aaa535f5a/examples/ascend/README.md) · [FA example](https://github.com/tile-ai/tilelang/blob/92458c19c378934889711ab4796cef8aaa535f5a/examples/ascend/flash_attention/README.md) | Direct GEMM, split-K, MHA/GQA and manual/automatic pipeline examples on Ascend 950. The documented FA example fixes head_dim 128, BF16 and aligned tiles and has no causal/varlen mask; it is an instructional kernel, not a general serving replacement. |

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
