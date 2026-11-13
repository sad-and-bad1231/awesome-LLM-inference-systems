# MiniMax + ByteDance — primary-source organization audit (2026-11-13)

## Decision and scope

Expand **two existing organization profiles** into readable, first-party-sourced technical maps: model lineage, multimodal generation workloads, open-code systems mechanisms, deployable integrations, and limits of what can be claimed about proprietary runtime internals. The source audit follows [organization admission rules](../organizations/README.md) and [G0–G5 scope boundaries](../STRICT_REVIEW.md).

**Editorial outcome:** organization documentation only. **Zero** new canonical paper rows, so the current topic corpus remains **930**. This is not a complete source-level reproduction, independent deployment verification, or quantitative benchmark.

## MiniMax — anchors and boundaries

| First-party source | Verified, useful signal | Scope restriction |
|---|---|---|
| [M3 research](https://www.minimax.io/blog/minimax-m3) · [model code](https://github.com/MiniMax-AI/MiniMax-M3) · [MSA paper](https://arxiv.org/abs/2606.13392) | Indexed/block-sparse MSA, KV-outer-gather-Q, 1M context and native image/video understanding; self-host deployment references | Vendor prefill/decode acceleration is measured in a particular **M3 vs M2** comparison, not an isolated, cross-accelerator operator benchmark |
| [M3.1-Flash model](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) · [Oct 19 release](https://www.minimax.io/blog/minimax-m31f) | 428B/23B MoE, sparse attention throughout, attention/expert QAT and a released DSpark draft head | Release of the model/drafter is **not** independent verification of speculation acceptance, speedups or CANN support |
| [H3 open repository](https://github.com/MiniMax-AI/MiniMax-H3) · [research](https://www.minimax.io/blog/minimax-h3) | H3-Context-IR / Base / Regenerate-2K stages; VisualVAE and AudioVAE; 33B dense Omni Transformer and inference-cacheable AdaLN parameters | **H3-Context-IR is hosted, not released**; public initial inference supports **full attention**, while sparse attention is described but not yet shipped in that release |
| [H3-Image Nov 11 announcement](https://www.minimax.io/blog/minimax-h3-image) · [weights](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image) | Open-weight image generation/editing, 4K and 16 reference image inputs, deployment/sampling-step optimization | Company under-10s claim is **not** independently reproduced or normalized for hardware/quality |
| [Music 3.0 technical post](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model) · [Speech 2.8 release](https://www.minimax.io/news/minimax-speech-28) | Global–local hybrid language modeling + RVQ/Flow-VAE for music; expressive speech synthesis | Do not transpose audio-generation quality claims into autoregressive text-serving latency |

MiniMax's [open-weight H3 architecture repository](https://github.com/MiniMax-AI/MiniMax-H3) is especially valuable because it **states what is absent**. A local full-attention pipeline and hosted end-to-end product are materially different workloads.

## ByteDance — anchors and boundaries

| First-party source | Verified, useful signal | Scope restriction |
|---|---|---|
| [Seed model directory](https://seed.bytedance.com/en/models) · [Seed official research](https://seed.bytedance.com/en/research) | Seed2.1, Seedance 2.5, Seedream 5.5, SeedRealtime and Seed Audio 1.0; includes vision, robotics and science adjacent lines | Featured model/menu entries are **not** kernel/source/production engine evidence |
| [Seedream 5.5 Nov 9](https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5) · [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) | Multi-turn editing consistency and RGBA output; up-to-30s generation and multimodal referencing | Quality/duration are not measured model-serving throughput or latency |
| [SeedRealtime Aug 5](https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction) | Native full-duplex audio/video/text interaction and active observation | End-to-end interaction timing needs streaming and interruption metrics, not only text-token TTFT |
| [Triton-distributed code](https://github.com/ByteDance-Seed/Triton-distributed) · [paper](https://arxiv.org/abs/2504.19442) | Distributed compiler, compute/communication overlap, FlashComm EP and distributed decode; historical Ascend RDMA | Default **Triton 3.7** branch's Ascend build is **not integrated**; earlier **triton-v3.4** branch only, no assumed 910B2/CANN 9.1 compatibility |
| [FLUX/COMET code](https://github.com/bytedance/flux) · [MLSys 2025 paper](https://seed.bytedance.com/en/public_papers/comet-fine-grained-computation-communication-overlapping-for-mixture-of-experts) | Fine-grained overlap and fused EP communication/computation | Published cluster-scale deployment and prominent numbers concern **training**, not a blanket LLM online Serving gain |
| [Volcano ServingKit docs](https://docs.volcengine.com/docs/vke/servingkit-overview?lang=zh) | Production offering with P/D disaggregation, EIC-backed KV, orchestration, gateway, observability, model distribution, and diffusion-serving support | Integration with vLLM/SGLang/Dynamo is documented but proprietary internal source and Seed's direct production engine are **not** established |
| [Charon](https://arxiv.org/abs/2605.17164) · [ByteIR](https://github.com/bytedance/byteir) | Simulation for training/inference deployment; MLIR compilation substrate | Simulated predictions ≠ directly observed GPU throughput; a compiler is not a token scheduler |
| [ByteTransformer](https://github.com/bytedance/ByteTransformer) · [ByteExpress](https://arxiv.org/abs/2610.12815) | Older BERT encoder kernels; production RDMA transport in parameter-server inference/training | Respect **BERT encoder** and **recommendation/search parameter-server** workload boundaries, not autoregressive LLM or KV-transfer evidence |

## Inclusion and deferral

**KEEP_ORG:** Source-linked model families, H3 public implementation boundary, MSA/DSpark, SeedRealtime workload, Triton-distributed, FLUX/COMET, TileLink, ByteIR, ServingKit, Charon, UltraMem and RDMA/ByteExpress (with workload qualifier).

**DEFER_TOPIC:** No new canonical topic row until cross-checking for duplicates against all eight topic categories and validating individual paper novelty/evidence. Existing organization profiles are navigational pointers, **not** a competing bibliography.

**UNVERIFIED / do not claim:**
- MiniMax H3 full hosted pipeline or unreleased sparse kernel is self-hostable from the public repository.
- MiniMax DSpark acceptance or a given model's 1M-context throughput is reproducible on Ascend 910B2.
- Triton-distributed's main branch provides a tested Ascend 910B2 backend.
- FLUX training gains, ByteExpress's parameter-server latency or Volcano ServingKit marketing results imply a specific vLLM-Ascend speedup.
- Seed products/Volcano services share one publicly inspectable production runtime.

## Change receipt

Updated [MiniMax](../organizations/MiniMax.md), [ByteDance](../organizations/ByteDance.md) and [organization index](../organizations/README.md). Added this dated audit to the [review index](README.md). No modifications to canonical paper files or paper counts, no unsupported benchmark replication.

## November 13 follow-up — company-blueprint alignment

The first pass covered model lines, select execution details and evidence boundaries. A follow-up compared the current [Baidu](../organizations/Baidu.md), [Alibaba](../organizations/Qwen-Alibaba.md) and [Tencent](../organizations/Tencent.md) profiles and corrected the **reading hierarchy**: technology map first, then key model families, representative research, inference/AI infrastructure and product ecosystem. No kernel audit, paper intake or new benchmark was performed.

- **MiniMax:** Added first-party [Forge agent RL](https://www.minimax.io/blog/forge-scalable-agent-rl-en-1779896141), [MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution), [Agent Team](https://www.minimax.io/blog/minimax-agent-team-long-running-1779893953) and [company product coverage](https://www.minimax.io/about) alongside M3/M3.1, H3/H3-Image, Speech and Music. These works are separate **training/reasoning/agent-runtime** tracks, not proof of a released low-level inference engine.
- **ByteDance:** Added [Seed's research directory](https://seed.bytedance.com/en/research), [MegaScale-Omni and other AI Infra research](https://seed.bytedance.com/en/research), [VeOmni](https://github.com/ByteDance-Seed/VeOmni), [ByteDance's official product portfolio](https://www.bytedance.com/products-services) and a company-to-cloud view including Doubao, creative tools and Volcano/BytePlus. Company products reveal application categories, **not** proprietary deployment topology or system ownership.
- **Editorial:** Shortened granular execution notes within the live pages, leaving original research/model/repository links and the evidence boundaries available. Navigation and reading order now match the broader organizational treatment of recent Baidu/Alibaba/Tencent updates.

**No additional canonical paper rows; total remains 930.** The December-facing release watch and deeper kernel-level investigations are out of scope for this company-blueprint closeout.
