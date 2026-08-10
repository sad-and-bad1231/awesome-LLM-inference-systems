# 华为完整 AI 栈专题扩展设计

## 目标

在已完成的“昇腾 / 华为 AI 系统专题”推理主线之后，补齐华为 AI 栈的框架、云平台与异构基础设施层。扩展仍是公司专题导航，不放宽七主题主线的严格判定。

## 范围

新增四个官方或第一方正式锚点：

- CloudMatrix384：超节点互联与生产 LLM Serving；
- MindSpore：端、边、云训练/推理框架及昇腾软硬协同；
- ModelArts：开发、训练、部署、资源调度和运维平台；
- Kunpeng BoostKit 推理加速：鲲鹏 CPU 上的推理算子与异构支撑。

专题新增 `training-frameworks`、`cloud-platform`、`cpu-heterogeneous` 三个分组，放在第一阶段四组之后。CloudMatrix384 直接属于生产推理系统，可保留 `core`；MindSpore、ModelArts 和 Kunpeng 使用 `adjacent`，避免泛平台材料进入七主题主线。

## 展示和预算

内部工业清单展示完整专题。公共清单继续遵守每公司专题 8 项预算，因此优先保留第一阶段推理链和 CloudMatrix384，再展示最高排序的平台锚点；完整事实仍可从内部清单和 JSONL 获取。不提高全局预算，不复制 release 记录。

## 验收

- 专题分组顺序为：工具链、运行时、Serving/KV、生产系统、训练框架、云平台、CPU/异构基础设施。
- 四个新增锚点均有官方或第一方正式来源。
- MindSpore、ModelArts、Kunpeng 不进入七主题 `core` 主线。
- 内部专题完整显示十个项目，公共专题保持 8 项预算。
- 全量测试、validate 和重复生成幂等检查通过。
