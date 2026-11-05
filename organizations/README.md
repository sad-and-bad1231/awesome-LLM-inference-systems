# Organizations

Source-linked maps of **first-party model families plus inference infrastructure**. Model-family crosswalks were first checked on **2026-10-24** and selectively updated through **2026-11-04**; it covers named releases and relevant modalities rather than only 1–2 selected flagships. This is **not** a byte-for-byte mirror of ever-changing API snapshot IDs, thousands of checkpoint quantizations, or other vendors' hosted models. Read the linked provider catalog when exact live endpoints matter.

[← Home](../README.md) · [Research labs & open source](../communities/README.md)

## China

| Organization | Public work |
|---|---|
| [DeepSeek](DeepSeek.md) | V4.1-Flash-1017 revision · asymmetric causal encoder–decoder · DeepInfer · TileKernels / TileLang · DeepEP |
| [Tencent](Tencent.md) | **Hy4 final (Nov 4)** vs Hy4-preview artifacts · Gated DSA / IndexCache · MoE / MTP |
| [Qwen (Alibaba)](Qwen-Alibaba.md) | Qwen3.5–3.8 · Gated DeltaNet / QSA · multimodal models · MNN |
| [Huawei / Ascend](Huawei.md) | CANN · MindIE · vLLM Ascend · third-party TileLang Ascend 950 backend |
| [StepFun](StepFun.md) | **Step 5 Preview open weights** · Gated SWA / Sparse GQA · Step3 MFA + Attention–FFN Disaggregation |
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
| [Google](Google.md) | **TorchTPU-native vLLM/SGLang** · Ragged Paged Attention · JetStream · AlphaEvolve (RSI-adjacent) |
| [Microsoft](Microsoft.md) | DeepSpeed · Splitwise · vAttention · ONNX Runtime |
| [AMD](AMD.md) | ROCm · AITER · kernel libraries |
| [OpenAI](OpenAI.md) | gpt-oss · Triton · token/runtime formats |
| [Anthropic](Anthropic.md) | Claude serving-visible API behavior; no inferred internals |
| [Meta](Meta.md) | Llama · xFormers · ExecuTorch · torchao |
| [AWS](AWS.md) | Neuron · DJL Serving · Bedrock |
| [Apple](Apple.md) | MLX · local/on-device inference |
| [Intel](Intel.md) | OpenVINO · GenAI inference |
| [Together AI](Together-AI.md) | **Together Compiler** · persistent-engine agent optimization · polymorphic serving |
| [Asari AI](Asari-AI.md) | **Whole-stack agent optimization** · vLLM profiling/verification/experience reuse |
| [Cerebras](Cerebras.md) | **CS-4 / Nexus** · wafer-scale inference and rack-scale co-design |
| [Modal](Modal.md) | **FlashAttention-4 decode optimization** · SGLang speculative inference · deployment |
| [Fireworks AI](Fireworks-AI.md) | **Disaggregated inference engine** · KV routing · multi-node EP · FireOptimizer |
| [Groq](Groq.md) | **LPU / deterministic dataflow** · on-chip SRAM · latency-oriented hardware/runtime |

## November 4 update — model revisions and US inference-system sources

**Release identity first.** The links below are primary sources, not extra canonical paper rows. First-party speedups remain author-reported.

| Organization / source | Auditable new signal | Scope boundary |
|---|---|---|
| [StepFun Step 5 Preview](https://platform.stepfun.com/blog/inside-step-5-preview) · [released weights](https://huggingface.co/collections/stepfun-ai/step-5-preview) | 92-layer sparse MoE, Gated SWA and Sparse GQA; model weight variants are public. | The published model is still named **Preview**; architecture ≠ full-engine speedup. |
| [DeepSeek-V4.1-Flash-1017](https://api-docs.deepseek.com/news/news261017/) · [weights](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | Oct 17 revised weights and API alias for V4.1 Flash. | **Not** a distinct model architecture or new inference engine. |
| [Tencent Hy4 final](https://cloud.tencent.com/document/product/1823/132252) · [release](https://adp.tencent.com/zh/blog/tencent-cloud-adp-hunyuan-hy4-release) | Nov 4 formal Hy4 vision/agent/computer-use model available through API. | **Final weights/system card not yet publicly verified**; do not substitute [Hy4-preview](https://github.com/Tencent-Hunyuan/Hy4-preview) checkpoint. |
| [Google TorchTPU](https://developers.googleblog.com/en/announcing-new-vllm-and-sglang-inference-engines-on-tpu/) · [Ragged Paged Attention](https://research.google/pubs/ragged-paged-attention-a-high-performance-and-flexible-llm-inference-kernel-for-tpu/) | Native PyTorch TPU serving and ragged attention primitives, in cooperation with Inferact/RadixArk. | TPU-specific performance, not generic CUDA/Ascend acceleration. |
| [Google DeepMind AlphaEvolve](https://deepmind.google/blog/alphaevolve-impact/) · [Cloud rollout](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-on-cloud/) | Evaluator-guided algorithm evolution, with reported TPU design/cache-policy contributions. | **RSI-adjacent algorithm optimization**, not proof of recursive Gemini/model-weight improvement or evolving serving engine. |
| [Together Compiler](https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference) · [Asari AI](https://asari.ai/blog/inference-optimization) | Multi-iteration, profile-guided or persistent-engine agent optimization of inference stacks. | Company reports only; distinguish faster *experiment throughput* from actual token throughput and optimizer self-improvement. |
| [Cerebras](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026) · [Groq](https://groq.com/blog/the-groq-lpu-explained) | Wafer-scale / SRAM-centric deterministic execution are alternative inference hardware contracts. | Hardware product claims are not universal serving Goodput or energy-cost comparisons. |
| [Modal](https://modal.com/blog/flash-attention-4-faster) · [Fireworks](https://fireworks.ai/platform/disaggregated-inference-engine) | Decode-oriented kernel improvements and production disaggregated P/D, distributed KV, cache-aware routing. | Engineering and product evidence; single-kernel gains and marketing speedups are not interchangeable with audited E2E results. |

**US coverage rule:** infrastructure companies are added for identifiable inference mechanism or publicly inspectable engineering, not merely for operating a hosted model API. [Together AI](Together-AI.md), [Asari AI](Asari-AI.md), [Cerebras](Cerebras.md), [Modal](Modal.md), [Fireworks AI](Fireworks-AI.md) and [Groq](Groq.md) now have focused first-party pages. The related [engine-evolution Frontier](../frontiers/README.md#autonomous-inference-engine-evolution-separate-engine-evolution-from-rsi) keeps strict RSI claims evidence-gated.
## October 31 follow-up: additional first-party engine/kernel signals

These were missed in the original October 31 industrial pass. **Repositories, implementation blog posts and live backend support are not extra canonical paper entries.** Always pin commits, models, hardware and runtime paths before asserting measured speedups.

| Official source | Executed mechanism / deployment signal | Scope and evidence caveat |
|---|---|---|
| **Ant Group × vLLM Community: [Humming quantized kernel library](https://vllm.ai/blog/2026-10-21-humming)** · [source](https://github.com/vllm-project/humming) · Oct 21 | A unified typed quantization representation with JIT dense/MoE kernels, hardware+shape-specialized pipeline/compute/tile selection and BF16/FP8/FP4/int formats. Upstream vLLM 0.29.0+ CUDA lane includes an integrated backend. | First-party **8×H20 TP8 DeepSeek-V4.1-Flash** W4A8 vs Marlin W4A16 with the same MXFP4 weights but **different activation precision**: author reports +14–43% E2E output throughput across concurrency 1–64 and reduced TTFT. **Not a precision-identical Kernel A/B**; no Ascend native support demonstrated. |
| **Google TorchTPU / vLLM / SGLang** · [Oct 20 launch](https://developers.googleblog.com/en/announcing-new-vllm-and-sglang-inference-engines-on-tpu/) · [vLLM TorchTPU design](https://vllm.ai/blog/2026-10-20-vllm-torchtpu) | New **native PyTorch `tpu` device** with XLA/`torch.compile` and `torch.distributed`, TPU-oriented vLLM/SGLang serving integrated with Pallas optimized kernels. | Real upstream/backend support; **not** proof ordinary CUDA/Ascend plugins inherit performance or can use their kernels. TPU-availability and model coverage vary by branch and release. Collaboration credits: Google + Inferact (vLLM), Google + RadixArk (SGLang). |
| **vLLM Wide-EP / P-D industrial field report** · [DeepSeek-V4.1 Flash on GB300 NVL72](https://vllm.ai/blog/2026-10-23-deepseek-v41-flash-pd-wide-ep) · Oct 23 | P/D disaggregation and Wide Expert Parallelism integrate high-bandwidth rack-scale link fabric, expert scheduling and GPU serving of DeepSeek-V4.1 Flash. | First-party benchmark **model/hardware/AgentX/SLO-dependent**: quoted throughput and 7.9× are relative to stated aggregated single-node configuration, **not** cross-product DeepInfer superiority or an Ascend 910B2 TP4 result. |
| **vLLM model-specific day-0 deployment** · [Mistral Large 4](https://vllm.ai/blog/2026-10-29-mistral-large-4) · Oct 29 | Sparse MLA, cross-layer KV sharing, DSpark verifier, context-parallel prefill and NIXL P/D transport; a practical software signal for hybrid attention + KV lifecycle mapping. | **Engine integration report**, not an independent research-paper identity or universal speedup. Cross-layer cache ownership, model correctness and backend-specific support remain mandatory validation tasks. |

**October source-level synthesis:** Quantized Kernel Formats/Task Mapping (**Humming**), heterogeneous PyTorch backend contracts (**TorchTPU**), rack-wide Expert Parallelism + staged scheduling (**vLLM Wide-EP**) and new cross-layer attention/KV semantics (**Mistral Large 4**) are all implementation-level advances worth reading, without inventing new canonical research publications. [October 31 second-pass evidence ledger](../reviews/OCTOBER_2026_FOLLOWUP_SWEEP_20261031.md).

## October 2026 engineering releases — source/implementation, not new paper rows

The following are **official repositories, release notes and technical reports**, cross-checked at the **2026-10-31** monthly close. An upstream version, packaged vendor image and NPU plugin release are different build baselines. These changes add **zero** papers to the eight canonical topic tables; publisher articles and experimental results receive independent G0–G5 scrutiny.

| Source and dated release | Concrete deployed/released mechanism | Evidence boundary / engineering implication |
|---|---|---|
| **DeepSeek** · [DeepInfer open-source release](https://github.com/deepseek-ai/DeepInfer) · Oct 2026 · [production deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) | Public **offline** DeepSeek-V4.1-Flash engine: FlashMLA/DeepGEMM/DeepEP/TileKernels, DSpark + confidence-aware verification, asynchronous batching, deterministic sampling and Batch Invariance option. First-party production **architecture** separately describes E/P/D disaggregation and Wide-EP Decode (EP64–128). | The public offline code **is not the complete production online control plane**, and the Nvidia-only Batch-Invariant switch should not be presented as verified on Ascend. Author architecture claims are not independent throughput reproduction. |
| **vLLM upstream** · [v0.31.0 Oct 5 / v0.32.0 Oct 18](https://github.com/vllm-project/vllm/releases) | Changed inference engine implementation, structured request handling, DeepSeek-V4.1 attention/KV and frontend support, including `/v1/systemone` in v0.32.0. | Concrete release tags, not a promise that each feature works on every backend. Repo benchmark results apply only to their disclosed model/hardware/config. |
| **vLLM Ascend** · [v0.30.0 stable Oct 26](https://docs.vllm.ai/projects/ascend/en/v0.30.0/user_guide/release_notes.html) | FlashMLA+DCP/DSpark, KV Pool layerwise pooling, PCP, Model Runner v2 conditional support, EPLB/quantization and hybrid/SSM correctness fixes. Version contract **upstream vLLM 0.30.0 + CANN 9.2.1 + torch-npu 2.10.0.post7**. | **Not a claim of compatibility** with 910B2/CANN 9.1/vLLM 0.23; MRV1 still default on some models and v2 needed by others. Model/hardware limits are explicit in the notes. |
| **SGLang** · [v0.5.22 Oct 19](https://github.com/sgl-project/sglang/releases/tag/v0.5.22) · [HiCache Oct 19](https://www.sglang.io/blog/hicache) | HiCache extends GPU prefix cache across CPU and Mooncake L3: **15.5× effective input throughput** is a *DeepSeek-V4-Flash cache-hit-heavy multi-turn benchmark*, not the universal model throughput. | GPU-only, CPU, L3, model and prefix distribution must be matched. Article is first-party engineering evidence, not a separate peer-reviewed paper. |
| **SGLang** · [Unified Memory Oct 22](https://www.sglang.io/blog/unified-memory) | Hybrid KV + recurrent-state allocators use shared page-major memory and more accurate Eviction stopping; in a **Qwen3.5-4B/RTX5090/28-prefix replay** authors retain 19 vs 10 prefixes (1.9×) and lower return-request time 37.9%. | Both measured arms already use Unified Memory; this is **an eviction-policy comparison**, not 1.9× extra HBM or blanket 37.9% server throughput gain. Backend-layout constraints remain. |
| **SGLang Omni** · [Oct 20 unified interactive runtime](https://www.sglang.io/blog) · [first-party repo](https://github.com/sgl-project/sglang-omni) | Full-duplex interactive sessions, multi-stage multimodal and composable graphs, Oct release v0.2.0. | **Engine/software release**, not a uniquely peer-reviewed paper; latency/voice UX is workload-/hardware-specific. |
| **NVIDIA NGC** · [vLLM 26.10](https://docs.nvidia.com/deeplearning/frameworks/vllm-release-notes/rel-26-10.html) · [SGLang 26.10](https://docs.nvidia.com/deeplearning/frameworks/sglang-release-notes/rel-26-10.html) | Container-pinned stacks: **vLLM 0.31.0/FlashInfer 0.7.1rc5**; **SGLang 0.5.21/FlashInfer 0.7.0.post1** with CUDA 13.4.3 and cloud networking integration. | **Packaged versions lag upstream** vLLM 0.32/SGLang 0.5.22. The image is not a substitute for checking driver/CUDA/SM compatibility and listed known issues. |

**Full October system/research cross-check:** [Monthly source audit](../reviews/OCTOBER_2026_MONTHLY_SWEEP_20261031.md). Model vendor catalogs below remain a separate first-party product view, not a bibliographic source of truth.

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
| [Google](Google.md) | TorchTPU-native vLLM/SGLang, Ragged Paged Attention, JetStream/SAXML, AlphaEvolve optimization tooling, Gemini/Gemma model architecture | **ENGINEERING / first-party research / model**; Inferact/RadixArk backend collaborations credited. AlphaEvolve is not demonstrated recursive inference-agent self-improvement. |
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

**Strict reading rule:** owning an API model is not owning its inference framework; owning a kernel repo is not proof of production adoption. A product/model-family entry is **not** a new canonical paper and does not change the current [topic bibliography inventory](../topics/README.md). New model generations must be cross-checked against the official model menu *and* the release/retirement log. A provider's total downloadable checkpoint count is not feasible to freeze as a manually maintained Markdown list; the authoritative site is linked instead.

**Editorial boundary.** Organization pages represent verifiable first-party releases or research directly attributable to a team. Coauthored work belongs in the topical paper lists unless the institution is explicitly presenting its own system. An API feature is not proof of an undisclosed serving implementation.
