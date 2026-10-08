# Decoding Acceleration

Breaking sequential decode bottlenecks through draft/verify, parallel prediction and token-tree verification.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Choose here when the main novelty is the token acceptance/verification mechanism; SLO admission or fleet scheduling belongs in Runtime.

**Foundational context.** See also: [Blockwise Parallel Decoding (2018), Speculative Decoding (2023), Medusa (2024), SpecInfer (2024)](../README.md#foundational-and-influential-papers).
## Papers (10)

A selective, chronological bibliography; each paper's principal mechanism determines its only full-topic entry. See [curation criteria](../CURATION.md) and the [migration record](serving-systems.md) for historical changes.

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2023 | [Speculative Decoding: Exploiting Speculative Execution for Accelerating Seq2seq Generation](https://aclanthology.org/2023.findings-emnlp.257/) | Findings EMNLP 2023 | 提出早期 Seq2seq Speculative Execution 与验证方案，是后续损失无关 Draft/Verify 体系的前驱。 |
| 2024 | [Break the Sequential Dependency of LLM Inference Using Lookahead Decoding](https://proceedings.mlr.press/v235/fu24a.html) | ICML 2024 | 以 Jacobi 风格的并行序列修正与 N-gram 验证加速自回归推理，减少独立 Draft Model 依赖。 |
| 2024 | [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8766fbc68e1ed1cdef712ce273e0a363-Abstract-Conference.html) | ICLR 2024 | 以蒸馏优化 Draft Model 与 Target 的接受概率，减少验证开销。 |
| 2024 | [EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees](https://aclanthology.org/2024.emnlp-main.422/) | EMNLP 2024 | 依据上下文相关的接受率动态构造 Draft Tree，区别于静态树推测路径。 |
| 2024 | [EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://proceedings.mlr.press/v235/li24bt.html) | ICML 2024 | 在倒数第二层特征空间预测草稿，修正 Feature Uncertainty；评测生成速度与分布保持。 |
| 2025 | [Accelerating LLM Inference with Lossless Speculative Decoding Algorithms for Heterogeneous Vocabularies](https://proceedings.mlr.press/v267/timor25a.html) | ICML 2025 | 消除 Draft 与 Target 必须共享 Tokenizer/Vocabulary 的约束，保留目标采样分布。 |
| 2025 | [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c7b5a35ea98b62512a869c19ea7b03cb-Abstract-Conference.html) | NeurIPS 2025 | 跨层 Feature Fusion 与 Training-time Test 优化 Speculative Drafter，增加高概率接受 Token。 |
| 2025 | [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://proceedings.mlr.press/v267/chen25s.html) | ICML 2025 | 构建基于检索短上下文的 Draft LLM 来推测长上下文 Target 的生成结果。 |
| 2026 | [AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding](https://dl.acm.org/doi/10.1145/3767295.3769315) | EuroSys 2026 | 按请求 SLO 设计 Speculative Draft/Verify 策略，将加速与服务目标联动。 |
| 2026 | [NanoSpec: Accelerating Speculative Decoding using Minimalist In-Context Vocabularies](https://proceedings.mlr.press/v306/chen26fm.html) | ICML 2026 | 动态收缩 Draft 词表，并以异步 Gather/GPU 驻留状态克服稀疏访存瓶颈，报告端到端推测解码收益。 |

*Venue and mechanisms follow primary publication material; authors' experimental claims are not independently reproduced.*
