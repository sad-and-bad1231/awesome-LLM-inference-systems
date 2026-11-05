# StepFun

StepFun's public model-system co-design and generation architectures.

[← Organizations](README.md) · [← Home](../README.md)

## Official model-family coverage (updated 2026-11-04)

The [StepFun official platform model navigation](https://platform.stepfun.com/) lists **three flagship entries and five StepAudio 3 functions** in the October 24 snapshot, with separate historical Step3 and older specialized releases. **Step 5 Preview weights are now published** under the team's [official model collection](https://huggingface.co/collections/stepfun-ai/step-5-preview); the model is **still named Preview**, not an independently verified Step 5 final release.

| Official family / listed model | Workload and systems relevance | Primary source |
|---|---|---|
| Step 5 Preview | 600B MoE / 27B active; 92 Transformer blocks, 1M-token text/vision context, interleaved Gated Sliding Window Attention + Sparse GQA; official FP8/BF16/NVFP4 checkpoints are available. **Preview** remains the published identity. | [Architecture report](https://platform.stepfun.com/blog/inside-step-5-preview) · [official weights](https://huggingface.co/collections/stepfun-ai/step-5-preview) |
| Step 3.7 Flash | Production Agent/omni-oriented fast model; decoding and modality scheduling needs | [Official code](https://github.com/stepfun-ai/Step-3.7-Flash) |
| Step 3.5 Flash | Efficient Flash model family; distinguish release from 3.7 | [Official code](https://github.com/stepfun-ai/Step-3.5-Flash) |
| Step3 | MFA + Attention–FFN Disaggregation first-party systems work | [Official code/report](https://github.com/stepfun-ai/Step3) |
| StepAudio 3 Realtime | Bidirectional real-time audio streaming | [Official portfolio](https://platform.stepfun.com/) |
| StepAudio 3 TTS | Speech synthesis | [Official portfolio](https://platform.stepfun.com/) |
| StepAudio 3 Gen | Audio generation | [Official portfolio](https://platform.stepfun.com/) |
| StepAudio 3 Music | Music generation | [Official portfolio](https://platform.stepfun.com/) |
| StepAudio 3 ASR | Speech recognition | [Official portfolio](https://platform.stepfun.com/) |
| Step Image Edit 2 / StepAudio 2.5 TTS | Older specialized image editing and speech models; not part of the current eight-item model-navigation denominator | [StepFun platform](https://platform.stepfun.com/) |

**Counts:** 3 flagship + 5 audio-specific official listing items = **8** current displayed entries. Step3 and legacy specialized releases are archival context, not extra current model IDs.

## Selected first-party architecture and execution sources

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Step 5 Preview (2026-10-15 architecture report)** | Narrow/deep 92-layer MoE with 3:1 Gated SWA vs sparse full-attention interleaving; Sparse GQA uses an indexer with block-wise token merging to reduce long-context selection cost. It creates concrete hybrid-KV/indexer and speculative-decoding implementation requirements, **not a measured end-to-end runtime speedup**. | [First-party architecture report](https://platform.stepfun.com/blog/inside-step-5-preview) · [weights and model card](https://huggingface.co/stepfun-ai/Step-5-Preview) |
| **Step3: model-system co-design** | MFA attention and Attention–FFN Disaggregation (AFD) for decoding efficiency; official repository contains its systems report. | [Official source](https://github.com/stepfun-ai/Step3) |
| **Step-3.5-Flash** | Efficiency-oriented model release; check official deployment notes rather than inferring a proprietary serving runtime. | [Official source](https://github.com/stepfun-ai/Step-3.5-Flash) |
| **Step-3.7-Flash** | Official agentic, efficiency-oriented model implementation and references. | [Official source](https://github.com/stepfun-ai/Step-3.7-Flash) |
