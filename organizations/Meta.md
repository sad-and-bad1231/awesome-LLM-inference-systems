# Meta

Selected **Llama architectural choices and first-party execution components**. Model announcements and research infrastructure are distinguished.

[← Organizations](../README.md#organizations)

## Llama model families

| Work | Inference relevance | Primary source |
|---|---|---|
| **Llama 3** (2024) | GQA in 8B and 70B models, with tokenizer efficiency improvements. | [Meta announcement](https://ai.meta.com/blog/meta-llama-3/) |
| **Llama 3.1** (2024) | 405B deployment and FP8 inference choices; longer-context model serving requirements. | [Meta announcement](https://ai.meta.com/blog/meta-llama-3-1/) |
| **Llama 4** (2025) | MoE with limited active parameters per token and natively multimodal execution, introducing expert routing requirements. | [Meta announcement](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |

## Execution

| Project | Role | Official source |
|---|---|---|
| **xFormers** | Efficient Transformer/Attention operators and memory-efficient implementations. | [GitHub](https://github.com/facebookresearch/xformers) |
| **ExecuTorch** | On-device inference runtime for edge and mobile hardware. | [GitHub](https://github.com/pytorch/executorch) |
| **torchao** | Quantization and low-precision tensor techniques relevant to inference execution. | [GitHub](https://github.com/pytorch/ao) |
| **FBGEMM** | High-performance CPU/GPU matrix and embedding operations, including lower-precision computation. | [GitHub](https://github.com/pytorch/FBGEMM) |

**Boundary.** PyTorch ecosystem components are included for their widely used open-source inference capabilities; the page does not claim all PyTorch contributors or each component's work is exclusively Meta's.
