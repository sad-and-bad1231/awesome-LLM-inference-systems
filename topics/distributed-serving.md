# Distributed & Disaggregated Serving

Organizing compute, state movement and parallelism across accelerators, nodes and disaggregated resources.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Cross-node architecture, topology, communication and resource placement form the central contribution.

**Foundational context.** See also: [DistServe and Splitwise (2024), FlexGen (2023)](../README.md#foundational-and-influential-papers).

## Papers (38)

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
| 2025 | [Context Parallelism for Scalable Million-Token Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html) | MLSys 2025 | 以 Pass-KV/Pass-Q 环形 Attention 和多节点通信优化百万上下文精确计算。 |
| 2025 | [DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency](https://ieeexplore.ieee.org/document/10946802) | HPCA 2025 | 动态重配实例、并行方案与 GPU 频率以优化 SLO 下的集群能耗。 |
| 2025 | [Enabling Efficient GPU Communication over Multiple NICs with FuseLink](https://www.usenix.org/conference/osdi25/presentation/ren) | OSDI 2025 | 利用 GPU Relay 和 NIC Pooling 缓解跨节点热点，论文含 LLM Serving TTFT 实际评估。 |
| 2025 | [FlexInfer: Flexible LLM Inference with CPU Computations](https://proceedings.mlsys.org/paper_files/paper/2025/hash/698cfaf72a208aef2e78bcac55b74328-Abstract-Conference.html) | MLSys 2025 | 按硬件配置和序列形状动态选择 CPU/GPU Prefill/Decode 执行策略。 |
| 2025 | [HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment](https://openreview.net/pdf?id=Cs6MrbFuMq) | ICLR 2025 | 以图划分和最大流联合规划异构 GPU、P/D 并行与跨阶段 KV 通信。 |
| 2025 | [NEO: Saving GPU Memory Crisis with CPU Offloading for Online LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/66a026c0d17040889b50f0dfa650e5e0-Abstract-Conference.html) | MLSys 2025 | 将部分 Attention 计算和 KV 状态转至 CPU，并执行异步流水与负载感知调度。 |
| 2025 | [Seesaw: High-throughput LLM Inference via Model Re-sharding](https://proceedings.mlsys.org/paper_files/paper/2025/hash/cbc4ab80cd77aa0eb87da062fbcddb46-Abstract-Conference.html) | MLSys 2025 | 跨 Prefill/Decode 动态调整模型 Sharding，配合分层 KV 缓冲减少转换开销。 |
| 2025 | [Star Attention: Efficient LLM Inference over Long Sequences](https://proceedings.mlr.press/v267/acharya25a.html) | ICML 2025 | 通过分布式上下文 Block Attention 与 Anchor Token 降低多 GPU Long-context 通信。 |
| 2025 | [TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms](https://doi.org/10.1145/3676641.3716025) | ASPLOS 2025 | 将动态功耗、温度和服务请求纳入云端 LLM 集群调度。 |
| 2025 | [ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments](https://proceedings.mlsys.org/paper_files/paper/2025/hash/c2a0e26dd9ee7d57e92bb1c24b39659a-Abstract-Conference.html) | MLSys 2025 | 联立异构 GPU 分组、P/D 配置与轻量在线重调度，降低重启和迁移成本。 |
| 2025 | [WaferLLM: Large Language Model Inference at Wafer Scale](https://www.usenix.org/conference/osdi25/presentation/he) | OSDI 2025 | 用 PLMR 硬件模型驱动晶圆级 Mesh 并行、MeshGEMM/GEMV，验证非共享内存加速器上的端到端推理。 |
| 2026 | [AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving](https://dl.acm.org/doi/10.1145/3767295.3769345) | EuroSys 2026 | 依据工作负载实时重配集群资源与请求分配，重点优化服务延迟。 |
| 2026 | [Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration (EcoServe)](https://www.usenix.org/conference/osdi26/presentation/du) | OSDI 2026 | 以 Macro-instance 协作与自适应分配，缓解低带宽 GPU 集群跨实例传输。 |
| 2026 | [Efficient, VRAM-Constrained xLM Inference on Clients](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7cd265ae802235b8d5778a4a96ff22dd-Abstract-Conference.html) | MLSys 2026 | 面向低 VRAM 客户端以子层级 CPU–GPU Pipelined Sharding、Tensor Placement 和 Copy/Compute 重叠执行 LLM/VLM。 |
| 2026 | [FaaScale: Unlocking Fast LLM Scaling for Serverless Inference](https://openreview.net/forum?id=jgL8LuOVyT) | MLSys 2026 | 优化 Serverless 模型扩缩容关键路径，实现低延迟容量调整。 |
| 2026 | [fabric-lib: RDMA Point-to-Point Communication for LLM Systems](https://proceedings.mlsys.org/paper_files/paper/2026/hash/dea9b4b6f55ae611c54065d6fc750755-Abstract-Conference.html) | MLSys 2026 | 跨 NIC 的 WriteImm / ImmCounter 原语用于跨节点 KV Transfer 与 MoE Dispatch。 |
| 2026 | [GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving](https://openreview.net/forum?id=xKjYiUgeOK) | MLSys 2026 | GhostServe 在 host memory 中以 erasure coding 为 streaming KV cache 生成 parity shards，故障时重建丢失 KV 状态并继续推理，避免完整重算或全量状态复制 |
| 2026 | [HexGen-3: A Fully Disaggregated LLM Serving Framework with Fine-Grained Heterogeneous Resource Autoscaling](https://icml.cc/virtual/2026/poster/62564) | ICML 2026 | HexGen-3（ICML 2026）提出全分离（fully disaggregated）的 LLM serving 框架，把推理的各阶段解耦独立部署，并以分层调度器配合异构资源的自动扩缩（autoscaling），在成本与性能之间取得更优平衡 |
| 2026 | [HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds](https://www.usenix.org/conference/nsdi26/presentation/lou) | NSDI 2026 | 模型预分布、阶段重叠、无网络热点放置和 Pipeline Consolidation。 |
| 2026 | [Kairox: Adaptive GPU-CPU Hybrid LLM Inference via Online Neuron Balancing](https://www.usenix.org/conference/osdi26/presentation/jiang-yapeng) | OSDI 2026 | 按在线神经元负载重分配 CPU/GPU 推理计算，缓解设备利用率失衡。 |
| 2026 | [Not All Prefills Are Equal: PPD Disaggregation for Multi-turn LLM Serving](https://icml.cc/virtual/2026/poster/64036) | ICML 2026 | 针对多轮 serving 采用 prompt 长度感知的 prefill-decode 分离，把增量 prefill 按长度路由以减少争用、提升 SLO 达成率 |
| 2026 | [OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving](https://www.usenix.org/conference/osdi26/presentation/yao) | OSDI 2026 | 在跨 Slurm/HPC/异构计算环境提供发现、路由与故障控制平面。 |
| 2026 | [RaidServe: High-performance Resilient Serving](https://proceedings.mlsys.org/paper_files/paper/2026/hash/507b4aacefe5325908e24f042617b741-Abstract-Conference.html) | MLSys 2026 | RaidServe 面向 tensor-parallel serving 中的 GPU 故障，通过 cyclic KVCache placement 均衡显存、hybrid attention 消除 straggler、fine-grained load-aware routing 动态分配请求，并主动备份 KVCac… |
| 2026 | [REMIX: Dynamic Partitioning for Fine-Grained Heterogeneous LLM Serving](https://mlsys.org/virtual/2026/poster/10182) | MLSys 2026 | 以细粒度动态 Partition 调整异构设备上的计算和内存利用。 |
| 2026 | [Revisiting Pipeline Parallelism for LLM Serving](https://www.usenix.org/conference/osdi26/presentation/hwang) | OSDI 2026 | 针对动态 Prefill/Decode 负载重新设计 Chunk Size 与阶段负载平衡。 |
| 2026 | [SHIP: SRAM-Based Huge Inference Pipelines for Fast LLM Serving](https://proceedings.mlsys.org/paper_files/paper/2026/hash/9c20f16b05f5e5e70fa07e2a4364b80e-Abstract-Conference.html) | MLSys 2026 | SHIP 总结 Groq 基于 LPUv1 SRAM 的大规模 LLM serving：以低直径同步互联和静态编译 pipeline 扩展到数千芯片，并在受限 SRAM 中实现 PagedAttention、prefix caching、speculative decoding 及动态 chunked prefill，… |
| 2026 | [SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems](https://www.usenix.org/conference/nsdi26/presentation/agarwal) | NSDI 2026 | 将 KV Memory 与 Compute 分离，针对长上下文请求设计内存与执行协同。 |
| 2026 | [Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism](https://doi.org/10.1109/ISCA66397.2026.00098) | ISCA 2026 | 在分离式集群按 Chunk 动态扩缩 Sequence Parallelism，使用碎片资源。 |
| 2026 | [TokenWeave: Efficient Compute-Communication Overlap for Distributed LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2026/hash/73ba81c7b25134a559c8a9c39ec1a4c3-Abstract-Conference.html) | MLSys 2026 | 使用融合 AllReduce–RMSNorm 和 Multimem 降低 TP 小批次通信开销。 |
| 2026 | [TriInfer: Hybrid EPD Disaggregation for Efficient Multimodal Large Language Model Inference](https://openreview.net/forum?id=nNovi8fvGN) | MLSys 2026 | TriInfer 在多模态 serving 中把 encode、prefill、decode 作为可组合阶段，按 profile 选择 E/P/D/EP/ED 实例角色 |

*Mechanism summaries reflect the official publications; experimental results have not been independently reproduced.*
