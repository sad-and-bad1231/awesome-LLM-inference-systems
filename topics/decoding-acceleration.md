# Decoding Acceleration

Breaking sequential decode bottlenecks through draft/verify, parallel prediction and token-tree verification.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Choose here when the main novelty is the token acceptance/verification mechanism; SLO admission or fleet scheduling belongs in Runtime.

**Foundational context.** See also: [Blockwise Parallel Decoding (2018), Speculative Decoding (2023), Medusa (2024), SpecInfer (2024)](../README.md#foundational-and-influential-papers).

## Papers (35)

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2023 | [Speculative Decoding: Exploiting Speculative Execution for Accelerating Seq2seq Generation](https://aclanthology.org/2023.findings-emnlp.257/) | Findings EMNLP 2023 | 提出早期 Seq2seq Speculative Execution 与验证方案，是后续损失无关 Draft/Verify 体系的前驱。 |
| 2024 | [Break the Sequential Dependency of LLM Inference Using Lookahead Decoding](https://proceedings.mlr.press/v235/fu24a.html) | ICML 2024 | 以 Jacobi 风格的并行序列修正与 N-gram 验证加速自回归推理，减少独立 Draft Model 依赖。 |
| 2024 | [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8766fbc68e1ed1cdef712ce273e0a363-Abstract-Conference.html) | ICLR 2024 | 以蒸馏优化 Draft Model 与 Target 的接受概率，减少验证开销。 |
| 2024 | [EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees](https://aclanthology.org/2024.emnlp-main.422/) | EMNLP 2024 | 依据上下文相关的接受率动态构造 Draft Tree，区别于静态树推测路径。 |
| 2024 | [EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://proceedings.mlr.press/v235/li24bt.html) | ICML 2024 | 在倒数第二层特征空间预测草稿，修正 Feature Uncertainty；评测生成速度与分布保持。 |
| 2025 | [Accelerating LLM Inference with Lossless Speculative Decoding Algorithms for Heterogeneous Vocabularies](https://proceedings.mlr.press/v267/timor25a.html) | ICML 2025 | 消除 Draft 与 Target 必须共享 Tokenizer/Vocabulary 的约束，保留目标采样分布。 |
| 2025 | [AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving](https://github.com/cerebellumking/AdaSpec) | SoCC 2025 | 在线感知请求负载与设备环境，动态改变 Draft/Verify 策略，在多 SLO 工作负载下控制投机成本。 |
| 2025 | [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c7b5a35ea98b62512a869c19ea7b03cb-Abstract-Conference.html) | NeurIPS 2025 | 跨层 Feature Fusion 与 Training-time Test 优化 Speculative Drafter，增加高概率接受 Token。 |
| 2025 | [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/13f972adf12bdf886583d48cd528002f-Abstract-Conference.html) | ICLR 2025 | 采用 Sparse-KV Draft Model 在高并发 Long-context Serving 中进行 Draft-Verify，并以性能模型选取 Draft 策略。 |
| 2025 | [Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference](https://arxiv.org/abs/2510.13161) | arXiv 2025 (preprint) | 在 GPU/NPU 异构并行执行 Draft 早退路径与 Target 后缀，并用多 Token Speculative Streaming 打破串行 Draft 路径；作者用 14B–66B 模型端到端实测。 |
| 2025 | [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://proceedings.mlr.press/v267/chen25s.html) | ICML 2025 | 构建基于检索短上下文的 Draft LLM 来推测长上下文 Target 的生成结果。 |
| 2025 | [SpecMemo: Speculative Decoding is in Your Pocket](https://arxiv.org/abs/2506.01986) | arXiv 2025 (preprint) | 以细粒度 Token/Mem Allocation 抑制投机失败造成的冗余 KV 显存占用，并扩展分布式 Batched Draft-Verify；作者在 Titan RTX 与八卡 AMD MI250 实测。 |
| 2025 | [Utility-Driven Speculative Decoding for Mixture-of-Experts](https://arxiv.org/abs/2506.20675) | arXiv 2025 (preprint; Cascade system) | 在 vLLM 五类 MoE 实测发现投机验证可放大 Expert 权重加载；以短测试窗口估计 Token Gain/Verification Cost，按迭代启停并自适应调整 Draft 长度，避免静态 Speculation 引起的吞吐回退。 |
| 2026 | [Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding](https://proceedings.mlsys.org/paper_files/paper/2026/hash/66a026c0d17040889b50f0dfa650e5e0-Abstract-Conference.html) | MLSys 2026 | SpecGen 利用 PillarAttn 稀疏 Draft、延迟验证和运行时 KV 管理。 |
| 2026 | [AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding](https://dl.acm.org/doi/10.1145/3767295.3769315) | EuroSys 2026 | 按请求 SLO 设计 Speculative Draft/Verify 策略，将加速与服务目标联动。 |
| 2026 | [Breaking the Reward Barrier: Accelerating Tree-of-Thought Reasoning via Speculative Exploration](https://www.usenix.org/conference/osdi26/presentation/zhong) | OSDI 2026 | SPEX 以查询内推测性路径选择、查询间预算分配与自适应早停破除 Tree-of-Thought 的奖励同步壁垒，在 SGLang 上使各类 ToT 算法加速 1.2×–3×，与 token 级 speculative decoding 叠加最高累计加速 4.1× |
| 2026 | [BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html) | ICLR 2026 | 训练无关地跨 Denoising Step 缓存并复用 DiT Block Feature，以相似性阈值触发重算，实测视频扩散推理延迟与视觉质量权衡（邻接领域；非 KV Cache）。 |
| 2026 | [Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding](https://doi.org/10.1109/ISCA66397.2026.00022) | ISCA 2026 | 使用剪枝和尾数截断实现无需训练的轻量 Self-speculative Drafter，并在消费级 GPU 验证。 |
| 2026 | [CDLM: Consistency Diffusion Language Models for Faster Sampling](https://proceedings.mlsys.org/paper_files/paper/2026/hash/054de805fcceb78a201f5e9d53c85908-Abstract-Conference.html) | MLSys 2026 | 通过一致性建模降低 Diffusion LM 的 Refinement Steps，并通过 Block Causal Mask 与微调实现可复用 KV；训练-推理协同加速，开源实验代码，非无需重训练的纯 Runtime 系统。 |
| 2026 | [D-cut: Adaptive Verification Depth Pruning for Batched Speculative Decoding](https://arxiv.org/abs/2607.14647) | arXiv 2026 (preprint) | 跨请求按 Draft Confidence 分配 Verification Budget，以设备和 Parallelism Cost Model 自适应裁剪 Depth；Dense 和 MoE 高并发实测 Speculation 验证开销与吞吐。 |
| 2026 | [DSB: Dynamic Sliding Block Scheduling for Diffusion LLMs](https://proceedings.mlr.press/v306/luo26o.html) | ICML 2026 | 自适应滑动 Block 和配套 KV Cache 提升扩散语言模型的并行生成效率。 |
| 2026 | [Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding](https://proceedings.mlr.press/v306/lee26d.html) | ICML 2026 | 利用 Draft Lookahead 和目标历史 Attention 在长上下文 Speculation 中识别必要 KV，限制重要性评分 Head 数以降低 Verify 的 KV 加载；在 Qwen2.5-72B、32K 上报告端到端实测。 |
| 2026 | [DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection and Partial Attention](https://proceedings.mlr.press/v306/lee26i.html) | ICML 2026 | 通过相邻去噪步骤 Attention Context 相似性挑选 Salient Tokens，仅重算这些 Token 的 Attention/FFN，复用其余激活；LLaDA、Dream 的推理吞吐与准确率实测。 |
| 2026 | [Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM](https://openreview.net/forum?id=SdnkB5pGbq) | ICLR 2026 | Dynamic Cache Updating 按层和扩散步骤调整 KV 更新预算，Adaptive Parallel Decoding 基于 Token 分布动态调整提交门槛；在多模型和推理任务中报告时延/精度权衡并有公开代码。 |
| 2026 | [ECHO: Elastic Speculative Decoding with Sparse Gating for High-Concurrency Scenarios](https://proceedings.mlr.press/v306/hu26ar.html) | ICML 2026 | 在 SGLang 统一 Batch Super-tree 上使用 Sparse Confidence Gating 动态分配 Draft 深度/宽度及 Verify 计算预算；覆盖 Qwen3-235B 与高并发吞吐对照。 |
| 2026 | [Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding](https://nvlabs.github.io/Fast-dLLM/) | ICLR 2026 | 为双向 Diffusion LLM 设计 Block-wise Approximate KV Cache，并以置信度策略并行提交 Token；提供 LLaDA/Dream 质量与端到端生成性能对照及公开实现，注意非严格等价解码。 |
| 2026 | [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/abs/2606.18394) | arXiv 2026 (formerly JetFlow) | 训练基于 Frozen Target Fused Hidden States 的 Causal Parallel Draft Head，单次 Forward 并行生成树并整体 Verify；H100/B200 GPU 与 vLLM 集成实测 Speculative Acceptance、延迟和端到端解码。 |
| 2026 | [NanoSpec: Accelerating Speculative Decoding using Minimalist In-Context Vocabularies](https://proceedings.mlr.press/v306/chen26fm.html) | ICML 2026 | 动态收缩 Draft 词表，并以异步 Gather/GPU 驻留状态克服稀疏访存瓶颈，报告端到端推测解码收益。 |
| 2026 | [PRISM: Parametrically Refactor Inference for Speculative Decoding Draft Models](https://openreview.net/forum?id=cvU2HuuxEf) | MLSys 2026 | PRISM（MLSys 2026）对 speculative decoding 中的 draft 模型推理做参数化重构，在保持验证阶段正确性的前提下降低草稿生成的算力与延迟开销，从而提升草稿生成效率与验证吞吐量 |
| 2026 | [Rolling Forcing: Autoregressive Long Video Diffusion in Real Time](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) | ICLR 2026 | 用多帧联合去噪与 Rolling Window 减少自回归视频生成的误差积累，以 Attention Sink 稳定跨窗口状态；单 GPU 实测多分钟实时视频生成（邻接领域）。 |
| 2026 | [SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding](https://proceedings.mlsys.org/paper_files/paper/2026/hash/041dad5ed2191b44ba3ed0e00cdc3187-Abstract-Conference.html) | MLSys 2026 | 使用离散扩散并行 Drafter 与自回归验证器对齐，提高接受率。 |
| 2026 | [TiDAR: Think in Diffusion, Talk in Autoregression](https://proceedings.mlsys.org/paper_files/paper/2026/hash/1367d856028f65a9555b0274db09e608-Abstract-Conference.html) | MLSys 2026 | 在一次 Forward Pass 中执行 Diffusion Draft 与自回归采样，用结构化 Attention Mask 实现推测式并行生成。 |
| 2026 | [Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match](https://proceedings.iclr.cc/paper_files/paper/2026/hash/acb94e709f02895fd98b5867f0b184f3-Abstract-Conference.html) | ICLR 2026 | FLy 将精确匹配放宽为熵门控和延迟验证窗口，利用目标模型自纠正行为接纳语义等价 Draft；在 70B/405B 模型上测得端到端加速，但不保证与严格 Speculative Decoding 的输出分布恒等。 |
| 2026 | [Vegas: Self-Speculative Decoding with Verification-Guided Sparse Attention](https://proceedings.mlr.press/v306/yue26a.html) | ICML 2026 | Verify 阶段复用 KV 重要性信息，为后续 Self-speculative Draft 加速。 |
| 2026 | [WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference](https://proceedings.mlr.press/v306/liu26av.html) | ICML 2026 | 用 Topological Reordering 将已知 Token 移至物理 Prefix，同时保持逻辑位置和 Causal Mask，使 Diffusion 解码兼容标准 Prefix KV Cache；Streaming Commit 在与 vLLM 同部署条件下比较生成速度。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
