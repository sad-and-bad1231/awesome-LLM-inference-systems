# Tencent

Tencent's public LLM model releases and inference-oriented systems work. The index separates Tencent-owned projects from broader multi-company collaborations.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Hunyuan-A13B** | Efficient MoE model architecture with a low active-parameter footprint; inference-related architecture, not a serving scheduler. | [Official source](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) |
| **Hy3** (2026) | 295B MoE / 21B activated, GQA, expert routing and native MTP head. Public vLLM/SGLang deployment guidance informs real serving compatibility; quality ranking is not a systems measurement. | [Official repository](https://github.com/Tencent-Hunyuan/Hy3) |
| **Hy4-preview** (2026) | 770B MoE / 49B activated; **Gated DeepSeek Sparse Attention** with cross-layer **IndexCache** reuse, iHC residual branches and an MTP head. Interesting for indexer reuse, sparsity, KV layout and expert placement; **preview model**, not independent engine/kernel evidence. | [Official repository](https://github.com/Tencent-Hunyuan/Hy4-preview) |
| **Hunyuan-Large** | Technical report and code for Tencent's large MoE model; inspect model architecture and sparse expert execution. | [Official source](https://github.com/Tencent/Hunyuan-Large) |
| **Angel** | Tencent's distributed ML systems toolkit; useful background but predominantly broader than LLM inference. | [Official source](https://github.com/Tencent/Angel) |

**Scope:** Model architectures and first-party components only. The reused DSA/IndexCache principles are attributed as such, not claimed as newly invented by Tencent; do not infer full-serving acceleration or Ascend support from model release claims.

## Official model-family coverage (2026-10-24)

**First-party model list:** [Tencent HY model center](https://llm.hunyuan.tencent.com/), [Tencent Hunyuan portal](https://hunyuan.tencent.com/) and [cloud migration notices](https://cloud.tencent.com/document/product/1729/131925). Tencent moved newer API access to TokenHub; **legacy API IDs have been retired**.

| Official family | Execution / model context | Primary source |
|---|---|---|
| Hy4-preview | 770B-class MoE, Gated DSA + IndexCache and MTP, not an independently optimized inference runtime | [Model / source](https://github.com/Tencent-Hunyuan/Hy4-preview) |
| Hy3 / Hy3-preview | 295B/21B MoE, GQA, MTP and thinking modes; current flagship on the Tencent HY site | [Hy3](https://github.com/Tencent-Hunyuan/Hy3) · [official model center](https://llm.hunyuan.tencent.com/) |
| Hy-MT2-30B-A3B / Hy-MT2-7B / Hy-MT2-1.8B | Multilingual translation; one MoE variant and smaller dense deployments | [Tencent HY model center](https://llm.hunyuan.tencent.com/) |
| HY-1.8B-2Bit | Quantized edge/local deployment exemplar; not a general Hy3 checkpoint | [Tencent HY model center](https://llm.hunyuan.tencent.com/) |
| Hunyuan-A13B / Hunyuan-Large / HY 2.0 | Earlier MoE and model-family heritage, separate from current live access | [A13B code](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) · [cloud product doc](https://cloud.tencent.com/document/product/1729/104753) |
| HY Vision 2.0 / HY-ASR 3.0 Preview | Vision-language understanding and speech recognition, distinct prefill/modal pipelines | [Official Hunyuan portal](https://hunyuan.tencent.com/) |
| HY Image3.5 Preview / HY-Video 1.5 / HY-3D 3.1 | Image/video/3D generation; adjacent to rather than identical to text autoregressive serving | [Official model portal](https://hunyuan.tencent.com/) · [TokenHub migration](https://cloud.tencent.com/announce/detail/2405) |
| Legacy Hunyuan T1/Turbo/TurboS/standard/role/translation | Historical API families **retired/replaced in 2026**; do not present their IDs as current | [Formal deprecation matrix](https://cloud.tencent.com/document/product/1729/131925) |

**Official naming rule:** HY model *portfolio* is not the same as legacy Tencent Cloud API model IDs; cite both and record retirement/TokenHub migration when recommending implementations.
