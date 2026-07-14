# Awesome AI Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

A curated, evidence-aware collection of LLM inference serving papers and industrial systems.

This repository focuses on the serving mainline: runtime, P/D disaggregation, KV state, kernels, compilers, scheduling, reliability, and production infrastructure.

## Contents

- [Academic Papers](papers/README.md)
- [Industry & Open-Source Systems](industry/README.md)
- [Contribution Guide](CONTRIBUTING.md)

## Coverage

| Collection | Records | Evidence breakdown |
|---|---:|---|
| Academic papers | 432 | Formal Conference · Legacy Import: 178, Poster / Workshop · Legacy Import: 37, Preprint · Legacy Import: 160, Unclassified · Legacy Import: 57 |
| Industry / open-source systems | 120 | Industrial Material · Legacy Import: 120 |

## Taxonomy

- **KV State & Memory**: system-level techniques and evidence for the serving stack.
- **P/D Disaggregation & KV Transfer**: system-level techniques and evidence for the serving stack.
- **KV Compression & Low-Bit State**: system-level techniques and evidence for the serving stack.
- **Kernel & Compiler**: system-level techniques and evidence for the serving stack.
- **Runtime & Serving**: system-level techniques and evidence for the serving stack.
- **Reliability & Benchmarks**: system-level techniques and evidence for the serving stack.

## Featured Papers

- **A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs**<br>
  `ASPLOS 2026` · `Formal Conference · Legacy Import` · `long-context` `rag`<br>
  该工作把长上下文离线推理的数据密集部分下沉到近存储处理器，降低主机内存和 I/O 成本。
- **A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints**<br>
  `ICML 2026` · `Formal Conference · Legacy Import` · `kv-cache` `memory`<br>
  该工作把计算和 KV cache 显存同时纳入排队稳定性分析，给出 LLM inference 系统何时会因内存约束失稳的理论条件。
- **ADS: AN AGENTIC DETECTION SYSTEM FOR ENTERPRISE AGENTIC AI SECURITY**<br>
  `MLSys 2026` · `Formal Conference · Legacy Import` · `serving` `agent` `rag`<br>
  ADS 面向企业 agentic AI 安全构建检测系统，把 agent 行为、工具调用和安全策略纳入运行时监控。
- **AIRS: Scaling Live Inference in Resource Constrained Environments**<br>
  `MLSys 2026` · `Formal Conference · Legacy Import` · <br>
  AIRS 面向资源受限的在线推理流水线动态分配加速器与任务优先级，提高多阶段 LLM 评估/预测服务的吞吐和延迟稳定性。
- **Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding**<br>
  `MLSys 2026` · `Formal Conference · Legacy Import` · `kv-cache`<br>
  SparseSpec 以稀疏注意力版本的同一模型充当 draft，并联合调度 drafting、verification 和动态 KV 管理以加速长 CoT。
- **Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design**<br>
  `OSDI 2026` · `Formal Conference · Legacy Import` · `decode` `prefill` `gpu` `kernel` `kv-cache` `moe`<br>
  该工作用 stream-loading prefill、SmallEP、零拷贝 prefill/decode 分离和 CPU FP8 kernel，把本地 CPU-GPU 平台上的 MoE serving 拉近云端 SLO。
- **AgenticCache: Cache-Driven Asynchronous Planning for Embodied AI Agents**<br>
  `MLSys 2026` · `Formal Conference · Legacy Import` · `serving` `agent` `rag`<br>
  AgenticCache 用缓存命中和状态复用驱动 embodied agent 的异步规划，减少重复上下文构造和工具调用等待。
- **Agentix: An Efficient Serving Engine for LLM Agents as General Programs**<br>
  `NSDI 2026` · `Formal Conference · Legacy Import` · `serving` `agent` `rag`<br>
  Agentix 把 agent program 而非单次请求作为调度对象，利用程序依赖和已完成调用对后续 LLM call 抢占与提权。
- **BAT: Efficient Generative Recommender Serving with Bipartite Attention**<br>
  `ASPLOS 2026` · `Formal Conference · Legacy Import` · `serving`<br>
  BAT 为生成式推荐设计 bipartite attention 和相应 serving 路径，减少推荐上下文与生成阶段的冗余计算。
- **BEAM: Joint Resource-Power Optimization for Energy-Efficient LLM Inference under SLO constraints**<br>
  `MLSys 2026` · `Formal Conference · Legacy Import` · `slo`<br>
  BEAM 联合选择资源分配和功耗状态，在满足 SLO 的同时降低 LLM inference 的能耗。
- **BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding**<br>
  `MLSys 2026` · `Formal Conference · Legacy Import` · `decode` `prefill`<br>
  BLASST 在 online softmax 中按阈值动态跳过低贡献 attention block，减少 Value block 加载和后续矩阵乘法以加速长上下文 prefill/decode。
- **BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization**<br>
  `MLSys 2026` · `Formal Conference · Legacy Import` · `serving` `gpu`<br>
  BOute 用多目标贝叶斯优化在异构模型和 GPU 组合中选择 serving 配置，联合降低成本并满足质量和延迟目标。

## Featured Industry Systems

- **[AI200 / AI250](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-unveils-ai200-and-ai250-ai-inference-accelerators-hexagon-takes-on-amd-and-nvidia-in-the-booming-data-center-realm)**<br>
  `Qualcomm` · `2026` · `Industrial Material · Legacy Import` · `npu` `memory`<br>
  将 Hexagon NPU 扩展到数据中心，强调大容量 LPDDR、低比特格式、near-memory compute、机架扩展和 disaggregated inference。
- **[ATOM inference engine](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html)**<br>
  `AMD ROCm` · `2026` · `Industrial Material · Legacy Import` · `serving` `amd` `rocm` `kernel` `moe` `moe`<br>
  以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。
- **[ATOMesh distributed serving gateway](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html)**<br>
  `AMD ROCm` · `2026` · `Industrial Material · Legacy Import` · `decode` `prefill` `amd` `gpu` `routing` `sglang`<br>
  作为 AMD GPU 集群的分布式推理控制面，统一 prefill/decode routing、KV-aware scheduling、worker lifecycle、retries、observability，并协调 ATOM、vLLM、SGLang 后端。
- **[BlueField-4 STX / context memory storage](https://www.tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai)**<br>
  `NVIDIA` · `2026` · `Industrial Material · Legacy Import` · `kv-cache` `memory` `agent` `rag`<br>
  用 DPU/加速存储绕过 host CPU，把长上下文 KV cache 放到近存储路径，面向 agentic AI 的大上下文状态。
- **[DroidSpeak](https://www.microsoft.com/en-us/research/publication/droidspeak-kv-cache-sharing-for-efficient-multi-llm-serving/)**<br>
  `Microsoft Research` · `2026` · `Industrial Material · Legacy Import` · `prefill` `serving` `kv-cache` `agent`<br>
  在相同架构的 fine-tuned model variants 之间共享 KV cache，降低企业多模型/多 agent 的重复 prefill。
- **[Dynamo 1.0 Production-Scale Multi-Node Inference](https://developer.nvidia.com/blog/?p=113961)**<br>
  `NVIDIA` · `2026` · `Industrial Material · Legacy Import` · `routing` `routing` `agent` `multimodal` `kubernetes`<br>
  Dynamo 1.0 强化多节点部署、Kubernetes 编排、agentic/multimodal KV routing、ModelExpress 快速启动和 KV Block Manager。
- **[Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm)**<br>
  `NVIDIA` · `2026` · `Industrial Material · Legacy Import` · `memory` `tensorrt-llm` `vllm`<br>
  KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。
- **[Dynamo Snapshot](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/)**<br>
  `NVIDIA` · `2026` · `Industrial Material · Legacy Import` · `cuda` `kv-cache` `kubernetes`<br>
  用 CRIU + cuda-checkpoint 做 Kubernetes 上推理 worker 快照恢复，并通过 KV cache unmap 减小 checkpoint 体积。
- **[FlexKV](https://github.com/taco-project/FlexKV)**<br>
  `Tencent Cloud TACO + NVIDIA` · `2026` · `Industrial Material · Legacy Import` · `sglang` `vllm`<br>
  分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。
- **[Full-Stack Optimizations for Agentic Inference with Dynamo](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/)**<br>
  `NVIDIA` · `2026` · `Industrial Material · Legacy Import` · `agent`<br>
  针对 coding agent / multi-agent 的 write-once-read-many KV 模式，强调 router、cache pinning、ephemeral KV block 生命周期和 agent-native KV 管理。
- **[Gemma 4 on vLLM-TPU](https://arxiv.org/abs/2605.25645)**<br>
  `Google TPU ecosystem` · `2026` · `Industrial Material · Legacy Import` · `serving` `gpu` `tpu` `vllm`<br>
  展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。
- **[KEEP](https://www.microsoft.com/en-us/research/publication/keep-a-kv-cache-centric-memory-management-system-for-efficient-embodied-planning/)**<br>
  `Microsoft Research` · `2026` · `Industrial Material · Legacy Import` · `kv-cache` `memory`<br>
  Embodied planning 中用 KV-cache-centric memory management 替代原始文本记忆，减少频繁 KV 更新和重算。

## Evidence Policy

Venue status and source type are factual metadata. Technical tags summarize the system surface. Internal triage priority is not a publication-quality ranking and is not shown here.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.
