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
