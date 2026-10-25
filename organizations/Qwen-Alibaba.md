# Qwen (Alibaba)

The Qwen team's publicly released model families and inference-related model architecture. Runtime implementations from vLLM/SGLang/LMDeploy remain credited to their respective maintainers.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Qwen3** | Dense/MoE model family with thinking and non-thinking execution modes; inspect active experts, KV and decoding requirements. | [Official source](https://github.com/QwenLM/Qwen3) |
| **Qwen3-Next / Qwen3.5–3.8** (2025–26) | Qwen's hybrid **Gated DeltaNet recurrent state + gated full attention** family; Qwen3.5 uses an approximately 3:1 linear/full-attention stack. Recurrent-state and KV attention require distinct memory layouts/kernels; Qwen3.8 largely evolves the family rather than introducing another basic inference attention primitive. | [Official family repository](https://github.com/QwenLM/Qwen3.8) · [Qwen3.5 architecture reference](https://huggingface.co/docs/transformers/en/model_doc/qwen3_5) |
| **Qwen3.8-Flash-Next** (2026) | Early architectural preview combining **Gated DeltaNet + Qwen Sparse Attention (QSA)**, gated residual streams and N-gram embeddings with asynchronous host prefetch. Substantive inference contracts: sparse indexer, recurrent state, cache/offload and execution overlap. Claims remain author-reported. | [Official repository](https://github.com/QwenLM/Qwen3.8-Flash-Next) |
| **Qwen3-Coder** | Code-oriented model family; long-context and agentic generation create distinct serving workloads. | [Official source](https://github.com/QwenLM/Qwen3-Coder) |
| **Qwen3-Omni** | Multimodal model family with streaming audio/video/text execution considerations. | [Official source](https://github.com/QwenLM/Qwen3-Omni) |
| **MNN (Alibaba)** | Alibaba-maintained efficient inference engine, including on-device model execution. | [Official source](https://github.com/alibaba/MNN) |

**Scope:** Architecture/runtime-relevant releases only. A model-family repository is not proof of a new online serving algorithm or NPU performance result; vLLM/SGLang backend implementation and checkpoint compatibility must be checked independently.
