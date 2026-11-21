# November 21, 2026 — independent high-recall arXiv and inference-engine resweep

**Start point:** merged PR #95 `main@aa589f9`, 965 canonical entries; 90 distinct `2611.*` arXiv IDs in existing eight topic tables. This resweep adds **12 nonduplicates (10 EVIDENCED, 2 EXPLORE)** for **977 total**. All accelerators, experiments and E2E claims are **author-reported; not independently run**. Do not conflate manuscript inspection with replication.

## 1. Search methods actually used (and how they changed results)

1. **Official category reverse-diff:** independently inspect [arXiv cs.DC new](https://arxiv.org/list/cs.DC/new), [recent](https://arxiv.org/list/cs.DC/recent), [cs.AR](https://arxiv.org/list/cs.AR/new), [cs.PF](https://arxiv.org/list/cs.PF/new), [cs.OS](https://arxiv.org/list/cs.OS/new) rather than relying on term `LLM inference`. Compare newly noticed identities against **all eight 965-row main topics**, not simply the 21-paper last PR. This exposed GDN live migration, Berth, LightningMoBA, SASS and Kameleo; original source was checked.
2. **Cross-class / neglected publication windows:** targeted cs.LG/cs.CL/cs.SE/cs.AI and hardware, agent, engine, cache, communication, SLO queries. This found past omissions from Nov 2 and Nov 9 as well as newer Nov 18–19 work, including AttentionIndex, KernelSeek and OverlapAdvisor.
3. **Secondary-lead → first-party validation:** the [Nov 19 paper digest](https://amarcu.github.io/ai-paper-digest/archive/2026-11-19.html) surfaced `RSIBench-Infra` in cs.LG. Then inspect original [arXiv](https://arxiv.org/abs/2611.24395) manuscript/PDF and simulation vs real evidence. An X post, digest, HF Trending or industry article is **discovery**, never source-of-truth.
4. **Code/first-party triangulation:** browse dated [vLLM archive](https://vllm.ai/blog/archive), [LMSYS engineering](https://www.lmsys.org/blog), [NVIDIA dev blog](https://developer.nvidia.com/blog), [ROCm](https://rocm.blogs.amd.com), and model/card/API docs, then inspect corresponding GitHub release/PR/implementation when accessible. Engineering announcements inform a company/community page, **not another paper row**.
5. **Evidence and alias gate:** verify real arXiv paper identity, methods, comparative experiment, hardware and precision/quality contract. Distinguish a GPU simulation, TPU operator, mixed training+inference benchmark, and deployed vLLM service. Old HOLD decisions can be upgraded only by source-specific new evidence.

**Limits:** the complete raw search result denominators, the entire every-category RSS history and exact per-query result ranks were not persisted, so a quantitative recall/precision or no-omission claim is **not** justified. We observed genuine omissions relative to the 965 baseline. Keep search heuristics adaptive and discovery broad, preserve evidence strict. No automated daily process has been run or installed by this PR.

## 2. New source-reviewed additions — precise claim boundaries

| Canonical home | Source | Status | Mechanism and experiment boundary |
|---|---|---|---|
| kernels-compilers / Attention & Sparse Kernels | [Accelerating Mixture of Block Attention via Dynamic Routing, KV-Centric Execution and Runtime Pipelining](https://arxiv.org/abs/2611.26268) | KEEP_PREPRINT_EVIDENCED | 融合稀疏 Block Routing、KV-centric Tile Ownership 和 GPU Kernel Pipeline；作者长上下文真实 Hopper GPU、五模型与 FlashMoBA 在匹配 Top-16 保留预算下报告端到端 Generation 约 1.20–1.60×，须保持 Sparse Quality/Route Budget；不是在线 Serving Goodput |
| kernels-compilers / Attention & Sparse Kernels | [AttentionIndex: Accelerating Learned Sparse Attention with a Causal Inverted-File Index](https://arxiv.org/abs/2611.02508) | KEEP_PREPRINT_EVIDENCED | NVIDIA 作者针对百万上下文 Sparse Attention 的 Index Search 本身做因果索引/选择优化，真实 GPU 报告 Indexer/Prefill 效率与 Recall；Sparse Approximation、质量和模型范围独立核查 |
| kernels-compilers / Kernel Automation & Tools | [Dissecting an Unexplored SASS Control-Code Field: Barrier Exemption and Programmable Warp Priority](https://arxiv.org/abs/2611.24437) | KEEP_PREPRINT_EVIDENCED | 从原生 SASS Control Code 实现 Barrier Exemption / Warp Priority 和后编译 Binary Optimizer；六款 GPU Kernel 最高 31.9%，llama.cpp/vLLM 端到端最高 3.6%；CUDA CUBIN 专属、非 CANN 迁移证据 |
| kernels-compilers / Kernel Automation & Tools | [Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization (KernelSeek)](https://arxiv.org/abs/2611.03517) | KEEP_PREPRINT_EVIDENCED | Minimal Correctness Harness + 问题导向 Agent 引导，Hopper/Blackwell FlashAttention Forward 各 182 场景通过、作者几何平均 FA3/FA4 1.16×/1.46×；存在 162 条人工消息和 11.5K Agent Tool Calls，不是完全自主 RSI 或 Serving TPS |
| kv-cache-memory / Sparse KV Retrieval | [Twindex: Index Cache Offloading with Coarse-to-Fine Selection for Long-Context Sparse-Attention Serving](https://arxiv.org/abs/2611.25078) | KEEP_PREPRINT_EVIDENCED | 将稀疏 Attention Index Cache 视为独立 HBM 驻留瓶颈，Index State 压缩+CPU Host Tiering/Prefetch；真实 GPU 长上下文多模型测量，需对照 KV-only Offload、检索精度和模型输出质量 |
| quantization-compression / Mixed Precision & Bit Allocation | [Kameleo: In-Situ Activation-Precision Selection for Bit-Serial LLM Accelerators](https://arxiv.org/abs/2611.25971) | KEEP_PREPRINT_EXPLORE | 利用 Bit-serial PE 部分和近似质量信号在线选择 GEMM Activation Precision；四 LLM/七数据集在约 1% PPL Budget 下作者模拟 MXU Prefill Cycles 减少 2.11–2.34×、合成面积 +3.7%；无真实芯片端到端 Serving |
| moe-sparse-execution / Expert Routing & Communication | [OverlapAdvisor: Modeling and Adapting Computation-Communication Overlap for Distributed MoE Serving](https://arxiv.org/abs/2611.11857) | KEEP_PREPRINT_EVIDENCED | 以性能预测器选择 MoE EP Dispatch/Combine Granularity/Overlap；作者 SGLang/vLLM E2E 相对 MegaMoE/UniEP/DeepEP 平均 +1.78%/+4.57%/+9.97%，特定最大 +31.72%，不能合并为普适收益 |
| moe-sparse-execution / Expert Routing & Communication | [Fuse-All MoE Inference Kernel with Load Balancing on TPUs](https://arxiv.org/abs/2611.17857) | KEEP_PREPRINT_EVIDENCED | TPU Pallas MoE EP Fusion、Direct-write DMA 与负载均衡；作者 TPU EP8TP2 Kernel 对 Fused EP16 延迟最高 -21.3%，加上其他 Serving Stack 优化后 E2E 对 Megablox EP16 +12–34.5%；不可将整栈收益归因单 Kernel |
| runtime-scheduling / Preemption & Multi-Tenancy | [Berth: SLO-Preserving GPU Sharing Without New Preemption](https://arxiv.org/abs/2611.25091) | KEEP_PREPRINT_EVIDENCED | User-space GPU 调度控制保护前台 vLLM SLO 并运行 Best-effort Work，A100 混合租户/MLPerf 对照；依赖 CUDA 驱动语义、具体 SLO 和资源干扰，不是原生 Ascend 证据 |
| distributed-serving / Fleet Scaling & Reliability | [Live Migration of Gated DeltaNet Requests: Exact Catch-Up and the Cost of Log Backlog](https://arxiv.org/abs/2611.26153) | KEEP_PREPRINT_EXPLORE | 针对 Recurrent GDN State 迁移分析复制、日志追赶和一致性预算；真实 RTX GPU 验证主要限纯 GDN，并采用受控带宽与 Hybrid Pilot；非已部署混合 MoE/全量 PD 迁移系统 |
| benchmarking-analysis / Serving Benchmarks & Workloads | [RSIBench-Infra: Can Agents Optimize Their Own Training and Inference Infrastructure at Production Scale?](https://arxiv.org/abs/2611.24395) | KEEP_PREPRINT_EVIDENCED | 20 个真实训练+推理 Infra 任务（GPU/Ascend NPU，最多 32 加速器），Agent 可交 OCI Layer 并在独立正确性/质量门槛下量 E2E；作者 66.2% Task Results >1.1× 统计混合 Training 和 Inference，非全推理 TPS 或模型权重 RSI |
| benchmarking-analysis / Performance & Efficiency Studies | [Benchmarking LLM Inference on Desktop-Scale NVIDIA Grace Blackwell Clusters](https://arxiv.org/abs/2611.20289) | KEEP_PREPRINT_EVIDENCED | 17 Checkpoints，vLLM 单/双 DGX Spark，TP2/PP2/Replica 并发 1–64，每配置三独立启动与置信区间、能效；TP2 峰值吞吐中位 1.59×、PP2 1.39×，设备和 TCP/Host-stage 传输特定 |

**Bookkeeping:** Kernel 133→137; KV 185→186; Decoding remains 100; Quantization 52→53; MoE 89→91; Runtime 163→164; Distributed 145→146; Benchmark 98→100. 44 subgroups unchanged. Do not recategorize the older 965 or count Frontier cross-links as new papers.

## 3. November 1–20 research landscape: beyond incremental paper counts

- **Kernels/Compilers:** Attention I/O plus sparse indexer, dynamic ownership and subcompiler warp scheduling. [MegaOps](https://arxiv.org/abs/2611.16248), [SubGPU Pipelining](https://arxiv.org/abs/2611.14904), [Together Compiler](https://arxiv.org/abs/2611.14681), [EngineAgent](https://arxiv.org/abs/2611.14356), [CompoundingKernel](https://arxiv.org/abs/2611.19230), [Warpline](https://arxiv.org/abs/2611.04331), [ForgeKernel](https://arxiv.org/abs/2611.04998) were **already canonical**. New [KernelSeek](https://arxiv.org/abs/2611.03517) supplies a strong minimal-harness, question-driven agent counterpoint (humans heavily involved).
- **KV:** workload-specific state residency supersedes a single eviction policy; [MORTIS](https://arxiv.org/abs/2611.08638), [TripleKV](https://arxiv.org/abs/2611.25112), [Nebula](https://arxiv.org/abs/2611.09474) and [TideCache](https://arxiv.org/abs/2611.26619) span cross-session ownership, transfer, tool waits, hybrid recurrence. New Twindex makes **Sparse Index Cache** a first-class HBM tiering target.
- **Decoding:** [HybridSpec](https://arxiv.org/abs/2611.04055), [ForeSpark](https://arxiv.org/abs/2611.13442), [D3Tree](https://arxiv.org/abs/2611.11371), [DForkTree](https://arxiv.org/abs/2611.12356), [SpecSearch](https://arxiv.org/abs/2611.22296), [Weights That Stay](https://arxiv.org/abs/2611.00506) cover hybrid targets, adaptive verifier budgets and draft-vs-onchip cost. The current resweep found no new source-eligible, nonduplicate Decoding-only item; **not evidence the field stopped evolving**.
- **Quant/MoE:** FP4, Mixed Precision and runtime Bit Budget must be evaluated against hardware and quality. [EchoMoE](https://arxiv.org/abs/2611.22215) changes the model by fine-tuning; new OverlapAdvisor chooses EP Strategy using device/config costs; Fuse-All integrates TPU MoE dataflow (entire stack gains not a kernel-only baseline).
- **Runtime/Distributed/Benchmark:** agent working-set metastability [Basin](https://arxiv.org/abs/2611.02543), adaptive PD [Evolving Infra](https://arxiv.org/abs/2611.12304), capacity routing [Cap-and-Track](https://arxiv.org/abs/2611.24891), quality-gated agent traces and RSI benchmark. GDN state migration and GPU multi-tenancy require new contracts beyond token-level arithmetic.

**Frontier distinction:** Kernel Agent improvement (KDA, CAKE, ForgeKernel, KernelSeek); full Engine artifact improvement (SEIS, Together Compiler, ERNIE Evolve); optimization agent competence upgrade on held-out tasks (unproven). RSIBench-Infra covers training and inference and up to 32 GPU/Ascend NPUs under controlled tasks. Its 66.2% >1.1× is a pooled task result **not inference-only TPS nor Agent/model-weight RSI**. Agent-native KV/session lifecycle, realtime multi-modal, dLLM and embodied serving remain execution-contract frontiers, not extra canonical categories.

## 4. Industry / implementation scan beyond Nov 20 merged audit

- [SGLang Unified Memory (Nov 11)](https://www.lmsys.org/blog/2026-11-11-unified-memory): token-lifetime-aware unified allocator vs distinct pools; [SGLang Consortium (Nov 12)](https://www.lmsys.org/blog/2026-11-12-sglang-consortium): multi-vendor governance and source attribution; [SGLang-Neuron](https://www.lmsys.org/blog/2026-11-12-sglang-neuron-v0.1.0) is **Trainium**, not Ascend.
- [vLLM EPD (Nov 11)](https://vllm.ai/blog/2026-11-11-encoder-disaggregation-epd): encoder→prefill→decode and metadata-only DeepSeek V4.1 Flash main-path support; not 910B2 fixed-pair compatibility.
- [NVIDIA MLPerf Endpoints (Nov 16)](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/): trace-level agentic serving, Dynamo routing, cache locality and kernel per-model tuning; GPU/rack/throughput-per-watt denominators must not be conflated.
- [AMD ROCm 10.2 (Nov 18)](https://rocm.blogs.amd.com/ecosystems-and-partners/rocm-10.2-blog/README.html) and [AITER Inductor (Nov 17)](https://rocm.blogs.amd.com/software-tools-optimization/inductor-aiter-conversion/README.html): backend/toolchain releases; not universal model serving speedup.
- [Meta TLX (Nov 10)](https://engineering.fb.com/2026/11/10/open-source/tlx-a-hardware-native-gpu-compiler-for-production-ml/): production ML/RecSys, **not** proof causal-LLM token decoding improvement; authored [Fuse-All TPU MoE](https://arxiv.org/abs/2611.17857) is public research not Meta production deployment.
- ByteDance Seed coauthors [Twindex](https://arxiv.org/abs/2611.25078) and [RSIBench-Infra](https://arxiv.org/abs/2611.24395): independent technical research, not proof shipping engine support in Volcengine.
- Existing [Nov 20 organization release audit](NOVEMBER_2026_INFERENCE_SYSTEMS_REFRESH_20261120.md) already covers Tencent Hy4-flash, Alibaba Qwen4-Max, OpenAI GPT-6.2, Google Gemini4, DeepSeek V4.1, Kimi/MiniMax, TRT-LLM/AMD/SGLang and vLLM-Ascend release compatibility. No need to add duplicate profiles or turn an API update into disclosed Kernel architecture.

## 5. All 90 pre-existing November arXiv-ID canonical papers (before this resweep)

**Note:** `2611.*` metadata is an arXiv numbering-window identifier, not independently verified manuscript first-submission date for every row; see date-conflict hold for MobiInfer. These were not 90 new admissions; they are the required complete pre-existing topic coverage.

### kernels-compilers (14)
- [AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling](https://arxiv.org/abs/2611.26106) — `2611.26106`
- [DTS: Delta-Based Tile Scoring for Efficient Long-Context Sparse Attention](https://arxiv.org/abs/2611.25938) — `2611.25938`
- [TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM Inference](https://arxiv.org/abs/2611.07256) — `2611.07256`
- [FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through Affine Folding](https://arxiv.org/abs/2611.09722) — `2611.09722`
- [Understanding GPU Megakernels: Why Residency Can Mislead](https://arxiv.org/abs/2611.00495) — `2611.00495`
- [KOSMOS: Self-scheduling Persistent Kernels for Communication-Compute Overlap](https://arxiv.org/abs/2611.07477) — `2611.07477`
- [MegaOps: A Kernel Overlapping Framework with PyTorch-like Modularity and Megakernel Performance](https://arxiv.org/abs/2611.16248) — `2611.16248`
- [SubGPU Pipelining: Intra-GPU Fine-Grained Spatial Parallelism for LLM Inference](https://arxiv.org/abs/2611.14904) — `2611.14904`
- [A Fast, Programmable GPU-to-CPU Invocation Layer for GPU-Initiated Communication (KIWI)](https://arxiv.org/abs/2611.23848) — `2611.23848`
- [Together Compiler: Continual Compilation for AI Inference](https://arxiv.org/abs/2611.14681) — `2611.14681`
- [EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities](https://arxiv.org/abs/2611.14356) — `2611.14356`
- [CompoundingKernel: Self-Improving from Zero to First](https://arxiv.org/abs/2611.19230) — `2611.19230`
- [ForgeKernel: Self-Evolving Kernels Catching and Surpassing Experts and Agents](https://arxiv.org/abs/2611.04998) — `2611.04998`
- [Warpline: Binary-Level Tracing and Unified Evidence for Agentic GPU Kernel Optimization](https://arxiv.org/abs/2611.04331) — `2611.04331`

### kv-cache-memory (17)
- [KaleidoKV: Rearranging Evidence for Efficient KV Cache Reuse in Offline RAG Inference](https://arxiv.org/abs/2611.19253) — `2611.19253`
- [DARIC: A Position-Independent KV Cache Reuse System with Distribution-Aware Recomputation](https://arxiv.org/abs/2611.09109) — `2611.09109`
- [MORTIS: Compiler-Guided KV-Cache Management for LLM Agent Programs](https://arxiv.org/abs/2611.08638) — `2611.08638`
- [CacheWeave: Learning to Recompute for Efficient Position-Independent KV Caching](https://arxiv.org/abs/2611.01735) — `2611.01735`
- [RoCoKV: Accelerating LLM Inference Serving through Uncertainty and Redundancy Aware KV Cache Compression](https://arxiv.org/abs/2611.25433) — `2611.25433`
- [Memory-Efficient Speculative Decoding with Quantized Draft KV Cache](https://arxiv.org/abs/2611.20565) — `2611.20565`
- [Intent-Aware Caching for Efficient LLM Serving](https://arxiv.org/abs/2611.09715) — `2611.09715`
- [BasisKV: Value Latents for Communication and Key Routing](https://arxiv.org/abs/2611.02583) — `2611.02583`
- [Rethinking KV Cache Eviction for Agentic LLM Serving](https://arxiv.org/abs/2611.00391) — `2611.00391`
- [LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time](https://arxiv.org/abs/2611.07025) — `2611.07025`
- [TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming](https://arxiv.org/abs/2611.26619) — `2611.26619`
- [TripleKV: Predict, Prefetch, Protect -- KV Cache Management for AI Agents](https://arxiv.org/abs/2611.25112) — `2611.25112`
- [FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving](https://arxiv.org/abs/2611.07542) — `2611.07542`
- [Recompute or Restore? Host-Tier KV for Multi-Model Agent Workflows on a Static-Graph NPU Serving Stack](https://arxiv.org/abs/2611.15126) — `2611.15126`
- [Nebula: Distributed Position-Independent Caching for LLM Serving](https://arxiv.org/abs/2611.09474) — `2611.09474`
- [Beyond Compression Ratio: High-Throughput KV Compression for Disaggregated LLM Serving](https://arxiv.org/abs/2611.04382) — `2611.04382`
- [ReKV: Overlapping Quantized KV Transfer and Suffix Recomputation](https://arxiv.org/abs/2611.08770) — `2611.08770`

### decoding-acceleration (15)
- [ChainFlow: Few-Step Latent Flow Matching for Speculative Decoding](https://arxiv.org/abs/2611.08669) — `2611.08669`
- [Give the Drafter a Second Chance to Guess: Parallel Reconsideration for Speculative Decoding](https://arxiv.org/abs/2611.05724) — `2611.05724`
- [Weights That Stay: On-Chip Megakernels for Serial Heads in Speculative Decoding](https://arxiv.org/abs/2611.00506) — `2611.00506`
- [REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding](https://arxiv.org/abs/2611.14399) — `2611.14399`
- [Phrase-Level Speculative Decoding on a Frozen Target](https://arxiv.org/abs/2611.12464) — `2611.12464`
- [Towards Green Text Generation: Memory-Based Speculative Decoding](https://arxiv.org/abs/2611.16714) — `2611.16714`
- [DForkTree: Accelerating Speculative Decoding with Fork-Aware Block Diffusion Draft Trees](https://arxiv.org/abs/2611.12356) — `2611.12356`
- [D3Tree: Learning to Prune Block-Diffusion Draft Trees for Efficient Verification](https://arxiv.org/abs/2611.11371) — `2611.11371`
- [SpecSearch: Towards Hardware-Aware Efficient Speculative Decoding](https://arxiv.org/abs/2611.22296) — `2611.22296`
- [SpecPilot: Autonomous Algorithm Discovery and Systems Optimization for Speculative Decoding](https://arxiv.org/abs/2611.02501) — `2611.02501`
- [Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models](https://arxiv.org/abs/2611.01617) — `2611.01617`
- [ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding](https://arxiv.org/abs/2611.13442) — `2611.13442`
- [HybridSpec: Throughput-Aware Speculative Decoding for Hybrid GDN-MoE Models](https://arxiv.org/abs/2611.04055) — `2611.04055`
- [SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains](https://arxiv.org/abs/2611.08362) — `2611.08362`
- [Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference](https://arxiv.org/abs/2611.01320) — `2611.01320`

### quantization-compression (6)
- [ResServe: Accurate and Efficient FP4 LLM Inference with Residue Compensation](https://arxiv.org/abs/2611.08713) — `2611.08713`
- [StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference](https://arxiv.org/abs/2611.08363) — `2611.08363`
- [Elastic Precision: Software-Hardware Co-Design of a Mixed-Precision Architecture for Long-Context LLM Inference](https://arxiv.org/abs/2611.00915) — `2611.00915`
- [BitDecoding-FP4: Native FP4 KV Cache Decoding via Algorithm-System Co-Design](https://arxiv.org/abs/2611.09825) — `2611.09825`
- [LoopKV: Loop-Aware KV Cache Compression for Serving Looped Transformers](https://arxiv.org/abs/2611.04137) — `2611.04137`
- [MINE: Entropy-coded Memory-efficient Inference for Large Language Models](https://arxiv.org/abs/2611.09424) — `2611.09424`

### moe-sparse-execution (8)
- [Communicate the Change: Efficient Expert Parallelism via Activation Compression (EchoMoE)](https://arxiv.org/abs/2611.22215) — `2611.22215`
- [GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts](https://arxiv.org/abs/2611.04222) — `2611.04222`
- [ISER-MoE: Dynamic In-Switch Replication of Hot Experts for Load Balancing in Expert-Parallel](https://arxiv.org/abs/2611.09008) — `2611.09008`
- [vExpert: Virtualizing Expert Storage for Adaptive Load Balancing in Distributed MoE Inference](https://arxiv.org/abs/2611.06057) — `2611.06057`
- [Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests](https://arxiv.org/abs/2611.04794) — `2611.04794`
- [Apto: Self-Adaptive CPU-GPU Hybrid MoE Inference on Shared PCs](https://arxiv.org/abs/2611.01859) — `2611.01859`
- [MatMoE: Matryoshka Mixture-of-Experts with Dynamic Mixed-Precision Quantization for Efficient Inference](https://arxiv.org/abs/2611.01704) — `2611.01704`
- [CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention](https://arxiv.org/abs/2611.03200) — `2611.03200`

### runtime-scheduling (12)
- [VelServe: Taming Decode Jitters in LLM Inference with Tail-Calibrated Scheduling](https://arxiv.org/abs/2611.18392) — `2611.18392`
- [Asymptotic Optimality of cμ-Rule for LLM Inference Scheduling under Memory Constraint](https://arxiv.org/abs/2611.04807) — `2611.04807`
- [Not All Loops Cost the Same: Phase-Dependent Depth for Serving Looped Transformers](https://arxiv.org/abs/2611.07211) — `2611.07211`
- [Fairway: Load-Aware KV Cache Reuse for LLM Prefill Scheduling](https://arxiv.org/abs/2611.02082) — `2611.02082`
- [Cap-and-Track: Optimizing LLM Inference Request Dispatch Across Shifting Capacity](https://arxiv.org/abs/2611.24891) — `2611.24891`
- [Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304) — `2611.12304`
- [Ripple: Deadline-Aware CPU-GPU Sharing for Embodied Inference](https://arxiv.org/abs/2611.01067) — `2611.01067`
- [Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls in the Request Queue](https://arxiv.org/abs/2611.26435) — `2611.26435`
- [Serving Agentic Robot Fleets: Workload Characterization, KV-Cache Thrashing, and Admission Control](https://arxiv.org/abs/2611.01404) — `2611.01404`
- [When Cache Pressure Becomes a Trap: Metastability in Agent Serving](https://arxiv.org/abs/2611.02543) — `2611.02543`
- [MobiInfer: Accelerating On-Device GUI Agents with Workload-Aware Inference](https://arxiv.org/abs/2611.08496) — `2611.08496`
- [Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination](https://arxiv.org/abs/2611.16661) — `2611.16661`

### distributed-serving (8)
- [Workload-Static Optical Circuit Switching For Scalable LLM Inference Decode](https://arxiv.org/abs/2611.05104) — `2611.05104`
- [XM-Sparse: High-Throughput Sparse-Attention LLM Serving over Scale-up Memory Pools](https://arxiv.org/abs/2611.22280) — `2611.22280`
- [flash-comm: Self-Synchronizing Collective Communication for LLM Decoding](https://arxiv.org/abs/2611.06634) — `2611.06634`
- [HyCoInfer: Cloud-Edge Collaborative Inference for Large Language Models on Heterogeneous GPU-FPGA Architectures](https://arxiv.org/abs/2611.22086) — `2611.22086`
- [UMLoad: Fast On-Demand Model Loading on Unified Memory Architecture](https://arxiv.org/abs/2611.04253) — `2611.04253`
- [UniExit: A Unified Latency-Aware Early-Exit Runtime for Heterogeneous Edge AI](https://arxiv.org/abs/2611.09159) — `2611.09159`
- [HELIX: HEterogeneous LLM Inference with FleXible and Fine-Grained Partitioning](https://arxiv.org/abs/2611.06513) — `2611.06513`
- [Accelerating LLM Decoding with In-DRAM Parallelism](https://arxiv.org/abs/2611.02401) — `2611.02401`

### benchmarking-analysis (10)
- [Validation-driven Deployment of LLM Inference Platforms for Agentic Workloads](https://arxiv.org/abs/2611.25905) — `2611.25905`
- [Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes](https://arxiv.org/abs/2611.26480) — `2611.26480`
- [ServerBench: How can your coding agents design specialized LLM serving systems?](https://arxiv.org/abs/2611.06841) — `2611.06841`
- [A Controlled Experimental Evaluation of Configuration and Cache Architecture in LLM Serving Engines](https://arxiv.org/abs/2611.05991) — `2611.05991`
- [VLALagBench: Understanding When and Why VLA Inference Latency Matters](https://arxiv.org/abs/2611.03103) — `2611.03103`
- [The GPU Needs an Operating System](https://arxiv.org/abs/2611.08720) — `2611.08720`
- [Where Is VLA Inference Time Spent? Bottlenecks and Optimization Interactions Across GPUs](https://arxiv.org/abs/2611.06710) — `2611.06710`
- [ROCm InferaSim: Cut LLM Serving Trial Costs and Deploy the Best Configuration](https://arxiv.org/abs/2611.04032) — `2611.04032`
- [Inside the Trap: A Renewal Law for Prefix-Cache Collapse in LLM Agent Serving](https://arxiv.org/abs/2611.08902) — `2611.08902`
- [KVGuard: A KV Cache Safety Checker for LLM Serving Systems](https://arxiv.org/abs/2611.06138) — `2611.06138`

## 6. Additional 12 new 2611 IDs

- [Accelerating Mixture of Block Attention via Dynamic Routing, KV-Centric Execution and Runtime Pipelining](https://arxiv.org/abs/2611.26268) — `2611.26268`; kernels-compilers; EVIDENCED
- [AttentionIndex: Accelerating Learned Sparse Attention with a Causal Inverted-File Index](https://arxiv.org/abs/2611.02508) — `2611.02508`; kernels-compilers; EVIDENCED
- [Dissecting an Unexplored SASS Control-Code Field: Barrier Exemption and Programmable Warp Priority](https://arxiv.org/abs/2611.24437) — `2611.24437`; kernels-compilers; EVIDENCED
- [Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization (KernelSeek)](https://arxiv.org/abs/2611.03517) — `2611.03517`; kernels-compilers; EVIDENCED
- [Twindex: Index Cache Offloading with Coarse-to-Fine Selection for Long-Context Sparse-Attention Serving](https://arxiv.org/abs/2611.25078) — `2611.25078`; kv-cache-memory; EVIDENCED
- [Kameleo: In-Situ Activation-Precision Selection for Bit-Serial LLM Accelerators](https://arxiv.org/abs/2611.25971) — `2611.25971`; quantization-compression; EXPLORE
- [OverlapAdvisor: Modeling and Adapting Computation-Communication Overlap for Distributed MoE Serving](https://arxiv.org/abs/2611.11857) — `2611.11857`; moe-sparse-execution; EVIDENCED
- [Fuse-All MoE Inference Kernel with Load Balancing on TPUs](https://arxiv.org/abs/2611.17857) — `2611.17857`; moe-sparse-execution; EVIDENCED
- [Berth: SLO-Preserving GPU Sharing Without New Preemption](https://arxiv.org/abs/2611.25091) — `2611.25091`; runtime-scheduling; EVIDENCED
- [Live Migration of Gated DeltaNet Requests: Exact Catch-Up and the Cost of Log Backlog](https://arxiv.org/abs/2611.26153) — `2611.26153`; distributed-serving; EXPLORE
- [RSIBench-Infra: Can Agents Optimize Their Own Training and Inference Infrastructure at Production Scale?](https://arxiv.org/abs/2611.24395) — `2611.24395`; benchmarking-analysis; EVIDENCED
- [Benchmarking LLM Inference on Desktop-Scale NVIDIA Grace Blackwell Clusters](https://arxiv.org/abs/2611.20289) — `2611.20289`; benchmarking-analysis; EVIDENCED

## 7. Explicit HOLD and uncertainty

- [Timeout Cascades for Coding Agents](https://arxiv.org/abs/2611.24324): policy routing and trace-driven simulation, insufficient distinct low-level engine mechanism for canonical addition.
- [Measuring and Charging for Retained Context](https://arxiv.org/abs/2611.24071): pricing/accounting and scenario model, not executable KV acceleration.
- Generic training-only network or code agents lacking a discrete inference contract are discovery WATCHs, not automatic adds.
- Existing unresolved historical HOLD/identity backlog and time-bounded external site availability remain open. **No assertion of total arXiv universe recall or independent GPU/NPU reproduction.**
