# IBM

[← Organizations](README.md)

IBM's inference-system signals include **community distributed serving and hardware-backend prototyping**. The public evidence is narrower than IBM's complete hosted AI catalog.

| Source | Inference engineering | Attribution and status |
|---|---|---|
| [llm-d](https://github.com/llm-d/llm-d) · [router](https://github.com/llm-d/llm-d-router) | Founding collaborative work on distributed routing, KV locality, P/D placement and Kubernetes InferencePool. | Multi-organization community (Red Hat, Google, CoreWeave, NVIDIA, IBM Research and others); no exclusive ownership inference. |
| [vLLM Spyre proof-of-concept](https://github.com/IBM/vllm-spyre) | Historical vLLM hardware plugin and backend integration interface. | **Archived Mar 5, 2025** and tied to older vLLM versions; **not current hardware compatibility evidence**. |
| [IBM Granite family](https://www.ibm.com/granite) | First-party model portfolio relevant to memory/latency/workload deployment requirements. | Architecture/model endpoint disclosures are not new public inference-engine benchmarks. |

**Research fit:** cross-layer routing and lifecycle correctness; separate deployment control planes from accelerator kernels. Technical status must be checked at commit level.
