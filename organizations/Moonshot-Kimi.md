# Moonshot AI / Kimi

Moonshot AI/Kimi's model architecture and **production-oriented KV-cache infrastructure**.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Kimi-K2** | Open model family with sparse expert execution and long-running generation serving implications. | [Official source](https://github.com/MoonshotAI/Kimi-K2) |
| **Kimi-K3** (2026) | Open 2.8T MoE with 104B activated; **69 KDA + 24 Gated MLA** attention layers, Attention Residuals (AttnRes), Stable LatentMoE, 1M context and MXFP4/MXFP8 quantized execution. Recurrent state and KV-cache paths are different memory-management contracts. | [Official architecture / weights](https://github.com/MoonshotAI/Kimi-K3) |
| **Kimi K3.1 Pro / Highspeed** (2026-10-23) | **Post-trained K3 variant**, not evidence of a new attention algorithm. Official Kimi technical note describes 1M context and a faster serving tier; as of Oct 24 full weights are *planned* for Nov 4. No kernel-level attribution for the advertised Highspeed gain. | [Official technical note](https://www.kimi.ai/blog/kimi-k3-1-pro) · [Official release documentation](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| **Mooncake** | KV-cache-centric disaggregated serving: Transfer Engine, distributed KV storage, and reusable state across instances; developed for Kimi. | [Official source](https://github.com/kvcache-ai/Mooncake) |
| **Kimi Linear** | Technical exploration of linear / hybrid attention with potential memory and decoding consequences. | [Official source](https://github.com/MoonshotAI/Kimi-Linear) |
| **Attention Residuals (AttnRes)** | Model architectural change to residual-stream propagation; affects inter-layer dependencies and fusion opportunities, but is not directly a serving runtime optimization. | [Official source](https://github.com/MoonshotAI/Attention-Residuals) |

**Evidence boundary:** K3.1 Pro is a product/model release with official technical context; it is not a new public KDA implementation or an independently measured kernel improvement. Keep Mooncake (serving infrastructure), KDA/AttnRes (architecture), and K3.1 post-training (capability) as separate layers.
