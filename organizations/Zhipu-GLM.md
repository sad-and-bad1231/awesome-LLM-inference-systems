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
