# Cloudflare / Workers AI

A **real serving operator** with unusually specific first-party material on cache locality, disaggregated inference, low-bit memory use and **KV lifecycle correctness**. Unlike generic provider API docs, some reports disclose real production failures and upstream engineering fixes.

[← Organizations](README.md)

## First-party engineering evidence

| Source | Reusable mechanism | Boundary |
|---|---|---|
| [High-performance LLMs on Workers AI](https://blog.cloudflare.com/high-performance-llms) (2026) | Documents workload-driven **P/D disaggregation** and input-heavy agent serving, where prefill and decode have different GPU resource needs. | Architecture from a production operator, not a full reproducible fleet benchmark or a Cloudflare-owned SGLang engine. |
| [Running Kimi / GLM at scale](https://blog.cloudflare.com/smaller-faster-safer-models/) (2026-08-03) | Layers **KV quantization, model-weight compression and cache protection** over disaggregated MoE serving. | Model/hardware-specific tradeoffs; memory savings and quantization may change numerical outputs. |
| [Prompt caching documentation](https://developers.cloudflare.com/workers-ai/features/prompt-caching/) | Explicit **session-affinity header** to improve co-location with cached prefix tensors, plus cached-token accounting. | Describes a public API/routing contract; exact internal KV layout and request placement policy are not all published. |
| [Cross-request KV exposure and SGLang remediation](https://blog.cloudflare.com/kv-cache-exposure-remediation/) (2026-10-26) | Documents a prefill rejection/transfer/decode admission mismatch that exposed stale cross-request KV pages; links coordinated upstream **SGLang v0.5.20–0.5.22** fixes covering admission, abort/acknowledgment and transfer/release lifecycle. | **Incident and remediation report**, not a generalized claim that current deployments leak; verify patched versions and model-specific configuration before inference. |
| [AI Gateway caching](https://developers.cloudflare.com/ai-gateway/features/caching/) | Caches completed response objects for identical requests at gateway layer. | **Response cache ≠ KV prefix cache**; do not combine hit metrics or exactness claims. |

## Research contract

A disaggregated engine must guarantee **request admission → KV ownership → transfer completion → safe release** across cancellation, overload and failure. Optimize with *both* TTFT/TPOT/Goodput and multi-tenant isolation/error-path testing. The engineering counterexample is more instructive than a speedup headline.

**Status:** production-operator engineering posts, public docs, community-upstream fix links; no local replication.
