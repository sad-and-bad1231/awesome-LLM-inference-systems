# Zhipu AI / GLM

Zhipu AI / Z.ai's published GLM architectures and official deployment references. The inference engines that serve GLM models should be credited independently.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **GLM-4.5** | Official model family and documentation; MoE model execution and inference deployment information. | [Official source](https://github.com/zai-org/GLM-4.5) |
| **GLM-5** | Official model-family documentation and architecture/deployment notes. | [Official source](https://github.com/zai-org/GLM-5) |
| **GLM-5.3 / GLM-5.3-Flash** (2026) | Updated DSA/MoE inference contracts; GLM-5.3 model metadata declares `glm_moe_dsa` and GLM-5.3-Flash declares `glm5_next` (multimodal). These are **checkpoint model-family updates**, not stand-alone proof of novel serving kernels. | [GLM-5.3 official model card](https://huggingface.co/zai-org/GLM-5.3) · [5.3-Flash official model card](https://huggingface.co/zai-org/GLM-5.3-Flash) |
| **GLM-4** | Earlier model releases and reference deployment paths; historical context only. | [Official source](https://github.com/THUDM/GLM-4) |

**Scope:** Only source-documented model/execution contracts. Serving-engine and attention-backend support requires version-specific source evidence; provider speed and quantized deployment claims are not independent kernel evaluations.

## Official model-family crosswalk (2026-10-24)

**First-party release map:** [GLM models used by Z.ai AutoClaw](https://autoclaw.z.ai/models/) and [official GLM-5.3 research note](https://z.ai/blog/glm-5.3).

| Official release | Architecture / execution note | Primary source |
|---|---|---|
| GLM-5.3 | Same GLM-5.2 **base model**, post-training updated; should **not** be counted as a new DSA/KV architecture | [Official GLM-5.3 explanation](https://z.ai/blog/glm-5.3) |
| GLM-5.3-Flash | Independently named efficient **native multimodal** model using **hybrid sparse and linear attention**, relevant to indexer/recurrent-state execution | [Official model menu](https://autoclaw.z.ai/models/) · [Model card](https://huggingface.co/zai-org/GLM-5.3-Flash) |
| GLM-5.2 | IndexShare long-context lineage, model base for 5.3 | [Official GLM-5.3 note](https://z.ai/blog/glm-5.3) |
| GLM-5-Turbo / GLM-5V-Turbo | Agent-focused and vision+UI-focused API/model offerings; distinct modality workload contracts, not separate compiler advances | [Official model menu](https://autoclaw.z.ai/models/) |
| GLM-5 | Earlier 5th-generation MoE/DSA checkpoint family | [Official repository](https://github.com/zai-org/GLM-5) |
| GLM-4 / GLM-4.5 and 4.x historical variants | Historical open GLM, MoE and multimodal work; precise endpoint availability requires current API catalog | [GLM-4](https://github.com/THUDM/GLM-4) · [GLM-4.5](https://github.com/zai-org/GLM-4.5) |

**Source correction:** GLM-5.3-Flash's hybrid sparse + linear execution is technically different from GLM-5.3's same-base-model post-training story; neither should be conflated with the other's speedups.
