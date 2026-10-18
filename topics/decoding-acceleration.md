# Decoding Acceleration

Breaking the sequential decode bottleneck through draft/verify, parallel prediction, token-tree verification and diffusion-LLM decoding schedules.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Decoding-path mechanisms lead this category: draft/verify and speculative sampling, training-free or retrieval drafting, self-speculation and layer skipping, candidate-tree and parallel drafting, verification execution, adaptive/online speculation control, and diffusion-LLM (dLLM) decoding schedules. Choose here when the decisive reusable mechanism changes token acceptance or verification; SLO-aware request admission, routing or fleet scheduling belongs to Runtime & Scheduling even when it schedules speculation, KV eviction/compression to KV Cache & Context Memory, fused draft/verify kernels to Kernels & Compilers, numeric weight/activation representation to Quantization & Compression, and sparse-attention algorithms to MoE & Sparse Execution. Entries are classified by their decisive reusable mechanism, never by model family, workload, hardware or claimed speedup.

**Foundational context.** See also: [Blockwise Parallel Decoding (2018), Speculative Decoding (2023), Medusa (2024), SpecInfer (2024)](../README.md#foundational-and-influential-papers); rows here that originate a sub-direction of this taxonomy carry an inline `KEEP_FOUNDATIONAL` tag.

## Mechanism map

Nine internal groups, **71 canonical entries in total**. Subsections are a reading/navigation structure, **not new public categories** and not G0–G5 admission verdicts.

| Research mechanism | Papers |
|---|---:|
| [Drafter Design, Training & Target Pairing](#drafter-design-training--target-pairing-14) | 14 |
| [Training-Free, Retrieval & N-gram Speculation](#training-free-retrieval--n-gram-speculation-4) | 4 |
| [Self-Speculative & Layer-Skipping Decoding](#self-speculative--layer-skipping-decoding-5) | 5 |
| [Tree, Parallel Drafting & Verification Execution](#tree-parallel-drafting--verification-execution-7) | 7 |
| [Adaptive & Online Speculation Control](#adaptive--online-speculation-control-8) | 8 |
| [Heterogeneous, Edge & Distributed Speculation](#heterogeneous-edge--distributed-speculation-4) | 4 |
| [Diffusion & Non-Autoregressive LLM Decoding](#diffusion--non-autoregressive-llm-decoding-14) | 14 |
| [Adjacent Modality & Cross-Topic Boundary](#adjacent-modality--cross-topic-boundary-11) | 11 |
| [Long-Context & MoE-Specific Speculation](#long-context--moe-specific-speculation-4) | 4 |
| **Total** | **71** |

### Where this taxonomy came from

- vLLM（Ascend 侧文档）把投机解码写成 Proposer/Verifier 两段：`ngram`、`suffix`、`medusa`、`eagle`、`eagle3`、`mtp`、`dflash`、`draft_model`、`extract_hidden_states` 作为可替换的 Proposer，再配 Rejection Sampler 与可选 Block Verify/Entropy Verify，并用 `num_speculative_tokens` 控制每次前向的候选数；这支撑了本文件把「草稿器设计/训练」「免训练来源」「自投机」分成不同组（[vLLM Speculative Decoding 指南](https://docs.vllm.ai/projects/ascend/en/v0.23.0rc1/_sources/user_guide/feature_guide/speculative_decoding.md)）。
- SGLang 把 EAGLE/EAGLE3/NEXTN/STANDALONE 作为并列投机算法，把 `speculative_eagle_topk` 的树分枝、接受阈值与 `--disable-overlap-schedule` 的验证重叠分别曝光，并**单独设有 Adaptive Speculative Decoding 文档页**，对应本文件的「树/并行草稿与验证执行」与「自适应在线控制」两组（[SGLang Speculative Decoding](https://docs.sglang.io/docs/advanced_features/speculative_decoding)、[SGLang Adaptive Speculative Decoding](https://docs.sglang.io/docs/advanced_features/adaptive_speculative_decoding)、[SGLang-JAX Speculative Decoding](https://github.com/sgl-project/sglang-jax/blob/main/docs/features/speculative_decoding.md)）。
- TensorRT-LLM 把 Draft-Target-Model、NGram、Medusa、ReDrafter、EAGLE/EAGLE-3（含 **Disaggregated Serving**）、Lookahead、MTP 与用户显式 Draft Token 做成一等配置类；其 DeepSeek R1 MTP 实现笔记给出 MTP Vanilla 与 MTP-Eagle 两条路线、放宽接受准则与拒绝 Draft 的 KV Cache 回退，直接对应本文件的 MTP 头归属与「近似接受」边界（[TensorRT-LLM Speculative Sampling](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html)、[TensorRT-LLM DeepSeek R1 MTP](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog02_DeepSeek_R1_MTP_Implementation_and_Optimization.html)）。
- 边缘/消费级设备上，MLX-Swift 的 `speculative-decoding` 以 Draft/Target 模型对（含 Mamba Drafter 与 `numDraftTokens`）在 Apple Silicon 上运行，与本文件记录的 Dovetail（CPU/GPU 异构）、Cassandra（Edge 自投机）与 Mirror（GPU/NPU 异构）属于同一部署语境（[mlx-community/speculative-decoding](https://github.com/mlx-community/speculative-decoding)）。
- Diffusion LLM 已成为独立子方向：Fast-dLLM 以 Block-wise Approximate KV 与置信度并行提交加速 LLaDA/Dream，dLLM-Serve（ICS 2026）把扩散 LM Serving 的显存缺口当作系统问题处理；社区综述则把 Multi-Token Prediction、Diffusion LMs、Multimodal、Long-Context 与 MoE 投机列为相互独立的章节，支撑本文件的第 7、9 组（[Fast-dLLM](https://nvlabs.github.io/Fast-dLLM/)、[dLLM-Serve (ICS 2026)](https://dl.acm.org/doi/full/10.1145/3797905.3800532)、[SpeculativeDecodingPapers](https://github.com/hemingkx/SpeculativeDecodingPapers)）。

**Coverage gaps for later discovery — not new admissions:** ① 免训练侧缺少 Arctic Inference 式 Suffix/Tree 解码与 Token Recycling 的独立条目（现仅由 Lookahead、SSSD、UniSpec 代表）；② 缺少 TensorRT Model Optimizer 生成 ReDrafter/Medusa/EAGLE 草稿检查点的训练侧条目；③ 语法/结构化输出约束下的投机、语音与视频 Token 级投机仍是空档；④ PD 分离部署中 `num_speculative_tokens` 的预算分配与 Draft KV 显存管理没有独立条目；⑤ 缺少 Spec-Bench 式投机解码基准与接受长度/草稿成本的系统测量条目；⑥ 机制缺失不作为把「仅实现细节」材料当作论文引入的理由，草稿-验证 Kernel 融合仍归 Kernels & Compilers。

## Papers (71)

### Drafter Design, Training & Target Pairing (14)

**草稿器的构造与配对**：特征级/跨层隐藏态草稿、蒸馏与对齐训练、MTP/并行草稿头、位置与专家专业化的草稿模块、草稿词表收缩，以及 Draft 与 Target 词表或 Tokenizer 异构时的配对与概率重映射。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2023 | [Speculative Decoding: Exploiting Speculative Execution for Accelerating Seq2seq Generation](https://aclanthology.org/2023.findings-emnlp.257/) | Findings EMNLP 2023 | 提出早期 Seq2seq Speculative Execution 与验证方案，是后续损失无关 Draft/Verify 体系的前驱。（KEEP_FOUNDATIONAL） |
| 2024 | [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8766fbc68e1ed1cdef712ce273e0a363-Abstract-Conference.html) | ICLR 2024 | 以蒸馏优化 Draft Model 与 Target 的接受概率，减少验证开销。 |
| 2024 | [EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://proceedings.mlr.press/v235/li24bt.html) | ICML 2024 | 在倒数第二层特征空间预测草稿，修正 Feature Uncertainty；评测生成速度与分布保持。 |
| 2025 | [Accelerating LLM Inference with Lossless Speculative Decoding Algorithms for Heterogeneous Vocabularies](https://proceedings.mlr.press/v267/timor25a.html) | ICML 2025 | 消除 Draft 与 Target 必须共享 Tokenizer/Vocabulary 的约束，保留目标采样分布。 |
| 2025 | [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c7b5a35ea98b62512a869c19ea7b03cb-Abstract-Conference.html) | NeurIPS 2025 | 跨层 Feature Fusion 与 Training-time Test 优化 Speculative Drafter，增加高概率接受 Token。 |
| 2026 | [HCSpec: Two-Tier Horizontal Cascade Speculative Decoding for High-Efficiency Large Language Model Inference](https://aclanthology.org/2026.acl-long.353/) | ACL 2026 | 根据 Draft 位置边际价值递减采用重/轻双层级 Draft 模块并横向级联；与 EAGLE-3 有端到端加速对照，需计入额外 Draft 训练和维护。 |
| 2026 | [Jakiro: Boosting Speculative Decoding via Decoupled MoE](https://aclanthology.org/2026.acl-long.487/) | ACL 2026 | 将位置共享特征的 Draft 解耦为多 Expert 路径，配合 Contrastive Enhanced Parallel Decoding 增加候选多样性；作者推理实验与 Strong Draft Baseline 对照，未独立复现。 |
| 2026 | [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/abs/2606.18394) | arXiv 2026 (formerly JetFlow) | 训练基于 Frozen Target Fused Hidden States 的 Causal Parallel Draft Head，单次 Forward 并行生成树并整体 Verify；H100/B200 GPU 与 vLLM 集成实测 Speculative Acceptance、延迟和端到端解码。 |
| 2026 | [NanoSpec: Accelerating Speculative Decoding using Minimalist In-Context Vocabularies](https://proceedings.mlr.press/v306/chen26fm.html) | ICML 2026 | 动态收缩 Draft 词表，并以异步 Gather/GPU 驻留状态克服稀疏访存瓶颈，报告端到端推测解码收益。 |
| 2026 | [PARD: Accelerating LLM Inference with Low-Cost Parallel Draft Model Adaptation](https://openreview.net/pdf/1effe7e77a921bb4b55fe9a203cee43f0674fc6d.pdf) | ICLR 2026 | Conditional Drop-token 训练使单次 Draft Forward 并行产生多个候选 Token，Target-independent Draft 可跨模型复用；作者有 vLLM 实测与公开代码，适合复现。 |
| 2026 | [PRISM: Parametrically Refactor Inference for Speculative Decoding Draft Models](https://openreview.net/forum?id=cvU2HuuxEf) | MLSys 2026 | PRISM（MLSys 2026）对 speculative decoding 中的 draft 模型推理做参数化重构，在保持验证阶段正确性的前提下降低草稿生成的算力与延迟开销，从而提升草稿生成效率与验证吞吐量（HOLD_IDENTITY） |
| 2026 | [SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding](https://proceedings.mlsys.org/paper_files/paper/2026/hash/041dad5ed2191b44ba3ed0e00cdc3187-Abstract-Conference.html) | MLSys 2026 | 使用离散扩散并行 Drafter 与自回归验证器对齐，提高接受率。 |
| 2026 | [SPEED: Specialized Position Experts for Efficient Speculative Decoding](https://openreview.net/forum?id=ugRJVwcjbZ) | COLM 2026 (full paper; author alias PosS) | 通过按 Draft Position 专业化小型 Draft Expert，缓解累积 Feature Deviation，提升后位置 Acceptance。**G0 别名已由作者 [代码 README](https://github.com/shrango/PosS) 明确确认：SPEED=旧版 PosS**；代码现支持 SpecForge 训练、EAGLE-2/EAGLE-3 Backbone 与 [vLLM 下 SPEED(E3)/EAGLE-3 对照脚本](https://github.com/shrango/PosS)。原 2025 PosS v1 在 Llama3-8B/Llama2-13B 六任务报告相比 HASS 最多 +5.7% 相对加速，**不能直接套用成 2026 正式 SPEED(E3) 的收益**；待核实最终论文实机、Draft Cost、Batch/SLO Goodput 与数值完全可复现。（HOLD_EVIDENCE） |
| 2026 | [TokenTiming: A Dynamic Alignment Method for Universal Speculative Decoding Model Pairs](https://aclanthology.org/2026.acl-long.1983/) | ACL 2026 | 以 Dynamic Time Warping 对齐不同 Tokenizer 的 Draft/Target 序列，并重新映射概率以避免重训练专用 Draft Model；作者报告约 1.57× 加速，Tokenizer 对齐成本和精确采样约束待复核。（HOLD_EVIDENCE） |

### Training-Free, Retrieval & N-gram Speculation (4)

**免训练与检索式候选来源**：Prompt/Suffix N-gram 匹配、检索增强的短上下文 Draft、Jacobi 式并行序列修正等不训练新神经草稿器的候选生成，并做硬件感知的部署适配。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [Break the Sequential Dependency of LLM Inference Using Lookahead Decoding](https://proceedings.mlr.press/v235/fu24a.html) | ICML 2024 | 以 Jacobi 风格的并行序列修正与 N-gram 验证加速自回归推理，减少独立 Draft Model 依赖。 |
| 2025 | [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://proceedings.mlr.press/v267/chen25s.html) | ICML 2025 | 构建基于检索短上下文的 Draft LLM 来推测长上下文 Target 的生成结果。 |
| 2026 | [SSSD: Simply-Scalable Speculative Decoding](https://aclanthology.org/2026.acl-long.1530/) | ACL 2026 | 无训练 N-gram Matching 搭配 Hardware-aware Speculation，降低引入辅助 Draft 模型的部署门槛；作者在多领域和长上下文报告延迟收益，非自动保证线上 Goodput。 |
| 2026 | [UniSpec: Training-Free Speculative Decoding for Robust LLM Acceleration Across Languages and Hardware](https://aclanthology.org/2026.acl-long.285/) | ACL 2026 | 设备校准的 Draft 大小、N-gram Confidence Scoring 与 Speculation Tree Expansion，跨语言多硬件免训练投机解码；作者发布代码与 Benchmark，并声称保持自回归输出质量，未复现。 |

### Self-Speculative & Layer-Skipping Decoding (5)

**目标模型自投机**：以层跳过/早退、剪枝或互补量化的自草稿替代独立外部 Draft 模型，并用验证结果反过来指导稀疏注意力与 KV 复用。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [QSpec: Speculative Decoding with Complementary Quantization Schemes](https://aclanthology.org/2025.emnlp-main.240/) | EMNLP 2025 | 用低精度权重+激活 Draft 与高精度 Weight-only Verify 共享权重及 KV，避免独立 Draft 模型/重训练；作者测试 Batch Decode 质量与性能，旧账本误记 EMNLP 2026。 |
| 2026 | [Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding](https://proceedings.mlsys.org/paper_files/paper/2026/hash/66a026c0d17040889b50f0dfa650e5e0-Abstract-Conference.html) | MLSys 2026 | SpecGen 利用 PillarAttn 稀疏 Draft、延迟验证和运行时 KV 管理。 |
| 2026 | [ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference](https://arxiv.org/abs/2609.17943) | COLM 2026 | 统一 Mixed Forward 允许不同请求异步 Draft/Verify，按 Acceptance Rate 自适应 Draft 长度并在中间层刷新 Sparse Context；正式 COLM 2026 名单与公开 Benchmark+逐请求计时/Token Hash 工程已查证，速度提升仍为作者报告。 |
| 2026 | [Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding](https://doi.org/10.1109/ISCA66397.2026.00022) | ISCA 2026 | 使用剪枝和尾数截断实现无需训练的轻量 Self-speculative Drafter，并在消费级 GPU 验证。 |
| 2026 | [Vegas: Self-Speculative Decoding with Verification-Guided Sparse Attention](https://proceedings.mlr.press/v306/yue26a.html) | ICML 2026 | Verify 阶段复用 KV 重要性信息，为后续 Self-speculative Draft 加速。 |

### Tree, Parallel Drafting & Verification Execution (7)

**候选组织与验证执行**：动态/各向异性候选树与固定验证预算分配、批量与树验证、Draft/Verify 异步重叠、单次 Forward 内融合 Diffusion-Draft 与 AR-Verify，以及把精确匹配放宽为语义接受的验证准则。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees](https://aclanthology.org/2024.emnlp-main.422/) | EMNLP 2024 | 依据上下文相关的接受率动态构造 Draft Tree，区别于静态树推测路径。 |
| 2026 | [Accelerating Speculative Decoding with Block Diffusion Draft Trees](https://arxiv.org/abs/2604.12989) | COLM 2026 (accepted; author preprint) | **DDTree** 以 Block Diffusion *Drafter* 的逐位置概率构造固定节点预算的 Best-first Speculation Tree，使用祖先掩码单次验证 AR Target；不同于直接服务 Diffusion LM。作者提供 [CUDA/PyTorch Benchmark](https://github.com/liranringel/ddtree)，与 DFlash、EAGLE-3 等 Draft Baseline 比较；仅作者报告的单请求/Benchmark 速度，在线 Batch/SLO Goodput 未核验。（HOLD_EVIDENCE） |
| 2026 | [Calibrated Speculative Decoding: Frequency-Guided Candidate Selection for Efficient Inference](https://aclanthology.org/2026.acl-long.1369/) | ACL 2026 | Draft/Verify 候选树或多 Token 解码的执行/验证开销；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [Goose: Anisotropic Speculation Trees for Training-Free Speculative Decoding](https://arxiv.org/abs/2604.02047) | COLM 2026 (accepted; author preprint) | **GOOSE** 用 Prompt N-gram Match 的可靠 Deep Spine 配合基于历史 Logits 的 Wide Branch，非对称分配固定 Tree Verification Budget；作者在 A40/2×A100、5 模型 × 5 任务、Batch=1 Greedy 下报告严格相同输出与墙钟速度，对比 PLD、Token Recycling、REST、Lookahead、EAGLE-2，代码含 [Test/Benchmark](https://github.com/2kinto/GOOSE_Speculative_Decoding)；未测在线并发/随机 Sampling。 |
| 2026 | [Talon: Breaking the Synchronization Barrier in Speculative Decoding with Hybrid Model-based and Retrieve-based Drafting](https://doi.org/10.1609/aaai.v40i25.39266) | AAAI 2026 (Full Paper) | 通过 Asynchronous Draft/Verify 执行与混合 Model-based/Retrieval-based Drafting 减轻同步等待并改善不同领域接受率；作者报告 Vicuna/DeepSeek/LLaMA 多任务与 EAGLE/Hydra/Medusa 等对照。推理分布等价性、硬件并发开销及与现代批处理 Serving Goodput 仍待审。（HOLD_EVIDENCE） |
| 2026 | [TiDAR: Think in Diffusion, Talk in Autoregression](https://proceedings.mlsys.org/paper_files/paper/2026/hash/1367d856028f65a9555b0274db09e608-Abstract-Conference.html) | MLSys 2026 | 在一次 Forward Pass 中执行 Diffusion Draft 与自回归采样，用结构化 Attention Mask 实现推测式并行生成。 |
| 2026 | [Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match](https://proceedings.iclr.cc/paper_files/paper/2026/hash/acb94e709f02895fd98b5867f0b184f3-Abstract-Conference.html) | ICLR 2026 | FLy 将精确匹配放宽为熵门控和延迟验证窗口，利用目标模型自纠正行为接纳语义等价 Draft；在 70B/405B 模型上测得端到端加速，但不保证与严格 Speculative Decoding 的输出分布恒等。（APPROXIMATE_QUALITY_CHECKED） |

### Adaptive & Online Speculation Control (8)

**在线投机策略控制**：按接受率、置信度或熵自适应 Draft 深度与宽度，按 SLO 或验证成本预算分配投机开销，以及多 Draft 模型在线选择与强化学习策略。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving](https://github.com/cerebellumking/AdaSpec) | SoCC 2025 | 在线感知请求负载与设备环境，动态改变 Draft/Verify 策略，在多 SLO 工作负载下控制投机成本。 |
| 2026 | [AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding](https://dl.acm.org/doi/10.1145/3767295.3769315) | EuroSys 2026 | 按请求 SLO 设计 Speculative Draft/Verify 策略，将加速与服务目标联动。 |
| 2026 | [D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://arxiv.org/abs/2607.14647) | arXiv 2026 (preprint) | 跨请求按 Draft Confidence 分配 Verification Budget，以设备和 Parallelism Cost Model 自适应裁剪 Depth；Dense 和 MoE 高并发实测 Speculation 验证开销与吞吐。 |
| 2026 | [ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios](https://proceedings.mlr.press/v306/hu26ar.html) | ICML 2026 | 在 SGLang 统一 Batch Super-tree 上使用 Sparse Confidence Gating 动态分配 Draft 深度/宽度及 Verify 计算预算；覆盖 Qwen3-235B 与高并发吞吐对照。 |
| 2026 | [EDSD: Entropy-Driven Design for Faster Speculative Decoding](https://aclanthology.org/2026.acl-long.2145/) | ACL 2026 | Draft/Verify 候选树或多 Token 解码的执行/验证开销；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [HeteroSpec: Leveraging Contextual Heterogeneity for Efficient Speculative Decoding](https://aclanthology.org/2026.acl-long.589/) | ACL 2026 | 根据候选 Token 的预测 Entropy 分组，动态决定 Speculative Draft 深度及验证预算，减少高置信 Token 的冗余 Verification；作者报告四模型解码加速且保持输出分布。 |
| 2026 | [Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/34345e243156da67605d4b63d71c8d98-Abstract-Conference.html) | ICLR 2026 | 通过两个协同 RL Policy 直接优化 Draft/Verify 实际执行时间，而非仅优化 Acceptance Length；多模型解码评估，政策训练成本需计入。 |
| 2026 | [Not-a-Bandit: Provably No-Regret Drafter Selection in Speculative Decoding for LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/20563b8508ba42e1b688d922e926ee26-Abstract-Conference.html) | ICLR 2026 | 利用一次 Target Verification 的反馈估计多个 Draft 模型，并建立有无遗憾保证的在线选择策略；有算法/系统开销和解码实验，适用多 Drafter 场景。 |

### Heterogeneous, Edge & Distributed Speculation (4)

**异构与分布式投机执行**：把 Draft 与 Verify 拆到 CPU/GPU/NPU、边云或分布式设备上，包括减小验证通信粒度、异构并行早退路径与投机失败造成的显存冗余控制。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [Dovetail: A CPU/GPU Heterogeneous Speculative Decoding for LLM inference](https://aclanthology.org/2025.emnlp-main.879/) | EMNLP 2025 | 在消费级异构设备上将 Draft 部署 GPU、Target Verification 放于 CPU，设计减小验证通信粒度的无损投机解码；真实设备 13B 推理，旧账本误记 EMNLP 2026。 |
| 2025 | [Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference](https://arxiv.org/abs/2510.13161) | arXiv 2025 (preprint) | 在 GPU/NPU 异构并行执行 Draft 早退路径与 Target 后缀，并用多 Token Speculative Streaming 打破串行 Draft 路径；作者用 14B–66B 模型端到端实测。 |
| 2025 | [SpecMemo: Speculative Decoding is in Your Pocket](https://arxiv.org/abs/2506.01986) | arXiv 2025 (preprint) | 以细粒度 Token/Mem Allocation 抑制投机失败造成的冗余 KV 显存占用，并扩展分布式 Batched Draft-Verify；作者在 Titan RTX 与八卡 AMD MI250 实测。 |
| 2026 | [E$^2$-SCI: Elastic Edge-Cloud Speculative Decoding via Credit Inertia](https://openaccess.thecvf.com/content/CVPR2026/html/Li_E2-SCI_Elastic_Edge-Cloud_Speculative_Decoding_via_Credit_Inertia_CVPR_2026_paper.html) | CVPR 2026 | 边云分离的投机解码与分布式验证；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |

### Diffusion & Non-Autoregressive LLM Decoding (14)

**文本 Diffusion/非自回归 LLM 的解码调度**：块并行提交与 Block Size 自适应、扩散 KV 缓存与预算、去噪步早期跳过与语义感知去噪（LLaDA/Dream 系 serving 侧机制）。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [AdaBlock-dLLM: Semantic-Aware Diffusion LLM Inference via Adaptive Block Size](https://openreview.net/pdf?id=0Cv9PwL7cI) | ICLR 2026 | 以语义分隔符置信度和 Volatility Band 动态选择半自回归 DLM 的 Block Size；训练免改造，有 Dream/LLaDA 可执行代码，质量-吞吐需要配套审查。 |
| 2026 | [Attention Is All You Need for KV Cache in Diffusion LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3afaa2102fb8ea44cbadc13e45bba718-Abstract-Conference.html) | ICLR 2026 | Diffusion LM 的并行解码、缓存复用与去噪迭代压缩；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes](https://proceedings.iclr.cc/paper_files/paper/2026/hash/91a23b3e6a2ebaad62e17d0269f88c6b-Abstract-Conference.html) | ICLR 2026 | Diffusion LM 的并行解码、缓存复用与去噪迭代压缩；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [CDLM: Consistency Diffusion Language Models for Faster Sampling](https://proceedings.mlsys.org/paper_files/paper/2026/hash/054de805fcceb78a201f5e9d53c85908-Abstract-Conference.html) | MLSys 2026 | 通过一致性建模降低 Diffusion LM 的 Refinement Steps，并通过 Block Causal Mask 与微调实现可复用 KV；训练-推理协同加速，开源实验代码，非无需重训练的纯 Runtime 系统。（REQUIRES_FINETUNING） |
| 2026 | [DSB: Dynamic Sliding Block Scheduling for Diffusion LLMs](https://proceedings.mlr.press/v306/luo26o.html) | ICML 2026 | 自适应滑动 Block 和配套 KV Cache 提升扩散语言模型的并行生成效率。 |
| 2026 | [DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection and Partial Attention](https://proceedings.mlr.press/v306/lee26i.html) | ICML 2026 | 通过相邻去噪步骤 Attention Context 相似性挑选 Salient Tokens，仅重算这些 Token 的 Attention/FFN，复用其余激活；LLaDA、Dream 的推理吞吐与准确率实测。 |
| 2026 | [Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM](https://openreview.net/forum?id=SdnkB5pGbq) | ICLR 2026 | Dynamic Cache Updating 按层和扩散步骤调整 KV 更新预算，Adaptive Parallel Decoding 基于 Token 分布动态调整提交门槛；在多模型和推理任务中报告时延/精度权衡并有公开代码。 |
| 2026 | [ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6fc63067ef32cfda806afbd8328ab27e-Abstract-Conference.html) | ICLR 2026 | 基于相邻去噪步的 Hidden-State 变化和 Token Confidence 决定早期 Layer Token Skipping；H200 实机推理实验兼顾吞吐与质量。 |
| 2026 | [Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding](https://nvlabs.github.io/Fast-dLLM/) | ICLR 2026 | 为双向 Diffusion LLM 设计 Block-wise Approximate KV Cache，并以置信度策略并行提交 Token；提供 LLaDA/Dream 质量与端到端生成性能对照及公开实现，注意非严格等价解码。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [FlashDLM: Accelerating Diffusion Language Model Inference via Efficient KV Caching and Guided Diffusion](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f930c6e1292a1160189a0734f22b465b-Abstract-Conference.html) | ICLR 2026 | 以 FreeCache 复用稳定 Denoising-step KV，Guided Diffusion 采用轻量 AR 模型减少去噪迭代；作者开源端到端实验，但需计入辅助模型运行开销。 |
| 2026 | [Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing](https://aclanthology.org/2026.acl-long.556/) | ACL 2026 | 利用去噪步 Confidence 的时间稳定性预测 Attention Region，按 Sink/Layer 复用稀疏位置，在长上下文 dLLM 减少双向 Attention 计算；论文声称高 Kernel/Inference 加速，必须核完整端到端和输出质量。（HOLD_EVIDENCE） |
| 2026 | [Learning to Parallel: Accelerating Diffusion Large Language Models via Learnable Parallel Decoding](https://proceedings.iclr.cc/paper_files/paper/2026/hash/86b1472b3eb0e1111cb9e496bdb3baf3-Abstract-Conference.html) | ICLR 2026 | Diffusion LM 的并行解码、缓存复用与去噪迭代压缩；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（HOLD_EVIDENCE） |
| 2026 | [Towards Efficient and Effective Diffusion Language Model Inference via Semantic-Aware Adaptive Denoising](https://aclanthology.org/2026.acl-long.819/) | ACL 2026 (Long Paper) | Ada-DLM 根据 token Confidence 轨迹检测语义收敛、减少无效 Denoising，并结合 System-level 执行优化；作者报告相对既有 DLM 加速方法的速度/生成质量收益。**近似推理，非输出等价**；具体模型、实机配置、Kernel vs E2E 与公平基线仍待方法审查。（HOLD_EVIDENCE） |
| 2026 | [WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference](https://proceedings.mlr.press/v306/liu26av.html) | ICML 2026 | 用 Topological Reordering 将已知 Token 移至物理 Prefix，同时保持逻辑位置和 Causal Mask，使 Diffusion 解码兼容标准 Prefix KV Cache；Streaming Commit 在与 vLLM 同部署条件下比较生成速度。 |

### Adjacent Modality & Cross-Topic Boundary (11)

**邻接模态与跨主题边界材料**：相邻模态（VLM/视频/图像扩散）的并行或投机解码、推理路径级投机，以及按决定性机制应归属其他主题的稀疏注意力算法；全部标注 KEEP_ADJACENT，属跨主题重分类候选，不构成本主题的文本解码投机机制。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [Breaking the Reward Barrier: Accelerating Tree-of-Thought Reasoning via Speculative Exploration](https://www.usenix.org/conference/osdi26/presentation/zhong) | OSDI 2026 | SPEX 以查询内推测性路径选择、查询间预算分配与自适应早停破除 Tree-of-Thought 的奖励同步壁垒，在 SGLang 上使各类 ToT 算法加速 1.2×–3×，与 token 级 speculative decoding 叠加最高累计加速 4.1×（KEEP_ADJACENT） |
| 2026 | [BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html) | ICLR 2026 | 训练无关地跨 Denoising Step 缓存并复用 DiT Block Feature，以相似性阈值触发重算，实测视频扩散推理延迟与视觉质量权衡（邻接领域；非 KV Cache）。（KEEP_ADJACENT） |
| 2026 | [DREAM-S: Speculative Decoding with Searchable Drafting and Target-Aware Refinement for Multimodal Generation](https://aclanthology.org/2026.acl-long.2177/) | ACL 2026 | 相邻 VLM Decoding：针对目标硬件以 NAS 搜索 Draft–Target 交互和 Draft 架构，结合 Attention Entropy 控制知识蒸馏；需要训练，不是 Drop-in Serving Scheduler。（KEEP_ADJACENT / REQUIRES_FINETUNING） |
| 2026 | [Long-Context Modeling with Dynamic Hierarchical Sparse Attention for Memory-Constrained LLM Inference](https://proceedings.mlr.press/v306/xiong26q.html) | ICML 2026 | DHSA 按 Chunk→Token 动态预测 Attention 稀疏性，包含 GPU/CPU Tiled Backend；提供 100K/128K 长上下文推理性能和任务精度，需计入掩码预测成本。（KEEP_ADJACENT） |
| 2026 | [Multi-Scale Local Speculative Decoding for Image Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Peruzzo_Multi-Scale_Local_Speculative_Decoding_for_Image_Generation_CVPR_2026_paper.html) | CVPR 2026 | 相邻视觉 AR 生成：低分辨率 Draft+上采样，在局部空间范围内 Reject/Resample 高分辨率目标 Token；有 CVPR 正式实验和开源项目，但质量指标与 Text LLM Speculative Decoding 不同。（KEEP_ADJACENT） |
| 2026 | [ParallelVLM: Lossless Video-LLM Acceleration with Visual Alignment Aware Parallel Speculative Decoding](https://openaccess.thecvf.com/content/CVPR2026/html/Kong_ParallelVLM_Lossless_Video-LLM_Acceleration_with_Visual_Alignment_Aware_Parallel_Speculative_CVPR_2026_paper.html) | CVPR 2026 | 视频 VLM 的并行候选生成与验证（相邻多模态推理）；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（KEEP_ADJACENT / HOLD_EVIDENCE） |
| 2026 | [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) | ICLR 2026 | 用多帧联合去噪与 Rolling Window 减少自回归视频生成的误差积累，以 Attention Sink 稳定跨窗口状态；单 GPU 实测多分钟实时视频生成（邻接领域）。（KEEP_ADJACENT） |
| 2026 | [SALE: Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling](https://proceedings.mlr.press/v306/ji26m.html) | ICML 2026 | 通过低 Bit QK 估计和 Relative Attention Score 产生细粒度稀疏 Mask，定制 CUDA Attention Kernel；GPU 长上下文 Prefill 实测，需计入 Mask 构造开销。（KEEP_ADJACENT） |
| 2026 | [Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference](https://proceedings.mlr.press/v306/le26c.html) | ICML 2026 | Hadamard Sketch 估计 Attention Score，跨 Layer Walk 汇总重要性，并使用可复用的动态稀疏 Kernel 同时处理 Prefill/Decode；Kernel 级收益不能等同完整 Serving Goodput。（KEEP_ADJACENT） |
| 2026 | [Stochastic Sparse Attention for Memory-Bound Inference](https://proceedings.mlr.press/v306/lee26j.html) | ICML 2026 | SANTA 采用方差受控的 Softmax 分布采样减少 Value-cache 全量读取，实现 GPU Stratified/Systematic Sampling Attention；有 RTX 6000 Ada Kernel 和端到端 Decode 测量。（KEEP_ADJACENT） |
| 2026 | [Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection](https://proceedings.mlr.press/v306/jo26a.html) | ICML 2026 | 跨 Head/Layer 动态选择 Token 执行 Attention，后续 Layer 可重新考虑此前 Token；与既有 FlashAttention 兼容，作者报告 128K Attention Kernel 和质量对照。（KEEP_ADJACENT） |

### Long-Context & MoE-Specific Speculation (4)

**长上下文与 MoE 场景的定制投机**：稀疏 KV Draft 模型、常数大小 Draft KV 与位置索引修正、Draft Lookahead 识别必要 KV，以及专家加载成本感知的投机启停。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/13f972adf12bdf886583d48cd528002f-Abstract-Conference.html) | ICLR 2025 | 采用 Sparse-KV Draft Model 在高并发 Long-context Serving 中进行 Draft-Verify，并以性能模型选取 Draft 策略。 |
| 2025 | [Utility-Driven Speculative Decoding for Mixture-of-Experts](https://arxiv.org/abs/2506.20675) | arXiv 2025 (preprint; Cascade system) | 在 vLLM 五类 MoE 实测发现投机验证可放大 Expert 权重加载；以短测试窗口估计 Token Gain/Verification Cost，按迭代启停并自适应调整 Draft 长度，避免静态 Speculation 引起的吞吐回退。 |
| 2026 | [Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding](https://proceedings.mlr.press/v306/lee26d.html) | ICML 2026 | 利用 Draft Lookahead 和目标历史 Attention 在长上下文 Speculation 中识别必要 KV，限制重要性评分 Head 数以降低 Verify 的 KV 加载；在 Qwen2.5-72B、32K 上报告端到端实测。 |
| 2026 | [LongSpec: Long-Context Lossless Speculative Decoding with Efficient Drafting and Verification](https://aclanthology.org/2026.acl-long.83/) | ACL 2026 | 使用常数大小 Draft KV、位置索引修正训练与长上下文执行差异，并重构前缀/Tree Attention 计算；论文报告长上下文真实 Wall-clock 收益，需核 Target/Draft 与 Prefix 实测公平性。（HOLD_EVIDENCE） |

---
*Publication source and mechanism screened; speedup claims are not independently reproduced. Acceptance-length- or kernel-level gains are not service-level TTFT/TPOT/Goodput, and explicit HOLD tags remain unresolved strict-review items.*
