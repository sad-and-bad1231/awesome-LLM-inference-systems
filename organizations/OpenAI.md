# OpenAI

Only **publicly documented inference-relevant model designs, execution tooling and interfaces** are listed. Public API availability does not disclose OpenAI's internal serving architecture.

[← Organizations](../README.md#organizations)

## Models and execution

| Work | Inference relevance | Official source |
|---|---|---|
| **gpt-oss (20B / 120B)** | Open-weight MoE reasoning models with documented quantized deployment and reference inference paths. | [Model + reference code](https://github.com/openai/gpt-oss) |
| **gpt-oss reference backends** | PyTorch, Triton and Metal inference implementations; examples are **reference implementations**, not a claim about OpenAI production serving. | [Inference implementations](https://github.com/openai/gpt-oss) |
| **GPT-4o** | Public low-latency multimodal interaction design and model capabilities; not a published kernel/serving architecture. | [Official announcement](https://openai.com/index/hello-gpt-4o/) |

## Infrastructure and interfaces

| Project | Role | Official source |
|---|---|---|
| **Triton** | GPU kernel language/compiler **originated at OpenAI**; now maintained as a wider open-source ecosystem project. | [GitHub](https://github.com/triton-lang/triton) |
| **Harmony** | Public serialization/conversation format, relevant to inference I/O and tool interaction, **not** a scheduler. | [GitHub](https://github.com/openai/harmony) |
| **tiktoken** | Tokenization library used in input processing and token budgeting. | [GitHub](https://github.com/openai/tiktoken) |

**Boundary.** No claims about unpublished model architecture, distributed inference topology, GPU fleet or internal batching policies. The Responses API is an external interface, not evidence of the underlying implementation.
