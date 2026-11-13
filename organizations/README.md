# Organizations

Source-linked maps of **first-party model families plus inference infrastructure**. Model-family crosswalks were first checked on **2026-10-24** and selectively updated through **2026-11-12**; it covers named releases and relevant modalities rather than only 1–2 selected flagships. This is **not** a byte-for-byte mirror of ever-changing API snapshot IDs, thousands of checkpoint quantizations, or other vendors' hosted models. Read the linked provider catalog when exact live endpoints matter.

[← Home](../README.md) · [Research labs & open source](../communities/README.md)

## How organizations are selected

These **49 China/US profiles** are an engineering-source map, **not** a company ranking or exhaustive global coverage. An organization is useful here when its first-party evidence reveals a relevant part of the inference execution stack: **(1)** a model architectural decision that changes inference cost, **(2)** an inspectable runtime/kernel/compiler/transport implementation, **(3)** production engineering with identifiable mechanisms and constraints, or **(4)** an accelerator/backend design. A source-only service or API is explicitly labeled; it does not establish ownership of undocumented kernels, schedulers, or benchmark results.

**Reading priority:** follow source code/implementation and published system artifacts first; read engineering reports for workload and deployment context; use model catalogs and service pages for compatibility and requirements. Community-owned or co-developed projects remain attributed to their actual maintainers. Profiles vary in evidence depth deliberately; a short page should not be padded with unsupported architecture claims. See the [research/open-source map](../communities/README.md) for projects that cross company boundaries, and the [source audits](../reviews/ORG_LAB_OSS_SWEEP_20261105.md) for provenance.

## China

| Organization | Public work |
|---|---|
| [DeepSeek](DeepSeek.md) | V4.1-Flash-1017 · DeepInfer production E/P/D + 3FS KV design · FlashMLA/DeepSelect · DeepEP/DeepGEMM Ascend backends · TileKernels/DeepJIT (950/CANN 9.2) |
| [Tencent](Tencent.md) | **Hy4 final vs Preview** · WorkBuddy model/product co-design · AngelSlim/AngelSpec · KsanaLLM · Hy4-preview RSI signal |
| [Alibaba Group / Qwen](Qwen-Alibaba.md) | Qwen4 preview / Qwen-AgentWorld · **RTP-LLM + BladeLLM** · Tair / FlashKV · AgentScope / GUI-Owl / AgentCore · RollArt / EPIC · MNN · Zhenwu V900 |
| [Huawei / Ascend](Huawei.md) | CANN · **TorchNPU** backend · MindIE · community vLLM-Ascend |
| [StepFun](StepFun.md) | **Step 5 Preview open weights** · Gated SWA / Sparse GQA · Step3 MFA + Attention–FFN Disaggregation |
| [MiniMax](MiniMax.md) | **MiniMax-01/M1/M3/M3.1 + MSA/DSpark** · **H3/H3-Image video and image** · Speech/Music · **Forge / MaxProof / Agent Team** · MiniMax Code/Hailuo/Audio · public inference boundary |
| [Moonshot AI / Kimi](Moonshot-Kimi.md) | **k1.5→K3.1 Pro** · MoBA/KDA/AttnRes · **Kimi-VL/Audio/Prover** · **Mooncake/MoonEP/FlashKDA/Checkpoint Engine** · Kimi Code |
| [Zhipu AI / GLM](Zhipu-GLM.md) | **THUDM GLM→5.3/5.3-Flash** · **CogVideo/GLM-Image/ASR** · AutoGLM/ZCode · **slime/IndexCache** · **GLM-5.3-Flash EPD / Infra Agent** |
| [Xiaomi / MiMo](Xiaomi.md) | MiMo hybrid attention + MTP |
| [ByteDance / Seed](ByteDance.md) | **Seed2.1 + Seedance/Seedream/SeedRealtime** · **Agent HarnessDev/Aspire** · **MegaScale-Omni / VeOmni / Charon** · **Triton-distributed / FLUX–COMET / ByteIR** · **Doubao / Jimeng / CapCut** · Volcano Ark/ServingKit |
| [Baidu / Paddle](Baidu.md) | **ERNIE 2019→5.5 research lineage** · **HCA/MLA/Latent MoE/ECHO** · FastDeploy P/D + KV/EP · **FlashMask-4** · **ERNIE Evolve (inference-engine optimization)** · **DCore (controlled speculation evaluation)** |
| [Meituan / LongCat](Meituan.md) | **[CODE]** SGLang-FluentLLM · P/D KV transfer · sparse MoE/LSA · W4A4 / numerical consistency |
| [Xiaohongshu / Rednote](Xiaohongshu.md) | **[CODE + PREPRINT]** HYPIC hybrid-position-independent cache · Relax training/rollout |
| [Ant Group](Ant-Group.md) | **[CODE + COMMUNITY]** Humming quantized dense/MoE JIT kernels with vLLM |
| [Kuaishou / Kwai](Kuaishou.md) | **[MODEL + SERVICE]** Keye-VL DSA · StreamLake Vanchin prefix cache / observability |
| [JD.com / JD Cloud](JDCloud.md) | **[CODE + SERVICE]** xLLM Service cluster/engine layer · JoyMaaS API gateway |
| [iFLYTEK / Spark](iFLYTEK.md) | **[SERVICE]** domestic heterogeneous AI platform · online/batch deployment |
| [Moore Threads](MooreThreads.md) | **[CODE]** MUSA vLLM backend fork · MUSA tensor engine / kernel tooling |
| [Cambricon / MLU](Cambricon.md) | **[BACKEND CODE]** torch_mlu · CNToolkit/CNNL/CNCL device stack; older public release matrix |

## United States

| Organization | Primary focus |
|---|---|
| [NVIDIA](NVIDIA.md) | TensorRT-LLM · Dynamo · NIXL · GPU kernels |
| [Google](Google.md) | **TorchTPU vLLM/SGLang** · **TPU Sync / Agent Compute Engine (Nov 9)** · **XLA Serving Engine (Nov 5)** · llm-d / Ragged Paged Attention · AlphaEvolve |
| [Microsoft](Microsoft.md) | DeepSpeed · Splitwise · vAttention · ONNX Runtime |
| [AMD](AMD.md) | ROCm · AITER · **ATOM** engine · **MORI** EP/KV communication · **InferaSim** |
| [OpenAI](OpenAI.md) | gpt-oss · Triton · token/runtime formats |
| [Anthropic](Anthropic.md) | **Fable/Mythos 5.2 (Nov 9)** public API behavior; no inferred internals |
| [Meta](Meta.md) | Llama · **KernelEvolve optimization agent** · TP/CP/EP systems · ExecuTorch / xFormers |
| [AWS](AWS.md) | Neuron · DJL Serving · Bedrock |
| [Apple](Apple.md) | MLX · local/on-device inference |
| [Intel](Intel.md) | OpenVINO · GenAI inference |
| [Together AI](Together-AI.md) | **Together Compiler** · persistent-engine agent optimization · polymorphic serving |
| [Asari AI](Asari-AI.md) | **Whole-stack agent optimization** · vLLM profiling/verification/experience reuse |
| [Cerebras](Cerebras.md) | **CS-4 / Nexus** · wafer-scale inference and rack-scale co-design |
| [Modal](Modal.md) | **FlashAttention-4 decode optimization** · SGLang speculative inference · deployment |
| [Fireworks AI](Fireworks-AI.md) | **Disaggregated inference engine** · KV routing · multi-node EP · FireOptimizer |
| [Groq](Groq.md) | **LPU / deterministic dataflow** · on-chip SRAM · latency-oriented hardware/runtime |
| [Anyscale / Ray Serve](Anyscale.md) | **[CODE + ARCHITECTURE]** LLMServer / replica routing · P/D and DP-attention deployment patterns |
| [Baseten](Baseten.md) | **[CODE + ENGINEERING]** Truss · engine-specific deployment/compile/autoscaling |
| [Databricks](Databricks.md) | **[CASE STUDY]** CPU+kernel+FP8 full-stack optimization · Model Serving |
| [Red Hat / llm-d](Red-Hat.md) | **[COMMUNITY CODE]** distributed inference router · KV/P-D · multi-tenant QoS |
| [Cloudflare / Workers AI](Cloudflare.md) | **[PRODUCTION ENGINEERING]** P/D · KV compression/cache · SGLang isolation fixes |
| [Predibase / LoRAX](Predibase.md) | **[CODE]** multi-adapter batching · LoRA load/evict/prefetch scheduler |
| [CoreWeave](CoreWeave.md) | **[COMMUNITY + PLATFORM]** llm-d founding contributor · K8s production inference |
| [Modular](Modular.md) | **[COMPILER + SERVER CODE]** MAX graph compiler/runtime · Mojo kernels · OpenAI-compatible model server |
| [Hugging Face](Hugging-Face.md) | **[CODE + ARCHIVE]** Transformers/Optimum · TGI now archived; cross-runtime interoperability |
| [Inferact](Inferact.md) | **[CODE + COLLAB]** vLLM maintainers · joint TorchTPU backend / CI with Google |
| [RadixArk](RadixArk.md) | **[CODE + COLLAB]** SGLang community · joint TorchTPU backend with Google |
| [Tenstorrent](Tenstorrent.md) | **[KERNEL + HARDWARE]** TT-Metal / TT-NN · low-level kernel / multi-chip LLM programming |
| [IBM](IBM.md) | **[COMMUNITY + ARCHIVE]** llm-d collaboration · historical archived vLLM Spyre plugin |
| [BentoML](BentoML.md) | **[DEPLOYMENT CODE]** BentoVLLM launcher · service worker/replica scaling · model lifecycle |

**November 9 primary-source checkpoint:** [model and inference-stack reconciliation](../reviews/NOVEMBER_2026_SYSTEMS_SWEEP_20261109.md) verified K3.1 Pro public weights and sparse-serving mechanics, Fable/Mythos 5.2 API status, AMD InferaSim; **Qwen4, DeepSeek V4.1 Pro and Astra 6.2 remain unverified** and out of live release tables.

## Historical source notes and model release reconciliation

The live directory above is the stable **49-profile navigation** (19 China / 30 US), not a model-release feed. Dated company additions, version crosswalks, source corrections, first-party launch receipts and old catalog reconciliation have been preserved **verbatim** in [Organizations source chronology](SOURCE_CHRONOLOGY.md) (2026-10-24 through 2026-11-09); the [Baidu primary-source audit](../reviews/BAIDU_PRIMARY_SOURCE_AUDIT_20261111.md), [Alibaba primary-source audit](../reviews/ALIBABA_PRIMARY_SOURCE_AUDIT_20261112.md) and [MiniMax/ByteDance source audit](../reviews/MINIMAX_BYTEDANCE_PRIMARY_SOURCE_AUDIT_20261113.md) and [Kimi/Zhipu source audit](../reviews/KIMI_ZHIPU_PRIMARY_SOURCE_AUDIT_20261113.md) document the recent company maps. New product/API/model names should be verified against original vendor sources before being described as current. The [November 5 source audit](../reviews/ORG_LAB_OSS_SWEEP_20261105.md) records inclusion boundaries.

**Editorial boundary.** Organization pages represent verifiable first-party releases or research directly attributable to a team. Coauthored work belongs in topical paper lists unless an institution explicitly presents its own system. An API feature is not proof of an undisclosed serving implementation.
