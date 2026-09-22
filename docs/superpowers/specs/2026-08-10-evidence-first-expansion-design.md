# 证据优先的研究—工程资料扩充设计

## 目标

在不限制内部事实库规模的前提下，大幅提升 AI 推理系统论文与工业方案的完整性、可核验性和更新能力，同时把公开视图收敛成有限、稳定、适合快速阅读的入口。扩充顺序是先修可靠性基础，再补最新顶会论文，最后补工业方案与新公司专题。

## 四层结构

1. **内部事实层**：`data/papers.jsonl`、`data/industry.jsonl` 和候选/归档保存完整记录，不设置总量上限。
2. **内部阅读层**：`paper-list.md` 与 `industrial-llm-inference-systems.md` 保留完整 core 主线和滚动探索，服务研究整理与审计。
3. **公开阅读层**：`papers/README.md`、`industry/README.md` 只展示有界精选，强调清晰、稳定和来源可追溯。
4. **归档层**：非主线、过期探索和原始 release 事实继续保留，不进入公开阅读预算。

## 公开阅读预算

- 论文每个七主题最多 8 条，探索区最多 15 条。
- 工业项目每个七主题最多 5 个，探索区最多 15 个项目。
- 每个公司专题最多 8 条。
- 预算只影响公开视图；内部 Markdown 和 JSONL 不截断。

主题内按 `foundation → frontier → supporting` 排序，并保持确定性。预算内优先保留正式会议/官方工程来源、具有 artifact 或物理评测的记录；同项目 release 聚合后只计一个项目。公司专题优先模型架构、kernel/通信、serving 和训练系统，再展示多模态、Agent 与工具生态。

## 可靠性契约

现有空字段无法区分“没有”“尚未检查”和“旧数据未迁移”。在 `evidence` 中增加以下可选字段，并由校验器约束枚举和类型：

- `affiliation_status`: `verified`、`partial`、`not_found`、`not_checked`、`legacy_present`。
- `artifact_status`: `official`、`author_repo`、`third_party`、`not_found`、`not_checked`、`legacy_linked`。
- `metadata_checked_at`: `YYYY-MM-DD`。
- `metadata_sources`: 支撑作者单位、代码或项目归属的 URL 列表。

所有 core 记录都必须具有明确状态。旧记录先机械迁移为 `legacy_present`/`legacy_linked` 或 `not_checked`；公开可见和 foundation/frontier core 记录随后优先核验为 `verified`、`official`、`author_repo` 或有证据的 `not_found`。不得把“搜索不到”直接写成“没有代码”。

## 质量审计

新增共享审计函数和 `monitor.py audit` 命令，输出紧凑 JSON，不读取或打印长摘要。至少统计：

- 各事实库及 scope 的记录数；
- core 中单位、artifact、正式来源和核验状态缺口；
- 七主题数量与公开视图选择数量；
- 最新精确核验日期；
- 超长摘要、缺组织、缺 URL 和重复 identity 数量。

验证器保证公开预算不超限、专题标题不重复、公开视图无原始 HTML，并检查 core 可靠性状态字段。审计本身不修改事实库。

## 扩充与核验顺序

第一批修复所有将进入公开视图的记录及 foundation/core 记录；随后覆盖 frontier/core。作者单位优先使用论文 PDF/正式 proceedings，其次使用 OpenReview、DBLP、OpenAlex 等可追溯来源。代码优先使用论文或作者官方链接、官方 GitHub 组织和 proceedings artifact；只在完成限定搜索并记录来源后标记 `not_found`。

最新论文仅从正式会议录用页、议程、proceedings 或 OpenReview venue 接口进入事实层。工业记录只接受官方仓库、正式工程博客、产品文档或含物理评测的技术报告。新记录必须同时写入来源层级、核验日期、单位/组织状态和 artifact 状态。

## 阶段验收

1. **基础阶段**：公开预算、可靠性字段、审计命令和验证规则完成；重复生成无漂移。
2. **数据修复阶段**：公开可见与 foundation/core 记录无含义不明的空状态，单位与代码结论均有来源。
3. **论文扩充阶段**：官方会议源完成一轮增量扫描，新入库论文通过同一可靠性契约。
4. **工业扩充阶段**：官方项目和公司专题完成一轮增量补充，release 仍按项目聚合。
5. **完成阶段**：全量测试、render、publish、validate、audit 与幂等性检查通过，并按需求逐项审计。
