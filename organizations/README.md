# Organizations

Source-linked maps of **first-party model families plus inference infrastructure**. Each model vendor page now contains an **official-model-family crosswalk checked on 2026-10-24**; it covers named releases and relevant modalities rather than only 1–2 selected flagships. This is **not** a byte-for-byte mirror of ever-changing API snapshot IDs, thousands of checkpoint quantizations, or other vendors' hosted models. Read the linked provider catalog when exact live endpoints matter.

[← Home](../README.md) · [Research labs & open source](../communities/README.md)

## China

| Organization | Public work |
|---|---|
| [DeepSeek](DeepSeek.md) | V4.1 causal encoder–decoder · DeepInfer · TileKernels / TileLang · MLA/DSA · DeepEP |
| [Tencent](Tencent.md) | Hy3 / Hy4-preview · Gated DSA / IndexCache · MoE / MTP |
| [Qwen (Alibaba)](Qwen-Alibaba.md) | Qwen3.5–3.8 · Gated DeltaNet / QSA · multimodal models · MNN |
| [Huawei / Ascend](Huawei.md) | CANN · MindIE · vLLM Ascend · third-party TileLang Ascend 950 backend |
| [StepFun](StepFun.md) | Step3 MFA + Attention–FFN Disaggregation |
| [MiniMax](MiniMax.md) | M3 / M3.1-Flash · sparse attention · QAT · DSpark |
| [Moonshot AI / Kimi](Moonshot-Kimi.md) | Mooncake · K3 / K3.1 Pro · KDA / Gated MLA · AttnRes |
| [Zhipu AI / GLM](Zhipu-GLM.md) | GLM-5.3 / 5.3-Flash · DSA · multimodal execution |
| [Xiaomi / MiMo](Xiaomi.md) | MiMo hybrid attention + MTP |
| [ByteDance / Seed](ByteDance.md) | Seed-OSS · ByteTransformer · ByteIR |
| [Baidu / Paddle](Baidu.md) | FastDeploy · PaddleNLP |

## United States

| Organization | Primary focus |
|---|---|
| [NVIDIA](NVIDIA.md) | TensorRT-LLM · Dynamo · NIXL · GPU kernels |
| [Google](Google.md) | JetStream · SAXML · MQA/GQA · speculative decoding |
| [Microsoft](Microsoft.md) | DeepSpeed · Splitwise · vAttention · ONNX Runtime |
| [AMD](AMD.md) | ROCm · AITER · kernel libraries |
| [OpenAI](OpenAI.md) | gpt-oss · Triton · token/runtime formats |
| [Anthropic](Anthropic.md) | Claude serving-visible API behavior; no inferred internals |
| [Meta](Meta.md) | Llama · xFormers · ExecuTorch · torchao |
| [AWS](AWS.md) | Neuron · DJL Serving · Bedrock |
| [Apple](Apple.md) | MLX · local/on-device inference |
| [Intel](Intel.md) | OpenVINO · GenAI inference |

## Recent first-party systems signals (2025–2026 cross-check)

[Eight research groups and their canonical-paper crosswalk](../communities/README.md#latest-group-originated-inference-signals-checked-2026-10-25) is maintained separately. The **company pages above remain authoritative for model families**. This short map highlights recent first-party *software/technical reports*; software projects do not have to be cloned into the 722-paper canonical bibliography. **TOPIC** = representative systems paper has a canonical row; **FOUNDATION** = homepage paper only; **ENGINEERING** = maintained implementation/model architecture rather than a distinct reviewed paper.

| Organization | Newer first-party systems / related release | Bibliography crosswalk and ownership limits |
|---|---|---|
| [DeepSeek](DeepSeek.md) | [DeepInfer](https://github.com/deepseek-ai/DeepInfer) (2026 offline V4.1-Flash runtime); [TileKernels](https://github.com/deepseek-ai/TileKernels), [DeepGEMM-Ascend](https://github.com/deepseek-ai/DeepGEMM-Ascend), DeepJIT, DeepEP and FlashMLA | **ENGINEERING** primary source. DeepInfer public release is **not a complete online Serving service**. [TileLang](https://github.com/tile-ai/tilelang) paper is **TOPIC** but is **not DeepSeek-owned**; DeepSeek adopts TileLang. Ascend 950/CANN9.2 does not imply 910B2/CANN9.1 reproducibility. |
| [NVIDIA](NVIDIA.md) | [Dynamo](https://github.com/ai-dynamo/dynamo), [NIXL](https://github.com/ai-dynamo/nixl), TensorRT-LLM; 2026 Fast Recovery and AIConfigurator studies; multimodal [EPD disaggregation](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/) | **TOPIC** Fast Recovery/Dynamo and AIConfigurator. Dynamo/NIXL/TRT-LLM **ENGINEERING**. EPD blog is a topology-specific product study; not automatically a new paper. |
| [Huawei / Ascend](Huawei.md) | CANN/Ascend C, MindIE, community [vLLM-Ascend](https://github.com/vllm-project/vllm-ascend); Ascend-native XY-Serve/ASAP/ENEC and CloudMatrix research | XY-Serve/ASAP/ENEC/CloudMatrix reports **TOPIC**; [AscendKernelGen](https://aclanthology.org/2026.findings-acl.1533/) is an independent laboratory **TOPIC**, not Huawei ownership. vLLM-Ascend is **community-maintained**, not exclusively first-party. |
| [Alibaba / Qwen](Qwen-Alibaba.md) | [RTP-LLM](https://arxiv.org/abs/2605.29639) production engine; Qwen3.5–3.8 Gated DeltaNet/QSA model family; MNN; first-party KV/sparse-indexer work | **TOPIC** RTP-LLM plus IndexCache/MISA and KV Prefetching (check each paper's actual authors); **ENGINEERING / model architecture** Qwen family and MNN. Don't equate Qwen release with an independently proved runtime speedup. |
| [Moonshot / Kimi](Moonshot-Kimi.md) | [Mooncake](https://github.com/kvcache-ai/Mooncake) KV transfer/storage; [FlashKDA](https://github.com/MoonshotAI/FlashKDA) recurrent kernel; Kimi-K3 KDA/AttnRes and K3.1 model generation | **FOUNDATION** Mooncake paper on homepage. **ENGINEERING / model architecture** FlashKDA, KDA and AttnRes; don't count API K3.1 high-speed tier as a new kernel paper. |
| [ByteDance / Seed](ByteDance.md) | Production LLM workload characterization; ByteTransformer / ByteIR compiler; Seed2.1 and multimodal model family | **TOPIC** cloud-native inference characterization. **ENGINEERING** ByteTransformer/ByteIR. Seed model-family news is workload context, not a Serving paper. |
| [Microsoft](Microsoft.md) | DeepSpeed-FastGen, MSCCL++, vAttention, Splitwise, Phi multimodal; DeepSpeed/ONNX ecosystem | **TOPIC** DeepSpeed-FastGen, MSCCL++; **FOUNDATION** Splitwise and vAttention; **ENGINEERING / model** other infrastructure and Phi, not automatically new canonical titles. |
| [Google](Google.md) | JetStream / SAXML TPU inference infrastructure, Gemini/Gemma family and deployment patterns | **ENGINEERING / model**; JetStream/SAXML need actual publication-identity and benchmark audit before canonical status; hosted model products are not publications. |
| [AMD](AMD.md) | [AITER](https://github.com/ROCm/aiter), ROCm, Composable Kernel; ROCm inference kernel releases | **ENGINEERING** kernel stack. The catalog includes an AMD Instinct deployment measurement study (**TOPIC**) but testing AMD hardware does not imply AMD authorship. |
| [Tencent](Tencent.md) | Hunyuan Hy3/Hy4 Gated DSA/MTP; sparse-indexer/IndexCache-related ecosystem | **ENGINEERING / model** Hunyuan lineage; attribution of third-party indexer patches must be paper- or repo-confirmed; model architecture is not itself a Serving system. |

**Selection rule:** research labs/companies are discovery sources; **canonical paper admission remains [G0–G5 evidence-first](../STRICT_REVIEW.md)**. Collaboration credit cannot be inferred from framework use or hardware used for tests.

## Official catalog reconciliation — 2026-10-24

The counts below use the **unit named in the source**: homepage featured model links, product families, or active endpoint IDs. They are deliberately **not combined** into a misleading global model count. Visit each page for all the first-party model names and their system-mechanism relevance.

| Provider | Official portfolio source | Coverage denominator / what was checked |
|---|---|---|
| DeepSeek | [Official news](https://www.deepseek.com/en/news/) · [API releases](https://api-docs.deepseek.com/updates/) | V2→V4.1 generational model/research lineage, special-purpose Vision/Reasoning versions and alias/retirement notes; DeepInfer and TileKernels separate |
| MiniMax | [Featured models](https://www.minimax.io/) · [developer plan](https://platform.minimax.io/subscribe/token-plan) | **5 current homepage featured families** (M3.1 Flash/M3/H3/Speech 2.8/Music 3.0); M2.5/M2.7 and legacy documented separately |
| Moonshot/Kimi | [Kimi Code exact models](https://www.kimi.com/code/docs/en/kimi-code/models) | **6 active endpoint IDs** mapped to **K3.1 Pro, K3, K2.8 Preview, K2.7 Code Highspeed**, plus older K2/Kimi Linear |
| Qwen/Alibaba | [Model Studio catalog](https://help.aliyun.com/zh/model-studio/web-search) · [Qwen code](https://github.com/QwenLM) | Qwen3.8/3.7/3.6/3.5/3/2.5, Coder/VL/Omni, hosted/snapshot and historical release distinction |
| Tencent | [Hunyuan portal](https://hunyuan.tencent.com/) · [model center](https://llm.hunyuan.tencent.com/) | Hy3/Hy4, translation, quantized small, vision, image/video/3D/ASR; TokenHub migration and retired historical endpoints |
| Z.ai/GLM | [Official GLM product model menu](https://autoclaw.z.ai/models/) | **6 named contemporary GLM releases** (5.3-Flash, 5.3, 5.2, 5-Turbo, 5V-Turbo, GLM-5) plus 4.x heritage |
| StepFun | [Official platform models](https://platform.stepfun.com/) | **8 current menu items** = Step 5 Preview, Step3.7/3.5 Flash and 5 StepAudio 3 functions, plus Step3 research |
| Xiaomi | [MiMo current API](https://mimo.mi.com/docs/en-US/quick-start/model) · [releases](https://mimo.mi.com/docs/en-US/updates/model) | V2.6 three live tiers; V2.5 retired text tiers, ASR/TTS family; prior V2-Flash architecture |
| ByteDance/Seed | [Official Seed portfolio](https://seed.bytedance.com/en/seed_model_portfolio) · [current models](https://seed.bytedance.com/en/models) | Seed 1.5→2.1, Diffusion Preview, Seedance/Seedream/Realtime/Audio, robotics/AI4Science adjacency |
| Baidu | [ERNIE model family](https://cloud.baidu.com/product/model.html) | ERNIE5.1/5.0/4.5, X1, PaddleOCR-VL and speech/media; third-party Qianfan hosted models excluded |
| Huawei | [Pangu official product family](https://www.huaweicloud.com/product/pangu) | **5 foundation categories** (LLM/vision/multimodal/prediction/weather), distinct from Ascend CANN/MindIE |
| NVIDIA | [Official NVIDIA models](https://build.nvidia.com/nvidia) | Nemotron 3/3.5 generations, Nano/Super/Ultra/Lightning/Bolt/Omni and retrieval/vision/safety branches; third-party hosted models excluded |
| Google | [Gemini API](https://ai.google.dev/gemini-api/docs/models) · [Gemma releases](https://ai.google.dev/gemma/docs/releases) | Gemini 4/3/2.5 multimodal, live/voice/image/music, Gemma 4 five sizes and specialized open Gemma |
| OpenAI | [First-party model catalog](https://developers.openai.com/api/docs/models/all) | GPT-6/5 families, gpt-oss, image, realtime/audio, embeddings and specialized; exact dated snapshot IDs remain in live registry |
| Anthropic | [Claude model catalog](https://platform.claude.com/docs/en/models/overview) | Fable / Opus / Sonnet / Haiku / limited Mythos, legacy variants, API capabilities vs unpublished kernels |
| Meta | [Official Llama family](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) | Llama4 Scout/Maverick and Llama3.x history; published runtimes tracked independently |
| Microsoft | [Phi family](https://azure.microsoft.com/en-us/products/phi) · [Phi-4 models](https://huggingface.co/collections/microsoft/phi-4) | Phi4 dense/reasoning/mini/multimodal; Phi3.5/3/2/1 history; Azure-hosted third-party models excluded |
| AWS | [Nova models](https://aws.amazon.com/nova/models/) · [Bedrock model catalog](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) | Nova2, Nova1, Titan owned models; other Bedrock hosted vendors excluded |
| Apple | [AFM 3 first-party research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) | **5 named AFM3 models** (two on-device, three cloud), plus MLX execution software |
| AMD / Intel | [AMD AITER](https://github.com/ROCm/aiter) · [Intel OpenVINO](https://github.com/openvinotoolkit/openvino) | In this collection these two are **hardware/software ecosystem** pages, not proprietary frontier-model portfolio owners; do not invent model releases to fill rows |

**Strict reading rule:** owning an API model is not owning its inference framework; owning a kernel repo is not proof of production adoption. A product/model-family entry is **not** a new canonical paper and does not affect the current 756-paper technical catalog. New model generations must be cross-checked against the official model menu *and* the release/retirement log. A provider's total downloadable checkpoint count is not feasible to freeze as a manually maintained Markdown list; the authoritative site is linked instead.

**Editorial boundary.** Organization pages represent verifiable first-party releases or research directly attributable to a team. Coauthored work belongs in the topical paper lists unless the institution is explicitly presenting its own system. An API feature is not proof of an undisclosed serving implementation.
