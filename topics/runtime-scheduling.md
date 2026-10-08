# Runtime & Scheduling

Scheduling tokens, requests and model instances within online inference services to satisfy latency, utilization and fairness.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Use this class when a new request-level policy, queueing rule, or batching/routing mechanism is decisive; physical cluster separation belongs in Distributed.

**Foundational context.** See also: [Orca (2022), Sarathi-Serve (2024), Llumnix (2024), NanoFlow (2025)](../README.md#foundational-and-influential-papers).

## Newly admitted · October 2026 (1)

These entries have individually checked primary publication records. Descriptions summarize *the authors' mechanisms and evidence*; they do not imply independent reproduction, nor final adjudication of all earlier repository entries.

| Year | Paper | Venue | Distinct system mechanism |
|---|---|---|---|
| 2024 | [Fairness in Serving Large Language Models](https://www.usenix.org/conference/osdi24/presentation/sheng) | OSDI 2024 | Virtual Token Counter 把 Prefill/Decode 的 Token Cost 计入公平服务定义和连续批处理调度。 |

**Legacy cohort.** Previously collected Serving papers remain on [Serving Systems](serving-systems.md) pending individual re-admission/reclassification. A paper is not automatically admitted into this category based on a prior status flag.
