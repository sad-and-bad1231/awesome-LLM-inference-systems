# Benchmarking & Systems Analysis

Measuring real inference workloads, modeling system performance, validating simulations and diagnosing production incidents.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Accept methods with an explicit workload/evaluation model and validation; generic leaderboards do not qualify.

**Foundational context.** See also: [Serving systems](serving-systems.md) for workload-focused execution studies.
## Papers (8)

A selective, chronological bibliography; each paper's principal mechanism determines its only full-topic entry. See [curation criteria](../CURATION.md) and the [migration record](serving-systems.md) for historical changes.

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [LLM-Inference-Bench: Inference Benchmarking of Large Language Models on AI Accelerators](https://ieeexplore.ieee.org/document/10820566) | SC24-W workshop 2024 | 提供硬件加速器推理吞吐和延迟评测方法；明确为 Workshop 而不是 SC 主会论文。 |
| 2024 | [LLMCompass: Enabling Efficient Hardware Design for Large Language Model Inference](https://ieeexplore.ieee.org/abstract/document/10609604) | ISCA 2024 | 映射搜索、硬件面积/成本模型及延迟预测联合评估 LLM 推理硬件设计，并与实测延迟对齐。 |
| 2024 | [LLMServingSim: A HW/SW Co-Simulation Infrastructure for LLM Inference Serving at Scale](https://doi.org/10.1109/IISWC63097.2024.00012) | IISWC 2024 | 构建 LLM 服务调度与硬件执行协同模拟，实现不同硬件/软件配置定量分析。 |
| 2024 | [The Importance of Workload Choice in Evaluating LLM Inference Systems](https://doi.org/10.1145/3642970.3655823) | EuroMLSys workshop 2024 | 系统比较输入/输出长度、请求到达过程等 Benchmark 设计对推理系统排名和判断的影响。 |
| 2024 | [Vidur: A Large-Scale Simulation Framework for LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/b74a8de47d2b3c928360e0a011f48351-Abstract-Conference.html) | MLSys 2024 | 基于算子 Profiling 与预测模型模拟 Batch/Parallelism/负载，使用真实推理数据校验仿真误差。 |
| 2025 | [Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/26289c647c6828e862e271ca3c490486-Abstract-Conference.html) | MLSys 2025 | 系统审视 KV Compression 的真实 GPU 服务端加速与任务质量，识别弱 Baseline 和不可信收益。 |
| 2026 | [ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) | NSDI 2026 | 基于真实云服务 Trace 刻画多类型推理负载并合成代表性请求流。 |
| 2026 | [StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference (Operational Systems)](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) | OSDI 2026 | 按关键同步点和异常触发跟踪降低生产推理诊断开销，结合关键路径与 Roofline 回归定位故障。 |

*Venue and mechanisms follow primary publication material; authors' experimental claims are not independently reproduced.*
