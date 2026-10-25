# Google

A short index of Google's **inference-system research, open-source serving software, and efficient model execution**.

[← Organizations](../README.md#organizations)

## Official Gemini and Gemma model portfolio (2026-10-24)

**Authorities:** [Gemini API complete model catalog](https://ai.google.dev/gemini-api/docs/models), [Gemma releases](https://ai.google.dev/gemma/docs/releases), [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4). This distinguishes **closed Gemini API IDs** from **downloadable Gemma weights**.

| Publicly listed family | Sub-models and inference implications | Official source |
|---|---|---|
| Gemini 4 | Gemini **4 Argon**, next flagship API family | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini 3 | 3.8 Flash; 3.6 Flash; 3.5 Flash-Lite; 3.1 Flash-Lite and older Pro/Flash preview entries | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini Live / speech | 3.8 Live, 3.8 Live Extended Thinking, 3.5 Live Translate, 3.8 Flash/Flash-Lite TTS, 3.5 Transcribe | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini 2.5 | 2.5 Pro, Flash, Flash-Lite and audio versions (generation lineage; not new 2026 releases) | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini media and tools | Nano Banana image family, Gemini Omni Flash video, Lyria music, Deep Research, Robotics ER, Gemini Embedding | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemma 4 | **E2B, E4B, 12B Unified, 26B A4B MoE, 31B Dense**; small-device/per-layer embeddings, attention variants, MTP edition | [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4) |
| Other Gemma specializations | Gemma 3/3n, EmbeddingGemma 2, FunctionGemma, TranslateGemma, MedGemma, ShieldGemma | [Gemma release history](https://ai.google.dev/gemma/docs/releases) |

**Full API ID scope:** the provider catalog also lists preview, retired, embedding, media and agent-specific endpoints. Use the linked official model catalog for the full and changeable *exact ID* inventory; individual service IDs are not standalone systems papers.

## Foundational techniques and models

| Work | Inference relevance | Primary source |
|---|---|---|
| **Multi-Query Attention (MQA)** (2019) | Sharing key/value heads reduces autoregressive decode KV bandwidth. | [Paper](https://arxiv.org/abs/1911.02150) |
| **Efficiently Scaling Transformer Inference** (MLSys 2023) | TPU parallelism and performance-model-guided latency/throughput engineering. | [MLSys](https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html) |
| **Speculative Decoding** (ICML 2023) | Draft-and-verify decoding while preserving the target distribution. | [PMLR](https://proceedings.mlr.press/v202/leviathan23a.html) |
| **Grouped-Query Attention (GQA)** (EMNLP 2023) | Attention-head grouping trades off decode bandwidth and model quality. | [ACL Anthology](https://aclanthology.org/2023.emnlp-main.298/) |
| **Gemma family** | Open-weight architectures and deployment examples; model design, **not** a disclosed Google production serving stack. | [Official models/docs](https://ai.google.dev/gemma/docs) |

## Infrastructure

| Project | Role | Official source |
|---|---|---|
| **JetStream** | High-throughput LLM inference engine targeting TPU-oriented deployments. | [GitHub](https://github.com/google/JetStream) |
| **SAX / SAXML** | Scalable JAX/TPU model-serving platform. | [GitHub](https://github.com/google/saxml) |
| **MaxText** | Open JAX/TPU LLM implementation with generation/inference paths; also a training framework. | [GitHub](https://github.com/google/maxtext) |
| **Gemma.cpp** | Lightweight C++ inference for Gemma on resource-constrained devices. | [GitHub](https://github.com/google/gemma.cpp) |

**Boundary.** Selected Google-authored research and first-party projects, not the entirety of Google Cloud's managed model catalog. A model architecture contribution is not evidence of an unpublished serving implementation.
