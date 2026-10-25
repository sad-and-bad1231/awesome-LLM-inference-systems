# Baidu

Baidu/PaddlePaddle's open inference engine and deployment toolchain. Broader Paddle training components are intentionally omitted.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **FastDeploy** | Production-facing inference deployment toolkit with hardware/backend integration. | [Official source](https://github.com/PaddlePaddle/FastDeploy) |
| **PaddleNLP** | Includes LLM model implementations and inference/deployment paths; wider than inference alone. | [Official source](https://github.com/PaddlePaddle/PaddleNLP) |

**Scope:** a brief technical map of publicly documented results and first-party components; not an exhaustive release history, ownership claim for independent runtimes, or independently reproduced benchmark.

## Official ERNIE / Paddle model-family crosswalk (2026-10-24)

**First-party catalog:** [Baidu ERNIE model overview](https://cloud.baidu.com/product/model.html) and [Qianfan ModelBuilder](https://cloud.baidu.com/product/wenxinworkshop.html). **Third-party models merely hosted on Qianfan are excluded from Baidu-owned models**.

| Owned model family | Model / inference implications | Source |
|---|---|---|
| ERNIE 5.1 | Newer optimized foundation family; deployment/EP/P-D claims are vendor evidence, not independently measured | [Official ERNIE models](https://cloud.baidu.com/product/model.html) |
| ERNIE 5.0 / 5.0-Thinking | Native multimodal generation and reasoning, distinct modality/caching contracts | [Official ERNIE models](https://cloud.baidu.com/product/model.html) |
| ERNIE 4.5 / 4.5 Turbo / 4.5 Turbo VL / 4.5-VL-28B-A3B / 4.5-0.3B | Dense/MoE and VL families across edge and server serving | [ERNIE lineup](https://cloud.baidu.com/product/wenxinworkshop.html) |
| ERNIE X1 / X1 Turbo / X1.1 | Reasoning-first model versions; not automatically a novel serving scheduler | [Qianfan first-party model list](https://cloud.baidu.com/product/wenxinworkshop.html) |
| PaddleOCR-VL / PaddleOCR-VL-1.5 / PP-StructureV3 | Document parsing/VL models; specialized encoder–decoder and dynamic input workloads | [Official ERNIE lineup](https://cloud.baidu.com/product/model.html) |
| Baidu speech models / MuseSteamer and iRAG | Speech/text/audio and image/video generation lines; document presence but outside core autoregressive LLM serving | [Qianfan models](https://cloud.baidu.com/qianfan/dev_center/home) |

[FastDeploy](https://github.com/PaddlePaddle/FastDeploy) and [PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP) are deployment/toolchains, **not** individual model releases.
