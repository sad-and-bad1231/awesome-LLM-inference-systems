# Alibaba Group / Qwen

**A compact map of Alibaba's public LLM-system work:** Qwen model architecture → inference engines → distributed KV infrastructure → production serving research → edge inference.

[← Organizations](README.md) · [← Home](../README.md) · [Detailed source audit and evidence boundaries](../reviews/ALIBABA_PRIMARY_SOURCE_AUDIT_20261112.md)

## 1. The technology map

| Layer | Main work | What to understand |
|---|---|---|
| **Models** | [Qwen](https://github.com/QwenLM) · [Qwen3.8](https://github.com/QwenLM/Qwen3.8) · [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) | Dense/MoE evolution; hybrid recurrent + attention; sparse attention and host-side embedding offload. |
| **Inference engines** | [RTP-LLM](https://github.com/alibaba/rtp-llm) · **BladeLLM** ([PAI docs](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/)) | Two distinct Alibaba engines: RTP-LLM is open source; BladeLLM is a PAI engine documented through product and model reports, with no public engine source identified here. |
| **KV / memory infrastructure** | [Tair KVCache](https://github.com/alibaba/tair-kvcache) · [FlashKV](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache) | Global KV metadata, data transfer, tiered storage, cross-instance prefix reuse and trace-driven simulation. |
| **Serving systems research** | [LMetric](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) · [ServeGen](https://github.com/alibaba/ServeGen) · [EPIC](https://doi.org/10.1145/3789240.3829201) · [StriaTrace](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) | Request routing, real production workloads, MoE communication and production diagnosis. |
| **Edge inference** | [MNN](https://github.com/alibaba/MNN) · [MNN-Pocket](https://arxiv.org/abs/2611.12311) · [Walle](https://www.usenix.org/conference/osdi22/presentation/lv) | Cross-platform mobile/device inference and device-cloud execution. |
| **Training / RL** | [PAI-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch) · [ChatLearn](https://github.com/alibaba/ChatLearn) · [ROLL](https://github.com/alibaba/ROLL) · [ROCK](https://github.com/alibaba/ROCK) | Pretraining, post-training, rollout and agent-environment infrastructure; adjacent to, but not a replacement for, an inference engine. |

**Fast orientation:** Alibaba is not one monolithic stack. Qwen owns model architecture; RTP-LLM and PAI's BladeLLM are separate inference-engine lines; Tair KVCache and PAI FlashKV address shared cache infrastructure; several major systems papers study production routing, workload, communication and diagnosis.

## 2. Qwen: model architecture that changes execution

- [Qwen official repositories](https://github.com/QwenLM) are the entry point for model implementations and open weights. Qwen3 includes dense and MoE variants, reasoning modes, coding and multimodal families.
- [Qwen3-Next / Qwen3.5–3.8](https://github.com/QwenLM/Qwen3.8) develops a hybrid **Gated DeltaNet (GDN) recurrent state + attention** architecture. This creates two different state-management paths: recurrent state and conventional attention KV.
- [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) is the most useful current architecture preview: **GDN + Qwen Sparse Attention (QSA)**, Gated Residual, N-gram Embedding and asynchronous host-memory prefetch. It is explicitly a preview of the architecture direction for Qwen4, **not the Qwen4 release itself**.
- [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder), [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) and [Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) matter because long coding sessions and streaming multimodal inputs create different serving workloads from ordinary text chat.

**Read:** model repository → model card / technical report → the actual runtime implementation supporting that architecture. A model release is not, by itself, a serving-system contribution.

## 3. Inference engines and the PAI platform

### RTP-LLM — open-source production inference engine

[Code](https://github.com/alibaba/rtp-llm) · [Documentation](https://rtp-llm.ai/) · [May 2026 report](https://arxiv.org/abs/2605.29639) · [October 2026 engineering report](https://arxiv.org/abs/2611.00967)

Developed by Alibaba's Foundation Model Inference Team. The repository describes a C++ scheduling/batching runtime with KV management, quantization, multi-LoRA, speculative decoding, distributed execution and multimodal support. The 2026 reports discuss model loading, P/D disaggregation, multi-tier KV reuse and how a shared engine evolves across many models.

**Reading focus:** trace request lifecycle, scheduler, KV allocation/reuse, P/D transfer and backend dispatch in the code. The May and October reports describe the **same evolving engine**, not two independent systems.

### BladeLLM — PAI's in-house inference engine

[PAI deployment guide](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/) · [PAI acceleration overview](https://www.alibabacloud.com/help/en/pai/ai-acceleration-1/) · [Qwen2.5-1M technical report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf)

PAI describes BladeLLM as its high-performance LLM inference engine, with model-specific optimization, quantization, batching, GPU-memory management and asynchronous/distributed execution. The Qwen2.5-1M report says its API service is powered by BladeLLM and discusses long-sequence prefill/decode optimizations.

**Boundary:** BladeLLM is distinct from RTP-LLM. The public evidence used here is product documentation and technical reports; no public BladeLLM engine repository was identified. Do not infer source-level behavior from the product description.

### PAI deployment and managed serving

- [PAI-EAS LLM deployment](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/) is the managed deployment/service layer. It can expose different engines, including vLLM, SGLang and BladeLLM.
- [InferX](https://www.alibabacloud.com/help/en/pai/inferx-overview) documents inference orchestration such as routing, P/D coordination, cache-aware scheduling and model warm-up.

Keep the **engine**, **deployment platform** and **managed cache service** as separate layers.

## 4. KV infrastructure: Tair KVCache and FlashKV

### Tair KVCache — open-source global cache management and simulation

[Repository](https://github.com/alibaba/tair-kvcache) · [Architecture guide](https://github.com/alibaba/tair-kvcache/blob/main/docs/design/module_architecture.md) · [Chinese README](https://github.com/alibaba/tair-kvcache/blob/main/README_zh.md)

Two components are especially useful:

- **Tair KVCache Manager (KVCM):** a global metadata manager. It supports prefix / sliding-window / hybrid-attention matching, cache-location indexing, two-phase writes, capacity control, eviction, garbage collection and tier migration.
- **Tair KVCache HiSim:** a CPU-based inference simulator that replays workload traces to estimate TTFT, TPOT and throughput without occupying GPUs.

The key architectural idea is the separation of **metadata plane** (where is a cache entry, and is it readable?) from **data plane** (the engine transfers KV payloads directly to/from storage). Connectors are documented for vLLM, SGLang, RTP-LLM and TRT-LLM.

### FlashKV — PAI's managed cluster-wide KV cache service

[Official documentation](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache)

FlashKV shares prefix KV across service replicas and uses memory, disk and remote-storage tiers. It is a cache service used alongside an inference engine, **not an inference engine itself**.

**Do not conflate them:** Tair KVCache is a public codebase with KVCM and HiSim; FlashKV is documented as a PAI managed service. The sources reviewed here do not establish that both expose the same implementation.

## 5. Production LLM systems research

These works reveal how Alibaba studies real serving systems beyond model architecture.

| Work | Venue | Main question | Entry point |
|---|---|---|---|
| **LMetric / Simple Is Better** | OSDI 2026 | Combine KV reuse opportunity and instance load for request routing without a tuned linear weight. | [Paper](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) |
| **ServeGen** | NSDI 2026 | Generate realistic online workloads from billions of production requests across 12 models. | [Paper](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) · [code and traces](https://github.com/alibaba/ServeGen) |
| **ACDC / Batched in Back** | SOSP 2026 | Characterize and optimize offline batch inference; a different problem from online TTFT/TPOT serving. | [Paper](https://doi.org/10.1145/3830418.3843877) · [offline traces](https://github.com/alibaba/ServeGen/tree/main/data/offline) |
| **Model-as-a-Service in the Wild (xMaaS)** | ATC 2026 | Analyze production LLM clusters, model/application diversity, GPU allocation and P/D imbalance. | [Paper and trace](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-v2026-maas) |
| **StriaTrace** | OSDI 2026 | Low-overhead tracing and diagnosis for production LLM inference anomalies. | [Paper](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) |
| **EPIC / Balancing and Beyond** | SIGCOMM 2026 | MoE Expert Parallelism: balance expert compute and NIC traffic, adapt transport to topology, and overlap communication. | [Paper DOI](https://doi.org/10.1145/3789240.3829201) · [accepted-paper list](https://conferences.sigcomm.org/sigcomm/2026/accepted/) |
| **Chorus** | ATC 2026 | GPU–CPU cooperative serving for length-skewed decode. | [Accepted paper](https://atc.sigops.org/2026/accepted.html) |
| **CacheFS** | ATC 2026 | Peer-to-peer cooperative caching for model-weight distribution; **weight cache, not KV cache**. | [Accepted paper](https://atc.sigops.org/2026/accepted.html) |
| **Axon** | ATC 2026 | Asynchronous global KV-aware scheduling across instances for agentic workloads. | [Accepted paper](https://atc.sigops.org/2026/accepted.html) |
| **Asynchronous KV Cache Prefetching** | AAAI 2026 | Overlap attention compute with Hopper L2 prefetch to hide KV memory latency. | [Paper](https://doi.org/10.1609/aaai.v40i25.39224) · [code](https://github.com/alibaba/vllm_xformers_prefetch) |

**How to read the list:** LMetric is request routing; ServeGen/ACDC/xMaaS are workload and production evidence; EPIC is MoE communication; Chorus is CPU–GPU decode cooperation; CacheFS is weight distribution; Axon is distributed KV-aware scheduling; StriaTrace is observability. They solve different layers and should not be collapsed into one “Alibaba inference engine”.

The AAAI prefetch paper is already in our canonical [KV Cache & Context Memory](../topics/kv-cache-memory.md) list. LMetric, ServeGen, ACDC, xMaaS and StriaTrace are also already indexed. **EPIC, Chorus, CacheFS and Axon are conference-accepted papers but still require our strict source/method/artifact review before canonical admission.**

[Heterogeneity at Hyperscale (OSDI 2026)](https://www.usenix.org/conference/osdi26/presentation/li-suyi) is another useful adjacent work on heterogeneous GPU-cluster resource management; it is cluster scheduling, not an LLM request scheduler.

## 6. Edge inference and training ecosystem

- **[MNN](https://github.com/alibaba/MNN) / [MNN-LLM](https://github.com/alibaba/MNN/tree/master/transformers):** cross-platform inference runtime for mobile, PC and IoT. [Walle (OSDI 2022)](https://www.usenix.org/conference/osdi22/presentation/lv) is the earlier device-cloud collaborative system built around MNN.
- **[MNN-Pocket-0.3B](https://arxiv.org/abs/2611.12311):** a mobile-native model/runtime co-design; useful as an edge-inference example, not a cloud-serving baseline.
- **[PAI-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch) + [ChatLearn](https://github.com/alibaba/ChatLearn):** large-scale model training and RL orchestration, using Megatron/FSDP with vLLM/SGLang rollout.
- **[ROLL](https://github.com/alibaba/ROLL) + [ROCK](https://github.com/alibaba/ROCK):** large-scale LLM/agent RL training and environment management. Relevant to agentic post-training, but not online inference runtimes.

## 7. Suggested reading order

1. **Understand the model contract:** [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) — GDN, QSA, recurrent state, sparse indexer and host embedding prefetch.
2. **Understand the engine:** [RTP-LLM code](https://github.com/alibaba/rtp-llm) → [May report](https://arxiv.org/abs/2605.29639) → [October report](https://arxiv.org/abs/2611.00967). Read BladeLLM's PAI documentation separately.
3. **Understand cache infrastructure:** [Tair KVCache README](https://github.com/alibaba/tair-kvcache) → [module architecture](https://github.com/alibaba/tair-kvcache/blob/main/docs/design/module_architecture.md) → [FlashKV docs](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache).
4. **Understand production scheduling and communication:** LMetric → EPIC → ServeGen/ACDC → StriaTrace.
5. **Explore a separate branch:** MNN for edge inference; ChatLearn/ROLL for training and agentic RL.

**Evidence boundary:** first-party code, co-authored papers, product documentation and author-reported benchmarks are labeled separately in the [detailed audit](../reviews/ALIBABA_PRIMARY_SOURCE_AUDIT_20261112.md). A product description is not source-code evidence; an accepted paper is not automatically a canonical admission; author-reported performance is not independent reproduction.
