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

## Official model-family coverage (2026-10-24)

**Authoritative catalog:** [Alibaba Cloud Model Studio models](https://help.aliyun.com/zh/model-studio/web-search) enumerates service families and versions; [Qwen repositories](https://github.com/QwenLM) are first-party code/weights. **Family vs API model ID vs open checkpoint** must be distinguished.

| Official family | Model inventory / inference contract | Primary source |
|---|---|---|
| Qwen3.8 | Max, Flash, 2.4T-A95B, 27B; 3.8-Flash-Next is a separate model/research implementation featuring GDN+QSA | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) · [Flash-Next source](https://github.com/QwenLM/Qwen3.8-Flash-Next) |
| Qwen3.7 | Max, Plus, Flash and dated API snapshots | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3.6 | Plus, Flash, 27B, 35B-A3B and dated API snapshots | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3.5 | Plus, Flash, 27B, 35B-A3B, 122B-A10B, 397B-A17B; Gated DeltaNet + full-attention execution | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3 / Qwen3-Max / Qwen3-Next | Foundational dense/MoE and historical hybrid-linear transition; Qwen3-Max is a hosted family rather than every published small checkpoint | [Qwen3 source](https://github.com/QwenLM/Qwen3) · [Model Studio](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3-Coder / Qwen3-VL / Qwen3-Omni | Code-heavy long outputs; multimodal image/video/voice inputs with distinct prefill/streaming pipelines | [Coder](https://github.com/QwenLM/Qwen3-Coder) · [Omni](https://github.com/QwenLM/Qwen3-Omni) |
| Qwen3.5-Omni / Qwen3.8-Omni | Plus/Flash, Realtime variants; low-latency streaming audio/visual model family | [Model Studio Omni list](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3.8-Omni-Flash / Realtime | Latest listed Omni Flash and real-time version; not identical to ordinary text Flash | [Model Studio Omni list](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen2.5 / Qwen2.5-VL and earlier | Historical dense/VL checkpoint families; retained as stable vLLM comparison workloads | [Model Studio import list](https://help.aliyun.com/zh/model-studio/model-import) |
| Qwen Image / Wan | Adjacent image/video generation workloads, **not** part of text LLM serving | [Alibaba/Qwen project navigation](https://github.com/QwenLM) |

**Policy:** Model Studio lists *many* dated snapshots and sizes. The primary catalog is the exhaustive API-ID registry; this curated page covers **all named major service families** without asserting every `-YYYY-MM-DD` snapshot is a new inference architecture.
