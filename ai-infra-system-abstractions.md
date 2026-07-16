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
| Memory Topology & Virtualization | 287 | 186 | 50 | 51 | KV cache、long-context state、offload、prefix/RAG cache、CXL/分层内存。 |
| Disaggregated Interconnects | 3219 | 167 | 86 | 2966 | P/D 分离、KV transfer、RDMA/NIXL/UCCL、collective 和跨节点路由。 |
| State Compression & Signal Coding | 8098 | 265 | 186 | 7647 | 低比特 KV、MLA latent、稀疏/量化/编码压缩与质量-成本权衡。 |
| Execution Compilation & Kernel Fusion | 3733 | 130 | 115 | 3488 | Triton/CUDA/HIP kernel、attention/GEMM/MoE 算子、编译和硬件后端。 |
| Program-Aware Scheduling | 618 | 199 | 53 | 366 | agent graph、structured generation、多阶段工作流和程序感知调度。 |
| SRE/Fault-Tolerance/Sparing | 1690 | 30 | 11 | 1649 | trace/benchmark、SLO、故障恢复、漂移、数值稳定性和生产降级。 |

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
| Decouple and Cache: KV Cache Construction for Streaming Video Understanding | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] [workload:video] |
| EpiCache: Episodic KV Cache Management for Long-Term Conversation on Resource-Constrained Environments | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |
| FlashAccel: Leveraging High-Bandwidth Flash for High-Throughput LLM Inference | paper | 2026 | Large language model (LLM) inference is increasingly limited by the capacity of High-Bandwidth Memory (HBM) in GPUs, as model weights and KV cache grow rapidly. High-Bandwidth Flash (HBF) provides higher capacity than HBM while retaining comparable bandwidth, making it a promising substrate for capacity-constrained LLM inference. However, its inherently high access latency, low bandwidth utilization, and lack of support for heterogeneous resource management make it difficult to integrate HBF into GPUs for LLM inference. We present FlashAccel, a co-designed system that enables efficient LLM inference using HBF. FlashAccel integrates HBF into HBM-based GPUs, providing architectural support to mitigate access latency. It improves bandwidth utilization through specialized data layouts for both model weights and KV cache, and introduces an HBF-aware storage management layer together with a programming model to organize persistent data in HBF and coordinate heterogeneous memory resources at the system level. Experimental results demonstrate that integrating six HBF stacks into the GPU enables FlashAccel to deliver an average improvement of 2.54$\times$ and 1.93$\times$ in throughput per GPU and energy efficiency over the HBM-only GPU under 100ms latency constraint, respectively. | [hardware:gpu] [optimization_layer:kv-cache,memory] [workload:agent,rag] [metrics:latency,throughput] |
| ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |
| HiServe: A Prefix Cache Serving System for Hybrid LLMs | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] |
| High Throughput and Low Latency LLM Serving via Adaptive KV Caching | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [metrics:latency,throughput] |
| KUNSERVE: Parameter-centric Memory Management for Efficient Memory Overloading Handling in LLM Serving | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:memory] |
| LRAgent: Efficient KV Cache Sharing for Multi-LoRA LLM Agents | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] [workload:agent,rag] |
| OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] [workload:long-context] |
| Predicting Future KV Utility: Global Combinatorial Optimization for Task-Agnostic KV Cache Eviction | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |
| Prefix cache aware data reordering for LLM augmented database analytics | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 |  |
| ProphetKV: User-Query-Driven Selective Recomputation for Efficient KV Cache Reuse in Retrieval-Augmented Generation | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |

### Disaggregated Interconnects

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| APEX: Asynchronous Parallel CPU-GPU Execution for Online LLM Inference on Constrained GPUs | paper | 2026 | IEEE IPDPS 2026 official detailed program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:compiler,compression,kernel] [workload:edge] |
| ARKV: Adaptive Resource-Efficient KV Cache Management for Long Context LLM Inference under Memory Constraints | paper | 2026 | CCGrid 2026 official program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache,memory] [workload:edge,long-context] |
| Accelerating Block Low-Rank Foundation Model Inference on Memory-Constrained GPUs | paper | 2026 | HPDC 2026 official program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques | paper | 2026 | IJCAI-ECAI 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression] [workload:agent,edge,rag] |
| An LLM-Guided Query-Aware Inference System for GNN Models on Large Knowledge Graphs | paper | 2026 | ICDE 2026 official accepted research papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression] [workload:agent,edge,rag] |
| An SLO-Driven Feedback Controller for Kubernetes Horizontal Pod Autoscaling | paper | 2026 | IEEE CLOUD 2026 official conference program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,rag] [framework_binding:kubernetes] [metrics:slo] |
| Aurora: A Disaggregated GPU-PNM-PIM System for High-Throughput Mixed-Length LLM Inference | paper | 2026 | ACM ICS 2026 official program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:compiler,kernel] [workload:edge] |
| BYSTANDER: State-Aware Execution-Time Prediction for Heterogeneous LLM Inference Scheduling | paper | 2026 | IEEE CLOUD 2026 official conference program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,rag] |
| Batchmon: Exploiting Serverless Functions for Cost-Effective, SLO-Driven Batch Inference Serving | paper | 2026 | Authors: Josep Calero and Marc Sanchez-Artigas | [phase:serving] [workload:agent,edge,rag] [metrics:slo] |
| Beyond Throughput: Performance and Energy Insights of LLM Inference Across AI Accelerators | paper | 2026 | IEEE IPDPS 2026 official detailed program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge] [metrics:throughput] |
| BridgeLoRA: Privacy-preserving Collaborative Skip-Layer Connectors for Efficient Transformer Inference on Edge Cloud Continuum | paper | 2026 | Authors: Vilhelm Toivonen, Xiang Su, Xiaoli Liu, Sasu Tarkoma and Pan Hui | [phase:serving] [workload:agent,edge,rag] |
| CIMERA: Compute-in-Interconnect and Memory with Reconfigurable Precision for LLM Inference | paper | 2026 | LLM impose significant computational and memory demands, creating challenges for energy-efficient inference across platforms ranging from data centers to power-constrained edge devices. Weight precision plays a critical role in balancing inference accuracy, throughput, and energy consumption, while modern LLM workloads exhibit pronounced heterogeneity and tolerance that favors adaptive precision execution. This paper presents CIMERA, a reconfigurable-precision LLM inference accelerator that integrates compute-in-interconnect and memory to mitigate the memory wall and enable precision-aware execution. Compared to Nvidia H100, CIMERA delivers up to $25\times$ and $10\times$ higher energy efficiency for 1B and 13B models, respectively. | [optimization_layer:memory] [workload:edge] [metrics:throughput] |

### State Compression & Signal Coding

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs | paper | 2026 | The key-value (KV) cache has become the dominant memory cost of transformer inference. It grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the ceiling on throughput. Two families of methods reduce it. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither family exploits the fact that the cache at a layer is naturally a third-order tensor whose three axes, the heads, the tokens, and the features, carry very different amounts of redundancy. We take this tensor view directly. Our method, JoLT, applies a partial Tucker decomposition that compresses only the token and feature axes while leaving the head and layer axes intact, and then restores the energy that truncation discards with a Johnson-Lindenstrauss (JL) rotated low-bit residual. A single Lagrangian dual allocates the Tucker ranks and the residual bit-widths together, per layer group and separately for keys and values, under one byte budget. The result is a near-lossless 2-3x compression: perplexity, GSM8K accuracy, and RULER needle-in-a-haystack retrieval all stay at or within statistical noise of the uncompressed baseline on both a grouped-query-attention model (Mistral-7B-v0.3) and a multi-head-attention model (LLaMA-2-13B). At 2x, JoLT reconstructs the cache to relative Frobenius error 0.009 (K) and 0.006 (V) on both architectures, roughly an order of magnitude below cross-layer SVD and 4-bit quantization. A randomized-SVD variant, FlashJoLT, delivers a 5-13x compression-time speedup at matched quality. | [optimization_layer:compiler,compression,kernel] [workload:long-context] [metrics:throughput] |
| ACCEPTANCE-GUIDED ADAPTIVE SPECULATIVE DECODING FOR EFFICIENT LARGE LANGUAGE MODEL INFERENCE | paper | 2026 | ICASSP 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,multimodal] |
| ADAPTIVE ERASURE CODING FOR FAULT-TOLERANT LLM SERVING WITH CONTINUOUS BATCHING | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] |
| ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference | paper | 2026 | COLM 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,long-context,rag] |
| AUM: Unleashing the Efficiency Potential of Shared Processors with Accelerator Units for LLM Serving | paper | 2026 | HPCA 2026 official detailed program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Accelerating Sparse Transformer Inference on GPU | paper | 2026 | PPoPP 2026 official detailed program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:compiler,compression,kernel] [workload:moe] |
| Accelerating Speculative Decoding with Block Diffusion Draft Trees | paper | 2026 | COLM 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,rag] |
| AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [metrics:slo] |
| AdaSpec: Adaptive Multilingual Speculative Decoding with Self-Synthesized Language-Aware Training and Vocabulary Simplification | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving,training] [workload:agent,edge,multimodal] |
| AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse | paper | 2026 | ACL 2026 official accepted main conference papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,rag] |
| Algorithms for Context Engineering in LLM Inference: Optimization of Placement, Compression, and Scheduling | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression] [workload:agent,edge,multimodal] |
| AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System | paper | 2026 | SIGMOD 2026 accepted research papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression] [workload:agent,rag] [metrics:throughput] |

### Execution Compilation & Kernel Fusion

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AP2O-Coder: Adaptively Progressive Preference Optimization for Reducing Compilation and Runtime Errors in LLM-Generated Code | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,multimodal] |
| AccKV: Towards Efficient Audio-Video LLMs Inference via Adaptive-Focusing and Cross-Calibration KV Cache Optimization | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] |
| Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] [metrics:throughput] |
| Act Before It's Too Late: Power-Efficient LLM Inference on Mobile Device | paper | 2026 | MobiSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,kernel] [workload:edge,multimodal] |
| Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference | paper | 2026 | Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest. On schema-dense input streams such as nested JSON, this score acts as a non-stationary filter that disproportionately retains noise: a non-content sink role (delimiters or whitespace) carries an order of magnitude more energy than any content role, and structural KEY tokens are over-retained at roughly 1.8x the rate of the answer-carrying VALUE tokens, collapsing exact-match accuracy from 88% to 0% at a 5% budget as the signal-to-noise ratio of the retained state degrades. A counterfactual experiment establishes that suppressing KEY tokens is the best deployable filter. Our retraining-free, role-conditional allocation over SnapKV's windowed score, governed by a single tuned hyperparameter, closes 63-98% of the H2O gap at sub-20% budgets and, at higher budgets, modestly matches or exceeds full-cache accuracy -- a small, seed-sensitive denoising effect (borderline significant at B=0.50; not distinguishable from zero at B=0.30 over four seeds). A 15 MB linear role probe supplies these labels at negligible inference cost, though matching parser-level downstream accuracy remains open. | [phase:training] [hardware:npu] [optimization_layer:compiler,kernel,kv-cache] [workload:edge,long-context] |
| Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results | paper | 2026 | Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses. We study inference-time feed-forward network (FFN) intervention for improving structured outputs without retraining model weights. Our project began with Orthogonal Residual Projection (ORP), a direction-changing repair attempt that revealed sensitive SwiGLU FFN intervention sites but often caused more harm than fixes. We therefore propose Amplitude Gating (AG), a non-destructive alternative that preserves pretrained FFN weight directions and modulates only activation magnitudes during generation. We define a fine-grained intervention system spanning P1/P2/P3 and branch-specific P1s/P2a/P2b sites, and introduce an evaluation protocol that separates combination-oracle headroom from fixed configurations and learned gates, enforces sample-level accounting, and uses task-aware metrics for binary and partial-credit datasets. Across Qwen3.5-9B, Qwen3-8B, and Qwen2.5-7B, AG is weakly positive in aggregate but strongest on tool-structured tasks. On Qwen3.5-9B, a category-level learned gate improves tool/structured/agentic performance from 38.66% to 42.92% (+4.27 percentage points), with Hermes function-call tasks reaching about +7.6 points. On Qwen3-8B, Hermes JSON mode improves by +11.36 points. Qwen2.5-7B retains oracle headroom but current learned gates fail to capture it, showing that deployment requires model- and category-specific routing. Comparisons of entropy AG with Newton-Schulz-windowed AG show that neither family is uniformly dominant. These results identify tool-structured inference as the most credible first target for safe FFN-level inference optimization, while prospective online validation and broader cross-model evaluation remain necessary. | [phase:routing,training] [hardware:tpu] [optimization_layer:compiler,kernel,routing] [workload:agent,rag] |
| Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices | paper | 2026 | Running large language models on consumer devices such as laptops and desktops is challenging because model weights often exceed GPU memory capacity, making offloading inference necessary to extend effective model capacity with CPU memory. Existing offloading systems, however, typically rely on coarse layer-level or expert-level scheduling, which overlooks substantial heterogeneity among tensors within the same layer and adapts poorly to changing hardware load conditions on such devices. This paper presents ATSInfer, a hybrid CPU-GPU inference system for consumer devices that performs offloading at tensor granularity. ATSInfer combines static tensor placement with load-aware dynamic transfer, and introduces asynchronous CPU-GPU coordination to efficiently schedule hardware storage, data movement, and computation across heterogeneous backends. We implement ATSInfer and evaluate it on representative consumer platforms using both dense and MoE models. Compared with existing systems, ATSInfer improves prefill throughput by up to 1.94$\times$ and decode throughput by up to 3.29$\times$, while also increasing GPU utilization and making more effective use of PCIe bandwidth. These results show that ATSInfer can substantially improve the user experience of local LLM deployment on personal consumer devices. | [phase:decode,prefill,serving] [hardware:gpu] [optimization_layer:memory,moe] [workload:agent,moe,rag] |
| COMPRESSING KV CACHE FOR LONG-CONTEXT LLM INFERENCE WITH INTER-LAYER ATTENTION SIMILARITY | paper | 2026 | ICASSP 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,kernel,kv-cache] [workload:agent,edge,long-context] |
| CORM: COARSE-TO-FINE-GRAINED OFFLOADING FOR SMOE LLM INFERENCE ON CONSUMER-GRADE GPU | paper | 2026 | ICASSP 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:moe] [workload:agent,edge,moe] |
| CasMoE: A Cascaded Framework for Efficient MoE Inference on Resource-constrained Devices | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:moe] [workload:agent,edge,moe] |
| CommitMoE: Efficient Fallback-Free MoE Inference with Offloading Under GPU Memory Constraints | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [hardware:gpu] [optimization_layer:memory,moe] [workload:agent,edge,moe] |
| DAVID: Dual-stage Adaptive Vision-text Integrated Decoupling for Multimodal KV Cache Eviction | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] |

### Program-Aware Scheduling

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:scheduler] [metrics:latency] |
| CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:moe] [workload:moe] |
| DecodeShare: Tracing the Shared Pathways of LLM Decode-Time Decisions | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:decode,serving] |
| DuetServe: Harmonizing Prefill and Decode for LLM Serving via Adaptive GPU Multiplexing | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:decode,prefill,serving] [hardware:gpu] |
| FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,rag] |
| From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:prefill,serving] [optimization_layer:moe] [workload:moe] [metrics:stall] |
| LYNX: Workload-Agnostic Expert Remapping for Efficient MoE Inference | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:moe] [workload:moe] |
| Least-Loaded Expert Parallelism: Load Balancing An Imbalanced Mixture-of-Experts | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:moe] [workload:moe] |
| On the Diminishing Returns of Expert Load Balancing in MoE LLM Serving | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:moe] [workload:moe] |
| Online Linear Programming for Multi-Objective Routing in LLM Serving | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:routing,serving] [optimization_layer:routing] |
| Opportunistic Expert Activation: Batch-Aware Expert Routing for Faster Decode Without Retraining | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:decode,routing,serving] [optimization_layer:routing] |
| Position: LLM Serving Needs Mathematical Optimization and Algorithmic Foundations, Not Just Heuristics | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] |

### SRE/Fault-Tolerance/Sparing

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| BEAM: Joint Resource–Power Optimization for Energy-Efficient LLM Inference under SLO contraints | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [metrics:slo] |
| GAPS: Global-Aware Prediction-driven Scheduling for Large-Scale LLM Inference | paper | 2026 | AAMAS 2026 official proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,rag] |
| Probe-and-Fetch: Dynamic KV Cache Pruning for Accelerated Long-Context Inference in Web-Scale AI Search | paper | 2026 | Authors: Yuchen Li:Baidu Inc.,Shanghai Jiao Tong University;Rui Kong:Baidu Inc.;Xinran Chen:Baidu Inc.;Chengzhe Zhang:Baidu Inc.;Jiamin Chen:City University of Hong Kong;Cheng Deng:University of Edinburgh;Xinyu Ma:Baidu Inc.;Haojie Zhang:Baidu Inc.;Tianhao Peng:Baidu Inc.;Hengyi Cai:Baidu Inc.;Shuaiqiang Wang:Baidu Inc.;Jiashu Zhao:Wilfrid Laurier University;Yongqi Zhang:The Hong Kong University of Science and Technology (Guangzhou);Haoyi Xiong:Baidu Inc.;Jimmy Xiangji Huang:York University;Lei Chen:The Hong Kong University of Science and Technology (Guangzhou);Jun Wang:University College London;Dawei Yin:Baidu Inc. | [phase:serving] [optimization_layer:kv-cache] [workload:agent,long-context,rag] |
| Understanding and Improving Communication Performance in Multi-node LLM Inference | paper | 2026 | ACM CAIS 2026 official accepted research papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,rag] |
| llm-tuna - Hyperparameter Optimization for LLM Inference | paper | 2026 | Authors: Thameem Abbas Ibrahim Bathusha:Red Hat LLC.;Aanya Sharma:Red Hat LLC.;Andy Huynh:Boston University;Rehan Samaratunga:Boston University;Ashish Kamra:Red Hat LLC. | [phase:serving] [workload:agent,rag] |
| ADS: AN AGENTIC DETECTION SYSTEM FOR ENTERPRISE AGENTIC AI SECURITY | paper | 2026 | ADS 面向企业 agentic AI 安全构建检测系统，把 agent 行为、工具调用和安全策略纳入运行时监控。 | [phase:serving] [workload:agent,rag] |
| Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study | paper | 2026 | 该工作在 MI325X 上比较 MLA、GQA、MoE 和多模态模型，说明 AITER、KV offload 与 block size 必须按架构选择。 | [hardware:amd,gpu] [optimization_layer:moe] [workload:moe] |
| Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy | paper | 2026 | 该工作用 GEMM 维度统一重组 LLM pruning 设计空间，比较不同剪枝族在真实内核与硬件上的实际推理加速边界。 | [optimization_layer:kv-cache] |
| Blueprint, Bootstrap, and Bridge: A Security Look at NVIDIA GPU Confidential Computing | paper | 2026 | 该工作系统分析 NVIDIA GPU confidential computing 的安全边界、启动链和桥接机制，为隐私推理与受保护训练部署提供风险视角。 | [hardware:gpu] |
| CSLE: A Reinforcement Learning Platform for Autonomous Security Management | paper | 2026 | CSLE 提供自治安全管理的强化学习平台，可用于评估 AI 基础设施中的自动防御、响应和策略学习。 |  |
| DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems | paper | 2026 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更。 | [phase:serving] |
| Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving | paper | 2026 | Execution-State Capsules 将 agent/physical-AI workflow 的执行状态绑定到图节点，用小批量 checkpoint/restore 降低端侧服务恢复延迟。 | [phase:serving] [workload:agent,rag] [metrics:latency] |
