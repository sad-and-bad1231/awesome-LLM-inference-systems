# NVIDIA

**Inference systems, execution libraries and the communication substrate.** This page tracks NVIDIA's relevant *public engineering artifacts and selected research*, not every product announcement or model launch. “NVIDIA” denotes ownership/maintainership of the linked projects unless marked **collaboration**.

[← Home](../README.md) · [Serving systems](../topics/serving-systems.md)

## Serving and deployment

| Work | Artifact type | Why it matters for inference | Official source |
|---|---|---|---|
| **TensorRT-LLM** | Open-source inference engine | Specialized kernels, KV-cache management, in-flight batching, quantized inference and multi-GPU execution. | [Repository](https://github.com/NVIDIA/TensorRT-LLM) |
| **Dynamo** | Open-source distributed serving framework | Multi-node inference orchestration above execution engines: disaggregated P/D, KV-aware routing, dynamic GPU allocation and KV block management. | [Repository](https://github.com/ai-dynamo/dynamo) |
| **NVIDIA Triton Inference Server** | Open-source model server | Backend integration, scheduling and standardized model serving; broader than LLMs. | [Repository](https://github.com/triton-inference-server/server) |
| **Dynamo KV Block Manager (KVBM)** | Framework subsystem | Tiered KV-cache lifecycle across GPU, CPU and storage, with cache movement via NIXL. **Not** a separate paper or engine. | [NVIDIA technical write-up](https://developer.nvidia.com/blog/how-to-reduce-kv-cache-bottlenecks-with-nvidia-dynamo/) |
| **NVIDIA Model Optimizer** | Open-source optimization toolkit | Quantization and model optimization to make lower-precision deployment feasible. | [Repository](https://github.com/NVIDIA/Model-Optimizer) |
| **TensorRT** | Inference compilation/runtime toolkit | General accelerated inference engine underneath some deployment stacks; not LLM-specific. | [Repository](https://github.com/NVIDIA/TensorRT) |

## Data movement and execution substrate

| Work | Artifact type | Why it matters | Official source |
|---|---|---|---|
| **NIXL** | Open-source transfer library | Point-to-point asynchronous movement across heterogeneous memory and storage, especially P/D KV transfers. | [Repository](https://github.com/ai-dynamo/nixl) |
| **CUTLASS / CuTe** | Open-source CUDA templates and abstractions | Programmable data movement and high-performance GEMM primitives used in LLM kernel design. | [Repository](https://github.com/NVIDIA/cutlass) |
| **NCCL** | Open-source GPU collectives | Collectives underlying TP/DP/EP communication; a reusable substrate, not an LLM serving runtime. | [Repository](https://github.com/NVIDIA/nccl) |
| **NVSHMEM** | Open-source GPU communication | GPU-initiated communication and distributed memory primitives; potential kernel/communication building block. | [Repository](https://github.com/NVIDIA/nvshmem) |
| **Transformer Engine** | Open-source precision/runtime components | FP8/other low-precision Transformer building blocks used across training and inference. | [Repository](https://github.com/NVIDIA/TransformerEngine) |
| **FasterTransformer** | Historical inference library | Earlier highly optimized Transformer inference kernels; useful for following the lineage of TensorRT-LLM. **Legacy**, not the recommended new serving stack. | [Repository](https://github.com/NVIDIA/FasterTransformer) |

## Selected research and technical materials

| Work | Provenance | Why included | Primary source |
|---|---|---|---|
| **FlashInfer** (MLSys 2025) | **Collaboration**, not exclusively NVIDIA | Serving-oriented Attention Engine with composable KV formats, JIT templates and scheduling. | [MLSys proceedings](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) |
| **Strata** (OSDI 2026) | **Collaboration**, Stanford / NVIDIA and others | Hierarchical context caching and I/O-aware KV layout/scheduling for long-context serving. | [USENIX proceedings](https://www.usenix.org/conference/osdi26/presentation/xie-zhiqiang) |
| **NVIDIA Dynamo architecture** (2025) | Official engineering documentation | Planner, KV-aware router, KVBM and NIXL in one distributed serving architecture. **Not peer-reviewed research.** | [NVIDIA technical blog](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) |
| **TensorRT-LLM KV reuse** (2025) | Official engineering documentation | Priority-based KV retention and event APIs for routing/cache observability. **Not a paper.** | [NVIDIA technical blog](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/) |

## Reading order

**Execution engine → Distributed control plane → Data movement → Kernel substrate**: TensorRT-LLM → Dynamo → NIXL/KVBM → CUTLASS/NCCL. Read FlashInfer and Strata as academic, cross-institutional evidence for specific mechanisms.

**Scope boundary.** NVIDIA's broader portfolio also includes training frameworks, hardware design, networking and model releases. These are not catalogued exhaustively; they are admitted here only when they illuminate inference execution. Vendor performance numbers are not treated as independently reproduced results.
