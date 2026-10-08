# Anthropic

Anthropic publishes **model-family tradeoffs and serving API behavior**, but comparatively little public detail about its internal inference kernels or scheduler. This distinction is intentional.

[← Organizations](../README.md#organizations)

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
