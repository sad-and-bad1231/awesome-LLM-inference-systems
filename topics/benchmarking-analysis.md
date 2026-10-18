# Benchmarking & Systems Analysis

Measuring real inference workloads, modeling system performance, validating simulations and diagnosing production incidents — from benchmark suites and traces to profiling, simulation and correctness audits. **The decisive reusable mechanism determines the subsection**: a measurement, modelling or analysis contribution, not the optimized technique it happens to measure.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Accept papers whose decisive contribution is *measurement, modelling or analysis* of LLM inference systems: benchmark suites and measurement methodology, production traces and workload characterisation, real-system performance/energy characterisation, profiling and production diagnosis, performance models and simulators, and reliability/correctness/semantic-integrity studies. Papers whose decisive mechanism is an optimization (kernel, KV, scheduling, parallelism) belong to their other canonical topic even when they contain strong measurements; model-quality leaderboards with no inference-execution measurement do not qualify.

**Foundational context.** [Serving systems](serving-systems.md) holds the workload-focused execution studies; [Orca, Sarathi-Serve, DistServe, Splitwise and Mooncake](../README.md#foundational-and-influential-papers) are homepage serving foundations, **not duplicate canonical rows** here.

## Mechanism map

Nine internal groups, **49 canonical entries in total**. Subsections are a reading/navigation structure, **not nine new public categories** and not G0–G5 admission verdicts.

| Research mechanism | Papers |
|---|---:|
| [Serving Benchmark Suites and Measurement Methodology](#serving-benchmark-suites-and-measurement-methodology-3) | 3 |
| [Acceleration-Technique Audits under Realistic Serving](#acceleration-technique-audits-under-realistic-serving-7) | 7 |
| [Production Traces and Workload Characterisation](#production-traces-and-workload-characterisation-5) | 5 |
| [Real-System Performance, Scaling and Energy Characterisation](#real-system-performance-scaling-and-energy-characterisation-7) | 7 |
| [Profiling, Diagnosis and Observability](#profiling-diagnosis-and-observability-4) | 4 |
| [Performance Modelling, Analytical Bounds and Simulators](#performance-modelling-analytical-bounds-and-simulators-8) | 8 |
| [Reliability, Correctness and Semantic Integrity](#reliability-correctness-and-semantic-integrity-7) | 7 |
| [Kernel and Agentic-Kernel Benchmarking](#kernel-and-agentic-kernel-benchmarking-4) | 4 |
| [Agentic, Session-Level and Multimodal Workloads](#agentic-session-level-and-multimodal-workloads-4) | 4 |
| **Total** | **49** |

### Where this taxonomy came from

The structure is cross-checked against how production teams actually measure and diagnose inference, not derived from conference session labels:

- **MLPerf Inference (MLCommons):** the [Datacenter](https://mlcommons.org/benchmarks/inference-datacenter/) and [Edge](https://mlcommons.org/benchmarks/inference-edge/) suites define scenario + metric rules, closed/open divisions, availability categories and wall-power measurement, with the [MLPerf Inference paper](https://arxiv.org/abs/1911.02549) as the methodology anchor; v6.1 extends coverage toward RAG, agentic and [API-based serving](https://mlcommons.org/2026/07/agentic-inference-for-mlperf-inference/), and [MLPerf Endpoints](https://mlcommons.org/2026/10/mlperf-endpoints-matters-to-buyers/) adds server/endpoint scenarios — which is why benchmark *methodology* and *agentic/endpoint workloads* are separate groups here.
- **vLLM bench suite:** [`vllm bench serve/latency/throughput`](https://docs.vllm.ai/en/latest/cli/bench/) plus the [`vllm.benchmarks` API](https://docs.vllm.ai/en/latest/api/vllm/benchmarks/) standardize TTFT/TPOT/ITL and request-rate/arrival methodology, while the official [inference-sim](https://github.com/inference-sim/inference-sim) and [Vidur](https://pypi.org/project/vidur/) anchor the separate simulator boundary.
- **SGLang:** [Bench Serving Guide](https://docs.sglang.io/docs/developer_guide/bench_serving) and [Benchmark and Profiling](https://docs.sglang.io/docs/developer_guide/benchmark_and_profiling) define the server-level load-generator + dataset protocol used as the reference for the serving-benchmark group.
- **NVIDIA serving measurement stack:** [GenAI-Perf](https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2520/user-guide/docs/perf_analyzer/genai-perf/README.html), [NIM LLM benchmarking](https://docs.nvidia.com/nim/benchmarking/llm/latest/overview.html) and [TensorRT-LLM benchmarking guidance](https://developer.nvidia.com/blog/llm-inference-benchmarking-performance-tuning-with-tensorrt-llm/) show the same metric vocabulary (TTFT, ITL/TPOT, request throughput, concurrency sweep) applied per-model, per-accelerator.
- **LLMPerf:** [ray-project/llmperf](https://github.com/ray-project/llmperf) keeps a deliberately minimal *load test + correctness test* pairing for API-level serving, motivating the split between benchmark methodology and correctness/reliability groups.
- **Production traces and workload generators:** [AzurePublicDataset](https://github.com/Azure/AzurePublicDataset), BurstGPT (KDD 2025) and ServeGen (NSDI 2026) releases, plus [Mooncake's Kimi conversation/tool traces](https://vllm.ai/blog/2026-05-06-mooncake-store), are the industry evidence that arrival process, length distribution, session structure and cache-hit rate are first-class measurement objects rather than incidental benchmark parameters.

**Coverage gaps for later discovery — not new admissions:** standardized multi-turn/session-level serving benchmarks beyond a single AgentSysBench-style entry; closed-division, MLPerf-style LLM *serving* harnesses published in academic venues; trace-driven cache-hit/prefix-reuse simulators (adjacent UniCache work lives under KV); energy/SLO Pareto benchmark standardization; output-consistency regression suites for serving-stack upgrades; and cost-model benchmarks for disaggregated P/D deployments. A missing mechanism does **not** justify importing model-quality leaderboards or training benchmarks.

## Papers (49)

### Serving Benchmark Suites and Measurement Methodology (3)

**端到端 Serving 基准与测量方法学**：定义吞吐/延迟/SLO 的基准设计、harness 与测量反模式，回答"系统应该被怎样公平地测量"。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [LLM-Inference-Bench: Inference Benchmarking of Large Language Models on AI Accelerators](https://ieeexplore.ieee.org/document/10820566) | SC24-W workshop 2024 | 提供硬件加速器推理吞吐和延迟评测方法；明确为 Workshop 而不是 SC 主会论文。 |
| 2024 | [The Importance of Workload Choice in Evaluating LLM Inference Systems](https://doi.org/10.1145/3642970.3655823) | EuroMLSys workshop 2024 | 系统比较输入/输出长度、请求到达过程等 Benchmark 设计对推理系统排名和判断的影响。 |
| 2025 | [On Evaluating Performance of LLM Inference Serving Systems](https://arxiv.org/abs/2507.09019) | arXiv 2025 (preprint) | 系统分析 Baseline Fairness、工作负载设置与 Serving Metric 设计的测量反模式，通过 Speculative Decoding Case Study 展示评估混淆及可复用核验清单。 |

### Acceleration-Technique Audits under Realistic Serving (7)

**加速技术的实证审计**：在真实 Batch/并发/负载下复测 Speculative Decoding、KV 压缩、P/D 分离与 Expert 负载均衡等技术的端到端收益，纠正"理论加速≠服务收益"。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/26289c647c6828e862e271ca3c490486-Abstract-Conference.html) | MLSys 2025 | 系统审视 KV Compression 的真实 GPU 服务端加速与任务质量，识别弱 Baseline 和不可信收益。 |
| 2026 | [An Empirical Study of Speculative Decoding for Small Language Models](https://aclanthology.org/2026.eacl-long.255/) | EACL 2026 (Long Paper) | 对 1–2B 小模型、三类 Model Family 和五类投机技术作实证比较，指出 Draft Overhead 经常比 Draft Quality 更限制加速，低计算开销 Retrieval Draft 更稳健；不宣称新 Serving Scheduler，实机配置、Batch/SLO 与工件可复现性待复审（HOLD_EVIDENCE）。 |
| 2026 | [Beyond the Buzz: A Pragmatic Take on Inference Disaggregation](https://proceedings.mlsys.org/paper_files/paper/2026/hash/d49cee5f3a79d97d719df255689d83d7-Abstract-Conference.html) | MLSys 2026 | 通过不同规模部署评估 P/D 分离的价值和资源、传输及调度边界。 |
| 2026 | [On the Diminishing Returns of Expert Load Balancing in MoE LLM Serving](https://mlsys.org/virtual/2026/poster/10193) | MLSys 2026 | 对 MoE Expert 负载均衡收益进行反向实证分析；快速准入（会议节目/书目索引），实机执行、Strong Baseline 与端到端服务指标待二审（HOLD_EVIDENCE）。 |
| 2026 | [SPEED-Bench: A Unified and Diverse Benchmark for Speculative Decoding](https://proceedings.mlr.press/v306/abramovich26a.html) | ICML 2026 | 在 vLLM/TensorRT-LLM 的真实 Batch/吞吐负载下量化 Speculative Decoding 对数据分布和 Draft 长度的敏感性。 |
| 2026 | [Scaling Up, Speeding Up: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling](https://openreview.net/forum?id=DjOmnwX4wJ) | ICLR 2026 | 标准化比较 Best-of-N/多轮推理中的模型型、训练型与 N-Gram Speculative Decoding，对重复推理轨迹的加速边界做实证研究；Benchmark 而非新 Runtime Scheduler。 |
| 2026 | [Speculative Decoding: Performance or Illusion?](https://proceedings.mlsys.org/paper_files/paper/2026/hash/554e056fe2b6d9fd27ffcd3367ae1267-Abstract-Conference.html) | MLSys 2026 | 在现实 vLLM Batch/负载下复测多类推测解码，并对比理论上限。 |

### Production Traces and Workload Characterisation (5)

**生产负载 Trace 与负载刻画**：真实请求日志的到达过程、输入/输出长度与会话结构、KV 命中与容量需求，以及可复现的负载合成。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [BurstGPT: A Real-World Workload Dataset to Optimize LLM Serving Systems](https://doi.org/10.1145/3711896.3737413) | KDD 2025 | 基于云端 LLM 请求日志发布 Bursty Traffic/长度/失败 Trace，并在真实负载特征下评估 Serving 调度与缓存设计。 |
| 2025 | [KVCache Cache in the Wild: Characterizing and Optimizing KVCache Cache at a Large Cloud Provider](https://www.usenix.org/conference/atc25/presentation/wang-jiahao) | USENIX ATC 2025 | 基于云厂商真实请求 Trace 刻画跨轮/单轮 KV 命中、复用时间和容量需求，评估工作负载感知的缓存决策。 |
| 2026 | [Characterizing Cloud-Native LLM Inference at ByteDance and Exposing Optimization Challenges and Opportunities for Future AI Accelerators](https://doi.org/10.1109/HPCA68181.2026.11408526) | HPCA 2026 (Industry Track) | 以 Doubao 生产负载与跨 Instruction/Kernel/Model 多级评估刻画异构 LLM 推理瓶颈及硬件选型边界。 |
| 2026 | [Reasoning Language Model Inference Serving Unveiled: An Empirical Study](https://iclr.cc/virtual/2026/poster/10011393) | ICLR 2026 | 该研究通过内存波动、掉队者与自适应运行时刻画推理模型 serving，并在真实负载下评估量化、KV 量化、speculative decoding 与前缀缓存 |
| 2026 | [ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) | NSDI 2026 | 基于真实云服务 Trace 刻画多类型推理负载并合成代表性请求流。 |

### Real-System Performance, Scaling and Energy Characterisation (7)

**真实系统的性能、扩展与能耗刻画**：跨加速器/集群测量 Prefill/Decode、并行度、通信与能耗行为，并分解 MoE 等执行的"税项"。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [Beyond Throughput: Performance and Energy Insights of LLM Inference Across AI Accelerators](https://doi.org/10.1109/IPDPS65963.2026.00083) | IPDPS 2026 | 真实物理加速器比较：六款 NVIDIA/AMD/Intel GPU 及两类 Cerebras/SambaNova Dataflow Accelerator、14 个开源模型，测量 Prefill/Decode、Batch/并行度、能耗 Pareto；作者公开 vLLM/功耗脚本（异构厂商依赖仍需注意）。 |
| 2026 | [Characterizing LLM Inference Energy-Performance Tradeoffs across Workloads and GPU Scaling](https://doi.org/10.1109/CCGrid68966.2026.00013) | CCGrid 2026 (full paper) | 基于不同 LLM Workload、GPU 规模、并行策略分析功耗、延迟和吞吐的实机权衡，为 GPU Scaling 的性能/能效选择提供测量参考；IEEE 正式论文身份已证实，但具体设备/模型矩阵、能耗传感器校准、GPU 动态功率限制和 SLO-constrained Energy Pareto 尚待核验（HOLD_EVIDENCE）。 |
| 2026 | [Characterizing Parallelism Strategies in LLM Inference: Fundamental Compute-Communication Trade-offs](https://arxiv.org/abs/2610.05305) | arXiv 2026 (preprint) | 解析 TP/PP/Hybrid 的 Collective、点对点通信与 Pipeline Bubble，比较 Prefill/Decode 不同瓶颈。 |
| 2026 | [Demystifying the Mixture of Experts Serving Tax](https://proceedings.mlsys.org/paper_files/paper/2026/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | MLSys 2026 | 将 MoE 的 Prefill/Decode 开销分解为可量化执行税项。 |
| 2026 | [Performance Characterization and Optimization of LLM Inference on Tenstorrent AI Accelerators](https://doi.org/10.1007/978-3-032-35251-4_32) | Euro-Par 2026 (Springer LNCS imprint 2027) | 真实 Tenstorrent Wormhole 的 Tensix Decode 剖析与 Chip-Pipe 跨芯片 Pipeline Parallel 调度；作者报告 Llama-3.1-8B 等四模型相对 TP 吞吐改善，需保留芯片专用编程与实验范围；会议于 2026 年举行、Springer 正式书卷标记 2027 出版。 |
| 2026 | [TokenPowerBench: Benchmarking the Power Consumption of LLM Inference](https://doi.org/10.1609/aaai.v40i38.40535) | AAAI 2026 (Full Paper) | 多层级 GPU/Node/System 能耗测量与请求级 Prefill/Decode Phase Attribution，覆盖四种模型系列及 Batch/Context/Parallelism/Quantization 的 J/token 对比；作者发布基准。测量校准、传感器精度和 Serving QoS/能效 Pareto 前沿待审（HOLD_EVIDENCE）。 |
| 2026 | [Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles](https://doi.org/10.1109/ISCA66397.2026.00084) | ISCA 2026 (Industry Track) | 在真实 GPU Cluster 上刻画 8B–671B 推理的 DP/TP/PP、长 CoT KV 容量陷阱与 MoE 同步瓶颈；提供部署权衡测量而非单一加速算法。 |

### Profiling, Diagnosis and Observability (4)

**Profiling、诊断与可观测性**：冷启动关键路径、eBPF/IR 级细粒度追踪、生产异常触发追踪与跨栈性能分析基础设施。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://proceedings.mlsys.org/paper_files/paper/2026/hash/29416b66c2149872b9d1415a3fd2c5e0-Abstract-Conference.html) | MLSys 2026 | 剖析 vLLM 冷启动的初始化、权重加载和图捕获关键路径。 |
| 2026 | [ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler](https://openreview.net/forum?id=tYHWS7YPof) | MLSys 2026 | ProfInfer 使用 eBPF 在不修改或重编译 llama.cpp 的情况下，对 token、计算图、算子和硬件计数器进行多粒度追踪，提供 ProfDAG、ProfTime、ProfStat 视图，覆盖 dense、MoE routing 与 offloading |
| 2026 | [StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference (Operational Systems)](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) | OSDI 2026 | 按关键同步点和异常触发跟踪降低生产推理诊断开销，结合关键路径与 Roofline 回归定位故障。 |
| 2026 | [XProf: An Open, Scalable, and Extensible Profiling System for the Modern ML Stack](https://proceedings.mlsys.org/paper_files/paper/2026/hash/280776fda5970060e6a5efcfd43e5d2d-Abstract-Conference.html) | MLSys 2026 | OpenXLA/PJRT Full-stack CPU–TPU/GPU Profiling、Roofline 与跨千卡低开销分布式 Trace；开源生产级性能分析基础设施，但不是 LLM Serving 专用评测（KEEP_ADJACENT）。 |

### Performance Modelling, Analytical Bounds and Simulators (8)

**性能建模、解析界与模拟器**：Roofline/排队/硬件延迟模型与协同模拟，用可校验的误差边界替代昂贵部署试验。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [LLMCompass: Enabling Efficient Hardware Design for Large Language Model Inference](https://ieeexplore.ieee.org/abstract/document/10609604) | ISCA 2024 | 映射搜索、硬件面积/成本模型及延迟预测联合评估 LLM 推理硬件设计，并与实测延迟对齐。 |
| 2024 | [LLMServingSim: A HW/SW Co-Simulation Infrastructure for LLM Inference Serving at Scale](https://doi.org/10.1109/IISWC63097.2024.00012) | IISWC 2024 | 构建 LLM 服务调度与硬件执行协同模拟，实现不同硬件/软件配置定量分析。 |
| 2024 | [Vidur: A Large-Scale Simulation Framework for LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/b74a8de47d2b3c928360e0a011f48351-Abstract-Conference.html) | MLSys 2024 | 基于算子 Profiling 与预测模型模拟 Batch/Parallelism/负载，使用真实推理数据校验仿真误差。 |
| 2026 | [A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints](https://proceedings.mlr.press/v306/nie26a.html) | ICML 2026 | 在队列稳定性模型中同时引入 GPU 计算和 KV 内存约束，推导稳定到达率/容量界，并在真实 GPU Serving 环境核验预测误差和 Provisioning 边界。 |
| 2026 | [Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference](https://proceedings.mlsys.org/paper_files/paper/2026/hash/dbc8ce0fdfcd55172d73fb05dbae07fc-Abstract-Conference.html) | MLSys 2026 | 精细化推理性能模拟并用跨模型/配置与真实部署验证预测误差。 |
| 2026 | [How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving](https://arxiv.org/abs/2605.28302) | arXiv 2026 (preprint) | 以实测 Kernel 与网络仿真对比聚合、P/D 与 AFD，在多工作负载和 SLO 下刻画拆分收益边界。 |
| 2026 | [LLMServingSim 2.0: A Unified Simulator for Heterogeneous and Disaggregated LLM Serving Infrastructure](https://arxiv.org/abs/2602.23036) | arXiv 2026 (preprint) | 把调度、路由、Offload、功率与互联行为置于统一 Runtime Loop，并对真实部署指标校准。 |
| 2026 | [When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference](https://arxiv.org/abs/2608.03741) | arXiv 2026 (preprint) | HeteroPanacea 联合模拟阶段量化、并行分配及 P/D/A/F 异构芯片，结论依赖硬件模型假设（HOLD_EVIDENCE）。 |

### Reliability, Correctness and Semantic Integrity (7)

**可靠性、正确性与语义完整性**：真实 Bug/故障注入、张量并行归约确定性、基础设施漂移与有损优化的语义风险审计。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [A First Look at Bugs in LLM Inference Engines](https://doi.org/10.1145/3788873) | ACM TOSEM 2026 | 对 llama.cpp、vLLM、DeepSpeed、MLC-LLM、TensorRT-LLM 的 929 个真实 Bug 手工标注，归纳六类症状、28 类根因并开放缺陷数据集，指导运行时故障定位。 |
| 2026 | [Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch](https://proceedings.mlr.press/v306/zhang26ag.html) | ICML 2026 | 剖析不同 Tensor Parallel Size 的归约顺序并实现确定性推理。 |
| 2026 | [DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems](https://openreview.net/forum?id=Xfzzp6grRP) | MLSys 2026 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更 |
| 2026 | [Not All Errors Are Equal: A Systematic Study of Error Propagation in Large Language Model Inference](https://doi.org/10.1145/3797905.3800513) | ICS 2026 (full paper) | **LLMFI** 可配置的确定性 Fault Injection，涵盖 3 开源 LLM、13 类推理/多语/数学/代码任务并归纳 17 条误差传播规律；属于推理可靠性的实证研究，不是加速新机制。需要核查 GPU/CPU Fault Site、误差注入统计置信度、数据/代码和模型输出有效性，**HOLD_REPRO**（HOLD_EVIDENCE）。 |
| 2026 | [Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression](https://proceedings.mlr.press/v306/liu26dz.html) | ICML 2026 | KVFundaBench 强调评估 KV 压缩对密集推理语义的真实影响（HOLD_EVIDENCE）。 |
| 2026 | [The Pitfalls of KV Cache Compression](https://aclanthology.org/2026.acl-long.1926/) | ACL 2026 | 实证审计 StreamingLLM/SnapKV/TOVA/H2O/K-Norm 在复杂多指令 Prompt 上的 KV 驱逐语义损失与指令忽略/系统 Prompt 泄露；是部署质量风险评测而非新增 GPU 加速算法（HOLD_EVIDENCE）。 |
| 2026 | [When KV Cache Reuse Fails in Multi-Agent Systems: Cross-Candidate Interaction is Crucial for LLM Judges](https://aclanthology.org/2026.acl-long.327/) | ACL 2026 (Long Paper) | 在 GSM8K、MMLU、HumanEval 的 Multi-Agent Judge 场景，以 Dense Prefill 为参考测量 KV 复用导致的 Judge Consistency Rate (JCR) 下降；包含 KVCOMM 对照与复现实验代码。属于 KV 复用正确性反例研究，论文明确不宣称系统级 TTFT/吞吐改进；G3/G5 仍待复审（HOLD_EVIDENCE）。 |

### Kernel and Agentic-Kernel Benchmarking (4)

**Kernel 与 Agentic Kernel 基准**：KernelBench 谱系的 Kernel 生成/评测环境、正确性反馈闭环与 AI 驱动 Kernel 优化评测；只评 Kernel 生成，不等同 Serving 加速。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [KernelBench: Can LLMs Write Efficient GPU Kernels?](https://proceedings.mlr.press/v267/ouyang25a.html) | ICML 2025 | 奠基性 Kernel Generation 测试环境：250 个 PyTorch ML Workload、正确性加速联合指标 fast_p，并考察迭代 Profiling Feedback；是通用 Kernel 评测前提，不是 LLM Serving 端到端 Benchmark（KEEP_FOUNDATIONAL）。 |
| 2026 | [FlashInfer-Bench: Building the Virtuous Cycle for AI-driven LLM Systems](https://proceedings.mlsys.org/paper_files/paper/2026/hash/37e44c4b5321605735be9761f9b758fc-Abstract-Conference.html) | MLSys 2026 | FlashInfer-Bench 构建了一套基准与反馈闭环，用于评测并迭代改进由 AI 驱动的 LLM 系统实现，形成“评测—优化”的良性循环 |
| 2026 | [KernelCraft: Benchmarking for Agentic Close-to-Metal Kernel Generation on Emerging Hardware](https://proceedings.mlr.press/v306/nie26c.html) | ICML 2026 | 面向新兴 NPU ISA 的 Agentic Kernel 编译、正确性反馈与性能评测；涵盖真实 AMD NPU、PLENA 模拟器与 Verilator RTL，基准代码的公开状态需复核，不是生产 Serving 加速。 |
| 2026 | [TritonGym: A Benchmark for Agentic LLM Workflows in Triton GPU Code Generation](https://proceedings.mlr.press/v306/guan26d.html) | ICML 2026 | 以可复现的工具调用/编译/正确性与速度反馈环境评估多轮 Triton Kernel Agent，覆盖 OOD 与扩展 DSL；是真实 Kernel 执行 Benchmark，不等于 LLM Serving Speedup。 |

### Agentic, Session-Level and Multimodal Workloads (4)

**Agentic、会话级与多模态负载刻画**：打破"单请求纯文本"假设的 Agent/多轮会话成本结构与多模态/VLA 推理瓶颈（邻接工作以 KEEP_ADJACENT 标注）。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [Towards Efficient Large Multimodal Model Serving](https://arxiv.org/abs/2502.00937) | arXiv 2025 (preprint) | 对真实多模态服务 Trace 和六类模型进行分阶段 Profiling，评估编码/Prefill/Decode 解耦及资源分配的 SLO 影响（KEEP_ADJACENT）。 |
| 2026 | [Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://proceedings.mlr.press/v306/zhou26e.html) | ICML 2026 | 在 GPU/NPU 等异构设备上实测 VLA Backbone 与 Action Expert 的不同 Roofline/资源瓶颈，以 DP-Cache 和异步 V-AE Pipeline 优化控制延迟与能效（邻接 Embodied Inference）（KEEP_ADJACENT）。 |
| 2026 | [From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems](https://arxiv.org/abs/2608.15127) | arXiv 2026 (preprint; AgentSysBench) | 用十类 Agent 应用、受控部署与真实 Trace 分离 GPU Inference、CPU Sandbox、Retrieval 和持久会话的系统成本，提供任务感知调度、状态卸载等可执行设计探索；未经独立复现。 |
| 2026 | [The Cost of Dynamic Reasoning: Demystifying AI Agents and Test-Time Scaling from an AI Infrastructure Perspective](https://2026.hpca-conf.org/details/hpca-2026-main-conference/17/The-Cost-of-Dynamic-Reasoning-Demystifying-AI-Agents-and-Test-Time-Scaling-from-an-A) | HPCA 2026 | 对 Agent/Test-Time Scaling 的计算、能耗与设备性能进行系统性测量。 |

---
*Publication source and mechanism screened; speedup claims are not independently reproduced. Inline HOLD tags remain unresolved strict-review items, and KEEP_ADJACENT / KEEP_FOUNDATIONAL rows are explicit scope exceptions rather than evidence of LLM-serving speedups.*
