# NVIDIA

NVIDIA's **first-party inference software stack**, from serving engines and cluster orchestration to GPU communication and kernels. This page intentionally excludes multi-institution academic collaborations; those belong in the paper collections, not the company index.

[← Organizations](../README.md#organizations)

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
