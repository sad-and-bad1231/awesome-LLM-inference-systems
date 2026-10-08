# KV Cache & Context Memory

Inference-time state: cache reuse, placement, offloading, compression, eviction and recovery.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Memory-state mechanisms lead this category; if the main contribution is where prefill/decode runs across GPUs, use Distributed Serving.

**Foundational context.** See also: [PagedAttention/vLLM (2023), Mooncake (2025), Strata (2026)](../README.md#foundational-and-influential-papers).
## Papers (18)

A selective, chronological bibliography; each paper's principal mechanism determines its only full-topic entry. See [curation criteria](../CURATION.md) and the [migration record](serving-systems.md) for historical changes.

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2023 | [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html) | NeurIPS 2023 | 基于注意力重尾分布识别 Heavy-Hitter KV，并与 Recent Token 构建高效保留策略。 |
| 2024 | [CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving](https://doi.org/10.1145/3651890.3672274) | SIGCOMM 2024 | 基于上下文传输的 KV Cache 压缩与流式发送，优化远端缓存加载关键路径。 |
| 2024 | [Efficient Streaming Language Models with Attention Sinks](https://openreview.net/forum?id=NG7sS51zVF) | ICLR 2024 | Attention Sinks + 滑动窗口缓存使长流式生成无需反复重计算完整上下文。 |
| 2024 | [InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management](https://www.usenix.org/conference/osdi24/presentation/lee) | OSDI 2024 | 预测关键 KV 项并按需预取，避免长上下文 Offloading 的全量回传。 |
| 2024 | [Keyformer: KV Cache reduction through key tokens selection for Efficient Generative Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/48fecef47b19fe501d27d338b6d52582-Abstract-Conference.html) | MLSys 2024 | 以关键 Token 选择压缩 KV 访存；同时评估生成性能与质量，属于近似状态保留而非精确缓存。 |
| 2024 | [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](https://proceedings.mlr.press/v235/liu24bz.html) | ICML 2024 | 根据 K/V 分布差异实行 Key 按通道和 Value 按 Token 量化，低精度保留推理状态。 |
| 2024 | [KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization](https://proceedings.neurips.cc/paper_files/paper/2024/hash/028fcbcf85435d39a40c4d61b42c99a4-Abstract-Conference.html) | NeurIPS 2024 | 针对 KV Outlier 和分布设计非均匀低比特量化，加速极长上下文 Decode。 |
| 2024 | [Prompt Cache: Modular Attention Reuse for Low-Latency Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html) | MLSys 2024 | 通过显式 Prompt Module 与位置约束实现跨请求 Attention State 复用，降低重复前缀处理。 |
| 2024 | [Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference](https://proceedings.mlr.press/v235/tang24l.html) | ICML 2024 | 按当前 Query 粗筛 KV Page 再精确算 Attention，降低长上下文 Decode 访存量。 |
| 2024 | [SnapKV: LLM Knows What You are Looking for Before Generation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/28ab418242603e0f7323e54185d19bde-Abstract-Conference.html) | NeurIPS 2024 | 通过观察窗口中的 Head-specific 重要位置，压缩未来 Decode 要保留的 KV。 |
| 2025 | [CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion](https://doi.org/10.1145/3689031.3696098) | EuroSys 2025 | 支持非连续知识块 KV 复用，降低 RAG 请求的 Prefill 重计算。 |
| 2025 | [Fast State Restoration in LLM Serving with HCache](https://doi.org/10.1145/3689031.3696072) | EuroSys 2025 | 以中间激活恢复状态，配合无 Bubble 调度与分块存储平衡计算/I/O。 |
| 2025 | [Marconi: Prefix Caching for the Era of Hybrid LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/7c180af017258d239bac6248d1eb26ac-Abstract-Conference.html) | MLSys 2025 | 针对 Attention+SSM 共同维护的状态建立收益感知 Cache Admission/Eviction。 |
| 2025 | [PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://www.microsoft.com/en-us/research/publication/pyramidkv-dynamic-kv-cache-compression-based-on-pyramidal-information-funneling/) | COLM 2025 | 以分层信息汇聚规律分配不同层的 KV Budget，避免统一保留比例的低效。 |
| 2025 | [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://proceedings.mlr.press/v267/behnam25a.html) | ICML 2025 | 先永久裁剪 KV 再作细粒度 Query-aware 稀疏访问，提供可执行的长上下文 Decode 加速。 |
| 2025 | [Stateful Large Language Model Serving with Pensieve](https://doi.org/10.1145/3689031.3696086) | EuroSys 2025 | 面向会话延续的状态管理与复用，避免每轮请求重复加载/重算上下文。 |
| 2026 | [ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs](https://www.usenix.org/conference/osdi26/presentation/liu-guangda) | OSDI 2026 | 原生 Sparse Attention 的图兼容 KV 淘汰与无损预测预取，把 Recall 与 Indexer 计算流水重叠。 |
| 2026 | [No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs](https://www.usenix.org/conference/osdi26/presentation/luo) | OSDI 2026 | DirectKV 以 Zero-copy 数据路径取消 Offloading Buffer 拷贝与冗余显存。 |

*Venue and mechanisms follow primary publication material; authors' experimental claims are not independently reproduced.*
