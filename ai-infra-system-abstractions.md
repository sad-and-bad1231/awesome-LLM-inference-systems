# AI Infra System Abstractions

<!-- generated from data/papers.jsonl, data/industry.jsonl, or data/candidates.jsonl; do not edit directly -->

主视图只保留结构、统计和代表条目；公开全量入口见 `papers/README.md` 和 `industry/README.md`，机器事实源见 JSONL。

## Reading Entry Points

| Need | File |
|---|---|
| 按系统抽象快速定位方向 | `ai-infra-system-abstractions.md` |
| 查 verified 学术论文全量明细 | `papers/README.md` |
| 查工业界/开源系统全量明细 | `industry/README.md` |
| 查待处理候选 | `ai-infra-candidates.md` |
| 机器可读论文事实源 | `data/papers.jsonl` |
| 机器可读工业事实源 | `data/industry.jsonl` |
| 候选 staging | `data/candidates.jsonl` |

## Coverage

| System Abstraction | Total | Papers | Industry/Projects | Candidates | Scope |
|---|---:|---:|---:|---:|---|
| Memory Topology & Virtualization | 114 | 91 | 18 | 5 | KV cache、long-context state、offload、prefix/RAG cache、CXL/分层内存。 |
| Disaggregated Interconnects | 332 | 85 | 13 | 234 | P/D 分离、KV transfer、RDMA/NIXL/UCCL、collective 和跨节点路由。 |
| State Compression & Signal Coding | 438 | 184 | 11 | 243 | 低比特 KV、MLA latent、稀疏/量化/编码压缩与质量-成本权衡。 |
| Execution Compilation & Kernel Fusion | 165 | 42 | 13 | 110 | Triton/CUDA/HIP kernel、attention/GEMM/MoE 算子、编译和硬件后端。 |
| Program-Aware Scheduling | 84 | 63 | 9 | 12 | agent graph、structured generation、多阶段工作流和程序感知调度。 |
| SRE/Fault-Tolerance/Sparing | 18 | 11 | 2 | 5 | trace/benchmark、SLO、故障恢复、漂移、数值稳定性和生产降级。 |

## SRE Metrics To Track

| Metric | Meaning |
|---|---|
| TTFT under Drift | 基础设施漂移、广域网抖动、Spot 节点切换时的首 token 延迟恶化边界。 |
| Generation Stall Rate | 推测解码验证失败、MoE all-to-all 热点或 tool-call 挂起造成的生成中断率。 |
| Numerical Reproducibility | 低精度混合量化、scale search 和异构执行导致的数值不稳定与非确定性。 |

## Representative Items

### Memory Topology & Virtualization

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving | paper | 2026 | AdaCache combines cache-aware partial recomputation with adaptive retrieval depth for RAG serving, reducing redundant long-input processing while preserving generation quality. | [phase:prefill,serving] [hardware:npu] [workload:agent,rag] |
| ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning | paper | 2026 | ArborKV manages KV cache using the tree structure of reasoning workloads, targeting reuse and memory efficiency for branching LLM inference. | [optimization_layer:kv-cache,memory] |
| Beyond Prediction: Tail-Aware Scheduling for LLM Inference | paper | 2026 | Beyond Prediction 用分布感知而非长度预测的调度与 cache-aware preemption 联合优化在线 LLM serving 的 TTFT 和尾延迟。 | [phase:serving] [metrics:ttft] |
| Decouple and Cache: KV Cache Construction for Streaming Video Understanding | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] [workload:video] |
| DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants | paper | 2026 | Compound AI systems, such as agentic systems, are an emerging trend in large-scale enterprise settings, with multiple LLMs specialized for different users, tasks, and/or roles working together. In these scenarios, different models often process inputs that share the same context prefix. Although much work was done in the past to enable the reuse of prefix KV caches across inputs for a single model, how to enable one model to reuse the prefix KV caches of a different model remains an open question. We introduce DroidSpeak, the first distributed LLM inference system that enables KV cache reuse across distributed nodes running inference of different LLMs, so long as the LLMs have the same architecture. We present the first study that aims at understanding the impact of sharing KV caches across different LLMs, and if/when such sharing affects quality. Inspired by the findings, we present DroidSpeak, which selectively recomputes a few layers of the KV cache produced by another LLM and reuses the remaining layers, with negligible quality loss. Moreover, carefully pipelining the layer-wise re-computation and the loading of reused KV cache further improves the inference performance. Experiments on diverse datasets and model pairs demonstrate that DroidSpeak achieves up to 4x throughput improvement and about 3.1× faster prefill (time to first token), with negligible loss of quality in F1 scores, Rouge-L or code similarity score, compared to the baseline which does not allow any sharing across models. | [phase:prefill,serving] [hardware:npu] [optimization_layer:kv-cache] [workload:agent,edge,rag] |
| ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs | paper | 2026 | 针对 native sparse attention 下随上下文增长的 KV 容量瓶颈，设计 GPU graph-friendly cache manager、无损 decode/prefill prefetch 和融合 GPU kernel；官方 OSDI 2026 页面报告长上下文下相对 SGLang/vLLM generation throughput 最高提升 2.1 倍。 | [phase:serving] [optimization_layer:kv-cache] |
| EpiCache: Episodic KV Cache Management for Long-Term Conversation on Resource-Constrained Environments | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |
| FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference | paper | 2026 | 以输出 token 为粒度实现可抢占的分布式 LLM serving，提出 skip-join 多级反馈队列，并主动在 GPU/主机内存间搬运中间状态；官方 NSDI 2026 页面报告相对 vLLM 吞吐最高提升 6.1 倍。 | [phase:serving] [hardware:gpu,npu,tpu] [optimization_layer:compiler,kernel,memory] [workload:agent,edge,rag] |
| FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management | paper | 2026 | FlexiCache 利用 attention head 重要性的时间稳定性动态管理 KV cache，减少长上下文生成中不必要的保留和加载。 | [optimization_layer:compression,kv-cache] [workload:rag] |
| ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |
| FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference | paper | 2026 | FreeKV moves KV selection off the critical path with speculative retrieval, hybrid CPU/GPU layouts, and double-buffered streaming, reporting up to 13x speedup with near-lossless quality. | [phase:serving] [hardware:gpu] [optimization_layer:compiler,kernel,kv-cache] |
| HiServe: A Prefix Cache Serving System for Hybrid LLMs | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] |

### Disaggregated Interconnects

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| ARKV: Adaptive Resource-Efficient KV Cache Management for Long Context LLM Inference under Memory Constraints | paper | 2026 | CCGrid 2026 official program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache,memory] [workload:edge,long-context] |
| BYSTANDER: State-Aware Execution-Time Prediction for Heterogeneous LLM Inference Scheduling | paper | 2026 | IEEE CLOUD 2026 official conference program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,rag] |
| Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding | paper | 2026 | Authors: Soongyu Choi (KAIST), Yuntae Kim (KAIST), Muyoung Son (KAIST), Joo-Young Kim (KAIST) | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| ConServe: Contiguity-Preserving Memory Management for Multi-Turn LLM Serving | paper | 2026 | Authors: Bingyao Li (University of California, Riverside) | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Connex: Endpoint Mobility Primitives for Dynamic LLM Serving | paper | 2026 | ACM SIGCOMM 2026 accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,kernel] |
| DIAMoND: Dynamic Inference for Adaptive Edge MoE with Heterogeneous In-NAND and Near-DRAM Compute Architecture | paper | 2026 | Authors: Ling Liang (Peking University), Tianyang Luo (Peking University), Shuzhang Zhong (Peking University), Dongxue Zhao (Peking University), Qichao Ma (Peking University), Renjie Wei (Peking University), Jingyu Wang (Xiaomi Corporation), Meng Li (Peking University), Guangyu Sun (Peking University), Zongwei Wang (Peking University), Yimao Cai (Peking University) | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| DoMoE: Domain-Aware Semantic Expert Prediction for Efficient MoE Inference Under Expert Offloading | paper | 2026 | IJCAI-ECAI 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression,moe] [workload:agent,edge,moe] |
| Dynamo-MoE: Accelerating Sparse Large Model Inference | paper | 2026 | HPDC 2026 official program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| DynoPipe: Heterogeneous Edge-Cloud LLM Serving with Dynamically Orchestrated Pipeline Boundaries | paper | 2026 | Authors: Yanying Lin (University of Chinese Academy of Sciences, UCSD), Baicheng Chen (University of California San Diego), Xinyu Zhang (University of California San Diego), Chengzhong Xu (University of Macau), Kejiang Ye (Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences) | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Efficient KV Cache Migration for Geo-Distributed LLM Inference in Collaborative Edge Computing | paper | 2026 | Authors: Mingjin Zhang, Jiannong Cao, Tao Wu, Xiangchun Chen and Ne Wang | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,rag] |
| Efficient MoE Inference on Single GPU with Dynamic Expert Caching | paper | 2026 | IEEE IPDPS 2026 official detailed program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Efficient Multi-round LLM Inference over Disaggregated Serving | paper | 2026 | AMPD 面向多轮 agent/RAG 工作流，在 PD 分离式服务中自适应协调增量 prefill 和阶段部署。 | [phase:prefill,serving] [workload:agent,rag] |

### State Compression & Signal Coding

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs | paper | 2026 | The key-value (KV) cache has become the dominant memory cost of transformer inference: it grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the throughput ceiling. Existing reductions fall into two families. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither exploits the fact that the cache at a layer is naturally a third-order tensor whose three axes, the heads, the tokens, and the features, carry very different amounts of redundancy. We take this tensor view directly. Our method, JoLT (Joint Lagrangian Tucker), applies a partial Tucker decomposition that compresses only the token and feature axes while leaving the head and layer axes intact, then restores the energy that truncation discards with a rotated low-bit residual: a random orthogonal rotation followed by low-bit quantization. A single Lagrangian dual allocates the Tucker ranks and the residual bit-widths together, per layer group and separately for keys and values, under one byte budget. The result is a near-lossless 2-3x compression. Perplexity stays near-lossless on both a grouped-query-attention model (Mistral-7B-v0.3) and a multi-head-attention model (LLaMA-2-13B), and GSM8K accuracy and needle-in-a-haystack retrieval hold at the uncompressed baseline at 2x on both architectures and through 3x on the GQA model. At 2x, JoLT reconstructs the cache to relative Frobenius error 0.009 (K) and 0.006 (V) on both architectures. A randomized-SVD variant, FlashJoLT, delivers a 5-13x compression-time speedup at 1024-token context and matched quality. | [optimization_layer:compiler,compression,kernel] [workload:long-context] [metrics:throughput] |
| ACCEPTANCE-GUIDED ADAPTIVE SPECULATIVE DECODING FOR EFFICIENT LARGE LANGUAGE MODEL INFERENCE | paper | 2026 | ICASSP 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,multimodal] |
| ADAPTIVE ERASURE CODING FOR FAULT-TOLERANT LLM SERVING WITH CONTINUOUS BATCHING | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] |
| ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping | paper | 2026 | ADAngel 用 DPR 模型生成多种混合精度 GEMM kernel，并通过 Oracle Policy Map 在运行时为任意 bit-width/shape 任务选择策略；相较 llama.cpp decode 吞吐最高提升 5.10x，相较 TensorRT-LLM prefill TTFT 提升 1.17x–2.38x。 | [phase:prefill,decode,serving] [hardware:gpu] [optimization_layer:compiler,compression,kernel] [framework_binding:tensorrt-llm] |
| ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference | paper | 2026 | COLM 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,long-context,rag] |
| AUM: Unleashing the Efficiency Potential of Shared Processors with Accelerator Units for LLM Serving | paper | 2026 | HPCA 2026 official detailed program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Accelerating Speculative Decoding with Block Diffusion Draft Trees | paper | 2026 | COLM 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,rag] |
| AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [metrics:slo,goodput] |
| AdaSpec: Adaptive Multilingual Speculative Decoding with Self-Synthesized Language-Aware Training and Vocabulary Simplification | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving,training] [workload:agent,edge,multimodal] |
| AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse | paper | 2026 | ACL 2026 official accepted main conference papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,rag] |
| Algorithms for Context Engineering in LLM Inference: Optimization of Placement, Compression, and Scheduling | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression] [workload:agent,edge,multimodal] |
| AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System | paper | 2026 | SIGMOD 2026 accepted research papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression] [workload:agent,rag] [metrics:throughput] |

### Execution Compilation & Kernel Fusion

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AccKV: Towards Efficient Audio-Video LLMs Inference via Adaptive-Focusing and Cross-Calibration KV Cache Optimization | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] |
| Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] [metrics:throughput] |
| Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference | paper | 2026 | Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest. On schema-dense input streams such as nested JSON, this score acts as a non-stationary filter that disproportionately retains noise: a non-content sink role (delimiters or whitespace) carries an order of magnitude more energy than any content role, and structural KEY tokens are over-retained at roughly 1.8x the rate of the answer-carrying VALUE tokens, collapsing exact-match accuracy from 88% to 0% at a 5% budget as the signal-to-noise ratio of the retained state degrades. A counterfactual experiment establishes that suppressing KEY tokens is the best deployable filter. Our retraining-free, role-conditional allocation over SnapKV's windowed score, governed by a single tuned hyperparameter, closes 63-98% of the H2O gap at sub-20% budgets and, at higher budgets, modestly matches or exceeds full-cache accuracy -- a small, seed-sensitive denoising effect (borderline significant at B=0.50; not distinguishable from zero at B=0.30 over four seeds). A 15 MB linear role probe supplies these labels at negligible inference cost, though matching parser-level downstream accuracy remains open. | [phase:training] [hardware:npu] [optimization_layer:compiler,kernel,kv-cache] [workload:edge,long-context] |
| Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices | paper | 2026 | Running large language models on consumer devices such as laptops and desktops is challenging because model weights often exceed GPU memory capacity, making offloading inference necessary to extend effective model capacity with CPU memory. Existing offloading systems, however, typically rely on coarse layer-level or expert-level scheduling, which overlooks substantial heterogeneity among tensors within the same layer and adapts poorly to changing hardware load conditions on such devices. This paper presents ATSInfer, a hybrid CPU-GPU inference system for consumer devices that performs offloading at tensor granularity. ATSInfer combines static tensor placement with load-aware dynamic transfer, and introduces asynchronous CPU-GPU coordination to efficiently schedule hardware storage, data movement, and computation across heterogeneous backends. We implement ATSInfer and evaluate it on representative consumer platforms using both dense and MoE models. Compared with existing systems, ATSInfer improves prefill throughput by up to 1.94$\times$ and decode throughput by up to 3.29$\times$, while also increasing GPU utilization and making more effective use of PCIe bandwidth. These results show that ATSInfer can substantially improve the user experience of local LLM deployment on personal consumer devices. | [phase:decode,prefill,serving] [hardware:gpu] [optimization_layer:memory,moe] [workload:agent,moe,rag] |
| COMPRESSING KV CACHE FOR LONG-CONTEXT LLM INFERENCE WITH INTER-LAYER ATTENTION SIMILARITY | paper | 2026 | ICASSP 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,kernel,kv-cache] [workload:agent,edge,long-context] |
| CasMoE: A Cascaded Framework for Efficient MoE Inference on Resource-constrained Devices | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:moe] [workload:agent,edge,moe] |
| CommitMoE: Efficient Fallback-Free MoE Inference with Offloading Under GPU Memory Constraints | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:memory,moe] [workload:agent,edge,moe] |
| DAVID: Dual-stage Adaptive Vision-text Integrated Decoupling for Multimodal KV Cache Eviction | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] |
| EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse | paper | 2026 | EARTH 根据 gating entropy 推测预取 expert 并复用结果，以降低 MoE expert 加载等待与误预取代价。 | [optimization_layer:moe] [workload:moe] |
| FIRM-MoE: Fine-GrainedExpert Decomposition for Resource-Adaptive MoE Inference | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:moe] [workload:agent,edge,moe] |
| HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference | paper | 2026 | Mixture-of-Experts (MoE) large language models (LLM) activate only a small number of experts during inference, but token routing introduces persistent expert hotness skew: a small set of hot experts continuously receives most tokens, while the remaining experts are lightly loaded. On 3.5D multi-chiplet systems, this skew not only causes compute imbalance but also amplifies pressure on communication, memory bandwidth, I/O, and execution queues. Therefore, the core problem is not simply to reduce token movement, but to dynamically place and reuse hot expert replicas across different memory tiers. This paper proposes HCRMap, a hot expert residency mapping framework for pressure-aware expert replica management in 3.5D MoE inference. Based on expert hotness, weight loading cost, migration overhead, and runtime resource pressure, HCRMap dynamically determines which experts should be promoted, retained, demoted, or evicted. It then maps routed token groups to suitable resident replicas, thereby jointly mitigating communication, memory, and queue bottlenecks. Experimental results show that HCRMap reduces end-to-end latency by 43.6% and 43.0% over Hydra in the prefill and decode stages, respectively; by 34.5% and 33.1% over MoEntwine; and by 46.7% and 46.0% over PIMoE. | [phase:decode,prefill,routing] [optimization_layer:memory,moe,routing] [workload:edge,moe] [metrics:latency] |
| Judge Q: Trainable Queries for Optimized Information Retention in KV Cache Eviction | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] |

### Program-Aware Scheduling

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving | paper | 2026 | 根据 prefill/decode 长度分类请求，逐步优化实例间 compute layout、负载平衡和选择性分布式执行，并用仿真估计器避免实际执行开销；基于生产工作负载评测，报告 SLO attainment 最高提升 3.6 倍、成本效率提升 2 倍。 | [phase:decode,prefill,serving] [optimization_layer:scheduler] [metrics:latency,slo] |
| Agentix: An Efficient Serving Engine for LLM Agents as General Programs | paper | 2026 | 把 agent 程序及其依赖的 LLM calls 作为 serving 调度的一等对象，利用已完成调用的程序级上下文进行抢占和优先级调度；官方 NSDI 2026 页面报告在相同延迟下，相比 vLLM 等系统程序吞吐提升 4–15 倍。 | [phase:serving] [hardware:tpu] [optimization_layer:compiler,kernel,scheduler] [workload:agent,rag] |
| Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration | paper | 2026 | Bullet 在空间放置和时间调度两个维度动态编排 LLM 请求，以减少 GPU 碎片并提高服务利用率。 | [phase:serving] [hardware:gpu] |
| CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving | paper | 2026 | CRAFT performs fine-grained, per-layer expert replication under a memory budget to improve load balance and serving goodput for large MoE models. | [phase:serving] [optimization_layer:memory,moe] [workload:moe] [metrics:goodput] |
| DecodeShare: Tracing the Shared Pathways of LLM Decode-Time Decisions | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:decode,serving] |
| DuetServe: Harmonizing Prefill and Decode for LLM Serving via Adaptive GPU Multiplexing | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:decode,prefill,serving] [hardware:gpu] |
| Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration | paper | 2026 | 提出面向普通 GPU 集群的 partially disaggregated serving，通过时间维度 P/D 分离、跨实例循环协作、adaptive routing 和 mitosis scaling 缓解 prefill-decode 干扰；在 32 张 NVIDIA L20 以太网集群上，相比 vLLM、Sarathi、DistServe、MoonCake 等基线 goodput 最高提升 2.51 倍，并开源 EcoServe。 | [phase:serving] [hardware:gpu] [metrics:goodput] |
| FlashAgents: Accelerating Multi-Agent LLM Systems via Streaming Prefill Overlap | paper | 2026 | FlashAgents 用 agent 间 token streaming、增量 prefill 和 prefix-aware coordination 重叠多智能体调用链中的等待与计算。 | [phase:prefill,serving] [workload:agent,rag] |
| FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,rag] |
| From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:prefill,serving] [optimization_layer:moe] [workload:moe] [metrics:stall] |
| HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving | paper | 2026 | HELIOS 在线选择模型和 early-exit 层数，只加载满足任务目标所需的层，从而在质量约束下提高吞吐和能效。 | [phase:serving] |
| HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds | paper | 2026 | 通过跨服务器预分发模型、重叠 cold-start 阶段、GPU 间 worker 放置和 pipeline consolidation，降低公有云 serverless LLM serving 冷启动；官方 NSDI 2026 页面报告冷启动延迟降低 1.7–4.7 倍，SLO attainment 提升 1.43–1.74 倍。 | [phase:serving] [hardware:gpu] [workload:agent,rag] [metrics:latency] |

### SRE/Fault-Tolerance/Sparing

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems | paper | 2026 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更。 | [phase:serving] |
| GAPS: Global-Aware Prediction-driven Scheduling for Large-Scale LLM Inference | paper | 2026 | AAMAS 2026 official proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,rag] |
| GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving | paper | 2026 | GhostServe 在 host memory 中以 erasure coding 为 streaming KV cache 生成 parity shards，故障时重建丢失 KV 状态并继续推理，避免完整重算或全量状态复制；单 batch checkpoint latency 最高降低 2.7x，recovery latency 降低 2.1x，中位响应延迟降低 1.2x。 | [phase:serving,decode] [hardware:gpu] [optimization_layer:compression,kv-cache,memory] [workload:long-context,agent] |
| Probe-and-Fetch: Dynamic KV Cache Pruning for Accelerated Long-Context Inference in Web-Scale AI Search | paper | 2026 | Authors: Yuchen Li:Baidu Inc.,Shanghai Jiao Tong University;Rui Kong:Baidu Inc.;Xinran Chen:Baidu Inc.;Chengzhe Zhang:Baidu Inc.;Jiamin Chen:City University of Hong Kong;Cheng Deng:University of Edinburgh;Xinyu Ma:Baidu Inc.;Haojie Zhang:Baidu Inc.;Tianhao Peng:Baidu Inc.;Hengyi Cai:Baidu Inc.;Shuaiqiang Wang:Baidu Inc.;Jiashu Zhao:Wilfrid Laurier University;Yongqi Zhang:The Hong Kong University of Science and Technology (Guangzhou);Haoyi Xiong:Baidu Inc.;Jimmy Xiangji Huang:York University;Lei Chen:The Hong Kong University of Science and Technology (Guangzhou);Jun Wang:University College London;Dawei Yin:Baidu Inc. | [phase:serving] [optimization_layer:kv-cache] [workload:agent,long-context,rag] |
| LUMEN: Coordinated Failure Recovery for Distributed LLM Serving | paper | 2026 | LUMEN 把分布式 LLM serving 的故障恢复建模为 checkpoint 放置、请求重分配和 reload 期间容量恢复的联合负载协调问题。 | [phase:serving] |
| ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters | paper | 2026 | ShuntServe 面向异构 spot GPU 集群联合做模型放置、负载分流和抢占恢复，以降低满足 SLO 的 serving 成本。 | [phase:serving] [hardware:gpu] [metrics:slo] |
| Tarragon: Making MoE-based LLM Inference Resilient | paper | 2026 | Tarragon 将 attention worker 和 expert worker 设为独立故障域，用 KV 增量 checkpoint 和 shadow experts 快速恢复。 | [optimization_layer:moe] [workload:moe,rag] |
| PhoenixOS: Concurrent OS-level GPU Checkpoint and Restore with Validated Speculation | paper | 2025 | PhoenixOS 在操作系统层并发执行 GPU checkpoint/restore，并通过验证式推测减少暂停时间。 | [hardware:gpu] |
| ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference | paper | 2025 | ShadowKV 在 GPU 侧保留低秩 keys、landmarks 和少量 outliers，并按需从 CPU DRAM 拉取匹配 value 以提升长上下文吞吐。 | [hardware:gpu] [optimization_layer:kv-cache] [workload:long-context] [metrics:throughput] |
| BurstGPT: A Real-world Workload Dataset to Optimize LLM Serving Systems | paper | 2024 | BurstGPT 发布 Azure OpenAI 服务的五百余万条真实 trace，揭示 burst、长度和失败模式对调度评估的影响。 | [phase:serving] |
| DejaVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving | paper | 2024 | DejaVu 用 KV-cache streaming 支持 prompt-token 分离、microbatch swapping 和状态复制，缓解流水线空泡、显存过配和故障恢复问题。 | [phase:serving] [optimization_layer:kv-cache] |
| Gemma 4 on vLLM-TPU | industry | 2026 | 展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。 | [phase:serving] [hardware:gpu,tpu] [framework_binding:vllm] |
