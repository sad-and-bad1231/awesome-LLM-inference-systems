# Awesome AI Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[![Academic Papers](https://img.shields.io/badge/Academic%20Papers-63-168de2)](papers/README.md) [![Industry Systems](https://img.shields.io/badge/Industry%20Systems-31-0a8f6a)](industry/README.md) [![Formal Venues](https://img.shields.io/badge/Formal%20Venues-52-7b61ff)](papers/README.md#evidence-and-selection) ![Last Updated](https://img.shields.io/badge/Last%20Updated-2026-09-20-555555) [![CI](https://img.shields.io/badge/CI-workflow-brightgreen)](https://github.com/sad-and-bad1231/awesome-LLM-inference-systems/actions/workflows/validate-and-render.yml)

![AI inference systems serving stack](figs/ai-inference-systems-cover.png)

> **A serving-first research entrance.** Follow the request path from admission to output, then inspect where state lives, how it moves, how kernels execute, and how production systems recover.

A curated, evidence-aware collection of LLM inference serving papers, industrial systems, and open-source AI infrastructure.

## Overview

This repository maps the serving mainline from request state to production operations: memory, transport, execution, runtime scheduling, and reliability. The public reading path follows guide.md and keeps peripheral records in the archive.

We prioritize work with system-level mechanisms, real hardware or production evidence, and clear connections to serving ecosystems such as vLLM, SGLang, TensorRT-LLM, Kubernetes, and LMCache.

Out of scope by default: training-only methods, algorithm-only simulations without serving evidence, generic vector databases, and peripheral hardware work without an inference-system connection.

| In scope | Usually excluded unless they directly affect serving |
|---|---|
| LLM serving, KV state, P/D transport, kernels, runtimes, scheduling, SRE, and production infrastructure | Training-only optimization, pure model quality work, generic databases, and hardware papers without an inference path |

## Start Here

| Research entry point | What you get |
|---|---|
| [中文接手与阅读指南](docs/START-HERE.md) | 第一次打开仓库时从这里开始：项目结构、分类哲学、阅读顺序和最少命令。 |
| [Paper map](figs/ai-inference-system-map.png) | The six system abstractions and the serving lifecycle in one figure. |
| [Academic papers](papers/README.md) | Formal venues, preprints, legacy imports, and evidence labels kept separate. |
| [Industry systems](industry/README.md) | Core runtimes, operators, hardware stacks, transfer layers, and production material. |
| [Adjacent / archive](archive/README.md) | Peripheral or lower-priority records retained for audit without occupying the main reading path. |
| [Machine facts](data/papers.jsonl) | The JSONL records used to regenerate every public view. |

## Contents

| Start here | Purpose |
|---|---|
| [Academic Papers](papers/README.md) | Conference, poster, workshop, preprint, and legacy-import paper records. |
| [Industry & Open-Source Systems](industry/README.md) | Core runtimes, operators, hardware stacks, transfer layers, and production material. |
| [Adjacent / Archive](archive/README.md) | Related but non-mainline records, preserved with reasons and links. |
| [System Abstraction Overview](ai-infra-system-abstractions.md) | Cross-collection taxonomy and full system map. |
| [Contribution Guide](CONTRIBUTING.md) | JSONL facts, evidence policy, and generated-view workflow. |

## Coverage

| Papers | Industry systems | Formal paper venues | System abstractions |
|---:|---:|---:|---:|
| 63 | 31 | 52 | 6 |

| Collection | Records | Evidence breakdown |
|---|---:|---|
| Academic papers | 63 | Formal Conference: 20, Formal Conference · Legacy Import: 32, Preprint: 2, Preprint · Legacy Import: 5, Unclassified: 2, Unclassified · Legacy Import: 2 |
| Industry / open-source systems | 31 | Industrial Material: 9, Industrial Material · Legacy Import: 22 |

## Reading Paths

| Research question | Follow this path |
|---|---|
| **Reduce first-token latency** | P/D disaggregation, KV transfer, prefix reuse ([open](papers/README.md#p-d-disaggregation-kv-transfer)) |
| **Fit longer context** | KV state, offload, compression, and memory tiers ([open](papers/README.md#kv-state-memory)) |
| **Raise decode goodput** | Kernels, compilation, MoE execution, and batching ([open](papers/README.md#kernel-compiler)) |
| **Operate in production** | Runtime policy, SLOs, recovery, and ecosystem bindings ([open](industry/README.md#runtime-serving)) |
| **Deploy beyond CUDA** | AMD, TPU, NPU, Apple, and heterogeneous serving stacks ([open](industry/README.md#hardware-ecosystem)) |

## Taxonomy

| System abstraction | Records | What it covers | Entry points |
|---|---:|---|---|
| **KV State & Memory** | 24 | KV blocks, prefix state, offload, external memory, and memory-aware serving. | [Papers](papers/README.md#kv-state-memory) · [Industry](industry/README.md#kv-state-memory) |
| **P/D Disaggregation & KV Transfer** | 6 | Prefill/decode separation, KV transfer, routing, and distributed transport. | [Papers](papers/README.md#p-d-disaggregation-kv-transfer) · [Industry](industry/README.md#p-d-disaggregation-kv-transfer) |
| **KV Compression & Low-Bit State** | 20 | KV quantization, latent state, sparsity, and quality-cost tradeoffs. | [Papers](papers/README.md#kv-compression-low-bit-state) · [Industry](industry/README.md#kv-compression-low-bit-state) |
| **Kernel & Compiler** | 24 | CUDA, Triton, HIP, attention, GEMM, MoE kernels, and compiler backends. | [Papers](papers/README.md#kernel-compiler) · [Industry](industry/README.md#kernel-compiler) |
| **Runtime & Serving** | 16 | Runtime scheduling, agent graphs, structured generation, and SLO-aware dispatch. | [Papers](papers/README.md#runtime-serving) · [Industry](industry/README.md#runtime-serving) |
| **Reliability & Benchmarks** | 4 | SLOs, drift, recovery, reproducibility, benchmarks, and graceful degradation. | [Papers](papers/README.md#reliability-benchmarks) · [Industry](industry/README.md#reliability-benchmarks) |

## System Map

![AI inference system abstractions](figs/ai-inference-system-map.png)

## Featured Papers

- **[FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `npu` `compiler` `kernel` `agent` `edge` `vllm`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-wu-bingyang.pdf)
  以输出 token 为粒度实现可抢占的分布式 LLM serving，提出 skip-join 多级反馈队列，并主动在 GPU/主机内存间搬运中间状态；官方 NSDI 2026 页面报告相对 vLLM 吞吐最高提升 6.1 倍。
- **CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion**
  `EuroSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `serving` `edge` `rag`
  CacheBlend 复用非前缀知识片段的预计算 KV，并用知识融合机制降低 RAG prefill 延迟。
- **Context Parallelism for Scalable Million-Token Inference**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill`
  该工作用 pass-KV/pass-Q 两种精确 ring attention 在 128 张 H100 上扩展百万 token prefill 和 persistent-KV decode。
- **FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kernel`
  FlashInfer 用 block-sparse/composable KV format、JIT attention template 和 load-balanced scheduling 提供 serving-oriented kernel。
- **KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models**
  `SOSP 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `gpu` `kernel` `moe`
  KTransformers 把活跃 expert、attention 与其他算子分配到 CPU/GPU，并用定制 kernel 提升本地 MoE 推理。
- **NanoFlow: Towards Optimal Large Language Model Serving Throughput**
  `OSDI 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `gpu` `memory` `throughput`
  NanoFlow 将请求拆成 operation-level nano-batches，并在单 GPU 内重叠 compute、memory 和 network 资源。
- **QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kv-cache` `quantization`
  QServe 联合 W4A8KV4 量化、SmoothAttention、权重重排和寄存器级并行，将理论低比特节省转成云端 serving 吞吐。
- **XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `gpu` `agent` `rag`
  XGrammar 预处理上下文无关 token、压缩运行时 grammar 状态，并与 GPU 推理重叠以实现近零开销结构化生成。

## Featured Industry Systems

- **[vLLM V1 + torch.compile](https://pytorch.org/projects/vllm/)**
  `PyTorch Foundation / vLLM community` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `vllm`
  vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。
- **[Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `memory` `tensorrt-llm` `vllm`
  KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。
- **[ROCm + vLLM/SGLang/TensorRT-LLM ecosystem](https://rocm.docs.amd.com/)**
  `AMD` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `amd` `gpu` `kernel` `sglang` `tensorrt-llm`
  通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。
- **[SGLang 商业化](https://github.com/sgl-project/sglang)**
  `SGLang maintainers / RadixArk` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `sglang`
  围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。
- **[sglang-omni](https://github.com/sgl-project/sglang-omni)**
  `SGLang community` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: foundation`
  Tags: `serving`
  SGLang-Omni：面向音频等全模态模型的高性能服务框架。
- **[FlashInfer production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)**
  `NVIDIA / University of Washington` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kernel` `sglang` `vllm`
  从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。

## Evaluation Lens

The collection tracks system behavior beyond isolated token throughput:

| Metric | What to look for |
|---|---|
| **TTFT under Drift** | 首 token 延迟在网络抖动、Spot 切换和基础设施漂移下的恶化边界。 |
| **Generation Stall Rate** | 由验证失败、专家拥塞或 tool-call 挂起造成的生成中断率。 |
| **Numerical Reproducibility** | 混合精度、量化和大规模部署中的数值稳定性与可复现性。 |

## Evidence Policy

Venue status and source type are factual metadata. Technical tags summarize the system surface. Legacy imports are marked explicitly. Internal triage priority is a discovery signal, not a publication-quality ranking.

### Evidence Ladder

| Evidence layer | How it is used |
|---|---|
| **Formal venue** | Conference or journal identity confirmed; publication status is shown as metadata. |
| **Artifact / ecosystem** | A code, runtime, hardware, deployment, or production entry point is linked when available. |
| **Physical evaluation** | Real hardware or end-to-end serving evidence is preferred over algorithm-only simulation. |
| **Legacy import** | Imported during migration and retained for coverage; not an implicit quality ranking. |

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Add facts to JSONL and regenerate the Markdown views; do not edit generated tables directly.
