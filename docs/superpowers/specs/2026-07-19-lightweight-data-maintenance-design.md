# 轻量数据维护与低开销自动化设计

## 目标

在不删除研究与工业事实、不引入数据库服务的前提下，让监控自动化稳定跟进近期会议录用和官方工业方案，并降低日常文件读取、Markdown 生成、Git diff 与 Codex 上下文开销。

本次增强不扩大采集范围，也不改变 `guide.md` 定义的研究—工程双线分类。`data/papers.jsonl` 和 `data/industry.jsonl` 继续作为完整事实层；优化对象主要是候选暂存库、运行状态和候选审计视图。

## 范围与非目标

### 范围

- 将已结束且超过保留窗口的候选从热文件移入不可变冷归档。
- 压缩状态文件中的旧终态记录，同时保留增量去重所需字段。
- 限制候选 Markdown 只展示活跃与近期记录，历史内容由归档统计和文件链接承接。
- 提供显式、幂等的 `maintain` 命令，并在周度 sweep 最后一个批次完成后运行。
- 保持现有 daily/weekly 来源配置、分类规则和正式事实库接口兼容。

### 非目标

- 不迁移到 SQLite、DuckDB 或外部数据库。
- 不删除或改写论文、工业记录及其原始摘要。
- 不重写 Git 历史。
- 不引入外部 LLM 分类、摘要或审核调用。
- 不让 daily 自动化加载冷归档。

## 数据布局

```text
data/
├── papers.jsonl
├── industry.jsonl
├── candidates.jsonl
└── archive/
    └── candidates/
        └── candidates-YYYY-MM.jsonl.gz
```

`data/candidates.jsonl` 是热暂存库，保留：

- 所有非终态候选；
- 最近 `candidate_hot_window_days` 天的终态候选；
- 日期缺失或无法可靠解析的候选，以避免猜测性迁移。

为防止一次大型会议扫描在窗口内生成数万条终态记录，近期终态候选还受 `candidate_hot_terminal_limit` 约束，默认保留按日期和 identity 稳定排序后的最近 500 条。活跃候选不受该数量限制。

只有 `status` 为 `drop` 或 `promote`、且候选日期早于窗口截止日的记录可以归档。候选日期依次取 `discovered`、`evidence.verified_at`，两者均不可用时不归档。默认窗口为 180 天。

归档按候选月份分片。维护命令会读取已有分片、按 canonical identity 去重、稳定排序，然后以确定性 gzip 元数据和原子替换方式写回。这样重复执行结果完全一致；已经不再接收记录的旧月份自然成为不可变文件。

冷归档进入 Git，以保留离线审计能力。日常分类、渲染与发布不会读取这些文件。

## 状态压缩

`ai-infra-state.json` 仍是本地、未跟踪的增量状态文件。维护时对超过同一保留窗口的终态项进行字段压缩：

- 保留 identity 字典键；
- 保留 `fingerprint`、`status`、`source_id` 和 `last_seen`；
- 删除只用于当次运行诊断的 `title`、`url` 和 `run_id`；
- `pending`、`deferred` 等活跃项保持完整；
- 保持最近 100 次 run 摘要的现有行为。

保存继续采用临时文件和 `os.replace`。JSON 改为紧凑编码，避免无意义缩进占用，但不改变 `load_state` 的接口。

## 命令与自动化

新增命令：

```powershell
python scripts/ai_infra_monitor/monitor.py maintain
```

默认读取配置：

```json
{
  "candidate_hot_window_days": 180,
  "candidate_hot_terminal_limit": 500,
  "candidate_archive_dir": "data/archive/candidates",
  "maintenance_on_weekly_sweep": true
}
```

命令执行顺序：

1. 计算以当前 UTC 日期为基准的截止日。
2. 将符合条件的候选按月归档。
3. 原子重写热候选文件。
4. 压缩旧状态项并原子保存状态文件。
5. 输出单行 JSON 统计：迁移数、热记录数、归档分片数、状态压缩数。

`sweep --mode weekly` 只在最后一个实际执行批次成功完成 queue 后调用维护；daily 不自动维护。维护失败时 sweep 返回失败，不继续 finalize，以免把部分维护误报为成功。

`maintain` 必须幂等：相同输入连续运行两次，第二次迁移数和状态压缩数均为零，文件内容无变化。

## 候选审计视图

`ai-infra-candidates.md` 不再展开全部历史终态记录。它展示：

- 所有活跃候选；
- 热文件内最近 180 天的终态候选；
- 冷归档总记录数和各月份分片的相对链接。

视图生成只读取 gzip 分片的逐行计数，不解析摘要和 curation，不将历史正文带入渲染上下文。若归档目录不存在，视为零归档并正常运行。

公共 `README.md`、研究线、工业线和公共归档页不读取候选冷归档，也不受其内容影响。

## 错误处理与恢复

- JSONL 中任一待迁移行不是合法 JSON 时，维护命令失败且不修改热文件或归档。
- 写入先落到目标目录下的临时文件，成功后再原子替换。
- gzip 分片损坏时，命令失败并保留现有文件。
- 热文件和某一归档分片出现同 identity 时，归档保留稳定合并后的单条记录，热文件仅在记录满足迁移条件时移除。
- 不自动处理日期缺失记录；它们留在热文件并计入 `skipped_undated`。
- 不删除 `runs/` manifest。它们仍是逐次发现审计证据。

## 低 Token 原则

- 自动化不调用外部 LLM。
- 命令标准输出仅包含汇总 JSON，不输出标题、摘要或逐记录日志。
- daily/weekly 主流程只读取热候选和两个正式事实库。
- 候选 Markdown 不再嵌入数万条历史候选。
- 冷归档只在显式维护、完整审计或归档验证时读取。

## 测试与验收

测试采用标准库 `unittest`，先失败再实现。至少覆盖：

- 仅归档超过窗口的 `drop/promote`，保留活跃、近期和无日期记录。
- 同一月份分片稳定排序、identity 去重、确定性 gzip 和重复运行无 diff。
- 非法热 JSONL 或损坏归档不会造成部分写入。
- 状态压缩保留增量去重字段，活跃状态不被裁剪。
- 候选视图只展开热记录，并输出冷归档计数与链接。
- weekly sweep 只在最后一批调用维护；daily 和中间批次不调用。
- `maintain` 输出紧凑汇总，CLI help 包含新命令。
- 既有 107 项测试和新增测试全部通过。
- 连续执行 `maintain`、`render`、`publish`、`validate` 两次后无新增 diff。
- 审查 Git diff，确认 `papers.jsonl`、`industry.jsonl` 原始事实未被维护命令改写，现有未提交工作未被覆盖。

## 迁移策略

首次运行使用同一 `maintain` 命令完成，不提供一次性脚本。运行前记录热文件行数和字节数，运行后校验：

- 迁移数等于归档新增 identity 数；
- 热记录数加冷归档记录数不小于迁移前记录数，差异只能来自跨热/冷重复 identity 的确定性去重；
- `new/keep/queued` 等活跃状态数量完全不变；
- 第二次运行没有变化。

首次迁移不会自动提交；用户可以在审查数据 diff 和归档统计后自行决定提交范围。
