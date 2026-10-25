# Benchmarking & Systems Analysis

**Start with the engineering bottleneck, then pick papers.** 要评估推理系统：缺负载、可靠测量、性能定位、预测模型、正确性检查，还是 Kernel Benchmark？

[← Topics](README.md) · [← Home](../README.md)

**Engineering references:** [vLLM bench](https://docs.vllm.ai/en/latest/cli/bench/) · [SGLang benchmark guide](https://docs.sglang.io/docs/developer_guide/bench_serving) · [MLPerf Inference](https://mlcommons.org/benchmarks/inference-datacenter/).

**Foundational context.** [Serving systems](serving-systems.md) holds the workload-focused execution studies; [Orca, Sarathi-Serve, DistServe, Splitwise and Mooncake](../README.md#foundational-and-influential-papers) are homepage serving foundations, **not duplicate canonical rows** here.

## Research directions (6)

这些是可直接立项/实现/Benchmark 的**方向**，不是严密的学术分类。论文按主要优化对象只出现一次；不同方向的论文也可以互为 Related Work。

| Direction | Papers | What to work on |
|---|---:|---|
| [Serving Benchmarks & Workloads](#serving-benchmarks--workloads-14) | 14 | Benchmark 定义、真实 Trace、Agent/多模态负载。 |
| [Performance & Efficiency Studies](#performance--efficiency-studies-15) | 15 | 端到端吞吐、尾延迟、能耗以及优化技术的独立评估。 |
| [Profiling & Diagnosis](#profiling--diagnosis-5) | 5 | 性能分析器、Tracing、可观测性和异常定位。 |
| [Models & Simulators](#models--simulators-11) | 11 | 性能建模、容量估计、仿真和边界分析。 |
| [Correctness & Reliability](#correctness--reliability-9) | 9 | 输出一致性、运行时 Bug、可靠性及数值语义检查。 |
| [Kernel Benchmarks](#kernel-benchmarks-5) | 5 | 单算子评测与自动生成 Kernel 的 Correctness/Speed 验收。 |
| **Total** | **59** | |

## Papers (59)

### Serving Benchmarks & Workloads (14)

Benchmark 定义、真实 Trace、Agent/多模态负载。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [LLM-Inference-Bench: Inference Benchmarking of Large Language Models on AI Accelerators](https://ieeexplore.ieee.org/document/10820566) | SC24-W workshop 2024 | 提供硬件加速器推理吞吐和延迟评测方法；明确为 Workshop 而不是 SC 主会论文。 |
| 2024 | [The Importance of Workload Choice in Evaluating LLM Inference Systems](https://doi.org/10.1145/3642970.3655823) | EuroMLSys workshop 2024 | 系统比较输入/输出长度、请求到达过程等 Benchmark 设计对推理系统排名和判断的影响。 |
| 2025 | [BurstGPT: A Real-World Workload Dataset to Optimize LLM Serving Systems](https://doi.org/10.1145/3711896.3737413) | KDD 2025 | 基于云端 LLM 请求日志发布 Bursty Traffic/长度/失败 Trace，并在真实负载特征下评估 Serving 调度与缓存设计。 |
| 2025 | [KVCache Cache in the Wild: Characterizing and Optimizing KVCache Cache at a Large Cloud Provider](https://www.usenix.org/conference/atc25/presentation/wang-jiahao) | USENIX ATC 2025 | 基于云厂商真实请求 Trace 刻画跨轮/单轮 KV 命中、复用时间和容量需求，评估工作负载感知的缓存决策。 |
| 2025 | [On Evaluating Performance of LLM Inference Serving Systems](https://arxiv.org/abs/2507.09019) | arXiv 2025 (preprint) | 系统分析 Baseline Fairness、工作负载设置与 Serving Metric 设计的测量反模式，通过 Speculative Decoding Case Study 展示评估混淆及可复用核验清单。 |
| 2025 | [Towards Efficient Large Multimodal Model Serving](https://arxiv.org/abs/2502.00937) | arXiv 2025 (preprint) | 对真实多模态服务 Trace 和六类模型进行分阶段 Profiling，评估编码/Prefill/Decode 解耦及资源分配的 SLO 影响（KEEP_ADJACENT）。 |
| 2026 | [Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study](https://arxiv.org/abs/2603.10031) | arXiv 2026 (preprint) | 在 MI325X 上统一对比 MLA、GQA、MoE 与多模态模型，量化 AITER 内核、KV offload 与 block size 等配置对吞吐与延迟的影响，指出部署参数须按架构选择。 |
| 2026 | [Benchmarking and Characterization of Large Language Model Inference on Apple Silicon](https://doi.org/10.1145/3771563) | PACM/POMACS 2025 (SIGMETRICS 2026) | 用延迟/吞吐对比与 ALU 利用率、内存带宽、cache 驻留等底层指标剖析，比较 Apple Silicon 统一内存与 NVIDIA GPU 的端侧 LLM 推理；在 M 系列与 RTX A6000 上覆盖 8B–405B、14 种量化方案。 （正式 POMACS 9(3), Article 48, 26 页；五个真实硬件平台、8B–405B 和 14 种量化格式。） |
| 2026 | [Characterizing Cloud-Native LLM Inference at ByteDance and Exposing Optimization Challenges and Opportunities for Future AI Accelerators](https://doi.org/10.1109/HPCA68181.2026.11408526) | HPCA 2026 (Industry Track) | 以 Doubao 生产负载与跨 Instruction/Kernel/Model 多级评估刻画异构 LLM 推理瓶颈及硬件选型边界。 |
| 2026 | [Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://proceedings.mlr.press/v306/zhou26e.html) | ICML 2026 | 在 GPU/NPU 等异构设备上实测 VLA Backbone 与 Action Expert 的不同 Roofline/资源瓶颈，以 DP-Cache 和异步 V-AE Pipeline 优化控制延迟与能效（邻接 Embodied Inference）（KEEP_ADJACENT）。 |
| 2026 | [From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems](https://arxiv.org/abs/2608.15127) | arXiv 2026 (preprint; AgentSysBench) | 用十类 Agent 应用、受控部署与真实 Trace 分离 GPU Inference、CPU Sandbox、Retrieval 和持久会话的系统成本，提供任务感知调度、状态卸载等可执行设计探索；未经独立复现。 |
| 2026 | [Reasoning Language Model Inference Serving Unveiled: An Empirical Study](https://iclr.cc/virtual/2026/poster/10011393) | ICLR 2026 | 该研究通过内存波动、掉队者与自适应运行时刻画推理模型 serving，并在真实负载下评估量化、KV 量化、speculative decoding 与前缀缓存 |
| 2026 | [ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) | NSDI 2026 | 基于真实云服务 Trace 刻画多类型推理负载并合成代表性请求流。 |
| 2026 | [The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective](https://2026.hpca-conf.org/details/hpca-2026-main-conference/17/The-Cost-of-Dynamic-Reasoning-Demystifying-AI-Agents-and-Test-Time-Scaling-from-an-A) | HPCA 2026 | 对 Agent/Test-Time Scaling 的计算、能耗与设备性能进行系统性测量。 |

### Performance & Efficiency Studies (15)

端到端吞吐、尾延迟、能耗以及优化技术的独立评估。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/26289c647c6828e862e271ca3c490486-Abstract-Conference.html) | MLSys 2025 | 系统审视 KV Compression 的真实 GPU 服务端加速与任务质量，识别弱 Baseline 和不可信收益。 |
| 2026 | [Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy](https://arxiv.org/abs/2606.09080) | arXiv 2026 (preprint) | 以 GEMM 维度为核心重组 LLM 剪枝设计空间，统一比较结构化与非结构化剪枝族在真实内核与硬件上取得的端到端加速，而非理论 FLOPs 收益。 |
| 2026 | [Beyond the Buzz: A Pragmatic Take on Inference Disaggregation](https://proceedings.mlsys.org/paper_files/paper/2026/hash/d49cee5f3a79d97d719df255689d83d7-Abstract-Conference.html) | MLSys 2026 | 通过不同规模部署评估 P/D 分离的价值和资源、传输及调度边界。 |
| 2026 | [Beyond Throughput: Performance and Energy Insights of LLM Inference Across AI Accelerators](https://doi.org/10.1109/IPDPS65963.2026.00083) | IPDPS 2026 | 真实物理加速器比较：六款 NVIDIA/AMD/Intel GPU 及两类 Cerebras/SambaNova Dataflow Accelerator、14 个开源模型，测量 Prefill/Decode、Batch/并行度、能耗 Pareto；作者公开 vLLM/功耗脚本（异构厂商依赖仍需注意）。 |
| 2026 | [Characterizing Parallelism Strategies in LLM Inference: Fundamental Compute-Communication Trade-offs](https://arxiv.org/abs/2610.05305) | arXiv 2026 (preprint) | 解析 TP/PP/Hybrid 的 Collective、点对点通信与 Pipeline Bubble，比较 Prefill/Decode 不同瓶颈。 |
| 2026 | [Characterizing Performance-Energy Trade-offs of Large Language Models in Multi-Request Workflows](https://doi.org/10.1145/3801489.3806907) | PACM/POMACS 2026 (SIGMETRICS Abstract) | 在 NVIDIA A100 上用 vLLM 与 Parrot 对顺序、交互、agentic 与复合四类多请求工作负载做性能-能耗刻画，量化 batch size、GPU power cap 与输出长度对延迟、吞吐及 CPU/GPU/DRAM 能耗的影响。 （另有 POMACS 10(1) 长文与 SIGMETRICS 三页摘要；作者在真实 A100 + vLLM/Parrot 比较多请求 Workflows。） |
| 2026 | [Demystifying the Mixture of Experts Serving Tax](https://proceedings.mlsys.org/paper_files/paper/2026/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | MLSys 2026 | 将 MoE 的 Prefill/Decode 开销分解为可量化执行税项。 |
| 2026 | [Performance Characterization and Optimization of LLM Inference on Tenstorrent AI Accelerators](https://doi.org/10.1007/978-3-032-35251-4_32) | Euro-Par 2026 (Springer LNCS imprint 2027) | 真实 Tenstorrent Wormhole 的 Tensix Decode 剖析与 Chip-Pipe 跨芯片 Pipeline Parallel 调度；作者报告 Llama-3.1-8B 等四模型相对 TP 吞吐改善，需保留芯片专用编程与实验范围；会议于 2026 年举行、Springer 正式书卷标记 2027 出版。 |
| 2026 | [Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling](https://openreview.net/forum?id=DjOmnwX4wJ) | ICLR 2026 | 标准化比较 Best-of-N/多轮推理中的模型型、训练型与 N-Gram Speculative Decoding，对重复推理轨迹的加速边界做实证研究；Benchmark 而非新 Runtime Scheduler。 |
| 2026 | [Speculative Decoding: Performance or Illusion?](https://proceedings.mlsys.org/paper_files/paper/2026/hash/554e056fe2b6d9fd27ffcd3367ae1267-Abstract-Conference.html) | MLSys 2026 | 在现实 vLLM Batch/负载下复测多类推测解码，并对比理论上限。 |
| 2026 | [SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://proceedings.mlr.press/v306/abramovich26a.html) | ICML 2026 | 在 vLLM/TensorRT-LLM 的真实 Batch/吞吐负载下量化 Speculative Decoding 对数据分布和 Draft 长度的敏感性。 |
| 2026 | [TokenPowerBench: Benchmarking the Power Consumption of LLM Inference](https://doi.org/10.1609/aaai.v40i38.40535) | AAAI 2026 (Full Paper) | 多层级 GPU/Node/System 能耗测量与请求级 Prefill/Decode Phase Attribution，覆盖四种模型系列及 Batch/Context/Parallelism/Quantization 的 J/token 对比；作者发布基准。测量校准、传感器精度和 Serving QoS/能效 Pareto 前沿待审。 **复审证据：**[AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40535) + [作者 Harness](https://github.com/chenxuniu/TokenPowerBench)，NVML/RAPL/IPMI 分级归因；分布式 GPU 实际验证尚未完成，GPU 能量≠节点总能量。 （KEEP_SOURCE_VERIFIED; AUTHOR_REPORTED; NOT_INDEPENDENTLY_REPRODUCED） |
| 2026 | [Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles](https://doi.org/10.1109/ISCA66397.2026.00084) | ISCA 2026 (Industry Track) | 在真实 GPU Cluster 上刻画 8B–671B 推理的 DP/TP/PP、长 CoT KV 容量陷阱与 MoE 同步瓶颈；提供部署权衡测量而非单一加速算法。 |
| 2026 | [When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference](https://arxiv.org/abs/2605.27435) | arXiv 2026 (preprint) | 按阶段分离移动端 LLM 推理的量化、通信与计算开销，定位 NPU 在 prefill/decode 中因算子 fallback 与调度开销反而慢于 CPU 的条件。 |
| 2026 | [Understanding Bottlenecks for Efficiently Serving LLM Inference With KV Offloading](https://arxiv.org/abs/2601.19910) | arXiv 2026 (preprint) | 系统拆解 KV offload 服务链路的瓶颈归属：分别量化 PCIe 传输、KV 重建与注意力计算的时间占比，指出传输与重建的重叠不足而非带宽本身构成主要损失，并据此给出预取与调度层面的优化空间。 |

### Profiling & Diagnosis (5)

性能分析器、Tracing、可观测性和异常定位。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://proceedings.mlsys.org/paper_files/paper/2026/hash/29416b66c2149872b9d1415a3fd2c5e0-Abstract-Conference.html) | MLSys 2026 | 剖析 vLLM 冷启动的初始化、权重加载和图捕获关键路径。 |
| 2026 | [ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler](https://openreview.net/forum?id=tYHWS7YPof) | MLSys 2026 | ProfInfer 使用 eBPF 在不修改或重编译 llama.cpp 的情况下，对 token、计算图、算子和硬件计数器进行多粒度追踪，提供 ProfDAG、ProfTime、ProfStat 视图，覆盖 dense、MoE routing 与 offloading |
| 2026 | [StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference (Operational Systems)](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) | OSDI 2026 | 按关键同步点和异常触发跟踪降低生产推理诊断开销，结合关键路径与 Roofline 回归定位故障。 |
| 2026 | [XProf: An Open, Scalable, and Extensible Profiling System for the Modern ML Stack](https://proceedings.mlsys.org/paper_files/paper/2026/hash/280776fda5970060e6a5efcfd43e5d2d-Abstract-Conference.html) | MLSys 2026 | OpenXLA/PJRT Full-stack CPU–TPU/GPU Profiling、Roofline 与跨千卡低开销分布式 Trace；开源生产级性能分析基础设施，但不是 LLM Serving 专用评测（KEEP_ADJACENT）。 |
| 2026 | [ProMCP: Profiling Token Flows and Latency Costs in Model Context Protocol–Based LLM Agents](https://aclanthology.org/2026.findings-acl.1967/) | ACL Findings 2026 (NOT ACL Main) | 对 LLM Agent **MCP Host–Client–Server** 端到端六阶段执行做请求级 Token/Latency Attribution，公开 [代码](https://github.com/ResponsibleAILab/ProMCP)；作者在 20 Servers / 169 Tools、不同部署 Topology 上表明 Planning/Schema Injection vs Generation 的主要瓶颈随 Client 形态变化。**属于 Agent Workflow Profiling，不是 GPU/NPU Kernel Profiler，也不证明 Token/s 加速**。（KEEP_ADJACENT; REAL_WORKFLOW_PROFILING; PUBLIC_CODE; AUTHOR_REPORTED） |

### Models & Simulators (11)

性能建模、容量估计、仿真和边界分析。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [Simulate Before You Scale: High-Fidelity LLM Inference Planning Without GPUs (BLIS)](https://arxiv.org/abs/2610.14255) | ACM SIGMETRICS 2027 accepted / arXiv 2026 (DOI:10.1145/3857382; final proceedings pending) | **Deterministic CPU Serving Simulator** 建模 Admission、llm-d Routing、Batching、KV/Preemption 与 P/D；36 组 **6 模型 × 3 GPU** 对真实 vLLM/llm-d 配置中位 E2E 误差 **6.7%**（作者报告），两项模拟器发现的策略在真实 GPU 验证，不能把其余配置扫描当实机实验。开源 [Simulator + Latency Kernel/Catalog](https://github.com/inference-sim/inference-sim)，llm-d Policy Merge 尚待具体 PR 核实。（KEEP_STRICT; REAL_GPU_VALIDATION; PUBLIC_SIM; AUTHOR_REPORTED） |
| 2024 | [LLMCompass: Enabling Efficient Hardware Design for Large Language Model Inference](https://ieeexplore.ieee.org/abstract/document/10609604) | ISCA 2024 | 映射搜索、硬件面积/成本模型及延迟预测联合评估 LLM 推理硬件设计，并与实测延迟对齐。 |
| 2024 | [LLMServingSim: A HW/SW Co-Simulation Infrastructure for LLM Inference Serving at Scale](https://doi.org/10.1109/IISWC63097.2024.00012) | IISWC 2024 | 构建 LLM 服务调度与硬件执行协同模拟，实现不同硬件/软件配置定量分析。 |
| 2024 | [Vidur: A Large-Scale Simulation Framework for LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/b74a8de47d2b3c928360e0a011f48351-Abstract-Conference.html) | MLSys 2024 | 基于算子 Profiling 与预测模型模拟 Batch/Parallelism/负载，使用真实推理数据校验仿真误差。 |
| 2025 | [TokenSim: Enabling Hardware and Software Exploration for Large Language Model Inference Systems](https://arxiv.org/abs/2503.08415) | arXiv 2025 (preprint) | 面向 LLM 推理的软硬件协同探索模拟器：把调度策略与显存管理建模为可扩展模块，支持在设计阶段替换不同调度/内存方案；对真实系统校验误差低于 1%，用于部署前评估新调度与显存管理的收益。 （KEEP_ADJACENT；作者报告真实推理负载校准的模拟误差小于 1%，非全形状/硬件通用保证。） |
| 2026 | [A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints](https://proceedings.mlr.press/v306/nie26a.html) | ICML 2026 | 在队列稳定性模型中同时引入 GPU 计算和 KV 内存约束，推导稳定到达率/容量界，并在真实 GPU Serving 环境核验预测误差和 Provisioning 边界。 |
| 2026 | [Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference](https://proceedings.mlsys.org/paper_files/paper/2026/hash/dbc8ce0fdfcd55172d73fb05dbae07fc-Abstract-Conference.html) | MLSys 2026 | 精细化推理性能模拟并用跨模型/配置与真实部署验证预测误差。 |
| 2026 | [GPU-Tile-Sim: A Tile-Centric GPU Simulation Framework for LLM Hardware-Software Co-Design](https://arxiv.org/abs/2607.11262) | MICRO 2026 | 以 warp 级 tile graph（节点为 tile 算子、边为依赖）驱动 GPU 模拟，用于 LLM 软硬件协同设计；在 H100 上用 8 个 GEMM 与 6 个 FA3 用例验证，报告 MAPE 与相关性。 （KEEP_ADJACENT；模拟器结果有 A100/H100 校准；公开 v0.1.0 Artifact 仅覆盖部分前端与算例，不是完整论文所有特性。） （模拟器研究本身有效，A100/H100 物理校准不等于模型/性能功能均已实物实现。） |
| 2026 | [How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving](https://arxiv.org/abs/2605.28302) | arXiv 2026 (preprint) | 以实测 Kernel 与网络仿真对比聚合、P/D 与 AFD，在多工作负载和 SLO 下刻画拆分收益边界。 |
| 2026 | [LLMServingSim 2.0: A Unified Simulator for Heterogeneous and Disaggregated LLM Serving Infrastructure](https://arxiv.org/abs/2602.23036) | arXiv 2026 (preprint) | 把调度、路由、Offload、功率与互联行为置于统一 Runtime Loop，并对真实部署指标校准。 |
| 2026 | [AIConfigurator: Lightning-Fast Configuration Optimization for Multi-Framework LLM Serving](https://arxiv.org/abs/2601.06288) | arXiv 2026 (preprint; open-source) | 用实测 **GEMM/Attention/Collective/MoE Op Perf DB + Engine-aware Iteration Model** 自动枚举 TP/DP/EP、Batch、P/D 配置，不依赖每个配置现场 Benchmark。作者在 **8×H100/H200、TRT-LLM/vLLM/Dynamo** 实机验证；真实 H200 Case 选出的 P/D 配置相比最优 Aggregated **648.3 vs 321.5 tokens/s/GPU**，但这是**不同部署拓扑方案的差异**，不是预测器自身的独立 2× 加速。总吞吐建模平均误差最高报告 25.49% 的评估组；[AIConfigurator](https://github.com/ai-dynamo/aiconfigurator) 已标记迁移至 AI Simulate，工具不保证配置真实最优。(KEEP_STRICT; REAL_GPU_VALIDATED_MODEL; OPEN_SOURCE; VERSION_SENSITIVE) |

### Correctness & Reliability (9)

输出一致性、运行时 Bug、可靠性及数值语义检查。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse](https://arxiv.org/abs/2610.13060) | arXiv 2026 (preprint) | [vLLM Testbed](https://github.com/taiga333/eval-kv-repurpose) 将非 Prefix 文档 Segment 复用与 Workload/Capacity/Cache-Aware Scheduling 结合，固定 **30GB/Zipf RAG** 报告 Token Hit Rate **63.9% vs Prefix 3.3%** 并缩短 TTFT；但非前缀复用破坏因果状态，**跨文档推理质量显著失效**，不能视作无损优化。作为可复现的语义正确性反例而非普适加速方法收录。（KEEP_STRICT; REAL_GPU_AUTHOR_ONLY; APPROXIMATE_QUALITY_REGRESSION; PUBLIC_CODE） |
| 2026 | [A First Look at Bugs in LLM Inference Engines](https://doi.org/10.1145/3788873) | ACM TOSEM 2026 | 对 llama.cpp、vLLM、DeepSpeed、MLC-LLM、TensorRT-LLM 的 929 个真实 Bug 手工标注，归纳六类症状、28 类根因并开放缺陷数据集，指导运行时故障定位。 |
| 2026 | [Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch](https://proceedings.mlr.press/v306/zhang26ag.html) | ICML 2026 | 剖析不同 Tensor Parallel Size 的归约顺序并实现确定性推理。 |
| 2026 | [DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems](https://openreview.net/forum?id=Xfzzp6grRP) | MLSys 2026 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更 |
| 2026 | [Hawkeye: Reproducing GPU-Level Non-Determinism](https://mlsys.org/virtual/2026/poster/3606) | MLSys 2026 | 构造针对 Tensor Core 的定向测试，反推舍入方向、次正规数处理与累加顺序，在 CPU 上逐位复现 GPU 矩阵乘；在 Ampere、Hopper、Lovelace 上以 FP16/BF16/FP8 验证。 |
| 2026 | [Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression](https://proceedings.mlr.press/v306/liu26dz.html) | ICML 2026 | KVFundaBench 强调评估 KV 压缩对密集推理语义的真实影响。 **复审证据：**[ICML 2026](https://proceedings.mlr.press/v306/liu26dz.html)：KVFundaBench 衡量 CoT 语义链对压缩的脆弱性，ShotKV 作者报告同条件某场景 −11% Latency；作为质量反例/评测标准，不当作全负载加速。 （KEEP_SOURCE_VERIFIED; AUTHOR_REPORTED; NOT_INDEPENDENTLY_REPRODUCED） |
| 2026 | [The Pitfalls of KV Cache Compression](https://aclanthology.org/2026.acl-long.1926/) | ACL 2026 | 实证审计 StreamingLLM/SnapKV/TOVA/H2O/K-Norm 在复杂多指令 Prompt 上的 KV 驱逐语义损失与指令忽略/系统 Prompt 泄露；是部署质量风险评测而非新增 GPU 加速算法。 **复审证据：**[ACL 2026](https://aclanthology.org/2026.acl-long.1926/)：5 种 KV 压缩、Llama3.1/Qwen2.5 + IFEval 多指令，实证指令忽略及系统 Prompt Leakage；是质量/安全反例，不是新 GPU 加速。 （KEEP_SOURCE_VERIFIED; AUTHOR_REPORTED; NOT_INDEPENDENTLY_REPRODUCED） |
| 2026 | [When KV Cache Reuse Fails in Multi-Agent Systems: Cross-Candidate Interaction is Crucial for LLM Judges](https://aclanthology.org/2026.acl-long.327/) | ACL 2026 (Long Paper) | 在 GSM8K、MMLU、HumanEval 的 Multi-Agent Judge 场景，以 Dense Prefill 为参考测量 KV 复用导致的 Judge Consistency Rate (JCR) 下降；包含 KVCOMM 对照与复现实验代码。属于 KV 复用正确性反例研究，论文明确不宣称系统级 TTFT/吞吐改进；G3/G5 仍待复审。 **复审证据：**[ACL 2026](https://aclanthology.org/2026.acl-long.327/)：多 Agent Judge 的 KV reuse vs Dense-prefill 控制组，GSM8K/MMLU/HumanEval 的 Judge Consistency 下降；原目录指出有作者代码，属于 correctness 反例，非性能优化。 （KEEP_SOURCE_VERIFIED; AUTHOR_REPORTED; NOT_INDEPENDENTLY_REPRODUCED） |
| 2026 | [Bit-Accurate Modeling of GPU Matrix Multiply-Accumulate Units: Demystifying Numerical Discrepancy and Accuracy](https://arxiv.org/abs/2511.10909) | MICRO 2026 | 提出闭环特征探测 CLFP，把 MMA 指令当黑盒反复探测以反推其内部浮点运算行为，为 Volta 到 RTX Blackwell 等十种 GPU 架构建立首个位精确 MMA 算术模型，并定位四类精度瓶颈与一类数值不对称。 |

### Kernel Benchmarks (5)

单算子评测与自动生成 Kernel 的 Correctness/Speed 验收。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [KernelBench: Can LLMs Write Efficient GPU Kernels?](https://proceedings.mlr.press/v267/ouyang25a.html) | ICML 2025 | 奠基性 Kernel Generation 测试环境：250 个 PyTorch ML Workload、正确性加速联合指标 fast_p，并考察迭代 Profiling Feedback；是通用 Kernel 评测前提，不是 LLM Serving 端到端 Benchmark（KEEP_FOUNDATIONAL）。 |
| 2026 | [FlashInfer-Bench: Building the Virtuous Cycle for AI-driven LLM Systems](https://proceedings.mlsys.org/paper_files/paper/2026/hash/37e44c4b5321605735be9761f9b758fc-Abstract-Conference.html) | MLSys 2026 | FlashInfer-Bench 构建了一套基准与反馈闭环，用于评测并迭代改进由 AI 驱动的 LLM 系统实现，形成“评测—优化”的良性循环 |
| 2026 | [KernelCraft: Benchmarking for Agentic Close-to-Metal Kernel Generation on Emerging Hardware](https://proceedings.mlr.press/v306/nie26c.html) | ICML 2026 | 面向新兴 NPU ISA 的 Agentic Kernel 编译、正确性反馈与性能评测；涵盖真实 AMD NPU、PLENA 模拟器与 Verilator RTL，基准代码的公开状态需复核，不是生产 Serving 加速。 |
| 2026 | [TritonGym: A Benchmark for Agentic LLM Workflows in Triton GPU Code Generation](https://proceedings.mlr.press/v306/guan26d.html) | ICML 2026 | 以可复现的工具调用/编译/正确性与速度反馈环境评估多轮 Triton Kernel Agent，覆盖 OOD 与扩展 DSL；是真实 Kernel 执行 Benchmark，不等于 LLM Serving Speedup。 |
| 2026 | [AscendKernelGen: LLM-Driven Kernel Generation for NPUs](https://aclanthology.org/2026.findings-acl.1533/) | ACL Findings 2026 (NOT ACL Main) | Ascend-CoT/KernelGen-LM 和 [NPUKernelBench](https://github.com/weich97/NPUKernelBench)：真实 AscendC Kernel 编译、PyTorch Reference Precision Oracle、性能测量；官方报告 Complex Level-2 Pass@10 Compile 95.5%、Functional Correctness 64%，**不是 LLM Serving 端到端加速**。Bench 与作者训练方案耦合，须防单固定 Shape Overfit；作为 Ascend Agentic Kernel 测评参考。（KEEP_ADJACENT; PUBLIC_BENCH; REAL_NPU_AUTHOR_REPORTED） |

*Paper links, venue, and mechanism notes are preserved from the prior curation. Inline HOLD/KEEP labels are review notes, not G0–G5 acceptance verdicts. Reported speedups are not independently reproduced.*
