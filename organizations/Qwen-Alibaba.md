# Qwen (Alibaba)

The Qwen team's publicly released model families and inference-related model architecture. Runtime implementations from vLLM/SGLang/LMDeploy remain credited to their respective maintainers.

[← Organizations](README.md) · [← Home](../README.md)

## Official model-family coverage (2026-10-24)

**Authoritative catalog:** [Alibaba Cloud Model Studio models](https://help.aliyun.com/zh/model-studio/web-search) enumerates service families and versions; [Qwen repositories](https://github.com/QwenLM) are first-party code/weights. **Family vs API model ID vs open checkpoint** must be distinguished.

| Official family | Model inventory / inference contract | Primary source |
|---|---|---|
| Qwen3.8 | Max, Flash, 2.4T-A95B, 27B; 3.8-Flash-Next is a separate model/research implementation featuring GDN+QSA | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) · [Flash-Next source](https://github.com/QwenLM/Qwen3.8-Flash-Next) |
| Qwen3.7 | Max, Plus, Flash and dated API snapshots | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3.6 | Plus, Flash, 27B, 35B-A3B and dated API snapshots | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3.5 | Plus, Flash, 27B, 35B-A3B, 122B-A10B, 397B-A17B; Gated DeltaNet + full-attention execution | [Model Studio listing](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3 / Qwen3-Max / Qwen3-Next | Foundational dense/MoE and historical hybrid-linear transition; Qwen3-Max is a hosted family rather than every published small checkpoint | [Qwen3 source](https://github.com/QwenLM/Qwen3) · [Model Studio](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3-Coder / Qwen3-VL / Qwen3-Omni | Code-heavy long outputs; multimodal image/video/voice inputs with distinct prefill/streaming pipelines | [Coder](https://github.com/QwenLM/Qwen3-Coder) · [Omni](https://github.com/QwenLM/Qwen3-Omni) |
| Qwen3.5-Omni / Qwen3.8-Omni | Plus/Flash, Realtime variants; low-latency streaming audio/visual model family | [Model Studio Omni list](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen3.8-Omni-Flash / Realtime | Latest listed Omni Flash and real-time version; not identical to ordinary text Flash | [Model Studio Omni list](https://help.aliyun.com/zh/model-studio/web-search) |
| Qwen2.5 / Qwen2.5-VL and earlier | Historical dense/VL checkpoint families; retained as stable vLLM comparison workloads | [Model Studio import list](https://help.aliyun.com/zh/model-studio/model-import) |
| Qwen Image / Wan | Adjacent image/video generation workloads, **not** part of text LLM serving | [Alibaba/Qwen project navigation](https://github.com/QwenLM) |

**Policy:** Model Studio lists *many* dated snapshots and sizes. The primary catalog is the exhaustive API-ID registry; this curated page covers **all named major service families** without asserting every `-YYYY-MM-DD` snapshot is a new inference architecture.

**Qwen4 release watch (Nov 9):** A verified first-party Qwen4 general-availability/weight-card release has **not been established**. The publicly inspectable [Qwen3.8-Flash-Next experimental architecture](https://github.com/QwenLM/Qwen3.8-Flash-Next) provides a **Gated DeltaNet + QSA indexer/offload** inference signal, but does not license a claim of published Qwen4 final weights, model IDs or compatibility. Recheck source identities on a real Qwen4 announcement.

## Selected first-party architecture and execution sources

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Qwen3** | Dense/MoE model family with thinking and non-thinking execution modes; inspect active experts, KV and decoding requirements. | [Official source](https://github.com/QwenLM/Qwen3) |
| **Qwen3-Next / Qwen3.5–3.8** (2025–26) | Qwen's hybrid **Gated DeltaNet recurrent state + gated full attention** family; Qwen3.5 uses an approximately 3:1 linear/full-attention stack. Recurrent-state and KV attention require distinct memory layouts/kernels; Qwen3.8 largely evolves the family rather than introducing another basic inference attention primitive. | [Official family repository](https://github.com/QwenLM/Qwen3.8) · [Qwen3.5 architecture reference](https://huggingface.co/docs/transformers/en/model_doc/qwen3_5) |
| **Qwen3.8-Flash-Next** (2026) | Early architectural preview combining **Gated DeltaNet + Qwen Sparse Attention (QSA)**, gated residual streams and N-gram embeddings with asynchronous host prefetch. Substantive inference contracts: sparse indexer, recurrent state, cache/offload and execution overlap. Claims remain author-reported. | [Official repository](https://github.com/QwenLM/Qwen3.8-Flash-Next) |
| **Qwen3-Coder** | Code-oriented model family; long-context and agentic generation create distinct serving workloads. | [Official source](https://github.com/QwenLM/Qwen3-Coder) |
| **Qwen3-Omni** | Multimodal model family with streaming audio/video/text execution considerations. | [Official source](https://github.com/QwenLM/Qwen3-Omni) |
| **MNN (Alibaba)** | Alibaba-maintained efficient inference engine, including on-device model execution. | [Official source](https://github.com/alibaba/MNN) |

## Alibaba infrastructure beyond Qwen models

| First-party execution source | Implemented mechanism | Attribution boundary |
|---|---|---|
| [RTP-LLM](https://github.com/alibaba/rtp-llm) | Alibaba's production-derived LLM engine with C++ scheduler/dynamic batching, KV-cache management/quantization, multi-LoRA, distributed TP and P/D separation. The maintainers describe use across Taobao, Tmall, Xianyu, Cainiao, Amap, Ele.me, AliExpress and Lazada. | **Alibaba inference team**, not the exclusive work of Qwen model designers. Runtime code acknowledges FasterTransformer, TensorRT-LLM and vLLM influences. Any internal-production usage statement is first-party, not independent audit. |
| [RTP-LLM technical README](https://github.com/alibaba/rtp-llm/blob/main/README_cn.md) | Documents system-prompt/context prefix caching, speculative decoding and weight-only INT8/INT4; optimization is across engine scheduling and kernels. | Features and performance vary by exact commit and hardware; do not infer compatibility with all current Qwen checkpoints or Ascend. |

### RTP-LLM paper lineage — performance vs. evolution (2026)

- [**RTP-LLM: High-Performance Alibaba LLM Inference Engine**](https://arxiv.org/abs/2605.29639) (May 28 preprint) describes the execution-level mechanisms: parallel model loading, P/D and multi-tier KV, modular speculative decoding, quantization and multimodal decoupling. Its comparative latency/throughput values are **author-reported, version/workload-specific**.
- [**RTP-LLM: Building an Evolvable and Reliable LLM Inference Engine at Alibaba Scale**](https://arxiv.org/abs/2611.00967) (October 31 submission, November announcement) focuses instead on separating model-specific execution from shared request/state/resource control, rapid model enablement and failure containment. The authors describe a large-scale deployed engine; no independent production or reliability experiment was performed by this catalog.

**Identity / novelty gate:** both discuss the **same evolving Alibaba engine**, and the May report already has a [canonical entry](../topics/distributed-serving.md). The November report is a useful **company-side engineering source**, not automatically another canonical paper. A separate row requires checking independent mechanism, methodology and baselines against the May source; the [scope audit](../reviews/ADJACENT_SCOPE_REVIEW_20261105.md) records the pending decision.

**Systems priority:** the **RTP-LLM runtime** is a more direct source for Alibaba Serving research than another incremental API model menu. Compare the shipped code with modern vLLM/SGLang under matched model, precision, concurrency and output correctness.

**Scope:** Architecture/runtime-relevant releases only. A model-family repository is not proof of a new online serving algorithm or NPU performance result; vLLM/SGLang backend implementation and checkpoint compatibility must be checked independently.
