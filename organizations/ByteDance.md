# ByteDance / Seed / Volcano Engine

**A full-scale AI ecosystem connecting foundation-model research, media creation, large consumer products, distributed AI infrastructure and commercial cloud serving.** A practical map is **Seed research → Doubao/creative/agent products → Volcano Engine/BytePlus → AI Infra**, while keeping first-party model research separate from cloud-product capabilities and open-source kernel projects.

[← Organizations](README.md) · [← Home](../README.md) · [2026-11-13 primary-source audit](../reviews/MINIMAX_BYTEDANCE_PRIMARY_SOURCE_AUDIT_20261113.md)

## 1. The technology map

| Layer | Main work | Why it matters |
|---|---|---|
| **Foundation models** | [Seed2.1](https://seed.bytedance.com/en/models) · [Seed2.0](https://seed.bytedance.com/en/seed2) · Seed1.8/1.6/1.5-VL · [Seed-OSS](https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct) | General reasoning/coding/agents and multimodal understanding, with both hosted and selected open-weight research artifacts. |
| **Generative media** | [Seedance 2.5](https://seed.bytedance.com/en/models) · [Seedream 5.5](https://seed.bytedance.com/en/seedream5_5) · [Seed Audio 1.0](https://seed.bytedance.com/en/models) | Video, image and voice/sound creation, connected to creator applications and multimodal API workloads. |
| **Omni / real-time interaction** | [SeedRealtime](https://seed.bytedance.com/en/seedrealtime) | Native full-duplex audio/video/text interaction; a different real-time execution profile from text chat and offline video generation. |
| **Frontier / agent research** | [Seed Diffusion Preview](https://seed.bytedance.com/en/seed_model_portfolio) · [Recycler / KV research](https://seed.bytedance.com/en/public_papers) · [HarnessDev / S³Gym / Aspire / Chain-of-Experience](https://seed.bytedance.com/en/public_papers) · [EdgeBench](https://seed.bytedance.com/en/research) | Alternative language decoding, reasoning-state reuse, agent-harness evolution, self-improvement and environment learning; research directions, not necessarily deployed serving products. |
| **Robotics / science / 3D** | [Seed GR-3 / GR-RL](https://seed.bytedance.com/en/models) · [Seed3D 2.0](https://seed.bytedance.com/en/research) · [Protenix](https://seed.bytedance.com/en/models) | Embodied intelligence, geometry/spatial synthesis and biomolecular models broaden Seed beyond ordinary LLMs. |
| **Training and model systems** | [MegaScale-Omni](https://seed.bytedance.com/en/research) · [VeOmni](https://github.com/ByteDance-Seed/VeOmni) · [Charon](https://arxiv.org/abs/2605.17164) | Multimodal training, distributed engineering and training/inference simulation; not equivalent to publishing a full online serving engine. |
| **Compiler / kernels / distributed communication** | [Triton-distributed](https://github.com/ByteDance-Seed/Triton-distributed) · [FLUX/COMET](https://github.com/bytedance/flux) · [ByteIR](https://github.com/bytedance/byteir) · [ByteTransformer](https://github.com/bytedance/ByteTransformer) | A particularly visible ByteDance strength: compute/communication overlap, MoE parallelism, compiler infrastructure and historical optimized Transformer inference. |
| **Commercial inference & cloud** | [Volcano Ark](https://docs.volcengine.com/docs/ark/model-list?lang=zh) · [ServingKit](https://docs.volcengine.com/docs/vke/servingkit-overview?lang=en) · [BytePlus](https://www.bytedance.com/products-services) | Model access, inference deployment, cluster operations, cache/orchestration and enterprise AI services. |
| **AI products and distribution** | [Doubao / Doubao Work / Dola](https://www.bytedance.com/products-services) · Jimeng / Dreamina · Jianying / CapCut · Feishu / Lark · PICO · Douyin / TikTok | Consumer and enterprise assistants, work agents, media creation, collaboration, XR and global distribution; product surfaces are not proof that every service runs the same Seed model. |

**Fast orientation:** ByteDance is not just a chatbot model vendor or a video-model lab. Its public footprint combines **foundation models + real-time/creative multimodal systems + communication/compiler work + a large-scale cloud serving product suite**. The connection among these layers is an organizational/engineering map; it is **not** evidence that one open-source engine powers every product.

## 2. Seed model portfolio — major lines

[Seed's official portfolio](https://seed.bytedance.com/en/seed_model_portfolio) is the best source for historical release names; [current highlighted models](https://seed.bytedance.com/en/models) and [Volcano Ark API listing](https://docs.volcengine.com/docs/ark/model-list?lang=zh) serve different purposes.

| Family | Development lineage / representative work | Official source |
|---|---|---|
| **General foundation** | Seed1.5 / 1.5-VL → Seed1.6 / 1.8 → **Seed2.0 Pro/Lite/Mini** → **Seed2.1 Pro/Turbo**, for general reasoning, code, agents and multimodal understanding. | [Portfolio](https://seed.bytedance.com/en/seed_model_portfolio) · [Seed2.0 card](https://seed.bytedance.com/en/seed2) · [Seed2.1 model page](https://seed.bytedance.com/en/models) |
| **Video generation** | Seedance 2.0 → **Seedance 2.5** with longer-form reference-conditioned generation and editing. | [Official announcement](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) |
| **Image generation** | Seedream 5.0 Pro → **Seedream 5.5 (Nov 9)** for image creation, editing precision and consistency. | [Release](https://seed.bytedance.com/en/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5) |
| **Speech/audio & live interaction** | **Seed Audio 1.0** creates audio content; **SeedRealtime** handles simultaneous hearing/seeing/speaking in full-duplex interaction. | [Seed Audio](https://seed.bytedance.com/en/research) · [SeedRealtime](https://seed.bytedance.com/en/seedrealtime) |
| **Alternative decoding / open research** | **Seed Diffusion Preview** is experimental diffusion-language modeling; **Seed-OSS-36B** is a separately released foundation-model research artifact. | [Portfolio](https://seed.bytedance.com/en/seed_model_portfolio) · [weights](https://huggingface.co/ByteDance-Seed/Seed-OSS-36B-Instruct) |
| **Robotics, spatial and science** | **Seed GR-3**, GR-RL, Seed3D, Depth Anything and Protenix extend Seed to action, perception and biomolecular tasks. | [Models](https://seed.bytedance.com/en/models) · [Research](https://seed.bytedance.com/en/research) |

**The central multimodal distinction:** Seed2.x handles understanding, agents and some multimodal input; Seedance/Seedream/Audio produce media; SeedRealtime targets continuous interaction. Each creates a distinct inference or dataflow contract, and should not be collapsed into a single LLM capability ranking.

## 3. First-party systems and research — what deserves an entry

| Workstream | Representative work | What a systems reader should know |
|---|---|---|
| **Parallelism and compute/communication** | [Triton-distributed](https://github.com/ByteDance-Seed/Triton-distributed) · [FLUX/COMET](https://github.com/bytedance/flux) · [TileLink](https://arxiv.org/abs/2503.20313) | ByteDance publishes programmable/fused communication–compute research relevant to MoE and distributed execution. FLUX/COMET's major published use includes **training**; hardware/backend support is version-dependent. |
| **Compiler and inference operators** | [ByteIR](https://github.com/bytedance/byteir) · [ByteTransformer](https://github.com/bytedance/ByteTransformer) | MLIR-based compiler infrastructure and the historical variable-length **BERT encoder** inference library; neither is by itself a current vLLM-style decoder scheduler. |
| **Training, simulation and production methodology** | [MegaScale-Omni](https://seed.bytedance.com/en/research) · [VeOmni](https://github.com/ByteDance-Seed/VeOmni) · [Charon](https://arxiv.org/abs/2605.17164) | Distributed multimodal training infrastructure and simulation for inference/training system design. Simulation claims must remain separate from measured Serving results. |
| **Networking / storage-adjacent systems** | [ByteExpress](https://arxiv.org/abs/2610.12815) | Production RDMA transport lessons; the published deployment concerns parameter-server recommendation/search inference, **not** a documented LLM KV-transfer implementation. |
| **Model efficiency and frontier mechanisms** | [UltraMem](https://arxiv.org/abs/2411.12364) · [Seed Diffusion Preview](https://seed.bytedance.com/en/seed_model_portfolio) · [Seed selected publications](https://seed.bytedance.com/en/research) | Sparse memory architectures, alternative decoding and state reuse offer distinct research threads without proving deployment in Doubao/Seed2.1. |
| **Agent harnesses / self-improvement** | [HarnessDev](https://seed.bytedance.com/en/public_papers) · [S³Gym / Aspire / Chain-of-Experience](https://seed.bytedance.com/en/public_papers) · [EdgeBench](https://seed.bytedance.com/en/research) | Evaluation and learning for agents that construct/evolve harnesses, self-test/self-judge or learn from experience; **not** verified recursive optimization of an inference engine. |
| **Research beyond LLM serving** | [Seed GR-RL](https://seed.bytedance.com/en/models) · [Seed3D 2.0](https://seed.bytedance.com/en/research) · [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3) | Embodied and world/spatial modeling, vision foundations and AI4Science: part of Seed's AI picture, but not canonical LLM-serving papers by default. |

**Ascend-related note:** [Triton-distributed](https://github.com/ByteDance-Seed/Triton-distributed) documents historical Ascend/RDMA support in the **Triton v3.4** line; its **v3.7 main** does **not** have the Ascend plugin build integrated. Do not infer CANN 9.1 / Ascend 910B2 compatibility.

## 4. Serving and AI products — ecosystem map, not undocumented internals

| Surface | Product / platform | Scope |
|---|---|---|
| **Developer and enterprise AI** | [Volcano Engine / Ark](https://docs.volcengine.com/docs/ark/model-list?lang=zh) · [ServingKit](https://docs.volcengine.com/docs/vke/servingkit-overview?lang=en) · [BytePlus](https://www.bytedance.com/products-services) | Model APIs and managed deployment. ServingKit documents orchestration, gateway, observability, distributed caching, P/D separation and integrations with vLLM/SGLang/Dynamo. |
| **Chat and work agents** | [Doubao / Doubao Work / Dola](https://www.bytedance.com/products-services) · [Feishu / Lark](https://www.bytedance.com/products-services) | China/global consumer assistants, multi-step work-agent tasks and enterprise collaboration. |
| **Creative and multimodal applications** | [Jimeng AI / Dreamina](https://www.bytedance.com/products-services) · [Jianying / CapCut](https://www.bytedance.com/products-services) | Image/video generation, editing and creative media workflows, a major consumer deployment domain. |
| **Broader product distribution** | [Douyin / TikTok / PICO](https://www.bytedance.com/products-services) and other ByteDance content platforms | Global content/discovery and XR provide distribution and multimodal demand; **not** proof of Seed-model ownership or inference-kernel reuse in every product. |

**Do not conflate** a Seed research model, Volcano Ark's API model ID, ServingKit's deployed container engine, and the proprietary runtime used by Doubao. Public offerings reveal workloads and interfaces; internal model placement, scheduling or kernel details require separate evidence.

## 5. Reading order

[Seed model families](https://seed.bytedance.com/en/models) → [Seed research/publications](https://seed.bytedance.com/en/research) → [ByteDance product map](https://www.bytedance.com/products-services) → [Volcano ServingKit](https://docs.volcengine.com/docs/vke/servingkit-overview?lang=en) → [Triton-distributed](https://github.com/ByteDance-Seed/Triton-distributed) / [FLUX](https://github.com/bytedance/flux).

This is a **company technology blueprint**, not a kernel tutorial or a ranking by model quality. Models, systems papers, source implementations, cloud service contracts and product adoption remain distinct evidence categories. **No new canonical topic papers** or independently reproduced speedups are asserted in this revision.
