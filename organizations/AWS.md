# AWS

Selected **cloud inference services and AWS-owned deployment/accelerator software**, rather than every supported model.

[← Organizations](../README.md#organizations)

## Official Amazon-owned model-family coverage (2026-10-24)

**Portfolio authorities:** [Amazon Nova family](https://aws.amazon.com/nova/models/), [Nova 2 official documentation](https://docs.aws.amazon.com/nova/latest/nova2-userguide/), [Bedrock provider/model list](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html).

| AWS-owned model family | First-party variants / inference impact | Source |
|---|---|---|
| Nova 2 | **Nova 2 Lite**, **Nova 2 Sonic / 2.5 Sonic**, **Nova Multimodal Embeddings**: multimodal 1M-context, low-latency voice and retrieval workloads | [Nova 2 docs](https://docs.aws.amazon.com/nova/latest/nova2-userguide/) · [Nova models](https://aws.amazon.com/nova/models/) |
| Nova 1 | **Nova Premier, Pro, Lite, Micro**, **Nova Canvas / Reel** older text/visual/creative workload families | [Nova first-generation docs](https://docs.aws.amazon.com/nova/latest/userguide/) |
| Titan | **Titan text/multimodal embedding** and other documented first-party Bedrock model endpoints | [Bedrock provider registry](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) |

**Ownership and evidence:** Bedrock's full catalog is multi-vendor; Claude, Llama, Qwen and DeepSeek hosted there should be indexed under their respective authors, not as Amazon-developed model architecture.

## Selected first-party architecture and execution sources

| Project / service | Role | Official source |
|---|---|---|
| **AWS Neuron** | Compile/runtime software stack for Inferentia and Trainium accelerators, including LLM inference. | [Developer documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/) |
| **NeuronX Distributed** | Model parallel and distributed execution utilities for Neuron devices; also supports training. | [GitHub](https://github.com/aws-neuron/neuronx-distributed) |
| **DJL Serving** | Java-based deep-learning model server with LLM deployment/inference examples; not exclusively AWS hardware. | [GitHub](https://github.com/deepjavalibrary/djl-serving) |
| **Amazon Bedrock** | Managed foundation-model inference API; exposes deployment/service capabilities but not low-level proprietary kernel internals. | [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) |

**Boundary.** Managed-service interfaces, hardware runtime stacks and open-source software have different evidence levels. No conjectures about Bedrock's internal request routing or cross-provider inference implementation.
