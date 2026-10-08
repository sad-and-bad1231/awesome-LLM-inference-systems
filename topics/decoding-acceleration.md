# Decoding Acceleration

Breaking sequential decode bottlenecks through draft/verify, parallel prediction and token-tree verification.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Choose here when the main novelty is the token acceptance/verification mechanism; SLO admission or fleet scheduling belongs in Runtime.

**Foundational context.** See also: [Blockwise Parallel Decoding (2018), Speculative Decoding (2023), Medusa (2024), SpecInfer (2024)](../README.md#foundational-and-influential-papers).

## Newly admitted · October 2026 (3)

These entries have individually checked primary publication records. Descriptions summarize *the authors' mechanisms and evidence*; they do not imply independent reproduction, nor final adjudication of all earlier repository entries.

| Year | Paper | Venue | Distinct system mechanism |
|---|---|---|---|
| 2024 | [EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty](https://proceedings.mlr.press/v235/li24bt.html) | ICML 2024 | 在倒数第二层特征空间预测草稿，修正 Feature Uncertainty；评测生成速度与分布保持。 |
| 2024 | [EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees](https://aclanthology.org/2024.emnlp-main.422/) | EMNLP 2024 | 依据上下文相关的接受率动态构造 Draft Tree，区别于静态树推测路径。 |
| 2026 | [NanoSpec: Accelerating Speculative Decoding using Minimalist In-Context Vocabularies](https://proceedings.mlr.press/v306/chen26fm.html) | ICML 2026 | 动态收缩 Draft 词表，并以异步 Gather/GPU 驻留状态克服稀疏访存瓶颈，报告端到端推测解码收益。 |

**Legacy cohort.** Previously collected Serving papers remain on [Serving Systems](serving-systems.md) pending individual re-admission/reclassification. A paper is not automatically admitted into this category based on a prior status flag.
