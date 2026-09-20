"""Shared, compact presentation helpers for research and engineering views."""

from __future__ import annotations

from collections import defaultdict
from html import unescape
import re
from typing import Any

from .curation import THEME_ORDER, curation_for, project_key_for_record


THEME_LABELS = {
    "attention-kernel": "Attention / Kernel",
    "kv-cache": "KV Cache",
    "prefill-decode-transfer": "Prefill–Decode 与传输",
    "speculative-decoding": "Speculative Decoding",
    "moe": "MoE",
    "compiler-dsl": "Compiler / DSL",
    "runtime-scheduling": "Runtime / Scheduling",
    "foundation": "奠基与架构 / Foundation",
}

# 展示用兜底主线，见 curation.THEME_ORDER 注释。
FOUNDATION_THEME = "foundation"


def display_themes(record: dict[str, Any], *, allow_foundation: bool = False) -> list[str]:
    """Return the presentation lanes for a record.

    ``core`` records that no keyword theme matches (for example manually pinned
    foundation root nodes such as architecture or quantization papers) would
    otherwise be missing from every themed section. When ``allow_foundation`` is
    set they fall back to the foundation lane so they stay visible.
    """
    curation = curation_for(record)
    themes = list(curation.get("themes") or [])
    if not themes and allow_foundation and curation.get("scope") == "core":
        return [FOUNDATION_THEME]
    return themes

# --------------------------------------------------------------- 公司专题注册表
# 有序注册表：新增公司只需在此追加一项，render_industry_topics 会自动纳入渲染，
# 无需改动调用方（自洽的扩充路径）。
#
# 每个专题字段：
#   key          记录 presentation.topic 的取值
#   title        专题标题
#   description  专题说明
#   groups       有序 (group_key, label)，对应 presentation.topic_group，兼作次级排序权重
#   generations  该公司「模型代际」的有序链，对应 presentation.generation。
#                排序时按链中下标升序（模型迭代优先）；未命中链的记录排在其后。
DEFAULT_TOPIC_GROUPS = (
    ("model-architecture", "模型架构"),
    ("inference-systems", "推理系统"),
    ("training-data", "训练与数据"),
    ("multimodal-agents", "多模态与 Agent"),
    ("tools-ecosystem", "工具与生态"),
)

INDUSTRY_TOPICS: tuple[dict[str, Any], ...] = (
    {
        "key": "deepseek-ai-systems",
        "title": "DeepSeek AI 系统专题",
        "description": "从模型架构到 kernel、通信、存储和应用数据路径的官方系统材料；专题仅作聚合导航，项目仍保留在原主题主表中。",
        "groups": (
            ("architecture", "架构与系统"),
            ("kernels", "核心算子与通信"),
            ("storage", "存储与数据路径"),
            ("speculative", "推测解码"),
            ("ocr-ecosystem", "OCR 与生态"),
        ),
        "generations": (
            "DeepSeek-V2",
            "DeepSeek-V2.5",
            "DeepSeek-V3",
            "DeepSeek-V3.1",
            "DeepSeek-V3.2",
            "DeepSeek-R1",
            "DeepSeek-OCR",
            "DeepSeek-OCR-2",
        ),
    },
    {
        "key": "moonshot-ai-systems",
        "title": "Moonshot / Kimi 系统专题",
        "description": "Kimi 模型代际与其配套的推理、存储与 Agent 工程材料；专题仅作聚合导航。",
        "groups": DEFAULT_TOPIC_GROUPS,
        "generations": (
            "Kimi-K1",
            "Kimi-K1.5",
            "Kimi-K2",
            "Kimi-K2.5",
            "Kimi-K3",
            "Kimi-Linear",
        ),
    },
    {
        "key": "minimax-ai-systems",
        "title": "MiniMax 系统专题",
        "description": "MiniMax 模型代际与其推理、多模态与 Agent 工具链材料；专题仅作聚合导航。",
        "groups": DEFAULT_TOPIC_GROUPS,
        "generations": (
            "MiniMax-01",
            "MiniMax-M1",
            "MiniMax-M2",
            "MiniMax-M2.1",
            "MiniMax-M2.5",
            "MiniMax-M2.7",
            "MiniMax-M3",
            "MiniMax-Music3",
        ),
    },
    {
        "key": "zhipu-ai-systems",
        "title": "智谱 / Z.ai 系统专题",
        "description": "GLM 模型代际与其推理、多模态与 Agent 工程材料；专题仅作聚合导航。",
        "groups": DEFAULT_TOPIC_GROUPS,
        "generations": (
            "GLM-130B",
            "ChatGLM-6B",
            "ChatGLM2-6B",
            "ChatGLM3",
            "GLM-4",
            "GLM-4-Voice",
            "GLM-4.5",
            "GLM-5",
            "GLM-Edge",
            "GLM-V",
            "GLM-Image",
            "GLM-OCR",
            "GLM-TTS",
            "GLM-ASR",
        ),
    },
    {
        "key": "stepfun-ai-systems",
        "title": "阶跃星辰 / StepFun 系统专题",
        "description": "Step 模型代际与其推理、语音、视频与多模态工程材料；专题仅作聚合导航。",
        "groups": DEFAULT_TOPIC_GROUPS,
        "generations": (
            "Step3",
            "Step3-VL-10B",
            "Step-3.5-Flash",
            "Step-3.7-Flash",
            "Step-Audio",
            "Step-Audio2",
            "Step-Audio-R1",
            "Step-Audio-EditX",
            "Step-Video-T2V",
            "Step-Video-TI2V",
            "Step1X-Edit",
            "Step1X-3D",
            "NextStep-1",
        ),
    },
    {
        "key": "bytedance-ai-systems",
        "title": "字节 Seed / 火山引擎系统专题",
        "description": "Seed 模型代际与其推理、训练与系统基础设施材料；专题仅作聚合导航。",
        "groups": DEFAULT_TOPIC_GROUPS,
        "generations": (
            "Seed1.5-VL",
            "Seed-Thinking-v1.5",
            "seed-oss",
            "Seed-Coder",
            "Seed-X-7B",
            "Seed-Prover",
            "BFS-Prover-V2",
            "Stable-DiffCoder",
        ),
    },
)

INDUSTRY_TOPICS_BY_KEY: dict[str, dict[str, Any]] = {
    str(topic["key"]): topic for topic in INDUSTRY_TOPICS
}


def industry_topic_group_rank(topic: str) -> dict[str, int]:
    groups = INDUSTRY_TOPICS_BY_KEY.get(topic, {}).get("groups") or DEFAULT_TOPIC_GROUPS
    return {key: index for index, (key, _label) in enumerate(groups)}


def industry_topic_group_labels(topic: str) -> dict[str, str]:
    groups = INDUSTRY_TOPICS_BY_KEY.get(topic, {}).get("groups") or DEFAULT_TOPIC_GROUPS
    return {key: label for key, label in groups}


def industry_topic_generation_rank(topic: str) -> dict[str, int]:
    generations = INDUSTRY_TOPICS_BY_KEY.get(topic, {}).get("generations") or ()
    return {label: index for index, label in enumerate(generations)}


def _is_release(record: dict[str, Any]) -> bool:
    title = str(record.get("title", "")).lower().strip()
    url = str(record.get("primary_url", "")).lower()
    channel = str(record.get("venue_or_channel", "")).lower()
    return "/releases/" in url or " releases" in channel or bool(re.fullmatch(r"(?:release\s+)?v?\d[\w.\-]*", title))


def _plain_text(value: str) -> str:
    text = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", value, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[`*_#>]", " ", text)
    return re.sub(r"\s+", " ", unescape(text)).strip()


def _truncate(value: str, max_chars: int) -> str:
    if max_chars <= 0:
        return ""
    if len(value) <= max_chars:
        return value
    return value[: max(0, max_chars - 1)].rstrip() + "…"


def display_summary(record: dict[str, Any], max_chars: int = 240) -> str:
    """Return compact display text without mutating the source record."""
    presentation = record.get("presentation") if isinstance(record.get("presentation"), dict) else {}
    raw = str(presentation.get("blurb") or record.get("summary") or "No summary provided.")
    themes = curation_for(record).get("themes", [])
    if not presentation.get("blurb") and _is_release(record) and (len(raw) > 2000 or "<" in raw):
        labels = [THEME_LABELS[theme] for theme in themes if theme in THEME_LABELS]
        neutral = "官方发布记录"
        if labels:
            neutral += "，涉及：" + "、".join(labels)
        return _truncate(neutral + "。", max_chars)
    return _truncate(_plain_text(raw), max_chars)


def project_key_for(record: dict[str, Any]) -> str:
    return project_key_for_record(record)


def _date_key(record: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(record.get("evidence", {}).get("verified_at") or record.get("discovered") or ""),
        str(record.get("year", "")),
        str(record.get("title", "")),
    )


def _is_prerelease(record: dict[str, Any]) -> bool:
    value = " ".join([str(record.get("title", "")), str(record.get("primary_url", ""))]).lower()
    return bool(re.search(r"(?:rc|alpha|beta|preview)\d*(?:$|[./\-\s])", value))


def _anchor_sort_key(record: dict[str, Any]) -> tuple[int, int, str, str]:
    presentation = record.get("presentation") if isinstance(record.get("presentation"), dict) else {}
    priority = {"foundation": 0, "frontier": 1, "supporting": 2}.get(
        curation_for(record).get("priority"), 3
    )
    return (
        0 if presentation.get("featured") is True else 1,
        priority,
        str(record.get("year", "")),
        str(record.get("title", "")),
    )


def aggregate_industry_records(
    records: list[dict[str, Any]], *, milestone_limit: int = 3
) -> list[dict[str, Any]]:
    """Collapse release-heavy industry facts into deterministic project entries."""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[project_key_for(record)].append(record)

    projects = []
    for key, rows in grouped.items():
        non_releases = [record for record in rows if not _is_release(record)]
        if non_releases:
            anchor = sorted(non_releases, key=_anchor_sort_key)[0]
        else:
            stable = [record for record in rows if not _is_prerelease(record)]
            anchor = max(stable or rows, key=_date_key)

        candidates = [
            record for record in rows
            if record is not anchor
            and curation_for(record).get("scope") == "core"
            and curation_for(record).get("priority") in {"foundation", "frontier"}
            and curation_for(record).get("themes")
        ]
        candidates.sort(key=lambda record: str(record.get("title", "")))
        candidates.sort(key=_date_key, reverse=True)
        candidates.sort(
            key=lambda record: {"foundation": 0, "frontier": 1}.get(
                curation_for(record).get("priority"), 2
            )
        )
        milestones = []
        seen_themes = set()
        for record in candidates:
            primary_theme = (curation_for(record).get("themes") or [""])[0]
            if primary_theme in seen_themes:
                continue
            seen_themes.add(primary_theme)
            milestones.append(record)
            if len(milestones) >= max(milestone_limit, 0):
                break

        themes = [
            theme for theme in THEME_ORDER
            if any(theme in curation_for(record).get("themes", []) for record in rows)
        ]
        scopes = {curation_for(record).get("scope", "archive") for record in rows}
        group_scope = "core" if "core" in scopes else "adjacent" if "adjacent" in scopes else "archive"
        projects.append({
            "project_key": key,
            "anchor": anchor,
            "milestones": milestones,
            "themes": themes,
            "scope": group_scope,
        })
    projects.sort(key=lambda project: _anchor_sort_key(project["anchor"]))
    return projects


def select_industry_topic(records: list[dict[str, Any]], topic: str) -> list[dict[str, Any]]:
    """Select explicitly tagged project anchors, ordered model-generation first.

    Records carrying ``presentation.generation`` sort by their position in the
    topic's generation chain so a company section reads as a model iteration
    timeline; records without a generation fall back to topic-group order.
    """
    tagged = [
        record
        for record in records
        if isinstance(record.get("presentation"), dict)
        and record["presentation"].get("topic") == topic
    ]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in tagged:
        grouped[project_key_for(record)].append(record)

    anchors = []
    for rows in grouped.values():
        non_releases = [record for record in rows if not _is_release(record)]
        if non_releases:
            anchors.append(sorted(non_releases, key=_anchor_sort_key)[0])
        else:
            stable = [record for record in rows if not _is_prerelease(record)]
            anchors.append(max(stable or rows, key=_date_key))

    group_rank = industry_topic_group_rank(topic)
    generation_rank = industry_topic_generation_rank(topic)
    # 未标注代际 / 未命中代际链的记录排在已标注者之后。
    unknown_generation = len(generation_rank)
    anchors.sort(
        key=lambda record: (
            generation_rank.get(
                str(record.get("presentation", {}).get("generation") or ""), unknown_generation
            ),
            group_rank.get(
                str(record.get("presentation", {}).get("topic_group", "")), len(group_rank)
            ),
            str(record.get("title", "")).casefold(),
        )
    )
    return anchors


def _markdown_cell(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def render_industry_topic(
    records: list[dict[str, Any]], topic: str, *, summary_max_chars: int = 240
) -> str:
    """Render one configured company topic table; empty text for unknown topics."""
    meta = INDUSTRY_TOPICS_BY_KEY.get(topic)
    if meta is None:
        return ""
    selected = select_industry_topic(records, topic)
    if not selected:
        return ""
    labels = industry_topic_group_labels(topic)
    lines = [
        f"## {meta['title']}",
        "",
        str(meta["description"]),
        "",
        "| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |",
        "|---|---|---|---|---|",
    ]
    for record in selected:
        presentation = record.get("presentation", {})
        generation = _markdown_cell(presentation.get("generation")) or "—"
        group = labels.get(str(presentation.get("topic_group", "")), "其他")
        url = str(record.get("primary_url") or record.get("artifact_url") or "")
        title = _markdown_cell(record.get("title"))
        linked_title = f"[{title}]({url})" if url else title
        lines.append(
            f"| {generation} | {_markdown_cell(group)} | {linked_title} | "
            f"{_markdown_cell(display_summary(record, summary_max_chars))} | "
            f"{('[official](' + url + ')') if url else '—'} |"
        )
    return "\n".join(lines) + "\n"


def render_industry_topics(
    records: list[dict[str, Any]], *, summary_max_chars: int = 240
) -> str:
    """Render every configured, non-empty company topic in registry order."""
    sections = [
        rendered
        for topic in INDUSTRY_TOPICS
        if (
            rendered := render_industry_topic(
                records, str(topic["key"]), summary_max_chars=summary_max_chars
            )
        )
    ]
    return "\n".join(section.rstrip() + "\n" for section in sections)
