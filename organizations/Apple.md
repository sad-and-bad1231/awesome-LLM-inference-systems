# Apple

**Local/on-device model inference** on Apple hardware, with emphasis on transparent execution frameworks.

[← Organizations](../README.md#organizations)

## Official Apple Foundation Models crosswalk (2026-10-24)

Apple's [June 2026 third-generation AFM technical introduction](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) explicitly names **five** first-party model roles.

| AFM 3 model | Where it runs / systems scope | First-party evidence |
|---|---|---|
| **AFM 3 Core** | On-device ~3B dense foundation model | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |
| **AFM 3 Core Advanced** | On-device ~20B sparse multimodal model with ~1–4B active parameters, constrained execution | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |
| **AFM 3 Cloud** | Private Cloud Compute server-side workhorse | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |
| **ADM 3 Cloud (Image)** | Private Cloud Compute image generation / editing (not autoregressive text LLM) | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |
| **AFM 3 Cloud Pro** | Complex reasoning/tool-use server model; first-party architecture details limited | [Apple ML Research](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) |

These are publicly described **product models**, not evidence of downloadable complete weights, and not proof that MLX/ExecuTorch/Core ML reproduce Apple production PCC paths.

## Selected first-party architecture and execution sources

| Project | Role | Official source |
|---|---|---|
| **MLX** | Array and autodiff framework optimized for Apple silicon and unified memory. | [GitHub](https://github.com/ml-explore/mlx) |
| **MLX LM** | Model loading, text generation, quantization and local LLM inference on MLX. | [GitHub](https://github.com/ml-explore/mlx-lm) |
| **MLX Swift LM** | Swift ecosystem implementations of on-device LLM/VLM generation. | [GitHub](https://github.com/ml-explore/mlx-swift-lm) |
| **Core ML Tools** | Conversion and optimization of neural networks for Apple's on-device inference runtime. | [GitHub](https://github.com/apple/coremltools) |

**Boundary.** This indexes public SDKs and execution libraries, not the unpublished internal serving behavior of Apple Intelligence.
