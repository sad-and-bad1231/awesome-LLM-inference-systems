# Organizations

Concise, source-linked maps of **public work with direct consequences for LLM inference**: model architecture, first-party runtime/kernel software, and vendor technical documentation. This is a reading guide, **not** a corporate research ranking or exhaustive publication list.

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

**Editorial boundary.** Organization pages represent verifiable first-party releases or research directly attributable to a team. Coauthored work belongs in the topical paper lists unless the institution is explicitly presenting its own system. An API feature is not proof of an undisclosed serving implementation.
