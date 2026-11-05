# Databricks

A model-serving operator with first-party disclosure of **large-scale production inference optimization** across kernel, CPU bottlenecks and request routing. Enterprise ML serving is broader than generative autoregressive decode.

[← Organizations](README.md)

## Public systems evidence

| Source | Concrete mechanism / workload | Critical evidence boundary |
|---|---|---|
| [Superhuman × Databricks serving case study](https://www.databricks.com/blog/how-superhuman-and-databricks-built-200k-qps-inference-platform-together) (2026-05-08) | Joint engineering migrated a **spelling/grammar correction inference workload** from a DIY vLLM stack, removed CPU-side overhead, used FP8 quantization and Hopper attention optimizations. Reports >200k QPS fleet and 750→1200 QPS/H100 pod. | **Joint Superhuman and Databricks work**; quality checked by authors. This *short-output correction service* workload is **not comparable** to long-reasoning, 1M-context autoregressive generation, and FP8 is a precision change. |
| [Model-adaptive AI serving platform](https://www.databricks.com/blog/ai-serving-platform-adapts-your-model) (2026-06-10) | Model/traffic-aware resource selection, serverless autoscaling and adaptive execution controls across models from classic ML to LLM. | One published platform encompasses **heterogeneous ML tasks**. Vendor-wide peak QPS and millisecond P99 must not be presented as token-streaming LLM benchmarks. |
| [Databricks Model Serving docs](https://docs.databricks.com/aws/en/machine-learning/model-serving/) | Managed online and batch inference endpoints, lifecycle, routing and governance contract. | Product behavior is distinct from undisclosed low-level GPU implementation. |

## Engineering focus

A strong study in **CPU overhead and kernel/precision changes translating to end-to-end production QPS**. Carefully normalize response lengths, prompt sizes, batching, model quality and service SLO before using it as a serving baseline.

**Status:** first-party + partner engineering reports and product docs; no independent local replay.
