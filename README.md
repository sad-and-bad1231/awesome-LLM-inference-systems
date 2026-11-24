# Awesome LLM Inference Systems

A curated, engineering-first map of LLM inference systems: principles, research literature, upstream implementations, industrial systems and emerging execution paradigms.

**977 source-curated papers** across eight technical topics, with 30 historical foundations and dedicated surveys in their topic homes. Selection indicates reading and research value, not independent performance reproduction.

## Surveys — start here

**4 global surveys** covering LLM inference and serving. Specialized surveys are part of their technical topics.

| Lens | Survey | Publication | Scope |
|---|---|---|---|
| Serving: algorithms → systems | [Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems](https://arxiv.org/abs/2312.15234) | arXiv 2023; revised 2025 | CMU/Purdue 等团队，研究解码算法到部署体系结构的完整 Serving 脉络；不覆盖所有 2026 工作。 |
| Hardware / full-stack | [Full Stack Optimization of Transformer Inference: a Survey](https://arxiv.org/abs/2302.14017) | arXiv 2023 | UC Berkeley 团队；算子分析、Mapping、专用加速器与 Gemmini 案例；不限于 LLM Serving。 |
| Resource efficiency | [Resource-efficient Algorithms and Systems of Foundation Models: A Survey](https://doi.org/10.1145/3706418) | ACM Computing Surveys 2025 | PKU/BUPT；覆盖跨计算、存储和部署的优化；包含训练、ViT 和 Diffusion。 |
| Inference architecture | [A Survey of LLM Inference Systems](https://arxiv.org/abs/2506.21901) | arXiv 2025 (preprint) | 清华团队；从 Kernel、Batching、KV 到多副本、P/D 分离和 Serverless；未标为已审稿。 |

## Technical Topics

| Topic | Focus |
|---|---|
| [Kernels & Compilers](topics/kernels-compilers.md) | Attention, GEMM, fusion, compilers and kernel agents |
| [KV Cache & Context Memory](topics/kv-cache-memory.md) | KV allocation, reuse, compression, offload and transfer |
| [Decoding Acceleration](topics/decoding-acceleration.md) | Speculative decoding, parallel verification and non-AR generation |
| [Quantization & Compression](topics/quantization-compression.md) | Weight, activation, KV and state precision |
| [MoE & Sparse Execution](topics/moe-sparse-execution.md) | Expert routing, placement and conditional computation |
| [Runtime & Scheduling](topics/runtime-scheduling.md) | Batching, routing, SLOs and runtime control |
| [Distributed & Disaggregated Serving](topics/distributed-serving.md) | Parallelism, disaggregation, communication and fleet execution |
| [Benchmarking & Systems Analysis](topics/benchmarking-analysis.md) | Workloads, performance models, profiling and correctness |

[Complete topic index](topics/README.md)

## Curation Policy

[Curation policy](CURATION.md) · [G0–G5 review protocol](STRICT_REVIEW.md) · [Review receipts](reviews/README.md). Prefer original papers, inspectable code and specific technical mechanisms. Preprints, published results and first-party engineering reports remain explicitly distinguished.

## Emerging Frontiers

[Frontiers](frontiers/README.md) tracks new execution or optimization contracts: agent-native inference, autonomous inference-engine evolution, diffusion-language-model serving and real-time multimodal / interactive inference. Concrete mechanisms are cross-linked to their topic homes.

## Organizations

[China & United States](organizations/README.md) — first-party model architectures, inference infrastructure, hardware and production engineering.

## Research Labs & Open-Source Communities

[Research labs and communities](communities/README.md) — upstream runtimes, compilers, kernel libraries, communication systems and research teams.

## Contributing

Follow the [curation policy](CURATION.md), preserve one primary paper identity, and keep links to original sources. Submit focused changes with the offline catalog checks passing.
