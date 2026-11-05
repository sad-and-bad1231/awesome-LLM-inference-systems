# Baseten

An inference infrastructure company with a useful public **deployment artifact**, plus kernel/engine selection guidance. This is a practical software operational layer, not a publicly complete proprietary decoder source release.

[← Organizations](README.md)

## First-party stack

| Artifact | Distinct system contribution | Evidence boundary |
|---|---|---|
| [Truss](https://github.com/basetenlabs/truss) | Deployment/package specification for model execution with TensorRT-LLM, vLLM, SGLang or custom frameworks; container builds, GPU assignment, model loading and autoscaled services. | **Open-source deployment stack**, not evidence that Baseten owns NVIDIA TensorRT-LLM or community vLLM/SGLang. |
| [Baseten Inference Stack](https://www.baseten.co/resources/guide/the-baseten-inference-stack) | Documents hardware-aware runtime choices, custom kernels, kernel fusion, model-specific attention and memory hierarchy considerations. | Vendor-authored guide; exact proprietary kernels, comparative precision and serving fleet traces may not be open. |
| [Inference Engineering Book](https://www.baseten.co/inference-engineering/book/04-software/inference-engines) (2026) | Compares vLLM, SGLang and TensorRT-LLM for workload-dependent deployment engineering. | Educational resource, **not** a new benchmark or technical paper for canonical admission. |

## Engineering focus

Study **model compile → container → device placement → deployment rollout** and isolation of engine effects from platform effects. Distinguish build-time GPU demand, cold start, warm inference and real load goodput. Explicitly account for weight precision and quantization in comparisons.

**Status:** public Truss source and first-party engineering docs; unverified numerical advertising omitted.
