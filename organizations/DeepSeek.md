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
| **DeepSeek-V4.1-Flash** (2026) | Official model / implementation reference | Supported model family in contemporary FlashMLA code. **No separate conference-paper status is asserted here.** | [Official model page](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) |

## Execution and communication libraries

| Work | Type | Technical role | Official source |
|---|---|---|---|
| **FlashMLA** | CUDA / Ascend Attention kernels | MLA/DSA-oriented prefill and decode execution, sparse attention and fusion. **Version compatibility is significant**: the 2026-09-30 release removes old Hopper/model-format support. | [Repository and compatibility notice](https://github.com/deepseek-ai/FlashMLA) |
| **DeepGEMM** | JIT GPU kernel library | FP8/FP4/BF16 GEMM, fused MoE operations and scoring primitives. | [Repository](https://github.com/deepseek-ai/DeepGEMM) |
| **DeepGEMM-Ascend** | NPU kernel backend | Ascend-native matrix and MoE primitives with a DeepGEMM-compatible interface; confirm version/device support before replication. | [Repository](https://github.com/deepseek-ai/DeepGEMM-Ascend) |
| **DeepEP** | GPU/NPU communication library | Low-latency and high-throughput expert-parallel All-to-All dispatch/combine and inference-specialized communication. | [Repository](https://github.com/deepseek-ai/DeepEP) |
| **DeepSelect** | TopK / Sampling kernels | Fast TopK selection for DSA indexers and sampling; CUDA and Ascend implementations. | [Repository](https://github.com/deepseek-ai/DeepSelect) |
| **DeepJIT** | Runtime kernel compilation | JIT tooling used by the DeepGEMM/DeepEP execution stack; an implementation component rather than a separate research publication. | [Repository](https://github.com/deepseek-ai/DeepJIT) |
| **DeepSeek-V3 inference demo** | Reference inference implementation | Exposes model architecture/configuration and checkpoint-conversion workflow; **not** a production serving runtime. | [Official repository](https://github.com/deepseek-ai/DeepSeek-V3/tree/main/inference) |

## Related context — not counted as serving research

**DeepSeek-R1** ([paper](https://arxiv.org/abs/2501.12948), [official repo](https://github.com/deepseek-ai/DeepSeek-R1)) changes *workload demand* through long reasoning traces but is principally a reasoning/RL contribution, not a serving-system design. Keep it as workload context rather than classifying it as a systems paper.

## Reading order

**V2 MLA → V3 MoE/MTP → V3.2 DSA → FlashMLA/DeepSelect → DeepGEMM/DeepEP → Ascend port.** This traces the path from algorithmic state representation to device kernels and inter-GPU communication.

**Scope boundary.** This is not an exhaustive index of DeepSeek model checkpoints, releases, OCR/RL work or community forks. A formal research paper, an official technical report and an open-source implementation are distinct evidence types. Features and supported models evolve rapidly; follow each repository's version notes before interpreting the code.
