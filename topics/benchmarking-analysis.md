# Benchmarking & Systems Analysis

Measuring real inference workloads, modeling system performance, validating simulations and diagnosing production incidents.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Accept methods with an explicit workload/evaluation model and validation; generic leaderboards do not qualify.

**Foundational context.** See also: [Serving systems](serving-systems.md) for workload-focused execution studies.

## Newly admitted · October 2026 (3)

These entries have individually checked primary publication records. Descriptions summarize *the authors' mechanisms and evidence*; they do not imply independent reproduction, nor final adjudication of all earlier repository entries.

| Year | Paper | Venue | Distinct system mechanism |
|---|---|---|---|
| 2024 | [Vidur: A Large-Scale Simulation Framework for LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2024/hash/b74a8de47d2b3c928360e0a011f48351-Abstract-Conference.html) | MLSys 2024 | 基于算子 Profiling 与预测模型模拟 Batch/Parallelism/负载，使用真实推理数据校验仿真误差。 |
| 2024 | [LLMCompass: Enabling Efficient Hardware Design for Large Language Model Inference](https://ieeexplore.ieee.org/abstract/document/10609604) | ISCA 2024 | 映射搜索、硬件面积/成本模型及延迟预测联合评估 LLM 推理硬件设计，并与实测延迟对齐。 |
| 2026 | [StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference (Operational Systems)](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) | OSDI 2026 | 按关键同步点和异常触发跟踪降低生产推理诊断开销，结合关键路径与 Roofline 回归定位故障。 |

**Legacy cohort.** Previously collected Serving papers remain on [Serving Systems](serving-systems.md) pending individual re-admission/reclassification. A paper is not automatically admitted into this category based on a prior status flag.
