# 2026-11-05 — adjacent-work scope disposition: complete 75-row editorial screening

## Protocol and evidence ceiling

Baseline: `main` at `3d8e108` (prior PR #75), **83 tagged `KEEP_ADJACENT`** across eight mechanisms. [Earlier 8-item review](ADJACENT_SCOPE_REVIEW_20261105.md) covered eight; **the 75 remaining published rows have each received a separate entry below**. This closes the **catalogue-level scope triage**, not an 83-paper full-text methods reproduction. The `INDEXED_SOURCE` label means the catalogue preserves a source link/mechanism but the primary source **was not independently reopened this turn**. No independent GPU/NPU experiment was performed. G0–G5 full-paper quality admission, reproducibility and comparisons remain a separate gate.

### Decision vocabulary

- `RETAIN_SCOPED`: the indexed execution mechanism is relevant, with hardware/task/quality boundary stated. Source evidence/metadata may still require individual re-verification; **not a reproducibility certification**.
- `RECLASSIFIED_KEEP`: the mechanism is worth retaining but its original engineering home was wrong; the paper was moved without changing total.
- `CHECK_G5`: possible low engineering value or modality/transferability gap: **no new endorsement**, requires specific source and closest-baseline re-review.
- `CHECK_EVIDENCE`: claimed measurement, production usage or simulation/reality distinction needs further G3/G4 verification; **no independent performance verdict**.
- `REMOVE_SCOPE`: the formal first-party publication establishes a pure adjacent video-generation algorithm without a specific LLM inference-system mechanism. Remove its canonical row while preserving original source and reason here. This is an editorial boundary **not a claim of poor scientific quality**.

### Accounting

- **83 total prior adjacent labels** = 8 earlier-reviewed + 75 newly screened.
- New 75 outcomes: **58 RETAIN_SCOPED**, **1 RECLASSIFIED_KEEP**, **10 CHECK_G5**, **4 CHECK_EVIDENCE**, **2 REMOVE_SCOPE**.
- Live corpus: **854 → 852** after 2 removals, otherwise one paper per canonical topic. One additional `SOL-ExecBench` migration: Kernels→Benchmarking, corpus count unchanged. Existing reviews are dated snapshots, not corrected retroactively.

**Key first-party corroboration:** [BWCache ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html) demonstrates training-free DiT block feature caching across video diffusion steps, not autoregressive LLM decoding; [Rolling Forcing ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) changes multi-frame denoising, state anchoring and distillation in a video generation model. Both retain merit for World Model / DiT background but not a canonical LLM inference systems entry. [SOL-ExecBench NVIDIA methodology](https://research.nvidia.com/benchmarks/sol-execbench/blog/introducing-sol-execbench) explicitly defines a cross-domain real-GPU kernel benchmarking harness; it belongs in Benchmarking & Systems Analysis.

## Individual decisions for all 75 newly screened rows

### kernels-compilers — 18 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach](https://www.usenix.org/conference/osdi25/presentation/dong) | `RETAIN_SCOPED` | 跨 ISA tensor-program translation 与符号修复，含真实硬件；多 DNN 工作负载，不是独立 LLM Serving TPS。 | primary USENIX |
| [TileLoom: Automatic Dataflow Planning for Tile-Based Languages on Spatial Dataflow Accelerators](https://www.usenix.org/conference/osdi26/presentation/li-wei) | `RETAIN_SCOPED` | MLIR + Tile→空间数据流硬件映射，Tenstorrent 实机 Kernel；无需暗示 Ascend 即插即用。 | primary USENIX |
| [VTC: DNN Compilation with Virtual Tensors for Data Movement Elimination](https://www.usenix.org/conference/osdi26/presentation/hu-muyan) | `RETAIN_SCOPED` | Virtual Tensor Index Mapping 消除 Data Movement，PyTorch Inductor 实现；包含通用 DNN。 | primary USENIX |
| [When and Why to Use TMA: A Workload-Grounded Characterization of Tensor Memory Acceleration on NVIDIA Hopper GPUs](https://arxiv.org/abs/2610.34907) | `RETAIN_SCOPED` | TMA/DSM 访存 crossover 的真实 GPU characterization，FA3/Paged KV 条件限定。 | INDEXED_SOURCE (not independently reopened) |
| [CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs](https://arxiv.org/abs/2605.19269) | `CHECK_G5` | GEMM-Epilogue 抽象与 Fusion 有价值，但原论文明确以训练栈为主要对象；核实推理 Forward 与模型端真实获益。 | primary arXiv |
| [GraCE: Unlocking CUDA Graphs with Compiler Support for ML Workloads](https://www.usenix.org/conference/osdi26/presentation/ghosh) | `RETAIN_SCOPED` | 编译期扩大 CUDA Graph Capture、消除 Parameter Copy；TorchBench/通用 ML 不等同在线 vLLM。 | primary USENIX |
| [Efficient GPU Multitasking with Morphable Kernels](https://doi.org/10.1145/3830418.3843904) | `RETAIN_SCOPED` | 共驻任务 Morphable GPU Kernels，资源干扰可迁移；未报告通用 LLM Goodput。 | INDEXED_SOURCE (not independently reopened) |
| [Theseus: Runtime-Adaptive GPU Collective Communication with Hot-Swappable Schedules](https://doi.org/10.1145/3789240.3829134) | `RETAIN_SCOPED` | Hot-swappable Collective Schedule 是通信 Runtime 机制；强调整机可测链路与拓扑约束。 | INDEXED_SOURCE (not independently reopened) |
| [SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits](https://arxiv.org/abs/2603.19173) | `RECLASSIFIED_KEEP` | 核心贡献是 SOL Bound、测试 Harness 与 Kernel 评测，不是生成/优化 Kernel 的方法；已移到 Benchmarking/Kernel Benchmarks。 | NVIDIA first-party |
| [KPerfIR: Towards a Open and Compiler-centric Ecosystem for GPU Kernel Performance Tooling on Modern AI Workloads](https://www.usenix.org/conference/osdi25/presentation/guan) | `RETAIN_SCOPED` | Triton 编译内置可编程微架构 Profiling，通用工具但可用于 LLM Kernel。 | primary USENIX |
| [KernelBand: Steering LLM-based Kernel Optimization via Hardware-Aware Multi-Armed Bandits](https://proceedings.mlr.press/v306/ran26b.html) | `RETAIN_SCOPED` | 真实 GPU Kernel 搜索 Budget/Bandit 机制，与 Serving 速度分离。 | INDEXED_SOURCE (not independently reopened) |
| [Triton-Sanitizer: A Fast and Device-Agnostic Memory Sanitizer for Triton with Rich Diagnostic Context](https://doi.org/10.1145/3779212.3790241) | `RETAIN_SCOPED` | Triton 记忆体/竞争 Sanitizer 属可复用 Correctness 工具，不直接加速服务。 | INDEXED_SOURCE (not independently reopened) |
| [VibeServe: Can AI Agents Build Bespoke LLM Serving Systems?](https://arxiv.org/abs/2605.06068) | `RETAIN_SCOPED` | Agent 搜索专用 Serving Stack 且有真实端到端负载，但非标准场景收益不能外推。 | INDEXED_SOURCE (not independently reopened) |
| [Ave: Guiding Agentic GPU Optimization Using Data-Flow Invariants (author version: ARGUS)](https://mast.stanford.edu/pubs/argus_agentic_gpu_optimization_guided_by_data_flow_invariants/) | `RETAIN_SCOPED` | Dataflow Invariant 与 SMT 保障 Agentic GPU Kernel Correctness；实测特定 AMD kernels。 | INDEXED_SOURCE (not independently reopened) |
| [JustGoal: With Only a Goal, the AI Baseline Is Above the Expert Kernels](https://arxiv.org/abs/2610.36434) | `RETAIN_SCOPED` | Goal-only kernel agent 是重要对照；仅 B200/Shape/预算约束内比较。 | INDEXED_SOURCE (not independently reopened) |
| [CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution](https://arxiv.org/abs/2608.12629) | `RETAIN_SCOPED` | Typed Compiler IR + Agent/Verifier 搜索；特定 GPU/Operator 收益不可泛化。 | INDEXED_SOURCE (not independently reopened) |
| [CANNBot-CAKE: Collaborative Agentic Kernel Evolution for Ascend NPU](https://arxiv.org/abs/2610.31034) | `RETAIN_SCOPED` | CANN Kernel Agent 具有 Ascend Operator 正确性报告；950PR 不等于 910B2 Serving。 | INDEXED_SOURCE (not independently reopened) |
| [Learning to Formulate: Agentic Hardware-Software Co-Design of AI Infrastructure through Progressive Optimization and Verification (Formulaic)](https://arxiv.org/abs/2610.39380) | `CHECK_EVIDENCE` | 真实 GB10 Layer 与模拟 Ventus 收益是独立子实验；应进一步验证真实 LLM Serving 闭环。 | INDEXED_SOURCE (not independently reopened) |

### kv-cache-memory — 10 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [VLMCache: Efficient On-Device Vision-Language Model Inference](https://doi.org/10.1145/3745756.3809243) | `RETAIN_SCOPED` | Edge VLM 的视觉 Prefix/Region 缓存；KV 一致性但不同于文本 Session。 | INDEXED_SOURCE (not independently reopened) |
| [WorldPlay: Towards Long-Term Geometric Consistency for Real-Time Interactive World Modeling](https://proceedings.mlr.press/v306/sun26az.html) | `CHECK_G5` | WorldPlay 主要是新训练的交互式视频 World Model；Reconstituted Context Memory 属执行状态但模型/训练共设计贡献需拆分。 | primary PMLR |
| [LatentRemedy: Efficient Remedy for Non-Prefix KV Cache Reuse in Multi-Agent Systems](https://arxiv.org/abs/2610.18014) | `RETAIN_SCOPED` | 多 Agent 非 Prefix KV 复用，引入训练 Adapter；必须保留语义/模型改变标签。 | INDEXED_SOURCE (not independently reopened) |
| [FAST-AR: Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://proceedings.mlr.press/v306/samuel26a.html) | `CHECK_G5` | FAST-AR 是纯 AR Video Diffusion 里的 Temporal KV/ANN Attention 优化；评价是否足够一般化为 KV 研究参考。 | primary PMLR |
| [HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://aclanthology.org/2026.acl-long.594/) | `RETAIN_SCOPED` | Multimodal KV 对不同 Head 和视觉 Token 采取异构 Budget；论文及模型场景明确。 | primary ACL |
| [VisCache: Visual KV Cache Pruning for Efficient Vision Large Language Model Inference](https://aclanthology.org/2026.emnlp-main.1196/) | `RETAIN_SCOPED` | VisCache 属视频 VLM KV Pruning，质量保持与实际上下文不可替换为普通文本 KV 结论。 | primary ACL |
| [HERMES: KV Cache as Hierarchical Memory for Efficient Streaming Video Understanding](https://aclanthology.org/2026.acl-long.381/) | `RETAIN_SCOPED` | HERMES 层次化 Streaming Video LLM KV，属于语音/视觉输入持续更新场景。 | primary ACL |

### decoding-acceleration — 10 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [DREAM-S: Speculative Decoding with Searchable Drafting and Target-Aware Refinement for Multimodal Generation](https://aclanthology.org/2026.acl-long.2177/) | `RETAIN_SCOPED` | VLM Draft 架构搜索及目标模型感知修正；需要额外训练，非 Drop-in Spec。 | primary ACL |
| [Multi-Scale Local Speculative Decoding for Image Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) | `CHECK_G5` | 纯图片 AR 的局部拒绝采样/上采样，需证明可迁移到文本 LLM 的 Verify Contract。 | INDEXED_SOURCE (not independently reopened) |
| [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/abs/2606.18967) | `RETAIN_SCOPED` | 动态 RL Policy 的 Quantized Self-drafter，需区分训练 rollout 与 Serving。 | INDEXED_SOURCE (not independently reopened) |
| [GPU-Resident Speculative Decoding for In-Browser LLM Inference with WebGPU](https://arxiv.org/abs/2610.39761) | `RETAIN_SCOPED` | 浏览器 GPU-resident Draft/Verify/KV Loop 消除 CPU Readback，真实 Client GPU 和量化语义。 | primary arXiv |
| [HIPPO: Accelerating Video Large Language Model Inference via Holistic-aware Parallel Speculative Decoding](https://aclanthology.org/2026.emnlp-main.155/) | `RETAIN_SCOPED` | Video LLM 的视觉 Token Selection 与 Draft/Verify Overlap；是实在的 VLM 推测解码。 | primary ACL |
| [Beat the long tail: Distribution-Aware Speculative Decoding for RL Training](https://openreview.net/forum?id=kMeqqPBjSl) | `RETAIN_SCOPED` | RL rollout 长尾导向自适应 Draft Budget，训练 Makespan ≠ 在线 P95。 | INDEXED_SOURCE (not independently reopened) |
| [BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html) | `REMOVE_SCOPE` | ICLR'26 正式论文；纯 Video DiT Block Feature Cache Across Denoising Steps，无 LLM Decode/Serving 执行主体。 | primary ICLR |
| [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) | `REMOVE_SCOPE` | ICLR'26 正式论文；视频扩散多帧联合去噪、Attention Sink 与 Distillation，属于新视频生成算法/模型。 | primary ICLR |
| [Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://arxiv.org/abs/2610.14162) | `CHECK_G5` | NCM 改变 Tokenizer/训练架构实现 Coarse-to-fine Text Generation；属于新模型推理合同，非既有 LLM 加速。 | Stanford first-party |

### quantization-compression — 6 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [Context-Aware Precision Scheduling for Small Language Models](https://arxiv.org/abs/2610.15640) | `RETAIN_SCOPED` | 小型 LLM Context-adaptive Weight Precision Scheduling，额外 Weight Bank 成本需体现。 | INDEXED_SOURCE (not independently reopened) |
| [Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization](https://doi.org/10.1145/3695053.3731019) | `RETAIN_SCOPED` | 在线/离线混合 KV Quantization 与硬件执行内核，属于实际 LLM KV 带宽优化。 | INDEXED_SOURCE (not independently reopened) |
| [JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference](https://doi.org/10.1145/3774934.3786428) | `RETAIN_SCOPED` | RtSmooth + 分层 KV 表示，端到端 Decode 与质量需保持同任务对照。 | INDEXED_SOURCE (not independently reopened) |
| [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157) | `RETAIN_SCOPED` | SGLang 4bit Paged KV 编解码代码，精度/吞吐一致性需要源实验限定。 | INDEXED_SOURCE (not independently reopened) |
| [Read What Matters: Query-Adaptive Quantization for KV Caches (ReadKV)](https://arxiv.org/abs/2610.11245) | `CHECK_EVIDENCE` | Query-Adaptive KV 读取是压缩机制，但目前主要 A10G 单层 Codec 对照；缺多请求 Serving Goodput。 | INDEXED_SOURCE (not independently reopened) |
| [Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization](https://proceedings.mlr.press/v306/xi26f.html) | `RETAIN_SCOPED` | ICML 正式视频 AR KV 量化，实际是 Quality/Memory 与额外 <4% Latency 开销权衡。 | primary PMLR |

### moe-sparse-execution — 6 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [DeepInfer-Mac: Running a 750B-Class MoE on a 24 GB Laptop](https://arxiv.org/abs/2610.36564) | `CHECK_G5` | 750B Mac 的容量可行性和 SSD 专家加载确实可测，但 0.21–0.72 tok/s 不应被包装成高性能服务。 | primary arXiv metadata |
| [Long-Context Modeling with Dynamic Hierarchical Sparse Attention for Memory-Constrained LLM Inference](https://proceedings.mlr.press/v306/xiong26q.html) | `RETAIN_SCOPED` | 动态分层 Sparse Attention + 后端执行，与长文推理质量和稀疏掩码开销相关。 | INDEXED_SOURCE (not independently reopened) |
| [SALE: Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling](https://proceedings.mlr.press/v306/ji26m.html) | `RETAIN_SCOPED` | 低比特近似 QK 生成 Mask，Prefill 实机 Kernel 可测，关注筛选成本。 | INDEXED_SOURCE (not independently reopened) |
| [Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference](https://proceedings.mlr.press/v306/le26c.html) | `RETAIN_SCOPED` | Sketch-and-Walk 动态 Token/Head 选择及稀疏 Kernel，需报告预测开销。 | INDEXED_SOURCE (not independently reopened) |
| [Stochastic Sparse Attention for Memory-Bound Inference](https://proceedings.mlr.press/v306/lee26j.html) | `RETAIN_SCOPED` | Sampling Sparse Attention 在真实 GPU 与 Decode 质量上有系统成本。 | INDEXED_SOURCE (not independently reopened) |
| [Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection](https://proceedings.mlr.press/v306/jo26a.html) | `RETAIN_SCOPED` | 交错动态 Token 选择复用历史层 Token，强调精度与 128K Kernel 边界。 | INDEXED_SOURCE (not independently reopened) |

### runtime-scheduling — 9 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [PlanetServe: A Decentralized, Scalable, and Privacy-Preserving Overlay for Democratizing Large Language Model Serving](https://www.usenix.org/conference/nsdi26/presentation/fang) | `RETAIN_SCOPED` | 真实 LLM 服务的去中心化 Overlay/Privacy/Quality 路由，场景与传统 Serving 不同。 | INDEXED_SOURCE (not independently reopened) |
| [dLLM-Serve: Bridging the Memory Gap in Diffusion Language Model Serving](https://doi.org/10.1145/3797905.3800532) | `RETAIN_SCOPED` | Diffusion LLM 共享 Logit/Activation Budget、Phase Scheduling，确有新 Decoder Execution Contract。 | INDEXED_SOURCE (not independently reopened) |
| [Scaling Up Large Language Models Serving Systems for Semantic Job Search](https://proceedings.mlsys.org/paper_files/paper/2026/hash/0a4c7cdfc0a4eb1b13bb84a9b6220c37-Abstract-Conference.html) | `CHECK_G5` | MLSys 行业案例目前 Catalog 描述过于泛化：需要从原论文提炼可复用的具体系统机制。 | INDEXED_SOURCE (not independently reopened) |
| [Improving GPU Sharing Performance through Adaptive Bubbleless Spatial-Temporal Sharing](https://doi.org/10.1145/3689031.3696070) | `CHECK_G5` | 通用 GPU Bubbleless Sharing，是否有独立 LLM Token Scheduler 证据待查；机制更像资源底座。 | INDEXED_SOURCE (not independently reopened) |
| [LithOS: An Operating System for Efficient Machine Learning on GPUs](https://doi.org/10.1145/3731569.3764818) | `RETAIN_SCOPED` | GPU OS 级 Kernel Atomization 与 TPC Scheduling，可影响共驻请求和 Isolation。 | INDEXED_SOURCE (not independently reopened) |
| [VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference](https://arxiv.org/abs/2512.01031) | `RETAIN_SCOPED` | VLA Action 与异步 Inference 之间的 State Staleness；机器人截止期是一种新执行合同。 | INDEXED_SOURCE (not independently reopened) |
| [Scalable Context Orchestration for Serving LLMs Over Voice (llmovoice)](https://doi.org/10.1145/3830418.3843860) | `RETAIN_SCOPED` | 语音 LLM Context + Runtime Directive 编排，行为/音频质量会改变，非纯 Kernel Speed。 | INDEXED_SOURCE (not independently reopened) |

### distributed-serving — 12 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism](https://proceedings.mlsys.org/paper_files/paper/2026/hash/db988b089d8d97d0f159c15ed0be6a71-Abstract-Conference.html) | `CHECK_G5` | 针对视觉 DiT 的双维稀疏 Attention 并行优化；是否能迁移到文本 LLM EP/CP 需证明。 | INDEXED_SOURCE (not independently reopened) |
| [PROMPTS: Performance Optimization via Multi-Agent Planning for LLM Training and Serving](https://research.google/pubs/prompts-performance-optimization-via-multi-agent-planning-for-llm-training-and-serving/) | `RETAIN_SCOPED` | Profiler-guided Multi-agent 并行拓扑方案优化，训练+Serving 混合生产证据须分开。 | INDEXED_SOURCE (not independently reopened) |
| [StreamDiffusionV2: A Streaming System for Dynamic and Interactive Video Generation](https://proceedings.mlsys.org/paper_files/paper/2026/hash/698cfaf72a208aef2e78bcac55b74328-Abstract-Conference.html) | `RETAIN_SCOPED` | 实时交互视频系统、Rolling KV 与多 GPU Pipeline，面向 World Model Frontier。 | INDEXED_SOURCE (not independently reopened) |
| [UCCL-Tran: An Extensible Software Transport Layer for GPU Networking](https://www.usenix.org/conference/osdi26/presentation/zhou-yang) | `RETAIN_SCOPED` | RDMA/GPU Networking 传输/控制平面解耦，对集群数据路径可迁移，非直接 P/D KV Speed。 | INDEXED_SOURCE (not independently reopened) |
| [Deploying RDMA for Large-Scale Inference and Training Workloads (ByteExpress)](https://arxiv.org/abs/2610.12815) | `RETAIN_SCOPED` | 字节 ByteExpress 生产推理参数 Fetch/RDMA 工程；不是 vLLM KV Transfer。 | INDEXED_SOURCE (not independently reopened) |
| [Resuming Vision-Language Inference across Onboard Interruptions (OrbitWeaver)](https://arxiv.org/abs/2610.29183) | `CHECK_EVIDENCE` | 卫星在轨 VLM 恢复的生产部署/性能为作者声明；公开可复现实验和测量边界需额外检查。 | INDEXED_SOURCE (not independently reopened) |
| [TensorHub: Scalable and Elastic Weight Transfer for LLM RL Training](https://arxiv.org/abs/2604.09107) | `CHECK_G5` | LLM RL Policy→Rollout Worker 的权重同步，不同于在线请求的 KV/状态传输。 | INDEXED_SOURCE (not independently reopened) |
| [Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference](https://doi.org/10.1145/3731569.3764808) | `RETAIN_SCOPED` | 真实 SoC CPU/GPU/NPU LLM inference characterisation，属于端侧 Execution 分区。 | INDEXED_SOURCE (not independently reopened) |
| [ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference](https://doi.org/10.1145/3745756.3809205) | `RETAIN_SCOPED` | 移动 NPU Attention fallback + Shadow Attention 有实机硬件/兼容性范围。 | INDEXED_SOURCE (not independently reopened) |
| [MeshRT: Compile-Time Governed Wafer-Scale Runtime for Low-Latency High-Throughput Inference](https://doi.org/10.1145/3830418.3843856) | `RETAIN_SCOPED` | Wafer-scale distributed core scheduling & compilation，硬件特殊但有 LLM 推理机制。 | INDEXED_SOURCE (not independently reopened) |

### benchmarking-analysis — 12 initially tagged

| Paper / primary source | Editorial screen | Why / exact boundary | Evidence checked |
|---|---|---|---|
| [Towards Efficient Large Multimodal Model Serving](https://arxiv.org/abs/2502.00937) | `RETAIN_SCOPED` | 多模态 LLM serving Trace/Profiling 真实任务，模型结构与云端负载分离评价。 | INDEXED_SOURCE (not independently reopened) |
| [Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://proceedings.mlr.press/v306/zhou26e.html) | `RETAIN_SCOPED` | VLA 各异构处理器 Roofline 和 Perception→Action Latency 测量，边缘硬件限定。 | INDEXED_SOURCE (not independently reopened) |
| [XProf: An Open, Scalable, and Extensible Profiling System for the Modern ML Stack](https://proceedings.mlsys.org/paper_files/paper/2026/hash/280776fda5970060e6a5efcfd43e5d2d-Abstract-Conference.html) | `RETAIN_SCOPED` | XProf TPU/GPU full-stack Profiler 有实测，通用 ML 工具须确认 LLM 路径。 | INDEXED_SOURCE (not independently reopened) |
| [ProMCP: Profiling Token Flows and Latency Costs in Model Context Protocol–Based LLM Agents](https://aclanthology.org/2026.findings-acl.1967/) | `RETAIN_SCOPED` | Agent MCP 的 Host/Client/Server Token/Latency Attribution；工具调用成本与 GPU Engine 分开。 | INDEXED_SOURCE (not independently reopened) |
| [Matching Workloads to Blackwell: Power-Resolved Benchmarking of NVIDIA B200 and B300 across HPC and AI Workloads](https://arxiv.org/abs/2610.41919) | `RETAIN_SCOPED` | B200/B300 电力分辨率测量含 LLM 与 HPC，软件版本变化会混淆硬件归因。 | INDEXED_SOURCE (not independently reopened) |
| [TokenSim: Enabling Hardware and Software Exploration for Large Language Model Inference Systems](https://arxiv.org/abs/2503.08415) | `CHECK_EVIDENCE` | TokenSim 声称较低模拟误差，但须核对校准 Workloads/Hardware，不能把单一低误差当普适保证。 | INDEXED_SOURCE (not independently reopened) |
| [GPU-Tile-Sim: A Tile-Centric GPU Simulation Framework for LLM Hardware-Software Co-Design](https://arxiv.org/abs/2607.11262) | `RETAIN_SCOPED` | Tile-graph Simulator 有真实 GPU Kernel 校准，模拟器结果不等于真实 Serving TPS。 | INDEXED_SOURCE (not independently reopened) |
| [COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies](https://arxiv.org/abs/2610.33404) | `RETAIN_SCOPED` | MoE Expert Residency/Offload Policy Emulation，策略误差改善而非 Engine 加速。 | INDEXED_SOURCE (not independently reopened) |
| [Dissecting the Carbon-SLO Tension in Geo-Distributed LLM Serving](https://arxiv.org/abs/2610.14571) | `RETAIN_SCOPED` | Carbon-SLO 的地理集群模拟以实机 Prefill/Decode Power 校准，排放/SLO 为模拟结论。 | INDEXED_SOURCE (not independently reopened) |
| [AscendKernelGen: LLM-Driven Kernel Generation for NPUs](https://aclanthology.org/2026.findings-acl.1533/) | `RETAIN_SCOPED` | Ascend KernelGen/Benchmark 有真实 NPU Compile/Correctness；不是 LLM Engine Goodput。 | INDEXED_SOURCE (not independently reopened) |
| [CommBench: Can LLMs Write Correct and Efficient GPU Communication Code?](https://arxiv.org/abs/2608.04450) | `RETAIN_SCOPED` | Communications Kernel Bench 有多卡通信/正确性评测，任务集与 vLLM 集成不同。 | INDEXED_SOURCE (not independently reopened) |
| [EdgeKernelBench: Unified LLM-Driven Kernel Generation for Edge Backends](https://arxiv.org/abs/2610.24648) | `RETAIN_SCOPED` | 端侧 CPU/GPU/Vulkan/OpenCL Kernel Benchmark，特定设备/任务约束清楚。 | INDEXED_SOURCE (not independently reopened) |

## G0–G5 follow-up order (not silently counted as complete)

**High-priority scope:** CODA (train-focused Fusion), WorldPlay/FAST-AR (video-model co-design), Multi-Scale Local Speculative Decoding (image-only), Next-Concept Modeling (new tokenizer/model), generic semantic-job-search serving, GPU-sharing Bless, db-SP (visual DiT), TensorHub (RL policy weights) and DeepInfer-Mac (storage-feasible but very-low-throughput). Ask whether each offers a generalizable **executed LLM-inference mechanism** beyond a neighboring application.

**High-priority G3/G4 evidence:** Formulaic's mixed GB10 Layer/ventus simulation, ReadKV's single-layer codec vs full Serving, OrbitWeaver's author-only satellite deployment claim and TokenSim's simulator calibration envelope.

**Required source comparison for any future removal:** authoritative publication + closest prior/strongest baseline + workload/hardware and model-quality parity + expected modern vLLM/SGLang/Ascend learning value. Keep a dated receipt and update counts in the same PR; no mechanical deletion by venue, benchmark size or `KEEP_ADJACENT` marker.

**Sources and limits:** Individual links above are original bibliography source pointers. Rows marked `INDEXED_SOURCE` are **source-linked screening judgments**, not independently source-opened proofs. Citations here describe reported work, not locally reproduced speedups; no paper is promoted to fully verified on the strength of this ledger alone.
