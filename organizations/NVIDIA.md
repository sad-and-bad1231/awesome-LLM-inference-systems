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

## November 5, 2026: co-designed agent KV memory hierarchy

NVIDIA's [first-party technical source](https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/) is a **vendor performance/architecture report**, not a new peer-reviewed systems paper or independent reproduction. Five distinct levers must not be counted as five separate benchmark results:

| Stack mechanism | What is exposed | Evidence and deployment boundary |
|---|---|---|
| **NVFP4 weight and KV** | Reduce low-bit model and KV memory footprints to allocate more HBM to concurrent sessions | NVFP4 KV is **approximate** and some DeepSeek-V4-Pro quality scores change; NVIDIA's peak ratios depend on model and comparison precision, not universal BF16-equivalent execution |
| **Wide-EP + TensorRT-LLM** | Spread MoE Expert weight storage and execution across devices for greater cache headroom and arithmetic intensity | Cost/throughput depends on expert distribution and collective topology; not a new NVIDIA ownership claim for the model |
| **Dynamo + NIXL KV tiering** | KV-aware routing, P/D transfer and multi-level KV cache runner | Distinguish global KV placement and transport from attention-kernel timing or a production cluster Goodput guarantee |
| **Vera CPU / NVLink-C2C idle-agent KV** | Fast CPU-side Tool execution shortens idle intervals; move session KV out of HBM into large coherent CPU memory while tools are running | This is a **Vera/Rubin-specific hardware/runtime co-design**; not demonstrated as an Ascend NPU result |
| **CMX G3.5 context storage** | BlueField-4 STX + Spectrum-X + DOCA Memos + Dynamo/NIXL pool NVMe KV across nodes | NVIDIA reports **up to 5×** token output/power-efficiency gains **against traditional storage on selected workloads**. Pod-level design/announcement is not proof that generic NVMe or all engines deliver 5× |

**Systems interpretation:** the new frontier is **session state lifecycle and data placement spanning tools, GPU, host and pod storage**, not “larger HBM automatically means faster decoding.” Inspect published code/release versions of Dynamo/NIXL/DOCA Memos separately before claiming a reproducible implementation.

**Boundary.** First-party software and documentation only. Research coauthored with Stanford, UW, CMU and other labs is not automatically classified as NVIDIA work. Software feature and hardware support claims depend on the linked repository version.
