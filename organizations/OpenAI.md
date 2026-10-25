# OpenAI

Only **publicly documented inference-relevant model designs, execution tooling and interfaces** are listed. Public API availability does not disclose OpenAI's internal serving architecture.

[← Organizations](../README.md#organizations)

## Models and execution

| Work | Inference relevance | Official source |
|---|---|---|
| **gpt-oss (20B / 120B)** | Open-weight MoE reasoning models with documented quantized deployment and reference inference paths. | [Model + reference code](https://github.com/openai/gpt-oss) |
| **gpt-oss reference backends** | PyTorch, Triton and Metal inference implementations; examples are **reference implementations**, not a claim about OpenAI production serving. | [Inference implementations](https://github.com/openai/gpt-oss) |
| **GPT-4o** | Public low-latency multimodal interaction design and model capabilities; not a published kernel/serving architecture. | [Official announcement](https://openai.com/index/hello-gpt-4o/) |

## Infrastructure and interfaces

| Project | Role | Official source |
|---|---|---|
| **Triton** | GPU kernel language/compiler **originated at OpenAI**; now maintained as a wider open-source ecosystem project. | [GitHub](https://github.com/triton-lang/triton) |
| **Harmony** | Public serialization/conversation format, relevant to inference I/O and tool interaction, **not** a scheduler. | [GitHub](https://github.com/openai/harmony) |
| **tiktoken** | Tokenization library used in input processing and token budgeting. | [GitHub](https://github.com/openai/tiktoken) |

**Boundary.** No claims about unpublished model architecture, distributed inference topology, GPU fleet or internal batching policies. The Responses API is an external interface, not evidence of the underlying implementation.

## Official model-family / API listing (2026-10-24)

**Authority:** [OpenAI API model catalog](https://developers.openai.com/api/docs/models/all). These are **published product/model interfaces**, not a public specification of internal training, attention architecture or serving engines.

| Family | Named first-party models / inference relevance | Source |
|---|---|---|
| GPT-6 | **GPT-6 Astra; GPT-6.1 Sol; GPT-6 Sol; GPT-6 Luna** with distinct cost/effort/concurrency tiers | [Official model catalog](https://developers.openai.com/api/docs/models/all) |
| GPT-5.x | GPT-5.6 Sol / Terra / Luna and GPT-5.5, GPT-5.4, GPT-5.2 legacy families, including dated snapshots and coding-focused variants | [Official model catalog](https://developers.openai.com/api/docs/models/all) |
| gpt-oss | **gpt-oss-120b; gpt-oss-20b** open-weight MoE; code/backends and checkpoint-level evidence distinct from closed GPT-6 internals | [Official model repository](https://github.com/openai/gpt-oss) |
| GPT-Image | GPT-Image-2.5 Sunburst, GPT-Image-2.5 Flare, GPT-Image-2; image generation is outside autoregressive text serving | [Official model catalog](https://developers.openai.com/api/docs/models/all) |
| GPT-Live / Realtime / Audio | GPT-Live 1, Realtime-2.x/Mini/Translate, Audio-1.5, speech recognition/transcription; low-latency bidirectional audio workload | [Official model catalog](https://developers.openai.com/api/docs/models/all) |
| Embeddings and specialized | text-embedding-3-large/small, GPT-5.6 Cyber, GPT-Rosalind and task-specific models | [Official model catalog](https://developers.openai.com/api/docs/models/all) |

**Coverage limit:** the API supports many exact dated model strings and deprecations; the canonical model page is the complete live **endpoint registry**. Do not present consumer marketing names, alias IDs, publicly downloaded checkpoints or unpublished internal serving stacks as equivalent.
