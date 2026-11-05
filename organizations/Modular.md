# Modular — MAX / Mojo inference stack

[← Organizations](README.md) · [← Open-source systems](../communities/README.md)

Modular is a compiler/runtime and inference-software company. The [Modular Platform repository](https://github.com/modular/modular) exposes inspectable components beyond a hosted-model API.

| Public source | Executable scope | Evidence boundary |
|---|---|---|
| [Modular/MAX/Mojo](https://github.com/modular/modular) | Mojo compiler and GPU programming abstractions, MAX accelerator kernels, graph compiler, ML runtime/driver, Python model pipelines and OpenAI-compatible MAX inference server. | **Source availability varies by component and license**; a GitHub code path is not proof every part of the commercial platform is fully open or hardware agnostic. |
| [MAX inference server code](https://github.com/modular/modular/tree/main/max/python/max/serve) | Model-serving entry points and runtime integration that can be audited across graph compilation, kernel dispatch and batching/deployment. | Compare actual source and versions against vLLM/SGLang; vendor demonstrations do not establish identical model/hardware/precision baselines. |

**Why follow:** MAX is an unusually direct **compiler ↔ model graph ↔ accelerator kernel ↔ online serving** design, relevant to graph/runtime representation and new-device bring-up. Its **licensed model/runtime** contracts differ from Apache-only open-source projects; check repository and product terms before adoption.

**Status:** inspectable vendor source and first-party documentation; no independent hardware reproduction, undisclosed proprietary internals or universal speedup claims.
