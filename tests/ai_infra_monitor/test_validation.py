import json
import tempfile
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.validation import validate_workspace


class ValidationTests(unittest.TestCase):
    def test_public_collection_budget_overflow_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paper = root / "paper-list.md"
            industry = root / "industrial.md"
            candidates = root / "candidates.md"
            for path in (paper, industry, candidates):
                path.write_text("# Generated\n", encoding="utf-8")
            for directory in (root / "papers", root / "industry", root / "archive"):
                directory.mkdir()
            notice = "<!-- generated from data/papers.jsonl, data/industry.jsonl, or data/candidates.jsonl; do not edit directly -->"
            (root / "README.md").write_text(notice + "\n", encoding="utf-8")
            (root / "papers" / "README.md").write_text(
                notice
                + "\n## At a Glance\n## Collection Navigation\n## Evidence and Selection\n"
                + "## Resource List\n### Runtime / Scheduling (9)\n### 探索观察\n",
                encoding="utf-8",
            )
            (root / "industry" / "README.md").write_text(notice + "\n", encoding="utf-8")
            (root / "archive" / "README.md").write_text(notice + "\n", encoding="utf-8")

            errors = validate_workspace(
                paper,
                industry,
                candidates,
                public_root=root,
                public_limits={"public_paper_limit_per_theme": 8},
            )

            self.assertTrue(any("public paper theme budget exceeded" in error.message for error in errors))

    def test_company_topic_records_have_official_evidence_and_valid_groups(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import INDUSTRY_TOPICS

        topic_configs = {item["key"]: item for item in INDUSTRY_TOPICS}
        expected = set(topic_configs)
        self.assertIn("huawei-ascend-ai-systems", expected)
        self.assertEqual(
            [key for key, _label in topic_configs["huawei-ascend-ai-systems"]["groups"]],
            [
                "hardware-toolchain",
                "inference-runtime",
                "serving-kv",
                "production-systems",
                "training-frameworks",
                "cloud-platform",
                "cpu-heterogeneous",
            ],
        )
        records = [
            json.loads(line)
            for line in (Path(__file__).resolve().parents[2] / "data" / "industry.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip()
        ]
        tagged = [record for record in records if record.get("presentation", {}).get("topic")]

        self.assertEqual({record["presentation"]["topic"] for record in tagged}, expected)
        for record in tagged:
            topic = record["presentation"]["topic"]
            allowed_groups = {key for key, _label in topic_configs[topic]["groups"]}
            self.assertIn(record["presentation"]["topic_group"], allowed_groups)
            self.assertTrue(record.get("primary_url") or record.get("artifact_url"))
            if topic != "deepseek-ai-systems":
                self.assertEqual(record["evidence"]["verification_level"], "official_source")

    def test_detects_duplicate_paper_and_empty_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paper = root / "paper.md"
            paper.write_text(
                "# Papers\n"
                "| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |\n"
                "|---|---|---|---|\n"
                "| Same Paper | A | B | C |\n"
                "| Same Paper | A | B | [bad]() |\n",
                encoding="utf-8",
            )
            industry = root / "industry.md"
            industry.write_text(
                "# Industry\n"
                "| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |\n"
                "|---|---|---:|---|---|---|\n",
                encoding="utf-8",
            )
            candidate = root / "candidate.md"
            candidate.write_text(
                "# Pool\n"
                "| Discovered | Tier | Kind | Source | Title | Topics | URL | Status |\n"
                "|---|---|---|---|---|---|---|---|\n",
                encoding="utf-8",
            )
            errors = validate_workspace(paper, industry, candidate)
            messages = "\n".join(error.message for error in errors)
            self.assertIn("duplicate paper title", messages)
            self.assertIn("empty markdown link", messages)


if __name__ == "__main__":
    unittest.main()

