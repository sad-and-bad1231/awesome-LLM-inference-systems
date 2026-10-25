# NVIDIA

NVIDIA's **first-party inference software stack**, from serving engines and cluster orchestration to GPU communication and kernels. This page intentionally excludes multi-institution academic collaborations; those belong in the paper collections, not the company index.

[← Organizations](../README.md#organizations)

## Official NVIDIA model-family crosswalk (2026-10-24)

**First-party model registry:** [NVIDIA-hosted model cards](https://build.nvidia.com/nvidia) and [official Nemotron family overview](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/llm-info/). This is different from the **TensorRT-LLM / Dynamo / NIXL** software stack.

| Published model family | Named variants and inference relevance | Source |
|---|---|---|
| Nemotron 3 | **Nano (30B-A3B / 4B), Nano Omni, Super (120B-A12B), Ultra (550B-A55B)**; hybrid Mamba/Transformer MoE and low-latency Agent workloads | [Official Nemotron family](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/llm-info/) |
| Nemotron 3.5 | **Lightning 30B-A3B**, **Bolt E4B**, **Super-VL 120B-A12B early access**; 3.5 extensions, not independent new inference systems | [Official model catalog](https://build.nvidia.com/nvidia) |
| Nemotron retrieval / document | Nemotron 3/3.5 Embed, Rerank, OCR, Parse; distinct encoder/retrieval/document workloads from text decoding | [Official model catalog](https://build.nvidia.com/nvidia) |
| Other NVIDIA models | Speech/safety/content-specific Nemotron and non-LLM physical/vision foundation models live in the **provider catalog**; do not imply the 67 catalog records are 67 new LLM architectures | [Official model catalog](https://build.nvidia.com/nvidia) |

**Do not confuse model ownership with support:** NVIDIA NIM can *host* DeepSeek or Qwen models, but that does not make them NVIDIA-designed model families. NVIDIA's runtime/kernel artifacts belong above this line under Execution.

## Inference and serving

| Project | Role | Official source |
|---|---|---|
| **TensorRT-LLM** | LLM inference engine: quantization, batching, attention kernels and distributed execution. | [GitHub](https://github.com/NVIDIA/TensorRT-LLM) |
| **Dynamo** | Distributed inference orchestration, KV-aware request routing, disaggregated serving and cache management. | [GitHub](https://github.com/ai-dynamo/dynamo) |
| **Triton Inference Server** | General model-serving server and backend/scheduling integration; broader than LLMs. | [GitHub](https://github.com/triton-inference-server/server) |
| **NVIDIA Model Optimizer** | Quantization and model compression workflows supporting efficient deployment. | [GitHub](https://github.com/NVIDIA/Model-Optimizer) |

## Communication and kernels

| Project | Role | Official source |
|---|---|---|
| **NIXL** | Asynchronous transfer interface for disaggregated inference and KV movement across heterogeneous memory/storage. | [GitHub](https://github.com/ai-dynamo/nixl) |
| **CUTLASS / CuTe** | GPU GEMM, tiling and data-movement programming primitives. | [GitHub](https://github.com/NVIDIA/cutlass) |
| **Transformer Engine** | Low-precision Transformer execution primitives. | [GitHub](https://github.com/NVIDIA/TransformerEngine) |
| **NCCL / NVSHMEM** | Multi-GPU collective communication and GPU-initiated communication substrates. | [NCCL](https://github.com/NVIDIA/nccl) · [NVSHMEM](https://github.com/NVIDIA/nvshmem) |

**Boundary.** First-party software and documentation only. Research coauthored with Stanford, UW, CMU and other labs is not automatically classified as NVIDIA work. Software feature and hardware support claims depend on the linked repository version.
