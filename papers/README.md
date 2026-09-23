# AI Inference Papers

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Industry systems](../industry/README.md)

A complete academic paper collection organized by serving-system abstraction. Formal venues, posters/workshops, preprints, and legacy imports are labeled separately.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. A bounded rolling exploration section keeps new workloads visible; the full adjacent/archive history remains in the [archive](../archive/README.md).

## At a Glance

| Records | Formal venue | With artifact | Tagged records |
|---:|---:|---:|---:|
| 63 | 52 | 4 | 57 |

## Collection Navigation

- [Attention / Kernel](#attention-kernel) (7)
- [KV Cache](#kv-cache) (8)
- [Prefill–Decode 与传输](#prefill-decode) (8)
- [Speculative Decoding](#speculative-decoding) (8)
- [MoE](#moe) (8)
- [Compiler / DSL](#compiler-dsl) (8)
- [Runtime / Scheduling](#runtime-scheduling) (8)
- [奠基与架构 / Foundation](#foundation) (8)
- [探索观察](#探索观察) (15)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |
| Scope | `core` records form the main reading themes; a bounded `adjacent` window appears under exploration, with full adjacent/archive history on the archive page. |
| Featured | A small editorial starting set within the bounded core reading set; complete facts remain in JSONL and the archive. |

## Resource List

### Attention / Kernel (7)

#### Featured

- **Featured:** **vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention**
  `ASPLOS 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `cuda` `kernel` `memory`
  vAttention 通过 CUDA virtual memory 保留连续虚拟 KV layout，同时按需分配物理页，避免重写 attention kernel。
#### Full Resource List

- **[FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691)**
  `ICLR 2024` · `2024` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `gpu`
  在 FA1 的 IO 优化之上改进 thread-block 与 warp 级工作划分，进一步提升 GPU 利用率。
- **Efficient Memory Management for Large Language Model Serving with PagedAttention**
  `SOSP 2023` · `2023` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kv-cache` `memory` `vllm`
  vLLM/PagedAttention 用块式虚拟内存管理 KV cache，显著减少碎片并支持 beam search、parallel sampling 和前缀共享。
- **[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)**
  `NeurIPS 2022` · `2022` · `Research record` · `Unclassified` · `Reading priority: foundation`
  Tags: `kernel` `memory`
  提出 IO-aware 的精确 attention，用 tiling 把 HBM 与 SRAM 之间的数据搬移降到最低，attention kernel 的真正根节点。
- **FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kernel`
  FlashAttention-4 针对非对称硬件扩展重做 attention 算法和 kernel pipeline 协同设计，提高长上下文与大模型注意力吞吐。
- **I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention**
  `ASPLOS 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  该工作从 I/O 复杂度而非 FLOPs 分析长序列 attention，指导算法与硬件在数据搬运瓶颈下协同优化。
- **[HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference](https://arxiv.org/abs/2607.04302v1)**
  `arXiv AI infrastructure query` · `2026` · `Research record` · `Preprint` · `Reading priority: frontier`
  Tags: `training` `npu` `tpu` `compiler` `compression` `edge` `latency`
  HiFA4 在昇腾 HIF4 NPU 上把 FlashAttention 的 QK^T 与 PV 以 4-bit HIF4 Cube GEMM 执行（softmax 保持 FP16），借 Smooth-QK 逐通道重标定与 P-Reordering 降量化漂移；Qwen3-8B 上恢复 37.5% 精度差距、MMLU 损失从 1.12pp 收到 0.70pp、回归数减 57%，关键路径延迟预计降 35.4%。

### KV Cache (8)

#### Full Resource List

- **InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `kv-cache` `memory`
  InfiniGen 用少量 rehearsal 预测下一层重要 KV，仅从 host memory 预取必要状态以加速 offloaded inference。
- **Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `long-context`
  Infinite-LLM 将 attention layer 解耦并使用 pooled distributed KVCache，支撑最长约两百万 token 的弹性服务。
- **Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving**
  `FAST 2025` · `2025` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: foundation`
  Tags: `serving`
  Mooncake 以 KVCache 为中心构建分离式 LLM serving 架构，利用 CPU/DRAM/SSD/NIC 资源扩展在线长上下文服务能力。
- **A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints**
  `ICML 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  该工作把计算和 KV cache 显存同时纳入排队稳定性分析，给出 LLM inference 系统何时会因内存约束失稳的理论条件。
- **[ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning](https://icml.cc/virtual/2026/poster/63539)**
  `ICML 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  ArborKV（ICML 2026）利用推理任务本身的树状结构来组织 KV cache，对树中共享前缀做复用、对分支节点有选择地保留与回收，以在分支式（tree-based）LLM 推理中提升显存效率与吞吐。
- **Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs**
  `ICLR 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  TRIM-KV 在 token 生成时预测长期保留价值，并随时间衰减以在固定内存预算下保留最有用的 KV。
- **[DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants](https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `prefill` `serving` `npu` `kv-cache` `agent` `edge` `throughput`
  DroidSpeak 是首个跨不同 LLM（同架构）复用前缀 KV cache 的分布式推理系统：选择性重算另一模型产生的少数层、复用其余层，并以流水线叠加重算与加载；相较不允许跨模型共享的基线最高提升 4× 吞吐、prefill（TTFT）快约 3.1×，质量损失可忽略。
- **[ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs](https://www.usenix.org/conference/osdi26/presentation/liu-guangda)**
  `USENIX OSDI 2026 technical sessions` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `kv-cache`
  ECHO 为原生稀疏注意力 LLM 设计 KV 卸载服务系统：图友好缓存管理器在 GPU graph 内动态淘汰/召回 KV，并以无损的查询内（decode）与查询间（prefill）预取配合融合 kernel 把召回开销与索引计算重叠；长上下文下生成吞吐比 SGLang/vLLM 高至多 2.1×、轻载延迟相当。

### Prefill–Decode 与传输 (8)

#### Featured

- **Featured:** **CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion**
  `EuroSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `serving` `edge` `rag`
  CacheBlend 复用非前缀知识片段的预计算 KV，并用知识融合机制降低 RAG prefill 延迟。
- **Featured:** **Context Parallelism for Scalable Million-Token Inference**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill`
  该工作用 pass-KV/pass-Q 两种精确 ring attention 在 128 张 H100 上扩展百万 token prefill 和 persistent-KV decode。
- **Featured:** **DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `gpu` `goodput` `tpot`
  DistServe 将 prefill 和 decode 放到不同 GPU 上，并按 TTFT/TPOT 约束联合优化资源与并行策略。
#### Full Resource List

- **Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `latency` `stall`
  Sarathi-Serve 用 chunked prefill 和 stall-free scheduling 缓解 prefill/decode 混批中的吞吐-延迟冲突。
- **MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill`
  MuxServe 结合模型流行度、空间共置和 prefill/decode 时间复用，提高多模型 serving 的显存与算力利用率。
- **[Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150)**
  `arXiv 2019` · `2019` · `Research record` · `Preprint` · `Reading priority: foundation`
  Tags: `decode`
  提出 Multi-Query Attention，只保留单个 KV head，直接从 decode 阶段的 KV 读取带宽瓶颈出发做优化。
- **[Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://www.usenix.org/conference/osdi26/presentation/wang-wenxin)**
  `USENIX OSDI 2026 technical sessions` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `prefill` `gpu` `kernel` `kv-cache` `moe` `slo`
  该 CPU-GPU 混合方案以流式/分布式加载 prefill（1200、1800 tokens/s）、节点内 P/D 分离与双批 overlap（延迟增 <15%、吞吐 +50%）、AVX-512 FP8 GEMV（CPU 延迟降 4–5×）和细粒度 CPU 并行（INT4 DeepSeek-V3 达 28 tokens/s）在消费级平台达成云级 SLO。
- **[AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving](https://dl.acm.org/doi/10.1145/3767295.3769345)**
  `EuroSys 2026 official accepted papers` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `decode` `prefill` `scheduler` `latency` `slo`
  根据 prefill/decode 长度分类请求，逐步优化实例间 compute layout、负载平衡和选择性分布式执行，并用仿真估计器避免实际执行开销；基于生产工作负载评测，报告 SLO attainment 最高提升 3.6 倍、成本效率提升 2 倍。

### Speculative Decoding (8)

#### Full Resource List

- **Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads**
  `ICML 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `kv-cache`
  Medusa 在目标模型上添加多个 decoding heads，无需独立 draft model 即可并行预测和验证多个未来 token。
- **[Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)**
  `ICML 2023` · `2023` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  提出 draft 模型 + 并行验证的投机解码，在不改变目标分布的前提下加速生成。
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
- **[PRISM: Parametrically Refactor Inference for Speculative Decoding Draft Models](https://openreview.net/forum?id=cvU2HuuxEf)**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `throughput`
  PRISM（MLSys 2026）对 speculative decoding 中的 draft 模型推理做参数化重构，在保持验证阶段正确性的前提下降低草稿生成的算力与延迟开销，从而提升草稿生成效率与验证吞吐量。
- **SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  SpecDiff-2 用离散扩散模型作为非自回归 drafter，并校准 diffusion drafter 与自回归 verifier 的分布差异，以提升 speculative decoding 接受率和并行度。

### MoE (8)

#### Featured

- **Featured:** **KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models**
  `SOSP 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `gpu` `kernel` `moe`
  KTransformers 把活跃 expert、attention 与其他算子分配到 CPU/GPU，并用定制 kernel 提升本地 MoE 推理。
#### Full Resource List

- **MegaBlocks: Efficient Sparse Training with Mixture-of-Experts**
  `MLSys 2023` · `2023` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `routing` `training` `kernel` `moe`
  MegaBlocks 把动态 token routing 转化为 block-sparse operation，避免 expert capacity padding；其 kernel 思路影响 MoE inference。
- **Tutel: Adaptive Mixture-of-Experts at Scale**
  `MLSys 2023` · `2023` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `kernel` `moe`
  Tutel 以自适应并行、all-to-all 和 fused kernel 构建通用 MoE runtime。
- **DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale**
  `ICML 2022` · `2022` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `training` `moe`
  DeepSpeed-MoE 联合优化 expert parallel、通信和模型压缩，使大规模 MoE 同时具备训练和推理可行性。
- **[GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding](https://arxiv.org/abs/2006.16668)**
  `ICLR 2020/2021` · `2021` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `moe`
  把 MoE 条件计算与自动分片结合，给出稀疏专家模型在分布式集群上的执行方案。
- **[Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)**
  `ICLR 2017` · `2017` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `moe` `rag`
  提出稀疏门控 MoE 层，用条件计算让参数量扩到极大规模而单样本计算量近似不变。
- **[Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961)**
  `JMLR 2021/2022` · `2022` · `Research record` · `Unclassified` · `Reading priority: foundation`
  Tags: `moe`
  用 top-1 路由大幅简化 MoE，把稀疏模型规模推到万亿参数级别。
- **[BatchGen: An Architecture for Scalable and Efficient Batch Inference](https://www.usenix.org/conference/osdi26/presentation/xu-tairan)**
  `USENIX OSDI 2026 technical sessions` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `scheduler` `memory` `moe` `heterogeneous` `throughput`
  Artifact: [source](https://www.usenix.org/system/files/osdi26-xu-tairan.pdf)
  BatchGen 以「序列协程」计算模型把每条序列表示为细粒度事件驱动协程，让运行时动态重组工作（更大专家级 batch、缓解掉队、跨设备重分配），在 128-GPU 集群上把批完成时间最多缩短 2.3×，在内存受限加速器上比最强卸载基线快至多 9.6×。

### Compiler / DSL (8)

#### Featured

- **Featured:** **[FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `npu` `compiler` `kernel` `agent` `edge` `vllm`
  Artifact: [source](https://www.usenix.org/system/files/nsdi26-wu-bingyang.pdf)
  以输出 token 为粒度实现可抢占的分布式 LLM serving，提出 skip-join 多级反馈队列，并主动在 GPU/主机内存间搬运中间状态；官方 NSDI 2026 页面报告相对 vLLM 吞吐最高提升 6.1 倍。
#### Full Resource List

- **[Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations](https://doi.org/10.1145/3315508.3329973)**
  `MAPL/PLDI 2019` · `2019` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `gpu` `compiler` `kernel`
  提出 tile 级 GPU kernel 编程语言与编译优化流水线，是现代 AI kernel DSL 的关键源头。
- **[TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://arxiv.org/abs/1802.04799)**
  `OSDI 2018` · `2018` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `compiler`
  端到端深度学习编译器，把图级优化与算子级调度分离，让同一模型可移植到多样硬件。
- **Punica: Multi-Tenant LoRA Serving**
  `arXiv 预印本, 2023/持续使用` · `2023` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `cuda` `kernel`
  Punica 用 heterogeneous batching CUDA kernel 和共享 base model 支撑多租户 LoRA serving。
- **LightSeq: A High Performance Inference Library for Transformers**
  `NAACL 2021 System Demonstrations` · `2021` · `Research record` · `Unclassified · Legacy Import` · `Reading priority: foundation`
  Tags: `cuda` `kernel`
  LightSeq 通过 layer fusion、定制 CUDA kernel 和显存复用提供 Transformer 推理库。
- **[Agentix: An Efficient Serving Engine for LLM Agents as General Programs](https://www.usenix.org/conference/nsdi26/presentation/luo)**
  `NSDI 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `tpu` `compiler` `kernel` `agent` `rag` `vllm` `latency`
  把 agent 程序及其依赖的 LLM calls 作为 serving 调度的一等对象，利用已完成调用的程序级上下文进行抢占和优先级调度；官方 NSDI 2026 页面报告在相同延迟下，相比 vLLM 等系统程序吞吐提升 4–15 倍。
- **Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants**
  `MLSys 2026` · `2026` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: frontier`
  Tags: `compiler`
  Flashlight 扩展 PyTorch compiler 来支持 attention 变体加速，使新注意力算子更容易进入生产编译与执行路径。
- **[MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs](https://www.usenix.org/conference/osdi26/presentation/cheng)**
  `USENIX OSDI 2026 technical sessions` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: frontier`
  Tags: `serving` `gpu` `compiler` `kernel` `rag` `latency`
  Artifact: [source](https://github.com/mirage-project/mirage)
  MPK 用 SM 级图表示把多 GPU 推理编译为单一 mega-kernel，实现跨算子软件流水与计算-通信重叠，并以持久内核内运行时执行，端到端 latency 降低至多 1.7×。

### Runtime / Scheduling (8)

#### Featured

- **Featured:** **FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kernel`
  FlashInfer 用 block-sparse/composable KV format、JIT attention template 和 load-balanced scheduling 提供 serving-oriented kernel。
- **Featured:** **QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kv-cache` `quantization`
  QServe 联合 W4A8KV4 量化、SmoothAttention、权重重排和寄存器级并行，将理论低比特节省转成云端 serving 吞吐。
- **Featured:** **DejaVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving**
  `ICML 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kv-cache`
  DejaVu 用 KV-cache streaming 支持 prompt-token 分离、microbatch swapping 和状态复制，缓解流水线空泡、显存过配和故障恢复问题。
#### Full Resource List

- **Llumnix: Dynamic Scheduling for Large Language Model Serving**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving`
  Llumnix 通过请求及其 KV 状态的 live migration，在多实例间动态重调度以改善尾延迟、隔离和负载均衡。
- **ServerlessLLM: Low-Latency Serverless Inference for Large Language Models**
  `OSDI 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `gpu` `latency`
  ServerlessLLM 利用近 GPU 多层存储、快速 checkpoint loading 和 live migration 降低 serverless LLM 冷启动延迟。
- **Taming the Titans: A Survey of Efficient LLM Inference Serving**
  `arXiv 综述, 2025` · `2025` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `serving`
  该综述按 instance、cluster 和新兴应用场景系统整理模型放置、调度、存储、分离架构及云端策略。
- **BurstGPT: A Real-world Workload Dataset to Optimize LLM Serving Systems**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `serving`
  BurstGPT 发布 Azure OpenAI 服务的五百余万条真实 trace，揭示 burst、长度和失败模式对调度评估的影响。
- **Preble: Efficient Distributed Prompt Scheduling for LLM Serving**
  `arXiv 预印本, 2024` · `2024` · `Research record` · `Preprint · Legacy Import` · `Reading priority: foundation`
  Tags: `serving`
  Preble 在分布式集群中联合优化共享前缀 KV 复用和计算负载均衡，并用分层调度处理 prompt locality。

### 奠基与架构 / Foundation (8)

#### Featured

- **Featured:** **NanoFlow: Towards Optimal Large Language Model Serving Throughput**
  `OSDI 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `gpu` `memory` `throughput`
  NanoFlow 将请求拆成 operation-level nano-batches，并在单 GPU 内重叠 compute、memory 和 network 资源。
- **Featured:** **XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models**
  `MLSys 2025` · `2025` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `gpu` `agent` `rag`
  XGrammar 预处理上下文无关 token、压缩运行时 grammar 状态，并与 GPU 推理重叠以实现近零开销结构化生成。
- **Featured:** **[AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978)**
  `MLSys 2024` · `2024` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  Tags: `compression` `kv-cache`
  提出激活感知的权重量化，只保护少量显著通道即可显著降低量化误差，部署侧被广泛采用。
#### Full Resource List

- **EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty**
  `ICML 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  EAGLE 在倒数第二层 feature space 中自回归预测草稿，降低 token-level drafting 的不确定性和开销。
- **[Efficient Streaming Language Models with Attention Sinks](https://arxiv.org/abs/2309.17453)**
  `ICLR 2024` · `2024` · `Academic paper` · `Formal Conference` · `Reading priority: foundation`
  发现 attention sink 现象并用有界 KV 维持流式长上下文，使显存不随序列长度增长。
- **Prompt Cache: Modular Attention Reuse for Low-Latency Inference**
  `MLSys 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `latency` `ttft`
  Prompt Cache 用显式 prompt module schema 预计算并复用非连续文本模块的 attention state，降低长提示 TTFT。
- **S-LoRA: Serving Thousands of Concurrent LoRA Adapters**
  `MLSys 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kernel`
  S-LoRA 用 unified paging、异构 LoRA kernel 和 tensor parallelism 在单集群中服务数千 adapter。
- **SpecInfer: Accelerating Generative Large Language Model Serving with Tree-based Speculative Inference and Verification**
  `ASPLOS 2024` · `2024` · `Academic paper` · `Formal Conference · Legacy Import` · `Reading priority: foundation`
  Tags: `serving`
  SpecInfer 用多个小模型构造候选 token tree，并由目标模型一次并行验证多条生成路径。

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
  FlexLLM 首个在共享 GPU 上以 token 级融合共服务 LLM 推理与 PEFT 微调：静态编译（依赖并行、图剪枝）把激活内存最多降 80%，混合 token 调度在每轮内交错推理与训练 token，在 20 req/s 下仍满足推理 SLO，微调吞吐在重/轻负载下分别提升 1.9×–4.8×/2.5×–6.8×。
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
- **[ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference](https://www.sigmobile.org/mobisys/2026/program/#shadownpu-system-and-algorithm-co-design-for-npu-centric-on-device-llm-inference)**
  `MobiSys 2026` · `2026` · `Academic paper` · `Formal Conference` · `Reading priority: supporting`
  Tags: `prefill` `decode` `npu` `edge` `kernel` `quantization` `latency` `throughput`
  Artifact: [source](https://www.sigmobile.org/mobisys/2026/program/)
  ShadowNPU 将 attention 重要性估计放到 Qualcomm Hexagon NPU 上以 INT8 执行，再把重要 token 索引交给 CPU/GPU 做稀疏高精度 attention，并配合 NPU compute-graph bucketing、head-wise pipeline 和细粒度 sparsity；MobiSys 评审报告端到端最高 4.5x 加速、能耗最高降低 7.7x，精度损失 0.4 个百分点。
