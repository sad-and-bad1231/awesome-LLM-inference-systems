# ByteDance

ByteDance/Seed open research releases and low-level Transformer execution, rather than the undisclosed internals of commercial services.

[← Organizations](README.md) · [← Home](../README.md)

## Official Seed model portfolio crosswalk (2026-10-24)

[Seed's official model portfolio](https://seed.bytedance.com/zh/seed_model_portfolio) is the completeness source; [current featured models](https://seed.bytedance.com/zh/models) distinguish model research from text-LLM serving. Volcengine Ark has additional dated API snapshots.

| Official family | Modality / inference relevance | Primary source |
|---|---|---|
| Seed2.1 (Pro / Turbo / Lite service variants) | Agent/Coding-oriented foundation generation, distinct model tiers and API resource profiles | [Seed model portfolio](https://seed.bytedance.com/zh/models) · [Ark model list](https://docs.volcengine.com/docs/ark/model-list?lang=zh) |
| Seed2.0 / Seed1.8 / Seed1.6 / Seed1.5 / Seed1.5-VL | Full publicly listed historical foundation-family lineage, including multimodal VL | [Official Seed portfolio](https://seed.bytedance.com/zh/seed_model_portfolio) |
| Seed Diffusion Preview | **Diffusion language modeling**, materially different iterative decoding workload | [Official Seed portfolio](https://seed.bytedance.com/zh/seed_model_portfolio) |
| Seedance 2.5 / Seedream 5.0 Pro | Current video/image generative family; media diffusion, **not** autoregressive text serving | [Official current models](https://seed.bytedance.com/zh/models) |
| SeedRealtime / Seed Audio 1.0 | Full-duplex audio-video streaming and audio generation; real-time multimodal serving | [Official current models](https://seed.bytedance.com/zh/models) |
| Seed GR-3 / Seed GR-RL | Embodied/VLA and robotics-related methods (GR-RL is an RL framework, **not** a standalone inference model) | [Official Seed portfolio](https://seed.bytedance.com/zh/models) |
| Protenix | AI-for-science protein foundation model, beyond current text inference mainline | [Official Seed portfolio](https://seed.bytedance.com/zh/models) |
| Doubao-Seed-Evolving / Seed-Code / Seed-Translation | Ark-hosted service families; model-routing/endpoint labels should not be promoted to distinct new architectures without technical reports | [Volcengine model catalog](https://docs.volcengine.com/docs/ark/model-list?lang=zh) |

**Scope:** the official portfolio includes model families across GenMedia, Robotics and AI4Science; they appear here for completeness, but only execution-relevant work warrants a canonical LLM-inference paper admission.

## Selected first-party architecture and execution sources

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Seed-OSS** | Official long-context model family with GQA and a controllable reasoning budget; model capability, **not** a new serving system. | [Official source](https://github.com/ByteDance-Seed/seed-oss) |
| **ByteTransformer** | Transformer inference optimization and operator implementation; historical engineering reference. | [Official source](https://github.com/bytedance/ByteTransformer) |
| **ByteIR** | ML compiler infrastructure and intermediate representation; included as compiler substrate, not necessarily an online serving stack. | [Official source](https://github.com/bytedance/ByteIR) |
