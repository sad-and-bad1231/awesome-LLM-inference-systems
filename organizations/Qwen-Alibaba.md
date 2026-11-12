# Qwen (Alibaba)

The Qwen team's publicly released model families and inference-related model architecture. Runtime implementations from vLLM/SGLang/LMDeploy remain credited to their respective maintainers.

[← Organizations](README.md) · [← Home](../README.md)

## Official model-family coverage (2026-11-12)

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

### Production workload, routing and cache infrastructure

| Work | System boundary | Source / evidence |
|---|---|---|
| **LMetric / Simple Is Better** (OSDI 2026) | Instance-level request routing: combines cache-aware recomputation cost and current batch load. | [USENIX paper](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) · coauthored with SJTU; canonical entry already in [Runtime & Scheduling](../topics/runtime-scheduling.md). |
| **ServeGen** (NSDI 2026) | Online workload characterization and realistic request generation from Alibaba Cloud Model Studio production traffic. | [Paper](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) · [official traces/code](https://github.com/alibaba/ServeGen); already canonical in [Benchmarking](../topics/benchmarking-analysis.md). |
| **ACDC / Batched in Back** (SOSP 2026) | Offline batch inference, a separate workload and scheduling problem from online TTFT/TPOT serving. | [Paper](https://doi.org/10.1145/3830418.3843877) · [offline trace](https://github.com/alibaba/ServeGen/tree/main/data/offline); already canonical in [Runtime & Scheduling](../topics/runtime-scheduling.md). |
| **xMaaS / Model-as-a-Service in the Wild** (ATC 2026) | Production cluster/application/model-level LLM inference trace; online and offline jobs, heterogeneous GPUs and P/D imbalance. | [Official dataset](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-v2026-maas); already canonical in [Distributed Serving](../topics/distributed-serving.md). |
| **Heterogeneity at Hyperscale** (OSDI 2026) | General AI-cluster resource scheduling and heterogeneity, not an LLM request scheduler. | [Paper](https://www.usenix.org/conference/osdi26/presentation/li-suyi) · [GPU cluster trace](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2026); already canonical. |

### PAI managed inference: InferX / FlashKV

- [InferX](https://www.alibabacloud.com/help/en/pai/inferx-overview) is documented as an enterprise inference platform with intelligent routing, cache-aware scheduling, P/D orchestration, model warm-up and global scheduling.
- [FlashKV](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache) is documented as a distributed multi-tier KV cache service (memory/disk/remote storage) for cross-instance prefix reuse.

**Evidence boundary:** these are first-party product documents. This profile has not identified public source for the full InferX router or FlashKV implementation; do not attribute a specific algorithm, internal data structure or independently measured speedup without further evidence. FlashKV is a KV service, not a complete inference engine.

### Edge inference and device-cloud lineage

- [Walle (OSDI 2022)](https://www.usenix.org/conference/osdi22/presentation/lv) is the production device-cloud collaborative ML system whose compute container is based on MNN; its paper describes operator decomposition and semi-automatic backend search.
- [MNN](https://github.com/alibaba/MNN) is a cross-platform device/edge inference runtime; its current line includes MNN-LLM and the [MNN-Pocket-0.3B report](https://arxiv.org/abs/2611.12311). The MNN README reports 350 tok/s on iPhone 18 Pro, while the report states up to 466 tok/s on iPad Pro M5: distinct device results, not a head-to-head comparison.

### Supporting training/compiler stack

- [PAI-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch): Megatron-Core based LLM/VLM pretraining, SFT, RL and checkpoint conversion.
- [ChatLearn](https://github.com/alibaba/ChatLearn): distributed LLM alignment/RL orchestration; supports vLLM/SGLang as rollout engines.
- [EasyDist](https://github.com/alibaba/easydist): automated parallelization and SPMD rules for PyTorch/JAX.
- [BladeDISC](https://github.com/alibaba/BladeDISC): historical PAI-Blade dynamic-shape ML compiler; important compiler lineage, but not the current RTP-LLM serving runtime.

**Qwen4 status:** Alibaba's September 2026 Apsara announcement says Qwen4 is in training. [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) is explicitly an early architecture preview, not the released Qwen4 model. No final Qwen4 architecture or deployment support should be inferred.

**Surface-audit receipt:** [Alibaba primary-source audit (2026-11-12)](../reviews/ALIBABA_PRIMARY_SOURCE_AUDIT_20261112.md) records the broader research map, paper-pool crosswalk, product-only boundaries and next deep-audit gates.

### RTP-LLM paper lineage — performance vs. evolution (2026)

- [**RTP-LLM: High-Performance Alibaba LLM Inference Engine**](https://arxiv.org/abs/2605.29639) (May 28 preprint) describes the execution-level mechanisms: parallel model loading, P/D and multi-tier KV, modular speculative decoding, quantization and multimodal decoupling. Its comparative latency/throughput values are **author-reported, version/workload-specific**.
- [**RTP-LLM: Building an Evolvable and Reliable LLM Inference Engine at Alibaba Scale**](https://arxiv.org/abs/2611.00967) (October 31 submission, November announcement) focuses instead on separating model-specific execution from shared request/state/resource control, rapid model enablement and failure containment. The authors describe a large-scale deployed engine; no independent production or reliability experiment was performed by this catalog.

**Identity / novelty gate:** both discuss the **same evolving Alibaba engine**, and the May report already has a [canonical entry](../topics/distributed-serving.md). The November report is a useful **company-side engineering source**, not automatically another canonical paper. A separate row requires checking independent mechanism, methodology and baselines against the May source; the [scope audit](../reviews/ADJACENT_SCOPE_REVIEW_20261105.md) records the pending decision.

**Systems priority:** the **RTP-LLM runtime** is a more direct source for Alibaba Serving research than another incremental API model menu. Compare the shipped code with modern vLLM/SGLang under matched model, precision, concurrency and output correctness.

**Scope:** Architecture/runtime-relevant releases only. A model-family repository is not proof of a new online serving algorithm or NPU performance result; vLLM/SGLang backend implementation and checkpoint compatibility must be checked independently.
