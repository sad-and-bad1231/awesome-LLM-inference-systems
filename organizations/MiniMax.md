# MiniMax

MiniMax's published long-context attention and model architectures, with their serving implications.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **MiniMax-01** | Model family with efficient long-context attention design; primarily a model architecture / technical report. | [Official source](https://github.com/MiniMax-AI/MiniMax-01) |
| **MiniMax-M2** | MoE-style model and deployment guidance for coding and agentic workloads, not a standalone serving framework. | [Official source](https://github.com/MiniMax-AI/MiniMax-M2) |
| **MiniMax-M3** (2026) | MoE with MiniMax Sparse Attention (MSA): lightning-indexer/block-sparse attention introduces a separate index-state and indexed-attention kernel path. This is **model architecture**, not a reusable scheduler. | [Official repository](https://github.com/MiniMax-AI/MiniMax-M3) · [MSA preprint](https://arxiv.org/abs/2606.13392) |
| **MiniMax-M3.1-Flash** (2026-10) | 428B MoE / 23B activated; native multimodal, up to 1M context. Replaces the former first-three full-attention layers with sparse attention; combines attention/expert quantization-aware training and **DSpark** speculative draft head. Architecture/weights and deployment recipes are public; vendor online TPS/cost claims are **not independently reproduced or cross-model matched**. | [Official model card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) · [Official release](https://www.minimax.io/blog/minimax-m31f) |

**Evidence boundary:** M3.1-Flash is a model / kernel workload contract, not proof that DSpark or its sparse-attention backend is available on Ascend 910B2 or in the user's pinned vLLM pair. Model speedups reported by the vendor are not independent serving measurements.

## Official model-family crosswalk (2026-10-24)

**Catalog authority:** [MiniMax model navigation](https://www.minimax.io/) and [developer model/pricing catalog](https://platform.minimax.io/subscribe/token-plan). The website's **five currently featured families** are not the same denominator as historical models or API model IDs.

| Official model family | Serving classification / scope | Source |
|---|---|---|
| MiniMax-M3.1-Flash | Current promoted flagship, model+runtime co-design, sparse attention / QAT / DSpark | [Official October launch](https://www.minimax.io/blog/minimax-m31f) |
| MiniMax-M3 | Current featured LLM, open model; MSA indexed/sparse execution | [Official repo](https://github.com/MiniMax-AI/MiniMax-M3) |
| MiniMax-M2.7 / M2.7-highspeed | Still documented on developer platform, with highspeed as service tier, not an independently published attention primitive | [Official developer plan](https://platform.minimax.io/subscribe/token-plan) |
| MiniMax-M2.5 | Older but still exposed in website/model navigation; separate model family from M3 | [Official model navigation](https://www.minimax.io/) |
| MiniMax-M2 / M2.1 / MiniMax-01 | Historical text/long-context architectures; retain for architecture lineage, not current SOTA inference claims | [M2 code](https://github.com/MiniMax-AI/MiniMax-M2) · [01 code](https://github.com/MiniMax-AI/MiniMax-01) |
| MiniMax H3 | Current featured **video/omni generation** model: not autoregressive text LLM serving | [Official model navigation](https://www.minimax.io/) |
| MiniMax Speech 2.8 (HD / Turbo) | Current featured TTS generation, different streaming and decoder workload | [Official API pricing](https://platform.minimax.io/subscribe/token-plan?tab=api-enterprise) |
| MiniMax Music 3.0 | Current featured music/audio generation; not text-LLM Kernel benchmark | [Official release listing](https://www.minimax.io/blog) |

**Coverage:** 5 prominent website family links (M3.1 Flash, M3, H3, Speech 2.8, Music 3.0); M2.5/M2.7 remain on other first-party navigation/API pages. Do not count highspeed/HD/Turbo as independently novel architectures.
