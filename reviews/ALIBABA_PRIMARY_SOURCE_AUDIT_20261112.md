# Alibaba / Qwen — primary-source surface audit (2026-11-12)

**Status: SURFACE_MAP_COMPLETE / DEEP_CODE_AUDIT_PENDING / NO_NEW_PAPER_ADMISSION.**

This is the first-pass map of Alibaba Group's earlier work before the next Qwen generation. It follows the evidence discipline used in the Baidu audit, but does **not** pretend that reading project descriptions is equivalent to tracing implementation or reproducing performance. The current canonical paper inventory remains **853**; this receipt adds no paper rows.

## 1. Executive map: Alibaba is not just Qwen

There are six distinct technical layers worth keeping separate:

1. **Foundation-model research — DAMO Academy → Qwen/Tongyi:** M6/OFA as earlier multimodal-pretraining lineage; Qwen 1/2/2.5/3 and the Qwen3.5–3.8 hybrid/MoE evolution; reasoning, coding and omni-modal variants.
2. **Production online inference engine — RTP-LLM:** a public Alibaba-owned C++ inference engine, with production-serving claims and two 2026 technical reports.
3. **Serving policy and production evidence — Alibaba Cloud PAI / xMaaS:** LMetric request routing, ServeGen online workload generation, ACDC offline inference, xMaaS production traces and large-cluster scheduling research.
4. **Managed inference platform — InferX / FlashKV:** documented router, cache-aware scheduling, shared multi-tier KV and model warm-up. These are **product/documentation evidence**, not public engine source.
5. **On-device inference — MNN / MNN-LLM:** long-running mobile/edge runtime, rooted in Walle (OSDI'22), now supporting local multimodal LLMs and MNN-Pocket.
6. **Training/compiler/hardware support — PAI-Megatron-Patch, ChatLearn, EasyDist, BladeDISC, T-Head:** important surrounding infrastructure, but not interchangeable with an online LLM serving engine.

**First-pass conclusion:** the highest-value Alibaba inference research is the combination of **RTP-LLM + PAI/xMaaS production serving research + Qwen's changing model execution contracts**. MNN is a separate edge-inference lineage. Training/compiler and silicon should be retained as supporting layers, not allowed to dilute the inference focus.

## 2. Model and architecture lineage

### 2.1 Before Qwen: DAMO Academy's M6 / OFA

- [M6: A Chinese Multimodal Pretrainer](https://arxiv.org/abs/2103.00823), KDD 2021: a unified text/image/multimodal pretraining effort. The paper reports a 10B-scale model; the later [M6-10T: A Sharing-Delinking Paradigm for Efficient Multi-Trillion Parameter Pretraining](https://arxiv.org/abs/2110.03888) studies a 10T-parameter training recipe and CPU offload. These are **historical large-scale training/multimodal research**, not online LLM inference engines.
- [OFA: Unifying Architectures, Tasks, and Modalities Through a Simple Sequence-to-Sequence Learning Framework](https://proceedings.mlr.press/v162/wang22al.html), ICML 2022: task/modality-agnostic sequence-to-sequence multimodal pretraining. The Qwen team's [OFA project page](https://qwenlm.github.io/blog/ofa/) preserves the first-party context.

These projects establish that Alibaba's model lineage did not begin with Qwen; however, the current inference-engine investigation should start from RTP-LLM and the modern Qwen architectures, not attempt to catalog every DAMO NLP/CV publication.

### 2.2 Qwen generation map

| Family / milestone | What matters to inference | Primary evidence |
|---|---|---|
| **Qwen 1 / 2 / 2.5** (2023–24) | Dense and MoE model scaling, multilingual capability, long context and specialized model families. Qwen2.5 reports 18T pretraining tokens and extensive post-training; these are model/training claims, not engine speedups. | [Qwen2.5 report](https://arxiv.org/abs/2412.15115) · [Qwen official repo](https://github.com/QwenLM/Qwen) |
| **QwQ / Qwen3** (2024–25) | Reasoning-heavy generation and hybrid thinking/non-thinking modes; Qwen3 spans dense and MoE variants. Output-length and reasoning distributions become first-class serving workload properties. | [Qwen3 report](https://arxiv.org/abs/2505.09388) · [official Qwen3 source](https://github.com/QwenLM/Qwen3) |
| **Qwen3-Coder / Coder-Next** | Coding-agent workload, long context and executable environment interaction; relevant to long-lived sessions, tool-use bursts and prefix reuse. | [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) · [Coder-Next report](https://arxiv.org/abs/2603.00729) |
| **Qwen2.5-Omni → Qwen3-Omni** | End-to-end text/image/audio/video input and streamed text/speech output; Thinker–Talker and codec-token generation introduce stage and streaming-latency contracts beyond text-only decode. | [Qwen2.5-Omni report](https://arxiv.org/abs/2503.20215) · [Qwen3-Omni report](https://arxiv.org/abs/2509.17765) |
| **Qwen3-Next → Qwen3.5/3.6/3.7/3.8** | Hybrid recurrent Gated DeltaNet (GDN) plus attention, sparse MoE, MTP and changing state/cache requirements. This is a major change in the model execution contract, not merely a larger checkpoint. | [Qwen3.8 official repository](https://github.com/QwenLM/Qwen3.8) |
| **Qwen3.8-Flash-Next** (Aug 2026) | An explicit early preview of the architecture intended for Qwen4: GDN + Qwen Sparse Attention (QSA), micro-block indexer, four-branch Gated Residual, N-gram embedding and MTP. Main model 125B + 51B embedding parameters, 6B active/token per the model card. Host-side embedding offload/prefetch is particularly relevant to memory hierarchy. | [official repository and technical report](https://github.com/QwenLM/Qwen3.8-Flash-Next) · [first-party design explanation](https://www.alibabacloud.com/blog/qwen3-8-flash-next-a-new-architecture-towardsultimate-cost-efficiency_603501) |

**Qwen4 boundary:** Alibaba's September 25, 2026 Apsara announcement says Qwen4 is **in training**. Qwen3.8-Flash-Next is explicitly an architecture preview, **not Qwen4 itself**. Do not invent Qwen4's final architecture, checkpoint, launch date or runtime support. Track it as a forward watch item. [First-party announcement](https://home.alibabagroup.com/en-US/document-2041268239081668608).

**RSI boundary:** the same Apsara announcement reports Qwen3.8-Max iterative improvement and a chip-design/EDA experiment. These are company-reported model/agent feedback-loop claims; they do **not** demonstrate recursive self-improvement of an inference engine. Keep this separate from the existing autonomous-engine-evolution frontier.

## 3. RTP-LLM: Alibaba's own production inference engine

**Project:** [alibaba/rtp-llm](https://github.com/alibaba/rtp-llm) · [documentation](https://rtp-llm.ai/).

The first-party repository identifies RTP-LLM as an engine developed by Alibaba's Foundation Model Inference Team and reports use across Taobao, Tmall, Xianyu, Cainiao, Amap, Ele.me, AliExpress and Lazada. It describes CUDA kernels (PagedAttention/FlashAttention/FlashDecoding), dynamic batching, weight-only INT8/INT4, adaptive KV quantization, multi-LoRA, prefix/system-prompt cache and speculative decoding.

The 0.2.0 release feature list additionally names P/D disaggregation, EPLB, microbatch/overlap, MTP, DeepEP, 3FS, FP8 KV, KV reuse, Attention–FFN disaggregation and frontend/backend disaggregation. These are **feature claims at the release/version boundary**; support and correctness must be checked against exact commit, hardware and model. [0.2.0 release notes](https://github.com/alibaba/rtp-llm/releases/tag/v0.2.0).

### Two 2026 RTP-LLM reports — same evolving engine, different questions

- [RTP-LLM: High-Performance Alibaba LLM Inference Engine](https://arxiv.org/abs/2605.29639), May 28, 2026: describes file-order-driven and parallel model loading, I/O/communication overlap, P/D, multi-tier KV reuse, modular speculative decoding, adaptive KV quantization and multimodal decoupling. All reported comparisons (including vLLM/SGLang) remain **author-reported and workload/version-specific**.
- [RTP-LLM: Building an Evolvable and Reliable LLM Inference Engine at Alibaba Scale](https://arxiv.org/abs/2611.00967), Oct 31, 2026: focuses on separating model-specific execution from shared request processing, state management and resource coordination; reports support for around 100 models and hundreds of trillions of tokens/day. These are **author-reported production scale claims**, not independently audited telemetry.

**Identity/novelty decision:** both papers describe the **same evolving RTP-LLM project**. The later report is a valuable architecture/reliability account, not automatically a second independent engine or canonical paper row. The May report already has a canonical entry under [Distributed & Disaggregated Serving](../topics/distributed-serving.md).

**Attribution boundary:** RTP-LLM's own README acknowledges its foundation in [FasterTransformer](https://github.com/NVIDIA/FasterTransformer), integration of some [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) kernels, and inspiration from [vLLM](https://github.com/vllm-project/vllm), Transformers and other projects. This is normal ecosystem evolution; do not attribute every familiar mechanism as an Alibaba invention.

## 4. Production-serving research and workload evidence

These works form a coherent research line: **measure production workload → generate representative replay → design routing/scheduling → understand cluster-level resource constraints**.

| Work | Venue / status | Main question and source |
|---|---|---|
| **LMetric / Simple Is Better: Multiplication May Be All You Need for LLM Request Scheduling** | OSDI 2026 | Combines a KV-aware indicator (new prefill tokens if routed to an instance) and a load indicator (current batch size) multiplicatively to avoid tuning a linear-combination weight. [Publisher page](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan). Co-authored by SJTU and Alibaba. |
| **ServeGen: Workload Characterization and Generation of LLM Serving in Production** | NSDI 2026 | Uses billions of requests across 12 production models to capture bursty arrivals, temporal I/O-length shifts, multimodal composition and reasoning-length distributions. [Paper](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) · [code/data](https://github.com/alibaba/ServeGen). |
| **Batched in Back / ACDC** | SOSP 2026 | Studies offline batch inference: 1.5M tasks and 23B requests in the reported production analysis; exploits determinism and throughput orientation rather than treating the workload as online arrivals. The repository publishes anonymized trace subsets. [DOI / paper identity](https://doi.org/10.1145/3830418.3843877) · [offline traces](https://github.com/alibaba/ServeGen/tree/main/data/offline). |
| **Model-as-a-Service in the Wild** | ATC 2026 | Six-month production LLM inference trace across 56 clusters, 30 GPU types, >100,000 GPUs, ~300,000 applications and ~70,000 model variants. Useful for memory overprovisioning, cold-model residency and P/D imbalance research. [Dataset and reproduction scripts](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-v2026-maas). |
| **Heterogeneity at Hyperscale** | OSDI 2026 | Six-month Alibaba Serverless Infrastructure trace across 155,410 GPUs and 81 departments; studies stranded capacity, heterogeneous resources and cluster scheduling. Reports a GPU defragmentation solution and SpotGPU. This is **general AI-cluster resource management**, not an LLM request scheduler. [Paper](https://www.usenix.org/conference/osdi26/presentation/li-suyi) · [trace](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-gpu-v2026). |

**Do not conflate the datasets:** ServeGen online traces, ACDC offline task traces, xMaaS LLM-cluster traces and ASI heterogeneous GPU-cluster traces describe different units and time scales. They are complementary, not interchangeable benchmarks.

### New ATC 2026 collaboration signals — candidate review, not admission

- **Chorus: GPU–CPU Cooperative LLM Serving for Length-Skewed Decode** — HKUST/Nokia/Alibaba co-authorship; [ATC accepted-paper record](https://atc.sigops.org/2026/accepted.html). Worth reading for CPU–GPU cooperation under decode-length skew. Full mechanism and artifact audit remains pending.
- **CacheFS: Peer-to-Peer Cooperative Caching for LLM Weight Distribution at Cloud Scale** — Zhejiang University/Alibaba co-authorship; [ATC accepted-paper record](https://atc.sigops.org/2026/accepted.html), [artifact status](https://sysartifacts.github.io/atc2026/results). Relevant to weight distribution/model loading, but not a KV cache paper.
- **Axon: Asynchronous Global KV-Aware Scheduling Across Distributed Instances for Agentic Workloads** — University of Macau/Alibaba co-authorship; appears in the [ATC poster listing](https://atc.sigops.org/2026/poster.html). Track as a collaboration signal; verify its exact publication/artifact status before treating it as a full paper admission.

These are not exclusively Alibaba-owned projects. The conference's accepted/poster status and author affiliations should remain explicit.

## 5. Alibaba Cloud PAI: InferX and FlashKV

- [InferX overview](https://www.alibabacloud.com/help/en/pai/inferx-overview) describes an enterprise inference platform with intelligent routing, P/D orchestration, token-level rate limiting, cache-aware scheduling, model warm-up and global scheduling.
- [FlashKV documentation](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache) describes a distributed KV cache service with memory/disk/remote-storage tiers and cross-instance prefix reuse.
- [InferX configuration center](https://www.alibabacloud.com/help/en/pai/inferx-config-center) documents session affinity → prefix cache → load balancing routing priorities, plus traffic splitting, mirroring and P/D-specific scheduling.

**Evidence classification: PRODUCT/DOCUMENTATION ONLY in this pass.** No public source for the full InferX scheduler or FlashKV implementation was identified here. The product docs establish externally documented behavior and operational configuration, not the internal algorithms, implementation correctness or independently measured speedups. FlashKV is a **KV service**, not a complete inference engine.

## 6. Edge inference: MNN and Walle

- [MNN](https://github.com/alibaba/MNN) is Alibaba's lightweight cross-platform inference/training runtime; [MNN-LLM](https://github.com/alibaba/MNN/tree/master/transformers) extends it to on-device LLM execution. The repository reports use across 30+ Alibaba apps and multiple device backends.
- [Walle (OSDI 2022)](https://www.usenix.org/conference/osdi22/presentation/lv) is the earlier device-cloud collaborative ML system. Its compute container is based on MNN; the paper describes operator decomposition and semi-automatic backend search to support many hardware backends.
- **MNN-Pocket-0.3B** (Nov 2026) is a co-designed mobile-native 300M model/runtime line: 32K context, QAT INT4 package reported at 173 MB. The [MNN README](https://github.com/alibaba/MNN) reports 350 tok/s on iPhone 18 Pro; the [technical report](https://arxiv.org/abs/2611.12311) reports up to 466 tok/s on iPad Pro M5. These are **different devices and author-reported results**, not a directly comparable benchmark.

MNN should be mapped as a distinct **edge/device inference** line; do not treat its phone throughput as a cloud-serving baseline.

## 7. Training and compiler ecosystem — supporting layer

| Project | What it does | Boundary |
|---|---|---|
| [PAI-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch) | Megatron-Core based large-scale LLM/VLM pretraining, SFT, RL and checkpoint conversion; tracks Qwen3/Next/Omni and other model families. | Primarily **training/finetuning infrastructure**, not online serving. |
| [ChatLearn](https://github.com/alibaba/ChatLearn) | Distributed LLM alignment/RL orchestration; integrates Megatron/FSDP training with vLLM/SGLang rollout engines. | RL training/control plane; vLLM/SGLang remain the serving/rollout engines. |
| [EasyDist](https://github.com/alibaba/easydist) | Automated parallelization across PyTorch/JAX and operator-level SPMD rules. | Training/inference parallelization infrastructure; not a full serving runtime. |
| [BladeDISC](https://github.com/alibaba/BladeDISC) | MLIR-based dynamic-shape compiler for TensorFlow/PyTorch, part of PAI-Blade. | Important compiler lineage, but the visible major release history is older (2023); do not call it the current Qwen serving engine. |

## 8. Hardware and future watch

- [T-Head Zhenwu V900](https://home.alibabagroup.com/en-US/document-2041268239081668608) was announced at Apsara 2026 with FP8/FP4 support, 216 GB memory and 1,200 GB/s inter-chip bandwidth; the announcement targets Q1 2027 mass production. This is a **roadmap/product announcement**, not an independently verified performance comparison or a public runtime stack.
- Qwen4 is reported **in training**; Qwen3.8-Flash-Next is the public architecture preview. Track actual model card, weights, framework support and hardware compatibility only when released.

## 9. What is already in our canonical paper pool

No duplicates should be added for the following already-indexed works:

- [LMetric](../topics/runtime-scheduling.md) — Runtime & Scheduling.
- [ServeGen](../topics/benchmarking-analysis.md) — Benchmarking & Systems Analysis.
- [ACDC](../topics/runtime-scheduling.md) — Offline workload scheduling/execution.
- [RTP-LLM (May 2026 report)](../topics/distributed-serving.md) — Distributed & Disaggregated Serving.
- [Heterogeneity at Hyperscale](../topics/distributed-serving.md) and [Model-as-a-Service in the Wild](../topics/distributed-serving.md) — cluster/production workload analysis.

**No canonical topic count change in this surface pass.** MNN-Pocket is a new technical report to assess under the strict paper rules; Chorus and CacheFS need full-text/artifact review; the October RTP report is a same-engine follow-up, not an automatic second entry.

## 10. Next deep-dive priorities

1. **RTP-LLM source audit:** freeze a commit; map frontend/router → scheduler → request state → KV allocator/cache → P/D handoff → backend/kernel dispatch. Compare only equivalent boundaries against pinned vLLM and SGLang.
2. **PAI routing + FlashKV:** establish the real control/data path, cache key and ownership semantics, eviction/persistence, transfer protocol, failure handling and routing consistency. Public docs alone are insufficient.
3. **Qwen3.8-Flash-Next execution contract:** GDN recurrent state + QSA sparse attention + MTP + N-gram host offload. Trace actual runtime support and correctness rather than treating it as ordinary dense/MoE attention.
4. **Production workload research:** connect ServeGen, ACDC and xMaaS traces to our benchmark/workload methodology; keep online, offline and cluster traces separate.
5. **MNN edge runtime:** separate track only if on-device/heterogeneous inference is a deliberate objective.

**Ascend compatibility warning:** the current vLLM-Ascend Qwen3.8-Flash-Next guide names A2/A3/950DT deployment paths; it does not establish compatibility with our pinned 910B2/CANN 9.1 baseline. Do not infer support from the model being open-weight. [Current guide](https://docs.vllm.ai/projects/ascend/en/main/tutorials/models/Qwen3.8-Flash-Next.html).

**Decision:** this pass establishes the surface map and research priorities. Deep implementation claims, benchmark claims and paper admission are deferred to separate evidence-gated passes.
