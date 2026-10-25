# Moonshot AI / Kimi

Moonshot AI/Kimi's model architecture and **production-oriented KV-cache infrastructure**.

[← Organizations](README.md) · [← Home](../README.md)

## Official model-family and live API ID crosswalk (2026-10-24)

**Authoritative current source:** [Kimi Code model configuration](https://www.kimi.com/code/docs/en/kimi-code/models). It explicitly exposes **six model IDs**, but they map to fewer underlying model versions.

| Official model ID | Model version / distinction | Source |
|---|---|---|
| `k3.1-pro` | **K3.1 Pro**, new 3T-class long-context flagship; K3.1 family follows K3, but no architecture-level change should be assumed without a technical source | [Official Kimi Code models](https://www.kimi.com/code/docs/en/kimi-code/models) |
| `k3.1-pro-highspeed` | K3.1 Pro high-speed **serving tier**, same declared model quality; no public Kernel-level speed attribution | [Official Kimi Code models](https://www.kimi.com/code/docs/en/kimi-code/models) |
| `k3` | K3, 2.8T MoE, up to 1M context; published KDA/Gated MLA/AttnRes mechanics | [K3 official code](https://github.com/MoonshotAI/Kimi-K3) |
| `k3-256k` | K3 with 256K context quota, not a new model architecture | [Official Kimi Code models](https://www.kimi.com/code/docs/en/kimi-code/models) |
| `kimi-for-coding` | K2.8 Preview, alias routes to this current coding model | [Official Kimi Code models](https://www.kimi.com/code/docs/en/kimi-code/models) |
| `kimi-for-coding-highspeed` | K2.7 Code Highspeed, different underlying version from K2.8; don't alias it to K3 | [Official Kimi Code models](https://www.kimi.com/code/docs/en/kimi-code/models) |
| Historical Kimi K2 / K2.5 / Kimi Linear | Distinct MoE and recurrent/hybrid-attention research lineage; retained as architecture context, *not* entries in current six-ID Kimi Code catalog | [Kimi-K2 official repo](https://github.com/MoonshotAI/Kimi-K2) · [Kimi Linear](https://github.com/MoonshotAI/Kimi-Linear) |

**Stateful systems relevance:** [Mooncake](https://github.com/kvcache-ai/Mooncake) (KV transfer/service) vs KDA recurrent state and Gated MLA (model-internal caches) vs Kimi Code's API IDs (service routing) are three separate concepts.

## Selected first-party architecture and execution sources

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Kimi-K2** | Open model family with sparse expert execution and long-running generation serving implications. | [Official source](https://github.com/MoonshotAI/Kimi-K2) |
| **Kimi-K3** (2026) | Open 2.8T MoE with 104B activated; **69 KDA + 24 Gated MLA** attention layers, Attention Residuals (AttnRes), Stable LatentMoE, 1M context and MXFP4/MXFP8 quantized execution. Recurrent state and KV-cache paths are different memory-management contracts. | [Official architecture / weights](https://github.com/MoonshotAI/Kimi-K3) |
| **Kimi K3.1 Pro / Highspeed** (2026-10-23) | **New K3.1-series release**: the launch alone does not prove a newly published attention mechanism; the Highspeed option is a serving tier. Official Kimi technical note describes 1M context and a faster serving tier; as of Oct 24 full weights are *planned* for Nov 4. No kernel-level attribution for the advertised Highspeed gain. | [Official technical note](https://www.kimi.ai/blog/kimi-k3-1-pro) · [Official release documentation](https://www.kimi.com/code/docs/en/kimi-code/whats-new.html) |
| **Mooncake** | KV-cache-centric disaggregated serving: Transfer Engine, distributed KV storage, and reusable state across instances; developed for Kimi. | [Official source](https://github.com/kvcache-ai/Mooncake) |
| **Kimi Linear** | Technical exploration of linear / hybrid attention with potential memory and decoding consequences. | [Official source](https://github.com/MoonshotAI/Kimi-Linear) |
| **Attention Residuals (AttnRes)** | Model architectural change to residual-stream propagation; affects inter-layer dependencies and fusion opportunities, but is not directly a serving runtime optimization. | [Official source](https://github.com/MoonshotAI/Attention-Residuals) |

**Evidence boundary:** K3.1 Pro is a product/model release with official technical context; it is not a new public KDA implementation or an independently measured kernel improvement. Keep Mooncake (serving infrastructure), KDA/AttnRes (architecture), and K3.1 post-training (capability) as separate layers.
