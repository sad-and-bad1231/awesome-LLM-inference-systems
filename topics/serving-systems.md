# Serving systems · legacy selection

*Runtime · Scheduling · Resource management · Disaggregated serving*

**Legacy cohort (50 papers, 2024–2026), pending individual source and mechanism re-audit.** This index is frozen: new admission and canonical technical categorization occur under the [eight topic pages](README.md). Original scope: an intentionally selective set of works. Its boundary is the **request-to-GPU execution path**: routing, batching, KV state, disaggregation, parallelism, elastic capacity, multi-model service and production workloads. Specific kernel work appears only where tightly co-designed with serving.

> **Evidence standard:** venue and identity checked against publisher/conference/author records. The fourth column is an editorial summary of the *proposed mechanism*, not an independently replicated performance claim. Entries link to a publisher paper page, the author's PDF, or an official conference program (if a stable per-paper page was not available). Not a ranking.

[← Home](../README.md) · [Curation policy](../CURATION.md)

## Navigation

- **2024:** foundational resource-aware and multi-tenant serving
- **2025:** SLOs, phase separation, cache restoration, energy and autoscaling
- **2026:** fine-grained scheduling, elastic P/D, heterogeneous multi-node serving

## 2024 (6)

| Paper | Venue | Systems lens | Distinct contribution |
|---|---|---|---|
| [ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference](https://www.asplos-conference.org/asplos2024/main-program/abstracts/) | ASPLOS 2024 | SLO / Resource allocation | 将推理资源配置与约束条件共同纳入调度，比较部署配置的延迟与吞吐。 |
| [MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving](https://proceedings.mlr.press/v235/duan24a.html) | ICML 2024 | Multi-model | 按模型热度联合空间/时间复用显存与计算，区分 Prefill/Decode 的资源需求。 |
| [Punica: Multi-Tenant LoRA Serving](https://proceedings.mlsys.org/paper_files/paper/2024/file/054de805fcceb78a201f5e9d53c85908-Paper-Conference.pdf) | MLSys 2024 | Multi-tenant | 以 SGMV Kernel 合批不同 LoRA Adapter 的 Decode，并统一调度多租户请求。 |
| [SpotServe: Serving Generative Large Language Models on Preemptible Instances](https://www.asplos-conference.org/asplos2024/main-program/abstracts/) | ASPLOS 2024 | Elasticity / Recovery | 针对 Spot 抢占实施动态重并行、低成本实例迁移和有状态恢复。 |
| [ServerlessLLM: Low-Latency Serverless Inference for Large Language Models](https://www.usenix.org/conference/osdi24/presentation/fu) | OSDI 2024 | Serverless / Cold start | 多层 Checkpoint Loading、位置感知调度与推理迁移协同减少冷启动。 |
| [InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management](https://www.usenix.org/conference/osdi24/presentation/lee) | OSDI 2024 | KV / CPU offload | 预测关键 KV 项并按需预取，避免长上下文 Offloading 的全量回传。 |

## 2025 (19)

| Paper | Venue | Systems lens | Distinct contribution |
|---|---|---|---|
| [Preble: Efficient Distributed Prompt Scheduling for LLM Serving](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5bc342f48de8264779952fac378f96dc-Abstract-Conference.html) | ICLR 2025 | Prefix-aware routing | 在分布式请求调度中联合 KV 复用收益与负载均衡，复用重复 Prompt。 |
| [SOLA: Optimizing SLO Attainment for Large Language Model Serving with State-Aware Scheduling](https://proceedings.mlsys.org/paper_files/paper/2025/hash/bc82dbfbfa43232be85b8d9838f49c3e-Abstract-Conference.html) | MLSys 2025 | SLO / Scheduling | 按请求和全局状态动态调节 Iteration 调度以协调 TTFT 与 TPOT。 |
| [ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments](https://proceedings.mlsys.org/paper_files/paper/2025/hash/c2a0e26dd9ee7d57e92bb1c24b39659a-Abstract-Conference.html) | MLSys 2025 | Heterogeneous cloud | 联立异构 GPU 分组、P/D 配置与轻量在线重调度，降低重启和迁移成本。 |
| [Seesaw: High-throughput LLM Inference via Model Re-sharding](https://proceedings.mlsys.org/paper_files/paper/2025/hash/cbc4ab80cd77aa0eb87da062fbcddb46-Abstract-Conference.html) | MLSys 2025 | Parallelism | 跨 Prefill/Decode 动态调整模型 Sharding，配合分层 KV 缓冲减少转换开销。 |
| [CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion](https://2025.eurosys.org/accepted-papers.html) | EuroSys 2025 | Cache reuse | 支持非连续知识块 KV 复用，降低 RAG 请求的 Prefill 重计算。 |
| [DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs](https://2025.eurosys.org/accepted-papers.html) | EuroSys 2025 | Multi-model / Storage | 使用权重 Delta 编码与服务端加载/切换设计支撑多个全量微调模型。 |
| [Fast State Restoration in LLM Serving with HCache](https://doi.org/10.1145/3689031.3696072) | EuroSys 2025 | KV restoration | 以中间激活恢复状态，配合无 Bubble 调度与分块存储平衡计算/I/O。 |
| [Stateful Large Language Model Serving with Pensieve](https://2025.eurosys.org/accepted-papers.html) | EuroSys 2025 | Multi-turn state | 面向会话延续的状态管理与复用，避免每轮请求重复加载/重算上下文。 |
| [SkyServe: Serving AI Models across Regions and Clouds with Spot Instances](https://2025.eurosys.org/accepted-papers.html) | EuroSys 2025 | Geo / Spot | 跨区域与跨云按价格、资源和服务约束调度可抢占 GPU。 |
| [Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market](https://doi.org/10.1145/3731569.3764815) | SOSP 2025 | Multi-model pooling | Token 粒度复用 GPU 承载模型长尾，低开销弹性调整并验证生产服务。 |
| [BlitzScale: Fast and Live Large Model Autoscaling with O(1) Host Caching](https://www.usenix.org/conference/osdi25/presentation/zhang-dingyan) | OSDI 2025 | Autoscaling | 借计算网络加载权重，以 Layer 粒度 Live Scaling 消除等待完整启动的停顿。 |
| [Cauchy: A Cost-Efficient LLM Serving System through Adaptive Heterogeneous Deployment](https://doi.org/10.1145/3772052.3772264) | SoCC 2025 | Heterogeneous deployment | 针对异构资源与 Workload 变化动态调整部署以降低成本。 |
| [NEO: Saving GPU Memory Crisis with CPU Offloading for Online LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/66a026c0d17040889b50f0dfa650e5e0-Abstract-Conference.html) | MLSys 2025 | Hybrid execution | 将部分 Attention 计算和 KV 状态转至 CPU，并执行异步流水与负载感知调度。 |
| [Marconi: Prefix Caching for the Era of Hybrid LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/7c180af017258d239bac6248d1eb26ac-Abstract-Conference.html) | MLSys 2025 | Hybrid-model cache | 针对 Attention+SSM 共同维护的状态建立收益感知 Cache Admission/Eviction。 |
| [LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/cc8c6b9d89f7a898a29f58869b238e46-Abstract-Conference.html) | MLSys 2025 | Long-context runtime | 统一 Prefill/Decode 的结构化稀疏 Attention，并设计分层 KV Page 选择。 |
| [HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment](https://openreview.net/pdf?id=Cs6MrbFuMq) | ICLR 2025 | P/D / Heterogeneity | 以图划分和最大流联合规划异构 GPU、P/D 并行与跨阶段 KV 通信。 |
| [POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference](https://doi.org/10.1145/3676641.3715996) | ASPLOS 2025 | Kernel–runtime co-design | 在共享 SM 中重叠计算密集 Prefill 与访存密集 Decode Attention。 |
| [DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency](https://ieeexplore.ieee.org/document/10946802) | HPCA 2025 | Power / SLO | 动态重配实例、并行方案与 GPU 频率以优化 SLO 下的集群能耗。 |
| [TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms](https://doi.org/10.1145/3676641.3716025) | ASPLOS 2025 | Power / Thermal | 将动态功耗、温度和服务请求纳入云端 LLM 集群调度。 |

## 2026 (25)

| Paper | Venue | Systems lens | Distinct contribution |
|---|---|---|---|
| [JITServe: SLO-aware LLM Serving with Imprecise Request Information](https://www.usenix.org/conference/nsdi26/presentation/zhang-wei) | NSDI 2026 | Goodput / Uncertainty | 渐进修正未知请求长度估计，以 Just-in-time 资源分配优化 Goodput。 |
| [HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds](https://www.usenix.org/conference/nsdi26/presentation/lou) | NSDI 2026 | Serverless / Startup | 模型预分布、阶段重叠、无网络热点放置和 Pipeline Consolidation。 |
| [FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees](https://www.usenix.org/conference/nsdi26/presentation/oliaro) | NSDI 2026 | Co-serving | 共享 GPU 上按 Token 协同 PEFT 与在线推理，优化激活内存和 SLO。 |
| [Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads](https://www.usenix.org/conference/nsdi26/presentation/ruan-libra) | NSDI 2026 | Micro-request scheduling | 以 Micro-request 分解动态 Prefill/Decode 工作量，在不均衡负载下调度并满足 SLO。 |
| [SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems](https://www.usenix.org/conference/nsdi26/presentation/agarwal) | NSDI 2026 | Memory disaggregation | 将 KV Memory 与 Compute 分离，针对长上下文请求设计内存与执行协同。 |
| [Agentix: An Efficient Serving Engine for LLM Agents as General Programs](https://www.usenix.org/conference/nsdi26/presentation/luo) | NSDI 2026 | Program-aware serving | 将 Agent 程序依赖纳入服务调度，降低请求和程序级 Head-of-line Blocking。 |
| [ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) | NSDI 2026 | Workload / Measurement | 基于真实云服务 Trace 刻画多类型推理负载并合成代表性请求流。 |
| [Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration (EcoServe)](https://www.usenix.org/conference/osdi26/presentation/du) | OSDI 2026 | Commodity networks | 以 Macro-instance 协作与自适应分配，缓解低带宽 GPU 集群跨实例传输。 |
| [Revisiting Pipeline Parallelism for LLM Serving](https://www.usenix.org/conference/osdi26/presentation/hwang) | OSDI 2026 | Pipeline parallelism | 针对动态 Prefill/Decode 负载重新设计 Chunk Size 与阶段负载平衡。 |
| [Simple Is Better: Multiplication May Be All You Need for LLM Request Scheduling](https://www.usenix.org/conference/osdi26/technical-sessions) | OSDI 2026 | KV-aware routing | 结合缓存重算量与实例 Batch 规模构造免调参 Routing Metric，并验证生产部署。 |
| [OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving](https://www.usenix.org/conference/osdi26/presentation/yao) | OSDI 2026 | Federated / HPC serving | 在跨 Slurm/HPC/异构计算环境提供发现、路由与故障控制平面。 |
| [Kairox: Adaptive GPU-CPU Hybrid LLM Inference via Online Neuron Balancing](https://www.usenix.org/conference/osdi26/presentation/jiang-yapeng) | OSDI 2026 | Hybrid CPU–GPU | 按在线神经元负载重分配 CPU/GPU 推理计算，缓解设备利用率失衡。 |
| [PLA-Serve: A Prefill-Length-Aware LLM Serving System](https://openreview.net/forum?id=dzjCkSEDyG) | MLSys 2026 | Length-aware serving | 按 Prompt Prefill 长度协调请求分配，处理长短输入混合下的资源干扰。 |
| [BatchLLM: Optimizing Large Batched LLM Inference with Global Prefix Sharing and Throughput-oriented Token Batching](https://proceedings.mlsys.org/paper_files/paper/2026/hash/5b7ae1758452854dee4e962207d38304-Abstract-Conference.html) | MLSys 2026 | Offline / Batch | 对离线大批量任务跨请求共享全局 Prefix，并采用吞吐导向 Token Batching。 |
| [MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing](https://openreview.net/forum?id=1JyePezdlF) | MLSys 2026 | Memory / Elasticity | 动态调整量化 Layer Residency 与 KV 容量以适应请求规模变化。 |
| [FaaScale: Unlocking Fast LLM Scaling for Serverless Inference](https://openreview.net/forum?id=jgL8LuOVyT) | MLSys 2026 | Fast scaling | 优化 Serverless 模型扩缩容关键路径，实现低延迟容量调整。 |
| [REMIX: Dynamic Partitioning for Fine-Grained Heterogeneous LLM Serving](https://mlsys.org/virtual/2026/poster/10182) | MLSys 2026 | Heterogeneous partition | 以细粒度动态 Partition 调整异构设备上的计算和内存利用。 |
| [AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving](https://dl.acm.org/doi/10.1145/3767295.3769345) | EuroSys 2026 | Cluster orchestration | 依据工作负载实时重配集群资源与请求分配，重点优化服务延迟。 |
| [TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling](https://doi.org/10.1145/3767295.3769328) | EuroSys 2026 | Streaming / Preemption | 利用客户端 Token Buffer 的富余量实施抢占调度与主动 KV Offload。 |
| [KUNSERVE: Parameter-centric Memory Management for Efficient Memory Overloading Handling in LLM Serving](https://dl.acm.org/doi/10.1145/3767295.3769348) | EuroSys 2026 | Parameter memory | 以参数为中心处理 Serving 的显存超额占用，减少模型切换及请求停顿。 |
| [MFS: An Efficient Model Family Serving System for LLMs](https://doi.org/10.1145/3767295.3769355) | EuroSys 2026 | Model family | 利用同系列模型之间的参数/执行共享特征优化多模型服务。 |
| [AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding](https://dl.acm.org/doi/10.1145/3767295.3769315) | EuroSys 2026 | Speculation / SLO | 按请求 SLO 设计 Speculative Draft/Verify 策略，将加速与服务目标联动。 |
| [Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration](https://doi.org/10.1145/3779212.3790135) | ASPLOS 2026 | GPU space/time sharing | 联合时间与空间调度降低在线推理的 GPU 空闲与资源碎片。 |
| [QoServe: Breaking the Silos of LLM Inference Serving](https://doi.org/10.1145/3779212.3790206) | ASPLOS 2026 | Multi-tenant isolation | 针对独立 Serving 部署的资源孤岛，研究跨服务资源共享与 QoS。 |
| [Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism](https://doi.org/10.1109/ISCA66397.2026.00098) | ISCA 2026 | Sequence parallelism | 在分离式集群按 Chunk 动态扩缩 Sequence Parallelism，使用碎片资源。 |

## Boundary notes

The topic deliberately omits training-only schedulers, speculative-decoding algorithms without serving evidence, purely simulated placement strategies, and minor extensions without a distinct system mechanism. Historical anchors such as Orca, vLLM/PagedAttention, Sarathi-Serve, DistServe, Llumnix and FastServe remain in the [core chronology](../README.md) rather than being duplicated here.

**Source note.** For ExeGPT, SpotServe, CacheBlend, DeltaZip, Pensieve, and SkyServe the link targets the official program/accepted-paper list; those links attest venue and title but are not individual article pages. See the associated conference or publisher for full text.
