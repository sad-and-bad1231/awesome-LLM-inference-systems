# Runtime & Scheduling

Scheduling tokens, requests and model instances within online inference services to satisfy latency, utilization and fairness.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Use this class when a new request-level policy, queueing rule, or batching/routing mechanism is decisive; physical cluster separation belongs in Distributed.

**Foundational context.** See also: [Orca (2022), Sarathi-Serve (2024), Llumnix (2024), NanoFlow (2025)](../README.md#foundational-and-influential-papers).

## Newly admitted · October 2026 (1)

These entries have individually checked primary publication records. Descriptions summarize *the authors' mechanisms and evidence*; they do not imply independent reproduction, nor final adjudication of all earlier repository entries.

| Year | Paper | Venue | Distinct system mechanism |
|---|---|---|---|
| 2024 | [Fairness in Serving Large Language Models](https://www.usenix.org/conference/osdi24/presentation/sheng) | OSDI 2024 | Virtual Token Counter 把 Prefill/Decode 的 Token Cost 计入公平服务定义和连续批处理调度。 |

**Legacy cohort.** Previously collected Serving papers remain on [Serving Systems](serving-systems.md) pending individual re-admission/reclassification. A paper is not automatically admitted into this category based on a prior status flag.

## Legacy Serving cohort — re-admitted (19)

Reclassified by **primary systems mechanism**, not legacy “Serving” keywords. Bibliographic links have been updated where a stronger individual source was found; other links preserve the original proceedings record.

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2024 | [ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference](https://arxiv.org/abs/2404.07947) | ASPLOS 2024 | 将推理资源配置与约束条件共同纳入调度，比较部署配置的延迟与吞吐。 |
| 2024 | [MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving](https://proceedings.mlr.press/v235/duan24a.html) | ICML 2024 | 按模型热度联合空间/时间复用显存与计算，区分 Prefill/Decode 的资源需求。 |
| 2024 | [Punica: Multi-Tenant LoRA Serving](https://proceedings.mlsys.org/paper_files/paper/2024/file/054de805fcceb78a201f5e9d53c85908-Paper-Conference.pdf) | MLSys 2024 | 以 SGMV Kernel 合批不同 LoRA Adapter 的 Decode，并统一调度多租户请求。 |
| 2025 | [Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market](https://doi.org/10.1145/3731569.3764815) | SOSP 2025 | Token 粒度复用 GPU 承载模型长尾，低开销弹性调整并验证生产服务。 |
| 2025 | [Preble: Efficient Distributed Prompt Scheduling for LLM Serving](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5bc342f48de8264779952fac378f96dc-Abstract-Conference.html) | ICLR 2025 | 在分布式请求调度中联合 KV 复用收益与负载均衡，复用重复 Prompt。 |
| 2025 | [SOLA: Optimizing SLO Attainment for Large Language Model Serving with State-Aware Scheduling](https://proceedings.mlsys.org/paper_files/paper/2025/hash/bc82dbfbfa43232be85b8d9838f49c3e-Abstract-Conference.html) | MLSys 2025 | 按请求和全局状态动态调节 Iteration 调度以协调 TTFT 与 TPOT。 |
| 2026 | [Agentix: An Efficient Serving Engine for LLM Agents as General Programs](https://www.usenix.org/conference/nsdi26/presentation/luo) | NSDI 2026 | 将 Agent 程序依赖纳入服务调度，降低请求和程序级 Head-of-line Blocking。 |
| 2026 | [BatchLLM: Optimizing Large Batched LLM Inference with Global Prefix Sharing and Throughput-oriented Token Batching](https://proceedings.mlsys.org/paper_files/paper/2026/hash/5b7ae1758452854dee4e962207d38304-Abstract-Conference.html) | MLSys 2026 | 对离线大批量任务跨请求共享全局 Prefix，并采用吞吐导向 Token Batching。 |
| 2026 | [Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration](https://doi.org/10.1145/3779212.3790135) | ASPLOS 2026 | 联合时间与空间调度降低在线推理的 GPU 空闲与资源碎片。 |
| 2026 | [FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees](https://www.usenix.org/conference/nsdi26/presentation/oliaro) | NSDI 2026 | 共享 GPU 上按 Token 协同 PEFT 与在线推理，优化激活内存和 SLO。 |
| 2026 | [JITServe: SLO-aware LLM Serving with Imprecise Request Information](https://www.usenix.org/conference/nsdi26/presentation/zhang-wei) | NSDI 2026 | 渐进修正未知请求长度估计，以 Just-in-time 资源分配优化 Goodput。 |
| 2026 | [KUNSERVE: Parameter-centric Memory Management for Efficient Memory Overloading Handling in LLM Serving](https://dl.acm.org/doi/10.1145/3767295.3769348) | EuroSys 2026 | 以参数为中心处理 Serving 的显存超额占用，减少模型切换及请求停顿。 |
| 2026 | [Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads](https://www.usenix.org/conference/nsdi26/presentation/ruan-libra) | NSDI 2026 | 以 Micro-request 分解动态 Prefill/Decode 工作量，在不均衡负载下调度并满足 SLO。 |
| 2026 | [MFS: An Efficient Model Family Serving System for LLMs](https://doi.org/10.1145/3767295.3769355) | EuroSys 2026 | 利用同系列模型之间的参数/执行共享特征优化多模型服务。 |
| 2026 | [MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing](https://openreview.net/forum?id=1JyePezdlF) | MLSys 2026 | 动态调整量化 Layer Residency 与 KV 容量以适应请求规模变化。 |
| 2026 | [PLA-Serve: A Prefill-Length-Aware LLM Serving System](https://openreview.net/forum?id=dzjCkSEDyG) | MLSys 2026 | 按 Prompt Prefill 长度协调请求分配，处理长短输入混合下的资源干扰。 |
| 2026 | [QoServe: Breaking the Silos of LLM Inference Serving](https://doi.org/10.1145/3779212.3790206) | ASPLOS 2026 | 针对独立 Serving 部署的资源孤岛，研究跨服务资源共享与 QoS。 |
| 2026 | [Simple Is Better: Multiplication May Be All You Need for LLM Request Scheduling](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) | OSDI 2026 | 结合缓存重算量与实例 Batch 规模构造免调参 Routing Metric，并验证生产部署。 |
| 2026 | [TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling](https://doi.org/10.1145/3767295.3769328) | EuroSys 2026 | 利用客户端 Token Buffer 的富余量实施抢占调度与主动 KV Offload。 |

## Newly admitted · Wave 2 (2)

Publisher/conference identity and the distinct inference mechanism were reviewed. Very early compiler papers are included as *foundational execution primitives*; work with cross-model training applicability is explicitly described.

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2024 | [dLoRA: Dynamically Orchestrating Requests and Adapters for LoRA LLM Serving](https://www.usenix.org/conference/osdi24/presentation/wu-bingyang) | OSDI 2024 | Credit-based LoRA Batching 与 Adapter/Request 协同迁移，提高多租户低秩适配器 Serving 效率。 |
| 2024 | [Parrot: Efficient Serving of LLM-based Applications with Semantic Variable](https://www.usenix.org/conference/osdi24/presentation/lin-chaofan) | OSDI 2024 | 以 Semantic Variable 暴露请求间数据依赖，支持 Agentic Workflow 级任务排程和 Prefix 复用。 |

