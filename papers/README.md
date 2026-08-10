# AI Inference Papers

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Industry systems](../industry/README.md)

A bounded academic reading view organized by serving-system abstraction. Complete facts remain in JSONL and the archive.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. A bounded rolling exploration section keeps new workloads visible; the full adjacent/archive history remains in the [archive](../archive/README.md).

## At a Glance

| Records | Formal venue | With artifact | Tagged records |
|---:|---:|---:|---:|
| 50 | 46 | 16 | 47 |

## Collection Navigation

- [Attention / Kernel](#attention-kernel) (6)
- [KV Cache](#kv-cache) (8)
- [Prefill–Decode 与传输](#prefill-decode) (8)
- [Speculative Decoding](#speculative-decoding) (8)
- [MoE](#moe) (8)
- [Compiler / DSL](#compiler-dsl) (4)
- [Runtime / Scheduling](#runtime-scheduling) (8)
- [探索观察](#探索观察) (15)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |
| Scope | `core` records form the seven main themes; a bounded `adjacent` window appears under exploration, with full adjacent/archive history on the archive page. |
| Featured | A small editorial starting set within the bounded core reading set; complete facts remain in JSONL and the archive. |

## Resource List

### Attention / Kernel (6)

#### Featured

- **Featured:** **[vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention](https://arxiv.org/abs/2405.04437)**
  `ASPLOS 2025` · `2025` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `serving` `cuda` `kernel` `memory`
  Artifact: [source](https://github.com/microsoft/vattention)
  vAttention 通过 CUDA virtual memory 保留连续虚拟 KV layout，同时按需分配物理页，避免重写 attention kernel。
- **Featured:** **[Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)**
  `SOSP 2023` · `2023` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `serving` `kv-cache` `memory` `vllm`
  Artifact: [source](https://github.com/vllm-project/vllm)
  vLLM/PagedAttention 用块式虚拟内存管理 KV cache，显著减少碎片并支持 beam search、parallel sampling 和前缀共享。
- **Featured:** **[FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision](https://arxiv.org/abs/2407.08608)**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint` · `Reading priority: foundation`
  Tags: `hopper` `kv-cache` `quantization`
  Artifact: [source](https://github.com/Dao-AILab/flash-attention)
  FlashAttention-3 利用 Hopper TMA、warp specialization 和 FP8 block quantization 重叠数据移动、matmul 与 softmax。
#### Full Resource List

- **FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kernel`
  FlashAttention-4 针对非对称硬件扩展重做 attention 算法和 kernel pipeline 协同设计，提高长上下文与大模型注意力吞吐。
- **I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  该工作从 I/O 复杂度而非 FLOPs 分析长序列 attention，指导算法与硬件在数据搬运瓶颈下协同优化。
- **FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kernel`
  FastTree 为 radix-tree KV 共享设计专用 attention kernel，并在 runtime 中自适应划分共享上下文查询组。

### KV Cache (8)

#### Full Resource List

- **A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints**
  `ICML 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  该工作把计算和 KV cache 显存同时纳入排队稳定性分析，给出 LLM inference 系统何时会因内存约束失稳的理论条件。
- **Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs**
  `ICLR 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  TRIM-KV 在 token 生成时预测长期保留价值，并随时间衰减以在固定内存预算下保留最有用的 KV。
- **[DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants](https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `npu` `kv-cache` `agent` `edge` `throughput`
  Compound AI systems, such as agentic systems, are an emerging trend in large-scale enterprise settings, with multiple LLMs specialized for different users, tasks, and/or roles working together. In these scenarios, different models often pr…
- **[ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs](https://www.usenix.org/conference/osdi26/presentation/liu-guangda)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `kv-cache`
  针对 native sparse attention 下随上下文增长的 KV 容量瓶颈，设计 GPU graph-friendly cache manager、无损 decode/prefill prefetch 和融合 GPU kernel；官方 OSDI 2026 页面报告长上下文下相对 SGLang/vLLM generation throughput 最高提升 2.1 倍。
- **[FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management](https://openreview.net/forum?id=GgX6dPJx9M)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `compression` `kv-cache` `rag`
  FlexiCache 利用 attention head 重要性的时间稳定性动态管理 KV cache，减少长上下文生成中不必要的保留和加载。
- **Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `quantization`
  Kitty 用动态 channel-wise precision boost 和 page-centric layout 实现接近 2-bit 的 KV cache 压缩，同时保持规则访存和解量化效率。
- **KV Cache Transform Coding for Compact Storage in LLM Inference**
  `ICLR 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `rag`
  KVTC 借鉴媒体压缩，用 PCA 去相关、自适应量化和熵编码压缩可复用 KV cache。
- **KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving**
  `SIGCOMM 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `compression` `kv-cache` `slo`
  KVServe 用 Bayesian profiling 建立压缩策略 Pareto 集，并由在线 controller 按 workload、网络、SLO 和质量约束选择 KV 传输压缩方案。

### Prefill–Decode 与传输 (8)

#### Featured

- **Featured:** **[DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin)**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `decode` `prefill` `gpu` `goodput` `tpot`
  Artifact: [source](https://github.com/LLMServe/DistServe)
  DistServe 将 prefill 和 decode 放到不同 GPU 上，并按 TTFT/TPOT 约束联合优化资源与并行策略。
#### Full Resource List

- **[P/D-Serve: Serving Disaggregated Large Language Model at Scale](https://arxiv.org/abs/2408.08147)**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint` · `Reading priority: foundation`
  Tags: `decode` `prefill` `slo`
  P/D-Serve 面向大规模商业部署，将 prefill/decode 组织、调度和 KVCache 传输做端到端优化，以提升分离式 LLM 服务吞吐和 SLO 表现。
- **Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `gpu` `kernel` `kv-cache` `moe` `slo`
  该工作用 stream-loading prefill、SmallEP、零拷贝 prefill/decode 分离和 CPU FP8 kernel，把本地 CPU-GPU 平台上的 MoE serving 拉近云端 SLO。
- **[ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping](https://www.usenix.org/conference/osdi26/presentation/liu-yao)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `decode` `gpu` `compiler` `compression` `tensorrt-llm` `throughput` `ttft`
  Artifact: [source](https://www.usenix.org/system/files/osdi26-liu-yao.pdf)
  ADAngel 用 DPR 模型生成多种混合精度 GEMM kernel，并通过 Oracle Policy Map 在运行时为任意 bit-width/shape 任务选择策略；相较 llama.cpp decode 吞吐最高提升 5.10x，相较 TensorRT-LLM prefill TTFT 提升 1.17x–2.38x。
- **[FaaScale: Unlocking Fast LLM Scaling for Serverless Inference](https://openreview.net/forum?id=jgL8LuOVyT)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `gpu` `rdma` `memory` `scheduler` `heterogeneous` `ttft`
  Artifact: [source](https://github.com/lambda-scale/lambda-scale)
  FaaScale 以 PipeCast 将模型分块 multicast 与跨节点 pipeline-parallel inference 协同，在模型传输尚未完成时即开始执行，并结合 GPU/host memory 管理应对突发 serverless 负载；真实 LLM traces 上 P90 TTFT 改善 2.4x–5x、GPU 成本降低 17.8%–31.3%。
- **[FlashAgents: Accelerating Multi-Agent LLM Systems via Streaming Prefill Overlap](https://openreview.net/pdf?id=m14PPUfgEc)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `agent` `rag`
  FlashAgents 用 agent 间 token streaming、增量 prefill 和 prefix-aware coordination 重叠多智能体调用链中的等待与计算。
- **From Tokens to Layers: Redefining Stall-Free Scheduling for LLM Serving with Layered Prefill**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `moe` `stall`
  该工作把 prefill 调度单位从 token chunk 改为 layer group，在 MoE serving 中减少重复 expert 权重加载并维持 stall-free decode。
- **[GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving](https://openreview.net/forum?id=xKjYiUgeOK)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `decode` `gpu` `compression` `kv-cache` `long-context` `agent` `latency`
  Artifact: [source](https://arxiv.org/abs/2605.00831)
  GhostServe 在 host memory 中以 erasure coding 为 streaming KV cache 生成 parity shards，故障时重建丢失 KV 状态并继续推理，避免完整重算或全量状态复制；单 batch checkpoint latency 最高降低 2.7x，recovery latency 降低 2.1x，中位响应延迟降低 1.2x。

### Speculative Decoding (8)

#### Featured

- **Featured:** **[Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads](https://proceedings.mlr.press/v235/cai24b.html)**
  `ICML 2024` · `2024` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `kv-cache`
  Artifact: [source](https://github.com/FasterDecoding/Medusa)
  Medusa 在目标模型上添加多个 decoding heads，无需独立 draft model 即可并行预测和验证多个未来 token。
#### Full Resource List

- **Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache`
  SparseSpec 以稀疏注意力版本的同一模型充当 draft，并联合调度 drafting、verification 和动态 KV 管理以加速长 CoT。
- **Beat the long tail: Distribution-Aware Speculative Decoding for RL Training**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `training`
  DAS 利用历史 rollout 维护非参数 drafter，并按轨迹长度分配 speculative budget，缩短 RL post-training 中长尾生成阶段。
- **DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `gpu` `kv-cache`
  DFVG 将 draft 放在 FPGA、verify 放在 GPU，以异构流水降低推测解码的草稿成本并提高验证硬件利用率。
- **NexSpec: Towards Optimizing Speculative Decoding in Reinforcement Learning Systems**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  NexSpec 针对 RL 系统中的 speculative decoding 动态调参、更新 drafter 并按 rollout reward 加权，缓解大 batch 和 actor 漂移下的加速失效。
- **SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  SpecDiff-2 用离散扩散模型作为非自回归 drafter，并校准 diffusion drafter 与自回归 verifier 的分布差异，以提升 speculative decoding 接受率和并行度。
- **Speculative Decoding: Performance or Illusion?**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving`
  该工作用真实 serving 条件重新评估 speculative decoding，区分离线 speedup 与在线负载下的端到端收益。
- **AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving**
  `SoCC 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `kv-cache` `slo`
  AdaSpec 根据请求 SLO、草稿成本和接受率动态选择 speculative decoding 配置。

### MoE (8)

#### Featured

- **Featured:** **[MegaBlocks: Efficient Sparse Training with Mixture-of-Experts](https://proceedings.mlsys.org/paper_files/paper/2023/hash/5a54f79333768effe7e8927bcccffe40-Abstract-mlsys2023.html)**
  `MLSys 2023` · `2023` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `routing` `training` `kernel` `moe`
  Artifact: [source](https://github.com/databricks/megablocks)
  MegaBlocks 把动态 token routing 转化为 block-sparse operation，避免 expert capacity padding；其 kernel 思路影响 MoE inference。
- **Featured:** **[Tutel: Adaptive Mixture-of-Experts at Scale](https://proceedings.mlsys.org/paper_files/paper/2023/hash/5616d34cf8ff73942cfd5aa922842556-Abstract-mlsys2023.html)**
  `MLSys 2023` · `2023` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `kernel` `moe`
  Artifact: [source](https://github.com/microsoft/Tutel)
  Tutel 以自适应并行、all-to-all 和 fused kernel 构建通用 MoE runtime。
- **Featured:** **[DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale](https://proceedings.mlr.press/v162/rajbhandari22a.html)**
  `ICML 2022` · `2022` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `training` `moe`
  Artifact: [source](https://github.com/microsoft/DeepSpeed)
  DeepSpeed-MoE 联合优化 expert parallel、通信和模型压缩，使大规模 MoE 同时具备训练和推理可行性。
#### Full Resource List

- **EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `moe`
  EARTH 根据 gating entropy 推测预取 expert 并复用结果，以降低 MoE expert 加载等待与误预取代价。
- **FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `moe` `quantization`
  FP8-Flow-MoE 为 MoE 设计避免重复量化误差的 FP8 执行配方，减少 expert 路径中的 cast 和量化开销。
- **LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `training` `moe`
  LAER-MoE 根据 expert 负载动态重排布局，属于与推理基础设施相邻的 MoE 训练系统工作。
- **MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `moe`
  MoE-APEX 根据 expert 热度和执行需求自适应选择精度与卸载方式，缓解 MoE 权重容量和传输瓶颈。
- **MoEBlaze: Breaking the Memory Wall for Efficient MoE Training on Modern GPUs**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `training` `gpu` `memory` `moe`
  MoEBlaze 针对现代 GPU 上 MoE 训练的显存墙优化 expert 参数、激活和通信组织，为大规模 MoE 系统提供训练侧基础设施。

### Compiler / DSL (4)

#### Featured

- **Featured:** **[FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `npu` `compiler` `kernel` `agent` `edge` `vllm`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-wu-bingyang.pdf)
  以输出 token 为粒度实现可抢占的分布式 LLM serving，提出 skip-join 多级反馈队列，并主动在 GPU/主机内存间搬运中间状态；官方 NSDI 2026 页面报告相对 vLLM 吞吐最高提升 6.1 倍。
#### Full Resource List

- **[Agentix: An Efficient Serving Engine for LLM Agents as General Programs](https://www.usenix.org/conference/nsdi26/presentation/luo)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `tpu` `compiler` `kernel` `agent` `rag` `vllm` `latency`
  把 agent 程序及其依赖的 LLM calls 作为 serving 调度的一等对象，利用已完成调用的程序级上下文进行抢占和优先级调度；官方 NSDI 2026 页面报告在相同延迟下，相比 vLLM 等系统程序吞吐提升 4–15 倍。
- **Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `compiler`
  Flashlight 扩展 PyTorch compiler 来支持 attention 变体加速，使新注意力算子更容易进入生产编译与执行路径。
- **ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `kernel`
  ParallelKittens 提供更系统的多 GPU kernel 编程与组合方式，降低跨 GPU LLM inference kernel 的实现复杂度。

### Runtime / Scheduling (8)

#### Featured

- **Featured:** **[FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `serving` `kernel`
  Artifact: [source](https://github.com/flashinfer-ai/flashinfer)
  FlashInfer 用 block-sparse/composable KV format、JIT attention template 和 load-balanced scheduling 提供 serving-oriented kernel。
- **Featured:** **[Llumnix: Dynamic Scheduling for Large Language Model Serving](https://www.usenix.org/conference/osdi24/presentation/sun-biao)**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `serving`
  Artifact: [source](https://github.com/AlibabaPAI/llumnix)
  Llumnix 通过请求及其 KV 状态的 live migration，在多实例间动态重调度以改善尾延迟、隔离和负载均衡。
- **Featured:** **BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu`
  BOute 用多目标贝叶斯优化在异构模型和 GPU 组合中选择 serving 配置，联合降低成本并满足质量和延迟目标。
#### Full Resource List

- **[MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool](https://arxiv.org/abs/2406.17565)**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint` · `Reading priority: foundation`
  Tags: `serving` `memory`
  MemServe 以 MemPool 统一管理跨实例分布式 KV，并联合 context caching、PD 分离和全局 locality-aware scheduling。
- **[SGLang: Efficient Execution of Structured Language Model Programs](https://arxiv.org/abs/2312.07104)**
  `NeurIPS 2024` · `2024` · `Research record` · `Unclassified` · `Reading priority: foundation`
  Tags: `serving` `agent` `rag` `sglang`
  Artifact: [source](https://github.com/sgl-project/sglang)
  SGLang 用 RadixAttention、结构化生成语言和高性能 runtime 统一优化多调用、共享前缀和约束生成工作流。
- **Breaking the Ice: Analyzing Cold Start Latency in vLLM**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `vllm` `latency`
  该工作拆解 vLLM 冷启动中的 CPU-bound 阶段并建立延迟模型，为 serverless LLM 的预热、调度和容量规划提供依据。
- **Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu`
  Bullet 在空间放置和时间调度两个维度动态编排 LLM 请求，以减少 GPU 碎片并提高服务利用率。
- **[DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems](https://openreview.net/forum?id=Xfzzp6grRP)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving`
  DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更。

### 探索观察

最近 180 天内有正式或工程证据、但尚未成为稳定主线的新语境工作。

- **AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `kernel` `agent`
  AccelOpt 将 LLM agent 用于 AI accelerator kernel 优化闭环，让生成、profile、修复和迭代搜索共同改进算子实现。
- **CDLM: CONSISTENCY DIFFUSION LANGUAGE MODELS FOR FASTER SAMPLING**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  CDLM 将 consistency/diffusion language model 的采样过程系统化加速，减少扩散式文本生成需要的迭代步数。
- **FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `edge`
  FastTTS 面向边缘设备优化 test-time scaling，使多次候选生成与验证能够在受限资源上高效执行。
- **[FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees](https://www.usenix.org/conference/nsdi26/presentation/oliaro)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `serving` `training` `gpu` `memory` `scheduler` `agent` `rag` `latency`
  Finetuning large language models (LLMs) is essential for task adaptation, yet today's serving stacks isolate inference and finetuning on separate GPU clusters—wasting resources and under-utilizing hardware. We introduce FlexLLM, the first…
- **[Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with Sereno](https://www.usenix.org/conference/osdi26/presentation/xin)**
  `OSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `memory`
  分析移动设备前台应用与 LLM 推理之间不对称的内存带宽干扰，利用 speculative decoding 提供可抢占 yield points，让推理动态让出带宽；官方 OSDI 2026 页面报告前台 jank rate 平均降低 58.5%、LLM throughput 平均提升 26.4%。
- **IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `edge`
  IntAttention 用整数域 IndexSoftmax 和端到端 INT8 attention pipeline 消除反量化-浮点 softmax-再量化路径，降低端侧延迟和能耗。
- **NodeSweep: Practical Straggler Detection and Health Monitoring for Large-Scale Foundation Model Training**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `training` `rag`
  NodeSweep 将在线性能监控与离线 node sweep 结合，识别传统 NCCL/burn-in 检查漏掉的慢节点，提升大规模基础模型训练集群稳定性。
- **Optimizing PyTorch Inference with LLM-Based Multi-Agent Systems**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `kernel` `agent`
  该工作系统比较 LLM 多智能体优化 PyTorch 推理代码的策略，用 KernelBench/H100 评估 agentic kernel tuning 对端到端推理性能的提升。
- **PROMPTS: PeRformance Optimization via Multi-Agent Planning for LLM Training and Serving**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `training` `agent`
  PROMPTS 用 analyzer/proposal 多智能体系统读取 profiler 数据并生成 sharding 配置，在训练和 serving workload 上自动提出系统级优化方案。
- **SAKURAONE: An Open Ethernet-Based AI HPC System and Its Observed Workload Dynamics in a Single-Tenant LLM Development Environment**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  SAKURAONE 报告开放以太网 AI HPC 系统及单租户 LLM 开发环境中的 workload dynamics，为非专有互连大模型集群提供生产参照。
- **[ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `serving` `multimodal`
  Artifact: [source](https://github.com/alibaba/ServeGen)
  基于全球云端生产 serving 服务，刻画语言、多模态和 reasoning 模型 workload，并按 client 组合生成更真实的 serving traces；官方 NSDI 2026 页面明确提供开源实现 https://github.com/alibaba/ServeGen。
- **TiDAR: Think in Diffusion, Talk in Autoregression**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kv-cache`
  TiDAR 在单次 forward 中用 diffusion draft 和 autoregressive sampling 结合生成，保留精确 KV cache 支持并提高 serving 吞吐。
- **db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `agent` `rag`
  db-SP 面向视觉生成模型的稀疏 attention 设计 dual-balanced sequence parallelism，降低长序列视觉生成中的负载不均和跨设备通信。
- **[Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access for LLM via Semantic-Aware Knowledge Caching](https://www.usenix.org/conference/nsdi26/presentation/ruan-cortex)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `memory` `agent` `rag` `latency` `throughput`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-ruan-cortex.pdf)
  Cortex 为 LLM agent 构建跨区域语义知识缓存，以 Semantic Element 和 Semantic Retrieval Index 支持语义命中、成本感知淘汰与主动预取；在代表性搜索任务上吞吐最高提升 3.6x，代码任务最高提升 20x，同时保持近似非缓存基线的准确率。
- **[ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler](https://openreview.net/forum?id=tYHWS7YPof)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `prefill` `decode` `edge` `gpu` `memory` `scheduler` `moe` `latency`
  Artifact: [source](https://arxiv.org/abs/2601.20755)
  ProfInfer 使用 eBPF 在不修改或重编译 llama.cpp 的情况下，对 token、计算图、算子和硬件计数器进行多粒度追踪，提供 ProfDAG、ProfTime、ProfStat 视图，覆盖 dense、MoE routing 与 offloading；在线开销低于 4%，用于定位内存/计算瓶颈和支持资源感知调度。
