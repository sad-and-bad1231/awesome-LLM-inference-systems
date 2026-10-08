# AWS

Selected **cloud inference services and AWS-owned deployment/accelerator software**, rather than every supported model.

[← Organizations](../README.md#organizations)

| Project / service | Role | Official source |
|---|---|---|
| **AWS Neuron** | Compile/runtime software stack for Inferentia and Trainium accelerators, including LLM inference. | [Developer documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/) |
| **NeuronX Distributed** | Model parallel and distributed execution utilities for Neuron devices; also supports training. | [GitHub](https://github.com/aws-neuron/neuronx-distributed) |
| **DJL Serving** | Java-based deep-learning model server with LLM deployment/inference examples; not exclusively AWS hardware. | [GitHub](https://github.com/deepjavalibrary/djl-serving) |
| **Amazon Bedrock** | Managed foundation-model inference API; exposes deployment/service capabilities but not low-level proprietary kernel internals. | [AWS documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) |

**Boundary.** Managed-service interfaces, hardware runtime stacks and open-source software have different evidence levels. No conjectures about Bedrock's internal request routing or cross-provider inference implementation.
