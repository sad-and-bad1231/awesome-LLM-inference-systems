# DeepSeek

**Model architecture ↔ inference kernel ↔ expert communication.** The focus is on how DeepSeek's public work changes *inference computation, KV state, sparsity, MoE dispatch and deployment*. Model-quality and RL results appear only as context; they are not misrepresented as serving-system papers.

[← Home](../README.md) · [Serving systems](../topics/serving-systems.md)

## Official model-family crosswalk (updated 2026-11-12)

**First-party catalog:** [DeepSeek official research/releases](https://www.deepseek.com/en/news/) and [API changelog](https://api-docs.deepseek.com/updates/). Model weights, API aliases and experimental releases are not interchangeable.

| Official model or family | Lifecycle / inference significance | Source |
|---|---|---|
| DeepSeek-V2 / V2.5 | Historical MLA + DeepSeekMoE architecture and serving-state foundation | [V2 code/report](https://github.com/deepseek-ai/DeepSeek-V2) |
| DeepSeek-V3 / V3.1 / V3.1-Terminus | MLA/MoE + MTP lineage; distinct model revisions rather than new serving frameworks | [V3 official code](https://github.com/deepseek-ai/DeepSeek-V3) · [API updates](https://api-docs.deepseek.com/updates/) |
| DeepSeek-R1 / R1-0528 | Reasoning/long-output *workload* evolution; do not count as kernel papers | [R1 official repository](https://github.com/deepseek-ai/DeepSeek-R1) |
| DeepSeek-V3.2-Exp / V3.2 / V3.2-Speciale | DSA sparse indexer and MLA serving kernel demand; Speciale is a model variant | [V3.2 code](https://github.com/deepseek-ai/DeepSeek-V3.2) · [official news](https://www.deepseek.com/en/news/) |
| DeepSeek-V4 Preview / V4-Flash / V4-Pro | 2026 V4 generation, long-context and high-throughput model releases; model availability and alias state require release-specific documentation | [Official April 2026 V4 preview release](https://www.deepseek.com/en/news/) · [API changelog](https://api-docs.deepseek.com/updates/) |
| DeepSeek-V4-Flash-Vision-Exp | August 2026 experimental visual model; now **retired** from API, alias maps to V4.1 Flash | [API changelog](https://api-docs.deepseek.com/updates/) |
| DeepSeek-V4.1-Flash / V4.1-Flash-1017 | 552B causal encoder–decoder asymmetric MoE (8B active input / 16B output), native vision and lower KV footprint. **1017 is the Oct 17 model revision**, not a distinct V4.1 architecture or new inference engine. `deepseek-flash` API alias points to the updated model; **1017 open weights** are available. | [Sep 10 architecture announcement](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) · [Oct 17 API revision](https://api-docs.deepseek.com/updates/) · [official 1017 weights](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) |

**DeepSeek V4.1 Pro watch (checked 2026-11-12):** no first-party V4.1-Pro model card, weight release or API route is confirmed in the checked [official news](https://www.deepseek.com/en/news/) and [API changelog](https://api-docs.deepseek.com/updates/). The changelog confirms that `deepseek-flash` serves V4.1-Flash-1017, while the older `deepseek-v4-pro` service remains a separate V4 Pro endpoint. **V4 Pro is not V4.1 Pro**; do not infer a future Pro architecture from Flash.

**Systems map:** model dataflow → [DeepInfer](https://github.com/deepseek-ai/DeepInfer) (public offline path) → [TileKernels](https://github.com/deepseek-ai/TileKernels) / independently maintained [TileLang](https://github.com/tile-ai/tilelang) → [FlashMLA](https://github.com/deepseek-ai/FlashMLA), [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM), [DeepEP](https://github.com/deepseek-ai/DeepEP). Do not infer that commercial API models, open-weight checkpoints and open-sourced runtime features have identical deployment scope.

## Architecture papers and official artifacts

| Work | Status | Inference-system contribution / boundary | Primary source |
|---|---|---|---|
| **DeepSeek-V2** (2024) | Technical report | Multi-head Latent Attention (MLA) compresses KV state; DeepSeekMoE makes sparse-expert execution a central serving concern. | [Paper](https://arxiv.org/abs/2405.04434) · [Official repo](https://github.com/deepseek-ai/DeepSeek-V2) |
| **DeepSeek-V3** (2024) | Technical report | Production-scale MLA/MoE design, Multi-Token Prediction and engineering tradeoffs; FP8/DualPipe details primarily concern **training**. | [Paper](https://arxiv.org/abs/2412.19437) · [Official repo](https://github.com/deepseek-ai/DeepSeek-V3) |
| **DeepSeek-V3.2-Exp** (2025) | Official experimental release | Introduces DeepSeek Sparse Attention (DSA), motivating indexer TopK and sparse MLA kernel implementations. Experimental release, not a conference paper. | [Official repo](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) |
| **DeepSeek-V3.2** (2025) | Technical report | DeepSeek Sparse Attention: long-context computation is reduced through learned fine-grained sparse selection. Discussion of RL and agent performance is outside this page's systems focus. | [Paper](https://arxiv.org/abs/2512.02556) · [Official repo](https://github.com/deepseek-ai/DeepSeek-V3.2) |
| **DeepSeek-V4.1-Flash / -1017** (2026) | Official model release + Oct 17 checkpoint revision | Asymmetric causal encoder–decoder MoE (552B total; 8B/16B activated in input/output phases), designed to reduce KV-storage costs. **1017** further targets shorter task runs and agent-harness workflows; its self-feedback RL is a **training claim**, not RSI of a deployed inference engine. No independently controlled throughput improvement is established by the model update alone. | [Architecture](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) · [1017 release](https://api-docs.deepseek.com/news/news261017/) · [open weights](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) |

## Execution and communication libraries

| Work | Type | Technical role | Official source |
|---|---|---|---|
| **FlashMLA** | CUDA / Ascend attention kernels | Current code targets V4.1 sparse prefill and FP8/FP4 KV-cache decoding. The Ascend sparse kernels target **Ascend 950 / CANN 9.2.0+**. The 2026-09-30 release removes Hopper and earlier V3/V3.2/V4.0 model-format support and changes the FP8/FP4 KV layout; pin a compatible commit for older models. | [Repository and compatibility notice](https://github.com/deepseek-ai/FlashMLA) |
| **DeepGEMM** | CUDA kernel library | FP8/FP4/BF16 GEMM, fused MoE operations and scoring primitives; GPU implementation. | [Repository](https://github.com/deepseek-ai/DeepGEMM) |
| **DeepGEMM-Ascend** | Ascend kernel backend | DeepGEMM-API-compatible BF16/FP8/FP4 GEMM, MQA indexer logits and MegaMoE. The public release is validated on **Ascend 950/950DT with CANN 9.20**; no 910B2 validation is documented. | [Repository](https://github.com/deepseek-ai/DeepGEMM-Ascend) |
| **DeepEP** | CUDA expert-parallel communication | GPU All-to-All dispatch/combine for MoE training and inference. The Ascend implementation is a separate backend, not implied by this CUDA repository. | [Repository](https://github.com/deepseek-ai/DeepEP) |
| **DeepEP-Ascend** | Ascend communication backend | MoE EP dispatch/combine All-to-All, FP8 dispatch and deferred epilogues; uses Ascend C with HCCL/HCOMM, UBMEM and URMA. Public validation is **Ascend 950DT / CANN 9.2.0 / PoC HDK**; several collectives and expert-load-balancing paths remain work in progress, and other Ascend generations are not established. | [Repository](https://github.com/deepseek-ai/DeepEP-Ascend) |
| **DeepSelect** | TopK / sampling kernels | DSA indexer and sampler TopK for CUDA and Ascend. The documented Ascend path is narrower: BF16 input, int32 indices and TopK up to 4096; do not imply CUDA dtype/shape parity. | [Repository](https://github.com/deepseek-ai/DeepSelect) |
| **DeepJIT** | Runtime JIT toolchain | Header-only C++20 runtime shared by CUDA and Ascend extensions: compile, cache, load and launch kernels; supports local/distributed cache. DeepGEMM-Ascend and DeepEP-Ascend cite it as their JIT layer. | [Repository](https://github.com/deepseek-ai/DeepJIT) |
| **TileKernels** | Official TileLang kernel library | MoE routing, Engram, quantization and mHC kernels used in DeepSeek's internal training/inference workloads. Public Ascend backend targets **Ascend 950 / CANN 9.2.0+**, not 910B2/CANN 9.1. | [Repository](https://github.com/deepseek-ai/TileKernels) |
| **DeepInfer** (2026) | Open-source inference engine | Production-derived V4.1-Flash offline runtime: Attention DP/balanced CP, MoE EP+EPLB, DSpark confidence-scheduled verification, bounded SWA replay, asynchronous scheduling and optimized kernels. **The public release is not a complete online service**: its README lists the KV-cache system, VE/P/D disaggregation and DP-replica load balancing as not included. Targets NVIDIA SM100 and Ascend 950 / CANN 9.2. | [Official repository](https://github.com/deepseek-ai/DeepInfer) · [Deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) |
| **deepseek-recipe** | API-to-token I/O | Rust/Python request/response conversion, model-specific prompt encoding, multimodal preprocessing and streaming parsing; **does not itself perform inference or transport**. | [Repository](https://github.com/deepseek-ai/deepseek-recipe) |
| **DeepSeek-V3 inference demo** | Reference inference implementation | Exposes model architecture/configuration and checkpoint-conversion workflow; **not** a production serving runtime. | [Official repository](https://github.com/deepseek-ai/DeepSeek-V3/tree/main/inference) |

## Production serving architecture — what is and is not open-sourced

DeepSeek's [V4.1-Flash deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) describes the production design behind the public runtime: **Vision Encoder / Prefill / Decode disaggregation**, separate load balancers for each stage plus Expert Parallel, and a dedicated **3FS-backed KV-cache storage** tier. Its example configuration uses smaller Prefill groups (EP2–8 / DP2–8) and Wide-EP Decode groups (EP64–128 / DP64–128); these are deployment-specific recommendations, not universal defaults. Agent traffic uses a 72-hour cache TTL and chatbot traffic up to 7 days in the disclosed configuration.

The Q&A explicitly says KV-cache management and load-balancing code remain tightly coupled to internal infrastructure and are **not fully open-sourced**. Treat the production architecture description as an engineering disclosure, not as code present in DeepInfer. In particular, do not describe the public offline release as a complete P/D serving stack.

## Compiler ecosystem — correct ownership

**[TileLang](https://github.com/tile-ai/tilelang)** ([ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/76fb92288bf90360c527efb0d1c2aba6-Abstract-Conference.html)) is a separately maintained tiled Kernel DSL/compiler, **not a DeepSeek-owned project**. DeepSeek uses it for [TileKernels](https://github.com/deepseek-ai/TileKernels) and provides research-oriented [DSA examples](https://github.com/tile-ai/tilelang/tree/main/examples/deepseek_v32). The published Ascend 950 backend is not proof that the frozen Ascend 910B2/CANN 9.1.0 pair can run it.

## Related context — not counted as serving research

**DeepSeek-R1** ([paper](https://arxiv.org/abs/2501.12948), [official repo](https://github.com/deepseek-ai/DeepSeek-R1)) changes *workload demand* through long reasoning traces but is principally a reasoning/RL contribution, not a serving-system design. Keep it as workload context rather than classifying it as a systems paper.

## Reading order

**V2 MLA → V3 MoE/MTP → V3.2 DSA → V4.1 asymmetric architecture → DeepInfer + production E/P/D/KV design → FlashMLA/DeepSelect → DeepGEMM/DeepEP → Ascend backends (950/CANN 9.2) → TileKernels/TileLang + DeepJIT.** This traces the path from model state representation to kernels, communication and serving topology.

**Scope boundary.** This is not an exhaustive index of DeepSeek model checkpoints, releases, OCR/RL work or community forks. A formal research paper, an official technical report and an open-source implementation are distinct evidence types. Features and supported models evolve rapidly; follow each repository's version notes before interpreting the code.
