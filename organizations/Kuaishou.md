# Kuaishou / Kwai

Distinct public evidence for **multimodal model execution requirements** and **a commercial inference service surface**. The team's hosted portfolio is not evidence that it invented all underlying model-server kernels.

[← Organizations](README.md)

## Verified public signals

| Official source | Inference concern | Evidence boundary |
|---|---|---|
| [Keye-VL 2.0](https://github.com/Kwai-Keye/Keye) (2026 model source) | 30B-class / 3B-active visual-language MoE with DSA-style sparse attention and a published 256K long-video context target; specialized encoding, indexer and KV workload. | **Model architecture and release**, not a newly disclosed Kuaishou production serving engine. Distinguish Keye-owned checkpoints from third-party models hosted by StreamLake. |
| [StreamLake Vanchin model deployment](https://www.streamlake.com/document/WANQING/mf6l61u2aijzj4m3ly8) (service docs) | Dedicated online model deployments, resource isolation, elastic scaling and endpoint management. | An **API/product contract**, not source for the internal scheduler, model placement or GPU kernels. |
| [Vanchin explicit context cache](https://streamlake.com/document/WANQING/mkxypaeruepm2t9mp78) (service docs) | Explicit reusable-prefix cache creation and expiration for repeated system prompts and multi-turn workloads. | User-facing cache API semantics do not reveal the exact memory format, KV transport or eviction implementation. |
| [Vanchin release notes](https://www.streamlake.com/document/WANQING/mdptalisb06i7ai3zdd) (2026) | Publishes cache-hit counters and prompt/completion token observability in inference endpoints. | Monitoring capability is not an independent throughput result or unique cache algorithm. |

## Research reading angle

Keye motivates **long-video sparse attention** serving; Vanchin supplies a real **MaaS resource isolation, caching and observability** contract. Compare cache-hit accounting, session/tenant isolation, multimodal prompt cost and platform SLOs. Do not equate hosted model availability with first-party model engineering.

**Status:** official model code and product documentation; independent engine source not established in reviewed material.
