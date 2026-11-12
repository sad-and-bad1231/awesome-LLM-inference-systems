# Tencent

Tencent's public model families, product/model co-design and first-party inference tooling. Model architecture, product evidence, speculative-decoding training and serving engines are separated rather than treated as one runtime.

[← Organizations](README.md) · [← Home](../README.md)

## Official model-family coverage (updated 2026-11-12)

**First-party model list:** [Tencent HY model center](https://llm.hunyuan.tencent.com/), [Tencent Hunyuan portal](https://hunyuan.tencent.com/) and [cloud migration notices](https://cloud.tencent.com/document/product/1729/131925). Tencent moved newer API access to TokenHub; **legacy API IDs have been retired**.

| Official family | Execution / model context | Primary source |
|---|---|---|
| **Hy4 (official release, 2026-11-04)** | Final product/API release adds native visual understanding, CLI/GUI computer use and stronger long-horizon agentic tasks. The launch notice says weights and system card would follow; it does **not** establish that the final model shares Preview's exact parameter count or architecture. Do not transfer Preview specifications to Hy4 final. | [Tencent official release](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/) · [TokenHub model docs](https://cloud.tencent.com/document/product/1823/132252) |
| **Hy4-preview (2026-08-28)** | 770B total / 49B active MoE, 1M context; Gated DeepSeek Sparse Attention with cross-layer IndexCache, iHC residual pathway and a native MTP layer. These specifications belong to the **Preview artifact only**; the repo itself describes the architecture as inspired by DeepSeek and GLM. | [Official Preview repository](https://github.com/Tencent-Hunyuan/Hy4-preview) |
| Hy3 / Hy3-preview | Predecessor model family: 295B/21B MoE, 256K context and a native 3.8B MTP layer; official deployment guidance covers vLLM and SGLang. | [Hy3](https://github.com/Tencent-Hunyuan/Hy3) · [official model center](https://llm.hunyuan.tencent.com/) |
| Hy-MT2-30B-A3B / Hy-MT2-7B / Hy-MT2-1.8B | Multilingual translation; one MoE variant and smaller dense deployments | [Tencent HY model center](https://llm.hunyuan.tencent.com/) |
| HY-1.8B-2Bit | Quantized edge/local deployment exemplar; not a general Hy3 checkpoint | [Tencent HY model center](https://llm.hunyuan.tencent.com/) |
| Hunyuan-A13B / Hunyuan-Large / HY 2.0 | Earlier MoE and model-family heritage, separate from current live access | [A13B code](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) · [cloud product doc](https://cloud.tencent.com/document/product/1729/104753) |
| HY Vision 2.0 / HY-ASR 3.0 Preview | Vision-language understanding and speech recognition, distinct prefill/modal pipelines | [Official Hunyuan portal](https://hunyuan.tencent.com/) |
| HY Image3.5 Preview / HY-Video 1.5 / HY-3D 3.1 | Image/video/3D generation; adjacent to rather than identical to text autoregressive serving | [Official model portal](https://hunyuan.tencent.com/) · [TokenHub migration](https://cloud.tencent.com/announce/detail/2405) |
| Legacy Hunyuan T1/Turbo/TurboS/standard/role/translation | Historical API families **retired/replaced in 2026**; do not present their IDs as current | [Formal deprecation matrix](https://cloud.tencent.com/document/product/1729/131925) |

**Official naming rule:** HY model *portfolio* is not the same as legacy Tencent Cloud API model IDs; cite both and record retirement/TokenHub migration when recommending implementations.

## Selected first-party model, runtime and inference-tooling sources

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Hunyuan-A13B** | Efficient MoE model architecture with a low active-parameter footprint; inference-related architecture, not a serving scheduler. | [Official source](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) |
| **Hy3** (2026) | 295B MoE / 21B activated, GQA, expert routing and native MTP head. Public vLLM/SGLang deployment guidance informs real serving compatibility; quality ranking is not a systems measurement. | [Official repository](https://github.com/Tencent-Hunyuan/Hy3) |
| **Hy4 (final; Nov 4, 2026)** | Product/API model revision adds vision understanding and computer-use workflows; model remains a 770B-class MoE in Tencent's release description. **Formal weights/system card pending** in checked official documentation; internal capability comparisons are not inference speedups or architectural evidence. | [First-party release](https://adp.tencent.com/zh/blog/tencent-cloud-adp-hunyuan-hy4-release) · [Tencent TokenHub model documentation](https://cloud.tencent.com/document/product/1823/132252) |
| **Hy4-preview** (2026) | 770B MoE / 49B activated; **Gated DeepSeek Sparse Attention** with cross-layer **IndexCache** reuse, iHC residual branches and an MTP head. Interesting for indexer reuse, sparsity, KV layout and expert placement; **preview model**, not independent engine/kernel evidence. | [Official repository](https://github.com/Tencent-Hunyuan/Hy4-preview) |
| **Hunyuan-Large** | Technical report and code for Tencent's large MoE model; inspect model architecture and sparse expert execution. | [Official source](https://github.com/Tencent/Hunyuan-Large) |
| **AngelSlim** | Model compression toolkit spanning PTQ/QAT, quantization-aware distillation and deployment tooling; it integrates AngelSpec as a submodule. It is not a serving engine. | [Official repository](https://github.com/Tencent/AngelSlim) | 
| **AngelSpec** (2026) | Torch-native **speculative-drafter training** framework for MTP and block-parallel methods (DFly, DFlash, DFlare, Eagle3, DSpark, etc.). Training and target-model inference are disaggregated; Mooncake transfers hidden states over RDMA. This is drafter training infrastructure, not an inference runtime. | [Repository](https://github.com/Tencent/AngelSpec) · [Technical report](https://arxiv.org/abs/2607.25852) | 
| **KsanaLLM** | Tencent's open-source LLM serving engine: prefix caching, multiple decoding modes and an optional Mooncake-backed global KV-cache connector. Its current public README documents Ascend **910B2C / CANN 8.0RC2**; treat this as that repository's documented legacy NPU path, not proof of Hy4 production deployment or CANN 9.x compatibility. | [Official repository](https://github.com/Tencent/KsanaLLM) | 
| **Angel** | Tencent's distributed ML systems toolkit; useful background but broader than LLM inference. | [Official source](https://github.com/Tencent/Angel) |

## Product and organization context

Tencent publicly frames its AI strategy around a **Foundation–Product–Frontier** triangle. Shunyu Yao is identified by Tencent as its **Chief Scientist for AI** and has articulated this framework; that title alone should not be read as evidence that he personally owns every Hunyuan engineering subsystem. The Hunyuan team describes deep model/product co-design with **WorkBuddy** and **CodeBuddy**; WorkBuddy connects model capability to enterprise workflows, including WeCom chats, email, documents, calendars and meetings.

Tencent Cloud reported that WorkBuddy had handled **9 billion+ task requests**, reached **50+ industries** and **50% of China's Top 500 enterprises**, with an ecosystem of **50,000+ developers/partners and 200,000+ skills**. These are company-reported cumulative adoption figures, not DAU or independently audited active-user metrics. **TokenHub** provides a unified API surface for Hunyuan and third-party models; it is a model-access/service layer, not the underlying inference engine. Sources: [Tencent AI strategy dialogue](https://www.tencent.com/tencent-cloud-debuts-productivity-agent-suite-creating-a-new-gateway-to-ai-for-users-and-enterprises/) · [Tencent Cloud ecosystem update](https://www.tencent.com/zh-cn/tencent-cloud-accelerates-international-growth-advances-enterprise-ai-and-expands-global-partnerships/) · [TokenHub](https://cloud.tencent.com/product/tokenhub).

## Recursive self-improvement — separate the two public claims

The **Hy4-preview (Aug 28)** release describes an early-stage loop in which the model proposed changes to training methods/data/evaluation and low-level operators, ran experiments and iterated from code/log/feedback. Tencent separately reports that it identified inference bottlenecks and optimized **operator fusion and communication**, claiming **31.8% end-to-end throughput improvement** over its baseline across different context lengths and concurrency levels. This is a **vendor-reported result**: the release does not provide a public reproducible code/trace bundle or enough matched configuration detail to independently verify the 31.8% figure here. Treat it as a serious RSI signal, not a reproduced benchmark. [Official Hy4-preview release](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/).

The **Hy4 final (Nov 4)** announcement describes a separate Hyra 2.0 effort that optimized **pre-training infrastructure** for smaller models sharing the same architecture, and open-sourced the HyCell and HyPDE foundation models. This is evidence of model-research/training-infrastructure self-optimization; it should not be conflated with the Preview's inference operator/communication optimization claim. [Official Hy4 release](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/).

**Scope:** model architectures, product/model co-design and first-party inference tooling. The reused DSA/IndexCache principles are attributed as such, not claimed as newly invented by Tencent. Product adoption, model quality, reported throughput and serving-engine capability are distinct evidence types; do not infer full-serving acceleration or Ascend support from a model release alone.
