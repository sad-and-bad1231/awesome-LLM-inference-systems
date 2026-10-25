# StepFun

StepFun's public model-system co-design and generation architectures.

[← Organizations](README.md) · [← Home](../README.md)

## Official model-family coverage (2026-10-24)

The [StepFun official platform model navigation](https://platform.stepfun.com/) lists **three current flagship models and five StepAudio 3 functions**, with separate historical Step3 and older specialized image/audio releases.

| Official family / listed model | Workload and systems relevance | Primary source |
|---|---|---|
| Step 5 Preview | Current flagship preview (production task execution); **preview** label retained | [Official model navigation](https://platform.stepfun.com/) |
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
| **Step3: model-system co-design** | MFA attention and Attention–FFN Disaggregation (AFD) for decoding efficiency; official repository contains its systems report. | [Official source](https://github.com/stepfun-ai/Step3) |
| **Step-3.5-Flash** | Efficiency-oriented model release; check official deployment notes rather than inferring a proprietary serving runtime. | [Official source](https://github.com/stepfun-ai/Step-3.5-Flash) |
| **Step-3.7-Flash** | Official agentic, efficiency-oriented model implementation and references. | [Official source](https://github.com/stepfun-ai/Step-3.7-Flash) |
