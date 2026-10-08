# Benchmarking & Systems Analysis

Measuring real inference workloads, modeling system performance, validating simulations and diagnosing production incidents.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Accept methods with an explicit workload/evaluation model and validation; generic leaderboards do not qualify.

**Foundational context.** See also: [Serving systems](serving-systems.md) for workload-focused execution studies.

## Papers (20)

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [LLM-Inference-Bench: Inference Benchmarking of Large Language Models on AI Accelerators](https://ieeexplore.ieee.org/document/10820566) | SC24-W workshop 2024 | 提供硬件加速器推理吞吐和延迟评测方法；明确为 Workshop 而不是 SC 主会论文。 |
| 2024 | [LLMCompass: Enabling Efficient Hardware Design for Large Language Model Inference](https://ieeexplore.ieee.org/abstract/document/10609604) | ISCA 2024 | 映射搜索、硬件面积/成本模型及延迟预测联合评估 LLM 推理硬件设计，并与实测延迟对齐。 |
| 2024 | [LLMServingSim: A HW/SW Co-Simulation Infrastructure for LLM Inference Serving at Scale](https://doi.org/10.1109/IISWC63097.2024.00012) | IISWC 2024 | 构建 LLM 服务调度与硬件执行协同模拟，实现不同硬件/软件配置定量分析。 |
| 2024 | [The Importance of Workload Choice in Evaluating LLM Inference Systems](https://doi.org/10.1145/3642970.3655823) | EuroMLSys workshop 2024 | 系统比较输入/输出长度、请求到达过程等 Benchmark 设计对推理系统排名和判断的影响。 |
| 2024 | [Vidur: A Large-Scale Simulation Framework for LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/b74a8de47d2b3c928360e0a011f48351-Abstract-Conference.html) | MLSys 2024 | 基于算子 Profiling 与预测模型模拟 Batch/Parallelism/负载，使用真实推理数据校验仿真误差。 |
| 2025 | [Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/26289c647c6828e862e271ca3c490486-Abstract-Conference.html) | MLSys 2025 | 系统审视 KV Compression 的真实 GPU 服务端加速与任务质量，识别弱 Baseline 和不可信收益。 |
| 2026 | [Beyond the Buzz: A Pragmatic Take on Inference Disaggregation](https://proceedings.mlsys.org/paper_files/paper/2026/hash/d49cee5f3a79d97d719df255689d83d7-Abstract-Conference.html) | MLSys 2026 | 通过不同规模部署评估 P/D 分离的价值和资源、传输及调度边界。 |
| 2026 | [Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://proceedings.mlsys.org/paper_files/paper/2026/hash/29416b66c2149872b9d1415a3fd2c5e0-Abstract-Conference.html) | MLSys 2026 | 剖析 vLLM 冷启动的初始化、权重加载和图捕获关键路径。 |
| 2026 | [Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference](https://proceedings.mlsys.org/paper_files/paper/2026/hash/dbc8ce0fdfcd55172d73fb05dbae07fc-Abstract-Conference.html) | MLSys 2026 | 精细化推理性能模拟并用跨模型/配置与真实部署验证预测误差。 |
| 2026 | [Demystifying the Mixture of Experts Serving Tax](https://proceedings.mlsys.org/paper_files/paper/2026/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | MLSys 2026 | 将 MoE 的 Prefill/Decode 开销分解为可量化执行税项。 |
| 2026 | [Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch](https://proceedings.mlr.press/v306/zhang26ag.html) | ICML 2026 | 剖析不同 Tensor Parallel Size 的归约顺序并实现确定性推理。 |
| 2026 | [DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems](https://openreview.net/forum?id=Xfzzp6grRP) | MLSys 2026 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更 |
| 2026 | [FlashInfer-Bench: Building the Virtuous Cycle for AI-driven LLM Systems](https://proceedings.mlsys.org/paper_files/paper/2026/hash/37e44c4b5321605735be9761f9b758fc-Abstract-Conference.html) | MLSys 2026 | FlashInfer-Bench 构建了一套基准与反馈闭环，用于评测并迭代改进由 AI 驱动的 LLM 系统实现，形成“评测—优化”的良性循环 |
| 2026 | [ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler](https://openreview.net/forum?id=tYHWS7YPof) | MLSys 2026 | ProfInfer 使用 eBPF 在不修改或重编译 llama.cpp 的情况下，对 token、计算图、算子和硬件计数器进行多粒度追踪，提供 ProfDAG、ProfTime、ProfStat 视图，覆盖 dense、MoE routing 与 offloading |
| 2026 | [Reasoning Language Model Inference Serving Unveiled: An Empirical Study](https://iclr.cc/virtual/2026/poster/10011393) | ICLR 2026 | 该研究通过内存波动、掉队者与自适应运行时刻画推理模型 serving，并在真实负载下评估量化、KV 量化、speculative decoding 与前缀缓存 |
| 2026 | [Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression](https://proceedings.mlr.press/v306/liu26dz.html) | ICML 2026 | KVFundaBench 强调评估 KV 压缩对密集推理语义的真实影响。 |
| 2026 | [ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) | NSDI 2026 | 基于真实云服务 Trace 刻画多类型推理负载并合成代表性请求流。 |
| 2026 | [Speculative Decoding: Performance or Illusion?](https://proceedings.mlsys.org/paper_files/paper/2026/hash/554e056fe2b6d9fd27ffcd3367ae1267-Abstract-Conference.html) | MLSys 2026 | 在现实 vLLM Batch/负载下复测多类推测解码，并对比理论上限。 |
| 2026 | [StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference (Operational Systems)](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) | OSDI 2026 | 按关键同步点和异常触发跟踪降低生产推理诊断开销，结合关键路径与 Roofline 回归定位故障。 |
| 2026 | [The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective](https://2026.hpca-conf.org/details/hpca-2026-main-conference/17/The-Cost-of-Dynamic-Reasoning-Demystifying-AI-Agents-and-Test-Time-Scaling-from-an-A) | HPCA 2026 | 对 Agent/Test-Time Scaling 的计算、能耗与设备性能进行系统性测量。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
