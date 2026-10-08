# Google

A short index of Google's **inference-system research, open-source serving software, and efficient model execution**.

[← Organizations](../README.md#organizations)

## Foundational techniques and models

| Work | Inference relevance | Primary source |
|---|---|---|
| **Multi-Query Attention (MQA)** (2019) | Sharing key/value heads reduces autoregressive decode KV bandwidth. | [Paper](https://arxiv.org/abs/1911.02150) |
| **Efficiently Scaling Transformer Inference** (MLSys 2023) | TPU parallelism and performance-model-guided latency/throughput engineering. | [MLSys](https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html) |
| **Speculative Decoding** (ICML 2023) | Draft-and-verify decoding while preserving the target distribution. | [PMLR](https://proceedings.mlr.press/v202/leviathan23a.html) |
| **Grouped-Query Attention (GQA)** (EMNLP 2023) | Attention-head grouping trades off decode bandwidth and model quality. | [ACL Anthology](https://aclanthology.org/2023.emnlp-main.298/) |
| **Gemma family** | Open-weight architectures and deployment examples; model design, **not** a disclosed Google production serving stack. | [Official models/docs](https://ai.google.dev/gemma/docs) |

## Infrastructure

| Project | Role | Official source |
|---|---|---|
| **JetStream** | High-throughput LLM inference engine targeting TPU-oriented deployments. | [GitHub](https://github.com/google/JetStream) |
| **SAX / SAXML** | Scalable JAX/TPU model-serving platform. | [GitHub](https://github.com/google/saxml) |
| **MaxText** | Open JAX/TPU LLM implementation with generation/inference paths; also a training framework. | [GitHub](https://github.com/google/maxtext) |
| **Gemma.cpp** | Lightweight C++ inference for Gemma on resource-constrained devices. | [GitHub](https://github.com/google/gemma.cpp) |

**Boundary.** Selected Google-authored research and first-party projects, not the entirety of Google Cloud's managed model catalog. A model architecture contribution is not evidence of an unpublished serving implementation.
