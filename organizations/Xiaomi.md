# Xiaomi

Xiaomi MiMo's publicly documented inference-efficient model designs.

[← Organizations](README.md) · [← Home](../README.md)

## Official model/API family coverage (2026-10-24)

**Authoritative listing:** [MiMo models API page](https://mimo.mi.com/docs/zh-CN/quick-start/summary/model) and [official release chronology](https://mimo.mi.com/docs/zh-CN/updates/model). The model-list API example contains older versions; deprecations override stale examples.

| Official model / API-ID grouping | State and inference significance | Primary source |
|---|---|---|
| `mimo-v2.6-pro` | Current flagship multimodal/long-context reasoning, 1M context | [Official models](https://mimo.mi.com/docs/en-US/quick-start/model) |
| `mimo-v2.6-flash` | Current cost/throughput-oriented generation tier | [Official models](https://mimo.mi.com/docs/en-US/quick-start/model) |
| `mimo-v2.6-pro-ultraspeed` | Current special high-speed API tier; not an independent published attention architecture | [Official models](https://mimo.mi.com/docs/en-US/quick-start/model) |
| `mimo-v2.5` / `mimo-v2.5-pro` | **Retired from API 2026-10-21**; historical 1M multimodal / trillion-class MoE | [Official deprecation note](https://mimo.mi.com/docs/zh-CN/quick-start/summary/model) |
| `mimo-v2.5-asr` | Speech recognition, different streaming serving path | [Official releases](https://mimo.mi.com/docs/en-US/updates/model) |
| `mimo-v2.5-tts` / `-voiceclone` / `-voicedesign` | TTS and speech customization API variants; not text-LLM model architectures | [Official model list API example](https://mimo.mi.com/docs/zh-CN/api/model/list-models) |
| MiMo-V2-Flash | Historical hybrid sliding-window/global attention + MTP, explicitly kept for architecture lineage | [Source](https://github.com/XiaomiMiMo/MiMo-V2-Flash) |

**Availability:** do not conflate V2.6 product tiers, deprecated V2.5 models and the older GitHub open-weight architecture.

## Selected first-party architecture and execution sources

| Public work | Inference relevance | Primary source |
|---|---|---|
| **MiMo-V2-Flash** | Hybrid sliding-window/global attention and MTP for reduced KV footprint and accelerated decoding; official deployment recipes. | [Official source](https://github.com/XiaomiMiMo/MiMo-V2-Flash) |
