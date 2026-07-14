# Awesome AI Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[![Academic Papers](https://img.shields.io/badge/Academic%20Papers-432-168de2)](papers/README.md) [![Industry Systems](https://img.shields.io/badge/Industry%20Systems-120-0a8f6a)](industry/README.md) [![Formal Venues](https://img.shields.io/badge/Formal%20Venues-178-7b61ff)](papers/README.md#evidence-and-selection) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2026-555555) [![CI](https://img.shields.io/badge/CI-workflow-brightgreen)](https://github.com/sad-and-bad1231/awesome-LLM-inference-systems/actions/workflows/validate-and-render.yml)

![AI inference systems serving stack](figs/ai-inference-systems-cover.png)

A curated, evidence-aware collection of LLM inference serving papers, industrial systems, and open-source AI infrastructure.

## Overview

This repository maps the serving mainline from request state to production operations: memory, transport, execution, runtime scheduling, and reliability.

We prioritize work with system-level mechanisms, real hardware or production evidence, and clear connections to serving ecosystems such as vLLM, SGLang, TensorRT-LLM, Kubernetes, and LMCache.

Out of scope by default: training-only methods, algorithm-only simulations without serving evidence, generic vector databases, and peripheral hardware work without an inference-system connection.

## Contents

- [Academic Papers](papers/README.md)
- [Industry & Open-Source Systems](industry/README.md)
- [System Abstraction Overview](ai-infra-system-abstractions.md)
- [Contribution Guide](CONTRIBUTING.md)

## Coverage

| Collection | Records | Evidence breakdown |
|---|---:|---|
| Academic papers | 432 | Formal Conference · Legacy Import: 178, Poster / Workshop · Legacy Import: 37, Preprint · Legacy Import: 160, Unclassified · Legacy Import: 57 |
| Industry / open-source systems | 120 | Industrial Material · Legacy Import: 120 |

## Taxonomy

| System abstraction | Records | Entry points |
|---|---:|---|
| **KV State & Memory** | 174 | [Papers](papers/README.md#kv-state-memory) · [Industry](industry/README.md#kv-state-memory) |
| **P/D Disaggregation & KV Transfer** | 51 | [Papers](papers/README.md#p-d-disaggregation-kv-transfer) · [Industry](industry/README.md#p-d-disaggregation-kv-transfer) |
| **KV Compression & Low-Bit State** | 87 | [Papers](papers/README.md#kv-compression-low-bit-state) · [Industry](industry/README.md#kv-compression-low-bit-state) |
| **Kernel & Compiler** | 76 | [Papers](papers/README.md#kernel-compiler) · [Industry](industry/README.md#kernel-compiler) |
| **Runtime & Serving** | 144 | [Papers](papers/README.md#runtime-serving) · [Industry](industry/README.md#runtime-serving) |
| **Reliability & Benchmarks** | 20 | [Papers](papers/README.md#reliability-benchmarks) · [Industry](industry/README.md#reliability-benchmarks) |

## System Map

![AI inference system abstractions](figs/ai-inference-system-map.png)

## Featured Papers

- **FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference**
  `NSDI 2026` · `2026` · `Formal Conference · Legacy Import`
  FastServe 用 token 粒度抢占、skip-join MLFQ 和 KV 状态换入换出降低长请求造成的队头阻塞。
- **HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds**
  `NSDI 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `serving` `latency`
  HydraServe 主动分发模型、重叠 worker 冷启动阶段并规避网络争用，以 pipeline consolidation 降低 serverless LLM 启动资源。
- **QoServe: Breaking the Silos of LLM Inference Serving**
  `ASPLOS 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `serving`
  QoServe 统一管理原本割裂的 LLM serving 资源池，以减少不同服务等级和工作负载之间的资源孤岛。
- **PLA-Serve: A Prefill-Length-Aware LLM Serving System**
  `MLSys 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `prefill` `serving` `gpu`
  PLA-Serve 将 prefill 长度显式纳入请求分组和批处理决策，减少长短 prompt 混合时的首 token 延迟和 GPU 空闲。
- **MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing**
  `MLSys 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `serving` `kv-cache`
  MorphServe 在运行时联合调整层级量化换入和 KV cache 大小，使服务配置随负载和内存压力动态变化。
- **AIRS: Scaling Live Inference in Resource Constrained Environments**
  `MLSys 2026` · `2026` · `Formal Conference · Legacy Import`
  AIRS 面向资源受限的在线推理流水线动态分配加速器与任务优先级，提高多阶段 LLM 评估/预测服务的吞吐和延迟稳定性。
- **Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration**
  `OSDI 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `serving` `gpu`
  该工作用跨实例编排减少 commodity GPU 集群中的重复数据搬运和状态开销，提高低成本 GPU 上的 serving 效率。
- **SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems**
  `NSDI 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `serving` `kv-cache` `memory`
  SYMPHONY 将计算和 KV cache 存储解耦为 disaggregated memory management layer，以满足多轮会话状态的低延迟访问。
- **SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading**
  `NSDI 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `cuda` `rdma` `moe`
  SwiftEP 用 buffer fusion 消除 MoE all-to-all staging copy，并以 TMA、RDMA scatter-gather 和 CUDA IPC 提高链路利用率。
- **TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference**
  `ASPLOS 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `decode` `prefill`
  TPLA 将 latent attention 与 tensor parallel 结合，降低 PD 分离推理中的 KV 和跨卡通信压力。
- **XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads**
  `ASPLOS 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `serving` `kernel`
  XY-Serve 用 token-wise P/D/V 调度、任务分解重排和 Ascend meta-kernel 平滑动态 shape 与混合阶段负载。
- **BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization**
  `MLSys 2026` · `2026` · `Formal Conference · Legacy Import`
  Tags: `serving` `gpu`
  BOute 用多目标贝叶斯优化在异构模型和 GPU 组合中选择 serving 配置，联合降低成本并满足质量和延迟目标。

## Featured Industry Systems

- **[Dynamo](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)**
  `NVIDIA` · `2025` · `Industrial Material · Legacy Import`
  Tags: `routing` `serving` `kv-cache`
  分布式/分离式推理框架，组合 disaggregated serving、KV cache-aware routing、KV offloading，并用 NIXL 做低延迟 KV 传输。
- **[NIXL / KV cache transfer](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html)**
  `NVIDIA` · `2025` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `kv-cache`
  面向推理数据移动的传输层，在 prefill/decode 分离时把 KV cache 从 prefill worker 传到 decode worker。
- **[FlashMLA](https://github.com/deepseek-ai/FlashMLA)**
  `DeepSeek` · `2025` · `Industrial Material · Legacy Import`
  Tags: `decode` `gpu` `hopper` `kernel` `kv-cache`
  面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。
- **[vLLM V1 + torch.compile](https://pytorch.org/projects/vllm/)**
  `PyTorch Foundation / vLLM community` · `2025` · `Industrial Material · Legacy Import`
  Tags: `prefill` `vllm`
  vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。
- **[llm-d + LMCache + vLLM](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes)**
  `IBM / Red Hat / llm-d` · `2025` · `Industrial Material · Legacy Import`
  Tags: `kubernetes` `llm-d`
  Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。
- **[LMCache](https://arxiv.org/abs/2510.09665)**
  `LMCache 社区 / 企业采用` · `2025` · `Industrial Material · Legacy Import`
  Tags: `gpu` `kv-cache` `rag` `lmcache`
  将 KV cache 抽成独立层，支持跨 engine/query 复用和 GPU/CPU/storage/network 多层编排。
- **[Mooncake](https://www.usenix.org/conference/fast25/presentation/qin)**
  `Moonshot AI + Tsinghua` · `2025` · `Industrial Material · Legacy Import`
  Tags: `serving`
  以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。
- **[Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm)**
  `NVIDIA` · `2026` · `Industrial Material · Legacy Import`
  Tags: `memory` `tensorrt-llm` `vllm`
  KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。
- **[ROCm + vLLM/SGLang/TensorRT-LLM ecosystem](https://rocm.docs.amd.com/)**
  `AMD` · `2024` · `Industrial Material · Legacy Import`
  Tags: `amd` `gpu` `kernel` `sglang` `tensorrt-llm`
  通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。
- **[SGLang 商业化](https://github.com/sgl-project/sglang)**
  `SGLang maintainers / RadixArk` · `2026` · `Industrial Material · Legacy Import`
  Tags: `sglang`
  围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。

## Evaluation Lens

The collection tracks system behavior beyond isolated token throughput:

| Metric | What to look for |
|---|---|
| **TTFT under Drift** | 首 token 延迟在网络抖动、Spot 切换和基础设施漂移下的恶化边界。 |
| **Generation Stall Rate** | 由验证失败、专家拥塞或 tool-call 挂起造成的生成中断率。 |
| **Numerical Reproducibility** | 混合精度、量化和大规模部署中的数值稳定性与可复现性。 |

## Evidence Policy

Venue status and source type are factual metadata. Technical tags summarize the system surface. Legacy imports are marked explicitly. Internal triage priority is a discovery signal, not a publication-quality ranking.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Add facts to JSONL and regenerate the Markdown views; do not edit generated tables directly.
