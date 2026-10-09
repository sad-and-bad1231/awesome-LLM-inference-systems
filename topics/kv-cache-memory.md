# KV Cache & Context Memory

Inference-time state: cache reuse, placement, offloading, compression, eviction and recovery.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Memory-state mechanisms lead this category; if the main contribution is where prefill/decode runs across GPUs, use Distributed Serving.

**Foundational context.** See also: [PagedAttention/vLLM (2023), Mooncake (2025), Strata (2026)](../README.md#foundational-and-influential-papers).

## Papers (53)

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
| 2025 | [ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2987f911151b39cd3a1761e212319e8e-Abstract-Conference.html) | NeurIPS 2025 | 以语义完整 Chunk 作为 KV 保留单元，并复用跨层保留索引。 |
| 2025 | [Fast State Restoration in LLM Serving with HCache](https://doi.org/10.1145/3689031.3696072) | EuroSys 2025 | 以中间激活恢复状态，配合无 Bubble 调度与分块存储平衡计算/I/O。 |
| 2025 | [FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling](https://arxiv.org/abs/2504.03775) | arXiv 2025 (preprint) | 将分散 KV Page 组织为少量传输段并联合负载感知的 P/D 实例分配，减轻传输碎片。 |
| 2025 | [Marconi: Prefix Caching for the Era of Hybrid LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/7c180af017258d239bac6248d1eb26ac-Abstract-Conference.html) | MLSys 2025 | 针对 Attention+SSM 共同维护的状态建立收益感知 Cache Admission/Eviction。 |
| 2025 | [PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://www.microsoft.com/en-us/research/publication/pyramidkv-dynamic-kv-cache-compression-based-on-pyramidal-information-funneling/) | COLM 2025 | 以分层信息汇聚规律分配不同层的 KV Budget，避免统一保留比例的低效。 |
| 2025 | [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://proceedings.mlr.press/v267/behnam25a.html) | ICML 2025 | 先永久裁剪 KV 再作细粒度 Query-aware 稀疏访问，提供可执行的长上下文 Decode 加速。 |
| 2025 | [SALS: Sparse Attention in Latent Space for KV Cache Compression](https://proceedings.neurips.cc/paper_files/paper/2025/hash/00a0ebcad584c59dbc439c2af8793638-Abstract-Conference.html) | NeurIPS 2025 | 在 RoPE 友好潜空间实现稀疏 KV 表示以减少缓存恢复计算。 |
| 2025 | [Stateful Large Language Model Serving with Pensieve](https://doi.org/10.1145/3689031.3696086) | EuroSys 2025 | 面向会话延续的状态管理与复用，避免每轮请求重复加载/重算上下文。 |
| 2026 | [AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving](https://iclr.cc/virtual/2026/poster/10010915) | ICLR 2026 | AdaCache 把缓存感知的部分重计算与自适应检索深度结合用于 RAG serving，在保留生成质量的同时减少长输入的冗余处理 |
| 2026 | [ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning](https://icml.cc/virtual/2026/poster/63539) | ICML 2026 | ArborKV（ICML 2026）利用推理任务本身的树状结构来组织 KV cache，对树中共享前缀做复用、对分支节点有选择地保留与回收，以在分支式（tree-based）LLM 推理中提升显存效率与吞吐 |
| 2026 | [BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](https://proceedings.mlr.press/v306/kim26af.html) | ICML 2026 | 识别长推理回访 Token，为远端历史状态分配缓存预算。 |
| 2026 | [BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache](https://2026.hpca-conf.org/details/hpca-2026-main-conference/92/BitDecoding-Unlocking-Tensor-Cores-for-Long-Context-LLMs-with-Low-Bit-KV-Cache) | HPCA 2026 | 低比特 KV 布局与 Warp 解量化让 Decode Attention 利用 Tensor Core。 |
| 2026 | [ContextPilot: Fast Long-Context Inference via Context Reuse](https://proceedings.mlsys.org/paper_files/paper/2026/hash/b0131b6ee02a00b03fc3320176fec8f5-Abstract-Conference.html) | MLSys 2026 | ContextPilot 识别可复用上下文片段并规划复用路径，把长上下文请求转化为更少的 prefill 和 cache 恢复操作 |
| 2026 | [DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants](https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan) | NSDI 2026 | DroidSpeak 是首个跨不同 LLM（同架构）复用前缀 KV cache 的分布式推理系统：选择性重算另一模型产生的少数层、复用其余层，并以流水线叠加重算与加载 |
| 2026 | [ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs](https://www.usenix.org/conference/osdi26/presentation/liu-guangda) | OSDI 2026 | 原生 Sparse Attention 的图兼容 KV 淘汰与无损预测预取，把 Recall 与 Indexer 计算流水重叠。 |
| 2026 | [ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving](https://2026.hpca-conf.org/details/hpca-2026-main-conference/13/ELORA-Efficient-LoRA-and-KV-Cache-Management-for-Multi-LoRA-LLM-Serving) | HPCA 2026 | 统一缓存管理器协调 LoRA Adapter 与 KV 驻留及替换。 |
| 2026 | [FAFO: Lossy KV Cache Compression for Lossless Inference Acceleration via Draftless Fumble Decoding](https://proceedings.mlr.press/v306/le26g.html) | ICML 2026 | 结合有损 KV 压缩与 Draftless 验证恢复无损生成分布。 |
| 2026 | [FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management](https://proceedings.mlsys.org/paper_files/paper/2026/hash/94bcb01789fccf15afe2764d8fe0f40e-Abstract-Conference.html) | MLSys 2026 | FlexiCache 利用 attention head 重要性的时间稳定性动态管理 KV cache，减少长上下文生成中不必要的保留和加载 |
| 2026 | [FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference](https://iclr.cc/virtual/2026/poster/10006722) | ICLR 2026 | FreeKV 以推测式检索、CPU/GPU 混合布局与双缓冲流式传输把 KV 选择移出关键路径，报告最高 13× 加速且质量近无损 |
| 2026 | [High Throughput and Low Latency LLM Serving via Adaptive KV Caching](https://doi.org/10.1145/3767295.3803570) | EuroSys 2026 | 动态平衡 KV 保留、重算与 Decode 数据传输。 |
| 2026 | [ICaRus: Identical Cache Reuse for Efficient Multi-Model Inference](https://iclr.cc/virtual/2026/poster/10007206) | ICLR 2026 | ICaRus 让专用模型在多模型与智能体负载中共享相同的提示 KV cache，官方页面报告 P95 延迟最高降 11.1×、吞吐提升 3.8× |
| 2026 | [IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference](https://proceedings.mlr.press/v306/yang26p.html) | ICML 2026 | 学习 KV 重要性并以潜空间记忆补偿淘汰后的信息丢失。 |
| 2026 | [Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost](https://proceedings.mlsys.org/paper_files/paper/2026/hash/e4d8d1b5120be349d3fff8878650cf45-Abstract-Conference.html) | MLSys 2026 | 量化敏感 KV 通道动态保留高精度，使用分页低精度布局与 Triton Kernel。 |
| 2026 | [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://proceedings.mlr.press/v306/xia26f.html) | ICML 2026 | 将位置编码调整下推到 Attention Kernel，实现零拷贝非前缀 KV 复用。 |
| 2026 | [LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/746222c1871d3fa7a94bdacabc34e26c-Abstract-Conference.html) | ICLR 2026 | 通过轻量预测未来 Token 重要性决定缓存淘汰，无需试生成。 |
| 2026 | [LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b241c515433caae3051266668d808b7-Abstract-Conference.html) | ICLR 2026 | 使用语义边界触发长输入长输出的 KV 检索与换入。 |
| 2026 | [MAC-Attention: a Match--Amend--Complete scheme for fast and accurate attention computation](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7398289396de403d7d0505ed791e704a-Abstract-Conference.html) | MLSys 2026 | 对相似 Query 的 Attention 结果进行 Match/Amend/Complete 修正与合并，在不丢弃 KV 的情况下复用计算。 |
| 2026 | [No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs](https://www.usenix.org/conference/osdi26/presentation/luo) | OSDI 2026 | DirectKV 以 Zero-copy 数据路径取消 Offloading Buffer 拷贝与冗余显存。 |
| 2026 | [OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference](https://icml.cc/virtual/2026/poster/62607) | ICML 2026 | OBCache（ICML 2026）把 optimal brain 的剪枝思想迁移到 KV cache，按其重要性评估并剪除低贡献的 KV 条目，在长上下文推理中同时削减 KV 显存与 attention 计算量，并尽量保持生成质量 |
| 2026 | [OPKV: A High-Throughput Plugin-Driven Framework for Recallable Sparsity in Paged KV Cache Systems](https://openreview.net/forum?id=EB5bgzv4qA) | MLSys 2026 | OPKV 为 paged KV cache 提供可插拔稀疏召回框架，使不同稀疏策略能在高吞吐 serving runtime 中复用同一数据通路 |
| 2026 | [PatternKV: Flattening KV Representation Expands Quantization Headroom](https://proceedings.mlr.press/v306/zhang26ci.html) | ICML 2026 | 调整 KV 数值分布以提高低比特缓存量化可行性。 |
| 2026 | [PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving](https://arxiv.org/abs/2602.12029) | arXiv 2026 (preprint) | 共享冻结 Prefill Module，通过 Cache-conditioned Decode 微调与路由实现多模型跨任务 KV 复用。 |
| 2026 | [QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill](https://iclr.cc/virtual/2026/poster/10008892) | ICLR 2026 | QuoKA 在分块 prefill 中用面向 query 的稀疏 attention，只评估 88% 更少的 KV 对即把 TTFT 降低 3×、GPU attention 快 5×、CPU attention 快近 7× |
| 2026 | [RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](https://proceedings.mlr.press/v306/li26al.html) | ICML 2026 | 随机旋转二值量化与二值-INT4 算法加速 KV 重要性预估。 |
| 2026 | [RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse](https://proceedings.mlr.press/v306/geng26a.html) | ICML 2026 | 跨 Agent 重用前一阶段 Decode KV，并局部修正 Prefill 差异。 |
| 2026 | [SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models](https://proceedings.mlsys.org/paper_files/paper/2026/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) | MLSys 2026 | SkipKV 以句子级冗余评分进行 KV 存储淘汰，并用隐空间自适应 steering 跳过冗余句生成，再通过按 prefill 长度重排提升多 batch 的有效 KV 预算 |
| 2026 | [SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer](https://arxiv.org/abs/2607.28150) | arXiv 2026 (preprint) | 主动推送重要 KV、按需并行读取及后续推送全部状态，缩短 P/D 交接等待。 |
| 2026 | [Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token](https://openreview.net/forum?id=FuRo7Ur5Ib) | MLSys 2026 | Stream2LLM 将上下文流式加载与 prefill 计算重叠，把长 prompt 的数据到达时间隐藏到首 token 前的执行流水中 |
| 2026 | [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](https://iclr.cc/virtual/2026/poster/10009980) | ICLR 2026 | ThinKV 结合思维感知低比特量化与渐进式 KV 淘汰并配 PagedAttention 扩展 kernel，官方评测仅保留不到 5% 原缓存却取得至多 5.8× 更高吞吐 |
| 2026 | [TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://proceedings.mlr.press/v306/mao26e.html) | ICML 2026 | 利用三角结构筛选长 Reasoning Trace 的高价值 KV。 |
| 2026 | [Using Span Queries to Optimize Cache and Attention Locality](https://proceedings.mlsys.org/paper_files/paper/2026/hash/f5d77f1e501e0496377d8b68c8e81a48-Abstract-Conference.html) | MLSys 2026 | 使用可交换 Span Query 依赖树统一 Chat/RAG/Agent 的 KV 复用优化。 |
| 2026 | [V-Rex: Real-Time Streaming Video LLM Acceleration via Dynamic KV Cache Retrieval](https://2026.hpca-conf.org/details/hpca-2026-main-conference/55/V-Rex-Real-Time-Streaming-Video-LLM-Acceleration-via-Dynamic-KV-Cache-Retrieval) | HPCA 2026 | 针对视频流的时间相关性动态选择 KV 状态。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
