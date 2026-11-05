# Meta

Selected **Llama architectural choices and first-party execution components**. Model announcements and research infrastructure are distinguished.

[← Organizations](../README.md#organizations)

## Official Llama / on-device model-family coverage (2026-10-24)

| Publicly disclosed family | What to include in the model-engineering map | Primary source |
|---|---|---|
| Llama 4 | **Scout and Maverick** MoE and multimodal model variants, sparse expert execution vs Llama 3 baseline | [Official Llama 4 announcement](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |
| Llama 3 / 3.1 / 3.2 / 3.3 | Dense/GQA, edge/multimodal sizes, 405B deployment history, documented historical variants | [Official Llama 3.1 release](https://ai.meta.com/blog/meta-llama-3-1/) |
| Open model runtimes | [ExecuTorch](https://github.com/pytorch/executorch), [torchao](https://github.com/pytorch/ao), [xFormers](https://github.com/facebookresearch/xformers), FBGEMM | [First-party GitHub](https://github.com/pytorch/executorch) |

This is the **public Llama model-family** inventory, not an unsupported enumeration of Meta proprietary production/consumer endpoints. No newer Llama base architecture is asserted without a first-party release.

## Llama model families

| Work | Inference relevance | Primary source |
|---|---|---|
| **Llama 3** (2024) | GQA in 8B and 70B models, with tokenizer efficiency improvements. | [Meta announcement](https://ai.meta.com/blog/meta-llama-3/) |
| **Llama 3.1** (2024) | 405B deployment and FP8 inference choices; longer-context model serving requirements. | [Meta announcement](https://ai.meta.com/blog/meta-llama-3-1/) |
| **Llama 4** (2025) | MoE with limited active parameters per token and natively multimodal execution, introducing expert routing requirements. | [Meta announcement](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |

## Production inference-system engineering (2025–2026)

| First-party source | Reusable mechanism | Scope and evidence |
|---|---|---|
| [KernelEvolve](https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/) (2026-04-02) | Meta's **evaluator-guided kernel optimization agent** searches candidates for GPU/AMD/MTIA/CPU inference and training kernels with operational deployment feedback. | Meta reports **60% ads-model inference throughput** improvement in a specified deployment; this is **not** LLM decoding engine speedup or a verified recursive change to the agent's own model weights. |
| [LLM inference TP/CP/EP engineering](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/) (2025) | Practical parallel execution choices for production LLM inference, communication/memory tradeoffs and deployment efficiency. | Team engineering evidence; do not attribute every Meta service to this configuration. |
| [Opportunistic inference capacity](https://engineering.fb.com/2026/10/12/ml-applications/turning-opportunistic-ai-inference-capacity-into-better-ads-recommendations/) (2026-10-12) | Exploits idle inference fleet capacity with elasticity controls while guarding baseline request performance. | **Advertising recommendation inference**, not autoregressive text generation; a useful workload elasticity analogue, not canonical LLM-serving performance. |
| [Meta Adaptive Ranking Model](https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/) (2026) | Context-aware request-dependent inference complexity / routing for large ads recommender networks. | “LLM-scale” **RecSys** does not mean a causal LLM token decoder; apply as an adjacent systems idea only. |

**RSI research boundary:** [KernelEvolve](https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/) is a stronger first-party **production kernel agent** signal than a generic agent coding demo. It belongs beside [autonomous engine evolution](../frontiers/README.md#autonomous-inference-engine-evolution-separate-engine-evolution-from-rsi) but does **not** prove that a full model-serving engine or the optimizer's underlying LLM recursively self-improves.

## Execution

| Project | Role | Official source |
|---|---|---|
| **xFormers** | Efficient Transformer/Attention operators and memory-efficient implementations. | [GitHub](https://github.com/facebookresearch/xformers) |
| **ExecuTorch** | On-device inference runtime for edge and mobile hardware. | [GitHub](https://github.com/pytorch/executorch) |
| **torchao** | Quantization and low-precision tensor techniques relevant to inference execution. | [GitHub](https://github.com/pytorch/ao) |
| **FBGEMM** | High-performance CPU/GPU matrix and embedding operations, including lower-precision computation. | [GitHub](https://github.com/pytorch/FBGEMM) |

**Boundary.** PyTorch ecosystem components are included for their widely used open-source inference capabilities; the page does not claim all PyTorch contributors or each component's work is exclusively Meta's.
