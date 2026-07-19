# AI Inference Papers

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Industry systems](../industry/README.md)

A complete academic paper collection organized by serving-system abstraction. Formal venues, posters/workshops, preprints, and legacy imports are labeled separately.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. A bounded rolling exploration section keeps new workloads visible; the full adjacent/archive history remains in the [archive](../archive/README.md).

## At a Glance

| Records | Formal venue | With artifact | Tagged records |
|---:|---:|---:|---:|
| 241 | 111 | 22 | 232 |

## Collection Navigation

- [Attention / Kernel](#attention-kernel) (6)
- [KV Cache](#kv-cache) (59)
- [Prefill–Decode 与传输](#prefill-decode) (26)
- [Speculative Decoding](#speculative-decoding) (23)
- [MoE](#moe) (34)
- [Compiler / DSL](#compiler-dsl) (3)
- [Runtime / Scheduling](#runtime-scheduling) (90)
- [探索观察](#探索观察) (18)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |
| Scope | `core` records form the seven main themes; a bounded `adjacent` window appears under exploration, with full adjacent/archive history on the archive page. |
| Featured | A small editorial starting set; all core records remain below. |

## Resource List

### Attention / Kernel (6)

#### Featured

- **Featured:** **vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention**
  `ASPLOS 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `cuda` `kernel` `memory`
  vAttention 通过 CUDA virtual memory 保留连续虚拟 KV layout，同时按需分配物理页，避免重写 attention kernel。
#### Full Resource List

- **Efficient Memory Management for Large Language Model Serving with PagedAttention**
  `SOSP 2023` · `2023` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kv-cache` `memory` `vllm`
  vLLM/PagedAttention 用块式虚拟内存管理 KV cache，显著减少碎片并支持 beam search、parallel sampling 和前缀共享。
- **FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `hopper` `kv-cache` `quantization`
  FlashAttention-3 利用 Hopper TMA、warp specialization 和 FP8 block quantization 重叠数据移动、matmul 与 softmax。
- **FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kernel`
  FlashAttention-4 针对非对称硬件扩展重做 attention 算法和 kernel pipeline 协同设计，提高长上下文与大模型注意力吞吐。
- **I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  该工作从 I/O 复杂度而非 FLOPs 分析长序列 attention，指导算法与硬件在数据搬运瓶颈下协同优化。
- **FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kernel`
  FastTree 为 radix-tree KV 共享设计专用 attention kernel，并在 runtime 中自适应划分共享上下文查询组。

### KV Cache (59)

#### Featured

- **Featured:** **[MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing](https://openreview.net/forum?id=1JyePezdlF)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `decode` `gpu` `cuda` `compression` `kv-cache` `long-context` `vllm`
  Artifact: [source](https://arxiv.org/abs/2506.02006)
  MorphServe 以反馈控制方式在运行时联合调整量化层和 KV cache 容量：高压时异步换入低精度层并弹性扩缩 KVC，压力恢复后再切回；在 Vicuna/Llama 和真实 workload 上平均 SLO 违规降低 92.45%，P95 TTFT 相较全精度 serving 改善 2.2x–3.9x，并保持生成质量。
#### Full Resource List

- **A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints**
  `ICML 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  该工作把计算和 KV cache 显存同时纳入排队稳定性分析，给出 LLM inference 系统何时会因内存约束失稳的理论条件。
- **Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs**
  `ICLR 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  TRIM-KV 在 token 生成时预测长期保留价值，并随时间衰减以在固定内存预算下保留最有用的 KV。
- **[DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants](https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `npu` `kv-cache` `agent` `edge` `throughput`
  Compound AI systems, such as agentic systems, are an emerging trend in large-scale enterprise settings, with multiple LLMs specialized for different users, tasks, and/or roles working together. In these scenarios, different models often pr…
- **[ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs](https://www.usenix.org/conference/osdi26/presentation/liu-guangda)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `kv-cache`
  针对 native sparse attention 下随上下文增长的 KV 容量瓶颈，设计 GPU graph-friendly cache manager、无损 decode/prefill prefetch 和融合 GPU kernel；官方 OSDI 2026 页面报告长上下文下相对 SGLang/vLLM generation throughput 最高提升 2.1 倍。
- **[FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management](https://openreview.net/forum?id=GgX6dPJx9M)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `compression` `kv-cache` `rag`
  FlexiCache 利用 attention head 重要性的时间稳定性动态管理 KV cache，减少长上下文生成中不必要的保留和加载。
- **KV Cache Transform Coding for Compact Storage in LLM Inference**
  `ICLR 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `rag`
  KVTC 借鉴媒体压缩，用 PCA 去相关、自适应量化和熵编码压缩可复用 KV cache。
- **KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving**
  `SIGCOMM 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `compression` `kv-cache` `slo`
  KVServe 用 Bayesian profiling 建立压缩策略 Pareto 集，并由在线 controller 按 workload、网络、SLO 和质量约束选择 KV 传输压缩方案。
- **[KVSwap: Disk-aware KV Cache Offloading for Long-Context On-device Inference](https://www.sigmobile.org/mobisys/2026/program/#kvswap-disk-aware-kv-cache-offloading-for-long-context-on-device-inference)**
  `MobiSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `serving` `gpu` `edge` `kv-cache` `memory` `long-context` `throughput`
  Artifact: [source](https://eprints.whiterose.ac.uk/id/eprint/240121/1/kvswap.pdf)
  KVSwap 针对统一内存的移动/嵌入式设备，将完整 KV cache 放到磁盘，仅在 RAM 保留低秩 K 元数据预测下一层关键 token，并以连续磁盘访问和异步 I/O 与计算重叠；MobiSys 评审确认其在 NVIDIA Jetson 上相较既有 offloading 方案提升紧内存预算下吞吐。
- **Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `quantization`
  Kitty 用动态 channel-wise precision boost 和 page-centric layout 实现接近 2-bit 的 KV cache 压缩，同时保持规则访存和解量化效率。
- **LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `lmcache`
  LMCache 将 KV cache 抽象为独立可复用层，支持跨请求、跨 engine、跨存储层的 KV offload、传输和复用。
- **[No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs](https://www.usenix.org/conference/osdi26/presentation/luo)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `gpu` `cuda` `kernel` `kv-cache` `long-context` `latency`
  Artifact: [source](https://github.com/shutianluo/DirectKV)
  DirectKV 在 NVIDIA GH200/GB200 的 NVLink-C2C 平台上实现零拷贝 KV offloading：GPU kernel 直接访问 CPU-resident KV，结合 CPU-aware tiling、warp pipeline 与 kernel fusion；相较既有方案最多减少 50% CPU-GPU 传输、降低 43% GPU 内存并提升端到端性能 1.2x。
- **[OPKV: A High-Throughput Plugin-Driven Framework for Recallable Sparsity in Paged KV Cache Systems](https://openreview.net/forum?id=EB5bgzv4qA)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `kv-cache` `throughput`
  OPKV 为 paged KV cache 提供可插拔稀疏召回框架，使不同稀疏策略能在高吞吐 serving runtime 中复用同一数据通路。
- **REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `kv-cache`
  REPA 用可重构 PIM 同时加速 KV cache 的卸载传输与就地处理，减少长上下文推理的数据移动。
- **[ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](https://iclr.cc/virtual/2026/poster/10009980)**
  `ICLR 2026 Oral` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `compiler` `compression` `throughput`
  ThinKV combines thought-aware low-bit quantization and progressive KV eviction with a PagedAttention extension kernel; the official evaluation keeps less than 5% of the original cache and reports up to 5.8x higher throughput.
- **[UniCache: Unifying Prefix Cache Eviction for Heterogeneous LLM Serving Workloads](https://www.sigmetrics.org/sigmetrics2026/accepted.html#unicache-unifying-prefix-cache-eviction-for-heterogeneous-llm-serving-workloads)**
  `ACM SIGMETRICS 2026 official accepted papers` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `gpu` `kv-cache` `scheduler` `heterogeneous` `multi-turn` `vllm`
  Artifact: [source](https://jxing.me/pdf/unicache-sigmetrics26.pdf)
  针对异构多轮与单轮 workload 下 prefix reuse 模式不同的问题，设计统一的 task-aware eviction policy，并在 vLLM 中实现；公开评测报告 prefix-cache hit rate 最高提升 17.32%，推理延迟最高降低 3.63 倍。该条目为 SIGMETRICS 2026 formal abstract/proceedings 记录。
- **Which Heads Matter for Reasoning? RL-Guided KV Cache Compression**
  `ICML 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `compression` `kv-cache`
  RLKV 用强化学习探针识别对推理链关键的注意力头，并优先保留这些头的 KV cache 来压缩长 CoT 推理开销。
- **Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving**
  `SoCC 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `kv-cache`
  Oneiros 通过参数重映射提高不同 tenant 间 KV cache 的兼容和复用能力。
- **RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression**
  `ICML 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `compression` `kv-cache` `long-context`
  RocketKV 先粗粒度永久淘汰输入 KV token，再用动态稀疏注意力进行细粒度 top-k 选择以加速长上下文解码。
- **ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference**
  `ICML 2025 Spotlight` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `kv-cache` `long-context` `throughput`
  ShadowKV 在 GPU 侧保留低秩 keys、landmarks 和少量 outliers，并按需从 CPU DRAM 拉取匹配 value 以提升长上下文吞吐。
- **[FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference](https://iclr.cc/virtual/2026/poster/10006722)**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop` · `Reading priority: frontier`
  Tags: `serving` `gpu` `compiler` `kernel`
  FreeKV moves KV selection off the critical path with speculative retrieval, hybrid CPU/GPU layouts, and double-buffered streaming, reporting up to 13x speedup with near-lossless quality.
- **[LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation](https://iclr.cc/virtual/2026/poster/10009483)**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop` · `Reading priority: frontier`
  Tags: `compression` `kv-cache`
  LookaheadKV predicts future KV importance with lightweight parameter-efficient modules, avoiding draft generation while retaining the accuracy benefits of future-aware eviction at negligible runtime overhead.
- **[LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences](https://iclr.cc/virtual/2026/poster/10011378)**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop` · `Reading priority: frontier`
  Tags: `decode` `serving` `npu` `tpu` `kv-cache`
  LouisKV exploits temporal locality and different input/output KV distributions, triggering retrieval at semantic boundaries and using decoupled fine-grained cache management for long reasoning sequences.
- **InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache` `memory`
  InfiniGen 用少量 rehearsal 预测下一层重要 KV，仅从 host memory 预取必要状态以加速 offloaded inference。
- **Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `long-context`
  Infinite-LLM 将 attention layer 解耦并使用 pooled distributed KVCache，支撑最长约两百万 token 的弹性服务。
- **Attention Is All You Need for KV Cache in Diffusion LLMs**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  Elastic-Cache 基于 attention-aware drift test 和 layer-aware schedule 选择何时、何处刷新 DLM KV cache，减少 denoising step 间重复计算。
- **Beyond Speedup - Utilizing KV Cache for Sampling and Reasoning**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  该工作把 KV cache 从单纯加速结构扩展为采样和 reasoning-time reuse 的状态载体，探索更高层次的推理复用。
- **Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache` `memory`
  Bottlenecked Transformer 用轻量 cache processor 周期性重写和整合 KV segments，把推理链中的 latent memory 作为可优化状态。
- **DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache` `rag`
  DefensiveKV 分析基于注意力稳定性的 KV 淘汰脆弱性，并引入更稳健的保留策略降低长上下文质量崩溃风险。
- **Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `training` `kv-cache`
  Fast-dLLM 为 diffusion LLM 引入 KV cache 和并行解码路径，在无需训练的情况下缩小其与自回归模型的推理速度差距。
- **PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache` `quantization` `long-cot`
  PM-KVQ 采用渐进式混合精度量化和长位置分布校准，降低长 CoT 推理中 KV cache 量化的累积误差。
- **ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `tpu` `kv-cache`
  ReST-KV 通过逐层输出重构和时空平滑修正 token 删除后的注意力重分布，使 KV eviction 更适合长序列生成。
- **AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving**
  `SOSP 2025 BigMem Workshop` · `2025` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `rag`
  AdaptCache 为每个 KV entry 联合选择有损压缩算法、压缩率和 DRAM/SSD 放置，在质量约束下提高 DRAM 命中并降低恢复延迟。
- **AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `compression` `kv-cache`
  AnchorKV 在 KV 压缩保留分数中引入 refusal anchor 的软惩罚，使压缩后的长上下文推理兼顾内存节省与安全对齐。
- **CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `kv-cache` `scheduler`
  CacheFlow 将 KV 恢复重构为 token、layer、GPU 三维并行，并以 batch-aware scheduler 联合分配重算和 I/O。
- **CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `agent`
  CacheWise 将 coding agent 的前缀复用与 tool-call 元数据结合做复用感知驱逐和前缀感知调度，显著降低 KV eviction 并缩短会话完成时间。
- **Can I Buy Your KV Cache?**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `prefill` `kv-cache`
  该工作把热门文档的预填充 KV 视作可交易的 provider-side 资产，用服务端复用替代重复 prefill。
- **Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  Nexus Sampling 面向固定预算下的流式 KV eviction，用采样式保留机制维持长上下文质量并控制 cache 增长。
- **HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `kv-cache` `throughput`
  HERALD 利用 block diffusion 每个 block 内 top-k KV 选择可复用的性质，只选一次并与 denoising 重叠，以 CPU-GPU 协同稀疏召回 host DRAM 中的 KV。
- **Information-Aware KV Cache Compression for Long Reasoning**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `compression` `kv-cache`
  InfoKV 将预测不确定性和层间表示演化构成的 entropy signal 与 attention 分数结合，用 Forward Influence 感知的 token 选择改进长推理 KV 压缩。
- **KV Cache Optimization Strategies for Scalable and Efficient LLM Inference**
  `arXiv 综述, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  该综述从淘汰、压缩、混合内存、新注意力和组合策略五条路线比较 KV 优化，并映射到七类部署场景。
- **KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  KVEraser 用学习式 steering state 只改被删除跨度的 KV 区间，在不重算整段 suffix 的前提下做局部上下文擦除。
- **Models Take Notes at Prefill: KV Cache Can Be Editable and Composable**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `prefill` `kv-cache`
  该工作把 KV cache 视作可编辑、可组合的“笔记本”，支持附加勘误与 RoPE 重定位拼接来复用预填充结果。
- **ORBITFLOW: SLO-Aware Long-Context LLM Serving with Fine-Grained KV Cache Reconfiguration**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `kv-cache` `long-context` `slo`
  ORBITFLOW 以轻量 ILP 按请求和层动态决定 GPU/CPU KV 放置，并根据运行反馈重配置以控制尾延迟。
- **PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `compression` `kv-cache`
  PolyKV 在层级粒度上联合选择 KV 压缩策略和预算分配，用异构保留方案替代统一 cache budget。
- **SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `cxl` `gpu` `kv-cache`
  SAC 将稀疏注意力 LLM 的冷 KV cache 下沉到 CXL 内存池，并用访问预测和批量迁移降低 GPU 显存压力。
- **SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `prefill` `serving` `kv-cache`
  SwiftCache 在异构会话间共享 KV cache 并协调多轮对话的缓存放置与复用，降低重复 prefill 和内存占用。
- **Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `agent` `rag`
  Tangram 以确定性 head 预算、Head Group Page 和 AOT 负载均衡，把非均匀 KV 压缩转化为可高效执行的 serving layout。
- **TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `agent`
  TokenDance 利用多 agent round 的 All-Gather 结构集中复用共享 KV，并用 block-sparse diff 压缩 sibling cache。
- **Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `kv-cache` `long-context`
  Tutti 构建 GPU-centric KV object store、GPU io uring 和 slack-aware I/O 调度，使 SSD-backed KV 恢复绕开 CPU 控制瓶颈。
- **VeriCache: Turning Lossy KV Cache into Lossless LLM Inference**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  VeriCache 用压缩 KV 起草、完整 KV 验证，并重叠 HBM 解码与 PCIe/网络换入，保证输出与 full-KV 完全一致。
- **FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `kv-cache` `latency`
  FlowKV 优化块级 KV cache 传输并引入负载感知调度，降低 prefill 到 decode 的传输延迟和节点不均衡。
- **Online Scheduling for LLM Inference with KV Cache Constraints**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  该工作将 KV cache 容量约束纳入 online scheduling 理论，分析 batching、延迟与 hindsight optimal 的竞争关系。
- **TraCT: Disaggregated LLM Serving with CXL Shared Memory KV Cache at Rack-Scale**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `cxl` `kv-cache` `memory`
  TraCT 用 CXL shared memory 同时作为 KV transfer substrate 和 rack-wide prefix-aware KV cache，探索机架级 KV cache 共享。
- **CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving**
  `FAST 2026` · `2026` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `agent`
  CacheSlide 针对 agent prompt 中相对位置稳定的片段设计 RPDC、位置校正和 layer-wise spill-aware KV 复用。
- **Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving**
  `FAST 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  Mooncake 以 KVCache 为中心构建分离式 LLM serving 架构，利用 CPU/DRAM/SSD/NIC 资源扩展在线长上下文服务能力。
- **Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization**
  `ISCA 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `quantization`
  Oaken 将离线量化与在线自适应 KV 量化结合，在降低 cache 带宽和容量的同时控制运行时开销。
- **RefreshKV: Updating Small KV Cache During Long-form Generation**
  `ACL 2025 Long Papers` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  RefreshKV 在长文本生成中交替执行全量注意力和小 KV cache 注意力，动态刷新保留 token 以改善长生成质量。
- **SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference**
  `NeurIPS 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `compression` `kv-cache`
  SmallKV 用小模型注意力补偿大模型 KV 压缩中的显著性漂移和边际信息过压缩。

### Prefill–Decode 与传输 (26)

#### Featured

- **Featured:** **[PLA-Serve: A Prefill-Length-Aware LLM Serving System](https://openreview.net/forum?id=dzjCkSEDyG)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `gpu` `scheduler` `scheduling` `multi-turn` `long-context` `sglang`
  Artifact: [source](https://arxiv.org/abs/2601.11589)
  PLA-Serve（预印本标题 LAPS）在 prefill 阶段按 prompt 长度做双队列与时空分离：长 prefill 与短 prefill 隔离，并对短请求采用 length-aware batching 与 CUDA Graph clustering；在真实多轮 workload 上，相较 vanilla SGLang prefill 延迟降低超过 30%，SLO 违规降低 28%，多 GPU 下进一步降低 12%，Qwen2.5-32B prefill 吞吐提…
- **Featured:** **TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `prefill`
  TPLA 将 latent attention 与 tensor parallel 结合，降低 PD 分离推理中的 KV 和跨卡通信压力。
#### Full Resource List

- **DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `gpu` `goodput` `tpot`
  DistServe 将 prefill 和 decode 放到不同 GPU 上，并按 TTFT/TPOT 约束联合优化资源与并行策略。
- **P/D-Serve: Serving Disaggregated Large Language Model at Scale**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `slo`
  P/D-Serve 面向大规模商业部署，将 prefill/decode 组织、调度和 KVCache 传输做端到端优化，以提升分离式 LLM 服务吞吐和 SLO 表现。
- **[ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping](https://www.usenix.org/conference/osdi26/presentation/liu-yao)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `decode` `gpu` `compiler` `compression` `tensorrt-llm` `throughput` `ttft`
  Artifact: [source](https://www.usenix.org/system/files/osdi26-liu-yao.pdf)
  ADAngel 用 DPR 模型生成多种混合精度 GEMM kernel，并通过 Oracle Policy Map 在运行时为任意 bit-width/shape 任务选择策略；相较 llama.cpp decode 吞吐最高提升 5.10x，相较 TensorRT-LLM prefill TTFT 提升 1.17x–2.38x。
- **[FlashAgents: Accelerating Multi-Agent LLM Systems via Streaming Prefill Overlap](https://openreview.net/pdf?id=m14PPUfgEc)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `agent` `rag`
  FlashAgents 用 agent 间 token streaming、增量 prefill 和 prefix-aware coordination 重叠多智能体调用链中的等待与计算。
- **From Tokens to Layers: Redefining Stall-Free Scheduling for LLM Serving with Layered Prefill**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `moe` `stall`
  该工作把 prefill 调度单位从 token chunk 改为 layer group，在 MoE serving 中减少重复 expert 权重加载并维持 stall-free decode。
- **RDMA Point-to-Point Communication for LLM Systems**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `routing` `serving` `rdma` `moe`
  TransferEngine 为分离式推理、MoE routing 和 RL 权重更新提供可移植 RDMA 点到点通信接口，避免 serving runtime 绑定单一 NIC 栈。
- **[Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token](https://openreview.net/forum?id=FuRo7Ur5Ib)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving`
  Stream2LLM 将上下文流式加载与 prefill 计算重叠，把长 prompt 的数据到达时间隐藏到首 token 前的执行流水中。
- **Towards High-Goodput LLM Serving with Prefill-decode Multiplexing**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `prefill` `gpu` `goodput` `slo`
  MuxWise 在单 GPU 内对 prefill/decode 进行多路复用，并结合估计器和 SLO 调度提升 goodput。
- **[UEP: Portable Expert-Parallel Communication](https://www.usenix.org/conference/osdi26/presentation/mao-ziming-uep)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `training` `gpu` `amd` `moe` `routing` `sglang` `throughput`
  Artifact: [source](https://www.usenix.org/system/files/osdi26-mao-ziming-uep.pdf)
  UEP 以 GPU-CPU 控制通道和 CPU proxy 代替强耦合的 GPU-initiated RDMA，使 expert-parallel 通信跨 NVIDIA/AMD GPU、AWS EFA 与 Broadcom NIC 保持可移植；在 EFA 上 dispatch/combine 吞吐提升 2.1x，SGLang token 吞吐提升最高 40%，16 节点 AMD+Broadcom DeepSeek-V3 训练吞吐提升最高 45%。
- **Alibaba Stellar: A New Generation RDMA Network for Cloud AI**
  `SIGCOMM 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `rdma`
  Stellar 针对云 AI 集群重构 RDMA 网络的可靠性、拥塞控制和多租户隔离。
- **ByteDance Jakiro: Enabling RDMA and TCP over Virtual Private Cloud**
  `SIGCOMM 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `rdma`
  Jakiro 在 VPC 中统一支持 RDMA 和 TCP，使云端 AI workload 获得高性能且可隔离的网络。
- **LeanAttention: Hardware-Aware Scalable Attention Mechanism for the Decode-Phase of Transformers**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode`
  LeanAttention 重构 decode attention 的执行流，在保持精确 attention 的同时提高超长上下文可扩展性。
- **POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference**
  `ASPLOS 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `gpu` `kernel`
  POD-Attention 设计可同时处理 prefill/decode 混合批的 GPU attention kernel，提升两阶段重叠执行效率。
- **PrefillOnly: An Inference Engine for Prefill-only Workloads in Large Language Model Applications**
  `SOSP 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `kv-cache`
  PrefillOnly 专门优化 embedding、reranking 和 prompt encoding 等只有 prefill、没有 decode 的 LLM 应用。
- **THORN-ML: Transparent Hardware Offloaded Resilient Networks for RDMA based Distributed ML Workloads**
  `SoCC 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `rdma`
  THORN-ML 将故障检测和恢复逻辑下沉到网络硬件，提高 RDMA 大模型作业的透明容错能力。
- **Vedrfolnir: RDMA Network Performance Anomalies Diagnosis in Collective Communications**
  `SIGCOMM 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `rdma`
  Vedrfolnir 关联 RDMA telemetry 与 collective 行为，诊断分布式 AI 集群的尾延迟和性能异常。
- **[QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill](https://iclr.cc/virtual/2026/poster/10008892)**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop` · `Reading priority: frontier`
  Tags: `prefill` `serving` `gpu` `compiler` `kernel` `ttft`
  QuoKA uses query-oriented sparse attention for chunked prefill, reporting 3x lower TTFT, 5x faster GPU attention, and nearly 7x faster CPU attention while evaluating 88% fewer KV pairs.
- **[Efficient Multi-round LLM Inference over Disaggregated Serving](https://icml.cc/virtual/2026/poster/64461)**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint` · `Reading priority: frontier`
  Tags: `prefill` `serving` `agent` `rag`
  AMPD 面向多轮 agent/RAG 工作流，在 PD 分离式服务中自适应协调增量 prefill 和阶段部署。
- **ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `moe` `routing`
  ELDR 根据 prefill expert activation 构建 expert signature，并用 locality-band routing 把请求发往 expert locality 更好的 decode worker，降低 PD 分离式 MoE serving 的 decode 延迟。
- **Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `gpu` `tpot` `ttft`
  该工作按 Prefill/Decode 两阶段分别测 TTFT、TPOT 和批量吞吐，比较 GPU 与新型 AI 加速器的相位优势。
- **The Price of Anarchy in Disaggregated Inference**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  该工作从博弈角度分析分离式推理中的自利资源选择如何恶化全局效率，并给出调度设计的效率边界。
- **vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `multimodal` `vllm`
  vLLM-Omni 把任意到任意多模态模型分解为独立 stage graph，为 LLM、扩散模型和编码器分别批处理和分配 GPU。
- **SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill`
  SPAD 分别设计面向 prefill 和 decode 的专用芯片，以更低硬件成本匹配两阶段不同的算力和带宽需求。
- **SDR-RDMA: Software-Defined Reliability Architecture for Planetary Scale RDMA Communication**
  `SC 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `rdma`
  SDR-RDMA 将可靠性策略软件定义化，以支撑跨地域超大规模 RDMA 通信。

### Speculative Decoding (23)

#### Full Resource List

- **Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads**
  `ICML 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `kv-cache`
  Medusa 在目标模型上添加多个 decoding heads，无需独立 draft model 即可并行预测和验证多个未来 token。
- **Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache`
  SparseSpec 以稀疏注意力版本的同一模型充当 draft，并联合调度 drafting、verification 和动态 KV 管理以加速长 CoT。
- **Beat the long tail: Distribution-Aware Speculative Decoding for RL Training**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `training`
  DAS 利用历史 rollout 维护非参数 drafter，并按轨迹长度分配 speculative budget，缩短 RL post-training 中长尾生成阶段。
- **DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `gpu` `kv-cache`
  DFVG 将 draft 放在 FPGA、verify 放在 GPU，以异构流水降低推测解码的草稿成本并提高验证硬件利用率。
- **NexSpec: Towards Optimizing Speculative Decoding in Reinforcement Learning Systems**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  NexSpec 针对 RL 系统中的 speculative decoding 动态调参、更新 drafter 并按 rollout reward 加权，缓解大 batch 和 actor 漂移下的加速失效。
- **SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  SpecDiff-2 用离散扩散模型作为非自回归 drafter，并校准 diffusion drafter 与自回归 verifier 的分布差异，以提升 speculative decoding 接受率和并行度。
- **Speculative Decoding: Performance or Illusion?**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving`
  该工作用真实 serving 条件重新评估 speculative decoding，区分离线 speedup 与在线负载下的端到端收益。
- **AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving**
  `SoCC 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `kv-cache` `slo`
  AdaSpec 根据请求 SLO、草稿成本和接受率动态选择 speculative decoding 配置。
- **MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding**
  `ICML 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `long-context` `latency` `throughput`
  MagicDec 指出长上下文下 target verification 成本相对下降，并联合优化 draft/target KV cache 以兼顾 batch throughput 和 latency。
- **PhoenixOS: Concurrent OS-level GPU Checkpoint and Restore with Validated Speculation**
  `SOSP 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu`
  PhoenixOS 在操作系统层并发执行 GPU checkpoint/restore，并通过验证式推测减少暂停时间。
- **Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  LTD 将 draft/verify 时间分配建模为 RL 环境，联合学习两个策略以直接优化每轮 speculative decoding 的吞吐。
- **Not-a-Bandit: Provably No-Regret Drafter Selection in Speculative Decoding for LLMs**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Not-a-Bandit 把 drafter 选择建模为带理论保证的在线决策问题，在不同请求和模型下自适应选择推测解码草稿器。
- **Self-Speculative Decoding Accelerates Lossless Inference in Any-Order and Any-Subset Autoregressive Models**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  ASSD 让 any-subset autoregressive model 并行生成并自校正 token 分布，在保持无损采样的同时减少生成调用。
- **Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `training`
  Loosely Speculative Decoding 放宽 exact-match 验证，只接受语义等价草稿，提升推测解码在开放生成中的可用接受率。
- **CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `memory`
  CATS 在显存受限场景下自适应选择 tree speculation 结构和草稿深度，减少推测解码额外 KV 与验证开销。
- **EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  EfficientRollout 为 RL rollout 设计自推测解码和系统感知开关策略，在活跃 batch 缩小时继续利用并行验证加速。
- **JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  JetFlow 用单次前向的并行 draft head 生成具因果一致性的候选树，突破 speculative decoding 在更大 draft budget 下的扩展瓶颈。
- **Speculative Speculative Decoding**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache`
  Saguaro 在目标模型验证当前草稿时预先推测验证结果并并行准备下一批草稿，从而进一步隐藏 drafting 串行开销。
- **AdaServe: SLO-Customized LLM Serving with Fine-Grained Speculative Decoding**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `goodput` `slo`
  AdaServe 将 speculative token tree 构造和请求级 SLO 结合，动态选择验证 token 以提高 goodput。
- **Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `gpu` `npu` `kv-cache`
  Mirror-SD 在异构 GPU/NPU 上并行运行互补的 draft/target 推测流水线，突破串行 drafting 的延迟上限。
- **SpecMemo: Speculative Decoding is in Your Pocket**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `gpu` `kv-cache`
  SpecMemo 建模推测解码的内存下界并优化 rejected-token 状态，使受限 GPU 和移动场景也能获得加速。
- **SwiftSpec: Ultra-Low Latency LLM Decoding by Scaling Asynchronous Speculative Decoding**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `kernel` `kv-cache` `latency`
  SwiftSpec 将 draft 与 target 异步解耦扩展，并加入 tree-aware KV management 和 fused kernels 追求单请求极低延迟。
- **LIA: A Single-GPU LLM Inference Acceleration with Layer Bypass and Adaptive Speculative Decoding**
  `ISCA 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `gpu` `kv-cache`
  LIA 联合 layer bypass 与自适应推测解码，在单 GPU 上减少不必要的层执行和 token generation 延迟。

### MoE (34)

#### Featured

- **Featured:** **[SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading](https://www.usenix.org/conference/nsdi26/presentation/li-xingyi)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `gpu` `cuda` `kernel` `moe` `throughput`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-li-xingyi.pdf)
  SwiftEP 面向 MoE prefill 的 all-to-all 通信，以 buffer fusion 消除 staging copy，并结合 TMA offloading、RDMA scatter-gather、QP 并行和 CUDA IPC 提升 NVLink/网络利用率；在 16/32 GPU 集群上相较 DeepEP，算法带宽最高提升 119.7%，SM 占用最高下降 66.7%，服务容量提升 21.2%。
#### Full Resource List

- **MegaBlocks: Efficient Sparse Training with Mixture-of-Experts**
  `MLSys 2023` · `2023` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `routing` `training` `kernel` `moe`
  MegaBlocks 把动态 token routing 转化为 block-sparse operation，避免 expert capacity padding；其 kernel 思路影响 MoE inference。
- **Tutel: Adaptive Mixture-of-Experts at Scale**
  `MLSys 2023` · `2023` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `kernel` `moe`
  Tutel 以自适应并行、all-to-all 和 fused kernel 构建通用 MoE runtime。
- **DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale**
  `ICML 2022` · `2022` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `training` `moe`
  DeepSpeed-MoE 联合优化 expert parallel、通信和模型压缩，使大规模 MoE 同时具备训练和推理可行性。
- **Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `gpu` `kernel` `kv-cache` `moe` `slo`
  该工作用 stream-loading prefill、SmallEP、零拷贝 prefill/decode 分离和 CPU FP8 kernel，把本地 CPU-GPU 平台上的 MoE serving 拉近云端 SLO。
- **EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `moe`
  EARTH 根据 gating entropy 推测预取 expert 并复用结果，以降低 MoE expert 加载等待与误预取代价。
- **FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `moe` `quantization`
  FP8-Flow-MoE 为 MoE 设计避免重复量化误差的 FP8 执行配方，减少 expert 路径中的 cast 和量化开销。
- **LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `training` `moe`
  LAER-MoE 根据 expert 负载动态重排布局，属于与推理基础设施相邻的 MoE 训练系统工作。
- **MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `moe`
  MoE-APEX 根据 expert 热度和执行需求自适应选择精度与卸载方式，缓解 MoE 权重容量和传输瓶颈。
- **MoEBlaze: Breaking the Memory Wall for Efficient MoE Training on Modern GPUs**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `training` `gpu` `memory` `moe`
  MoEBlaze 针对现代 GPU 上 MoE 训练的显存墙优化 expert 参数、激活和通信组织，为大规模 MoE 系统提供训练侧基础设施。
- **COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `moe`
  COMET 通过依赖分析、任务重排和自适应工作量分配细粒度重叠 MoE 通信与计算，并已用于万卡级生产集群。
- **KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models**
  `SOSP 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `kernel` `moe`
  KTransformers 把活跃 expert、attention 与其他算子分配到 CPU/GPU，并用定制 kernel 提升本地 MoE 推理。
- **MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kernel` `kv-cache` `moe`
  MiLo 用自适应低秩补偿器恢复超低比特 MoE 的精度，并配套 Tensor Core 友好的 3-bit kernel。
- **MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training**
  `SIGCOMM 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `routing` `training` `moe`
  MixNet 根据 MoE 动态 all-to-all 流量重配置光电混合 fabric，缓解 expert routing 热点。
- **Stratum: System-Hardware Co-Design with Tiered Monolithic 3D-Stackable DRAM for Efficient MoE Serving**
  `MICRO 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `serving` `moe`
  Stratum 将分层 monolithic-3D DRAM、近存计算和 expert 热度预测结合，提高 MoE decode 的带宽和能效。
- **Libra: Effective yet Efficient Load Balancing for Large-scale MoE Inference**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `moe`
  Libra 为大规模 MoE inference 设计低开销负载均衡机制，在避免 expert 热点的同时不引入新的通信瓶颈。
- **SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `routing` `moe`
  SERE 在 batch decoding 中按相似性重路由 expert，降低 MoE 批处理时的专家激活发散和内存带宽压力。
- **Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `moe`
  Semantic Parallelism 将 token 语义聚类和 expert 放置协同调度，减少 MoE expert parallel 中昂贵的跨设备 all-to-all。
- **A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `moe`
  ST-MoE 利用跨层和跨 token 的 expert 激活相关性做时空联合预取，以重叠 expert 加载和 MoE 推理计算。
- **Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `moe`
  该工作按任务相关性组织 MoE expert/grouping，减少多任务 MoE 推理中的跨设备通信和路由冲突。
- **Coordinated Scheduling for MoE LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `prefill` `serving` `moe`
  Gimbal 联合前端 DP-engine 调度与后端 expert 放置，按 KV 压力、prefill 余量和 expert 热点协调 MoE serving。
- **CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `moe`
  CrossPool 面向冷门 MoE 模型服务，把 KV cache 和权重分别做池化/分离管理，降低多模型长尾部署的显存常驻成本。
- **Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `moe` `edge`
  该实证研究比较 MoE 在消费级和边缘硬件上的真实延迟、内存和能耗收益，避免只用理论 FLOPs 判断端侧可行性。
- **Fast MoE Inference via Predictive Prefetching and Expert Replication**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `gpu` `moe`
  该工作预测热点 expert 并做动态复制和预取，以减少稀疏激活造成的等待和 GPU 空转。
- **Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `routing` `kv-cache` `moe`
  GQE 在 grouped-query attention 内只对 query head 做 expert routing，保留 GQA 的 KV cache 优势，同时减少长上下文 attention 的活跃计算。
- **NPUMoE: Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `routing` `gpu` `npu` `moe`
  NPUMoE 将静态密集 expert 计算卸载到 Apple NPU，并为动态 routing 保留 CPU/GPU fallback。
- **Tarragon: Making MoE-based LLM Inference Resilient**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `moe` `rag`
  Tarragon 将 attention worker 和 expert worker 设为独立故障域，用 KV 增量 checkpoint 和 shadow experts 快速恢复。
- **WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `kv-cache` `moe`
  WiSP 将 expert 权重与 KV cache 统一建模为 GPU working set，并用 MV-WSA 在两者之间动态分配 VRAM 以提升低资源 MoE serving 吞吐。
- **BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `routing` `moe`
  BEAM 用二值 expert activation mask 做动态路由，减少 MoE 推理中不必要的 expert 激活和通信。
- **BrownoutServe: SLO-Aware Inference Serving under Bursty Workloads for MoE-based LLMs**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `moe` `slo`
  BrownoutServe 在突发流量下动态减少部分 expert 访问并使用 united experts，在精度和 SLO 之间调节。
- **DuoServe-MoE: Dual-Phase Expert Prefetch and Cache Scheduling for Efficient MoE LLM Inference**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `moe`
  DuoServe-MoE 为 prefill 和 decode 设计不同 expert prefetch/cache 策略，以较小显存运行大型 MoE。
- **MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `moe`
  MegaScale-Infer 将 attention 与 MoE FFN 解耦部署，并以 ping-pong pipeline 和 M2N 通信库提高专家利用率。
- **CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution**
  `DAC 2026` · `2026` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `gpu` `moe` `throughput`
  CoX-MoE 用合并式 expert 执行、静态 expert 分层与选择性 attention offload 协调 CPU-GPU 协作，避免 micro-batch 导致的 MoE 推理低效。
- **Diff-MoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching**
  `SC 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `moe`
  Diff-MoE 根据 expert 优先级采用差异化缓存，并面向 batch 复用热点 expert。

### Compiler / DSL (3)

#### Full Resource List

- **[Agentix: An Efficient Serving Engine for LLM Agents as General Programs](https://www.usenix.org/conference/nsdi26/presentation/luo)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `tpu` `compiler` `kernel` `agent` `rag` `vllm` `latency`
  把 agent 程序及其依赖的 LLM calls 作为 serving 调度的一等对象，利用已完成调用的程序级上下文进行抢占和优先级调度；官方 NSDI 2026 页面报告在相同延迟下，相比 vLLM 等系统程序吞吐提升 4–15 倍。
- **Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `compiler`
  Flashlight 扩展 PyTorch compiler 来支持 attention 变体加速，使新注意力算子更容易进入生产编译与执行路径。
- **ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `kernel`
  ParallelKittens 提供更系统的多 GPU kernel 编程与组合方式，降低跨 GPU LLM inference kernel 的实现复杂度。

### Runtime / Scheduling (90)

#### Featured

- **Featured:** **FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kernel`
  FlashInfer 用 block-sparse/composable KV format、JIT attention template 和 load-balanced scheduling 提供 serving-oriented kernel。
- **Featured:** **BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu`
  BOute 用多目标贝叶斯优化在异构模型和 GPU 组合中选择 serving 配置，联合降低成本并满足质量和延迟目标。
- **Featured:** **[Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration](https://www.usenix.org/conference/osdi26/presentation/du)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `goodput`
  Artifact: [source](https://github.com/MLSysU/EcoServe)
  提出面向普通 GPU 集群的 partially disaggregated serving，通过时间维度 P/D 分离、跨实例循环协作、adaptive routing 和 mitosis scaling 缓解 prefill-decode 干扰；在 32 张 NVIDIA L20 以太网集群上，相比 vLLM、Sarathi、DistServe、MoonCake 等基线 goodput 最高提升 2.51 倍，并开源 EcoServe。
- **Featured:** **[FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `npu` `compiler` `kernel` `agent` `edge` `vllm`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-wu-bingyang.pdf)
  以输出 token 为粒度实现可抢占的分布式 LLM serving，提出 skip-join 多级反馈队列，并主动在 GPU/主机内存间搬运中间状态；官方 NSDI 2026 页面报告相对 vLLM 吞吐最高提升 6.1 倍。
- **Featured:** **[HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds](https://www.usenix.org/conference/nsdi26/presentation/lou)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `agent` `rag` `latency`
  Artifact: [source](https://www.usenix.org/system/files/conference/nsdi26/nsdi26spring_lou_prepub.pdf)
  通过跨服务器预分发模型、重叠 cold-start 阶段、GPU 间 worker 放置和 pipeline consolidation，降低公有云 serverless LLM serving 冷启动；官方 NSDI 2026 页面报告冷启动延迟降低 1.7–4.7 倍，SLO attainment 提升 1.43–1.74 倍。
- **Featured:** **QoServe: Breaking the Silos of LLM Inference Serving**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving`
  QoServe 统一管理原本割裂的 LLM serving 资源池，以减少不同服务等级和工作负载之间的资源孤岛。
- **Featured:** **[SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems](https://www.usenix.org/conference/nsdi26/presentation/agarwal)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `kv-cache` `memory` `agent` `multi-turn` `vllm` `latency` `throughput`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-agarwal.pdf)
  SYMPHONY 将计算与 KV cache 存储解耦为面向多轮会话的 disaggregated memory layer，通过 advisory prefetch、priority-based KV 管理和 cooperative memory management 避开关键路径；在 LLaMA/ShareGPT/Burst-GPT 上相较 vLLM 将端到端延迟降低 2.4x，并在小幅延迟增加下服务 4x 请求。
#### Full Resource List

- **Llumnix: Dynamic Scheduling for Large Language Model Serving**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving`
  Llumnix 通过请求及其 KV 状态的 live migration，在多实例间动态重调度以改善尾延迟、隔离和负载均衡。
- **MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `memory`
  MemServe 以 MemPool 统一管理跨实例分布式 KV，并联合 context caching、PD 分离和全局 locality-aware scheduling。
- **SGLang: Efficient Execution of Structured Language Model Programs**
  `NeurIPS 2024` · `2024` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `agent` `rag` `sglang`
  SGLang 用 RadixAttention、结构化生成语言和高性能 runtime 统一优化多调用、共享前缀和约束生成工作流。
- **Breaking the Ice: Analyzing Cold Start Latency in vLLM**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `vllm` `latency`
  该工作拆解 vLLM 冷启动中的 CPU-bound 阶段并建立延迟模型，为 serverless LLM 的预热、调度和容量规划提供依据。
- **Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu`
  Bullet 在空间放置和时间调度两个维度动态编排 LLM 请求，以减少 GPU 碎片并提高服务利用率。
- **[DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems](https://openreview.net/forum?id=Xfzzp6grRP)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving`
  DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更。
- **[FaaScale: Unlocking Fast LLM Scaling for Serverless Inference](https://openreview.net/forum?id=jgL8LuOVyT)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `gpu` `rdma` `memory` `scheduler` `heterogeneous` `ttft`
  Artifact: [source](https://github.com/lambda-scale/lambda-scale)
  FaaScale 以 PipeCast 将模型分块 multicast 与跨节点 pipeline-parallel inference 协同，在模型传输尚未完成时即开始执行，并结合 GPU/host memory 管理应对突发 serverless 负载；真实 LLM traces 上 P90 TTFT 改善 2.4x–5x、GPU 成本降低 17.8%–31.3%。
- **[GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving](https://openreview.net/forum?id=xKjYiUgeOK)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `decode` `gpu` `compression` `kv-cache` `long-context` `agent` `latency`
  Artifact: [source](https://arxiv.org/abs/2605.00831)
  GhostServe 在 host memory 中以 erasure coding 为 streaming KV cache 生成 parity shards，故障时重建丢失 KV 状态并继续推理，避免完整重算或全量状态复制；单 batch checkpoint latency 最高降低 2.7x，recovery latency 降低 2.1x，中位响应延迟降低 1.2x。
- **[HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving](https://openreview.net/forum?id=CV52m9NJFK)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving`
  HELIOS 在线选择模型和 early-exit 层数，只加载满足任务目标所需的层，从而在质量约束下提高吞吐和能效。
- **JITServe: SLO-aware LLM Serving with Imprecise Request Information**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `slo`
  JITServe 在输出长度和调用依赖未知时逐步收紧估计，并只分配满足 SLO 所需的 just-in-time serving bandwidth。
- **[Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads](https://www.usenix.org/conference/nsdi26/presentation/ruan-libra)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `prefill` `goodput` `slo`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-ruan-libra.pdf)
  提出 micro-request flexible partitioning and scheduling，将请求在 token 边界切分为协作片段，并用全局/本地两级调度与 chunked KV transfer 处理不均衡动态 workload；在 A100/H100 真实 trace 上，goodput 最高提升 1.91 倍、服务容量最高提升至 3.07 倍。
- **[OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving](https://www.usenix.org/conference/osdi26/presentation/yao)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `rag`
  以用户态 orchestration overlay 将异构、分散且由 Slurm 等管理的 HPC 集群统一为 serving 平台，提供 CRDT gossip 服务发现、统一 serving API、异构调度和容错；官方 OSDI 2026 页面报告已服务 13M 请求、15B tokens、142 个模型，并面向 1000+ 研究者部署。
- **[Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning](https://www.usenix.org/conference/osdi26/presentation/yu-shan)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `memory`
  Artifact: [source](https://github.com/ovg-project/kvcached)
  基于生产 trace 中动态 bursty model groups，使用 kvcached balloon driver 在多模型间弹性回收和分配 GPU memory，统一 spatial/time sharing；官方 OSDI 2026 页面称其已在 10K+ GPU 生产环境部署。
- **Revisiting Pipeline Parallelism for LLM Serving**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving`
  该工作重新分析 pipeline parallelism 在 LLM serving 中的阶段空泡、batch 形成和延迟权衡，为在线推理选择更稳健的流水配置。
- **[SHIP: SRAM-Based Huge Inference Pipelines for Fast LLM Serving](https://openreview.net/forum?id=IZaXDwDtL1)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `decode` `lpu` `sram` `compiler` `kernel` `long-context` `moe`
  Artifact: [source](https://mlsys.org/media/mlsys-2026/Slides/3834_VmkjzHq.pdf)
  SHIP 总结 Groq 基于 LPUv1 SRAM 的大规模 LLM serving：以低直径同步互联和静态编译 pipeline 扩展到数千芯片，并在受限 SRAM 中实现 PagedAttention、prefix caching、speculative decoding 及动态 chunked prefill，面向生产流量维持低延迟。
- **SchedFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `sglang` `vllm`
  SchedFlow 将逻辑模型定义与物理执行 schedule 解耦，用可编程 operator scheduling 在 vLLM、SGLang 和 HuggingFace Transformer 中透明接入设备内并行。
- **Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill`
  该工作用更简单的乘法式请求调度指标协调排队、prefill/decode 负载和 KV 压力，避免过度复杂的在线策略。
- **[SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips](https://openreview.net/forum?id=RuslSHdIHa)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `memory` `slo`
  SuperInfer 面向 GH200 的 NVLink-C2C 设计请求轮转调度和全双工 KV 搬运，缓解高负载下的 HOL blocking。
- **[TimelyLLM: Time-sensitive LLM Serving System for Physical-I/O Limited Agents](https://www.sigmobile.org/mobisys/2026/program/#timelyllm-time-sensitive-llm-serving-system-for-physical-i-o-limited-agents)**
  `MobiSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `serving` `gpu` `scheduler` `kv-cache` `agent` `latency` `slo`
  Artifact: [source](https://neawhen.github.io/neiwen.github.io/assets/pdf/timelyllm.pdf)
  TimelyLLM 面向机器人、无人机和语音助手等物理 I/O 受限 agent，把连续生成拆成可执行 segment，并在 agent 执行期间暂停/恢复 decode，以 slack-aware priority scheduler 按时间效用重新分配资源；MobiSys 2026 program 报告其 time utility 最高提升 1.52x、agent waiting time 最多降低 84%。
- **[TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling](https://doi.org/10.1145/3767295.3769328)**
  `EuroSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `kv-cache` `ttft`
  Artifact: [source](https://arxiv.org/abs/2510.02758)
  针对突发请求下的流式生成，提出可抢占请求调度与主动 KV cache 管理，依据 token buffer 占用和消费速率动态排序，并在 GPU/CPU 间后台迁移 KV、重叠 I/O 与计算；在 Llama 3 8B、Qwen2.5 32B 和 RTX 4090/A6000/H200 上评测，报告有效吞吐最高提升 82.5%、P99 TTFT 最高降低 80.2%。
- **[WISP: Waste- and Interference-Suppressed Distributed Speculative LLM Serving at the Edge via Dynamic Drafting and SLO-Aware Batching](https://www.sigmetrics.org/sigmetrics2026/accepted.html#wisp-waste-and-interference-suppressed-distributed-speculative-llm-serving-at-the-edge-via-dynam)**
  `ACM SIGMETRICS 2026 official accepted papers` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `decode` `gpu` `edge` `scheduler` `speculative-decoding` `goodput` `slo`
  Artifact: [source](https://arxiv.org/abs/2601.11652)
  将边缘设备纳入 speculative serving，针对 wasted drafting 与 verification interference，设计 speculation controller、verification-time estimator 和 verification batch scheduler；在公开实验中，系统容量最高提升 2.1/4.1 倍，goodput 最高提升 1.94/3.7 倍，相比 centralized serving 与 SLED。
- **Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market**
  `SOSP 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu`
  Aegaeon 通过细粒度 GPU pooling 和模型复用服务长尾模型市场，降低每个模型独占设备的成本。
- **Cauchy: A Cost-Efficient LLM Serving System through Adaptive Heterogeneous Deployment**
  `SoCC 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu` `slo`
  Cauchy 在不同 GPU 类型和云实例间动态放置模型，根据负载变化降低满足 SLO 的成本。
- **Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments**
  `MICRO 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `moe`
  Chameleon 联合管理大量 LoRA/adapter 的缓存和请求调度，减少多租户适配器服务中的换入与等待。
- **Fast State Restoration in LLM Serving with HCache**
  `EuroSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `prefill` `serving`
  HCache 缓存并恢复模型服务的中间状态，降低实例迁移、抢占或恢复后的重复 prefill 成本。
- **LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill`
  LServe 将 prefill 与 decode 的硬件友好结构化稀疏统一起来，以 streaming heads 和层次 KV page selection 加速长序列服务。
- **Multiplexed Heterogeneous LLM Serving via Stage-Aligned Parallelism**
  `SoCC 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill`
  该工作按模型阶段对齐异构设备的并行与复用方式，避免 prefill/decode 在不同硬件上的能力错配。
- **PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM**
  `HPCA 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode`
  PAISE 将 Transformer 请求调度与 PIM 执行特征联合建模，降低内存密集 decode 的排队和数据移动。
- **QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `kv-cache` `quantization`
  QServe 联合 W4A8KV4 量化、SmoothAttention、权重重排和寄存器级并行，将理论低比特节省转成云端 serving 吞吐。
- **SOLA: Optimizing SLO Attainment for Large Language Model Serving with State-Aware Scheduling**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `slo` `tpot`
  SOLA 在每次迭代感知请求状态和系统状态，动态平衡 TTFT、TPOT 及请求间公平性。
- **ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu`
  ThunderServe 在异构 GPU 和网络环境中联合优化部署与并行策略，并以轻量重调度适应故障和流量漂移。
- **throttLL'eM: Predictive GPU Throttling for Energy Efficient LLM Inference Serving**
  `HPCA 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu` `slo`
  throttLL'eM 预测 token 阶段的性能余量并动态调节 GPU 功率或频率，在满足 serving SLO 时降低能耗。
- **[AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving](https://iclr.cc/virtual/2026/poster/10010915)**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop` · `Reading priority: frontier`
  Tags: `prefill` `serving` `npu` `agent` `rag`
  AdaCache combines cache-aware partial recomputation with adaptive retrieval depth for RAG serving, reducing redundant long-input processing while preserving generation quality.
- **[Reasoning Language Model Inference Serving Unveiled: An Empirical Study](https://iclr.cc/virtual/2026/poster/10011393)**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop` · `Reading priority: frontier`
  Tags: `serving` `memory` `quantization` `rag`
  This official empirical study characterizes reasoning-model serving through memory fluctuation, stragglers, and adaptive runtime; it evaluates quantization, KV quantization, speculative decoding, and prefix caching under realistic workload…
- **[Beyond Prediction: Tail-Aware Scheduling for LLM Inference](https://icml.cc/virtual/2026/poster/63644)**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint` · `Reading priority: frontier`
  Tags: `serving` `ttft`
  Beyond Prediction 用分布感知而非长度预测的调度与 cache-aware preemption 联合优化在线 LLM serving 的 TTFT 和尾延迟。
- **[OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration](https://icml.cc/virtual/2026/poster/64482)**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint` · `Reading priority: frontier`
  Tags: `serving`
  OServe 针对请求空间异质性和流量时间变化，动态选择异构模型部署并迁移并行配置。
- **DejaVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving**
  `ICML 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache`
  DejaVu 用 KV-cache streaming 支持 prompt-token 分离、microbatch swapping 和状态复制，缓解流水线空泡、显存过配和故障恢复问题。
- **ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference**
  `ASPLOS 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  ExeGPT 根据输入输出长度分布和延迟约束搜索 batch、并行度及执行计划，以最大化约束下吞吐。
- **A First Look at Bugs in LLM Inference Serving Systems**
  `EuroSys 2026 poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  该工作系统归纳 LLM serving runtime 中的正确性、并发、内存和性能故障模式，为可靠性研究建立问题分类。
- **DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  DualMap 同时考虑 prefix cache affinity 和实例负载均衡，缓解分布式 LLM serving 中复用率与尾延迟的冲突。
- **Efficient LLM Serving for Agentic Workflows with Context-Aware State Management**
  `EuroSys 2026 poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `prefill` `serving` `agent` `rag`
  该工作针对 agent 多轮调用中的可复用上下文和中间状态设计 context-aware 管理机制，减少重复 prefill 与状态搬运。
- **PARD: Accelerating LLM Inference with Low-Cost PARallel Draft Model Adaptation**
  `ICLR 2026 Poster` · `2026` · `Academic paper` · `Poster / Workshop · Legacy Import` · `Reading priority: supporting`
  Tags: `vllm`
  PARD 将单个 draft model 低成本适配到同族目标模型，并在 draft 阶段一次预测多个未来 token 以提升 vLLM 推理吞吐。
- **Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `slo` `ttft`
  Festina 以 profiling-guided 全局放置、本地 phase-aware 调度、SM 划分和 GPU operating point 联合控制，在共享 GPU 的 serverless LLM serving 中降低集群能耗并守住 TTFT/TBT SLO。
- **Fine-Tuning and Serving Gemma 4 31B on Google Cloud TPU: A Technical Comparison with GPU Baselines**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `tpu` `vllm`
  该工作给出从 JAX/Tunix 微调到 vLLM-TPU serving 的完整路径，并在统一配置下比较 TPU 与 H100 的成本和延迟。
- **FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  FlexServe 在移动端用可调资源隔离和安全执行路径协调本地 LLM serving 的延迟、隔离和资源复用。
- **Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `vllm`
  该工作提出按 KV 占用几何体积增长而非仅按时长排序的 SVF/1-bit SVF 在线调度，并将其作为 vLLM 可插拔层降低平均与尾部时延。
- **HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `gpu` `memory` `quantization`
  HMA-Serve 将 GDDR 加速器用于 prefill、HBM GPU 用于 decode，并通过 phase-wise quantization、compute-transfer overlap 和 deferred dequantization 支撑跨厂商异构 PD serving。
- **HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `prefill` `serving`
  HYPIC 为 hybrid-attention LLM 引入 segment-cumulative transition cache、boundary seam recomputation 和跨实例 cache-miss prefill 并行化，使 PIC 可用于长上下文 serving。
- **Joint Encoding of KV-Cache Blocks for Scalable LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache`
  该工作跨请求融合相似 KV block 为共享表示，在维持标准 cache layout 的同时提高并发容量。
- **LLMServingSim 2.0: An Enhanced Simulator for LLM Serving Systems with Graph-Based Workloads**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `agent` `rag`
  LLMServingSim 2.0 用图结构表达多阶段、分支和 agent 请求，为新调度与异构部署方案提供可重复仿真平台。
- **LUMEN: Coordinated Failure Recovery for Distributed LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  LUMEN 把分布式 LLM serving 的故障恢复建模为 checkpoint 放置、请求重分配和 reload 期间容量恢复的联合负载协调问题。
- **MiniPIC: Flexible Position-Independent Caching in <100LOC**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `vllm`
  MiniPIC 在 vLLM 中以未旋转 K cache 和少量用户侧 primitive 实现位置无关缓存，并与 CPU offload 共存。
- **Pythia: Exploiting Workflow Predictability for Efficient Agent-Native LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `agent`
  Pythia 在 serving 层显式编码多 agent workflow 语义，用可预测拓扑结构改善 prefix cache、扩缩容与长上下文调度。
- **RTP-LLM: High-Performance Alibaba LLM Inference Engine**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  RTP-LLM 汇总阿里生产推理栈中的快速加载、PD 分离、分层 KV、推测解码、量化和多模态解耦能力。
- **ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  ReMP 将模型并行拓扑与运行时状态解耦，并用二维 KV 迁移在 TP/PP 重配置时尽量保留可复用缓存。
- **RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `routing` `serving`
  RouteBalance 把模型路由和实例负载均衡合并成一个在线分配问题，联合优化质量、延迟和成本。
- **SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `quantization`
  SAW-INT4 面向真实 serving 约束设计 4-bit KV quantization，强调 paged layout、规则访存和 fused attention 可落地性。
- **SPIN: Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `memory` `long-context`
  SPIN 用统一 page-based partition、locality-aware KV manager 和分层元数据把 sparse attention 与 CPU/GPU 分层 KV 存储协同起来。
- **Service-Induced Congestion in Memory-Constrained LLM Serving**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `memory`
  该工作把持续增长的 KV memory pressure 建模为服务自身诱发的拥塞过程，并分析 eviction-free 平衡与极限环失稳。
- **ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `gpu` `slo`
  ShuntServe 面向异构 spot GPU 集群联合做模型放置、负载分流和抢占恢复，以降低满足 SLO 的 serving 成本。
- **Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing**
  `arXiv 预印本, 2026` · `2026` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `slo` `tpot`
  Tropical 用 SLO-aware multiplexing 在非分离与分离 serving 之间折中排队时间和干扰，提升 TTFT/TPOT 的联合达标率。
- **AccelGen: Heterogeneous SLO-Guaranteed High-Throughput LLM Inference Serving for Diverse Applications**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `agent` `rag` `slo` `throughput`
  AccelGen 用动态 chunk、iteration SLO 优先级和 compute/KV 双资源感知 batching 服务长短 prompt 与不同延迟约束。
- **Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `goodput` `ttft`
  Apt-Serve 将 KV cache 与更省内存的 hidden cache 组合，并动态优化 batch composition 以扩大并发和 TTFT goodput。
- **AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `agent` `rag`
  AugServe 针对 tool-augmented 请求用两阶段调度和动态 token batch limit 缓解未知暂停与队头阻塞。
- **CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `cxl` `kv-cache` `memory`
  CXL-SpecKV 将 KV cache offload 到远端 FPGA/CXL memory，并用 speculative prefetch 与压缩/解压引擎降低带宽压力。
- **EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `compression` `kv-cache`
  EVICPRESS 联合优化 KV cache 的有损压缩和多层存储淘汰，在质量和延迟之间做全局权衡。
- **GreenLLM: SLO-Aware Dynamic Frequency Scaling for Energy-Efficient LLM Serving**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `gpu` `slo`
  GreenLLM 对 prefill/decode 分别建模和调频，在维持 token SLO 的同时降低 GPU 能耗。
- **HydraInfer: Hybrid Disaggregated Scheduling for Multimodal Large Language Model Serving**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `multimodal`
  HydraInfer 将视觉 encode、prefill 和 decode 分到异构实例，以 stage-level batching 和并行执行提高 MLLM 吞吐。
- **LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `training` `gpu`
  LeMix 联合调度持续训练与在线推理，通过预测干扰和动态资源分配利用空闲 GPU 而不牺牲 serving 响应性。
- **Niyama: Breaking the Silos of LLM Inference Serving**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  Niyama 以细粒度 QoS 分类、动态 chunking 和选择性请求降级在共享集群中混部交互式与批处理负载。
- **On Evaluating Performance of LLM Inference Serving Systems**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `stall`
  该工作归纳 baseline、实验配置和 metric 反模式，并用推测解码案例说明错误归一化会掩盖 generation stall。
- **Taming the Titans: A Survey of Efficient LLM Inference Serving**
  `arXiv 综述, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  该综述按 instance、cluster 和新兴应用场景系统整理模型放置、调度、存储、分离架构及云端策略。
- **TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill`
  TokenScale 用 token velocity 统一衡量 PD 各阶段压力，并允许 decoder 临时执行 prefill 以吸收突发流量。
- **semi-PD: Towards Efficient LLM Serving via Phase-Wise Disaggregated Computation and Unified Storage**
  `arXiv 预印本, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill` `rag`
  semi-PD 在 SM 级别分离 prefill/decode 计算但统一显存管理，减少完全 PD 分离带来的存储浪费和迁移开销。
- **BurstGPT: A Real-world Workload Dataset to Optimize LLM Serving Systems**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  BurstGPT 发布 Azure OpenAI 服务的五百余万条真实 trace，揭示 burst、长度和失败模式对调度评估的影响。
- **LLM Inference Serving: Survey of Recent Advances and Opportunities**
  `arXiv 综述, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  该综述聚焦 2023 年后的系统级 LLM serving 论文，覆盖调度、内存、并行和生产部署机会。
- **MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `prefill`
  MuxServe 结合模型流行度、空间共置和 prefill/decode 时间复用，提高多模型 serving 的显存与算力利用率。
- **Preble: Efficient Distributed Prompt Scheduling for LLM Serving**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  Preble 在分布式集群中联合优化共享前缀 KV 复用和计算负载均衡，并用分层调度处理 prompt locality。
- **The CAP Principle for LLM Serving: A Survey of Long-Context Large Language Model Serving**
  `arXiv 综述, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `long-context`
  该综述以 Context length、Accuracy、Performance 三目标冲突组织长上下文 serving，并强调用户感知指标定义。
- **3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving**
  `IEEE Computer Architecture Letters 2026` · `2026` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `serving`
  3DLS 用 logic-on-logic 3D chiplet 将 PD 分离中的 KV 传输切到垂直互连、把 decode 侧 TP collective 留在横向 D2D fabric，以隔离混合通信争用。
- **Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation-Storage Awareness**
  `FAST 2026` · `2026` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `rag`
  Bidaw 让计算调度感知 KV 加载延迟，并让两级存储利用模型响应预测访问与淘汰，提高多轮会话 KV 命中。
- **LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving**
  `SC 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kernel`
  LiquidGEMM 针对 W4A8 推理设计硬件高效的反量化、数据布局和 GEMM kernel。
- **MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving**
  `SC 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `rag`
  MaverIQ 用 workload fingerprint 预测资源需求，并以碎片感知的分层配置实现 intent-based serving。

### 探索观察

最近 180 天内有正式或工程证据、但尚未成为稳定主线的新语境工作。

- **AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `kernel` `agent`
  AccelOpt 将 LLM agent 用于 AI accelerator kernel 优化闭环，让生成、profile、修复和迭代搜索共同改进算子实现。
- **CDLM: CONSISTENCY DIFFUSION LANGUAGE MODELS FOR FASTER SAMPLING**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  CDLM 将 consistency/diffusion language model 的采样过程系统化加速，减少扩散式文本生成需要的迭代步数。
- **FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `edge`
  FastTTS 面向边缘设备优化 test-time scaling，使多次候选生成与验证能够在受限资源上高效执行。
- **[FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees](https://www.usenix.org/conference/nsdi26/presentation/oliaro)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `serving` `training` `gpu` `memory` `scheduler` `agent` `rag` `latency`
  Finetuning large language models (LLMs) is essential for task adaptation, yet today's serving stacks isolate inference and finetuning on separate GPU clusters—wasting resources and under-utilizing hardware. We introduce FlexLLM, the first…
- **[Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with Sereno](https://www.usenix.org/conference/osdi26/presentation/xin)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `memory`
  分析移动设备前台应用与 LLM 推理之间不对称的内存带宽干扰，利用 speculative decoding 提供可抢占 yield points，让推理动态让出带宽；官方 OSDI 2026 页面报告前台 jank rate 平均降低 58.5%、LLM throughput 平均提升 26.4%。
- **IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `edge`
  IntAttention 用整数域 IndexSoftmax 和端到端 INT8 attention pipeline 消除反量化-浮点 softmax-再量化路径，降低端侧延迟和能耗。
- **NodeSweep: Practical Straggler Detection and Health Monitoring for Large-Scale Foundation Model Training**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `training` `rag`
  NodeSweep 将在线性能监控与离线 node sweep 结合，识别传统 NCCL/burn-in 检查漏掉的慢节点，提升大规模基础模型训练集群稳定性。
- **Optimizing PyTorch Inference with LLM-Based Multi-Agent Systems**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `kernel` `agent`
  该工作系统比较 LLM 多智能体优化 PyTorch 推理代码的策略，用 KernelBench/H100 评估 agentic kernel tuning 对端到端推理性能的提升。
- **PROMPTS: PeRformance Optimization via Multi-Agent Planning for LLM Training and Serving**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `training` `agent`
  PROMPTS 用 analyzer/proposal 多智能体系统读取 profiler 数据并生成 sharding 配置，在训练和 serving workload 上自动提出系统级优化方案。
- **SAKURAONE: An Open Ethernet-Based AI HPC System and Its Observed Workload Dynamics in a Single-Tenant LLM Development Environment**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  SAKURAONE 报告开放以太网 AI HPC 系统及单租户 LLM 开发环境中的 workload dynamics，为非专有互连大模型集群提供生产参照。
- **[ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `serving` `multimodal`
  Artifact: [source](https://github.com/alibaba/ServeGen)
  基于全球云端生产 serving 服务，刻画语言、多模态和 reasoning 模型 workload，并按 client 组合生成更真实的 serving traces；官方 NSDI 2026 页面明确提供开源实现 https://github.com/alibaba/ServeGen。
- **TiDAR: Think in Diffusion, Talk in Autoregression**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache`
  TiDAR 在单次 forward 中用 diffusion draft 和 autoregressive sampling 结合生成，保留精确 KV cache 支持并提高 serving 吞吐。
- **db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `agent` `rag`
  db-SP 面向视觉生成模型的稀疏 attention 设计 dual-balanced sequence parallelism，降低长序列视觉生成中的负载不均和跨设备通信。
- **[Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access for LLM via Semantic-Aware Knowledge Caching](https://www.usenix.org/conference/nsdi26/presentation/ruan-cortex)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `memory` `agent` `rag` `latency` `throughput`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-ruan-cortex.pdf)
  Cortex 为 LLM agent 构建跨区域语义知识缓存，以 Semantic Element 和 Semantic Retrieval Index 支持语义命中、成本感知淘汰与主动预取；在代表性搜索任务上吞吐最高提升 3.6x，代码任务最高提升 20x，同时保持近似非缓存基线的准确率。
- **[ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler](https://openreview.net/forum?id=tYHWS7YPof)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `prefill` `decode` `edge` `gpu` `memory` `scheduler` `moe` `latency`
  Artifact: [source](https://arxiv.org/abs/2601.20755)
  ProfInfer 使用 eBPF 在不修改或重编译 llama.cpp 的情况下，对 token、计算图、算子和硬件计数器进行多粒度追踪，提供 ProfDAG、ProfTime、ProfStat 视图，覆盖 dense、MoE routing 与 offloading；在线开销低于 4%，用于定位内存/计算瓶颈和支持资源感知调度。
- **[ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference](https://www.sigmobile.org/mobisys/2026/program/#shadownpu-system-and-algorithm-co-design-for-npu-centric-on-device-llm-inference)**
  `MobiSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `prefill` `decode` `npu` `edge` `kernel` `quantization` `latency` `throughput`
  Artifact: [source](https://www.sigmobile.org/mobisys/2026/program/)
  ShadowNPU 将 attention 重要性估计放到 Qualcomm Hexagon NPU 上以 INT8 执行，再把重要 token 索引交给 CPU/GPU 做稀疏高精度 attention，并配合 NPU compute-graph bucketing、head-wise pipeline 和细粒度 sparsity；MobiSys 评审报告端到端最高 4.5x 加速、能耗最高降低 7.7x，精度损失 0.4 个百分点。
- **[TriInfer: Hybrid EPD Disaggregation for Efficient Multimodal Large Language Model Inference](https://openreview.net/forum?id=nNovi8fvGN)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `prefill` `decode` `kv-cache` `scheduler` `multimodal` `slo`
  Artifact: [source](https://mlsys.org/media/mlsys-2026/Slides/3756.pdf)
  TriInfer 在多模态 serving 中把 encode、prefill、decode 作为可组合阶段，按 profile 选择 E/P/D/EP/ED 实例角色；系统包含 stage-level batch scheduler、pull-based KV/image cache migration 和请求处理器，用混合 EPD disaggregation 适配文本与多模态请求的不同瓶颈。
- **[VLMCache: Efficient On-Device Vision-Language Model Inference](https://www.sigmobile.org/mobisys/2026/program/#vlmcache-efficient-on-device-vision-language-model-inference)**
  `MobiSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `prefill` `serving` `edge` `gpu` `kv-cache` `memory` `multimodal` `ttft`
  Artifact: [source](https://doi.org/10.1145/3745756.3809243)
  VLMCache 面向移动端 VLM 的重 prefill，将连续帧中的静态背景与动态前景语义分离，把稳定视觉块编码为可复用 KV prefix，仅对变化区域追加计算，再通过 isolate-then-fuse 恢复跨块 attention 和位置一致性；MobiSys 评审确认其显著降低 TTFT 且仅有很小精度损失。
