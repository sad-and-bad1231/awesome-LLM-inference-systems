# MiniMax

**A multimodal foundation-model company building both general-purpose intelligence and AI-native products.** MiniMax is best read through **M-series reasoning/agent models → H-series video/image generation → Speech/Music → agent post-training and applications**. Its public inference story includes sparse attention and speculative decoding, but **the company is not simply a kernel or LLM-serving vendor**.

[← Organizations](README.md) · [← Home](../README.md) · [2026-11-13 primary-source audit](../reviews/MINIMAX_BYTEDANCE_PRIMARY_SOURCE_AUDIT_20261113.md)

## 1. The technology map

| Layer | Main work | Why it matters |
|---|---|---|
| **Foundation LLM / agents** | [M3.1-Flash](https://www.minimax.io/blog/minimax-m31f) · [M3](https://github.com/MiniMax-AI/MiniMax-M3) · M2.7 / M2.5 / M2 / [M1](https://github.com/MiniMax-AI/MiniMax-M1) / MiniMax-01 | Coding, long-horizon agents, native multimodal *understanding* and long-context modeling. |
| **Video & omni generation** | [H3](https://github.com/MiniMax-AI/MiniMax-H3) · Hailuo 2.3 / 02 and predecessors | Multimodal-conditioned video with audio; multi-stage generation rather than autoregressive text serving. |
| **Image generation** | [H3-Image (Nov 11)](https://www.minimax.io/blog/minimax-h3-image) · older image models | Reference-based generation/editing, high-resolution visual output and open weights for H3-Image. |
| **Speech & music** | [Speech 2.8](https://www.minimax.io/news/minimax-speech-28) · [Music 3.0](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model) | Speech creation/voice styles and structured music generation, with distinct latency and synthesis workloads. |
| **Post-training / reasoning research** | [M1 / CISPO](https://github.com/MiniMax-AI/MiniMax-M1) · [Forge agent RL](https://www.minimax.io/blog/forge-scalable-agent-rl-en-1779896141) · [MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution) · [SynLogic / Visual RL](https://github.com/MiniMax-AI/MiniMax-AI.github.io) | Long-reasoning training, agent RL, verifiable reasoning-data construction and visual-reasoning RL. |
| **Inference architecture** | [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392) · M3.1 QAT and DSpark · H3 latent/Omni Transformer | Publicly described efficiency ideas spanning long-context KV traffic, speculation, quantization and staged media generation. |
| **AI-native products / APIs** | [MiniMax Code / Design](https://www.minimax.io/about) · [MiniMax Agent / Agent Team](https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953) · Hailuo AI · MiniMax Audio · Talkie · [Open Platform](https://platform.minimax.io/docs/) | Product demand spans coding, work agents, creative video, voices, companionship and developer integration; **products are not proof of published serving internals**. |

**Fast orientation:** MiniMax's distinguishing feature is a broad, internally developed multimodal model portfolio coupled to consumer/creator/agent products. The technical systems signals most directly visible to an inference engineer are **MSA, DSpark/QAT and the H3 generation pipeline**; **Forge and Agent Team** explain its agent-RL and product-engineering direction.

## 2. Major model families — complete the map, not every API revision

| Family | Public lineage and main contribution | Official entry |
|---|---|---|
| **M-series (text and multimodal understanding)** | **MiniMax-01 → M1 → M2/M2.1/M2.5/M2.7 → M3/M3.1-Flash**. MiniMax-01 established the Lightning Attention lineage; **M1** publicly documented hybrid attention, long-reasoning test-time scaling and CISPO RL; M3/M3.1 move toward indexed MSA and DSpark/QAT. | [Research chronology](https://www.minimax.io/blog) · [M1 source](https://github.com/MiniMax-AI/MiniMax-M1) · [M3](https://github.com/MiniMax-AI/MiniMax-M3) · [M3.1 model card](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) |
| **H-series / Hailuo (video, native audio-video)** | Hailuo 01/02/2.3 are the earlier video-product lineage; **H3** publicly exposes a unified 33B Omni Transformer and staged audio-video generation with up to 2K regeneration. | [H3 research](https://www.minimax.io/blog/minimax-h3) · [H3 repository](https://github.com/MiniMax-AI/MiniMax-H3) |
| **Image** | **H3-Image**, released with open weights on Nov 11, emphasizes generation/editing, references and high-resolution output. | [Launch](https://www.minimax.io/blog/minimax-h3-image) · [weights](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) |
| **Speech** | **Speech 2.8 HD/Turbo** and earlier speech families emphasize expressive TTS, voice identity and audio creation; HD/Turbo are service variants unless separate architectures are documented. | [Official release](https://www.minimax.io/news/minimax-speech-28) · [developer docs](https://platform.minimax.io/docs/) |
| **Music** | **Music 3.0** uses a global–local Hybrid-LM with structured/acoustic representation and waveform generation for longer composition. | [Technical release](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model) |

For **text output**, investigate TTFT/TPOT and long-context performance; for **audio/video/image generation**, reason about startup delay, stage latency, generated duration/resolution and output quality. Do not compare their advertised performance on a single text-token TPS scale.

## 3. Research direction beyond the flagship models

- **Reasoning and visual RL lineage:** [MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1) introduces CISPO RL for its hybrid-attention reasoning model; the team's [official publication pointers](https://github.com/MiniMax-AI/MiniMax-AI.github.io) also list **SynLogic** (verifiable synthetic reasoning data) and **One-RL-to-See-Them-All** (visual RL). These represent research directions, not independently proven online-serving optimizations.
- **Agent learning and long-horizon systems:** [Forge](https://www.minimax.io/blog/forge-scalable-agent-rl-en-1779896141) is a published description of the team's internal scalable agent-RL framework, involving environment/task diversity, asynchronous orchestration and training–inference co-design. It is **agent training infrastructure**, not an independently published production LLM inference engine.
- **Reasoning, verification and evolution:** [MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution) combines mathematical proof generation, verification and iterative search. MiniMax has also discussed [M2.7 self-evolution research](https://www.minimax.io/blog); these should not be conflated with released autonomous kernel optimization or recursive improvement of an inference server.
- **Product/agent orchestration:** [MiniMax Agent Team](https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953) documents leader/worker/verifier roles and stateful long-task execution. This is an **agent application runtime / harness**, not a GPU scheduler.
- **Long-context and multimodal modeling:** [MSA](https://arxiv.org/abs/2606.13392) and [H3](https://github.com/MiniMax-AI/MiniMax-H3) supply inspectable model-level execution contracts; separate model accuracy and service-level performance.

## 4. Public inference infrastructure and deployment boundary

| Public surface | Established scope | Important boundary |
|---|---|---|
| [M3/M3.1 model and deployment guidance](https://github.com/MiniMax-AI/MiniMax-M3) | Sparse-attention model, deployment recipes mentioning vLLM/SGLang/Transformers/KTransformers; DSpark/QAT described in [M3.1](https://www.minimax.io/blog/minimax-m31f) | Neither the existence of model weights nor published speed claims proves a reusable MiniMax-owned complete production serving engine, or a tested Ascend 910B2 path. |
| [H3 weights/repository](https://github.com/MiniMax-AI/MiniMax-H3) | Omni Transformer, visual/audio VAE, self-host options including diffusion-serving frameworks | Initial public inference provides **full attention**; the hosted **H3-Context-IR** pipeline and native sparse-attention implementation are **not** part of that initial public release. |
| [MiniMax developer platform](https://platform.minimax.io/docs/) | Hosted text, image/video, speech and music API contracts, developer access | A model endpoint/service tier is not a disclosed internal router, P/D implementation, GPU kernel or independent benchmark. |

## 5. Products and reading order

**Products connect the research lines:** [MiniMax Code / Design](https://www.minimax.io/about) and [Agent Team](https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953) express its work-agent path; [Hailuo](https://hailuoai.video/) is the creator-facing video route; [MiniMax Audio](https://www.minimax.io/about) and [Talkie](https://www.minimax.io/about) illustrate expressive speech and interactive entertainment; the [API platform](https://platform.minimax.io/docs/) exposes selected families to developers. Product availability and naming vary by market and date; refer to the current first-party catalogs.

**Suggested overview order:** [company/product map](https://www.minimax.io/about) → [research chronology](https://www.minimax.io/blog) → [M3/M3.1](https://github.com/MiniMax-AI/MiniMax-M3) → [H3](https://github.com/MiniMax-AI/MiniMax-H3) → [Forge](https://www.minimax.io/blog/forge-scalable-agent-rl-en-1779896141). Deeper kernel/performance study is **not** a prerequisite to understanding the company.

**Source boundaries (2026-11-13):** First-party architecture, repository and commercial API evidence are distinguished; vendor performance is not independently reproduced; no claims are made about unpublished full production infrastructure or Ascend support. Organization navigation only: **no new canonical paper entries**.
