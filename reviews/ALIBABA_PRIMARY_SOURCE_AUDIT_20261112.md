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

### Additional direct systems work: observability, kernels and MoE communication

- **Asynchronous KV Cache Prefetching** — AAAI 2026. Uses Hopper `cp.async.bulk.prefetch.L2.global` to overlap future KV loads with attention computation in vLLM's XFormers backend. The authors report up to 2.15× attention-kernel efficiency and 1.97× end-to-end throughput on NVIDIA H20. [AAAI paper](https://doi.org/10.1609/aaai.v40i25.39224) · [author patch](https://github.com/alibaba/vllm_xformers_prefetch). **Already canonical** in [KV Cache & Context Memory](../topics/kv-cache-memory.md); GPU/Hopper-specific and not an Ascend result.
- **StriaTrace: Efficient Tracing and Diagnosis for Online LLM Inference** — OSDI 2026 (Operational Systems). Production-oriented low-overhead tracing uses key synchronization points, critical paths and anomaly-triggered detail; combines a dynamic regression roofline model with correlation-based diagnosis. The authors report 97.8% lower tracing overhead than alternatives and hundreds of diagnosed anomalies across 19 root causes. **Already canonical** in [Benchmarking & Systems Analysis](../topics/benchmarking-analysis.md); do not duplicate it. [Official OSDI paper](https://www.usenix.org/conference/osdi26/presentation/wu-haonan).
- **Balancing and Beyond: Communication-Centric Optimizations in Expert Parallelism (EPIC)** — SIGCOMM 2026, Alibaba Cloud. Addresses production MoE EP: compute-only EPLB leaves NIC/topology imbalance; EPIC balances expert compute and per-NIC traffic, performs intra-host expert migration, selects topology-adaptive transport and overlaps communication at expert granularity. **Strict admission and code/artifact review pending.** [Official SIGCOMM accepted list](https://conferences.sigcomm.org/sigcomm/2026/accepted/) · [DOI](https://doi.org/10.1145/3789240.3829201).

### ATC 2026 accepted papers — collaborations; strict admission pending

The official ATC accepted-paper list confirms all three papers below as **full accepted papers**, not merely poster signals. Their co-authorship must remain explicit; acceptance does not automatically satisfy our canonical G0–G5 admission rules.

- **Chorus: GPU–CPU Cooperative LLM Serving for Length-Skewed Decode** — HKUST / Nokia Bell Labs / Alibaba Group. Studies CPU–GPU cooperation under decode-length skew. [Official accepted list](https://atc.sigops.org/2026/accepted.html).
- **CacheFS: Peer-to-Peer Cooperative Caching for LLM Weight Distribution at Cloud Scale** — Zhejiang University / Alibaba Group. Focuses on **model-weight distribution**, not KV-cache reuse. [Official accepted list](https://atc.sigops.org/2026/accepted.html).
- **Axon: Asynchronous Global KV-Aware Scheduling Across Distributed Instances for Agentic Workloads** — University of Macau / Alibaba Group. A full ATC paper on distributed, asynchronous KV-aware scheduling; the poster listing is not its only publication status. [Official accepted list](https://atc.sigops.org/2026/accepted.html) · [lab publication page](https://cds-macau.github.io/publication/conference-paper/axon/).

**Adjacent agent infrastructure:** [Scaling LLM Agent Tool Access: The MCP Gateway](https://atc.sigops.org/2026/accepted.html) is also an ATC 2026 accepted Alibaba Cloud-led paper. It belongs to the agent tool-access/control layer, not the core model execution engine.

## 5. Alibaba inference engines and KV infrastructure

### BladeLLM — PAI's in-house inference engine

- [PAI acceleration overview](https://www.alibabacloud.com/help/en/pai/ai-acceleration-1/) lists BladeLLM as its LLM inference engine; [PAI deployment guide](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/) describes model-specific optimization, quantization, batching and GPU-memory management.
- The [Qwen2.5-1M technical report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf) says its API services are powered by BladeLLM and describes long-sequence prefill/decode optimization through kernels, pipeline parallelism and scheduling.
- **Evidence boundary:** this pass found product documentation and model-report references, but no public BladeLLM engine repository. Do not infer its internal implementation from product descriptions. BladeLLM is a **separate PAI engine**, not another name for RTP-LLM.

### PAI-EAS / InferX / FlashKV — managed deployment and cache services

- [PAI-EAS LLM deployment](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/) is the model deployment/service layer and can expose vLLM, SGLang or BladeLLM.
- [InferX overview](https://www.alibabacloud.com/help/en/pai/inferx-overview) documents routing, P/D orchestration, token-level rate limiting, cache-aware scheduling and model warm-up.
- [FlashKV documentation](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache) (updated Nov 2, 2026) describes a cluster-wide KV cache service with memory/disk/remote-storage tiers and cross-replica prefix reuse. The document explicitly says FlashKV is used alongside an inference engine and does not provide inference by itself.

**Evidence classification:** first-party product/documentation evidence. No public source for the full InferX scheduler or FlashKV implementation was identified here.

### Tair KVCache — open-source global cache management and simulation

- [Official repository](https://github.com/alibaba/tair-kvcache) releases **Tair KVCache Manager (KVCM)** and **Tair KVCache HiSim**.
- KVCM separates the **metadata plane** (cache lookup, location, state and capacity) from the **data plane** (engine-side KV payload transfer directly to storage). Its documented mechanisms include prefix/sliding-window/hybrid-attention matching, two-phase writes, pluggable storage backends, DRAM/SSD tiering, quota/watermark eviction, asynchronous GC and migration.
- The README documents connectors for vLLM, SGLang, RTP-LLM and TRT-LLM. See the [module architecture guide](https://github.com/alibaba/tair-kvcache/blob/main/docs/design/module_architecture.md).
- HiSim is a CPU-based inference simulator that replays workload traces to estimate TTFT, TPOT and throughput. The current README's concrete support claim is narrow (SGLang 0.5.6.post2 + Qwen3 Dense + H20, with author-reported prediction error below 5%); do not generalize this to arbitrary models/engines/hardware.

**Do not conflate Tair and FlashKV:** Tair KVCache is a public codebase with KVCM/HiSim; FlashKV is documented as a PAI managed service. The reviewed sources do not establish that they share the same implementation.

## 6. Edge inference: MNN and Walle

- [MNN](https://github.com/alibaba/MNN) is Alibaba's lightweight cross-platform inference/training runtime; [MNN-LLM](https://github.com/alibaba/MNN/tree/master/transformers) extends it to on-device LLM execution. The repository reports use across 30+ Alibaba apps and multiple device backends.
- [Walle (OSDI 2022)](https://www.usenix.org/conference/osdi22/presentation/lv) is the earlier device-cloud collaborative ML system. Its compute container is based on MNN; the paper describes operator decomposition and semi-automatic backend search to support many hardware backends.
- **MNN-Pocket-0.3B** (Nov 2026) is a co-designed mobile-native 300M model/runtime line: 32K context, QAT INT4 package reported at 173 MB. The [MNN README](https://github.com/alibaba/MNN) reports 350 tok/s on iPhone 18 Pro; the [technical report](https://arxiv.org/abs/2611.12311) reports up to 466 tok/s on iPad Pro M5. These are **different devices and author-reported results**, not a directly comparable benchmark.

MNN should be mapped as a distinct **edge/device inference** line; do not treat its phone throughput as a cloud-serving baseline.

## 7. Training and agent-RL ecosystem — supporting layer

| Project | What it does | Boundary |
|---|---|---|
| [PAI-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch) | Megatron-Core based LLM/VLM pretraining, SFT, RL and checkpoint conversion. | Training/finetuning infrastructure, not online serving. |
| [ChatLearn](https://github.com/alibaba/ChatLearn) | Distributed LLM alignment/RL orchestration with Megatron/FSDP training and vLLM/SGLang rollout. | RL control/dataflow layer; vLLM/SGLang remain the inference engines. |
| [ROLL](https://github.com/alibaba/ROLL) | Large-scale LLM RL library with multi-role resource scheduling and Megatron/SGLang/vLLM integration. | Training and rollout system, not a general-purpose serving runtime. |
| [ROCK](https://github.com/alibaba/ROCK) | Sandbox/environment management for agentic RL. | Agent environment infrastructure, not model inference. |
| [EasyDist](https://github.com/alibaba/easydist) | Automated parallelization across PyTorch/JAX and operator-level SPMD rules. | Parallelization infrastructure, not a complete serving engine. |
| [BladeDISC](https://github.com/alibaba/BladeDISC) | MLIR-based dynamic-shape compiler for TensorFlow/PyTorch, part of PAI-Blade. | Compiler lineage; not the current Qwen serving engine. |

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

**No canonical topic count change in this surface pass.** StriaTrace and the AAAI KV-prefetch paper are already canonical. EPIC, Chorus, CacheFS and Axon are accepted papers awaiting strict source/method/artifact review; MNN-Pocket is a technical report to assess under strict rules. The October RTP report is a same-engine follow-up, not an automatic second entry.

## 10. Next deep-dive priorities

1. **RTP-LLM source audit:** freeze a commit; trace frontend → scheduler → request state → KV → P/D → kernel/backend dispatch.
2. **Tair KVCache:** inspect KVCM metadata/data-plane contracts, connector lifecycle, tier migration, eviction/GC and HiSim's simulation assumptions; compare with the separate FlashKV product docs.
3. **BladeLLM:** collect first-party documentation and technical-report evidence; keep internal implementation unknown unless source becomes public.
4. **EPIC + ATC systems:** inspect expert placement/communication and the Chorus, CacheFS and Axon full papers/artifacts before any canonical admission.
5. **Qwen3.8-Flash-Next:** map GDN recurrent state + QSA sparse attention + MTP + N-gram host offload to actual runtime support and correctness.
6. **Production workloads:** connect ServeGen, ACDC and xMaaS to our benchmark methodology; keep online, offline and cluster traces separate.
7. **MNN edge runtime:** separate track only if on-device/heterogeneous inference becomes a deliberate objective.

**Ascend compatibility warning:** the current vLLM-Ascend Qwen3.8-Flash-Next guide names A2/A3/950DT deployment paths; it does not establish compatibility with our pinned 910B2/CANN 9.1 baseline. Do not infer support from the model being open-weight. [Current guide](https://docs.vllm.ai/projects/ascend/en/main/tutorials/models/Qwen3.8-Flash-Next.html).

**Decision:** this pass establishes the surface map and research priorities. Deep implementation claims, benchmark claims and paper admission are deferred to separate evidence-gated passes.
