# Distributed & Disaggregated Serving

Organizing compute, state movement and parallelism across accelerators, nodes and disaggregated resources.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Cross-node architecture, topology, communication and resource placement form the central contribution.

**Foundational context.** See also: [DistServe and Splitwise (2024), FlexGen (2023)](../README.md#foundational-and-influential-papers).
## Papers (27)

A selective, chronological bibliography; each paper's principal mechanism determines its only full-topic entry. See [curation criteria](../CURATION.md) and the [migration record](serving-systems.md) for historical changes.

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [HeteGen: Efficient Heterogeneous Parallel Inference for Large Language Models on Resource-Constrained Devices](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5431dca75a8d2abc1fb51e89e8324f10-Abstract-Conference.html) | MLSys 2024 | 针对 GPU/CPU 异构设备规划推理执行与参数转移，实现受限资源大模型部署。 |
| 2024 | [LoongServe: Efficiently Serving Long-Context Large Language Models with Elastic Sequence Parallelism](https://doi.org/10.1145/3694715.3695948) | SOSP 2024 | Elastic Sequence Parallelism 随上下文长度和负载变化动态调整跨 GPU 并行度。 |
| 2024 | [RingAttention with Blockwise Transformers for Near-Infinite Context](https://proceedings.iclr.cc/paper_files/paper/2024/hash/1119587863e78451f080da2a768c4935-Abstract-Conference.html) | ICLR 2024 | Blockwise Attention 与跨设备 Ring KV 传输流水，改善超长序列可扩展执行（兼含训练）。 |
| 2024 | [ServerlessLLM: Low-Latency Serverless Inference for Large Language Models](https://www.usenix.org/conference/osdi24/presentation/fu) | OSDI 2024 | 多层 Checkpoint Loading、位置感知调度与推理迁移协同减少冷启动。 |
| 2024 | [SpotServe: Serving Generative Large Language Models on Preemptible Instances](https://arxiv.org/abs/2311.15566) | ASPLOS 2024 | 针对 Spot 抢占实施动态重并行、低成本实例迁移和有状态恢复。 |
| 2025 | [Attention-Level Speculation](https://proceedings.mlr.press/v267/cai25g.html) | ICML 2025 | 以 Attention 输出预测提前执行后续层，在异构 NPU 上重叠 Attention 与非 Attention 计算。 |
| 2025 | [BlitzScale: Fast and Live Large Model Autoscaling with O(1) Host Caching](https://www.usenix.org/conference/osdi25/presentation/zhang-dingyan) | OSDI 2025 | 借计算网络加载权重，以 Layer 粒度 Live Scaling 消除等待完整启动的停顿。 |
| 2025 | [Cauchy: A Cost-Efficient LLM Serving System through Adaptive Heterogeneous Deployment](https://doi.org/10.1145/3772052.3772264) | SoCC 2025 | 针对异构资源与 Workload 变化动态调整部署以降低成本。 |
| 2025 | [DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency](https://ieeexplore.ieee.org/document/10946802) | HPCA 2025 | 动态重配实例、并行方案与 GPU 频率以优化 SLO 下的集群能耗。 |
| 2025 | [Enabling Efficient GPU Communication over Multiple NICs with FuseLink](https://www.usenix.org/conference/osdi25/presentation/ren) | OSDI 2025 | 利用 GPU Relay 和 NIC Pooling 缓解跨节点热点，论文含 LLM Serving TTFT 实际评估。 |
| 2025 | [HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment](https://openreview.net/pdf?id=Cs6MrbFuMq) | ICLR 2025 | 以图划分和最大流联合规划异构 GPU、P/D 并行与跨阶段 KV 通信。 |
| 2025 | [NEO: Saving GPU Memory Crisis with CPU Offloading for Online LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/66a026c0d17040889b50f0dfa650e5e0-Abstract-Conference.html) | MLSys 2025 | 将部分 Attention 计算和 KV 状态转至 CPU，并执行异步流水与负载感知调度。 |
| 2025 | [Seesaw: High-throughput LLM Inference via Model Re-sharding](https://proceedings.mlsys.org/paper_files/paper/2025/hash/cbc4ab80cd77aa0eb87da062fbcddb46-Abstract-Conference.html) | MLSys 2025 | 跨 Prefill/Decode 动态调整模型 Sharding，配合分层 KV 缓冲减少转换开销。 |
| 2025 | [Star Attention: Efficient LLM Inference over Long Sequences](https://proceedings.mlr.press/v267/acharya25a.html) | ICML 2025 | 通过分布式上下文 Block Attention 与 Anchor Token 降低多 GPU Long-context 通信。 |
| 2025 | [TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms](https://doi.org/10.1145/3676641.3716025) | ASPLOS 2025 | 将动态功耗、温度和服务请求纳入云端 LLM 集群调度。 |
| 2025 | [ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments](https://proceedings.mlsys.org/paper_files/paper/2025/hash/c2a0e26dd9ee7d57e92bb1c24b39659a-Abstract-Conference.html) | MLSys 2025 | 联立异构 GPU 分组、P/D 配置与轻量在线重调度，降低重启和迁移成本。 |
| 2025 | [WaferLLM: Large Language Model Inference at Wafer Scale](https://www.usenix.org/conference/osdi25/presentation/he) | OSDI 2025 | 用 PLMR 硬件模型驱动晶圆级 Mesh 并行、MeshGEMM/GEMV，验证非共享内存加速器上的端到端推理。 |
| 2026 | [AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving](https://dl.acm.org/doi/10.1145/3767295.3769345) | EuroSys 2026 | 依据工作负载实时重配集群资源与请求分配，重点优化服务延迟。 |
| 2026 | [Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration (EcoServe)](https://www.usenix.org/conference/osdi26/presentation/du) | OSDI 2026 | 以 Macro-instance 协作与自适应分配，缓解低带宽 GPU 集群跨实例传输。 |
| 2026 | [FaaScale: Unlocking Fast LLM Scaling for Serverless Inference](https://openreview.net/forum?id=jgL8LuOVyT) | MLSys 2026 | 优化 Serverless 模型扩缩容关键路径，实现低延迟容量调整。 |
| 2026 | [HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds](https://www.usenix.org/conference/nsdi26/presentation/lou) | NSDI 2026 | 模型预分布、阶段重叠、无网络热点放置和 Pipeline Consolidation。 |
| 2026 | [Kairox: Adaptive GPU-CPU Hybrid LLM Inference via Online Neuron Balancing](https://www.usenix.org/conference/osdi26/presentation/jiang-yapeng) | OSDI 2026 | 按在线神经元负载重分配 CPU/GPU 推理计算，缓解设备利用率失衡。 |
| 2026 | [OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving](https://www.usenix.org/conference/osdi26/presentation/yao) | OSDI 2026 | 在跨 Slurm/HPC/异构计算环境提供发现、路由与故障控制平面。 |
| 2026 | [REMIX: Dynamic Partitioning for Fine-Grained Heterogeneous LLM Serving](https://mlsys.org/virtual/2026/poster/10182) | MLSys 2026 | 以细粒度动态 Partition 调整异构设备上的计算和内存利用。 |
| 2026 | [Revisiting Pipeline Parallelism for LLM Serving](https://www.usenix.org/conference/osdi26/presentation/hwang) | OSDI 2026 | 针对动态 Prefill/Decode 负载重新设计 Chunk Size 与阶段负载平衡。 |
| 2026 | [SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems](https://www.usenix.org/conference/nsdi26/presentation/agarwal) | NSDI 2026 | 将 KV Memory 与 Compute 分离，针对长上下文请求设计内存与执行协同。 |
| 2026 | [Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism](https://doi.org/10.1109/ISCA66397.2026.00098) | ISCA 2026 | 在分离式集群按 Chunk 动态扩缩 Sequence Parallelism，使用碎片资源。 |

*Venue and mechanisms follow primary publication material; authors' experimental claims are not independently reproduced.*
