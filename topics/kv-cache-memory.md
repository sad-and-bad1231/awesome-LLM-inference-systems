# KV Cache & Context Memory

Inference-time state: cache reuse, placement, offloading, compression, eviction and recovery.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Memory-state mechanisms lead this category; if the main contribution is where prefill/decode runs across GPUs, use Distributed Serving.

**Foundational context.** See also: [PagedAttention/vLLM (2023), Mooncake (2025), Strata (2026)](../README.md#foundational-and-influential-papers).

## Newly admitted · October 2026 (3)

These entries have individually checked primary publication records. Descriptions summarize *the authors' mechanisms and evidence*; they do not imply independent reproduction, nor final adjudication of all earlier repository entries.

| Year | Paper | Venue | Distinct system mechanism |
|---|---|---|---|
| 2024 | [Keyformer: KV Cache reduction through key tokens selection for Efficient Generative Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/48fecef47b19fe501d27d338b6d52582-Abstract-Conference.html) | MLSys 2024 | 以关键 Token 选择压缩 KV 访存；同时评估生成性能与质量，属于近似状态保留而非精确缓存。 |
| 2024 | [Prompt Cache: Modular Attention Reuse for Low-Latency Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html) | MLSys 2024 | 通过显式 Prompt Module 与位置约束实现跨请求 Attention State 复用，降低重复前缀处理。 |
| 2026 | [ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs](https://www.usenix.org/conference/osdi26/presentation/liu-guangda) | OSDI 2026 | 原生 Sparse Attention 的图兼容 KV 淘汰与无损预测预取，把 Recall 与 Indexer 计算流水重叠。 |

**Legacy cohort.** Previously collected Serving papers remain on [Serving Systems](serving-systems.md) pending individual re-admission/reclassification. A paper is not automatically admitted into this category based on a prior status flag.
