# Paper List（按类别整理；会议栏为最新发表/审稿状态）

<!-- generated from data/papers.jsonl, data/industry.jsonl, or data/candidates.jsonl; do not edit directly -->

核验口径：结构化事实源为 `data/papers.jsonl`；本文件由脚本生成，请勿直接编辑。

## 当前覆盖概览

| 类别 | 条目数 | 主用途 |
|---|---:|---|
| Runtime、调度与服务架构 | 59 | serving runtime、SLO、batching、autoscaling、serverless、模型路由 |
| 分离式推理、通信与 KV 传输 | 74 | prefill/decode 分离、KV transfer、collective、CXL/RDMA、多实例编排 |
| 长上下文、KV 状态与外部记忆 | 96 | 长上下文 serving、KV offload、prefix/RAG cache、分层存储与召回 |
| KV Cache 压缩、量化与淘汰 | 65 | KV 量化、token/head/layer 保留、稀疏选择、压缩-质量权衡 |
| 推测解码、Test-time Scaling 与生成加速 | 29 | speculative decoding、并行解码、tree drafting、reasoning 生成加速 |
| 算子、编译与硬件加速 | 111 | attention/GEMM/MoE kernel、编译器、端侧/NPU/GPU/wafer-scale 加速 |
| MoE、Adapter、多租户与模型服务 | 29 | expert routing、adapter serving、多租户 batching、MoE 通信与缓存 |
| Agent、RAG、多模态与应用级 Serving | 45 | agent workflow、RAG pipeline、多模态 stage graph、程序级调度 |
| Workload、评测、可靠性与方法论 | 40 | trace、benchmark、fault tolerance、profiling、数值稳定性和理论分析 |
| AI 集群、向量数据库、安全与周边基础设施 | 51 | GPU 集群、向量数据库、TEE/FHE、侧信道、spot/geo routing |

## Evidence Layers

事实层与评价层分开：venue status/source type 来自来源材料；triage priority/verdict 只表示筛选意见，不等同于发表等级。

| Venue Status | Count |
|---|---:|
| formal_conference | 300 |
| poster_or_workshop | 43 |
| preprint | 172 |
| unclassified | 84 |

## Runtime、调度与服务架构

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve | OSDI 2024 | Microsoft Research; Georgia Institute of Technology | Sarathi-Serve 用 chunked prefill 和 stall-free scheduling 缓解 prefill/decode 混批中的吞吐-延迟冲突。 |
| Llumnix: Dynamic Scheduling for Large Language Model Serving | OSDI 2024 | Tsinghua University; Alibaba Cloud | Llumnix 通过请求及其 KV 状态的 live migration，在多实例间动态重调度以改善尾延迟、隔离和负载均衡。 |
| Orca: A Distributed Serving System for Transformer-Based Generative Models | OSDI 2022 | Seoul National University; FriendliAI | Orca 以 iteration-level scheduling 和 selective batching 奠定现代 continuous batching LLM serving 的基础。 |
| FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU | ICML 2023 | Stanford University; UC Berkeley; ETH Zurich | FlexGen 用线性规划在 GPU、CPU 和磁盘间放置权重、激活和 KV cache，使单张消费级 GPU 也能做高吞吐超大模型离线推理。 |
| FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference | NSDI 2026 | Peking University | FastServe 用 token 粒度抢占、skip-join MLFQ 和 KV 状态换入换出降低长请求造成的队头阻塞。 |
| ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference | ASPLOS 2024 | Seoul National University; Samsung Research | ExeGPT 根据输入输出长度分布和延迟约束搜索 batch、并行度及执行计划，以最大化约束下吞吐。 |
| MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving | arXiv 预印本, 2024 | Shanghai AI Laboratory; UC Berkeley; UC San Diego | MuxServe 结合模型流行度、空间共置和 prefill/decode 时间复用，提高多模型 serving 的显存与算力利用率。 |
| DeepSpeed-FastGen: High-throughput Text Generation for LLMs via MII and DeepSpeed-Inference | arXiv 预印本, 2024 | Microsoft | DeepSpeed-FastGen 以 Dynamic SplitFuse 将长 prompt 拆分并与 generation 动态组合，兼顾有效吞吐和 token 尾延迟。 |
| Preble: Efficient Distributed Prompt Scheduling for LLM Serving | arXiv 预印本, 2024 | University of California, San Diego | Preble 在分布式集群中联合优化共享前缀 KV 复用和计算负载均衡，并用分层调度处理 prompt locality。 |
| SOLA: Optimizing SLO Attainment for Large Language Model Serving with State-Aware Scheduling | MLSys 2025 | Tsinghua University; Infinigence-AI | SOLA 在每次迭代感知请求状态和系统状态，动态平衡 TTFT、TPOT 及请求间公平性。 |
| ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments | MLSys 2025 | University of Cambridge; Peking University; ETH Zurich | ThunderServe 在异构 GPU 和网络环境中联合优化部署与并行策略，并以轻量重调度适应故障和流量漂移。 |
| Seesaw: High-throughput LLM Inference via Model Re-sharding | MLSys 2025 | University of Toronto; Microsoft | Seesaw 在 prefill/decode 阶段间动态重分片模型，并用分层 KV buffer 和 transition-aware scheduling 控制切换成本。 |
| TurboAttention: Efficient Attention Approximation for High-Throughput LLMs | MLSys 2025 | Microsoft Research; Georgia Institute of Technology | TurboAttention 结合量化 attention 乘法和 softmax 近似，减少 KV 带宽、反量化与指数计算开销。 |
| Niyama: Breaking the Silos of LLM Inference Serving | arXiv 预印本, 2025 | Microsoft Research | Niyama 以细粒度 QoS 分类、动态 chunking 和选择性请求降级在共享集群中混部交互式与批处理负载。 |
| LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems | arXiv 预印本, 2025 | University of California, Riverside 等 | LeMix 联合调度持续训练与在线推理，通过预测干扰和动态资源分配利用空闲 GPU 而不牺牲 serving 响应性。 |
| Cascadia: A Cascade Serving System for Large Language Models | ICLR 2026 Poster | University of Cambridge; HKUST | Cascadia 联合优化大小模型 cascade 的查询路由、资源分配和并行部署，在回答质量约束下改善延迟与成本。 |
| Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning | OSDI 2026 | UCLA; UC Berkeley; Harvard; NVIDIA; ByteDance 等 | Chimera 用 GPU memory ballooning 在多个 LLM 服务间动态伸缩显存占用，降低长尾模型共置时的成本。 |
| HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds | NSDI 2026 | Peking University; Alibaba Group | HydraServe 主动分发模型、重叠 worker 冷启动阶段并规避网络争用，以 pipeline consolidation 降低 serverless LLM 启动资源。 |
| JITServe: SLO-aware LLM Serving with Imprecise Request Information | NSDI 2026 | UIUC; Google; Cisco Research | JITServe 在输出长度和调用依赖未知时逐步收紧估计，并只分配满足 SLO 所需的 just-in-time serving bandwidth。 |
| FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees | NSDI 2026 | Carnegie Mellon University; Purdue University; Anthropic; Mistral AI; AWS | FlexLLM 在 token 粒度交错在线推理和 PEFT 微调，并用静态图裁剪与 hybrid scheduler 保持 inference SLO。 |
| On Evaluating Performance of LLM Inference Serving Systems | arXiv 预印本, 2025 | Microsoft Research; Georgia Institute of Technology | 该工作归纳 baseline、实验配置和 metric 反模式，并用推测解码案例说明错误归一化会掩盖 generation stall。 |
| SLOs-Serve: Optimized Serving of Multi-SLO LLMs | arXiv 预印本, 2025 | Carnegie Mellon University; Google | SLOs-Serve 用动态规划联合选择 chunked prefill、推测解码和 replica 路由，为不同应用与阶段分配 token budget。 |
| Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving | arXiv 预印本, 2025 | HKUST | Apt-Serve 将 KV cache 与更省内存的 hidden cache 组合，并动态优化 batch composition 以扩大并发和 TTFT goodput。 |
| Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration | ASPLOS 2026 | Sun Yat-sen University | Bullet 在空间放置和时间调度两个维度动态编排 LLM 请求，以减少 GPU 碎片并提高服务利用率。 |
| QoServe: Breaking the Silos of LLM Inference Serving | ASPLOS 2026 | Microsoft Research India | QoServe 统一管理原本割裂的 LLM serving 资源池，以减少不同服务等级和工作负载之间的资源孤岛。 |
| BAT: Efficient Generative Recommender Serving with Bipartite Attention | ASPLOS 2026 | Zhejiang University; University of Hong Kong; Alibaba Group; National University of Singapore | BAT 为生成式推荐设计 bipartite attention 和相应 serving 路径，减少推荐上下文与生成阶段的冗余计算。 |
| A First Look at Bugs in LLM Inference Serving Systems | EuroSys 2026 poster | Cornell University | 该工作系统归纳 LLM serving runtime 中的正确性、并发、内存和性能故障模式，为可靠性研究建立问题分类。 |
| SkyServe: Serving AI Models across Regions and Clouds with Spot Instances | EuroSys 2025 | University of California, Berkeley 等 | SkyServe 跨区域和多云使用 spot instance 部署模型，并在价格、可用性和服务延迟间动态迁移。 |
| DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | DeltaZip 只存储和加载相对基础模型的压缩参数增量，以较低显存成本服务大量全量微调模型。 |
| Stateful Large Language Model Serving with Pensieve | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | Pensieve 将会话 KV 和请求状态作为一等资源，在多轮 LLM 服务中联合管理迁移、复用和调度。 |
| Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market | SOSP 2025 | Alibaba Group 等 | Aegaeon 通过细粒度 GPU pooling 和模型复用服务长尾模型市场，降低每个模型独占设备的成本。 |
| DyOrc: Efficient Serving of Dynamic Machine Learning Workflows | SoCC 2025 | SoCC 2025 官方目录未列单位 | DyOrc 将动态 ML workflow 的依赖、分支和资源变化纳入服务编排，而非只调度独立模型请求。 |
| Cauchy: A Cost-Efficient LLM Serving System through Adaptive Heterogeneous Deployment | SoCC 2025 | SoCC 2025 官方目录未列单位 | Cauchy 在不同 GPU 类型和云实例间动态放置模型，根据负载变化降低满足 SLO 的成本。 |
| Power-aware Deep Learning Model Serving with μ-Serve | USENIX ATC 2024 | University of Illinois Urbana-Champaign; IBM Research | μ-Serve 联合优化模型复用和 GPU frequency scaling，在维持吞吐或延迟 SLO 时降低集群功耗。 |
| Harmonizing Efficiency and Practicability: Optimizing Resource Utilization in Serverless Computing with Jiagu | USENIX ATC 2024 | Shanghai Jiao Tong University; Huawei Cloud; EPFL | Jiagu 用 pre-decision scheduling 与 dual-staged scaling 提高 serverless 部署密度并降低冷启动。 |
| Starburst: A Cost-aware Scheduler for Hybrid Cloud | USENIX ATC 2024 | UC Berkeley; UC Santa Barbara | Starburst 通过可配置等待预算在私有集群与公有云间调度作业，优化云成本和 JCT。 |
| Beyond Prediction: Tail-Aware Scheduling for LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | Beyond Prediction 用分布感知而非长度预测的调度与 cache-aware preemption 联合优化在线 LLM serving 的 TTFT 和尾延迟。 |
| Can I Buy Your KV Cache? | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把热门文档的预填充 KV 视作可交易的 provider-side 资产，用服务端复用替代重复 prefill。 |
| Models Take Notes at Prefill: KV Cache Can Be Editable and Composable | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把 KV cache 视作可编辑、可组合的“笔记本”，支持附加勘误与 RoPE 重定位拼接来复用预填充结果。 |
| RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | RouteBalance 把模型路由和实例负载均衡合并成一个在线分配问题，联合优化质量、延迟和成本。 |
| Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice | arXiv 预印本, 2026 | Renmin University of China; Stanford University; Hong Kong University of Science and Technology | 该工作提出按 KV 占用几何体积增长而非仅按时长排序的 SVF/1-bit SVF 在线调度，并将其作为 vLLM 可插拔层降低平均与尾部时延。 |
| PLA-Serve: A Prefill-Length-Aware LLM Serving System | MLSys 2026 | OpenReview 公开稿未列单位 | PLA-Serve 将 prefill 长度显式纳入请求分组和批处理决策，减少长短 prompt 混合时的首 token 延迟和 GPU 空闲。 |
| BatchLLM: Optimizing Large Batched LLM Inference with Global Prefix Sharing and Throughput-oriented Token Batching | MLSys 2026 | OpenReview 公开稿未列单位 | BatchLLM 从全局前缀共享和 token batching 两层重构离线大 batch 推理，以提升共享 prompt 场景下的吞吐。 |
| MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing | MLSys 2026 | OpenReview 公开稿未列单位 | MorphServe 在运行时联合调整层级量化换入和 KV cache 大小，使服务配置随负载和内存压力动态变化。 |
| Optimizing Deployment Configurations for LLM Inference | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作系统搜索 LLM inference 的部署配置，覆盖模型并行、batch、内存和硬件选择对延迟与成本的端到端影响。 |
| BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization | MLSys 2026 | OpenReview 公开稿未列单位 | BOute 用多目标贝叶斯优化在异构模型和 GPU 组合中选择 serving 配置，联合降低成本并满足质量和延迟目标。 |
| BEAM: Joint Resource-Power Optimization for Energy-Efficient LLM Inference under SLO constraints | MLSys 2026 | OpenReview 公开稿未列单位 | BEAM 联合选择资源分配和功耗状态，在满足 SLO 的同时降低 LLM inference 的能耗。 |
| Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs | arXiv 预印本, 2026 | 作者公开稿未列单位 | Festina 以 profiling-guided 全局放置、本地 phase-aware 调度、SM 划分和 GPU operating point 联合控制，在共享 GPU 的 serverless LLM serving 中降低集群能耗并守住 TTFT/TBT SLO。 |
| From Tokens to Layers: Redefining Stall-Free Scheduling for LLM Serving with Layered Prefill | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作把 prefill 调度单位从 token chunk 改为 layer group，在 MoE serving 中减少重复 expert 权重加载并维持 stall-free decode。 |
| AIRS: Scaling Live Inference in Resource Constrained Environments | MLSys 2026 | OpenReview 公开稿未列单位 | AIRS 面向资源受限的在线推理流水线动态分配加速器与任务优先级，提高多阶段 LLM 评估/预测服务的吞吐和延迟稳定性。 |
| Breaking the Ice: Analyzing Cold Start Latency in vLLM | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作拆解 vLLM 冷启动中的 CPU-bound 阶段并建立延迟模型，为 serverless LLM 的预热、调度和容量规划提供依据。 |
| FaaScale: Unlocking Fast LLM Scaling for Serverless Inference | MLSys 2026 | OpenReview 公开稿未列单位 | FaaScale 针对 serverless LLM 快速扩缩容优化模型加载、实例启动和请求切换路径，降低突发流量下的冷启动影响。 |
| HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving | MLSys 2026 | OpenReview 公开稿未列单位 | HELIOS 在线选择模型和 early-exit 层数，只加载满足任务目标所需的层，从而在质量约束下提高吞吐和能效。 |
| Meeting SLOs, Slashing Hours: Automated Enterprise LLM Optimization with OptiKIT | MLSys 2026 | OpenReview 公开稿未列单位 | OptiKIT 自动化企业 LLM 压缩、调优和资源编排流程，让非专家团队在异构 GPU 集群上更稳定地满足 serving SLO。 |
| SchedFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling | MLSys 2026 | MLSys 2026 官方页面未列单位 | SchedFlow 将逻辑模型定义与物理执行 schedule 解耦，用可编程 operator scheduling 在 vLLM、SGLang 和 HuggingFace Transformer 中透明接入设备内并行。 |
| Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration | OSDI 2026 | Sun Yat-Sen University | 该工作用跨实例编排减少 commodity GPU 集群中的重复数据搬运和状态开销，提高低成本 GPU 上的 serving 效率。 |
| Revisiting Pipeline Parallelism for LLM Serving | OSDI 2026 | Korea University | 该工作重新分析 pipeline parallelism 在 LLM serving 中的阶段空泡、batch 形成和延迟权衡，为在线推理选择更稳健的流水配置。 |
| Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling | OSDI 2026 | Shanghai Jiao Tong University; Alibaba Group | 该工作用更简单的乘法式请求调度指标协调排队、prefill/decode 负载和 KV 压力，避免过度复杂的在线策略。 |
| Kairox: Adaptive GPU-CPU Hybrid LLM Inference via Online Neuron Balancing | OSDI 2026 | Sun Yat-sen University; HKUST; Pengcheng Laboratory; Qilu University of Technology | Kairox 在线平衡 GPU 与 CPU 上的 neuron 执行，把部分稀疏计算迁移到 CPU 以扩大本地和混合平台的可服务模型规模。 |

## 分离式推理、通信与 KV 传输

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Splitwise: Efficient Generative LLM Inference Using Phase Splitting | ISCA 2024 | University of Washington; Microsoft | Splitwise 将 prompt computation 与 token generation 部署到不同机器池，在吞吐、成本和功耗之间做阶段化资源优化。 |
| DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving | OSDI 2024 | Peking University; StepFun; UC San Diego | DistServe 将 prefill 和 decode 放到不同 GPU 上，并按 TTFT/TPOT 约束联合优化资源与并行策略。 |
| Inference without Interference: Disaggregate LLM Inference for Mixed Downstream Workloads | arXiv 预印本, 2024 | University of Chinese Academy of Sciences; ICT, CAS; Huawei Cloud | TetriInfer 通过请求分组、prefill/decode 分离和两级调度降低混合下游任务之间的推理干扰。 |
| Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving | FAST 2025 | Moonshot AI; Tsinghua University | Mooncake 以 KVCache 为中心构建分离式 LLM serving 架构，利用 CPU/DRAM/SSD/NIC 资源扩展在线长上下文服务能力。 |
| P/D-Serve: Serving Disaggregated Large Language Model at Scale | arXiv 预印本, 2024 | Huawei Technologies Co., Ltd. | P/D-Serve 面向大规模商业部署，将 prefill/decode 组织、调度和 KVCache 传输做端到端优化，以提升分离式 LLM 服务吞吐和 SLO 表现。 |
| POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference | ASPLOS 2025 | University of Washington; Microsoft Research | POD-Attention 设计可同时处理 prefill/decode 混合批的 GPU attention kernel，提升两阶段重叠执行效率。 |
| HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment | ICLR 2025 | The Hong Kong University of Science and Technology | HexGen-2 在异构 GPU 集群上联合优化资源分配、并行策略和跨阶段 KV 传输以降低成本。 |
| FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling | arXiv 预印本, 2025 | Alibaba Cloud Computing | FlowKV 优化块级 KV cache 传输并引入负载感知调度，降低 prefill 到 decode 的传输延迟和节点不均衡。 |
| Towards High-Goodput LLM Serving with Prefill-decode Multiplexing | ASPLOS 2026 | Shanghai Jiao Tong University; National University of Singapore | MuxWise 在单 GPU 内对 prefill/decode 进行多路复用，并结合估计器和 SLO 调度提升 goodput。 |
| semi-PD: Towards Efficient LLM Serving via Phase-Wise Disaggregated Computation and Unified Storage | arXiv 预印本, 2025 | Tsinghua University; Infinigence-AI; Shanghai Jiao Tong University | semi-PD 在 SM 级别分离 prefill/decode 计算但统一显存管理，减少完全 PD 分离带来的存储浪费和迁移开销。 |
| Beyond the Buzz: A Pragmatic Take on Inference Disaggregation | MLSys 2026 | NVIDIA Corporation | 该文系统分析分离式推理在真实规模下的设计空间，指出动态速率匹配和弹性扩缩容对 Pareto 最优性能很关键。 |
| 3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving | IEEE Computer Architecture Letters 2026 | 作者公开稿未列单位 | 3DLS 用 logic-on-logic 3D chiplet 将 PD 分离中的 KV 传输切到垂直互连、把 decode 侧 TP collective 留在横向 D2D fabric，以隔离混合通信争用。 |
| HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators | arXiv 预印本, 2026 | 作者公开稿未列单位 | HMA-Serve 将 GDDR 加速器用于 prefill、HBM GPU 用于 decode，并通过 phase-wise quantization、compute-transfer overlap 和 deferred dequantization 支撑跨厂商异构 PD serving。 |
| KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding | arXiv 预印本, 2026 | 作者公开稿未列单位 | KernelFlume 将 projection/FFN weight path 与 core-attention path 分离为可弹性扩缩的 weight node 和 attention node，并用 token-range 路由表与跨层流水重叠远程 attention 通信。 |
| SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference | arXiv 预印本, 2025 | Princeton University; University of Washington | SPAD 分别设计面向 prefill 和 decode 的专用芯片，以更低硬件成本匹配两阶段不同的算力和带宽需求。 |
| Efficient Multi-round LLM Inference over Disaggregated Serving | arXiv 预印本, 2026 | Southeast University; University of Cambridge; Peking University; Ant Group; Shanghai Jiao Tong University | AMPD 面向多轮 agent/RAG 工作流，在 PD 分离式服务中自适应协调增量 prefill 和阶段部署。 |
| SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems | NSDI 2026 | Adobe Research; University of Chicago; Microsoft Research 等 | SYMPHONY 将计算和 KV cache 存储解耦为 disaggregated memory management layer，以满足多轮会话状态的低延迟访问。 |
| KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving | SIGCOMM 2026 | 作者公开稿未列单位 | KVServe 用 Bayesian profiling 建立压缩策略 Pareto 集，并由在线 controller 按 workload、网络、SLO 和质量约束选择 KV 传输压缩方案。 |
| TraCT: Disaggregated LLM Serving with CXL Shared Memory KV Cache at Rack-Scale | arXiv 预印本, 2025 | University/industry collaboration | TraCT 用 CXL shared memory 同时作为 KV transfer substrate 和 rack-wide prefix-aware KV cache，探索机架级 KV cache 共享。 |
| CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving | arXiv 预印本, 2025 | Academic/industry collaboration | CXL-SpecKV 将 KV cache offload 到远端 FPGA/CXL memory，并用 speculative prefetch 与压缩/解压引擎降低带宽压力。 |
| NanoFlow: Towards Optimal Large Language Model Serving Throughput | OSDI 2025 | University of Washington | NanoFlow 将请求拆成 operation-level nano-batches，并在单 GPU 内重叠 compute、memory 和 network 资源。 |
| BlitzScale: Fast and Live Large Model Autoscaling with O(1) Host Caching | OSDI 2025 | Shanghai Jiao Tong University; Huawei Cloud | BlitzScale 使用 compute network 加载参数并按层协作执行，实现少 host cache 的快速、在线模型扩缩容。 |
| TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity | arXiv 预印本, 2025 | University of Edinburgh 等 | TokenScale 用 token velocity 统一衡量 PD 各阶段压力，并允许 decoder 临时执行 prefill 以吸收突发流量。 |
| vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models | arXiv 预印本, 2026 | Ant Group; vLLM community 等 | vLLM-Omni 把任意到任意多模态模型分解为独立 stage graph，为 LLM、扩散模型和编码器分别批处理和分配 GPU。 |
| RTP-LLM: High-Performance Alibaba LLM Inference Engine | arXiv 预印本, 2026 | Alibaba Group | RTP-LLM 汇总阿里生产推理栈中的快速加载、PD 分离、分层 KV、推测解码、量化和多模态解耦能力。 |
| Punica: Multi-Tenant LoRA Serving | arXiv 预印本, 2023/持续使用 | University of Washington | Punica 用 heterogeneous batching CUDA kernel 和共享 base model 支撑多租户 LoRA serving。 |
| MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism | arXiv 预印本, 2025 | ByteDance Seed; Peking University 等 | MegaScale-Infer 将 attention 与 MoE FFN 解耦部署，并以 ping-pong pipeline 和 M2N 通信库提高专家利用率。 |
| InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models | arXiv 预印本, 2026 | Shanghai Jiao Tong University; National University of Singapore 等 | InfiniLoRA 将 LoRA execution 从 base-model inference 解耦，通过共享 LoRA server 和专用 kernel 扩展 MoE/大 rank adapter 服务。 |
| MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool | arXiv 预印本, 2024 | Institute of Computing Technology, CAS; Huawei 等 | MemServe 以 MemPool 统一管理跨实例分布式 KV，并联合 context caching、PD 分离和全局 locality-aware scheduling。 |
| COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts | MLSys 2025 | Alibaba Cloud; Peking University | COMET 通过依赖分析、任务重排和自适应工作量分配细粒度重叠 MoE 通信与计算，并已用于万卡级生产集群。 |
| FuseLink: Enabling Efficient GPU Communication over Multiple NICs | OSDI 2025 | HKUST; USTC; Meta; Peking University | FuseLink 允许 GPU 经机内高速链路转发到空闲 NIC，消除静态 GPU-NIC 绑定造成的热点并加速首 token 生成。 |
| HydraInfer: Hybrid Disaggregated Scheduling for Multimodal Large Language Model Serving | arXiv 预印本, 2025 | Chinese Academy of Sciences; Beihang University 等 | HydraInfer 将视觉 encode、prefill 和 decode 分到异构实例，以 stage-level batching 和并行执行提高 MLLM 吞吐。 |
| LoRAServe: Serving Heterogeneous LoRA Adapters in Distributed LLM Inference Systems | arXiv 预印本, 2025 | Microsoft Research; University of Illinois Urbana-Champaign | LoRAServe 感知 adapter rank 差异，动态重平衡放置并通过 GPUDirect RDMA 远程访问 adapter，降低多租户尾延迟。 |
| TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing | arXiv 预印本, 2026 | Peking University | TokenDance 利用多 agent round 的 All-Gather 结构集中复用共享 KV，并用 block-sparse diff 压缩 sibling cache。 |
| Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads | NSDI 2026 | National University of Singapore; USTC; UC Berkeley | Libra 在任意 token 边界把请求拆为 micro-requests，以全局/局部两级调度和 chunked KV transfer 平衡动态负载。 |
| SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading | NSDI 2026 | Tencent; Nanjing University | SwiftEP 用 buffer fusion 消除 MoE all-to-all staging copy，并以 TMA、RDMA scatter-gather 和 CUDA IPC 提高链路利用率。 |
| XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads | ASPLOS 2026 | Huawei Technologies; Tsinghua University; Shanghai AI Laboratory | XY-Serve 用 token-wise P/D/V 调度、任务分解重排和 Ascend meta-kernel 平滑动态 shape 与混合阶段负载。 |
| It Takes Two to Entangle | ASPLOS 2026 | New York University; ByteDance | 该工作研究组合式 AI 系统中不同执行组件之间的耦合，揭示单独优化某一模型阶段可能无法改善端到端性能。 |
| MSCCL++: Rethinking GPU Communication Abstractions for AI Inference | ASPLOS 2026 | Microsoft Research; Microsoft Azure | MSCCL++ 以可编程通信抽象和优化 collective 支撑 tensor/expert parallel 与分离式 AI inference。 |
| STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems | ASPLOS 2026 | Rensselaer Polytechnic Institute; University of Massachusetts Amherst; IBM Research | STARC 通过 token 选择、重映射和聚类，让 PIM 系统只访问对当前解码关键的 KV 数据。 |
| TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference | ASPLOS 2026 | Peking University; Tencent YouTu Lab | TPLA 将 latent attention 与 tensor parallel 结合，降低 PD 分离推理中的 KV 和跨卡通信压力。 |
| HybridTier: An Adaptive and Lightweight CXL-Memory Tiering System | ASPLOS 2026 | University of Toronto; UC San Diego; University of Waterloo; CentML | HybridTier 以轻量在线策略在本地 DRAM 与 CXL memory 间迁移热页，为模型权重和 KV 的容量扩展提供通用基础。 |
| Transforming Torus Fabrics for Efficient Multi-tenant ML | ASPLOS 2026 | Cornell University; Lightmatter | 该工作重构 torus fabric 的路由和隔离方式，使多个 ML tenant 在共享互连上获得更稳定的 collective 性能。 |
| AlayaDB: The Data Foundation for Efficient and Effective Long-context LLM Inference | arXiv 预印本, 2025 | AlayaDB AI; Hong Kong Polytechnic University 等 | AlayaDB 将 KV cache、稀疏 attention 与查询优化封装为向量数据库，把长上下文推理转化为数据系统查询规划问题。 |
| Fine-Tuning and Serving Gemma 4 31B on Google Cloud TPU: A Technical Comparison with GPU Baselines | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作给出从 JAX/Tunix 微调到 vLLM-TPU serving 的完整路径，并在统一配置下比较 TPU 与 H100 的成本和延迟。 |
| Comprehensive Deadlock Prevention for GPU Collective Communication | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | 该工作系统化检测和预防 GPU collective 中由并发 stream、顺序和资源依赖产生的死锁。 |
| Mycroft: Tracing Dependencies in Collective Communication Towards Reliable LLM Training | SOSP 2025 | SOSP 2025 官方目录未列单位 | Mycroft 跟踪 collective 操作之间的依赖，定位分布式大模型中的 hang、顺序错误和通信故障。 |
| Oasis: Pooling PCIe Devices Over CXL to Boost Utilization | SOSP 2025 | SOSP 2025 官方目录未列单位 | Oasis 通过 CXL 池化 GPU、SSD 和 NIC 等 PCIe 设备，为弹性 AI 集群提供可组合硬件资源。 |
| THORN-ML: Transparent Hardware Offloaded Resilient Networks for RDMA based Distributed ML Workloads | SoCC 2025 | SoCC 2025 官方目录未列单位 | THORN-ML 将故障检测和恢复逻辑下沉到网络硬件，提高 RDMA 大模型作业的透明容错能力。 |
| HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference | SIGCOMM 2025 | Clemson University; Microsoft Research; Harvard University 等 | HACK 在压缩域直接执行可同态处理的 attention 运算，减少 PD 分离时 KV 传输和反复解压开销。 |
| SkeletonHunter: Diagnosing and Localizing Network Failures in Containerized Large Model Training | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | SkeletonHunter 从容器化大模型作业中提取通信骨架，定位网络故障和异常链路。 |
| SyCCL: Exploiting Symmetry for Efficient Collective Communication Scheduling | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | SyCCL 利用拓扑和 collective 的对称性缩小调度搜索空间，自动生成高效通信计划。 |
| Vedrfolnir: RDMA Network Performance Anomalies Diagnosis in Collective Communications | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | Vedrfolnir 关联 RDMA telemetry 与 collective 行为，诊断分布式 AI 集群的尾延迟和性能异常。 |
| ByteScale: Communication-Efficient Scaling of LLM Training with a 2048K Context Length on 16384 GPUs | SIGCOMM 2025 | ByteDance | ByteScale 为超长上下文训练优化并行、通信与负载均衡，其集群网络机制可迁移到大规模 prefill。 |
| ResCCL: Resource-Efficient Scheduling for Collective Communication | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | ResCCL 联合考虑链路和 GPU/CPU 资源，降低 collective 与计算竞争造成的端到端减速。 |
| ByteDance Jakiro: Enabling RDMA and TCP over Virtual Private Cloud | SIGCOMM 2025 | ByteDance | Jakiro 在 VPC 中统一支持 RDMA 和 TCP，使云端 AI workload 获得高性能且可隔离的网络。 |
| Alibaba Stellar: A New Generation RDMA Network for Cloud AI | SIGCOMM 2025 | Alibaba Cloud | Stellar 针对云 AI 集群重构 RDMA 网络的可靠性、拥塞控制和多租户隔离。 |
| A Streaming Collectives Interface Targeting Dataflow Acceleration and HPC Workloads | SC 2025 | SC 2025 官方目录未列单位 | 该工作提供 streaming collective 接口，使通信能够与细粒度 dataflow 和 kernel pipeline 重叠。 |
| SDR-RDMA: Software-Defined Reliability Architecture for Planetary Scale RDMA Communication | SC 2025 | SC 2025 官方目录未列单位 | SDR-RDMA 将可靠性策略软件定义化，以支撑跨地域超大规模 RDMA 通信。 |
| FasterMoE: Modeling and Optimizing Training of Large-Scale Dynamic Pre-Trained Models | PPoPP 2022 | Tsinghua University 等 | FasterMoE 用 shadowing、smart scheduling 和 topology-aware communication 缓解 MoE expert 负载不均。 |
| VBASE: Unifying Online Vector Similarity Search and Relational Queries via Relaxed Monotonicity | OSDI 2023 | University of Wisconsin-Madison; Microsoft Research 等 | VBASE 通过 relaxed monotonicity 将 ANN 与关系过滤和查询优化统一，减少 RAG 检索与数据库查询的割裂。 |
| Communication-Efficient Verifiable Attention for LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | VeriAttn 用 TEE 验证、GPU 执行 attention，并按 prefill/decode 两阶段减少验证与 KV 传输开销。 |
| ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories | arXiv 预印本, 2026 | 作者公开稿未列单位 | ITME 用 CXL 混合远端内存把 TB 级共享上下文层做成字节寻址扩展，并主动分层搬运权重与 prefix cache。 |
| Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | ConServe 将调度单位从单 turn 提升到整段 conversation，用首轮输入长度和 KV 占用等可观测量替代 decode-side 预测。 |
| The Price of Anarchy in Disaggregated Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作从博弈角度分析分离式推理中的自利资源选择如何恶化全局效率，并给出调度设计的效率边界。 |
| Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing | arXiv 预印本, 2026 | 作者公开稿未列单位 | Tropical 用 SLO-aware multiplexing 在非分离与分离 serving 之间折中排队时间和干扰，提升 TTFT/TPOT 的联合达标率。 |
| TriInfer: Hybrid EPD Disaggregation for Efficient Multimodal Large Language Model Inference | MLSys 2026 | OpenReview 公开稿未列单位 | TriInfer 将 encode、prefill 和 decode 混合分离并按多模态阶段调度，减少 MLLM serving 中阶段异质性造成的资源浪费。 |
| RDMA Point-to-Point Communication for LLM Systems | MLSys 2026 | OpenReview 公开稿未列单位 | TransferEngine 为分离式推理、MoE routing 和 RL 权重更新提供可移植 RDMA 点到点通信接口，避免 serving runtime 绑定单一 NIC 栈。 |
| SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL | arXiv 预印本, 2026 | 作者公开稿未列单位 | SAC 将稀疏注意力 LLM 的冷 KV cache 下沉到 CXL 内存池，并用访问预测和批量迁移降低 GPU 显存压力。 |
| KVComm: Enabling Efficient LLM Communication through Selective KV Sharing | ICLR 2026 Poster | OpenReview 公开稿未列单位 | KVComm 让多个 LLM 通过选择性共享关键 KV pairs 进行通信，减少多智能体系统中自然语言转述带来的推理成本和信息损失。 |
| Cache-to-Cache: Direct Semantic Communication Between Large Language Models | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Cache-to-Cache 让 LLM 之间直接传递语义 cache 状态，减少多模型协作时反复自然语言编码和解码造成的通信开销。 |
| See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作用 dense latent state 在异构 agent 之间传递视觉和意图信息，减少多智能体协作中自然语言转写造成的信息损失和额外推理开销。 |
| OpenTela | OSDI 2026 | ETH Zurich; University of Cambridge; EPFL; MIT; HKUST | LLMFabric 把去中心化 HPC 集群统一成异构 LLM serving 资源池，在不同网络和 GPU 条件下协调模型部署与请求路由。 |
| UEP: Portable Expert-Parallel Communication | OSDI 2026 | UC Berkeley; UC Davis; University of Wisconsin-Madison; AMD; Inferact; Tsinghua University; AWS; Broadcom | UEP 提供可移植 expert-parallel 通信层，降低 MoE serving 中专家并行对特定 collective 和网络栈的绑定。 |

## 长上下文、KV 状态与外部记忆

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion | EuroSys 2025 | CUHK Shenzhen; University of Chicago; Stanford University; Microsoft Research | CacheBlend 复用非前缀知识片段的预计算 KV，并用知识融合机制降低 RAG prefill 延迟。 |
| ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference | ICML 2025 Spotlight | ByteDance Seed; Carnegie Mellon University | ShadowKV 在 GPU 侧保留低秩 keys、landmarks 和少量 outliers，并按需从 CPU DRAM 拉取匹配 value 以提升长上下文吞吐。 |
| Cache-Craft: Managing Chunk-Caches for Efficient Retrieval-Augmented Generation | PACMMOD / SIGMOD 2025 | Adobe Research; IIT Bombay; IIT Kanpur | Cache-Craft 管理 RAG 中可复用的 chunk KV cache，并通过少量重计算修正位置影响以减少重复 prefill。 |
| RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression | ICML 2025 | NVIDIA; Georgia Institute of Technology | RocketKV 先粗粒度永久淘汰输入 KV token，再用动态稀疏注意力进行细粒度 top-k 选择以加速长上下文解码。 |
| KV Cache Transform Coding for Compact Storage in LLM Inference | ICLR 2026 | NVIDIA; University of Warsaw | KVTC 借鉴媒体压缩，用 PCA 去相关、自适应量化和熵编码压缩可复用 KV cache。 |
| LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference | MLSys 2026 | University of Chicago; Microsoft; Google; IBM/Red Hat 等 | LMCache 将 KV cache 抽象为独立可复用层，支持跨请求、跨 engine、跨存储层的 KV offload、传输和复用。 |
| RetroInfer: A Vector Storage Engine for Scalable Long-Context LLM Inference | PVLDB 19(5), 2026 | Microsoft Research; Peking University; Moonshot AI 等 | RetroInfer 把 KV cache 看作向量存储系统，用 attention-aware index 和 GPU-CPU buffer manager 支撑百万 token 级稀疏召回。 |
| DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants | NSDI 2026 | University of Chicago; Microsoft Research; UC Berkeley 等 | DroidSpeak 在同架构微调模型之间选择性共享 KV cache，并重算少量关键层以降低多模型 agent 工作流的重复 prefill。 |
| Medha: Efficient LLM Inference on Multi-Million Context Lengths Without Approximation | arXiv 预印本, 2025 | Microsoft Research; Carnegie Mellon University; University of Washington 等 | Medha 通过 adaptive prefill chunking、sequence pipeline parallelism 和 KV-cache parallelism 支撑千万 token 级精确长上下文推理。 |
| SPIN: Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving | arXiv 预印本, 2026 | Microsoft Research; University of Virginia 等 | SPIN 用统一 page-based partition、locality-aware KV manager 和分层元数据把 sparse attention 与 CPU/GPU 分层 KV 存储协同起来。 |
| KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning | arXiv 预印本, 2026 | Microsoft Research; Peking University 等 | KEEP 面向 embodied planning，将静态/动态记忆分组、multi-hop 重算和分层加载结合，减少长程记忆 prompt 的重复 prefill。 |
| Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Tutti 构建 GPU-centric KV object store、GPU io_uring 和 slack-aware I/O 调度，使 SSD-backed KV 恢复绕开 CPU 控制瓶颈。 |
| MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding | ICML 2025 | Microsoft Research 等 | MagicDec 指出长上下文下 target verification 成本相对下降，并联合优化 draft/target KV cache 以兼顾 batch throughput 和 latency。 |
| Tarragon: Making MoE-based LLM Inference Resilient | arXiv 预印本, 2026 | University of California, Riverside 等 | Tarragon 将 attention worker 和 expert worker 设为独立故障域，用 KV 增量 checkpoint 和 shadow experts 快速恢复。 |
| vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention | ASPLOS 2025 | Microsoft Research India | vAttention 通过 CUDA virtual memory 保留连续虚拟 KV layout，同时按需分配物理页，避免重写 attention kernel。 |
| Mirage: A Multi-Level Superoptimizer for Tensor Programs | OSDI 2025 | Carnegie Mellon University; Peking University; Purdue University | Mirage 用跨 kernel、thread block 和 thread 层级的统一表示搜索代数变换、调度和新 custom kernel。 |
| Mirage Persistent Kernel: A Compiler and Runtime for Mega-Kernelizing Tensor Programs | arXiv 预印本, 2025 | Carnegie Mellon University; University of Washington 等 | MPK 将多 GPU 模型推理降为 SM-level task graph 和单个 persistent megakernel，实现跨算子软件流水。 |
| InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management | OSDI 2024 | Seoul National University 等 | InfiniGen 用少量 rehearsal 预测下一层重要 KV，仅从 host memory 预取必要状态以加速 offloaded inference。 |
| Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache | OSDI 2024 | Tsinghua University; Alibaba Cloud | Infinite-LLM 将 attention layer 解耦并使用 pooled distributed KVCache，支撑最长约两百万 token 的弹性服务。 |
| Efficient Memory Management for Large Language Model Serving with PagedAttention | SOSP 2023 | UC Berkeley | vLLM/PagedAttention 用块式虚拟内存管理 KV cache，显著减少碎片并支持 beam search、parallel sampling 和前缀共享。 |
| Prompt Cache: Modular Attention Reuse for Low-Latency Inference | MLSys 2024 | Yale University | Prompt Cache 用显式 prompt module schema 预计算并复用非连续文本模块的 attention state，降低长提示 TTFT。 |
| Hydragen: High-Throughput LLM Inference with Shared Prefixes | arXiv 预印本, 2024 | Stanford University; Georgia Institute of Technology | Hydragen 将共享前缀与独有后缀的 attention 分开计算，把共享部分转成更高效的矩阵运算并扩展到树状前缀。 |
| LoongServe: Efficiently Serving Long-Context Large Language Models with Elastic Sequence Parallelism | arXiv 预印本, 2024 | Peking University | LoongServe 用弹性 sequence parallelism 按请求和阶段实时改变并行度，降低长短请求混合下的 KV 迁移和资源浪费。 |
| SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention | MLSys 2025 | Shanghai AI Laboratory; Tsinghua University; Infinigence-AI | SampleAttention 用 CRA 指标和两阶段 query-guided 结构化筛选，为不同 head 和输入动态选择最低必要稀疏度。 |
| NEO: Saving GPU Memory Crisis with CPU Offloading for Online LLM Inference | MLSys 2025 | UC Berkeley | NEO 将部分 attention 计算和 KV 状态卸载到 CPU，并以非对称 GPU-CPU 流水和负载感知调度扩大在线 batch。 |
| FlexInfer: Flexible LLM Inference with CPU Computations | MLSys 2025 | Georgia Institute of Technology | FlexInfer 根据硬件、序列长度和 batch 为 prefill/decode 分别选择 CPU-GPU 执行策略，降低单 GPU offload 延迟。 |
| Context Parallelism for Scalable Million-Token Inference | MLSys 2025 | Meta | 该工作用 pass-KV/pass-Q 两种精确 ring attention 在 128 张 H100 上扩展百万 token prefill 和 persistent-KV decode。 |
| Marconi: Prefix Caching for the Era of Hybrid LLMs | MLSys 2025 | University of Michigan; Together AI; Amazon | Marconi 为 attention-SSM hybrid models 设计基于复用概率和计算收益的 prefix cache admission/eviction。 |
| Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking | MLSys 2025 | Qualcomm AI Research | 该工作用 predictor-free 动态输入剪枝和 cache-aware masking 减少移动端 SwiGLU 模型的 DRAM 流量。 |
| LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention | MLSys 2025 | MIT Han Lab | LServe 将 prefill 与 decode 的硬件友好结构化稀疏统一起来，以 streaming heads 和层次 KV page selection 加速长序列服务。 |
| Tokencake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications | arXiv 预印本, 2025 | Peking University | Tokencake 针对 tool-call stall 和 agent 优先级联合做 KV 空间隔离、主动 offload 与预测 upload。 |
| ORBITFLOW: SLO-Aware Long-Context LLM Serving with Fine-Grained KV Cache Reconfiguration | arXiv 预印本, 2026 | UNIST 等 | ORBITFLOW 以轻量 ILP 按请求和层动态决定 GPU/CPU KV 放置，并根据运行反馈重配置以控制尾延迟。 |
| SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips | MLSys 2026 | University of Illinois Urbana-Champaign; Microsoft | SuperInfer 面向 GH200 的 NVLink-C2C 设计请求轮转调度和全双工 KV 搬运，缓解高负载下的 HOL blocking。 |
| The CAP Principle for LLM Serving: A Survey of Long-Context Large Language Model Serving | arXiv 综述, 2024 | ICT, CAS; Huawei 等 | 该综述以 Context length、Accuracy、Performance 三目标冲突组织长上下文 serving，并强调用户感知指标定义。 |
| PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel | ASPLOS 2026 | Tianjin University; Stevens Institute of Technology | PAT 利用 prefix-aware attention 和 resource-efficient multi-tile kernel 加速共享前缀场景下的 LLM 解码。 |
| BlendServe: Optimizing Offline Inference with Resource-Aware Batching | ASPLOS 2026 | UC Berkeley; University of Washington; UC Davis; Rice University | BlendServe 用 resource-aware prefix tree 维持 prefix sharing，并将计算密集和带宽密集请求混合执行。 |
| MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading | ASPLOS 2026 | Shanghai Jiao Tong University; Chinese University of Hong Kong | MoE-APEX 根据 expert 热度和执行需求自适应选择精度与卸载方式，缓解 MoE 权重容量和传输瓶颈。 |
| SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs | ASPLOS 2026 | Shanghai Jiao Tong University; Infinigence-AI; Tsinghua University; SII | SpeContext 推测长上下文中的稀疏访问区域，以减少 reasoning 阶段需要执行的 attention 上下文。 |
| I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention | ASPLOS 2026 | Illinois Institute of Technology; ICT, CAS; University of Chinese Academy of Sciences | 该工作从 I/O 复杂度而非 FLOPs 分析长序列 attention，指导算法与硬件在数据搬运瓶颈下协同优化。 |
| REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing | ASPLOS 2026 | Shanghai Jiao Tong University | REPA 用可重构 PIM 同时加速 KV cache 的卸载传输与就地处理，减少长上下文推理的数据移动。 |
| A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs | ASPLOS 2026 | Seoul National University; POSTECH | 该工作把长上下文离线推理的数据密集部分下沉到近存储处理器，降低主机内存和 I/O 成本。 |
| SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs | FAST 2026 | Shanghai Jiao Tong University | SolidAttention 以动态稀疏注意力、SSD KV 分块和推测预取，在内存受限 PC 上支撑长上下文本地推理。 |
| CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving | FAST 2026 | Shanghai Jiao Tong University; Inspur; Peking University; Huawei Cloud | CacheSlide 针对 agent prompt 中相对位置稳定的片段设计 RPDC、位置校正和 layer-wise spill-aware KV 复用。 |
| Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation-Storage Awareness | FAST 2026 | Tsinghua University; China University of Geosciences Beijing; China Telecom | Bidaw 让计算调度感知 KV 加载延迟，并让两级存储利用模型响应预测访问与淘汰，提高多轮会话 KV 命中。 |
| Fast Cloud Storage for AI Jobs via Grouped I/O API with Transparent Read/Write Optimizations | FAST 2026 | Shanghai Jiao Tong University; Huawei Cloud | AITURBO 利用加速器互连和 grouped I/O API 自动生成存储层读写计划，覆盖 checkpoint 与 KV-cache I/O。 |
| AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving | SOSP 2025 BigMem Workshop | University of Chicago; Microsoft Research 等 | AdaptCache 为每个 KV entry 联合选择有损压缩算法、压缩率和 DRAM/SSD 放置，在质量约束下提高 DRAM 命中并降低恢复延迟。 |
| InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference | HPCA 2025 | HPCA 2025 官方目录未列单位 | InstAttention 将长上下文 attention 的部分 KV 访问和计算下沉到存储设备，以低成本容量替代全量 HBM 常驻。 |
| FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference | HPCA 2025 | HPCA 2025 官方目录未列单位 | FACIL 动态调整 DRAM 地址映射，使 SoC 与 PIM 在端侧 LLM 不同阶段间高效协作。 |
| Stratum: System-Hardware Co-Design with Tiered Monolithic 3D-Stackable DRAM for Efficient MoE Serving | MICRO 2025 | UC San Diego; Georgia Institute of Technology 等 | Stratum 将分层 monolithic-3D DRAM、近存计算和 expert 热度预测结合，提高 MoE decode 的带宽和能效。 |
| Accelerating Retrieval Augmented Language Model via PIM and PNM Integration | MICRO 2025 | MICRO 2025 官方目录未列单位 | 该工作把向量检索和生成前的数据处理分配到 PIM/PNM 路径，减少 RAG pipeline 的跨设备搬运。 |
| LongSight: Compute-Enabled Memory to Accelerate Large-Context LLMs via Sparse Attention | MICRO 2025 | MICRO 2025 官方目录未列单位 | LongSight 在 compute-enabled memory 中筛选 sparse attention token，降低长上下文 KV 向 GPU 搬运的带宽。 |
| MCBP: A Memory-Compute Efficient LLM Inference Accelerator Leveraging Bit-Slice-enabled Sparsity and Repetitiveness | MICRO 2025 | Tsinghua University 等 | MCBP 在 bit-slice 粒度利用稀疏性和重复性，同时减少 GEMM、权重访问与 KV cache 访问。 |
| VectorLiteRAG: An Adaptive Vector Index Partitioning Scheme for Low-Latency RAG Pipeline | arXiv 预印本, 2025 | 作者公开稿未列单位 | VectorLiteRAG 根据索引访问偏斜动态在 CPU 与 GPU 间放置向量分区，并联动 LLM batch 控制端到端 TTFT。 |
| RAG-Stack: Co-Optimizing RAG Quality and Performance From the Vector Database Perspective | arXiv 预印本, 2025 | 作者公开稿未列单位 | RAG-Stack 以统一 IR、成本模型和计划搜索联合优化检索配置、系统性能与生成质量。 |
| WANSpec: Leveraging Global Compute Capacity for LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | WANSpec 将 speculative draft 分发到低负载区域或本地算力，并用冗余控制广域网抖动带来的延迟风险。 |
| Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作在 MI325X 上比较 MLA、GQA、MoE 和多模态模型，说明 AITER、KV offload 与 block size 必须按架构选择。 |
| SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | SpInfer 将低层非结构稀疏性映射到 GPU kernel 和数据布局，使稀疏 LLM 的理论压缩转化为实际推理加速。 |
| Fast State Restoration in LLM Serving with HCache | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | HCache 缓存并恢复模型服务的中间状态，降低实例迁移、抢占或恢复后的重复 prefill 成本。 |
| HedraRAG: Co-Optimizing Generation and Retrieval for Heterogeneous RAG Workflows | SOSP 2025 | SOSP 2025 官方目录未列单位 | HedraRAG 联合优化检索器、生成器与异构硬件分配，避免分别优化 RAG 两阶段造成资源失衡。 |
| IC-Cache: Efficient Large Language Model Serving via In-context Caching | SOSP 2025 | SOSP 2025 官方目录未列单位 | IC-Cache 缓存并组合可复用的 in-context computation，减少 few-shot、RAG 和 agent prompt 的重复 prefill。 |
| Jenga: Effective Memory Management for Serving LLM with Heterogeneity | SOSP 2025 | SOSP 2025 官方目录未列单位 | Jenga 在不同容量、带宽和互连的设备间联合管理权重与 KV，适配异构 serving 集群。 |
| DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction | SOSP 2025 | SOSP 2025 官方目录未列单位 | DiffKV 按请求和 KV 生命周期采用差异化内存策略，并并行压紧 cache 以缓解碎片。 |
| MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving | SC 2025 | SC 2025 官方目录未列单位 | MaverIQ 用 workload fingerprint 预测资源需求，并以碎片感知的分层配置实现 intent-based serving。 |
| Billion-scale Similarity Search with GPUs | IEEE Big Data 2017 | Meta AI Research | Faiss 用 GPU k-selection、量化和倒排索引建立十亿级向量检索基础，成为大量 RAG 系统的底层库。 |
| DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node | NeurIPS 2019 | Microsoft Research India | DiskANN 用 SSD-resident graph、内存导航结构和 beam search 在单机上支持十亿级低延迟 ANN。 |
| KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing | arXiv 预印本, 2026 | 作者公开稿未列单位 | KVEraser 用学习式 steering state 只改被删除跨度的 KV 区间，在不重算整段 suffix 的前提下做局部上下文擦除。 |
| MiniPIC: Flexible Position-Independent Caching in <100LOC | arXiv 预印本, 2026 | 作者公开稿未列单位 | MiniPIC 在 vLLM 中以未旋转 K cache 和少量用户侧 primitive 实现位置无关缓存，并与 CPU offload 共存。 |
| HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching | arXiv 预印本, 2026 | 作者公开稿未列单位 | HYPIC 为 hybrid-attention LLM 引入 segment-cumulative transition cache、boundary seam recomputation 和跨实例 cache-miss prefill 并行化，使 PIC 可用于长上下文 serving。 |
| Pythia: Exploiting Workflow Predictability for Efficient Agent-Native LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Pythia 在 serving 层显式编码多 agent workflow 语义，用可预测拓扑结构改善 prefix cache、扩缩容与长上下文调度。 |
| SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing | arXiv 预印本, 2026 | 作者公开稿未列单位 | SwiftCache 在异构会话间共享 KV cache 并协调多轮对话的缓存放置与复用，降低重复 prefill 和内存占用。 |
| TurboServe: Serving Streaming Video Generation Efficiently and Economically | arXiv 预印本, 2026 | 作者公开稿未列单位 | TurboServe 为流式视频生成设计在线放置与 GPU provisioning，并结合 chunk batching、offload 与 GPU-GPU 迁移降低时延与成本。 |
| HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval | arXiv 预印本, 2026 | Seoul National University; University of California, Berkeley | HERALD 利用 block diffusion 每个 block 内 top-k KV 选择可复用的性质，只选一次并与 denoising 重叠，以 CPU-GPU 协同稀疏召回 host DRAM 中的 KV。 |
| Recency/Frequency Adaptive KV Caching for Large Language Model Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把 recency 和 frequency 信号合并为 KV cache 淘汰/保留策略，在多轮和长上下文 serving 中减少低价值 cache 占用。 |
| CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution | DAC 2026 | KAIST | CoX-MoE 用合并式 expert 执行、静态 expert 分层与选择性 attention offload 协调 CPU-GPU 协作，避免 micro-batch 导致的 MoE 推理低效。 |
| Strata | OSDI 2026 | Stanford University; Shanghai Jiao Tong University; University of Colorado Boulder; Carnegie Mellon University; NVIDIA; University of Michigan | Contextra 构建分层 context cache，在长上下文服务中按复用粒度和存储层级管理 KV 状态，减少重复 prefill 和远端加载。 |
| ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs | OSDI 2026 | Shanghai Jiao Tong University; Huawei | ECHO 面向原生稀疏注意力模型做无损 KV 预取和 offload，使长上下文解码只把将被访问的 cache 及时拉回。 |
| No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs | OSDI 2026 | University of Virginia | 该工作用 zero-copy KV offloading 移除长上下文服务中的中间缓冲和额外拷贝，降低 GPU 与主机存储间的 cache 搬运瓶颈。 |
| Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token | MLSys 2026 | OpenReview 公开稿未列单位 | Stream2LLM 将上下文流式加载与 prefill 计算重叠，把长 prompt 的数据到达时间隐藏到首 token 前的执行流水中。 |
| OPKV: A High-Throughput Plugin-Driven Framework for Recallable Sparsity in Paged KV Cache Systems | MLSys 2026 | OpenReview 公开稿未列单位 | OPKV 为 paged KV cache 提供可插拔稀疏召回框架，使不同稀疏策略能在高吞吐 serving runtime 中复用同一数据通路。 |
| FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management | MLSys 2026 | OpenReview 公开稿未列单位 | FlexiCache 利用 attention head 重要性的时间稳定性动态管理 KV cache，减少长上下文生成中不必要的保留和加载。 |
| ContextPilot: Fast Long-Context Inference via Context Reuse | MLSys 2026 | OpenReview 公开稿未列单位 | ContextPilot 识别可复用上下文片段并规划复用路径，把长上下文请求转化为更少的 prefill 和 cache 恢复操作。 |
| RAGBoost: Efficient Retrieval-Augmented Generation with Accuracy-Preserving Context Reuse | MLSys 2026 | OpenReview 公开稿未列单位 | RAGBoost 检测并复用 RAG 请求间重叠检索片段的上下文计算，通过索引、排序和去重减少重复 prefill。 |
| Using Span Queries to Optimize Cache and Attention Locality | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作用 span query 表达上下文片段访问范围，让 cache placement 和 attention 执行更好利用局部性。 |
| FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference | ICLR 2026 Poster | OpenReview 公开稿未列单位 | FreeKV 改进长上下文 KV cache 检索策略，在保持生成质量的同时减少需要常驻或加载的 cache 条目。 |
| LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences | ICLR 2026 Poster | OpenReview 公开稿未列单位 | LouisKV 面向长输入长输出请求改进 KV cache 检索，减少 decode 过程中对完整历史 cache 的无差别访问。 |
| IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs | ICLR 2026 Poster | OpenReview 公开稿未列单位 | IceCache 为长序列 LLM 推理设计更省内存的 KV 管理策略，在有限显存下扩大可服务上下文和并发。 |
| QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill | ICLR 2026 Poster | OpenReview 公开稿未列单位 | QuoKA 在 prefill 阶段按 query 选择关键 KV 子集，降低长输入处理中的 attention 计算和 cache 写入。 |
| Reconstructing KV Caches with Cross-Layer Fusion for Enhanced Transformers | ICLR 2026 Poster | OpenReview 公开稿未列单位 | 该工作用跨层融合重建 KV cache，在压缩或缺失 cache 状态下尽量恢复 Transformer 推理质量。 |
| LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding | ICLR 2026 Poster | OpenReview 公开稿未列单位 | LycheeDecode 按 attention head 选择不同稀疏解码路径，降低长上下文 decode 阶段的 KV 访问和延迟。 |
| ICaRus: Identical Cache Reuse for Efficient Multi-Model Inference | ICLR 2026 Poster | OpenReview 公开稿未列单位 | ICaRus 让同架构任务模型共享相同 prompt 的 KV cache，仅在必要层重算差异，降低多模型 agent 场景的重复状态成本。 |
| DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving | ICLR 2026 Poster | OpenReview 公开稿未列单位 | DualMap 同时考虑 prefix cache affinity 和实例负载均衡，缓解分布式 LLM serving 中复用率与尾延迟的冲突。 |
| Tactic: Adaptive Sparse Attention with Clustering and Distribution Fitting for Long-Context LLMs | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Tactic 按层、头和输入分布自适应选择 sparse attention token budget，避免固定预算在长上下文 decoding 中过度保守。 |
| Universal Model Routing for Efficient LLM Inference | ICLR 2026 Poster | OpenReview 公开稿未列单位 | 该工作把模型表示成基于代表性 prompt 的特征向量，使 router 能在测试时把请求分配给未见过的新模型以降低推理成本。 |
| Beyond Speedup - Utilizing KV Cache for Sampling and Reasoning | ICLR 2026 Poster | OpenReview 公开稿未列单位 | 该工作把 KV cache 从单纯加速结构扩展为采样和 reasoning-time reuse 的状态载体，探索更高层次的推理复用。 |
| Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Bottlenecked Transformer 用轻量 cache processor 周期性重写和整合 KV segments，把推理链中的 latent memory 作为可优化状态。 |
| Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers | arXiv 预印本, 2026 | 作者公开稿未列单位 | Keyless Attention 取消显式 key cache，用 value-space routing 和 value-only cache 降低 Transformer 推理中的 KV 存储与访问开销。 |

## KV Cache 压缩、量化与淘汰

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| RefreshKV: Updating Small KV Cache During Long-form Generation | ACL 2025 Long Papers | New York University; Cornell University | RefreshKV 在长文本生成中交替执行全量注意力和小 KV cache 注意力，动态刷新保留 token 以改善长生成质量。 |
| TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate | ICLR 2026 | Google Research; New York University; Google DeepMind | TurboQuant 通过随机旋转、近最优标量量化和 QJL 残差校正，实现面向 KV cache 的在线低比特向量量化。 |
| PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | ICLR 2026 Poster | Tsinghua University; Infinigence-AI; Columbia University; OPPO AI Center; Shanghai Jiao Tong University | PM-KVQ 采用渐进式混合精度量化和长位置分布校准，降低长 CoT 推理中 KV cache 量化的累积误差。 |
| SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference | NeurIPS 2025 | Shanghai Jiao Tong University; Fudan University; Nanjing University; Wuhan University; University of Goettingen | SmallKV 用小模型注意力补偿大模型 KV 压缩中的显著性漂移和边际信息过压缩。 |
| ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | ICLR 2026 Oral | Georgia Institute of Technology; NVIDIA Research | ThinKV 根据 CoT 中不同 thought 类型的重要性进行自适应量化和逐级淘汰，并用扩展 PagedAttention kernel 复用释放页。 |
| Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | ICML 2026 | Westlake University; McGill University; Mila; Zhejiang University; MBZUAI | RLKV 用强化学习探针识别对推理链关键的注意力头，并优先保留这些头的 KV cache 来压缩长 CoT 推理开销。 |
| Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs | ICLR 2026 | Yale University; JPMorganChase AI Research | TRIM-KV 在 token 生成时预测长期保留价值，并随时间衰减以在固定内存预算下保留最有用的 KV。 |
| EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving | arXiv 预印本, 2025 | University of Chicago; UC Berkeley; Tensormesh; MIT; UC Santa Cruz; Stanford; Microsoft | EVICPRESS 联合优化 KV cache 的有损压缩和多层存储淘汰，在质量和延迟之间做全局权衡。 |
| LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation | ICLR 2026 Poster | Samsung Research | LookaheadKV 用轻量 lookahead tokens 和 LoRA 模块预测未来注意力分布，在无需草稿生成的情况下指导 KV 淘汰。 |
| SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving | arXiv 预印本, 2026 | Apple; University of Michigan 等 | SAW-INT4 面向真实 serving 约束设计 4-bit KV quantization，强调 paged layout、规则访存和 fused attention 可落地性。 |
| Information-Aware KV Cache Compression for Long Reasoning | arXiv 预印本, 2026 | 作者公开稿未列单位 | InfoKV 将预测不确定性和层间表示演化构成的 entropy signal 与 attention 分数结合，用 Forward Influence 感知的 token 选择改进长推理 KV 压缩。 |
| ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training | ICML 2026 | 作者公开稿未列单位 | ReQAT 在量化感知训练中学习 4-bit 浮点格式与推理友好的张量变换，使 reasoning 模型在低比特 KV/激活存储下接近全精度准确率。 |
| AdaServe: SLO-Customized LLM Serving with Fine-Grained Speculative Decoding | arXiv 预印本, 2025 | Carnegie Mellon University; Peking University 等 | AdaServe 将 speculative token tree 构造和请求级 SLO 结合，动态选择验证 token 以提高 goodput。 |
| Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads | ICML 2024 | Princeton University; Together AI; University of Illinois Urbana-Champaign | Medusa 在目标模型上添加多个 decoding heads，无需独立 draft model 即可并行预测和验证多个未来 token。 |
| SwiftSpec: Ultra-Low Latency LLM Decoding by Scaling Asynchronous Speculative Decoding | arXiv 预印本, 2025 | ByteDance Seed; University of Chicago 等 | SwiftSpec 将 draft 与 target 异步解耦扩展，并加入 tree-aware KV management 和 fused kernels 追求单请求极低延迟。 |
| Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference | arXiv 预印本, 2025 | Samsung Research 等 | Mirror-SD 在异构 GPU/NPU 上并行运行互补的 draft/target 推测流水线，突破串行 drafting 的延迟上限。 |
| SpecMemo: Speculative Decoding is in Your Pocket | arXiv 预印本, 2025 | University of Illinois Urbana-Champaign | SpecMemo 建模推测解码的内存下界并优化 rejected-token 状态，使受限 GPU 和移动场景也能获得加速。 |
| Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | MLSys 2026 | OpenReview 公开稿未列单位 | SparseSpec 以稀疏注意力版本的同一模型充当 draft，并联合调度 drafting、verification 和动态 KV 管理以加速长 CoT。 |
| Speculative Speculative Decoding | arXiv 预印本, 2026 | 作者公开稿未列单位 | Saguaro 在目标模型验证当前草稿时预先推测验证结果并并行准备下一批草稿，从而进一步隐藏 drafting 串行开销。 |
| FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision | arXiv 预印本, 2024 | Colfax Research; Princeton University | FlashAttention-3 利用 Hopper TMA、warp specialization 和 FP8 block quantization 重叠数据移动、matmul 与 softmax。 |
| Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving | MLSys 2025 | Nanyang Technological University | 该工作从生产实现、逐样本质量和输出变长三个角度重新评估 KV 压缩，指出内存节省不必然转化为端到端加速。 |
| MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators | MLSys 2025 | Microsoft Research; University of Illinois Urbana-Champaign | MiLo 用自适应低秩补偿器恢复超低比特 MoE 的精度，并配套 Tensor Core 友好的 3-bit kernel。 |
| QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving | MLSys 2025 | MIT Han Lab | QServe 联合 W4A8KV4 量化、SmoothAttention、权重重排和寄存器级并行，将理论低比特节省转成云端 serving 吞吐。 |
| DecDEC: A Systems Approach to Advancing Low-bit LLM Quantization | OSDI 2025 | UC Berkeley; Stanford University | DecDEC 将低比特表示、解码数据流和硬件执行联合设计，减少超低比特权重反量化对 LLM inference 的实际开销。 |
| VeriCache: Turning Lossy KV Cache into Lossless LLM Inference | arXiv 预印本, 2026 | University of Chicago; UIUC | VeriCache 用压缩 KV 起草、完整 KV 验证，并重叠 HBM 解码与 PCIe/网络换入，保证输出与 full-KV 完全一致。 |
| Joint Encoding of KV-Cache Blocks for Scalable LLM Serving | arXiv 预印本, 2026 | IBM Research | 该工作跨请求融合相似 KV block 为共享表示，在维持标准 cache layout 的同时提高并发容量。 |
| CompactFusion: Accelerating Parallel Diffusion Model Serving with Residual Compression | arXiv 预印本, 2025 | Tsinghua University | CompactFusion 利用相邻 denoising step 激活的时间冗余，只传压缩 residual 并用误差反馈控制质量损失。 |
| ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression | ASPLOS 2026 | HKUST Guangzhou; Harbin Institute of Technology Shenzhen; HKUST | ZipServ 以硬件感知无损压缩降低模型推理的内存占用和数据搬运，同时避免有损量化带来的质量风险。 |
| DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU | ASPLOS 2026 | Shanghai Jiao Tong University; Southeast University; Eastern Institute of Technology Ningbo | DFVG 将 draft 放在 FPGA、verify 放在 GPU，以异构流水降低推测解码的草稿成本并提高验证硬件利用率。 |
| M2XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization | ASPLOS 2026 | Shanghai Jiao Tong University; Huawei | M2XFP 用少量 metadata 扩展 microscaling 格式，在维持规则低比特硬件执行的同时恢复量化精度。 |
| KV Cache Optimization Strategies for Scalable and Efficient LLM Inference | arXiv 综述, 2026 | 作者公开稿未列单位 | 该综述从淘汰、压缩、混合内存、新注意力和组合策略五条路线比较 KV 优化，并映射到七类部署场景。 |
| Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization | ISCA 2025 | KAIST | Oaken 将离线量化与在线自适应 KV 量化结合，在降低 cache 带宽和容量的同时控制运行时开销。 |
| LUT Tensor Core: Lookup Table Enables Efficient Low-Bit LLM Inference Acceleration | ISCA 2025 | Microsoft Research Asia 等 | LUT Tensor Core 用查找表数据通路处理低比特权重与激活，降低超低精度 LLM 推理的解码和乘加成本。 |
| LIA: A Single-GPU LLM Inference Acceleration with Layer Bypass and Adaptive Speculative Decoding | ISCA 2025 | ISCA 2025 官方目录未列单位 | LIA 联合 layer bypass 与自适应推测解码，在单 GPU 上减少不必要的层执行和 token generation 延迟。 |
| VQ-LLM: High-performance Code Generation for Vector Quantization Augmented LLM Inference | HPCA 2025 | HPCA 2025 官方目录未列单位 | VQ-LLM 为向量量化模型自动生成高性能 kernel，将码本查找、解码与矩阵运算融合。 |
| M-ANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type | HPCA 2025 | HPCA 2025 官方目录未列单位 | M-ANT 根据分组数据分布选择数学自适应数值类型，提高低比特量化的精度和硬件效率。 |
| LAD: Efficient Accelerator for Generative Inference of LLM with Locality Aware Decoding | HPCA 2025 | HPCA 2025 官方目录未列单位 | LAD 利用 token decoding 中的局部性组织权重、KV 和计算单元，减少生成阶段的无效数据访问。 |
| DECA: A Near-Core LLM Decompression Accelerator Grounded on a 3D Roofline Model | MICRO 2025 | University of Illinois Urbana-Champaign; Intel | DECA 用三维 roofline 模型确定压缩、内存和计算瓶颈，并在 near-core 路径加速低比特权重解压。 |
| Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference | MICRO 2025 | MICRO 2025 官方目录未列单位 | Coruscant 联合设计 GPU kernel 和 sparse tensor core，使不规则稀疏权重能够获得端到端推理收益。 |
| MX+: Pushing the Limits of Microscaling Formats for Efficient Large Language Model Serving | MICRO 2025 | Seoul National University | MX+ 为 block 中的 outlier 扩展有效尾数，在接近 MXFP4 存储成本下提高低比特 serving 精度。 |
| T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge | EuroSys 2025 | Microsoft Research Asia 等 | T-MAC 用查表替代低比特矩阵乘的乘加路径，使 CPU 和边缘设备能够高效执行量化 LLM。 |
| PrefillOnly: An Inference Engine for Prefill-only Workloads in Large Language Model Applications | SOSP 2025 | SOSP 2025 官方目录未列单位 | PrefillOnly 专门优化 embedding、reranking 和 prompt encoding 等只有 prefill、没有 decode 的 LLM 应用。 |
| Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving | SoCC 2025 | SoCC 2025 官方目录未列单位 | Oneiros 通过参数重映射提高不同 tenant 间 KV cache 的兼容和复用能力。 |
| AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving | SoCC 2025 | SoCC 2025 官方目录未列单位 | AdaSpec 根据请求 SLO、草稿成本和接受率动态选择 speculative decoding 配置。 |
| Accelerating Large-Scale Inference with Anisotropic Vector Quantization | ICML 2020 | Google Research | ScaNN 用 anisotropic vector quantization 优先保留与最大内积相关的误差方向，提高 ANN 的速度和召回率。 |
| CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents | arXiv 预印本, 2026 | 作者公开稿未列单位 | CacheWise 将 coding agent 的前缀复用与 tool-call 元数据结合做复用感知驱逐和前缀感知调度，显著降低 KV eviction 并缩短会话完成时间。 |
| PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression | arXiv 预印本, 2026 | 作者公开稿未列单位 | PolyKV 在层级粒度上联合选择 KV 压缩策略和预算分配，用异构保留方案替代统一 cache budget。 |
| AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor | arXiv 预印本, 2026 | 作者公开稿未列单位 | AnchorKV 在 KV 压缩保留分数中引入 refusal anchor 的软惩罚，使压缩后的长上下文推理兼顾内存节省与安全对齐。 |
| Dual Dimensionality for Local and Global Attention | arXiv 预印本, 2026 | 作者公开稿未列单位 | Dual Dimensionality 用近邻 token 全维、远距 token 低维的 DAR 表示降低长程 KV 容量，同时保持局部预测精度。 |
| EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts | arXiv 预印本, 2026 | 作者公开稿未列单位 | EfficientRollout 为 RL rollout 设计自推测解码和系统感知开关策略，在活跃 batch 缩小时继续利用并行验证加速。 |
| From Tokens to Energy Flexibility: Quantization-Enabled Demand Response for Data Centers with LLM Inference Workloads | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把量化配置映射为可调度功率参数，并将 routing、实例切换与精度选择纳入推理数据中心的需求响应优化。 |
| JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting | arXiv 预印本, 2026 | 作者公开稿未列单位 | JetFlow 用单次前向的并行 draft head 生成具因果一致性的候选树，突破 speculative decoding 在更大 draft budget 下的扩展瓶颈。 |
| Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design | OSDI 2026 | Tsinghua University; Xingyun | 该工作用 stream-loading prefill、SmallEP、零拷贝 prefill/decode 分离和 CPU FP8 kernel，把本地 CPU-GPU 平台上的 MoE serving 拉近云端 SLO。 |
| Accelerating Speculative Diffusions via Block Verification | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把 LLM speculative decoding 的 block verification 扩展到 diffusion 采样，在无需额外训练的前提下提升 draft acceptance 和生成速度。 |
| ConSA: Controllable Sparsity in Hybrid Attention via Learnable Allocation | arXiv 预印本, 2026 | 作者公开稿未列单位 | ConSA 通过可学习的 FA/SWA 分配和稀疏度约束，为混合注意力模型学习层级或 KV-head 级的推理友好稀疏布局。 |
| Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作用 GEMM 维度统一重组 LLM pruning 设计空间，比较不同剪枝族在真实内核与硬件上的实际推理加速边界。 |
| Service-Induced Congestion in Memory-Constrained LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把持续增长的 KV memory pressure 建模为服务自身诱发的拥塞过程，并分析 eviction-free 平衡与极限环失稳。 |
| UltraQuant: 4-bit KV Caching for Context-Heavy Agents | arXiv 预印本, 2026 | Advanced Micro Devices; University of California, Los Angeles; Purdue University | UltraQuant 以 TurboQuant 风格 4-bit KV 表示为质量锚点，并结合 AMD GPU 的 FP4/FP8 decode kernel 路径压缩多轮 agent workload 的 KV cache。 |
| DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | ICLR 2026 Poster | OpenReview 公开稿未列单位 | DefensiveKV 分析基于注意力稳定性的 KV 淘汰脆弱性，并引入更稳健的保留策略降低长上下文质量崩溃风险。 |
| ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing | ICLR 2026 Poster | OpenReview 公开稿未列单位 | ReST-KV 通过逐层输出重构和时空平滑修正 token 删除后的注意力重分布，使 KV eviction 更适合长序列生成。 |
| SkipKV: Selective Skipping of KV Generation and Storage for Efficient Inference with Large Reasoning Models | MLSys 2026 | OpenReview 公开稿未列单位 | SkipKV 在大推理模型中跳过部分不关键 KV 的生成与存储，减少长 CoT 输出带来的线性 cache 增长。 |
| Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost | MLSys 2026 | OpenReview 公开稿未列单位 | Kitty 用动态 channel-wise precision boost 和 page-centric layout 实现接近 2-bit 的 KV cache 压缩，同时保持规则访存和解量化效率。 |
| ProtoKV: Long-context Knowledges Are Already Well-Organized Before Your Query | ICLR 2026 Poster | OpenReview 公开稿未列单位 | ProtoKV 将语义锚点 token 和位置决定 token 分开聚类压缩，在保留语义完整性的同时降低长上下文 KV cache 占用。 |
| Channel-Aware Mixed-Precision Quantization for Efficient Long-Context Inference | ICLR 2026 Poster | OpenReview 公开稿未列单位 | ChanMix 按 KV channel 敏感度重新分配低比特预算，并用 Triton kernel 支持 2-bit/FP8 混合精度长上下文推理。 |
| Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets | arXiv 预印本, 2026 | 作者公开稿未列单位 | Nexus Sampling 面向固定预算下的流式 KV eviction，用采样式保留机制维持长上下文质量并控制 cache 增长。 |

## 推测解码、Test-time Scaling 与生成加速

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| SpecInfer: Accelerating Generative Large Language Model Serving with Tree-based Speculative Inference and Verification | ASPLOS 2024 | Carnegie Mellon University; Peking University; Meta 等 | SpecInfer 用多个小模型构造候选 token tree，并由目标模型一次并行验证多条生成路径。 |
| EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty | ICML 2024 | Microsoft Research Asia; Peking University 等 | EAGLE 在倒数第二层 feature space 中自回归预测草稿，降低 token-level drafting 的不确定性和开销。 |
| EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees | EMNLP 2024 | Microsoft Research Asia; Peking University 等 | EAGLE-2 根据 draft confidence 动态构建候选树，避免静态树在不同上下文中的效率损失。 |
| Prism: Symbolic Superoptimization of Tensor Programs | arXiv 预印本, 2026 | Carnegie Mellon University 等 | Prism 用 symbolic hierarchical graph 和 e-graph verification 对 LLM tensor program 做可剪枝的符号超优化。 |
| EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse | ASPLOS 2026 | Shanghai Jiao Tong University; National University of Defense Technology | EARTH 根据 gating entropy 推测预取 expert 并复用结果，以降低 MoE expert 加载等待与误预取代价。 |
| FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning | ASPLOS 2026 | Imperial College London; Microsoft Research | FastTTS 面向边缘设备优化 test-time scaling，使多次候选生成与验证能够在受限资源上高效执行。 |
| ORCHES: Orchestrated Test-Time-Compute-based LLM Reasoning on Collaborative GPU-PIM Heterogeneous System | MICRO 2025 | MICRO 2025 官方目录未列单位 | ORCHES 在 GPU 与 PIM 间编排 test-time reasoning 的候选生成和验证，扩大推理计算预算而控制延迟。 |
| PRISM: Parametrically Restructured Inference for Speculative Sampling Draft Models | MLSys 2026 | OpenReview 公开稿未列单位 | PRISM 对 speculative sampling 的 draft model 做参数化重构，在保持验证正确性的前提下降低草稿生成成本。 |
| Speculative Decoding: Performance or Illusion? | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作用真实 serving 条件重新评估 speculative decoding，区分离线 speedup 与在线负载下的端到端收益。 |
| SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding | MLSys 2026 | MLSys 2026 官方页面未列单位 | SpecDiff-2 用离散扩散模型作为非自回归 drafter，并校准 diffusion drafter 与自回归 verifier 的分布差异，以提升 speculative decoding 接受率和并行度。 |
| TiDAR: Think in Diffusion, Talk in Autoregression | MLSys 2026 | 作者公开稿未列单位 | TiDAR 在单次 forward 中用 diffusion draft 和 autoregressive sampling 结合生成，保留精确 KV cache 支持并提高 serving 吞吐。 |
| Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Fast-dLLM 为 diffusion LLM 引入 KV cache 和并行解码路径，在无需训练的情况下缩小其与自回归模型的推理速度差距。 |
| Locality-Aware Beam Scheduling for Efficient Test-Time Compute with a Consumer-grade GPU | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作在消费级 GPU 上按 beam 的上下文局部性调度 test-time compute，减少多候选推理中的 cache 和显存搬运成本。 |
| Beat the long tail: Distribution-Aware Speculative Decoding for RL Training | MLSys 2026 | OpenReview 公开稿未列单位 | DAS 利用历史 rollout 维护非参数 drafter，并按轨迹长度分配 speculative budget，缩短 RL post-training 中长尾生成阶段。 |
| NexSpec: Towards Optimizing Speculative Decoding in Reinforcement Learning Systems | MLSys 2026 | OpenReview 公开稿未列单位 | NexSpec 针对 RL 系统中的 speculative decoding 动态调参、更新 drafter 并按 rollout reward 加权，缓解大 batch 和 actor 漂移下的加速失效。 |
| PARD: Accelerating LLM Inference with Low-Cost PARallel Draft Model Adaptation | ICLR 2026 Poster | OpenReview 公开稿未列单位 | PARD 将单个 draft model 低成本适配到同族目标模型，并在 draft 阶段一次预测多个未来 token 以提升 vLLM 推理吞吐。 |
| FlashDLM: Accelerating Diffusion Language Model Inference via Efficient KV Caching and Guided Diffusion | ICLR 2026 Poster | OpenReview 公开稿未列单位 | FlashDLM 结合 FreeCache 复用 denoising step 间稳定 KV projection，并用轻量 AR 模型引导扩散解码以降低 DLM 端到端时延。 |
| ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping | ICLR 2026 Poster | OpenReview 公开稿未列单位 | ES-dLLM 基于跨迭代 tensor 变化和置信度在早期层跳过低价值 token 计算，加速 diffusion LLM 推理。 |
| Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Dynamic-dLLM 用动态 cache 更新预算和自适应并行解码阈值，在无需训练的情况下提升 diffusion LLM 长序列推理效率。 |
| Attention Is All You Need for KV Cache in Diffusion LLMs | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Elastic-Cache 基于 attention-aware drift test 和 layer-aware schedule 选择何时、何处刷新 DLM KV cache，减少 denoising step 间重复计算。 |
| Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes | ICLR 2026 Poster | OpenReview 公开稿未列单位 | LSP scheduler 只提交最长稳定前缀，把 DLM 的 scattered acceptance 转成连续 KV append 和逐步收缩的 active suffix。 |
| AdaBlock-dLLM: Semantic-Aware Diffusion LLM Inference via Adaptive Block Size | ICLR 2026 Poster | OpenReview 公开稿未列单位 | AdaBlock-dLLM 根据 denoising 过程中的语义置信度动态调整 semi-AR block size，在相同吞吐预算下改善 DLM 解码质量。 |
| Learning to Parallel: Accelerating Diffusion Large Language Models via Learnable Parallel Decoding | ICLR 2026 Poster | OpenReview 公开稿未列单位 | 该工作学习 diffusion LLM 的并行解码策略，减少固定并行度或手工 scheduler 在不同上下文中的无效迭代。 |
| Self-Speculative Decoding Accelerates Lossless Inference in Any-Order and Any-Subset Autoregressive Models | ICLR 2026 Poster | OpenReview 公开稿未列单位 | ASSD 让 any-subset autoregressive model 并行生成并自校正 token 分布，在保持无损采样的同时减少生成调用。 |
| Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning | ICLR 2026 Poster | OpenReview 公开稿未列单位 | LTD 将 draft/verify 时间分配建模为 RL 环境，联合学习两个策略以直接优化每轮 speculative decoding 的吞吐。 |
| Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Loosely Speculative Decoding 放宽 exact-match 验证，只接受语义等价草稿，提升推测解码在开放生成中的可用接受率。 |
| Not-a-Bandit: Provably No-Regret Drafter Selection in Speculative Decoding for LLMs | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Not-a-Bandit 把 drafter 选择建模为带理论保证的在线决策问题，在不同请求和模型下自适应选择推测解码草稿器。 |
| CDLM: CONSISTENCY DIFFUSION LANGUAGE MODELS FOR FASTER SAMPLING | MLSys 2026 | MLSys 2026 官方页面未列单位 | CDLM 将 consistency/diffusion language model 的采样过程系统化加速，减少扩散式文本生成需要的迭代步数。 |
| CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration | arXiv 预印本, 2026 | 作者公开稿未列单位 | CATS 在显存受限场景下自适应选择 tree speculation 结构和草稿深度，减少推测解码额外 KV 与验证开销。 |

## 算子、编译与硬件加速

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| ServerlessLLM: Low-Latency Serverless Inference for Large Language Models | OSDI 2024 | University of Edinburgh 等 | ServerlessLLM 利用近 GPU 多层存储、快速 checkpoint loading 和 live migration 降低 serverless LLM 冷启动延迟。 |
| S-LoRA: Serving Thousands of Concurrent LoRA Adapters | MLSys 2024 | UC Berkeley; Stanford University | S-LoRA 用 unified paging、异构 LoRA kernel 和 tensor parallelism 在单集群中服务数千 adapter。 |
| FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving | MLSys 2025 | University of Washington; NVIDIA | FlashInfer 用 block-sparse/composable KV format、JIT attention template 和 load-balanced scheduling 提供 serving-oriented kernel。 |
| TileLang: A Composable Tiled Programming Model for AI Systems | arXiv 预印本, 2025 | Microsoft Research Asia; Alibaba 等 | TileLang 将 kernel dataflow 与线程绑定、layout、tensorize 和 pipeline 调度分离，提高 AI kernel 编程的表达力和性能。 |
| NeuronMM: High-Performance Matrix Multiplication for LLM Inference on AWS Trainium | arXiv 预印本, 2025 | University of California, Merced 等 | NeuronMM 针对 Trainium 的 systolic array、SRAM 和数据布局设计 fused/cached matmul，加速端到端 LLM inference。 |
| PowerInfer-2: Fast Large Language Model Inference on a Smartphone | arXiv 预印本, 2024 | Shanghai Jiao Tong University | PowerInfer-2 以 neuron cluster 为单位在 NPU/CPU/存储间调度和流水，实现超内存 LLM 的手机端推理。 |
| AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving | OSDI 2023 | UC Berkeley; Peking University | AlpaServe 将模型并行用于多模型 statistical multiplexing，在 burst workload 下联合优化模型放置和并行配置。 |
| LeanAttention: Hardware-Aware Scalable Attention Mechanism for the Decode-Phase of Transformers | MLSys 2025 | Microsoft Research | LeanAttention 重构 decode attention 的执行流，在保持精确 attention 的同时提高超长上下文可扩展性。 |
| FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference | MLSys 2025 | UC San Diego; Amazon | FastTree 为 radix-tree KV 共享设计专用 attention kernel，并在 runtime 中自适应划分共享上下文查询组。 |
| MAS-Attention: Memory-Aware Stream Processing for Attention Acceleration on Resource-Constrained Edge Devices | MLSys 2025 | University of Toronto | MAS-Attention 在边缘 NPU 上将向量和矩阵计算组织为双流多级 tiling，并主动覆盖 cache 以减少 spill。 |
| KPerfIR: Towards an Open and Compiler-centric Ecosystem for GPU Kernel Performance Tooling on Modern AI Workloads | OSDI 2025 | UC San Diego; Meta; OpenAI | KPerfIR 将可编程 profiling pass 集成进 Triton compiler，在较低开销下分析 GPU kernel 内细粒度单元重叠与瓶颈。 |
| QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach | OSDI 2025 | ICT, CAS; Cambricon; USTC | QiMeng-Xpiler 结合 LLM 代码生成、符号修复和分层 autotuning，在 CUDA、HIP、VNNI 和 BANG 间转译 tensor program。 |
| WaferLLM: Large Language Model Inference at Wafer Scale | OSDI 2025 | University of Edinburgh; Microsoft Research | WaferLLM 用 PLMR 模型、wafer-scale parallelism、MeshGEMM 和 MeshGEMV 将 LLM inference 映射到数十万片上 core。 |
| PipeThreader: Software-Defined Pipelining for Efficient DNN Execution | OSDI 2025 | Georgia Institute of Technology; Intel | PipeThreader 在 operator 和 kernel 内分片，按硬件资源流水执行 DNN stage，从系统层提高异构执行重叠。 |
| CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration | arXiv 预印本, 2026 | University of Michigan | CacheFlow 将 KV 恢复重构为 token、layer、GPU 三维并行，并以 batch-aware scheduler 联合分配重算和 I/O。 |
| NPUMoE: Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs | arXiv 预印本, 2026 | University of Virginia | NPUMoE 将静态密集 expert 计算卸载到 Apple NPU，并为动态 routing 保留 CPU/GPU fallback。 |
| BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal | arXiv 预印本, 2026 | 作者公开稿未列单位 | BaseRT 以原生 Metal kernel fusion、unified-memory-aware 优化和自定义 dispatch 逻辑，在 Apple Silicon 上提升 prefill/decode 吞吐并扩大 MoE 模型的本地推理能力。 |
| When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference | arXiv 预印本, 2026 | 多机构联合团队 | 该工作分离量化、通信和计算开销，揭示移动端 NPU 在 prefill/decode 中可能因调度和 fallback 而不如 CPU。 |
| Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with Sereno | OSDI 2026 | Shanghai Jiao Tong University | Sereno 针对移动端 LLM 推理中的内存带宽竞争设计缓解机制，降低本地部署在共享移动平台上的推理干扰。 |
| Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access for LLM via Semantic-Aware Knowledge Caching | NSDI 2026 | National University of Singapore; USTC; University of Toronto; Sea AI Lab | Cortex 以语义元素和两阶段判定实现跨区域 agent knowledge cache，并把延迟、成本和静态性纳入淘汰与预取。 |
| SCORPIO: Serving the Right Requests at the Right Time for Heterogeneous SLOs in LLM Inference | arXiv 预印本, 2025 | 作者公开稿未列单位 | SCORPIO 以 TTFT/TPOT 双 guard、deadline 重排、准入控制和 credit batching 提升异质 SLO goodput。 |
| Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads | ASPLOS 2026 | Snowflake AI Research | Shift Parallelism 在 TP 与 sequence parallelism 间动态切换，以适应实时流量中的延迟和吞吐变化。 |
| Insum: Sparse GPU Kernels Simplified and Optimized with Indirect Einsums | ASPLOS 2026 | MIT; Georgia Institute of Technology; NVIDIA | Insum 用 indirect einsum 抽象表达并优化稀疏 GPU kernel，降低实现不规则推理算子的复杂度。 |
| Mugi: Value Level Parallelism For Efficient LLMs | ASPLOS 2026 | University of Central Florida; Carnegie Mellon University | Mugi 在数值层面开发新的并行粒度，以提高 LLM 中细粒度运算的硬件利用率。 |
| oFFN: Outlier and Neuron-aware Structured FFN for Fast yet Accurate LLM Inference | ASPLOS 2026 | Sogang University; Santa Clara University | oFFN 感知 outlier 与 neuron 重要性构造结构化 FFN，在保持精度的同时提高规则硬件上的推理效率。 |
| Triton-Sanitizer: A Fast and Device-Agnostic Memory Sanitizer for Triton with Rich Diagnostic Context | ASPLOS 2026 | George Mason University; Google; Meta; Anthropic | Triton-Sanitizer 为 Triton kernel 提供跨设备内存错误检测和丰富诊断上下文，补齐生成式 AI kernel 的调试基础设施。 |
| Linear Layouts: Robust Code Generation of Efficient Tensor Computation Using F2 | ASPLOS 2026 | OpenAI; George Mason University | Linear Layouts 用有限域上的统一布局表示描述 tensor 数据映射，为高性能 GPU kernel 生成提供可组合基础。 |
| Ouroboros: Wafer-Scale SRAM CIM with Token-Grained Pipelining for Large Language Model Inference | ASPLOS 2026 | ICT, CAS; University of Chinese Academy of Sciences | Ouroboros 以 wafer-scale SRAM compute-in-memory 和 token-grained pipeline 加速大模型推理。 |
| Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation | ASPLOS 2026 | University of Toronto; CentML; Carnegie Mellon University; University of Waterloo; Anyscale; Amazon | Tilus 用 tile-level 语言表达低精度 GPGPU 运算，为量化推理 kernel 提供可组合代码生成。 |
| Neuralink: Fast on-Device LLM Inference with Neuron Co-Activation Linking | ASPLOS 2026 | Tsinghua University; Tianjin University; Microsoft Research | Neuralink 利用 neuron co-activation 关系减少端侧 LLM 推理中的无效权重访问与计算。 |
| PF-LLM: Large Language Model Hinted Hardware Prefetching | ASPLOS 2026 | Hong Kong University of Science and Technology; Duke University | PF-LLM 让 LLM 辅助识别访存模式并向硬件预取器提供提示，提高复杂数据访问下的 cache 命中。 |
| Asynchrony and GPUs: Bridging this Dichotomy for I/O with AGIO | ASPLOS 2026 | Pennsylvania State University; NVIDIA | AGIO 为 GPU 构建真正异步的 I/O 路径，使模型数据和状态传输可以与 kernel 执行重叠。 |
| RedFuser: An Automatic Operator Fusion Framework for Cascaded Reductions on AI Accelerators | ASPLOS 2026 | Alibaba Cloud | RedFuser 自动融合级联 reduction 算子，减少 AI accelerator 上的中间张量写回和 kernel launch。 |
| Performance Predictability in Heterogeneous Memory | ASPLOS 2026 | Virginia Tech; Microsoft; NVIDIA | 该工作研究异构内存中的性能可预测性，为模型权重、KV 和中间状态的分层放置提供基础模型。 |
| Accelerating Model Loading in LLM Inference by Programmable Page Cache | FAST 2026 | Huawei Technologies | PPC 提供非侵入可编程 page-cache 策略，MAIO 再以 I/O template、XPU affinity 和局部性优化模型加载。 |
| GPU Checkpoint/Restore Made Fast and Lightweight | FAST 2026 | Tsinghua University | GCR 通过控制/数据分离、CPU shadow execution 和 dirty template 降低 GPU checkpoint、restore 与增量快照开销。 |
| Taming LLM Inference: Lessons Learned from Optimizing Large Language Model Inference Across Diverse Hardware | arXiv 预印本, 2026 | Databricks | 该工作总结跨 GPU 和专用加速器优化 LLM inference 的工程经验，强调端到端 profile、内核适配和工作负载匹配。 |
| WSC-LLM: Efficient LLM Service and Architecture Co-exploration for Wafer-scale Chips | ISCA 2025 | Tsinghua University; Shanghai AI Laboratory; Shanghai Jiao Tong University | WSC-LLM 联合搜索 wafer-scale 芯片架构和 serving 配置，使模型并行、片上互连与请求负载共同决定部署方案。 |
| H2-LLM: Hardware-Dataflow Co-Exploration for Efficient Heterogeneous Hybrid Bonding-based LLM Inference | ISCA 2025 | ISCA 2025 官方目录未列单位 | H2-LLM 围绕异构 hybrid-bonding 芯粒联合探索硬件组织和数据流，以减少 LLM 推理中的跨层数据移动。 |
| AiF: Accelerating On-Device LLM Inference Using In-Flash Processing | ISCA 2025 | Seoul National University; Soongsil University; Kyungpook National University | AiF 将部分权重处理下沉到 flash 内部，缓解端侧设备加载大模型时的存储带宽和内存容量瓶颈。 |
| BitMoD: Bit-serial Mixture-of-Datatype LLM Acceleration | HPCA 2025 | HPCA 2025 官方目录未列单位 | BitMoD 用 bit-serial 数据通路支持多种低比特数据类型，使不同层和张量能按精度需求选择执行格式。 |
| Anda: Unlocking Efficient LLM Inference with a Variable-Length Grouped Activation Data Format | HPCA 2025 | KU Leuven; Nanjing University 等 | Anda 用可变长度 grouped activation 格式适配不同激活分布，在规则硬件上降低存储与计算成本。 |
| PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM | HPCA 2025 | HPCA 2025 官方目录未列单位 | PAISE 将 Transformer 请求调度与 PIM 执行特征联合建模，降低内存密集 decode 的排队和数据移动。 |
| Make LLM Inference Affordable to Everyone: Augmenting GPU Memory with NDP-DIMM | HPCA 2025 | HPCA 2025 官方目录未列单位 | NDP-DIMM 用带近数据处理能力的 DIMM 扩展 GPU 可用模型容量，并减少经 PCIe 搬运全部权重的开销。 |
| Lincoln: Real-Time 50~100B LLM Inference on Consumer Devices with LPDDR-Interfaced, Compute-Enabled Flash Memory | HPCA 2025 | HPCA 2025 官方目录未列单位 | Lincoln 用 LPDDR 接口连接具备计算能力的 flash，使消费设备能够流式执行 50B 到 100B 级模型。 |
| LLMulator: Generalizable Cost Modeling for Dataflow Accelerators with Input-Adaptive Control Flow | MICRO 2025 | ICT, CAS; University of Chinese Academy of Sciences | LLMulator 为带输入自适应控制流的数据流加速器建立可泛化成本模型，帮助预测 LLM workload 的性能。 |
| HLX: A Unified Pipelined Architecture for Optimized Performance of Hybrid Transformer-Mamba Language Models | MICRO 2025 | KAIST | HLX 为 Transformer-Mamba 混合模型统一 attention、state update 与 GEMM pipeline，减少架构切换空泡。 |
| Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving | MICRO 2025 | KAIST; Microsoft Research 等 | Pimba 用共享 state-update processing unit 和 MX 低精度算术支持 SSM、线性注意力及 Transformer 服务。 |
| MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation | arXiv 预印本, 2026 | 作者公开稿未列单位 | MX-SAFE 在线切换 exponent/mantissa 分配模式，使同一 microscaling 格式同时适应训练和直接量化推理。 |
| Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference | SOSP 2025 | SOSP 2025 官方目录未列单位 | 该工作测量移动 SoC 中 CPU、GPU、NPU 和内存子系统对不同 LLM 阶段的适配程度。 |
| KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models | SOSP 2025 | Tsinghua University; ICT, CAS 等 | KTransformers 把活跃 expert、attention 与其他算子分配到 CPU/GPU，并用定制 kernel 提升本地 MoE 推理。 |
| LithOS: An Operating System for Efficient Machine Learning on GPUs | SOSP 2025 | SOSP 2025 官方目录未列单位 | LithOS 以操作系统抽象管理 GPU kernel、内存和并发执行，为多租户 ML workload 提供隔离与复用。 |
| Mercury: Unlocking Multi-GPU Operator Optimization for LLMs via Remote Memory Scheduling | SOSP 2025 | SOSP 2025 官方目录未列单位 | Mercury 把远程 GPU 内存纳入 operator 调度，使单个算子可跨 GPU 利用空闲容量和带宽。 |
| PhoenixOS: Concurrent OS-level GPU Checkpoint and Restore with Validated Speculation | SOSP 2025 | SOSP 2025 官方目录未列单位 | PhoenixOS 在操作系统层并发执行 GPU checkpoint/restore，并通过验证式推测减少暂停时间。 |
| Multiplexed Heterogeneous LLM Serving via Stage-Aligned Parallelism | SoCC 2025 | SoCC 2025 官方目录未列单位 | 该工作按模型阶段对齐异构设备的并行与复用方式，避免 prefill/decode 在不同硬件上的能力错配。 |
| gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling | SC 2025 | SC 2025 官方目录未列单位 | gLLM 用全局平衡 pipeline 和 token throttling 控制阶段间流速，减少分布式 serving 的空泡和拥塞。 |
| LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving | SC 2025 | SC 2025 官方目录未列单位 | LiquidGEMM 针对 W4A8 推理设计硬件高效的反量化、数据布局和 GEMM kernel。 |
| HELM: Characterizing Unified Memory Accesses to Improve GPU Performance under Memory Oversubscription | SC 2025 | SC 2025 官方目录未列单位 | HELM 刻画统一内存超配时的访问与迁移行为，为超出 HBM 容量的模型部署提供优化依据。 |
| Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism | arXiv 预印本, 2019 | NVIDIA | Megatron-LM 建立 tensor model parallel 的核心拆分方法，后续成为训练和推理 runtime 的基础。 |
| TurboTransformers: An Efficient GPU Serving System for Transformer Models | PPoPP 2021 | Tencent; Peking University | TurboTransformers 用动态 batch、序列长度感知调度和融合 kernel 加速早期 Transformer 在线服务。 |
| LightSeq: A High Performance Inference Library for Transformers | NAACL 2021 System Demonstrations | ByteDance | LightSeq 通过 layer fusion、定制 CUDA kernel 和显存复用提供 Transformer 推理库。 |
| DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale | SC 2022 | Microsoft | DeepSpeed Inference 通过 inference-adapted parallelism、kernel injection 和量化部署超大 Transformer。 |
| MegaBlocks: Efficient Sparse Training with Mixture-of-Experts | MLSys 2023 | Stanford University; Google 等 | MegaBlocks 把动态 token routing 转化为 block-sparse operation，避免 expert capacity padding；其 kernel 思路影响 MoE inference。 |
| Tutel: Adaptive Mixture-of-Experts at Scale | MLSys 2023 | Microsoft Research Asia 等 | Tutel 以自适应并行、all-to-all 和 fused kernel 构建通用 MoE runtime。 |
| LUMEN: Coordinated Failure Recovery for Distributed LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | LUMEN 把分布式 LLM serving 的故障恢复建模为 checkpoint 放置、请求重分配和 reload 期间容量恢复的联合负载协调问题。 |
| Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作按 Prefill/Decode 两阶段分别测 TTFT、TPOT 和批量吞吐，比较 GPU 与新型 AI 加速器的相位优势。 |
| Efficient On-Device Diffusion LLM Inference with Mobile NPU | arXiv 预印本, 2026 | 作者公开稿未列单位 | llada.cpp 通过多块推测解码、渐进式修正与 swap 优化运行时，把 diffusion LLM 对齐到手机 NPU 的执行特性。 |
| Latency Prediction for LLM Inference on NPU Systems | arXiv 预印本, 2026 | 作者公开稿未列单位 | LENS 只用少量端到端 profile 即可建模 NPU 上由 compiler 和 bucketing 引起的非线性推理时延。 |
| FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation | arXiv 预印本, 2026 | 作者公开稿未列单位 | FlexServe 在移动端用可调资源隔离和安全执行路径协调本地 LLM serving 的延迟、隔离和资源复用。 |
| AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | AGENTSERVESIM 用 program orchestration、tool gap 模拟、session-aware routing 和 KV residency 模型，在 CPU 上逼真评估多轮 agent serving 策略。 |
| MemExplorer: Navigating the Heterogeneous Memory Design Space for Agentic Inference NPUs | arXiv 预印本, 2026 | 作者公开稿未列单位 | MemExplorer 联合搜索异构 NPU 与多级内存配置，在 agentic inference 的 prefill/decode 场景下平衡吞吐与功耗。 |
| Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | AsymCache 通过 Multi-Segment Attention、位置感知驱逐与自适应 chunking，让 lossless KV 管理与 GPU attention kernel 的效率目标对齐。 |
| ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | ReMP 将模型并行拓扑与运行时状态解耦，并用二维 KV 迁移在 TP/PP 重配置时尽量保留可复用缓存。 |
| SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions | arXiv 预印本, 2026 | 作者公开稿未列单位 | SMEPilot 用 roofline 驱动的算子级选择，在 CPU-only、SME-only 与 SME+CPU 协作执行之间动态切换。 |
| WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware | arXiv 预印本, 2026 | Nokia | WiSP 将 expert 权重与 KV cache 统一建模为 GPU working set，并用 MV-WSA 在两者之间动态分配 VRAM 以提升低资源 MoE serving 吞吐。 |
| LLMInfer-Bench: Building the Virtuous Cycle for AI-driven LLM Systems | MLSys 2026 | OpenReview 公开稿未列单位 | LLMInfer-Bench 把 AI 生成 kernel、benchmark 和 serving runtime 连接起来，为 LLM inference kernel 的自动优化提供闭环评测。 |
| Efficient, VRAM-Constrained xLM Inference on Clients | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作用 profile-guided CPU-GPU pipelined sharding、tensor placement 和 VLMOpt，在受限客户端 VRAM 上运行 dense/MoE LLM 与 VLM。 |
| PROMPTS: PeRformance Optimization via Multi-Agent Planning for LLM Training and Serving | MLSys 2026 | OpenReview 公开稿未列单位 | PROMPTS 用 analyzer/proposal 多智能体系统读取 profiler 数据并生成 sharding 配置，在训练和 serving workload 上自动提出系统级优化方案。 |
| Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel | MLSys 2026 | OpenReview 公开稿未列单位 | Event Tensor 用统一事件张量抽象编译动态 megakernel，减少 LLM inference 中 kernel launch 和跨算子同步开销。 |
| MAC-Attention: a Match-Amend-Complete scheme for fast and accurate attention computation | MLSys 2026 | OpenReview 公开稿未列单位 | MAC-Attention 将 attention 计算拆成匹配、修正和补全阶段，在控制误差的同时减少长上下文注意力开销。 |
| BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding | MLSys 2026 | OpenReview 公开稿未列单位 | BLASST 在 online softmax 中按阈值动态跳过低贡献 attention block，减少 Value block 加载和后续矩阵乘法以加速长上下文 prefill/decode。 |
| IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference | MLSys 2026 | OpenReview 公开稿未列单位 | IntAttention 用整数域 IndexSoftmax 和端到端 INT8 attention pipeline 消除反量化-浮点 softmax-再量化路径，降低端侧延迟和能耗。 |
| FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | MLSys 2026 | OpenReview 公开稿未列单位 | FlashAttention-4 针对非对称硬件扩展重做 attention 算法和 kernel pipeline 协同设计，提高长上下文与大模型注意力吞吐。 |
| ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels | MLSys 2026 | OpenReview 公开稿未列单位 | ParallelKittens 提供更系统的多 GPU kernel 编程与组合方式，降低跨 GPU LLM inference kernel 的实现复杂度。 |
| ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping | OSDI 2026 | Shanghai Jiao Tong University | ADAngel 为任意精度量化 LLM 自适应映射计算路径，使不同 bit-width 的解码和矩阵运算更好匹配硬件资源。 |
| SHIP: SRAM-Based Huge Inference Pipelines for Fast LLM Serving | MLSys 2026 | OpenReview 公开稿未列单位 | SHIP 用 SRAM-based huge inference pipeline 组织 LLM serving 数据流，减少生成阶段对外部内存带宽的依赖。 |
| MixLLM: LLM Quantization with Global Mixed-precision between Output-features and Highly-efficient System Design | MLSys 2026 | OpenReview 公开稿未列单位 | MixLLM 在 output-feature 维度做全局混合精度量化，并配套高效反量化和流水重叠 kernel 以提升低比特推理吞吐。 |
| Rethinking DVFS for Mobile LLMs: Unified Energy-Aware Scheduling with CORE | MLSys 2026 | OpenReview 公开稿未列单位 | CORE 将移动 LLM 的频率调节、阶段调度和能耗模型统一起来，在端侧 SLO 下减少 CPU/GPU/NPU 能耗。 |
| TokenBlend: Accelerating Tensor Parallelism LLM Inference Through Efficient Compute-Communication Overlap | MLSys 2026 | OpenReview 公开稿未列单位 | TokenBlend 融合 AllReduce 与 RMSNorm，在 tensor-parallel decode 中用少量 SM 重叠通信和计算，降低 NVLink 通信开销。 |
| Optimizing PyTorch Inference with LLM-Based Multi-Agent Systems | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作系统比较 LLM 多智能体优化 PyTorch 推理代码的策略，用 KernelBench/H100 评估 agentic kernel tuning 对端到端推理性能的提升。 |
| AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization | MLSys 2026 | MLSys 2026 官方页面未列单位 | AccelOpt 将 LLM agent 用于 AI accelerator kernel 优化闭环，让生成、profile、修复和迭代搜索共同改进算子实现。 |
| CATWILD: Compiler Autotuning for TPU workloads in the Wild | MLSys 2026 | MLSys 2026 官方页面未列单位 | CATWILD 面向真实 TPU workload 做 compiler autotuning，降低手工调参成本并改善生产模型在 TPU 上的执行效率。 |
| Agentic Operator Generation for ML ASICs | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作用 agentic generation 生成和优化 ML ASIC operator，把硬件目标、算子约束和验证反馈纳入自动化代码生成流程。 |
| ApproxMLIR: Accuracy-Aware Compiler for Compound ML System | MLSys 2026 | MLSys 2026 官方页面未列单位 | ApproxMLIR 把精度影响纳入 compound ML system 编译优化，使近似执行、算子替换和系统性能可以一起权衡。 |
| HipKittens: Fast and Furious AMD Kernels | MLSys 2026 | MLSys 2026 官方页面未列单位 | HipKittens 面向 AMD GPU 提供高性能 kernel 编程与优化路径，补齐 AI 推理/训练算子在非 CUDA 平台上的性能生态。 |
| WAVE: A SYMBOLIC PYTHON DSL AND COMPILER FOR HIGH PERFORMANCE MACHINE LEARNING | MLSys 2026 | MLSys 2026 官方页面未列单位 | WAVE 用符号化 Python DSL 和编译器表达高性能 ML kernel，降低从算法描述到硬件高效实现的距离。 |
| Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants | MLSys 2026 | MLSys 2026 官方页面未列单位 | Flashlight 扩展 PyTorch compiler 来支持 attention 变体加速，使新注意力算子更容易进入生产编译与执行路径。 |
| Search Your NVFP4 Scales! | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作围绕 NVFP4 量化 scale 搜索优化低精度执行配置，服务于新一代 GPU 上 LLM 推理的吞吐和精度折中。 |
| A Lightweight High-Throughput Collective-Capable NoC for Large-Scale ML Accelerators | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作为大规模 ML accelerator 设计支持 collective 的轻量高吞吐 NoC，针对多核/多芯粒训练和推理通信瓶颈优化片上互连。 |
| Dataflow Is All You Need | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作把 dataflow 作为 ML 系统执行和优化的核心抽象，面向复杂模型流水、并行和内存调度提供统一表达。 |
| ExecuTorch - A Unified PyTorch Solution to Run ML Models On-Device | MLSys 2026 | MLSys 2026 官方页面未列单位 | ExecuTorch 提供 PyTorch-native 端侧部署框架，覆盖微控制器、移动 SoC 和专用加速器，并支持量化与可插拔后端。 |
| Attribution-based Sparse Activation in Large Language Models | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作用 attribution 信号选择性激活 LLM 中的计算路径，为稀疏推理和低成本动态执行提供模型-系统接口。 |
| Unified LLM Model for Power, Performance, and Area Prediction from Hardware Code | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作用统一 LLM 模型从硬件代码预测功耗、性能和面积，辅助 AI accelerator 设计空间探索和早期筛选。 |
| Flash3DGS: Algorithm and System Co-Optimization for Fast 3D Gaussian Splatting on GPUs | MLSys 2026 | MLSys 2026 官方页面未列单位 | Flash3DGS 将算法结构与 GPU 系统实现协同优化，提高 3D Gaussian Splatting 的训练/渲染吞吐。 |
| Automated Algorithm Design for Auto-Tuning Optimizers | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作把算法设计自动化用于 optimizer auto-tuning，减少大模型训练优化器在不同模型和硬件上的手工搜索成本。 |
| Pylo: Towards Accessible Learned Optimizers in PyTorch | MLSys 2026 | MLSys 2026 官方页面未列单位 | Pylo 将 learned optimizer 更自然地接入 PyTorch 工作流，降低训练系统中使用和评估学习型优化器的工程门槛。 |
| VeriMoA: A Mixture-of-Agents Framework for Spec-to-HDL Generation | MLSys 2026 | MLSys 2026 官方页面未列单位 | VeriMoA 用 mixture-of-agents 流程从规格生成 HDL，并把多 agent 验证反馈纳入硬件设计自动化闭环。 |
| Spira: Exploiting Voxel Data Structural Properties for Efficient Sparse Convolution in Point Cloud Networks | MLSys 2026 | MLSys 2026 官方页面未列单位 | Spira 利用 voxel 数据结构特性优化 sparse convolution，为点云网络的高效训练和推理提供专用系统路径。 |
| Once-for-All Channel Mixers (HyperTinyPW): Generative Compression for TinyML | MLSys 2026 | MLSys 2026 官方页面未列单位 | HyperTinyPW 面向 TinyML 做生成式 channel mixer 压缩，减少端侧模型部署的参数和计算成本。 |
| SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation | arXiv 预印本, 2026 | 作者公开稿未列单位 | SpecGen 将 speculative generation 引入 GPU kernel 自动优化流程，复用历史候选和验证结果以减少 agentic kernel search 的迭代成本。 |
| EnerInfer: Energy-Aware On-Device LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | EnerInfer 面向端侧 LLM 推理联合调度模型阶段、设备频率和资源分配，在延迟约束下降低移动设备能耗。 |

## MoE、Adapter、多租户与模型服务

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| BrownoutServe: SLO-Aware Inference Serving under Bursty Workloads for MoE-based LLMs | arXiv 预印本, 2025 | Shenzhen University 等 | BrownoutServe 在突发流量下动态减少部分 expert 访问并使用 united experts，在精度和 SLO 之间调节。 |
| DuoServe-MoE: Dual-Phase Expert Prefetch and Cache Scheduling for Efficient MoE LLM Inference | arXiv 预印本, 2025 | University of Sydney 等 | DuoServe-MoE 为 prefill 和 decode 设计不同 expert prefetch/cache 策略，以较小显存运行大型 MoE。 |
| LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training | ASPLOS 2026 | Peking University; Shanghai Jiao Tong University; ByteDance Seed | LAER-MoE 根据 expert 负载动态重排布局，属于与推理基础设施相邻的 MoE 训练系统工作。 |
| gShare: Efficient GPU Sharing with Aggressive Scheduling in Multi-tenant FaaS Platform | ASPLOS 2026 | China Telecom | gShare 在多租户 FaaS 中采用激进 GPU 共享和调度，提高短时、突发 AI function 的设备利用率。 |
| CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation | arXiv 预印本, 2026 | 作者公开稿未列单位 | CrossPool 面向冷门 MoE 模型服务，把 KV cache 和权重分别做池化/分离管理，降低多模型长尾部署的显存常驻成本。 |
| Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments | MICRO 2025 | University of Illinois Urbana-Champaign; IBM | Chameleon 联合管理大量 LoRA/adapter 的缓存和请求调度，减少多租户适配器服务中的换入与等待。 |
| LLM Zeroth-Order Fine-Tuning is an Inference Workload | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把 zeroth-order 微调的重复 forward scoring 重构为 serving workload，使 adapter 更新可复用推理 runtime。 |
| Symbiosis: Multi-Adapter Inference and Fine-Tuning | SoCC 2025 | SoCC 2025 官方目录未列单位 | Symbiosis 在共享基础模型上协同执行多 adapter 推理和微调，减少参数副本与资源冲突。 |
| ZipBatch: Multi-Tenant GPU Batching with Dual-Resource Regulation | SoCC 2025 | SoCC 2025 官方目录未列单位 | ZipBatch 同时约束计算和内存两类资源，将不同 tenant 请求组合为稳定高效的 GPU batch。 |
| MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | MixNet 根据 MoE 动态 all-to-all 流量重配置光电混合 fabric，缓解 expert routing 热点。 |
| Diff-MoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching | SC 2025 | SC 2025 官方目录未列单位 | Diff-MoE 根据 expert 优先级采用差异化缓存，并面向 batch 复用热点 expert。 |
| DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale | ICML 2022 | Microsoft | DeepSpeed-MoE 联合优化 expert parallel、通信和模型压缩，使大规模 MoE 同时具备训练和推理可行性。 |
| Coordinated Scheduling for MoE LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Gimbal 联合前端 DP-engine 调度与后端 expert 放置，按 KV 压力、prefill 余量和 expert 热点协调 MoE serving。 |
| ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | ELDR 根据 prefill expert activation 构建 expert signature，并用 locality-band routing 把请求发往 expert locality 更好的 decode worker，降低 PD 分离式 MoE serving 的 decode 延迟。 |
| A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | ST-MoE 利用跨层和跨 token 的 expert 激活相关性做时空联合预取，以重叠 expert 加载和 MoE 推理计算。 |
| Fast MoE Inference via Predictive Prefetching and Expert Replication | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作预测热点 expert 并做动态复制和预取，以减少稀疏激活造成的等待和 GPU 空转。 |
| CRAFT: Cost-aware Expert Replica Allocation with Fine-Grained Layerwise Estimations | MLSys 2026 | MLSys 2026 官方页面未列单位 | CRAFT 按层估计 expert 负载和复制收益，在成本约束下为 MoE expert 分配副本，降低热点专家导致的排队和通信开销。 |
| MoEBlaze: Breaking the Memory Wall for Efficient MoE Training on Modern GPUs | MLSys 2026 | MLSys 2026 官方页面未列单位 | MoEBlaze 针对现代 GPU 上 MoE 训练的显存墙优化 expert 参数、激活和通信组织，为大规模 MoE 系统提供训练侧基础设施。 |
| FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error | MLSys 2026 | MLSys 2026 官方页面未列单位 | FP8-Flow-MoE 为 MoE 设计避免重复量化误差的 FP8 执行配方，减少 expert 路径中的 cast 和量化开销。 |
| Demystifying the Mixture of Experts Serving Tax | MLSys 2026 | OpenReview 公开稿未列单位 | 该工作量化 MoE serving 相比 dense 模型额外付出的通信、调度、缓存和尾延迟成本，为专家系统优化建立分解指标。 |
| BatchGen: An Architecture for Scalable and Efficient Batch Inference | OSDI 2026 | University of Edinburgh; Tencent | BatchGen 面向可扩展批量推理架构，优化大批请求在专家/混合推理负载中的组织与资源利用。 |
| Capacity-Aware Inference: Mitigating the Straggler Effect in Mixture of Experts | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Capacity-Aware Inference 通过 token drop 和 token reroute 缓解 MoE expert 负载不均造成的 straggler latency。 |
| FarSkip-Collectives: Unhobbling Blocking Communication in Mixture of Experts Models | MLSys 2026 | OpenReview 公开稿未列单位 | FarSkip-Collectives 针对 MoE 阻塞式通信设计可跳过或重排的 collective 路径，减少 expert 并行中的通信等待。 |
| Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Semantic Parallelism 将 token 语义聚类和 expert 放置协同调度，减少 MoE expert parallel 中昂贵的跨设备 all-to-all。 |
| Libra: Effective yet Efficient Load Balancing for Large-scale MoE Inference | ICLR 2026 Poster | OpenReview 公开稿未列单位 | Libra 为大规模 MoE inference 设计低开销负载均衡机制，在避免 expert 热点的同时不引入新的通信瓶颈。 |
| SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models | ICLR 2026 Poster | OpenReview 公开稿未列单位 | SERE 在 batch decoding 中按相似性重路由 expert，降低 MoE 批处理时的专家激活发散和内存带宽压力。 |
| BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE | arXiv 预印本, 2025 | 作者公开稿未列单位 | BEAM 用二值 expert activation mask 做动态路由，减少 MoE 推理中不必要的 expert 激活和通信。 |
| Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作按任务相关性组织 MoE expert/grouping，减少多任务 MoE 推理中的跨设备通信和路由冲突。 |
| Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention | arXiv 预印本, 2026 | 作者公开稿未列单位 | GQE 在 grouped-query attention 内只对 query head 做 expert routing，保留 GQA 的 KV cache 优势，同时减少长上下文 attention 的活跃计算。 |

## Agent、RAG、多模态与应用级 Serving

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| SGLang: Efficient Execution of Structured Language Model Programs | NeurIPS 2024 | Stanford University; UC Berkeley; Shanghai Jiao Tong University; Texas A&M University | SGLang 用 RadixAttention、结构化生成语言和高性能 runtime 统一优化多调用、共享前缀和约束生成工作流。 |
| Parrot: Efficient Serving of LLM-based Applications with Semantic Variable | arXiv 预印本, 2024 | Microsoft Research; Shanghai Jiao Tong University | Parrot 用 Semantic Variable 暴露多调用应用的数据流和依赖，使服务端能跨请求做 batching、缓存与流水优化。 |
| AI Metropolis: Scaling Large Language Model-based Multi-Agent Simulation with Out-of-order Execution | MLSys 2025 | Stanford University; Georgia Institute of Technology | AI Metropolis 跟踪 agent 间真实依赖并乱序执行，消除全局同步造成的伪依赖和 GPU 空闲。 |
| XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | MLSys 2025 | Carnegie Mellon University; MLC community | XGrammar 预处理上下文无关 token、压缩运行时 grammar 状态，并与 GPU 推理重叠以实现近零开销结构化生成。 |
| Towards Efficient Large Multimodal Model Serving | arXiv 预印本, 2025 | Microsoft Research; Clemson University; Brown University | 该工作基于生产多模态 trace 分析 encode/prefill/decode 的异质性，并提出分阶段资源分配和自适应伸缩。 |
| Cornserve: Efficiently Serving Any-to-Any Multimodal Models | arXiv 预印本, 2025 | University of Michigan | Cornserve 从任意到任意多模态 computation graph 自动规划组件拆分和部署，并用分布式 runtime 处理路径异质性。 |
| Serve Programs, Not Prompts | arXiv 预印本, 2025 | Yale University | 该工作提出 LLM Inference Program 和 Symphony OS，将 token prediction、KV 文件系统及工具执行变成服务端可调度程序。 |
| Agentix: An Efficient Serving Engine for LLM Agents as General Programs | NSDI 2026 | UC Berkeley; Google DeepMind; Shanghai Jiao Tong University | Agentix 把 agent program 而非单次请求作为调度对象，利用程序依赖和已完成调用对后续 LLM call 抢占与提权。 |
| Towards Sustainable Large Language Model Serving | HotCarbon 2024 | University of Waterloo; Purdue University | 该工作同时建模 GPU 运行能耗、电网碳强度和芯片 embodied carbon，分析硬件代际选择的碳排权衡。 |
| AccelGen: Heterogeneous SLO-Guaranteed High-Throughput LLM Inference Serving for Diverse Applications | arXiv 预印本, 2025 | University of Virginia | AccelGen 用动态 chunk、iteration SLO 优先级和 compute/KV 双资源感知 batching 服务长短 prompt 与不同延迟约束。 |
| AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving | arXiv 预印本, 2025 | Zhejiang University 等 | AugServe 针对 tool-augmented 请求用两阶段调度和动态 token batch limit 缓解未知暂停与队头阻塞。 |
| DiffServe: Efficiently Serving Text-to-Image Diffusion Models with Query-Aware Model Scaling | MLSys 2025 | University of Massachusetts Amherst | DiffServe 按 prompt 难度在不同规模 diffusion model 间路由，并联合优化模型选择与资源配置。 |
| ScaleFusion: Scalable Inference of Spatial-Temporal Diffusion Transformers for High-Resolution Long Video Generation | MLSys 2025 | University of Toronto; AWS | ScaleFusion 针对高分辨率长视频 DiT 设计时空并行、通信重叠和动态执行策略。 |
| MoDM: Efficient Serving for Image Generation via Mixture-of-Diffusion Models | arXiv 预印本, 2025 | Intel Labs 等 | MoDM 以最终图像 cache 和大小 diffusion model 混合路由，在响应质量、延迟和 GPU 分配间动态权衡。 |
| HADIS: Hybrid Adaptive Diffusion Model Serving for Efficient Text-to-Image Generation | arXiv 预印本, 2025 | University of Massachusetts Amherst | HADIS 联合选择 cascade、prompt routing 和 GPU allocation，让明显困难的请求绕过无效轻量模型阶段。 |
| TridentServe: A Stage-level Serving System for Diffusion Pipelines | arXiv 预印本, 2025 | Peking University; Carnegie Mellon University; University of Cambridge | TridentServe 将 encode、diffuse、decode 分阶段放置，并动态联合优化模型 placement 与请求 dispatch。 |
| Efficient LLM Serving for Agentic Workflows with Context-Aware State Management | EuroSys 2026 poster | University of Cambridge; Polytechnique Montréal | 该工作针对 agent 多轮调用中的可复用上下文和中间状态设计 context-aware 管理机制，减少重复 prefill 与状态搬运。 |
| LLMServingSim 2.0: An Enhanced Simulator for LLM Serving Systems with Graph-Based Workloads | arXiv 预印本, 2026 | Seoul National University | LLMServingSim 2.0 用图结构表达多阶段、分支和 agent 请求，为新调度与异构部署方案提供可重复仿真平台。 |
| Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Tangram 以确定性 head 预算、Head Group Page 和 AOT 负载均衡，把非均匀 KV 压缩转化为可高效执行的 serving layout。 |
| Pie: A Programmable Serving System for Emerging LLM Applications | SOSP 2025 | SOSP 2025 官方目录未列单位 | Pie 允许应用表达多阶段生成、工具调用和状态依赖，由可编程 runtime 统一调度。 |
| Rethinking Web Cache Design for the AI Era | SoCC 2025 | SoCC 2025 官方目录未列单位 | 该工作重新审视 AI agent 与生成内容对传统 Web cache 的对象、更新和一致性语义。 |
| Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention | USENIX ATC 2024 | National University of Singapore; Shanghai Jiao Tong University; Huawei Cloud | CachedAttention 维护分层 KV cache，并用 layer-wise preload、异步保存和 scheduler-aware 淘汰降低多轮会话 TTFT。 |
| Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents | arXiv 预印本, 2026 | 作者公开稿未列单位 | FCGraft 复用函数级代码骨架及其 KV cache，通过 stitching 和 patching 减少 embodied agent 代码策略生成中的重复 prefill。 |
| Agentic AI Workload Characteristics | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作用端到端 tracing 刻画 ReAct 类 agent workload，指出有效上下文缓存会让执行转向 decode-dominated 且依赖长寿命 KV 状态。 |
| KAIROS: Stateful, Context-Aware Power-Efficient Agentic Inference Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | KAIROS 以 agent 上下文为控制信号，联合调节 GPU 频率、并发度与跨实例放置，在避免 thrashing 的前提下降低 agentic serving 功耗。 |
| Parallel Context Compaction for Long-Horizon LLM Agent Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把长程 agent 的上下文压缩拆成并行 block compaction，在相同压缩输出量下缩短阻塞式 summarization 带来的端到端时延。 |
| AAFLOW: Scalable Patterns for Agentic AI Workflows | arXiv 预印本, 2026 | 作者公开稿未列单位 | AAFLOW 将 agent workflow 建模为算子图，并用 Arrow/Cylon 的零拷贝数据平面与异步批处理降低 embedding、upsert 与 orchestration 开销。 |
| Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Execution-State Capsules 将 agent/physical-AI workflow 的执行状态绑定到图节点，用小批量 checkpoint/restore 降低端侧服务恢复延迟。 |
| Murakkab: Resource-Efficient Agentic Workflow Orchestration in Cloud Platforms | OSDI 2026 | MIT CSAIL; Microsoft Azure Research | Murakkab 将 agentic workflow 的依赖、暂停和资源需求暴露给云平台，在多步 LLM 应用中减少同步等待和过量配置。 |
| AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving | ICLR 2026 Poster | OpenReview 公开稿未列单位 | AdaCache 针对 RAG 中高频检索片段做自适应缓存和上下文增强，减少重复处理长输入带来的 prefill 开销。 |
| RagInfer: Efficient Retrieval-Augmented Generation Inference with Lookahead Retrieval | MLSys 2026 | OpenReview 公开稿未列单位 | RagInfer 用 lookahead retrieval 将检索和生成阶段重叠，降低大规模 RAG datastore 引入的在线推理延迟。 |
| Hippocampus: An Efficient and Scalable Memory Module for Agentic AI | MLSys 2026 | OpenReview 公开稿未列单位 | Hippocampus 为 agentic AI 提供可扩展长期记忆模块，替代纯向量库或图遍历导致的高延迟记忆访问。 |
| FlashAgents: Accelerating Multi-Agent LLM Systems via Streaming Prefill Overlap | MLSys 2026 | OpenReview 公开稿未列单位 | FlashAgents 用 agent 间 token streaming、增量 prefill 和 prefix-aware coordination 重叠多智能体调用链中的等待与计算。 |
| Scaling Up Large Language Models Serving Systems for Semantic Job Search | MLSys 2026 | OpenReview 公开稿未列单位 | 该工业系统论文围绕语义职位搜索部署 LLM serving，处理检索、生成和在线容量约束下的规模化落地问题。 |
| AgenticCache: Cache-Driven Asynchronous Planning for Embodied AI Agents | MLSys 2026 | OpenReview 公开稿未列单位 | AgenticCache 用缓存命中和状态复用驱动 embodied agent 的异步规划，减少重复上下文构造和工具调用等待。 |
| Ontology-Guided Long-Term Memory for Conversational RAG | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作用 ontology 组织 conversational RAG 的长期记忆，使检索、更新和上下文装配更适合长会话与跨轮知识复用。 |
| StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation | MLSys 2026 | MLSys 2026 官方页面未列单位 | StreamDiffusionV2 面向动态交互式视频生成构建 streaming serving 系统，降低连续视频生成中的等待和资源浪费。 |
| EarthSight: A Distributed Framework for Low-Latency Satellite Intelligence | MLSys 2026 | MLSys 2026 官方页面未列单位 | EarthSight 将卫星智能任务组织为分布式低延迟推理框架，覆盖边缘采集、模型执行和结果回传的端到端系统问题。 |
| The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents | MLSys 2026 | MLSys 2026 官方页面未列单位 | OpenHands SDK 为生产级软件 agent 提供可组合、可扩展的执行基础设施，支撑工具调用、状态管理和多组件编排。 |
| Matrix: Peer-to-Peer Multi-Agent Synthetic Data Generation Framework | MLSys 2026 | MLSys 2026 官方页面未列单位 | Matrix 用 peer-to-peer 多智能体框架组织合成数据生成，关注 agent 间任务分配、通信和扩展性。 |
| ADS: AN AGENTIC DETECTION SYSTEM FOR ENTERPRISE AGENTIC AI SECURITY | MLSys 2026 | MLSys 2026 官方页面未列单位 | ADS 面向企业 agentic AI 安全构建检测系统，把 agent 行为、工具调用和安全策略纳入运行时监控。 |
| ViCoStream: Streaming VideoLLMs Can Run Beyond 100 FPS with Stage-Wise Coordinated Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | ViCoStream 将 streaming VideoLLM 推理拆成阶段并协调执行，使视频理解服务在高帧率输入下保持低延迟和高吞吐。 |
| TetherCache: Stabilizing Autoregressive Long-Form Video Generation with Gated Recall and Trusted Alignment | arXiv 预印本, 2026 | 作者公开稿未列单位 | TetherCache 为长视频生成维护 gated recall cache 和 trusted alignment，减少长程生成中的上下文漂移和重复计算。 |
| Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作尝试在 LLM-agent workflow 的并行分支之间合成 latent state，减少分支合并时的重复上下文构造和推理调用。 |
| db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism | MLSys 2026 | MLSys 2026 官方页面未列单位 | db-SP 面向视觉生成模型的稀疏 attention 设计 dual-balanced sequence parallelism，降低长序列视觉生成中的负载不均和跨设备通信。 |

## Workload、评测、可靠性与方法论

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| DejaVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving | ICML 2024 | ETH Zurich; Carnegie Mellon University; Microsoft Research | DejaVu 用 KV-cache streaming 支持 prompt-token 分离、microbatch swapping 和状态复制，缓解流水线空泡、显存过配和故障恢复问题。 |
| Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services | OSDI 2024 | University of Michigan | Andes 将用户可感知的首 token 和流式平滑度建模为 QoE，并用 token-level preemptive scheduling 优化体验。 |
| One Queue Is All You Need: Resolving Head-of-Line Blocking in Large Language Model Serving | arXiv 预印本, 2024 | IBM Research; University of Illinois Urbana-Champaign | QLM 用多模型队列编排、模型换入换出和请求状态迁移缓解 burst workload 下的队头阻塞。 |
| OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration | arXiv 预印本, 2026 | University of Cambridge; Shanghai Jiao Tong University 等 | OServe 针对请求空间异质性和流量时间变化，动态选择异构模型部署并迁移并行配置。 |
| BurstGPT: A Real-world Workload Dataset to Optimize LLM Serving Systems | arXiv 预印本, 2024 | Hong Kong Baptist University; Microsoft Azure 等 | BurstGPT 发布 Azure OpenAI 服务的五百余万条真实 trace，揭示 burst、长度和失败模式对调度评估的影响。 |
| Online Scheduling for LLM Inference with KV Cache Constraints | arXiv 预印本, 2025 | Microsoft Research | 该工作将 KV cache 容量约束纳入 online scheduling 理论，分析 batching、延迟与 hindsight optimal 的竞争关系。 |
| Fairness in Serving Large Language Models | arXiv 预印本, 2024 | UC Berkeley; Stanford University | VTC 用输入输出 token 成本定义 work-conserving fairness，避免长请求或大客户长期占用 continuous batching 能力。 |
| GreenLLM: SLO-Aware Dynamic Frequency Scaling for Energy-Efficient LLM Serving | arXiv 预印本, 2025 | EPFL | GreenLLM 对 prefill/decode 分别建模和调频，在维持 token SLO 的同时降低 GPU 能耗。 |
| FailSafe: High-performance Resilient Serving | arXiv 预印本, 2025 | Stanford University | FailSafe 用循环 KV 放置、混合 attention、负载路由和主动 KV 备份，使 tensor-parallel serving 在 GPU 故障后继续运行。 |
| ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production | NSDI 2026 | Peking University; Alibaba Group | ServeGen 基于全球云服务 trace 刻画语言、多模态和 reasoning 模型负载，并按 client 组合生成更真实的 benchmark workload。 |
| Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems | arXiv 综述, 2023 | Carnegie Mellon University 等 | 该综述从算法、单机 runtime 到分布式 serving 系统梳理生成式 LLM 推理的效率技术与研究问题。 |
| LLM Inference Serving: Survey of Recent Advances and Opportunities | arXiv 综述, 2024 | Northeastern University; MIT Lincoln Laboratory | 该综述聚焦 2023 年后的系统级 LLM serving 论文，覆盖调度、内存、并行和生产部署机会。 |
| Taming the Titans: A Survey of Efficient LLM Inference Serving | arXiv 综述, 2025 | Soochow University; Alibaba Cloud 等 | 该综述按 instance、cluster 和新兴应用场景系统整理模型放置、调度、存储、分离架构及云端策略。 |
| KernelSight-LM: A Kernel-Level LLM Inference Simulator | arXiv 预印本, 2026 | 作者公开稿未列单位 | KernelSight-LM 用 roofline kernel model、通信模型与 host-overhead model 组成 token-level discrete-event simulator，在少量目标 GPU 数据下预测 TTFT/TPOT/throughput 并给出 kernel bottleneck breakdown。 |
| TetriServe: Efficiently Serving Mixed DiT Workloads | ASPLOS 2026 | University of Michigan; University of Wisconsin-Madison; Nanyang Technological University | TetriServe 面向不同扩散 Transformer 请求联合做批处理和资源编排，提高混合 DiT workload 的服务效率。 |
| throttLL'eM: Predictive GPU Throttling for Energy Efficient LLM Inference Serving | HPCA 2025 | HPCA 2025 官方目录未列单位 | throttLL'eM 预测 token 阶段的性能余量并动态调节 GPU 功率或频率，在满足 serving SLO 时降低能耗。 |
| DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency | HPCA 2025 | University of Illinois Urbana-Champaign; Microsoft | DynamoLLM 动态选择集群硬件、并行和功率配置，在请求 SLO、成本和能耗之间联合优化。 |
| A House United Within Itself: SLO-Awareness for On-Premises Containerized ML Inference Clusters via Faro | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | Faro 在本地容器化推理集群中联合做 workload 预测、资源分配与 autoscaling，以维持多模型 SLO。 |
| Improving GPU Sharing Performance through Adaptive Bubbleless Spatial-Temporal Sharing | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | 该工作在空间和时间两个维度自适应共享 GPU，并消除切换气泡，提高混合 AI workload 的利用率。 |
| Fine-grained Automated Failure Management for Extreme-Scale GPU Accelerated Systems | SC 2025 | SC 2025 官方目录未列单位 | 该工作自动定位并隔离极大 GPU 系统中的细粒度故障，为长时间运行的推理集群提供可靠性参考。 |
| PUZZLE: Efficiently Aligning Large Language Models through Light-Weight Context Switch | USENIX ATC 2024 | Tsinghua University | PUZZLE 根据模型和阶段相似性降低 RLHF 多模型 workload 的上下文切换与参数迁移开销。 |
| Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL | arXiv 预印本, 2026 | 作者公开稿未列单位 | HEAL 分析 LLM 推理中的数值不稳定和不可复现来源，并用可控校正路径提高关键任务输出一致性。 |
| Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该实证研究比较 MoE 在消费级和边缘硬件上的真实延迟、内存和能耗收益，避免只用理论 FLOPs 判断端侧可行性。 |
| Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | Concordia 用 JIT 编译的 persistent-kernel checkpointing 降低小 batch LLM 推理的容错快照开销。 |
| StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference | OSDI 2026 | Shanghai Jiao Tong University; Alibaba Cloud; Alibaba Group | StriaTrace 面向在线 LLM inference 提供低开销 tracing 和诊断，把请求、kernel、KV 状态和服务异常关联起来定位性能问题。 |
| RaidServe: High-performance Resilient Serving | MLSys 2026 | OpenReview 公开稿未列单位 | RaidServe 针对 tensor-parallel LLM serving 的单 GPU 故障设计冗余和恢复路径，减少故障后的 KV 复制和模型重载停顿。 |
| GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving | MLSys 2026 | OpenReview 公开稿未列单位 | GhostServe 在后台用 erasure coding 保护流式 KV cache，避免故障恢复时完整重算或复制全部 serving 状态。 |
| ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler | MLSys 2026 | OpenReview 公开稿未列单位 | ProfInfer 用 eBPF 对 LLM inference engine 做低侵入细粒度 profiling，把 operator、kernel 和请求级瓶颈关联起来。 |
| DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems | MLSys 2026 | OpenReview 公开稿未列单位 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更。 |
| Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference | MLSys 2026 | OpenReview 公开稿未列单位 | Charon 提供细粒度仿真来评估大规模 LLM 训练和推理的并行策略、硬件配置和系统优化。 |
| XProf: An Open, Scalable, and Extensible Profiling System for the Modern ML Stack | MLSys 2026 | MLSys 2026 官方页面未列单位 | XProf 为现代 ML stack 提供开放、可扩展的 profiling 系统，帮助把训练/推理瓶颈定位到框架、runtime、kernel 和硬件层。 |
| MLCommons Chakra: Advancing Performance Benchmarking and Co-design using Standardized Execution Traces | MLSys 2026 | MLSys 2026 官方页面未列单位 | Chakra 用标准化 execution traces 支撑 ML 系统 benchmark 和软硬件协同设计，让不同 simulator、runtime 和硬件方案可比较。 |
| Hawkeye: Reproducing GPU-Level Non-Determinism | MLSys 2026 | MLSys 2026 官方页面未列单位 | Hawkeye 聚焦复现 GPU 级非确定性，帮助定位并解释大模型训练/推理中难以复现的数值和执行差异。 |
| When Machine Learning Isn't Sure: Building Resilient ML-Based Computer Systems by Embracing Uncertainty | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作把不确定性作为 ML-based computer systems 的一等信号，用于构建更稳健的系统决策、监控和降级机制。 |
| Sparing Strategies to Minimize Reliability Impact On Large Training Jobs | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作研究大规模训练作业中的 spare 资源策略，在故障、降级和资源成本之间降低可靠性事件对作业进度的影响。 |
| OSWorld-Human: Benchmarking the Efficiency of Computer-Use Agents | MLSys 2026 | MLSys 2026 官方页面未列单位 | OSWorld-Human 用人类基线评测 computer-use agent 的效率，为桌面/浏览器 agent 系统的延迟、步骤数和成功率比较提供基准。 |
| Shannonic: Efficient Entropy-Optimal Compression for ML Workloads | MLSys 2026 | MLSys 2026 官方页面未列单位 | Shannonic 面向 ML workload 提供接近熵最优的高效压缩，用于降低训练/推理数据流、特征和中间状态的存储与传输成本。 |
| Toward Principled LLM Safety Testing: Solving the Jailbreak Oracle Problem | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作把 jailbreak oracle 问题形式化，改进 LLM 安全测试中自动判定、复现和系统化评测的可靠性。 |
| Reasoning Language Model Inference Serving Unveiled: An Empirical Study | ICLR 2026 Poster | OpenReview 公开稿未列单位 | 该实证研究刻画 reasoning LLM 在长输出、KV 增长和请求完成时间上的 serving 行为，为调度和容量规划提供基线。 |
| A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints | ICML 2026 | 作者公开稿未列单位 | 该工作把计算和 KV cache 显存同时纳入排队稳定性分析，给出 LLM inference 系统何时会因内存约束失稳的理论条件。 |

## AI 集群、向量数据库、安全与周边基础设施

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| PlanetServe: A Decentralized, Scalable, and Privacy-Preserving Overlay for Democratizing Large Language Model Serving | NSDI 2026 | UC Santa Cruz; University of Nevada, Reno | PlanetServe 用去中心化 overlay 聚合分散算力，并联合设计转发、隐私和服务质量验证。 |
| GFS: A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management | ASPLOS 2026 | Shanghai Jiao Tong University; Zhejiang University; Alibaba Group | GFS 预测 spot instance 风险并进行抢占感知调度，降低 GPU 集群中任务中断和资源浪费。 |
| Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters | SOSP 2025 | SOSP 2025 官方目录未列单位 | Sailor 自动选择并调整跨区域异构集群的并行和通信计划，其动态规划方法也适用于广域推理。 |
| Robust LLM Training Infrastructure at ByteDance | SOSP 2025 | ByteDance | 该工作总结字节跳动大模型基础设施中的故障检测、恢复、网络与作业治理经验。 |
| Astral: A Datacenter Infrastructure for Large Language Model Training at Scale | SIGCOMM 2025 | ByteDance 等 | Astral 从拓扑、流量控制和作业编排层构建超大规模 LLM 集群网络，为推理集群提供生产级网络设计参照。 |
| StreamBox: A Lightweight GPU SandBox for Serverless Inference Workflow | USENIX ATC 2024 | Huazhong University of Science and Technology; Inria | StreamBox 用 stream 级 sandbox、自动伸缩显存和跨 function GPU 通信降低 serverless inference 的启动与隔离开销。 |
| Milvus: A Purpose-Built Vector Data Management System | SIGMOD 2021 | Zilliz | Milvus 将索引、segment、计算节点和存储节点解耦，建立面向向量数据的分布式数据库架构。 |
| Manu: A Cloud Native Vector Database Management System | PVLDB 2022 | Zilliz | Manu 以 log-as-data、云原生组件和时间戳一致性支持弹性向量数据库服务。 |
| SPFresh: Incremental In-Place Update for Billion-Scale Vector Search | SOSP 2023 | Microsoft Research | SPFresh 以 LIRE 和增量原地更新维持动态向量索引，避免频繁全量重建。 |
| CAGRA: Highly Parallel Graph Construction and Approximate Nearest Neighbor Search for GPUs | ICDE 2024 | NVIDIA | CAGRA 以 GPU 并行图构建和搜索支撑高吞吐 ANN，并进入 RAPIDS cuVS 向量检索栈。 |
| Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Bifrost 将线性层密文卸载到加速器、把非线性与 KV 状态更新留在 CPU TEE 中，构建 TEE 加 FHE 的混合隐私推理路径。 |
| OTRO: Oblivious Tokenization Path with Square-Root ORAM | arXiv 预印本, 2026 | 作者公开稿未列单位 | OTRO 用 square-root ORAM 副本池、epoch 轮转和 KV-aware 重建重叠，把 tokenizer 侧信道防护开销压到接近生产可用。 |
| Image Prompt Reconstruction Attacks on Distributed MLLM Inference Frameworks | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作揭示分布式 MLLM 推理中间 embedding 可泄露图像提示，并通过黑盒重建攻击量化多模态推理框架的隐私风险。 |
| STREAM: Multi-Tier LLM Inference Middleware with Dual-Channel HPC Token Streaming | arXiv 预印本, 2026 | 作者公开稿未列单位 | STREAM 通过本地、HPC、云三层路由和控制面/数据面分离的 HPC token streaming，把高校 HPC 资源变成低时延推理后端。 |
| ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters | arXiv 预印本, 2026 | 作者公开稿未列单位 | ShuntServe 面向异构 spot GPU 集群联合做模型放置、负载分流和抢占恢复，以降低满足 SLO 的 serving 成本。 |
| Solyx AI Grid: Hardware-Telemetry-Aware Routing Across Geographically Distributed GPU Clusters | arXiv 预印本, 2026 | 作者公开稿未列单位 | Solyx AI Grid 用硬件遥测和地理分布信息做请求路由，把跨区域 GPU 集群组织成可调度的 LLM inference 后端。 |
| Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作分析 RAG 中非前缀 KV cache 的侧信道风险，展示 agent 辅助攻击可从 vLLM/LMCache 类复用路径恢复敏感上下文。 |
| NodeSweep: Practical Straggler Detection and Health Monitoring for Large-Scale Foundation Model Training | MLSys 2026 | MLSys 2026 官方页面未列单位 | NodeSweep 将在线性能监控与离线 node sweep 结合，识别传统 NCCL/burn-in 检查漏掉的慢节点，提升大规模基础模型训练集群稳定性。 |
| FlexTrain: Scalable Hybrid-Parallel Training with Elastic Resource Utilization and Consistent Accuracy | MLSys 2026 | MLSys 2026 官方页面未列单位 | FlexTrain 在共享 GPU 集群中动态调整 pipeline/data parallel 配置，优先保持训练确定性和精度一致，同时利用空闲资源加速 LLM 训练。 |
| FlexScale: Flexible and High-Performance FSDP at Scale | MLSys 2026 | MLSys 2026 官方页面未列单位 | FlexScale 面向大规模 FSDP 训练优化 shard、通信和资源组织，使 fully-sharded 训练在大集群中更灵活且高性能。 |
| NEST: Network- and Memory-Aware Device Placement for Distributed Deep Learning | MLSys 2026 | MLSys 2026 官方页面未列单位 | NEST 将网络和内存约束纳入 distributed DL device placement，减少跨设备通信和内存压力导致的训练/推理低效。 |
| ML Fleet Efficiency: Improving TPU Systems at Scale with ML Productivity Goodput | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工业系统工作用 ML productivity goodput 衡量 TPU fleet 效率，把集群利用率、作业有效进展和平台优化统一到生产指标中。 |
| GriNNder: Breaking the Memory Capacity Wall in Full-Graph GNN Training with Storage Offloading | MLSys 2026 | MLSys 2026 官方页面未列单位 | GriNNder 用 storage offloading 打破 full-graph GNN 训练的内存容量限制，为大图训练提供系统级扩展路径。 |
| FreeScale: Distributed Training for Sequence Recommendation Models with Minimal Scaling Cost | MLSys 2026 | MLSys 2026 官方页面未列单位 | FreeScale 面向序列推荐模型的分布式训练，降低扩展到多设备时的通信、同步和资源成本。 |
| BOOST: BOttleneck-Optimized Scalable Training Framework for Low-Rank Large Language Models | MLSys 2026 | MLSys 2026 官方页面未列单位 | BOOST 针对低秩大语言模型训练识别并优化瓶颈阶段，提高参数高效训练在大模型上的可扩展性。 |
| SAKURAONE: An Open Ethernet-Based AI HPC System and Its Observed Workload Dynamics in a Single-Tenant LLM Development Environment | MLSys 2026 | MLSys 2026 官方页面未列单位 | SAKURAONE 报告开放以太网 AI HPC 系统及单租户 LLM 开发环境中的 workload dynamics，为非专有互连大模型集群提供生产参照。 |
| AXLearn: Modular, Hardware-Agnostic Large Model Training | MLSys 2026 | MLSys 2026 官方页面未列单位 | AXLearn 提供模块化、硬件无关的大模型训练框架，统一不同硬件后端上的模型构建、训练和扩展流程。 |
| DreamDDP: Accelerating Low-Bandwidth Geo-Distributed LLM Training with Layer-wise Partial Synchronization | MLSys 2026 | MLSys 2026 官方页面未列单位 | DreamDDP 用 layer-wise partial synchronization 降低低带宽跨地域 LLM 训练中的同步压力，让广域闲置算力更可用。 |
| HexiScale: Facilitating Large Language Model Training over Heterogeneous Hardware | MLSys 2026 | MLSys 2026 官方页面未列单位 | HexiScale 面向异构硬件上的 LLM 训练，协调并行配置、性能差异和资源分配以提升混合集群可用性。 |
| Grolar: Efficient LLM Training on Heterogeneous Clusters | MLSys 2026 | MLSys 2026 官方页面未列单位 | Grolar 进一步面向异构集群优化 LLM 训练的任务放置和并行执行，减少慢设备拖累与资源碎片。 |
| Efficient Long-Context Language Model Training by Core Attention Disaggregation | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作将核心 attention 计算解耦来支撑长上下文训练，减少超长序列训练中的显存、通信和负载不均压力。 |
| ProTrain: Efficient LLM Training via Automatic Memory Management | MLSys 2026 | MLSys 2026 官方页面未列单位 | ProTrain 通过自动内存管理降低 LLM 训练中的显存规划与重算/offload 配置成本，提高大模型训练可部署性。 |
| MTraining: Distributed Dynamic Sparse Attention for Efficient Ultra-Long Context Training | MLSys 2026 | MLSys 2026 官方页面未列单位 | MTraining 为超长上下文 LLM 训练设计分布式动态稀疏 attention、平衡 ring attention 和层次通信，缓解 worker 与 step 级负载不均。 |
| Zero redundancy distributed learning with differential privacy | MLSys 2026 | MLSys 2026 官方页面未列单位 | DP-ZeRO 将 ZeRO 式零冗余分布式训练与差分隐私结合，扩大可训练私有模型规模并降低多 GPU DP 训练开销。 |
| HetRL: Efficient Reinforcement Learning for LLMs in Heterogeneous Environments | MLSys 2026 | MLSys 2026 官方页面未列单位 | HetRL 面向异构环境中的 LLM 强化学习训练，协调不同设备能力、rollout 负载和优化阶段以提高 RLHF/RLVR 系统效率。 |
| Unleashing Scalable Context Parallelism for Foundation Models Pre-Training via FCP | MLSys 2026 | MLSys 2026 官方页面未列单位 | FCP 为基础模型预训练释放可扩展 context parallelism，缓解超长序列训练中的 attention 通信和内存瓶颈。 |
| Massive-Scale Out-Of-Core UMAP on the GPU | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作在 GPU 上实现超大规模 out-of-core UMAP，为大规模 embedding 可视化、聚类和数据诊断提供系统基础。 |
| DisAgg: Distributed Aggregators for Efficient Secure Aggregation | MLSys 2026 | MLSys 2026 官方页面未列单位 | DisAgg 将 secure aggregation 的聚合器分布化，降低隐私分布式学习中的集中瓶颈和扩展成本。 |
| FLoRIST: Singular Value Thresholding for Efficient and Accurate Federated Fine-Tuning of Large Language Models | MLSys 2026 | MLSys 2026 官方页面未列单位 | FLoRIST 用奇异值阈值化降低联邦微调 LLM 的通信和本地计算成本，同时尽量保持参数高效更新精度。 |
| ProToken: Token-Level Attribution for Federated Large Language Models | MLSys 2026 | MLSys 2026 官方页面未列单位 | ProToken 面向 federated LLM 做 token-level attribution，帮助解释和诊断跨客户端数据对模型行为的贡献。 |
| PLayer-FL: A Principled Approach to Personalized Layer-wise Cross-Silo Federated Learning | MLSys 2026 | MLSys 2026 官方页面未列单位 | PLayer-FL 以层级个性化方式组织 cross-silo federated learning，减少不同机构数据异质性导致的训练低效。 |
| SONAR: Benchmarking Topology and Collaboration in Decentralized Learning | MLSys 2026 | MLSys 2026 官方页面未列单位 | SONAR 为 decentralized learning 提供拓扑和协作模式 benchmark，帮助比较不同去中心化训练系统的通信与收敛表现。 |
| Virtual Machine NUMA Placement at Scale: Learning the Norm, Shielding the Tail | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作用学习式策略做大规模 VM NUMA placement，降低尾部性能异常；其调度方法可迁移到共享 AI 集群资源放置。 |
| Cost-aware Duration Prediction for Software Upgrades in Datacenters | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作预测数据中心软件升级持续时间并纳入成本模型，服务于大规模 AI/云基础设施维护窗口和风险控制。 |
| ZK-APEX: ZERO-KNOWLEDGE APPROXIMATE PERSONALIZED UNLEARNING WITH EXECUTABLE PROOFS | MLSys 2026 | MLSys 2026 官方页面未列单位 | ZK-APEX 结合近似个性化 unlearning 与可执行零知识证明，为隐私敏感模型更新和删除请求提供可验证系统机制。 |
| CSLE: A Reinforcement Learning Platform for Autonomous Security Management | MLSys 2026 | MLSys 2026 官方页面未列单位 | CSLE 提供自治安全管理的强化学习平台，可用于评估 AI 基础设施中的自动防御、响应和策略学习。 |
| Blueprint, Bootstrap, and Bridge: A Security Look at NVIDIA GPU Confidential Computing | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作系统分析 NVIDIA GPU confidential computing 的安全边界、启动链和桥接机制，为隐私推理与受保护训练部署提供风险视角。 |
| Privatar: Scalable Privacy-preserving Multi-user VR via Secure Offloading | MLSys 2026 | MLSys 2026 官方页面未列单位 | Privatar 用 secure offloading 支撑多用户 VR 的隐私保护和可扩展执行，为低延迟隐私感知 ML/图形推理提供系统参考。 |
| G-HEMP: FAST MULTI-GPU PRIVATE INFERENCE FOR LARGE-SCALE GCNS WITH HOMOMORPHIC ENCRYPTION | MLSys 2026 | MLSys 2026 官方页面未列单位 | G-HEMP 将同态加密 private inference 扩展到多 GPU 大规模 GCN，展示隐私推理在图模型上的系统化加速路径。 |
| When Enough is Enough: Rank-Aware Early Termination for Vector Search | MLSys 2026 | MLSys 2026 官方页面未列单位 | 该工作用 rank-aware early termination 缩短向量搜索过程，在 RAG 检索和 ANN serving 中减少无效候选扫描。 |
| LEANN: A Low-Storage Overhead Vector Index | MLSys 2026 | MLSys 2026 官方页面未列单位 | LEANN 设计低存储开销向量索引，降低大规模 RAG/ANN 系统的内存与存储成本。 |
