# 昇腾 / 华为 AI 系统专题设计

## 目标

在工业材料中增加独立的“昇腾 / 华为 AI 系统专题”，先把国产 NPU 推理执行栈做扎实，再为完整华为 AI 栈保留扩展位置。专题只是按公司与平台阅读的第二入口，不改变七主题主分类，也不复制或删除 JSONL 原始事实。

## 第一阶段边界：推理系统主线

第一阶段只收录有官方或正式证据、直接落在推理执行路径上的材料：

- 昇腾硬件之上的 CANN 与 Ascend C 算子/编译工具链；
- MindIE 与 vLLM Ascend 等推理运行时和服务框架；
- P/D 分离、KV Cache、传输、调度和生产 Serving 论文或工程材料；
- 具备正式会议、官方文档或官方仓库证据的相关系统工作。

不收录泛华为新闻、纯模型能力、纯训练优化、应用产品，以及只有媒体转述而缺少官方锚点的项目。第三方仅“支持 Ascend”不会自动进入专题。

## 聚合与展示

新增专题 key `huawei-ascend-ai-systems`，继续使用显式 `presentation.topic` 与 `presentation.topic_group`。分组固定为：

1. `hardware-toolchain`：CANN、Ascend C 与算子/编译工具链；
2. `inference-runtime`：MindIE、vLLM Ascend 等推理运行时；
3. `serving-kv`：P/D、KV Cache、传输和调度；
4. `production-systems`：有正式证据的生产推理系统。

专题复用现有项目去重、项目预算、摘要压缩和双视图渲染逻辑。现有记录优先补标签；仅为 CANN/Ascend C 和 vLLM Ascend 等关键缺口增加少量官方项目锚点。公共专题仍受每专题 8 项预算约束。

## 第二阶段边界：完整华为 AI 栈

第一阶段稳定后，沿用同一专题增加训练与平台生态分组，候选范围包括 MindSpore、ModelArts、鲲鹏及与 AI 系统直接相关的云和基础设施材料。第二阶段不得倒逼第一阶段放宽推理系统证据门槛，也不在本次实现中批量采集。

## 验收

- 两份工业视图均出现一次“昇腾 / 华为 AI 系统专题”，位置在字节跳动专题之后。
- 专题中至少覆盖工具链、运行时和 Serving/KV 三类官方或正式材料。
- 未显式标记的第三方 Ascend 项目不会因关键词进入专题。
- 每条专题记录的分组合法，非论文项目具有官方来源；原 JSONL 摘要不被改写。
- render、publish、validate 通过，连续生成无漂移。

