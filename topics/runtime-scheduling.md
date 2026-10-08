# Runtime & Scheduling

Scheduling tokens, requests and model instances within online inference services to satisfy latency, utilization and fairness.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Use this class when a new request-level policy, queueing rule, or batching/routing mechanism is decisive; physical cluster separation belongs in Distributed.

**Foundational context.** See also: [Orca (2022), Sarathi-Serve (2024), Llumnix (2024), NanoFlow (2025)](../README.md#foundational-and-influential-papers).

## Papers (49)

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [dLoRA: Dynamically Orchestrating Requests and Adapters for LoRA LLM Serving](https://www.usenix.org/conference/osdi24/presentation/wu-bingyang) | OSDI 2024 | Credit-based LoRA Batching 与 Adapter/Request 协同迁移，提高多租户低秩适配器 Serving 效率。 |
| 2024 | [ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference](https://arxiv.org/abs/2404.07947) | ASPLOS 2024 | 将推理资源配置与约束条件共同纳入调度，比较部署配置的延迟与吞吐。 |
| 2024 | [Fairness in Serving Large Language Models](https://www.usenix.org/conference/osdi24/presentation/sheng) | OSDI 2024 | Virtual Token Counter 把 Prefill/Decode 的 Token Cost 计入公平服务定义和连续批处理调度。 |
| 2024 | [MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving](https://proceedings.mlr.press/v235/duan24a.html) | ICML 2024 | 按模型热度联合空间/时间复用显存与计算，区分 Prefill/Decode 的资源需求。 |
| 2024 | [Parrot: Efficient Serving of LLM-based Applications with Semantic Variable](https://www.usenix.org/conference/osdi24/presentation/lin-chaofan) | OSDI 2024 | 以 Semantic Variable 暴露请求间数据依赖，支持 Agentic Workflow 级任务排程和 Prefix 复用。 |
| 2024 | [Punica: Multi-Tenant LoRA Serving](https://proceedings.mlsys.org/paper_files/paper/2024/file/054de805fcceb78a201f5e9d53c85908-Paper-Conference.pdf) | MLSys 2024 | 以 SGMV Kernel 合批不同 LoRA Adapter 的 Decode，并统一调度多租户请求。 |
| 2025 | [Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market](https://doi.org/10.1145/3731569.3764815) | SOSP 2025 | Token 粒度复用 GPU 承载模型长尾，低开销弹性调整并验证生产服务。 |
| 2025 | [Preble: Efficient Distributed Prompt Scheduling for LLM Serving](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5bc342f48de8264779952fac378f96dc-Abstract-Conference.html) | ICLR 2025 | 在分布式请求调度中联合 KV 复用收益与负载均衡，复用重复 Prompt。 |
| 2025 | [SOLA: Optimizing SLO Attainment for Large Language Model Serving with State-Aware Scheduling](https://proceedings.mlsys.org/paper_files/paper/2025/hash/bc82dbfbfa43232be85b8d9838f49c3e-Abstract-Conference.html) | MLSys 2025 | 按请求和全局状态动态调节 Iteration 调度以协调 TTFT 与 TPOT。 |
| 2025 | [XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html) | MLSys 2025 | 词表静态预检、持久 Grammar Stack 与 CPU/GPU 重叠减少结构化生成开销。 |
| 2026 | [Agentix: An Efficient Serving Engine for LLM Agents as General Programs](https://www.usenix.org/conference/nsdi26/presentation/luo) | NSDI 2026 | 将 Agent 程序依赖纳入服务调度，降低请求和程序级 Head-of-line Blocking。 |
| 2026 | [AUM: Unleashing the Efficiency Potential of Shared Processors with Accelerator Units for LLM Serving](https://2026.hpca-conf.org/details/hpca-2026-main-conference/36/AUM-Unleashing-the-Efficiency-Potential-of-Shared-Processors-with-Accelerator-Units-) | HPCA 2026 | 建模共享矩阵加速资源与频率干扰，调度服务执行。 |
| 2026 | [BatchGen: An Architecture for Scalable and Efficient Batch Inference](https://www.usenix.org/conference/osdi26/presentation/xu-tairan) | OSDI 2026 | BatchGen 以「序列协程」计算模型把每条序列表示为细粒度事件驱动协程，让运行时动态重组工作（更大专家级 batch、缓解掉队、跨设备重分配），在 128-GPU 集群上把批完成时间最多缩短 2.3×，在内存受限加速器上比最强卸载基线快至多 9.6× |
| 2026 | [BatchLLM: Optimizing Large Batched LLM Inference with Global Prefix Sharing and Throughput-oriented Token Batching](https://proceedings.mlsys.org/paper_files/paper/2026/hash/5b7ae1758452854dee4e962207d38304-Abstract-Conference.html) | MLSys 2026 | 对离线大批量任务跨请求共享全局 Prefix，并采用吞吐导向 Token Batching。 |
| 2026 | [BEAM: Joint Resource–Power Optimization for Energy-Efficient LLM Inference under SLO contraints](https://proceedings.mlsys.org/paper_files/paper/2026/hash/eb3c42ddfa16d8421fdba13528107cc1-Abstract-Conference.html) | MLSys 2026 | 在 vLLM 上联合调节 GPU 频率、Chunk Size 与 Microbatch，利用请求 SLO Slack 降低推理能耗。 |
| 2026 | [BlendServe: Optimizing Offline Inference with Resource-Aware Batching](https://doi.org/10.1145/3779212.3790133) | ASPLOS 2026 | 离线推理批次中协调 Prefill/Decode 的资源差异以提升 GPU 使用效率。 |
| 2026 | [BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Abstract-Conference.html) | MLSys 2026 | 以 MOBO 联合优化异构模型查询路由、GPU 配置和服务成本。 |
| 2026 | [Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration](https://doi.org/10.1145/3779212.3790135) | ASPLOS 2026 | 联合时间与空间调度降低在线推理的 GPU 空闲与资源碎片。 |
| 2026 | [Cascadia: An Efficient Cascade Serving System for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b76105b94a8c1286c860ad885ec588f1-Abstract-Conference.html) | ICLR 2026 | 以模型级联和跨实例路由优化 SLO 条件下的多模型 Serving。 |
| 2026 | [CONCUR: High-Throughput Agentic Batch Inference of LLM via Congestion-Based Concurrency Control](https://proceedings.mlr.press/v306/chen26fs.html) | ICML 2026 | 对 Agent KV Thrashing 引入拥塞感知并发控制。 |
| 2026 | [FlashAgents: Accelerating Multi-Agent LLM Systems via Streaming Prefill Overlap](https://proceedings.mlsys.org/paper_files/paper/2026/hash/9a6f6e0d6781d1cb8689192408946d73-Abstract-Conference.html) | MLSys 2026 | FlashAgents 用 agent 间 token streaming、增量 prefill 和 prefix-aware coordination 重叠多智能体调用链中的等待与计算 |
| 2026 | [FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees](https://www.usenix.org/conference/nsdi26/presentation/oliaro) | NSDI 2026 | 共享 GPU 上按 Token 协同 PEFT 与在线推理，优化激活内存和 SLO。 |
| 2026 | [From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill](https://proceedings.mlsys.org/paper_files/paper/2026/hash/c0f460c6d63599ea870ba9db63dc96a9-Abstract-Conference.html) | MLSys 2026 | 改用模型层分组而非 Token Chunk 执行 Prefill，减少 Expert Weight 重载。 |
| 2026 | [HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving](https://proceedings.mlsys.org/paper_files/paper/2026/hash/096b1019463f34eb241e87cfce8dfe16-Abstract-Conference.html) | MLSys 2026 | 动态预测 Early Exit 并跨模型切换以减少加载层数和延迟。 |
| 2026 | [HeraSys: Collaborative Serving of Multiple LLM Workflows via Fine-Grained End-to-End Optimization](https://icml.cc/virtual/2026/poster/66472) | ICML 2026 | HeraSys 对相互依赖的多个 LLM 工作流做细粒度端到端协同调度，在各自 serving 阶段间统一优化以提升多工作流协同 serving 的整体效率 |
| 2026 | [Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with Sereno](https://www.usenix.org/conference/osdi26/presentation/xin) | OSDI 2026 | SERENO 发现并发 LLM 推理使前台卡顿率升 153% 而自身吞吐仅降约 1%，遂复用 speculative decoding 插入细粒度让步点实现可抢占执行，在检测到带宽争用时把带宽让给前台 |
| 2026 | [JITServe: SLO-aware LLM Serving with Imprecise Request Information](https://www.usenix.org/conference/nsdi26/presentation/zhang-wei) | NSDI 2026 | 渐进修正未知请求长度估计，以 Just-in-time 资源分配优化 Goodput。 |
| 2026 | [KUNSERVE: Parameter-centric Memory Management for Efficient Memory Overloading Handling in LLM Serving](https://dl.acm.org/doi/10.1145/3767295.3769348) | EuroSys 2026 | 以参数为中心处理 Serving 的显存超额占用，减少模型切换及请求停顿。 |
| 2026 | [Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads](https://www.usenix.org/conference/nsdi26/presentation/ruan-libra) | NSDI 2026 | 以 Micro-request 分解动态 Prefill/Decode 工作量，在不均衡负载下调度并满足 SLO。 |
| 2026 | [Locality-Aware Beam Scheduling for Efficient Test-Time Compute with a Consumer-grade GPU](https://proceedings.mlsys.org/paper_files/paper/2026/hash/c74b624843218d9b6713fcf299d6d5e4-Abstract-Conference.html) | MLSys 2026 | 按照 Beam 间共享 Prefix 和 Token 局部性分组调度并预取，降低消费级 GPU 的 KV Offload。 |
| 2026 | [Meeting SLOs, Slashing Hours: Automated Enterprise LLM Optimization with OptiKIT](https://proceedings.mlsys.org/paper_files/paper/2026/hash/4904fad153f6434a7bcf04465d4be2cc-Abstract-Conference.html) | MLSys 2026 | 自动调节企业推理部署和资源配置以满足 SLO。 |
| 2026 | [MFS: An Efficient Model Family Serving System for LLMs](https://doi.org/10.1145/3767295.3769355) | EuroSys 2026 | 利用同系列模型之间的参数/执行共享特征优化多模型服务。 |
| 2026 | [MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing](https://openreview.net/forum?id=1JyePezdlF) | MLSys 2026 | 动态调整量化 Layer Residency 与 KV 容量以适应请求规模变化。 |
| 2026 | [Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms](https://www.usenix.org/conference/osdi26/presentation/chaudhry) | OSDI 2026 | 以 declarative abstraction 解耦 agent workflow 规格与执行配置，结合 profile-guided optimizer 和 adaptive runtime 联合映射模型、硬件与工作流阶段 |
| 2026 | [Optimizing Deployment Configurations for LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2026/hash/97dc07f1253ab33ee514f395a82fa7cc-Abstract-Conference.html) | MLSys 2026 | 研究服务部署方案的资源与性能配置空间，指导高性能推理服务选型。 |
| 2026 | [PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models](https://2026.hpca-conf.org/details/hpca-2026-main-conference/19/PASCAL-A-Phase-Aware-Scheduling-Algorithm-for-Serving-Reasoning-based-Large-Language) | HPCA 2026 | 分离 Reasoning/Answering 阶段的执行优先级与抢占规则。 |
| 2026 | [PLA-Serve: A Prefill-Length-Aware LLM Serving System](https://openreview.net/forum?id=dzjCkSEDyG) | MLSys 2026 | 按 Prompt Prefill 长度协调请求分配，处理长短输入混合下的资源干扰。 |
| 2026 | [PlanetServe: A Decentralized, Scalable, and Privacy-Preserving Overlay for Democratizing Large Language Model Serving](https://www.usenix.org/conference/nsdi26/presentation/fang) | NSDI 2026 | PlanetServe 构建去中心化 LLM serving 覆盖网络，结合资源感知转发、隐私机制与质量验证，原型相比基线覆盖网络把延迟降低超过 50% |
| 2026 | [QoServe: Breaking the Silos of LLM Inference Serving](https://doi.org/10.1145/3779212.3790206) | ASPLOS 2026 | 针对独立 Serving 部署的资源孤岛，研究跨服务资源共享与 QoS。 |
| 2026 | [Rethinking DVFS for Mobile LLMs: Unified Energy-Aware Scheduling with CORE](https://proceedings.mlsys.org/paper_files/paper/2026/hash/136b9a13861308c8948cd308ccd02658-Abstract-Conference.html) | MLSys 2026 | 联合优化移动端 CPU/GPU/内存 DVFS 策略，覆盖 Prefill 和 Decode 的端到端时延与能耗。 |
| 2026 | [Scaling Up Large Language Models Serving Systems for Semantic Job Search](https://proceedings.mlsys.org/paper_files/paper/2026/hash/0a4c7cdfc0a4eb1b13bb84a9b6220c37-Abstract-Conference.html) | MLSys 2026 | 基于真实生产语义搜索评估 Serving 的模型、硬件及执行优化。 |
| 2026 | [Scheduling LLM Inference with Uncertainty-Aware Output Length Predictions](https://proceedings.mlr.press/v306/zheng26ae.html) | ICML 2026 | 将输出长度分布的尾部风险纳入在线调度策略。 |
| 2026 | [Simple Is Better: Multiplication May Be All You Need for LLM Request Scheduling](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) | OSDI 2026 | 结合缓存重算量与实例 Batch 规模构造免调参 Routing Metric，并验证生产部署。 |
| 2026 | [SkyWalker: A Locality-Aware Cross-Region Load Balancer for LLM Inference](https://doi.org/10.1145/3767295.3769353) | EuroSys 2026 | 跨 Region 根据 Prefix Cache Locality 和排队状态动态迁移请求。 |
| 2026 | [SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips](https://openreview.net/forum?id=RuslSHdIHa) | MLSys 2026 | SuperInfer 面向 GH200 的 NVLink-C2C 设计请求轮转调度和全双工 KV 搬运，缓解高负载下的 HOL blocking |
| 2026 | [TeleRAG: Efficient Retrieval-Augmented Generation Inference with Lookahead Retrieval](https://proceedings.mlsys.org/paper_files/paper/2026/hash/7fd522b89ac21009b7bbe7560a9a5add-Abstract-Conference.html) | MLSys 2026 | 预测 Retrieval Data 并与 LLM Generation 重叠，配合 Cache-aware Scheduling 降低 RAG 推理关键路径。 |
| 2026 | [Threshold-Based Exclusive Batching for LLM Inference](https://proceedings.mlr.press/v306/zhang26eo.html) | ICML 2026 | THETA 按 Prefill/Decode 干扰阈值选择 Mixed/Exclusive Batch。 |
| 2026 | [TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling](https://doi.org/10.1145/3767295.3769328) | EuroSys 2026 | 利用客户端 Token Buffer 的富余量实施抢占调度与主动 KV Offload。 |
| 2026 | [Towards Resource-Efficient Serverless LLM Inference with SLINFER](https://2026.hpca-conf.org/details/hpca-2026-main-conference/8/Towards-Resource-Efficient-Serverless-LLM-Inference-with-SLINFER) | HPCA 2026 | 以 CPU/GPU 异构容量弹性支持 Serverless LLM 推理。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
