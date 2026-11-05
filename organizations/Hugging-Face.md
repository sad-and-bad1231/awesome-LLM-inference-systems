# Hugging Face — inference infrastructure

[← Organizations](README.md) · [← Open-source systems](../communities/README.md)

Hugging Face contributes **model interoperability, inference deployment and historical server infrastructure**; models merely hosted on its Hub are not Hugging Face-authored architectures.

| Source | What to study | Evidence boundary |
|---|---|---|
| [Text Generation Inference](https://github.com/huggingface/text-generation-inference) | Historical Rust/Python/gRPC server, batching, streaming and optimized backends. | **Archived by its owner on 2026-03-21; maintenance/read-only, not a current fast-moving engine**. Maintainers recommend modern vLLM/SGLang and interoperable local runtimes. |
| [Transformers](https://github.com/huggingface/transformers) | Shared reference model implementations and interoperability with external optimized serving backends. | Model code/reference execution ≠ production model-serving scheduler or guaranteed kernel performance. |
| [Optimum](https://github.com/huggingface/optimum) | Accelerator-specific conversion, quantization and deployment utilities across partner runtimes. | Backend integrations require version-specific validation; they are not wholly owned hardware kernels. |
| [Inference Endpoints](https://huggingface.co/docs/inference-endpoints/index) | Managed dedicated model-serving endpoints with deployment/autoscaling controls. | Hosted-service capabilities do not disclose internal per-model execution paths. |

**Engineering value:** compare model compatibility and deployment paths while respecting **TGI's archived status**. Do not infer ownership or performance from hosted checkpoint counts. First-party code and docs; no local benchmark reproduction.
