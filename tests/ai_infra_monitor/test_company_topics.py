"""数据契约：公司专题的标签必须与 reading.INDUSTRY_TOPICS 注册表自洽。

这组测试直接读真实事实源 `data/industry.jsonl`，用于保证：
「新增公司/代际只改注册表」这一扩充路径不会因为数据里出现未注册的标签而悄悄失效。
"""
import json
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.reading import INDUSTRY_TOPICS, INDUSTRY_TOPICS_BY_KEY

ROOT = Path(__file__).resolve().parents[2]
INDUSTRY = ROOT / "data" / "industry.jsonl"


def _tagged_rows() -> list[dict]:
    rows = [
        json.loads(line)
        for line in INDUSTRY.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return [
        row
        for row in rows
        if isinstance(row.get("presentation"), dict) and row["presentation"].get("topic")
    ]


class CompanyTopicContractTests(unittest.TestCase):
    def test_every_configured_topic_has_records(self):
        topics = {row["presentation"]["topic"] for row in _tagged_rows()}
        self.assertEqual(topics, set(INDUSTRY_TOPICS_BY_KEY))

    def test_tagged_rows_use_registry_groups_and_generations(self):
        for row in _tagged_rows():
            presentation = row["presentation"]
            topic = presentation["topic"]
            meta = INDUSTRY_TOPICS_BY_KEY[topic]
            groups = {key for key, _label in meta["groups"]}
            context = f"{topic} / {row.get('title')}"
            self.assertIn(presentation.get("topic_group"), groups, context)
            generation = presentation.get("generation")
            if generation:
                self.assertIn(generation, meta["generations"], context)
            self.assertTrue(
                str(row.get("primary_url") or "").startswith("https://"), context
            )

    def test_registry_keys_are_unique_and_ordered(self):
        keys = [str(topic["key"]) for topic in INDUSTRY_TOPICS]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(
            keys,
            [
                "deepseek-ai-systems",
                "moonshot-ai-systems",
                "minimax-ai-systems",
                "zhipu-ai-systems",
                "stepfun-ai-systems",
                "bytedance-ai-systems",
            ],
        )
        for topic in INDUSTRY_TOPICS:
            groups = [key for key, _label in topic["groups"]]
            generations = list(topic["generations"])
            self.assertEqual(len(groups), len(set(groups)), topic["key"])
            self.assertEqual(len(generations), len(set(generations)), topic["key"])


if __name__ == "__main__":
    unittest.main()
