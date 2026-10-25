# Anthropic

Anthropic publishes **model-family tradeoffs and serving API behavior**, but comparatively little public detail about its internal inference kernels or scheduler. This distinction is intentional.

[← Organizations](../README.md#organizations)

## Official Claude model-family / API catalog (2026-10-24)

The [Claude Platform model overview](https://platform.claude.com/docs/en/models/overview) is the authority for active models, platform-specific IDs, retirement schedules and caching/effort specifications.

| Model line | Current named model / status | Primary source |
|---|---|---|
| Claude Fable | **Fable 5.1**, current demanding-reasoning/long-agent tier; older Fable 5 historical | [Claude official model table](https://platform.claude.com/docs/en/models/overview) |
| Claude Opus | **Opus 5.5**, current long-horizon reasoning tier; previous Opus 5/4.8/4.7/4.6 historical | [Claude official model table](https://platform.claude.com/docs/en/models/overview) |
| Claude Sonnet | **Sonnet 5.5**, current speed/intelligence compromise; previous Sonnet 5/4.x historical | [Claude official model table](https://platform.claude.com/docs/en/models/overview) |
| Claude Haiku | **Haiku 5.5**, current low-latency tier; earlier Haiku 4.5/3 historical | [Claude official model table](https://platform.claude.com/docs/en/models/overview) |
| Claude Mythos | Mythos 5/5.1 **restricted availability**, not a universal public-serving model | [Official Claude model documentation](https://platform.claude.com/docs/en/models/overview) |

**Systems evidence rule:** context, pricing, caching, Batch, reasoning effort and latency expose a model's **client-visible execution contract** only. Claude scheduler, attention kernels and cluster topology remain undocumented; no inference-system claims from API menus.

## Models and observable inference characteristics

| Work | Inference relevance | Official source |
|---|---|---|
| **Claude 3: Haiku / Sonnet / Opus** | A documented family spanning different latency, cost and capability profiles; no public disclosure of implementation-level serving internals. | [Official announcement](https://www.anthropic.com/news/claude-3-family) |
| **Claude 3 Haiku** | Latency/throughput-oriented model option; reported product performance is not independently reproduced here. | [Official announcement](https://www.anthropic.com/news/claude-3-haiku) |
| **Extended / adaptive thinking** | Variable reasoning-token workloads relevant to latency and serving budget, **not** a documented inference acceleration algorithm. | [Platform documentation](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) |

## Public API infrastructure

| Feature | Meaning for systems readers | Official source |
|---|---|---|
| **Prompt caching** | Public API feature for reusable prompt prefixes and cache lifetimes; internal KV implementation is **not** disclosed. | [Platform documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) |
| **Message Batches** | Asynchronous bulk inference API; documents the interface, not an internal scheduler. | [API reference](https://platform.claude.com/docs/en/api/messages/batches/create) |

**Boundary.** Do not infer KV layout, quantization strategy, request placement, or prefill/decode architecture from the existence of a commercial feature.
