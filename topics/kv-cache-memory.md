# KV Cache & Context Memory

Inference-time state: cache reuse, placement, offloading, compression, eviction and recovery.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Memory-state mechanisms lead this category: KV/attention-state reuse, eviction and token selection, cache-state compression and quantization, offloading and tiering, paged layout management, prefix/radix caching policy, cross-instance KV state, context reuse and agent session memory. If the main contribution is where prefill or decode runs across GPUs (parallelism, P/D architecture, collectives), or request-level scheduling and SLOs, use Distributed Serving or Runtime & Scheduling instead. Entries are classified by their decisive reusable mechanism, never by model family, workload or hardware.

**Foundational context.** See also: [PagedAttention/vLLM (2023), Mooncake (2025), Strata (2026)](../README.md#foundational-and-influential-papers); rows here that originate a sub-direction of this taxonomy carry an inline `KEEP_FOUNDATIONAL` tag.

## Mechanism map

Eight internal groups, **144 canonical entries in total**. Subsections are a reading/navigation structure, **not new public categories** and not G0–G5 admission verdicts.

| Research mechanism | Papers |
|---|---:|
| [KV Layout, Paging & Memory Management](#kv-layout-paging--memory-management-7) | 7 |
| [Prefix, Radix & Cross-Request KV Reuse](#prefix-radix--cross-request-kv-reuse-23) | 23 |
| [KV Eviction, Token Selection & Budgeted Retention](#kv-eviction-token-selection--budgeted-retention-30) | 30 |
| [Query-Aware KV Selection & Sparse Retrieval](#query-aware-kv-selection--sparse-retrieval-11) | 11 |
| [KV Compression, Quantization & Low-Bit Cache State](#kv-compression-quantization--low-bit-cache-state-22) | 22 |
| [Hierarchical Offloading & Tiered KV Storage](#hierarchical-offloading--tiered-kv-storage-24) | 24 |
| [Distributed, Disaggregated & Cross-Model KV State](#distributed-disaggregated--cross-model-kv-state-14) | 14 |
| [Agent, Session & Multi-Turn KV Memory](#agent-session--multi-turn-kv-memory-13) | 13 |
| **Total** | **144** |

### Where this taxonomy came from

- vLLM 把前缀缓存的语义写成了 KV Block 的哈希身份 + LRU/引用计数驱逐，并把缓存键扩展到 Multi-LoRA 与多模态输入：这决定了本文件把“跨请求复用”与“布局/分页”分成两组（[vLLM Automatic Prefix Caching](https://docs.vllm.ai/en/v0.8.4/design/automatic_prefix_caching.html)）。
- SGLang 把 RadixAttention 的缓存驱逐策略、HiCache 的 Device/Host/Storage 三层、HiSparse 与量化 KV 分成相互独立的文档章节，对应本文件的第 2、3、5、6 组（[SGLang HiCache design](https://docs.sglang.io/docs/advanced_features/hicache_design)）。
- NVIDIA Dynamo 的 KVBM 明确列出 G1 Device / G2 Host pinned / G3 Local SSD / G4 Remote 层级、Block 状态机与 NIXL 远端路径，TensorRT-LLM 另设 KV Cache Connector 与 Offloading，这支撑了“层级卸载”与“跨实例 KV 状态”两组的分工（[Dynamo KVBM design](https://docs.dynamo.nvidia.com/dynamo/v1.4.2/knowledge-base/modular-components/kvbm/kvbm-design.md)、[TensorRT-LLM KV Cache Connector](https://nvidia.github.io/TensorRT-LLM/features/kv-cache-connector.html)）。
- llm-d 把 KV 管理拆成 Prefix-Cache-Aware Routing、KV-Cache Indexer 与 KV-Cache Offloading 三个模块，其中“近似热度 vs 精确 KV 索引”的区分对应本文件的缓存复用与查询感知检索两组（[llm-d KV management](https://llm-d.ai/docs/architecture/advanced/kv-management/prefix-cache-aware-routing)）。
- Mooncake 的 KVCache-centric 分离式架构与 LMCache 的外部共享 KV 层，把 KV 从单机显存对象变成可传输、可分层、可编排的服务级状态（[Mooncake (FAST '25)](https://www.usenix.org/system/files/fast25-qin.pdf)、[LMCache in vLLM](https://docs.vllm.ai/en/stable/examples/disaggregated/lmcache/)）。
- 文献侧的整理方式也与本分类一致：压缩/合并、预算分配、查询感知检索、跨层复用、量化、低秩、系统、观测与评测被分开陈列（[Awesome-LLM-KV-Cache](https://github.com/Zefan-Cai/Awesome-LLM-KV-Cache)、[LLM-inference-optimization-paper](https://github.com/chenhongyu2048/LLM-inference-optimization-paper)）。

**Coverage gaps for later discovery — not new admissions:** ① 本文件没有 LLMLingua 式的上下文/提示压缩条目，因此“Context & Prompt Compression”未单列，其真实条目按复用语义并入第 2 组；② 以“工作负载刻画优先”的条目只有 CacheWise 与 UniCache 两条，故“KV 工作负载刻画与缓存系统分析”并入第 8/2 组而不单独成节；③ 生产环境 KV 轨迹与遥测、MLA 潜在缓存与原生稀疏索引、缺少独立硅验证的 CXL/PIM 近内存原型、共享前缀缓存的确定性与租户公平性、以及 DiT/扩散 KV 状态在本文件中偏薄或缺失；④ 机制缺失不作为把“仅实现细节”材料当作同行评审论文引入的理由。

## Papers (144)

### KV Layout, Paging & Memory Management (7)

**KV 状态的布局、分页与内存管理**：分配器与块表、虚拟内存映射、碎片整理与并行压紧，以及跨层/异构推理状态（Attention+SSM、LoRA、混合精度）的驻留与共享布局。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction](https://doi.org/10.1145/3731569.3764810) | SOSP 2025 | 按 KV 类型、Head 与 Token 非均匀分配缓存预算，并行压缩和布局整理减少 Cache Compaction 关键路径。 |
| 2025 | [Jenga: Effective Memory Management for Serving LLM with Heterogeneity](https://doi.org/10.1145/3731569.3764823) | SOSP 2025 | 统一管理 Hybrid LLM 的异构推理状态及跨请求缓存驻留，适配 Attention/SSM 等不同内存需求。 |
| 2025 | [Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving](https://doi.org/10.1145/3772052.3772215) | SoCC 2025 | 在 CPU/GPU 快互联上单向迁移静态模型层参数以腾出 KV 常驻容量，而非频繁双向交换 KV Cache。 |
| 2025 | [SwiftKV: Fast Prefill-Optimized Inference with Knowledge-Preserving Model Transformation](https://aclanthology.org/2025.emnlp-main.1306/) | EMNLP 2025 | 利用较早 Transformer Layer 输出生成后续层 Prefill KV，再通过轻量蒸馏保留生成质量，并可结合跨层 KV 共享；有公开推理实现和优化 vLLM 端到端实验。历史库误标为 EMNLP 2026。（REQUIRES_FINETUNING / MODEL_CHANGED） |
| 2026 | [ConServe: Contiguity-Preserving Memory Management for Multi-Turn LLM Serving](https://doi.org/10.1109/ISCA66397.2026.00075) | ISCA 2026 | 按会话保留虚拟地址连续性、通过 CUDA VMM 按需映射/懒重映射物理 KV Pages，规避块表访存和地址转换开销；作者报告相对 vLLM/vAttention 的多轮 TTFT/吞吐实测，区别于同名 Online/Offline Co-serving 项目。 |
| 2026 | [ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving](https://2026.hpca-conf.org/details/hpca-2026-main-conference/13/ELORA-Efficient-LoRA-and-KV-Cache-Management-for-Multi-LoRA-LLM-Serving) | HPCA 2026 | 统一缓存管理器协调 LoRA Adapter 与 KV 驻留及替换。 |
| 2026 | [IceCache: Memory-Efficient KV-cache Management for Long-Sequence LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/94de1ef32f1b564b885720ab89fd95af-Abstract-Conference.html) | ICLR 2026 | 将语义相邻 KV Token 聚簇到 PagedAttention 层次结构，改善 CPU/GPU 选择性加载及长期生成精度。 |

### Prefix, Radix & Cross-Request KV Reuse (23)

**跨请求复用相同或相近上下文的 KV**：Prefix/Radix 索引、位置无关缓存、RAG/图检索的非连续块复用、缓存准入与驱逐调度，以及数据库侧的前缀命中优化。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [Prompt Cache: Modular Attention Reuse for Low-Latency Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html) | MLSys 2024 | 通过显式 Prompt Module 与位置约束实现跨请求 Attention State 复用，降低重复前缀处理。（KEEP_FOUNDATIONAL） |
| 2025 | [Cache-Craft: Managing Chunk-Caches for Efficient Retrieval-Augmented Generation](https://doi.org/10.1145/3725273) | PACMMOD 2025 | 跨 RAG Query 复用非连续 Chunk KV，按位置与依赖修正少量重计算，结合 Cache Admission/Eviction 控制质量。 |
| 2025 | [CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion](https://doi.org/10.1145/3689031.3696098) | EuroSys 2025 | 支持非连续知识块 KV 复用，降低 RAG 请求的 Prefill 重计算。（KEEP_FOUNDATIONAL） |
| 2025 | [DepCache: A KV Cache Management Framework for GraphRAG with Dependency Attention](https://doi.org/10.1145/3769778) | PACMMOD 2025 | 针对 GraphRAG 文本/依赖图的 Cache 组织与 Dependency Attention 复用，减少多跳生成的重复 Prefill。 |
| 2025 | [HotPrefix: Hotness-Aware KV Cache Scheduling for Efficient Prefix Sharing in LLM Inference Systems](https://doi.org/10.1145/3749168) | PACMMOD 2025 | 根据 Prefix 热度与缓存效益控制 KV Admission/Placement/Eviction，提高多请求共享 Prefix 的服务效率。 |
| 2025 | [Marconi: Prefix Caching for the Era of Hybrid LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/7c180af017258d239bac6248d1eb26ac-Abstract-Conference.html) | MLSys 2025 | 针对 Attention+SSM 共同维护的状态建立收益感知 Cache Admission/Eviction。 |
| 2026 | [AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving](https://iclr.cc/virtual/2026/poster/10010915) | ICLR 2026 | AdaCache 把缓存感知的部分重计算与自适应检索深度结合用于 RAG serving，在保留生成质量的同时减少长输入的冗余处理 |
| 2026 | [AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse](https://aclanthology.org/2026.acl-long.1990/) | ACL 2026 | 按输出 Entropy 适配 ICL Shot 数，并对旧 Shot Prefix KV 执行语义对齐、RoPE 重编码和拼接复用；作者同时报告 Many-shot Quality 与 Prefill 性能，需核多轮 Serving 适用性。 |
| 2026 | [CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving](https://www.usenix.org/conference/fast26/presentation/liu-yang) | FAST 2026 | 识别 Agent Prompt 中相对位置不变的可复用片段，用 Chunk Positional Encoding 与修正 Attention 处理位置漂移。 |
| 2026 | [ContextPilot: Fast Long-Context Inference via Context Reuse](https://proceedings.mlsys.org/paper_files/paper/2026/hash/b0131b6ee02a00b03fc3320176fec8f5-Abstract-Conference.html) | MLSys 2026 | ContextPilot 识别可复用上下文片段并规划复用路径，把长上下文请求转化为更少的 prefill 和 cache 恢复操作 |
| 2026 | [From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation](https://doi.org/10.1145/3786655) | Proc. ACM Manag. Data 2026 (SIGMOD) | FusionRAG 离线注入跨 Chunk 上下文信息，在线按 Attention 选择性重算失效 KV，以压缩 RAG Prefill TTFT 同时限制复用造成的答案质量下降；作者报告真实端到端推理实验。 |
| 2026 | [HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching](https://arxiv.org/abs/2607.01299) | arXiv 2026 (preprint) | 对 Hybrid Attention 的 Linear Layers 缓存每 Segment 的 State Transition 与 Zero-start End-state，对 Full Attention 只重算边界 Seam Window，冷 Segment 并行 Prefill；四模型五工作负载实测 TTFT/QPS 与准确率。 |
| 2026 | [KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing](https://arxiv.org/abs/2606.17034) | arXiv 2026 (preprint) | 对已缓存对话局部删除执行 Learned KV State Steering，复用未受影响的后缀状态而非全量重 Prefill；报告 1K–32K 上下文的实际延迟与质量权衡。 |
| 2026 | [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://proceedings.mlr.press/v306/xia26f.html) | ICML 2026 | 将位置编码调整下推到 Attention Kernel，实现零拷贝非前缀 KV 复用。 |
| 2026 | [MAC-Attention: a Match--Amend--Complete scheme for fast and accurate attention computation](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7398289396de403d7d0505ed791e704a-Abstract-Conference.html) | MLSys 2026 | 对相似 Query 的 Attention 结果进行 Match/Amend/Complete 修正与合并，在不丢弃 KV 的情况下复用计算。 |
| 2026 | [MiniPIC: Flexible Position-Independent Caching in <100LOC](https://arxiv.org/abs/2606.13126) | arXiv 2026 (preprint) | vLLM 缓存未旋转 Key，算 Attention 时才应用对应 RoPE，并增加 Span Separator/Prompt Depend 等用户 KV 复用原语；在 2WikiMultihopQA 实测 Prefill 吞吐/TTFT。 |
| 2026 | [Models Take Notes at Prefill: KV Cache Can Be Editable and Composable](https://arxiv.org/abs/2606.17107) | arXiv 2026 (preprint) | 将 Prefill KV 解释为可编辑、可 RoPE 重定位的结构化 Notes，利用 Append-only Erratum 和预编译 Segment 复用，提供可执行 KV Editing/Composition 实现及在线 vLLM P90 TTFT、跨模型质量对照；极端收益须结合所选重算基线理解。 |
| 2026 | [Prefix-Cache-Aware Data Reordering for LLM-Augmented Database Analytics](https://proceedings.mlr.press/v306/li26gn.html) | ICML 2026 | SOLO 基于 Prefix Radix Tree 同构关系重排行列 Prompt，让 LLM 增强型数据库分析更容易命中 Prefix KV Cache；有实测 Prefill 吞吐和规划开销。 |
| 2026 | [ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation](https://proceedings.mlr.press/v306/wang26y.html) | ICML 2026 | Query-aware Token Recompute Budget 与 Layer Attention 合并，缓解 RAG KV 复用中 Query-irrelevant Token 的预算挤出；作者报告准确率改善，GPU TTFT 证据待全文审查。 |
| 2026 | [SpecCache: Speculative KV Cache Reuse for Efficient RAG Serving](https://aclanthology.org/2026.acl-long.859/) | ACL 2026 | 以轻量 Draft Model 深层隐状态选出需重算的 RAG KV Token，在近似 Cache Reuse 中权衡 TTFT、吞吐与答案质量；论文报告实测推理效率，需核验评测部署范围。 |
| 2026 | [SubGCache: Accelerating Graph-based RAG with Subgraph-level KV Cache](https://doi.org/10.1609/aaai.v40i41.40827) | AAAI 2026 (full paper) | 用 Graph RAG 子图 Embedding 聚类并为代表子图预计算 KV，跨相似检索子图复用以减少重复 Prefill；作者在三个数据集、多个 LLM 上报告最高 6.68× **TTFT 降低**并比较生成质量。这里复用的是相似而非完全相同的上下文，**APPROXIMATE_QUALITY_CHECKED**；该效果不证明一般 Prompt 的 Exact Prefix 命中、在线 P95、Goodput 或不同检索图的语义等价，基线待严格审计。 |
| 2026 | [Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving (SPIN)](https://arxiv.org/abs/2604.26837) | arXiv 2026 (preprint) | 以统一 KV Partition 和两级 Metadata 兼容多种 Sparse Attention Granularity，GPU-friendly Bucketed LRU 自适应 HBM Budget 并削减 PCIe 小块搬运；在 vLLM 和三种 Sparse Attention 路径实测吞吐、TTFT、TPOT。 |
| 2026 | [VeriCache: Turning Lossy KV Cache into Lossless LLM Inference](https://arxiv.org/abs/2605.17613) | arXiv 2026 (preprint) | 将压缩 KV Decode 作为 Drafter，Full KV 在 CPU/远端以 PCIe/Network 搬回并 Verify，以 HBM Decode/数据传输并行覆盖开销；报告 Full KV 输出一致性与长上下文吞吐。 |

### KV Eviction, Token Selection & Budgeted Retention (30)

**在有限预算内决定保留、丢弃或合并哪些 KV**：重要性打分、Attention Sink 与滑动窗口保留、层/Head 级预算分配，以及推理链与结构化输入的近似保留策略。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2023 | [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html) | NeurIPS 2023 | 基于注意力重尾分布识别 Heavy-Hitter KV，并与 Recent Token 构建高效保留策略。（KEEP_FOUNDATIONAL） |
| 2024 | [Efficient Streaming Language Models with Attention Sinks](https://openreview.net/forum?id=NG7sS51zVF) | ICLR 2024 | Attention Sinks + 滑动窗口缓存使长流式生成无需反复重计算完整上下文。（KEEP_FOUNDATIONAL） |
| 2024 | [Keyformer: KV Cache reduction through key tokens selection for Efficient Generative Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/48fecef47b19fe501d27d338b6d52582-Abstract-Conference.html) | MLSys 2024 | 以关键 Token 选择压缩 KV 访存；同时评估生成性能与质量，属于近似状态保留而非精确缓存。 |
| 2024 | [SnapKV: LLM Knows What You are Looking for Before Generation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/28ab418242603e0f7323e54185d19bde-Abstract-Conference.html) | NeurIPS 2024 | 通过观察窗口中的 Head-specific 重要位置，压缩未来 Decode 要保留的 KV。（KEEP_FOUNDATIONAL） |
| 2025 | [ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2987f911151b39cd3a1761e212319e8e-Abstract-Conference.html) | NeurIPS 2025 | 以语义完整 Chunk 作为 KV 保留单元，并复用跨层保留索引。 |
| 2025 | [EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving](https://arxiv.org/abs/2512.14946) | arXiv 2025 (preprint) | 使用联合 Delay/Quality Utility 决定每条 KV Cache 的 Compress/Evict 与 DRAM/SSD Placement，并在 12 数据集、5 模型上对照同精度下的 TTFT；不是仅测压缩率。 |
| 2025 | [PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://www.microsoft.com/en-us/research/publication/pyramidkv-dynamic-kv-cache-compression-based-on-pyramidal-information-funneling/) | COLM 2025 | 以分层信息汇聚规律分配不同层的 KV Budget，避免统一保留比例的低效。 |
| 2025 | [RefreshKV: Updating Small KV Cache During Long-form Generation](https://aclanthology.org/2025.acl-long.1211/) | ACL 2025 | 长输出期间周期性从 Full KV Attention 刷新小型活跃 KV 集，减轻不可逆 Eviction 失准；A100 上对照 H2O/SnapKV 的输出质量与推理耗时。 |
| 2025 | [SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference](https://papers.neurips.cc/paper_files/paper/2025/hash/45790132b9f91b5787232e1cbe0712fc-Abstract-Conference.html) | NeurIPS 2025 | 利用小模型 Attention 估计补偿大模型 KV Eviction 的 Saliency Shift 与边缘信息损失，并报告长序列质量与真实吞吐基线对照。 |
| 2026 | [ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning](https://icml.cc/virtual/2026/poster/63539) | ICML 2026 | ArborKV（ICML 2026）利用推理任务本身的树状结构来组织 KV cache，对树中共享前缀做复用、对分支节点有选择地保留与回收，以在分支式（tree-based）LLM 推理中提升显存效率与吞吐（HOLD_IDENTITY） |
| 2026 | [BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](https://proceedings.mlr.press/v306/kim26af.html) | ICML 2026 | 识别长推理回访 Token，为远端历史状态分配缓存预算。 |
| 2026 | [Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c3887741ee4e655494770be95303383f-Abstract-Conference.html) | ICLR 2026 | TRIM-KV 以蒸馏得到的逐 Token Retention Gate 和时间衰减分数管理容量受限 KV Cache；作者评测长推理/长上下文质量，尚不能据此声称生产 Serving Goodput 提升。 |
| 2026 | [ContrastKV: Robust KV Cache Eviction via Contrastive Signal Fusion for Multi-Query Generalization](https://aclanthology.org/2026.acl-long.417/) | ACL 2026 | 面向同一知识库多 Query 的 Prefix KV Eviction，融合语义/结构对比信号和跨 Head/Layer 的 Score，在 20% KV 预算下报告质量保留与 Decode Latency；未核实在线 vLLM 工作负载。 |
| 2026 | [CriticalKV: Optimizing KV Cache Eviction from an Output Perturbation Perspective](https://proceedings.mlr.press/v306/feng26j.html) | ICML 2026 | 以 Attention Output Perturbation 约束修正仅按 Attention Weight 选择 KV 的不足；正式出版题名 CriticalKV，作者评估多种 Eviction 基线，非 Serving 端到端认证。 |
| 2026 | [FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management](https://proceedings.mlsys.org/paper_files/paper/2026/hash/94bcb01789fccf15afe2764d8fe0f40e-Abstract-Conference.html) | MLSys 2026 | FlexiCache 利用 attention head 重要性的时间稳定性动态管理 KV cache，减少长上下文生成中不必要的保留和加载 |
| 2026 | [ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution](https://proceedings.mlr.press/v306/dong26h.html) | ICML 2026 | 将 Future Attention Utility 蒸馏为排序策略，再用 GRPO 优化 Reasoning KV Eviction；代码公开，AIME 准确率评测与在线并发 Serving Goodput 应分开解读。 |
| 2026 | [High Throughput and Low Latency LLM Serving via Adaptive KV Caching](https://doi.org/10.1145/3767295.3803570) | EuroSys 2026 | 动态平衡 KV 保留、重算与 Decode 数据传输。（HOLD_EVIDENCE） |
| 2026 | [HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://aclanthology.org/2026.acl-long.594/) | ACL 2026 | 在 Qwen2.5-VL 上区分静态/动态注意力 Head，分配不同 KV Budget 与 Text-prior Pruning/Chunk Retrieval；作者报告 VLM KV 显存及 Decode Latency，不是纯文本 Serving。（KEEP_ADJACENT） |
| 2026 | [IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference](https://proceedings.mlr.press/v306/yang26p.html) | ICML 2026 | 学习 KV 重要性并以潜空间记忆补偿淘汰后的信息丢失。 |
| 2026 | [LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/746222c1871d3fa7a94bdacabc34e26c-Abstract-Conference.html) | ICLR 2026 | 通过轻量预测未来 Token 重要性决定缓存淘汰，无需试生成。 |
| 2026 | [ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection](https://proceedings.mlr.press/v306/datta26b.html) | ICML 2026 | 长上下文的 KV 重要性估计、容量管理与驱逐精度；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [MomentKV: Closing the Directional Gap in KV Cache Eviction for Long-Context Inference](https://arxiv.org/abs/2606.01563) | COLM 2026 (accepted; author preprint) | 不再仅按 Attention Mass 剪枝，而维护 Evicted KV 的 Mean/Covariance Moment，结合 Moment-guided Eviction 与一阶 Missing Attention Output Correction；LLaMA-3.1-8B/Qwen3-4B LongBench、RULER 对照 H2O、SnapKV、PyramidKV、Ada-KV 的**质量-缓存预算**。相对 SnapKV 单 Token 8.2→9.8ms（约 +19.5%）且引入 O(d²) 状态；在线同质量 TTFT/TPOT/Goodput 收益未证明，暂属 G3/G5 HOLD。（HOLD_EVIDENCE） |
| 2026 | [OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference](https://icml.cc/virtual/2026/poster/62607) | ICML 2026 | OBCache（ICML 2026）把 optimal brain 的剪枝思想迁移到 KV cache，按其重要性评估并剪除低贡献的 KV 条目，在长上下文推理中同时削减 KV 显存与 attention 计算量，并尽量保持生成质量 |
| 2026 | [Predicting Future Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction](https://proceedings.mlr.press/v306/tang26i.html) | ICML 2026 (PMLR 306) | LU-KV 针对不同 Attention Heads 的长期效用差异，用凸包松弛与贪心优化分配 KV Budget，并通过离线 Profiling/在线预算查表结合 SnapKV、KeyDiff、EA；作者报告 LongBench/RULER 的缓存、精度和延迟权衡。正式论文身份已核对；Serving Goodput 与 Baseline 公平性仍待严格复审。 |
| 2026 | [ProtoKV: Long-context Knowledges Are Already Well-Organized Before Your Query](https://proceedings.iclr.cc/paper_files/paper/2026/hash/e73ad1f690542144ce354637bb913c35-Abstract-Conference.html) | ICLR 2026 | 长上下文的 KV 重要性估计、容量管理与驱逐精度；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [Question Tells You Where the Answer Is: Intention-aware Long-Context KV Cache Compression](https://aclanthology.org/2026.acl-long.1250/) | ACL 2026 | 长上下文的 KV 重要性估计、容量管理与驱逐精度；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8be9c134bb193d8bd3827d4df8488228-Abstract-Conference.html) | ICLR 2026 | 优化 KV 驱逐后 Layer Output Reconstruction Error，并以时空平滑稳定选择；作者报告长上下文质量及 128K Decode Latency，完整 vLLM 端到端路径待审。 |
| 2026 | [Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective](https://proceedings.mlr.press/v306/yang26bv.html) | ICML 2026 | 长上下文的 KV 重要性估计、容量管理与驱逐精度；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models](https://proceedings.mlsys.org/paper_files/paper/2026/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html) | MLSys 2026 | SkipKV 以句子级冗余评分进行 KV 存储淘汰，并用隐空间自适应 steering 跳过冗余句生成，再通过按 prefill 长度重排提升多 batch 的有效 KV 预算 |
| 2026 | [TriAttention: Efficient Long Reasoning with Trigonometric KV Compression](https://proceedings.mlr.press/v306/mao26e.html) | ICML 2026 | 利用三角结构筛选长 Reasoning Trace 的高价值 KV。 |

### Query-Aware KV Selection & Sparse Retrieval (11)

**按当前 Query 选择真正需要参与 Attention 的 KV**：页/片段粒度查询感知稀疏、召回式稀疏与检索索引，以及把选择与数据搬运移出关键路径的调度。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference](https://proceedings.mlr.press/v235/tang24l.html) | ICML 2024 | 按当前 Query 粗筛 KV Page 再精确算 Attention，降低长上下文 Decode 访存量。（KEEP_FOUNDATIONAL） |
| 2025 | [AlayaDB: The Data Foundation for Efficient and Effective Long-context LLM Inference](https://doi.org/10.1145/3722212.3724428) | SIGMOD 2025 | 将 KV Cache 与 Attention 计算抽象为数据库 Query Processing，并以独立 Query Optimizer 为长上下文推理选择执行计划；包含工业案例和推理系统实验。 |
| 2025 | [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://proceedings.mlr.press/v267/behnam25a.html) | ICML 2025 | 先永久裁剪 KV 再作细粒度 Query-aware 稀疏访问，提供可执行的长上下文 Decode 加速。 |
| 2026 | [ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs](https://www.usenix.org/conference/osdi26/presentation/liu-guangda) | OSDI 2026 | 原生 Sparse Attention 的图兼容 KV 淘汰与无损预测预取，把 Recall 与 Indexer 计算流水重叠。 |
| 2026 | [FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference](https://iclr.cc/virtual/2026/poster/10006722) | ICLR 2026 | FreeKV 以推测式检索、CPU/GPU 混合布局与双缓冲流式传输把 KV 选择移出关键路径，报告最高 13× 加速且质量近无损 |
| 2026 | [LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b241c515433caae3051266668d808b7-Abstract-Conference.html) | ICLR 2026 | 使用语义边界触发长输入长输出的 KV 检索与换入。 |
| 2026 | [OPKV: A High-Throughput Plugin-Driven Framework for Recallable Sparsity in Paged KV Cache Systems](https://openreview.net/forum?id=EB5bgzv4qA) | MLSys 2026 | OPKV 为 paged KV cache 提供可插拔稀疏召回框架，使不同稀疏策略能在高吞吐 serving runtime 中复用同一数据通路 |
| 2026 | [QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill](https://iclr.cc/virtual/2026/poster/10008892) | ICLR 2026 | QuoKA 在分块 prefill 中用面向 query 的稀疏 attention，只评估 88% 更少的 KV 对即把 TTFT 降低 3×、GPU attention 快 5×、CPU attention 快近 7× |
| 2026 | [RetroInfer: A Vector Storage Engine for Scalable Long-Context LLM Inference](https://doi.org/10.14778/3796195.3796212) | PVLDB 2026 | 以 Attention-aware Wave Index 对远端 KV 执行候选检索，并通过 GPU/CPU Wave Buffer 联合降低稀疏 Attention 的索引与数据搬运开销。 |
| 2026 | [SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs](https://doi.org/10.1145/3779212.3790224) | ASPLOS 2026 | 以 Distilled Retrieval Head 预测原模型关注的长上下文 KV，异步预取和 Elastic KV Residency 重叠 GPU 计算；在云端和边缘实机评估准确率/吞吐/显存折中。 |
| 2026 | [Using Span Queries to Optimize Cache and Attention Locality](https://proceedings.mlsys.org/paper_files/paper/2026/hash/f5d77f1e501e0496377d8b68c8e81a48-Abstract-Conference.html) | MLSys 2026 | 使用可交换 Span Query 依赖树统一 Chat/RAG/Agent 的 KV 复用优化。 |

### KV Compression, Quantization & Low-Bit Cache State (22)

**对 KV 缓存状态本身的数值与表示压缩**：低比特与混精度量化、变换编码与矢量量化、低秩分解、跨请求共享编码，以及有损压缩的校验/恢复。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [KIVI: A Tuning-Free Asymmetric 2bit Quantization for KV Cache](https://proceedings.mlr.press/v235/liu24bz.html) | ICML 2024 | 根据 K/V 分布差异实行 Key 按通道和 Value 按 Token 量化，低精度保留推理状态。（KEEP_FOUNDATIONAL） |
| 2024 | [KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization](https://proceedings.neurips.cc/paper_files/paper/2024/hash/028fcbcf85435d39a40c4d61b42c99a4-Abstract-Conference.html) | NeurIPS 2024 | 针对 KV Outlier 和分布设计非均匀低比特量化，加速极长上下文 Decode。（KEEP_FOUNDATIONAL） |
| 2025 | [HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference](https://arxiv.org/abs/2502.03589) | arXiv 2025 (SIGCOMM 2025 poster) | 压缩跨 P/D 节点传输的 KV，并在量化表示上直接执行部分 Attention 计算，减少解量化与通信开销。 |
| 2025 | [SALS: Sparse Attention in Latent Space for KV Cache Compression](https://proceedings.neurips.cc/paper_files/paper/2025/hash/00a0ebcad584c59dbc439c2af8793638-Abstract-Conference.html) | NeurIPS 2025 | 在 RoPE 友好潜空间实现稀疏 KV 表示以减少缓存恢复计算。 |
| 2026 | [Channel-Aware Mixed-Precision Quantization for Efficient Long-Context Inference](https://proceedings.iclr.cc/paper_files/paper/2026/hash/55f5aa8d997a8071d0651e0009ec49a2-Abstract-Conference.html) | ICLR 2026 | ChanMix 通过敏感度驱动的逐 Channel Bit Reallocation 支持 2-bit KV 量化与 Triton Kernel，作者报告更高 Batch/更长 Context；需核质量和设备边界。 |
| 2026 | [FAFO: Lossy KV Cache Compression for Lossless Inference Acceleration via Draftless Fumble Decoding](https://proceedings.mlr.press/v306/le26g.html) | ICML 2026 | 结合有损 KV 压缩与 Draftless 验证恢复无损生成分布。 |
| 2026 | [FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://proceedings.mlr.press/v306/samuel26a.html) | ICML 2026 | 面向 Video World Model 的长时流式推理，以 TempCache 时间对应压缩 KV、ANN Cross/Self-Attention 限制冗余访问；作者实测长 Rollout 时延和 Peak GPU Memory（邻接领域，非文本 LLM）。（KEEP_ADJACENT） |
| 2026 | [Joint Encoding of KV-Cache Blocks for Scalable LLM Serving](https://arxiv.org/abs/2601.03067) | arXiv 2026 (preprint) | 跨请求与 Prompt Chunk 共享相似 KV Block 的融合表示，并保持标准缓存布局；有公开实现和单机 vLLM Token Throughput 测试，区分有损压缩和量化精度折中。 |
| 2026 | [Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost](https://proceedings.mlsys.org/paper_files/paper/2026/hash/e4d8d1b5120be349d3fff8878650cf45-Abstract-Conference.html) | MLSys 2026 | 量化敏感 KV 通道动态保留高精度，使用分页低精度布局与 Triton Kernel。 |
| 2026 | [KV Cache Reuse for Elastic LLM Inference on Edge Devices](https://doi.org/10.1109/2575-8411.2026.00035) | ICDCS 2026 | ElastKV 在端侧不同量化精度模型间保留混精度 KV，按估计贡献局部重算以降低设备精度切换代价；正式 IEEE 论文，需复核物理边缘设备与量化转换开销。（HOLD_EVIDENCE） |
| 2026 | [KV Cache Transform Coding for Compact Storage in LLM Inference](https://openreview.net/pdf?id=aNVKROYpLB) | ICLR 2026 | KVTC 将 PCA 特征去相关、分配精度的量化和熵编码组合用于可复用 KV Cache 的 GPU/Offload 压缩；报告跨 Llama/Mistral 模型的准确率-空间开销比较，压缩比不直接等价于 Serving Goodput。 |
| 2026 | [MixKVQ: Query-Aware Mixed-Precision KV Cache Quantization for Long-Context Reasoning](https://aclanthology.org/2026.acl-long.326/) | ACL 2026 | 低比特量化或低秩表示下的 KV 体积、保真与访问开销；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [MuKV: Multi-Grained KV Cache Compression for Long Streaming Video Question-Answering](https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_MuKV_Multi-Grained_KV_Cache_Compression_for_Long_Streaming_Video_Question-Answering_CVPR_2026_paper.html) | CVPR 2026 | 流式视频理解中的 KV 存储、压缩及时间窗口；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（KEEP_ADJACENT / HOLD_EVIDENCE） |
| 2026 | [Near-Zero Cost KV Cache Compression for Large Language Model Inference](https://doi.org/10.1109/IPDPS65963.2026.00058) | IPDPS 2026 | 已核对正式出版 DOI，但本轮尚未独立检查完整论文中的算法、Kernel 压缩/解压开销、模型质量和 TTFT/TPOT/Goodput；保持证据待审，不推定“near-zero”意味着服务层零开销。（HOLD_EVIDENCE） |
| 2026 | [PackKV: Reducing KV Cache Memory Footprint through LLM-Aware Lossy Compression](https://doi.org/10.1109/IPDPS65963.2026.00057) | IPDPS 2026 (full paper) | 对长上下文 KV 用有损自适应压缩，融合解压与 CUDA GEMV，论文 A100/RTX Pro 6000 Kernel 实测相较 **cuBLAS GEMV** 报告 K/V 平均 +75.7%/+171.7% *Kernel Throughput*，并报告相对其他 Quantization 的压缩与精度权衡。作者 [Artifact](https://github.com/BoJiang03/PackKV) 提供 CUDA Extensions、Benchmark 和 Evaluation，依赖 CUDA 12.8/13.0、特定 torch/FlashAttention 且适配 SM80/120；**未证明 vLLM/SGLang Online TTFT/Goodput 增益**。 |
| 2026 | [PatternKV: Flattening KV Representation Expands Quantization Headroom](https://proceedings.mlr.press/v306/zhang26ci.html) | ICML 2026 | 调整 KV 数值分布以提高低比特缓存量化可行性。 |
| 2026 | [PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/afb8caec018d3c8f6ef8b81fa52386fe-Abstract-Conference.html) | ICLR 2026 | 将长 CoT 的 KV 随生成进度渐进降 Bitwidth，以 Block 敏感度分配精度，并通过位置插值改进长序列校准；有公开代码与 LLM 推理吞吐/推理质量对照。 |
| 2026 | [RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](https://proceedings.mlr.press/v306/li26al.html) | ICML 2026 | 随机旋转二值量化与二值-INT4 算法加速 KV 重要性预估。 |
| 2026 | [STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://proceedings.mlr.press/v306/bhatnagar26a.html) | ICML 2026 | 通过 Soft Threshold 自适应 Rank、K/V 不对称低秩与混合量化压缩 KV；提供 Triton Kernel，并报告 Attention 与整体 Generation Throughput。 |
| 2026 | [ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models](https://iclr.cc/virtual/2026/poster/10009980) | ICLR 2026 | ThinKV 结合思维感知低比特量化与渐进式 KV 淘汰并配 PagedAttention 扩展 kernel，官方评测仅保留不到 5% 原缓存却取得至多 5.8× 更高吞吐 |
| 2026 | [V-Rex: Real-Time Streaming Video LLM Acceleration via Dynamic KV Cache Retrieval](https://2026.hpca-conf.org/details/hpca-2026-main-conference/55/V-Rex-Real-Time-Streaming-Video-LLM-Acceleration-via-Dynamic-KV-Cache-Retrieval) | HPCA 2026 | 针对视频流的时间相关性动态选择 KV 状态。（KEEP_ADJACENT） |
| 2026 | [VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization](https://aclanthology.org/2026.acl-long.1454/) | ACL 2026 | 采用 Smooth/Hadamard 抑制 K 的异常值提升低 Bit Codebook 利用率，并设计 CUDA Fused Dequant–Attention Kernel；论文在 Llama-3.1-8B 196K 上报告 2-bit 单批完整推理延迟收益与质量，仍需独立复现。 |

### Hierarchical Offloading & Tiered KV Storage (24)

**在实例内内存层次之间放置与搬运 KV**：HBM / Host DRAM / 本地 SSD-NVMe / CXL-attached 内存、近存储与近内存计算、预取与 I/O 重叠、零拷贝数据路径与状态恢复。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management](https://www.usenix.org/conference/osdi24/presentation/lee) | OSDI 2024 | 预测关键 KV 项并按需预取，避免长上下文 Offloading 的全量回传。（KEEP_FOUNDATIONAL） |
| 2025 | [AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving](https://www.microsoft.com/en-us/research/publication/adaptcache-kv-cache-native-storage-hierarchy-for-low-delay-and-high-quality-language-model-serving/) | SOSP BigMem Workshop 2025 | 以每条 KV Entry 的有损压缩算法、压缩率和 DRAM/SSD 分层放置联合优化缓存 Load Delay 与生成质量；三类任务报告固定质量下延迟改善，明确仅为 Workshop。 |
| 2025 | [Fast State Restoration in LLM Serving with HCache](https://doi.org/10.1145/3689031.3696072) | EuroSys 2025 | 以中间激活恢复状态，配合无 Bubble 调度与分块存储平衡计算/I/O。 |
| 2025 | [InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference](https://doi.org/10.1109/HPCA61900.2025.00113) | HPCA 2025 | 把 Decode Attention 与 KV 存储下沉到计算型 SSD，优化 GPU–存储 P2P 传输以减少 PCIe 往返。 |
| 2025 | [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://proceedings.mlr.press/v267/sun25b.html) | ICML 2025 | 保留低秩 Key/索引在 GPU，Value Offload 到 CPU 并按 Query 稀疏取回 KV，平衡长上下文质量与吞吐。 |
| 2026 | [A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs (HILOS)](https://doi.org/10.1145/3779212.3790119) | ASPLOS 2026 | 在 16 块真实 SmartSSD 上把长上下文 Attention 下沉到 Near-Storage，协同 X-cache 和延迟 KV Writeback；论文提供 HLS 与端到端推理部署/基线复现代码。 |
| 2026 | [Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching](https://doi.org/10.1609/aaai.v40i25.39224) | AAAI 2026 (full paper) | 采用 Hopper `cp.async.bulk.prefetch.L2.global`，在 Attention 计算期间将未来 KV Blocks 异步预取至 L2，缓解 XFormers 访存 Stall。原论文于 H20 真实 1/2/4/8 GPU、vLLM 0.7.1 的固定 512 Prompt/512–8192 Decode、Batch 1–128 对比 XFormers/FA3，报告 Kernel 最多 2.15×、**端到端 Tokens/s** 最多 1.97×；[作者 Patch](https://github.com/alibaba/vllm_xformers_prefetch) 后来标称 vLLM 0.10.2，版本/现代基线与动态 SLO Goodput 仍需复验。（HOLD_EVIDENCE） |
| 2026 | [Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation–Storage Awareness](https://www.usenix.org/conference/fast26/presentation/hu-shipeng) | FAST 2026 | 让 KV 加载延迟参与 Serving 排队，并用生成响应预测 Host/SSD 层次缓存重用和驱逐。 |
| 2026 | [CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration](https://arxiv.org/abs/2604.25080) | arXiv 2026 (preprint) | 对 KV Restore 统一 Token/Layer/GPU 三维计算-I/O 并行，加入 Batch-aware 双指针资源调度；论文报告多模型、负载与硬件 TTFT 对照。 |
| 2026 | [Dual-Blade: Dual-Path NVMe-Direct KV-Cache Offloading for Edge LLM Inference](https://doi.org/10.1109/2575-8411.2026.00065) | ICDCS 2026 | 按内存压力将 KV 映射至 Linux Page Cache 或 NVMe 直接 LBA 路径，同时 Pipeline SSD I/O 与 GPU DMA；论文报告真实边缘 GPU+NVMe Prefill/Decode 延迟，需审查正确性与缓存污染。 |
| 2026 | [HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/abs/2606.21633) | arXiv 2026 (preprint) | 在 Block dLLM 中将每 Block 一次的 Sparse KV Selection 移至 CPU，多次 Denoise 留在 GPU，采用 Draft Block 与双流缓冲重叠；两类实际 Block dLLM 上测吞吐与精度。 |
| 2026 | [HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding](https://aclanthology.org/2026.acl-long.381/) | ACL 2026 | 将连续视频输入转化为层次化 KV Memory，复用紧凑缓存实现无额外 Query Arrival 计算的流式回答；有 Qwen2.5-VL/LLaVA 官方实现与 TTFT 测量，属于相邻 Streaming Video LLM。（KEEP_ADJACENT） |
| 2026 | [HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference](https://aclanthology.org/2026.acl-long.1999/) | ACL 2026 | 按注意力 Head 的时间漂移和跨 Head 相似性分配 KV 容量，使用代表 Head 触发异步分层历史 KV Retrieval 以隐藏 I/O；有公开代码和长上下文实测。 |
| 2026 | [KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference](https://doi.org/10.1145/3802077) | PACMMOD 2026 | 联合管理 GPU/DRAM/SSD KV 驻留、注意力访问模式与跨层 I/O Pipeline，避免稀疏访问被缓存传输阻塞。 |
| 2026 | [KVSwap: Disk-aware KV Cache Offloading for Long-Context On-device Inference](https://arxiv.org/abs/2511.11907) | MobiSys 2026 | 以磁盘友好的 KV 布局和元数据预测选择性预取，重叠存储读写与设备长上下文 Decode。 |
| 2026 | [MatKV: Trading Compute for Flash Storage in LLM Inference](https://doi.org/10.1109/ICDE65706.2026.00071) | ICDE 2026 | 离线物化 RAG 文档 KV 到 SSD，在推理时读取替代重复 Prefill，并将 KV 加载与 Decode 重叠；提供真实 GPU/Flash 设备测量与开源实现，需关注上下文拼接正确性。 |
| 2026 | [No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs](https://www.usenix.org/conference/osdi26/presentation/luo) | OSDI 2026 | DirectKV 以 Zero-copy 数据路径取消 Offloading Buffer 拷贝与冗余显存。 |
| 2026 | [OrbitFlow: SLO-Aware Long-Context LLM Serving with Fine-Grained KV Cache Reconfiguration](https://doi.org/10.14778/3796195.3796214) | PVLDB 2026 | 用轻量 ILP 动态决定每个请求在 GPU 上保留哪些 Layer KV，运行时反馈更新 Offloading 计划以满足 TPOT SLO。 |
| 2026 | [Scaling Attention Beyond GPUs for LLM Inference](https://doi.org/10.1145/3806645.3807596) | HPDC 2026 | Beyond 使用 GPU 最近 KV 上的 Dense Attention 与 CPU 重要历史 KV 上的 Sparse Attention 并发执行，再以 LogSumExp 合并，减少 PCIe 搬运并扩大 Batch/Context；实机 CPU–GPU 系统。 |
| 2026 | [SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs](https://www.usenix.org/conference/fast26/presentation/zheng) | FAST 2026 | 对稀疏 Attention 的 KV 访问按大块写入 SSD 并做时序局部性预测预取，重叠 Attention 与 SSD I/O。 |
| 2026 | [SparseServe: Unlocking Parallelism for Dynamic Sparse Attention in Long-Context LLM Serving](https://arxiv.org/abs/2509.24626) | ICS 2026 | 针对动态稀疏 Attention 实现碎片感知 KV 传输、Working-set-aware Batch 和分层 Prefill，缓解 HBM 容量瓶颈。 |
| 2026 | [Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token](https://openreview.net/forum?id=FuRo7Ur5Ib) | MLSys 2026 | Stream2LLM 将上下文流式加载与 prefill 计算重叠，把长 prompt 的数据到达时间隐藏到首 token 前的执行流水中 |
| 2026 | [Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving](https://arxiv.org/abs/2605.03375) | arXiv 2026 (preprint) | 以 GPU-native KV Object Store、GPU io_uring 和 Slack-aware I/O Scheduling 避开 SSD KV Restore 的 CPU 小 I/O 控制路径，已集成 vLLM 并开源，实测对 GDS-enabled SSD LMCache 的 TTFT、QPS 和 GPU Stall。 |
| 2026 | [UniCache: Unifying Prefix Cache Eviction for Heterogeneous LLM Serving Workloads](https://doi.org/10.1145/3805652) | Proc. ACM Meas. Anal. Comput. Syst. 2026 (SIGMETRICS 2026) | 基于多轮对话与单轮 API 请求的异质 Prefix Reuse 特征设计 Eviction，提供 vLLM 控制面 Trace Simulator 与 GPU Demo；大规模结果以模拟 Trace 为主，不能直接代表实机 Serving 收益。（HOLD_EVIDENCE） |

### Distributed, Disaggregated & Cross-Model KV State (14)

**跨实例、跨节点与跨模型的 KV 状态迁移与共享**：P/D KV 传输与调度、全局/机架级 KV 池、跨模型变体与多模型缓存复用、远端缓存压缩加载。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving](https://doi.org/10.1145/3651890.3672274) | SIGCOMM 2024 | 基于上下文传输的 KV Cache 压缩与流式发送，优化远端缓存加载关键路径。（KEEP_FOUNDATIONAL） |
| 2025 | [FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling](https://arxiv.org/abs/2504.03775) | arXiv 2025 (preprint) | 将分散 KV Page 组织为少量传输段并联合负载感知的 P/D 实例分配，减轻传输碎片。 |
| 2025 | [LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference](https://arxiv.org/abs/2510.09665) | arXiv 2025 (technical report) | 为 vLLM/SGLang 提供可共享的外部 KV Layer，支持跨引擎缓存移动、分层驻留、P/D Disaggregation 与可编排控制 API。（KEEP_FOUNDATIONAL） |
| 2025 | [TraCT: Disaggregated LLM Serving with CXL Shared Memory KV Cache at Rack-Scale](https://arxiv.org/abs/2512.18194) | arXiv 2025 (preprint) | 以跨主机 CXL Shared Memory 取代网络 RDMA 作为 P/D KV Transfer 与 Prefix Cache，补上跨机 Lock/Consistency/Shared Directory；Dynamo 原型及论文和技术报告均提供真实 Serving 测量。 |
| 2026 | [CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving](https://doi.org/10.1145/3748173.3779188) | FPGA 2026 | 将 CXL 远端 KV Pool、预测式 Cache Prefetch 与 FPGA 压缩/解压整合到 LLM 服务路径，提供硬件 RTL/Driver 代码及论文性能对照。 |
| 2026 | [DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants](https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan) | NSDI 2026 | DroidSpeak 是首个跨不同 LLM（同架构）复用前缀 KV cache 的分布式推理系统：选择性重算另一模型产生的少数层、复用其余层，并以流水线叠加重算与加载 |
| 2026 | [Efficient Remote KV Cache Reuse with GPU-native Video Codec](https://doi.org/10.1145/3789240.3829120) | SIGCOMM 2026 | 复用 GPU Video Codec 压缩并传输远端 KV Cache，在解码端快速还原以降低跨节点 Cache 加载开销。 |
| 2026 | [ICaRus: Identical Cache Reuse for Efficient Multi-Model Inference](https://iclr.cc/virtual/2026/poster/10007206) | ICLR 2026 | ICaRus 让专用模型在多模型与智能体负载中共享相同的提示 KV cache，官方页面报告 P95 延迟最高降 11.1×、吞吐提升 3.8× |
| 2026 | [ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories](https://arxiv.org/abs/2606.12556) | arXiv 2026 (preprint) | 利用 CXL Hybrid Memory 将模型权重和 Prefix KV 映射到跨节点 Byte-addressable Memory 层；报告 SK hynix CMM 与 PCIe Gen5 设备测量及 FPGA 功能原型。 |
| 2026 | [KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving](https://doi.org/10.1145/3789240.3829139) | SIGCOMM 2026 | 按网络/服务 SLO 与质量损失预算自适应选择 KV Compression 及远端复用策略。 |
| 2026 | [PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving](https://arxiv.org/abs/2602.12029) | arXiv 2026 (preprint) | 共享冻结 Prefill Module，通过 Cache-conditioned Decode 微调与路由实现多模型跨任务 KV 复用。（REQUIRES_FINETUNING / MODEL_CHANGED） |
| 2026 | [SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL](https://arxiv.org/abs/2606.19746) | arXiv 2026 (preprint) | 将 DeepSeek-V3.2 稀疏 Attention KV Payload 放 CXL Pool，按索引选中的 Top-k 向量粒度搬运，而非 RDMA 整段传输；SGLang/HiSparse 和 H20+CXL 实机测 TTFT/TBT/吞吐。 |
| 2026 | [SmartGen: Seamless Disaggregated LLM Inference with Selective KV Cache Transfer](https://arxiv.org/abs/2607.28150) | arXiv 2026 (preprint) | 主动推送重要 KV、按需并行读取及后续推送全部状态，缩短 P/D 交接等待。 |
| 2026 | [SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing](https://arxiv.org/abs/2606.16135) | arXiv 2026 (preprint) | 让多个异构模型跨 NVLink 捐赠空闲 GPU HBM 作为会话 Prefix KV Cache，并令本地只保持活动层 KV；在真实多轮 Serving 负载对比 vLLM/SGLang 的 P99 TTFT、上下文长度及干扰。 |

### Agent, Session & Multi-Turn KV Memory (13)

**由会话、多轮与智能体结构驱动的 KV 记忆管理**：跨轮持久化与恢复、工具返回与计划状态的复用、多智能体/多 LoRA 共享、长期会话与流式交互记忆。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention](https://www.usenix.org/conference/atc24/presentation/gao-bin-cost) | USENIX ATC 2024 | CachedAttention 以跨会话分层 KV 持久化、逐层异步预取和 Scheduler-aware Eviction 降低多轮 Prefill 重算。（KEEP_FOUNDATIONAL） |
| 2025 | [Accelerating LLM Serving for Multi-turn Dialogues with Efficient Resource Management](https://doi.org/10.1145/3676641.3716245) | ASPLOS 2025 | FlashGen 面向多轮会话在 GPU/CPU/SSD 三层保留与搬运 KV Cache，并重排请求降低跨轮 Prefill 重计算。 |
| 2025 | [Stateful Large Language Model Serving with Pensieve](https://doi.org/10.1145/3689031.3696086) | EuroSys 2025 | 面向会话延续的状态管理与复用，避免每轮请求重复加载/重算上下文。 |
| 2025 | [TokenCake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications](https://arxiv.org/abs/2510.18586) | arXiv 2025 (updated 2026; NOT 2027 proceedings) | 以 Agent DAG 的 Critical Path/Tool-call Stalls 驱动 KV Spatial Partition、Event-triggered Offload 与预测性 Upload；在多 Agent Workload 和公开 vLLM Integration 比较 JCT 与显存利用率。 |
| 2026 | [CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents](https://arxiv.org/abs/2606.16824) | arXiv 2026 (preprint) | 基于真实 Coding Agent Session Traces，利用工具调用元数据进行 Prefix-aware Scheduling 与 Reuse-aware Eviction；在 vLLM 实现后对照 Agent 完整 Session 时间、驱逐次数。 |
| 2026 | [EpiCache: Episodic KV Cache Management for Long-Term Conversation on Resource-Constrained Environments](https://proceedings.mlr.press/v306/kim26ag.html) | ICML 2026 | Block-wise Prefill 限制多轮长对话的峰值 KV Cache，按 Topic Episode 进行缓存驱逐；报告准确率、峰值显存和延迟，非生产 vLLM Goodput 证据。 |
| 2026 | [KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning](https://arxiv.org/abs/2602.23592) | arXiv 2026 (preprint) | 对 Embodied Planning 的静态/动态记忆分组缓存 KV，以 Multi-hop 局部重算和 Layer-balanced Loading 避免失效/流水失衡；有代码和 ALFRED 真实推理实验，对比 CacheBlend 的 TTFT 与任务成功率。 |
| 2026 | [LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents](https://proceedings.mlr.press/v306/jeon26b.html) | ICML 2026 | 在不同 LoRA Agent 之间复用底座 KV，仅保存低秩 Adapter 增量，利用 Flash-LoRA-Attention 避免恢复全维物化；TTFT/吞吐和精度均有作者评估。 |
| 2026 | [RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse](https://proceedings.mlr.press/v306/geng26a.html) | ICML 2026 | 跨 Agent 重用前一阶段 Decode KV，并局部修正 Prefill 差异。 |
| 2026 | [SideQuest: Model-Driven KV Cache Management for Long-Horizon Agentic Workloads](https://openreview.net/forum?id=wNjm4WVkOW) | COLM 2026 (accepted; author preprint title: *Reasoning*) | 将 Agent Tool Responses 的 KV Eviction 决策移至并行辅助推理线程，而非固定 Attention Heuristic；需对 gpt-oss-20b 以 215 样本进行 LoRA 适配（**REQUIRES_FINETUNING / APPROXIMATE_QUALITY_CHECKED**）。作者报告 FRAMES/BrowseComp 质量与 KV 峰值，并提供 H100/SGLang 在线吞吐、全任务时间测试；不能与无需训练、输出等价的 KV Eviction 混比。G4/在线成本归因待核验。 |
| 2026 | [TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing](https://arxiv.org/abs/2604.03143) | arXiv 2026 (preprint) | 抓住多 Agent Round 的 All-Gather 输出模式，以跨 Agent Collective KV Reuse 和 Master-Mirror 稀疏 Delta 消除重复 Prefix；GenerativeAgents/AgentSociety 测量并发 Agent、KV 容量与 Prefill。 |
| 2026 | [VLMCache: Efficient On-Device Vision-Language Model Inference](https://doi.org/10.1145/3745756.3809243) | MobiSys 2026 | 将稳定视觉区域编码为可复用 KV Prefix，对动态前景重算后以 Isolate-then-fuse 保留 Attention 与位置一致性。（KEEP_ADJACENT） |
| 2026 | [WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling](https://proceedings.mlr.press/v306/sun26az.html) | ICML 2026 | 交互式视频 World Model 通过 Reconstituted Context Memory 动态重建历史帧上下文并控制长期漂移，配合 Context Forcing 蒸馏实现实测实时流式生成；属于模型-推理状态协同设计（邻接领域）。（KEEP_ADJACENT） |

---
*Publication source and mechanism screened; speedup claims are not independently reproduced. Kernel- or quality-level gains are not service-level TTFT/TPOT/Goodput, and explicit HOLD tags remain unresolved strict-review items.*
