# ResearchWork 接手与阅读指南

这份文档是整个仓库的单一入口。你不需要先读懂所有 Markdown，也不需要像程序一样遍历目录。把仓库理解成一张“LLM 推理请求如何穿过系统”的地图即可。

## 先用 30 分钟建立全局感

1. 用 5 分钟看根目录的 [README](../README.md)，只看封面、Overview、Reading Paths 和 Featured，不追求记住条目。
2. 用 15 分钟打开 [论文阅读页](../papers/README.md)，选择当前最关心的一条主线，只读该主题中的 foundation 和 frontier。
3. 用 10 分钟打开 [工业方案页](../industry/README.md)，沿同一主题看项目如何把论文机制做成 runtime、kernel、传输层或部署栈。

第一次阅读到这里就可以停。`data/*.jsonl`、候选页、归档页和自动化脚本都不是日常阅读材料。

## 用一条推理请求理解七条主线

可以把一次在线生成想成下面的路径：

```text
请求进入
  → Runtime / Scheduling：排队、批处理、路由、SLO 和扩缩容
  → Prefill–Decode 与传输：是否拆分两阶段，KV 如何跨 GPU/节点移动
  → KV Cache：状态如何分配、复用、压缩、卸载和分层存储
  → Attention / Kernel：每一步注意力和矩阵算子如何真正跑快
  → Compiler / DSL：如何生成、融合和适配不同硬件上的 kernel
  → Speculative Decoding：如何一次猜测并验证多个未来 token
  → MoE：token 如何路由到专家，以及专家通信和负载如何平衡
  → 输出 token
```

七条主线不是按论文社区或公司划分，而是按推理执行路径划分：

| 主线 | 你真正要问的问题 | 典型入口 |
|---|---|---|
| Attention / Kernel | 单次算子为什么慢，访存、并行和融合怎么改？ | FlashAttention、FlashInfer |
| KV Cache | 长上下文状态放在哪里，如何少占、复用和搬移？ | PagedAttention、vAttention |
| Prefill–Decode 与传输 | 首 token 和后续 token 是否应拆开，状态如何跨节点？ | DistServe、NIXL |
| Speculative Decoding | 怎样减少串行 decode 次数而不改变输出分布？ | Medusa、PRISM、AdaServe |
| MoE | 专家放置、复制、all-to-all 和热点如何处理？ | MegaBlocks、CRAFT、DeepEP |
| Compiler / DSL | 新模型和新硬件如何快速得到高效 kernel？ | Triton、torch.compile |
| Runtime / Scheduling | 多请求、多模型和多节点怎样满足吞吐与 SLO？ | vLLM、SGLang、Dynamo |

一篇论文可能跨多条线。阅读页只把它放在优先级最高的一条线，其他主题作为标签保留，避免同一篇论文反复出现。

## 这个仓库其实只有四层

| 层 | 文件 | 用途 | 平时要不要看 |
|---|---|---|---|
| 全量事实层 | `data/papers.jsonl`、`data/industry.jsonl`、`data/candidates.jsonl` | 保存来源、原始摘要、证据、状态和分类；可审计、不可随意删 | 不需要 |
| 内部阅读层 | [paper-list.md](../paper-list.md)、[industrial-llm-inference-systems.md](../industrial-llm-inference-systems.md) | 七主题的完整内部视图，包含更多 supporting 记录 | 深挖时看 |
| 外部阅读层 | [papers/README.md](../papers/README.md)、[industry/README.md](../industry/README.md) | 有固定预算的简洁入口；每主题只保留最值得先看的条目 | 日常主要看 |
| 探索与归档层 | [archive/README.md](../archive/README.md)、`ai-infra-candidates.md` | 新语境、旧版本、训练专用和非主线事实，不挤占主阅读路径 | 查漏或审计时看 |

公开页“少”不是数据丢失。论文页每主题最多 8 篇，工业页每主题最多 5 个项目，探索区每线最多 15 条；完整记录仍在 JSONL 和内部视图中。

工业记录按项目聚合，不按 release 逐行展示。普通版本、RC 和长 changelog 留在事实层；阅读页选择一个官方项目锚点，并只附少量有主题差异的里程碑。

## 分类哲学：看执行证据，不看关键词热闹

### core

直接改变推理执行路径的工作：KV、P/D、kernel、speculation、MoE、compiler、runtime 或 scheduling。进入 core 需要标题、正式 venue、结构化标签、artifact 或物理评测等证据，不能因为摘要或 release HTML 偶然出现 `inference`、`serving` 就进入。

### adjacent

与推理系统有关，但还不是稳定主线，例如 Agent、多模态生成、特定应用语境。最近 180 天且有正式会议、官方工程来源、artifact 或物理评测之一时，会进入滚动“探索观察”。过期后仍保留在归档。

### archive

训练专用、泛数据库、纯安全攻击、纯应用、缺少推理系统证据，或已被正式版本替代的历史记录。archive 不是“错误”或“垃圾”，只是不会占用当前阅读注意力。

### foundation / frontier / supporting

- `foundation`：建立了长期复用的系统抽象，优先补课。
- `frontier`：较新的主线推进，适合跟踪研究前沿。
- `supporting`：有价值但不是第一阅读顺位。

这个优先级是阅读顺序，不是论文质量排名。

## 证据字段应该怎么理解

- `affiliation_status=verified`：作者单位已由论文首页或官方页面核对。
- `partial`：官方项目是社区协作，能确认维护组织，但不宜伪装成单一公司归属。
- `not_found`：检查过官方材料但没有找到；不是漏填。
- `not_checked`：尚未人工核对，不能当作已验证。
- `artifact_status=official/author_repo`：官方项目或作者仓库可用。
- `legacy_*`：旧数据迁移而来，有信息但证据等级与新记录不同。

事实层保留原始 `summary`。阅读页的短说明优先用 `presentation.blurb`，否则清理 HTML、Markdown 和空白后截断到 240 字符。release changelog 不会原样灌入页面。

## 推荐的六次阅读路线

不要一次读完整个库。每次只解决一个问题，并把论文与工业实现配对。

1. **KV 内存基础**：PagedAttention → vAttention → vLLM。
2. **P/D 解耦**：DistServe → Mooncake/NIXL → Dynamo。
3. **Kernel 执行**：FlashAttention → FlashInfer → Triton/torch.compile。
4. **推测解码**：Medusa → PRISM → AdaServe。
5. **MoE 执行**：MegaBlocks/Tutel → CRAFT → DeepEP。
6. **完整 runtime**：Llumnix/SGLang 论文 → SGLang/vLLM → Production Stack。

读每个条目时只记四件事：瓶颈是什么、状态在哪里、决策由谁做、指标在哪种硬件和负载上成立。这样比记论文数量更有用。

## 公司专题怎么读

[工业方案页](../industry/README.md) 里有 DeepSeek、Kimi/Moonshot、MiniMax、GLM/智谱、阶跃星辰、字节跳动、昇腾/华为专题。专题只是“按公司看全栈”的第二入口，不会改变七主题主分类。

建议先按七主题建立机制地图，再用公司专题回答：这家公司在哪些系统层自研、哪些层依赖社区、论文和项目是否形成了连续工程链。不要把基础模型发布、Agent demo 和推理系统项目混成同一种证据。

昇腾/华为专题先按 **CANN/Ascend C 工具链 → MindIE/vLLM Ascend 运行时 → P/D、KV Cache 与 CloudMatrix384** 阅读国产 NPU 从算子到超节点服务的执行链；再读 **MindSpore → ModelArts → Kunpeng BoostKit**，补齐训练框架、云平台和 CPU/异构基础设施。后三者只作完整栈导航，不会因此进入七主题主线。

## 日常维护只需要这些命令

在 `D:\ResearchWork` 运行：

```powershell
# 最便宜的健康检查：只输出聚合统计，不打印长摘要
python scripts/ai_infra_monitor/monitor.py audit

# 检查 JSONL、重复、链接形状和生成页约束
python scripts/ai_infra_monitor/monitor.py validate

# 修改事实或分类后才重建视图
python scripts/ai_infra_monitor/monitor.py curate
python scripts/ai_infra_monitor/monitor.py render
python scripts/ai_infra_monitor/monitor.py publish
python scripts/ai_infra_monitor/monitor.py validate
```

手动执行这些 Python 命令本身不消耗 Codex/大模型 token。脚本的发现、去重、分类、渲染和验证都是确定性本地逻辑；网络发现会消耗网络请求，但当前 triage 不调用外部 LLM API。

想大致跟上新内容时，不需要全网搜索：

```powershell
# 日常：少量官方工业源和近期信号
python scripts/ai_infra_monitor/monitor.py sweep --mode daily

# 每周：将大源池拆成 6 个可恢复批次
python scripts/ai_infra_monitor/monitor.py sweep --mode weekly --source-batch-count 6 --report
```

自动化不会 push。发现结果先进入候选/运行状态，只有经过 queue、curate、render、publish、validate 后才进入稳定视图。

## 修改时最重要的规则

1. 不手工编辑带有 generated notice 的 Markdown；下一次 render 会覆盖。
2. 新论文写入 `data/papers.jsonl`，新项目写入 `data/industry.jsonl`。
3. 保留原始摘要和来源；展示短说明放在 `presentation.blurb`。
4. 正式录用、单位、代码和物理结果尽量使用会议官网、论文首页、作者仓库或官方工程文档。
5. 不确定时写 `not_checked` 或 `not_found`，不要猜。
6. 修改后至少运行 `validate`；涉及渲染逻辑时再运行完整测试。

更细的机器工作流在 [ai-infra-monitor-workflow.md](ai-infra-monitor-workflow.md)，贡献格式在 [CONTRIBUTING.md](../CONTRIBUTING.md)。只有真正维护自动化时才需要继续读它们。

## 接手时的最小检查单

- 根 README 能打开，论文页和工业页的导航正常。
- `audit` 没有 canonical ID 或标题重复。
- `validate` 通过。
- 公共工业页没有原始 HTML release 正文，也没有同一 GitHub 项目的重复主条目。
- 新增的 core 记录有明确的 affiliation/artifact 状态和来源。
- 连续运行两次 render/publish 不产生新 diff。

满足这些条件，仓库就是健康的。其余工作可以按兴趣逐主题推进，不需要一次理解完所有文件。
