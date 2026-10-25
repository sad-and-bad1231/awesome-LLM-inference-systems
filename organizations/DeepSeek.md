# DeepSeek

**Model architecture ↔ inference kernel ↔ expert communication.** The focus is on how DeepSeek's public work changes *inference computation, KV state, sparsity, MoE dispatch and deployment*. Model-quality and RL results appear only as context; they are not misrepresented as serving-system papers.

[← Home](../README.md) · [Serving systems](../topics/serving-systems.md)

## Architecture papers and official artifacts

| Work | Status | Inference-system contribution / boundary | Primary source |
|---|---|---|---|
| **DeepSeek-V2** (2024) | Technical report | Multi-head Latent Attention (MLA) compresses KV state; DeepSeekMoE makes sparse-expert execution a central serving concern. | [Paper](https://arxiv.org/abs/2405.04434) · [Official repo](https://github.com/deepseek-ai/DeepSeek-V2) |
| **DeepSeek-V3** (2024) | Technical report | Production-scale MLA/MoE design, Multi-Token Prediction and engineering tradeoffs; FP8/DualPipe details primarily concern **training**. | [Paper](https://arxiv.org/abs/2412.19437) · [Official repo](https://github.com/deepseek-ai/DeepSeek-V3) |
| **DeepSeek-V3.2-Exp** (2025) | Official experimental release | Introduces DeepSeek Sparse Attention (DSA), motivating indexer TopK and sparse MLA kernel implementations. Experimental release, not a conference paper. | [Official repo](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) |
| **DeepSeek-V3.2** (2025) | Technical report | DeepSeek Sparse Attention: long-context computation is reduced through learned fine-grained sparse selection. Discussion of RL and agent performance is outside this page's systems focus. | [Paper](https://arxiv.org/abs/2512.02556) · [Official repo](https://github.com/deepseek-ai/DeepSeek-V3.2) |
| **DeepSeek-V4.1-Flash / -1017** (2026) | Official model release | Asymmetric causal encoder–decoder MoE (552B total; 8B/16B activated in input/output phases), designed to reduce KV-storage costs. The published model architecture is not a serving-runtime performance proof. | [Official release](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) · [API changelog](https://api-docs.deepseek.com/updates/) |

## Execution and communication libraries

| Work | Type | Technical role | Official source |
|---|---|---|---|
| **FlashMLA** | CUDA / Ascend Attention kernels | MLA/DSA-oriented prefill and decode execution, sparse attention and fusion. **Version compatibility is significant**: the 2026-09-30 release removes old Hopper/model-format support. | [Repository and compatibility notice](https://github.com/deepseek-ai/FlashMLA) |
| **DeepGEMM** | JIT GPU kernel library | FP8/FP4/BF16 GEMM, fused MoE operations and scoring primitives. | [Repository](https://github.com/deepseek-ai/DeepGEMM) |
| **DeepGEMM-Ascend** | NPU kernel backend | Ascend-native matrix and MoE primitives with a DeepGEMM-compatible interface; confirm version/device support before replication. | [Repository](https://github.com/deepseek-ai/DeepGEMM-Ascend) |
| **DeepEP** | GPU/NPU communication library | Low-latency and high-throughput expert-parallel All-to-All dispatch/combine and inference-specialized communication. | [Repository](https://github.com/deepseek-ai/DeepEP) |
| **DeepSelect** | TopK / Sampling kernels | Fast TopK selection for DSA indexers and sampling; CUDA and Ascend implementations. | [Repository](https://github.com/deepseek-ai/DeepSelect) |
| **DeepJIT** | Runtime kernel compilation | JIT tooling used by the DeepGEMM/DeepEP execution stack; an implementation component rather than a separate research publication. | [Repository](https://github.com/deepseek-ai/DeepJIT) |
| **TileKernels** | Official TileLang kernel library | Real deployed MoE routing, FP8/FP4 conversion, Engram/mHC and transform kernels; the project states internal training/inference use. Public Ascend path currently targets Ascend 950 / CANN 9.2+, **not confirmed for 910B2**. | [Repository](https://github.com/deepseek-ai/TileKernels) |
| **DeepInfer** (2026) | Open-source inference engine | Production-derived model/runtime/communication integration: ADP/CP, MoE EP/EPLB, DSpark, bounded SWA replay, asynchronous scheduling, and optimized kernels. **Public drop is offline inference for V4.1-Flash, not a complete production online serving stack**; full KV service, P/D disaggregation and DP replica balancing are not included. NVIDIA SM100 and Ascend 950 / CANN 9.2 paths are documented. | [Official repository](https://github.com/deepseek-ai/DeepInfer) · [Deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) |
| **deepseek-recipe** | API-to-token I/O | Rust/Python request/response conversion, model-specific prompt encoding, multimodal preprocessing and streaming parsing; **does not itself perform inference or transport**. | [Repository](https://github.com/deepseek-ai/deepseek-recipe) |
| **DeepSeek-V3 inference demo** | Reference inference implementation | Exposes model architecture/configuration and checkpoint-conversion workflow; **not** a production serving runtime. | [Official repository](https://github.com/deepseek-ai/DeepSeek-V3/tree/main/inference) |

## Compiler ecosystem — correct ownership

**[TileLang](https://github.com/tile-ai/tilelang)** ([ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/76fb92288bf90360c527efb0d1c2aba6-Abstract-Conference.html)) is a separately maintained tiled Kernel DSL/compiler, **not a DeepSeek-owned project**. DeepSeek uses it for [TileKernels](https://github.com/deepseek-ai/TileKernels) and provides research-oriented [DSA examples](https://github.com/tile-ai/tilelang/tree/main/examples/deepseek_v32). The published Ascend 950 backend is not proof that the frozen Ascend 910B2/CANN 9.1.0 pair can run it.

## Related context — not counted as serving research

**DeepSeek-R1** ([paper](https://arxiv.org/abs/2501.12948), [official repo](https://github.com/deepseek-ai/DeepSeek-R1)) changes *workload demand* through long reasoning traces but is principally a reasoning/RL contribution, not a serving-system design. Keep it as workload context rather than classifying it as a systems paper.

## Reading order

**V2 MLA → V3 MoE/MTP → V3.2 DSA → V4.1 asymmetric architecture → DeepInfer runtime/scheduling → TileKernels/TileLang + FlashMLA/DeepGEMM/DeepEP → supported Ascend backend.** This traces the path from algorithmic state representation to device kernels and inter-GPU communication.

**Scope boundary.** This is not an exhaustive index of DeepSeek model checkpoints, releases, OCR/RL work or community forks. A formal research paper, an official technical report and an open-source implementation are distinct evidence types. Features and supported models evolve rapidly; follow each repository's version notes before interpreting the code.
