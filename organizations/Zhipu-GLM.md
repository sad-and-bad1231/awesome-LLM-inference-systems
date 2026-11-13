# Zhipu AI / Z.ai / GLM

**Tsinghua GLM research lineage → open foundation models → multimodal creation and computer-use agents → RL/rollout systems → domestically optimized inference and developer products.** Zhipu should be understood as a model-and-systems company with strong research roots, rather than only the current GLM-5.x API list.

[← Organizations](README.md) · [← Home](../README.md) · [2026-11-13 source audit](../reviews/KIMI_ZHIPU_PRIMARY_SOURCE_AUDIT_20261113.md)

## 1. The technology map

| Layer | Main work | Why it matters |
|---|---|---|
| **Foundation and academic lineage** | [GLM](https://github.com/THUDM/GLM) · [GLM-130B](https://github.com/zai-org/GLM-130B) · [ChatGLM](https://github.com/zai-org/ChatGLM3) · [GLM-4](https://github.com/zai-org/GLM-4) · [GLM-4.5](https://github.com/zai-org/GLM-4.5) | General Language Model (GLM) pretraining roots, Chinese open-model ecosystem and transition toward MoE + agentic foundation models. |
| **Latest GLM language/multimodal** | [GLM-5](https://github.com/zai-org/GLM-5) · [GLM-5.2](https://z.ai/blog/glm-5.2) · [GLM-5.3](https://z.ai/blog/glm-5.3) · [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) | Long-context DSA/IndexShare, model/post-training efficiency and a separately designed sparse+linear-attention multimodal Flash model. |
| **Vision and generative media** | [CogVLM / GLM-V](https://github.com/zai-org/GLM-V) · [CogVideoX](https://github.com/zai-org/CogVideo) · [CogView4](https://github.com/zai-org/CogView4) · [GLM-Image](https://github.com/zai-org/GLM-Image) | Image/video understanding, image generation/editing and video synthesis beyond text LLM serving. |
| **Speech, documents and edge** | [GLM-ASR](https://github.com/zai-org/GLM-ASR) · [GLM-TTS](https://github.com/zai-org/GLM-TTS) · [GLM-OCR](https://github.com/zai-org/GLM-OCR) · [GLM-Edge](https://github.com/zai-org/GLM-Edge) | ASR, speech generation, OCR/document extraction and deployment on smaller devices. |
| **Agents / code / device control** | [AutoGLM / Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) · [ZCode](https://github.com/zai-org/ZCode) · [CodeGeeX](https://github.com/zai-org/CodeGeeX) · [GLM Coding Plan](https://docs.z.ai/devpack/overview) | Computer/phone-control agents, coding assistant/runtime, developer models and paid API/service channels. |
| **Post-training and RL** | [slime](https://github.com/THUDM/slime) · [GLM-5.2 SAO/OPD](https://z.ai/blog/glm-5.2) · long-horizon task-environment generation in [GLM-5.3](https://z.ai/blog/glm-5.3) | Scalable asynchronous RL with Megatron training and inference rollout, plus agentic environments and verifier-based rewards. |
| **Attention & KV execution** | [IndexCache](https://github.com/THUDM/IndexCache) · [IndexShare](https://z.ai/blog/glm-5.2) · [GLM-5.3-Flash IndexPool](https://z.ai/blog/glm-5.3-flash) | Cross-layer sparse index reuse and hybrid recurrent/sparse-state handling. These are **distinct** mechanisms, not renamed identical algorithms. |
| **Native inference infrastructure** | [GLM-5.3-Flash Chinese accelerator serving](https://z.ai/blog/glm-built-its-inference-infrastructure) · [SGLang](https://github.com/sgl-project/sglang) · [GLM Infra Agent](https://z.ai/blog/glm-5.3-flash) | Vendor-reported custom SGLang-based serving, multimodal E/P/D disaggregation, mixed-precision caches and agent-assisted kernel/system optimization. |
| **Developer and enterprise platform** | [Z.ai](https://z.ai/) · [BigModel](https://bigmodel.cn/) · [ZCode](https://zcode.z.ai/) · [AutoClaw](https://autoclaw.z.ai/) | Model/API access, coding workflows, agent platforms and application distribution; products do not prove unpublished engine implementation. |

**Fast orientation:** GLM is not limited to the 5.x leaderboard. The public research arc connects **THUDM/GLM → ChatGLM → Cog-series multimodality → agentic GLM-5.x → slime/IndexCache → dedicated native inference**. The low-level inference work is **particularly relevant on Chinese accelerators**, but public articles and source code have different evidential weight.

## 2. Foundation models — architecture and chronology

| Family / current release | Development contribution | Source |
|---|---|---|
| **GLM → GLM-130B → ChatGLM → GLM-4** | General Language Model pretraining and early widely used Chinese/English conversational model research; some repositories originate from **Tsinghua THUDM**, not independently owned commercial product code. | [GLM](https://github.com/THUDM/GLM) · [GLM-130B](https://github.com/zai-org/GLM-130B) · [ChatGLM3](https://github.com/zai-org/ChatGLM3) · [GLM-4](https://github.com/zai-org/GLM-4) |
| **GLM-4.5 → GLM-5** | Open MoE, reasoning/coding and sparse-attention model lineage. | [GLM-4.5](https://github.com/zai-org/GLM-4.5) · [GLM-5](https://github.com/zai-org/GLM-5) |
| **GLM-5.2** | 1M-context model with **IndexShare** (indexer reuse every four sparse-attention layers), improved MTP/speculative decoding, SAO and scalable post-training. | [Official technical report](https://z.ai/blog/glm-5.2) · [IndexCache](https://github.com/THUDM/IndexCache) |
| **GLM-5.3** | **Same base model as 5.2**, with substantially scaled post-training and long-horizon coding/agent environments; not an independently invented sparse-attention architecture. | [Official release](https://z.ai/blog/glm-5.3) · [model card](https://huggingface.co/zai-org/GLM-5.3) |
| **GLM-5.3-Flash** | **Separate newly trained native multimodal base model**: 320B total / 18B active, hybrid sparse + linear attention, **IndexPool**, mHC and a cost-oriented design. Distinct from the GLM-5.3 post-training release. | [Official technical post](https://z.ai/blog/glm-5.3-flash) · [model card](https://huggingface.co/zai-org/GLM-5.3-Flash) |
| **GLM-5-Turbo / GLM-5V-Turbo** | Agent-oriented and visual UI/API variants; not necessarily new kernel/compiler inventions. | [Official model selection](https://autoclaw.z.ai/models/) |

**Technical boundary:** [GLM-5.2 IndexShare](https://z.ai/blog/glm-5.2) reuses one sparse indexer across layers; [IndexCache](https://github.com/THUDM/IndexCache) separately provides cross-layer index reuse implementation/patches; [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) combines linear and sparse attention with **IndexPool**, and is **not** the GLM-5.2 base. Do not transfer details between these model families.

## 3. Multimodal models and autonomous agents

| Research or product line | What it demonstrates | Official entry |
|---|---|---|
| **CogVLM / GLM-V / CogAgent** | Vision-language understanding, grounding and multimodal reasoning as a long-running research line. | [GLM-V](https://github.com/zai-org/GLM-V) · [CogAgent](https://github.com/zai-org/CogAgent) |
| **CogVideo / CogVideoX, CogView / GLM-Image** | Video/image generation and editing; [GLM-Image](https://github.com/zai-org/GLM-Image) combines autoregressive semantic generation with a diffusion decoder, distinct from token-by-token chat serving. | [CogVideo](https://github.com/zai-org/CogVideo) · [CogView4](https://github.com/zai-org/CogView4) · [GLM-Image](https://github.com/zai-org/GLM-Image) |
| **GLM-ASR / TTS / OCR / Edge** | Speech recognition and speech generation, OCR/document processing, and smaller-device deployment. | [ASR](https://github.com/zai-org/GLM-ASR) · [TTS](https://github.com/zai-org/GLM-TTS) · [OCR](https://github.com/zai-org/GLM-OCR) · [Edge](https://github.com/zai-org/GLM-Edge) |
| **AutoGLM / Open-AutoGLM** | Phone/computer-use agent using visual perception and tool/ADB actions; published repository gives an inspectable agent implementation. | [Official code](https://github.com/zai-org/Open-AutoGLM) |
| **ZCode / CodeGeeX** | Coding agents and IDE/CLI tools; [ZCode](https://github.com/zai-org/ZCode) publicly contains desktop/web/CLI runtime, while CodeGeeX is a longer-running coding-model ecosystem. | [ZCode](https://github.com/zai-org/ZCode) · [CodeGeeX](https://github.com/zai-org/CodeGeeX) |

**Scope:** these establish a *model, research and application* ecosystem. They are not evidence that CogVideo uses the same inference scheduler as GLM-5.3, or that every paid API tier has a separate architecture.

## 4. Training/rollout and native inference infrastructure

| Source | Contribution | Attribution / limits |
|---|---|---|
| **[slime](https://github.com/THUDM/slime)** | RL/post-training framework linking Megatron training and SGLang inference rollout with asynchronous orchestration; used in [GLM-5.2](https://z.ai/blog/glm-5.2) post-training. | Project lives in the **THUDM** research ecosystem; it is *not* a standalone production online serving engine. |
| **[IndexCache](https://github.com/THUDM/IndexCache)** | Tsinghua + Z.ai cross-layer sparse-attention index-reuse work with SGLang/vLLM patches. | A narrower open implementation than GLM's complete production inference architecture; source results are not locally reproduced. |
| **[GLM-5.3-Flash dedicated inference](https://z.ai/blog/glm-5.3-flash)** | Built **on SGLang** for Chinese AI accelerators; linear-attention TP, ReplaySSM, W8A8, mixed INT8/FP8/BF16 cache precision and Layer Split; **Encode–Prefill–Decode (EPD)** disaggregation into separate worker pools. | Public description is a first-party *engineering report*, not a completely open production engine or a verified 910B2/CANN 9.1 port. |
| **[GLM Infra Agent](https://z.ai/blog/glm-built-its-inference-infrastructure)** | Model-assisted kernel writing, bottleneck discovery and configuration iteration as part of the GLM-5.3-Flash deployment effort. | Interesting **inference-engine self-optimization (RSI-adjacent)** signal; not proof of an autonomous, recursively self-improving general AI or a released reproducible kernel-agent system. |
| **[GLM-5.3 RL environment work](https://z.ai/blog/glm-5.3)** | Scaled executable environments and verifier/reward construction for coding and long-horizon agents. | Post-training research, distinct from inference server scheduling and request routing. |

**Numerical claim handling:** Z.ai reports roughly **3× end-to-end serving improvement versus its initial baseline on the same hardware** after the GLM-5.3-Flash kernel/runtime work. The comparison is **vendor-reported**, without an independently reproduced setup here. It must not be compared directly to NVIDIA/Ascend metrics or cited as a general SGLang speedup. [Infrastructure retrospective](https://z.ai/blog/glm-built-its-inference-infrastructure).

## 5. Product and organizational context

- **[Z.ai](https://z.ai/) / [BigModel](https://bigmodel.cn/)**: model access, API services and developer subscriptions; API aliases and service costs should be read from the current official catalog.
- **[ZCode](https://github.com/zai-org/ZCode) / [GLM Coding Plan](https://docs.z.ai/devpack/overview)**: coding-agent workspace, CLI/desktop/web and third-party editor access. Agent workflow optimizations belong to the product/harness layer.
- **[AutoGLM](https://github.com/zai-org/Open-AutoGLM) / [AutoClaw](https://autoclaw.z.ai/)**: phone/computer-use and agent automation surfaces. They connect GLM visual understanding with GUI interaction and tool execution.
- **Research lineage:** Tsinghua THUDM is a major antecedent and collaborative research ecosystem; **THUDM open-source ownership should not automatically be rewritten as sole Zhipu corporate ownership**. Professor **Tang Jie (唐杰)** later co-founded Zhipu and previously mentored Kimi founder Yang Zhilin as an undergraduate researcher. [Tsinghua event](https://www.tsinghua.edu.cn/info/1181/51205.htm) · [contemporary transcript](https://tech.ifeng.com/c/8v1ZLaTFGkU).

## 6. Suggested reading order and source discipline

[Academic GLM](https://github.com/THUDM/GLM) → [GLM-5.2](https://z.ai/blog/glm-5.2) / [GLM-5.3](https://z.ai/blog/glm-5.3) versus [5.3-Flash](https://z.ai/blog/glm-5.3-flash) → [Cog/GLM multimodal](https://github.com/zai-org/GLM-Image) → [AutoGLM](https://github.com/zai-org/Open-AutoGLM) / [ZCode](https://github.com/zai-org/ZCode) → [slime](https://github.com/THUDM/slime), [IndexCache](https://github.com/THUDM/IndexCache) and [SGLang-based infrastructure story](https://z.ai/blog/glm-built-its-inference-infrastructure).

**Evidence boundary (2026-11-13):** Technical posts, released code, THUDM co-developed artifacts, hosted API products and vendor performance reports have separate evidential status. Do not claim public full-production source or an experimentally verified Ascend 910B2 path. This overview adds **no new canonical topic papers**.
