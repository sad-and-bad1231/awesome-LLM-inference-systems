# RadixArk

[← Organizations](README.md) · [← Open-source systems](../communities/README.md)

Inference infrastructure company whose documented open-source foundation is **SGLang**; **Miles** is a distinct post-training framework rather than a direct online serving engine.

| Public work | System role | Scope |
|---|---|---|
| [Company infrastructure statement](https://www.radixark.com/) | Explicitly describes continued investment in SGLang for high-performance runtime, and Miles for distributed post-training. | SGLang is a broad **open-source community**, not solely RadixArk-owned; attribution should follow repositories and actual contributors. |
| [Google TorchTPU launch](https://developers.googleblog.com/en/announcing-new-vllm-and-sglang-inference-engines-on-tpu/) | **RadixArk + Google** developed native PyTorch SGLang backend on TPU, alongside the separate Inferact/vLLM collaboration. | Hardware/backend support and reported throughput are scoped to the published TPU/model combinations; not evidence of universal production parity. |
| [SGLang code](https://github.com/sgl-project/sglang) · [SGLang-Omni](https://github.com/sgl-project/sglang-omni) | Continuous batching, RadixAttention, distributed/multimodal runtime paths. | Shared-source projects; do not claim company ownership of every subsystem. |

**Research fit:** hybrid serving, speculative decoding, persistent sessions and backend portability; record actual SGLang commit plus hardware before performance comparisons.
