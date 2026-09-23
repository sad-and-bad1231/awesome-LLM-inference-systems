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
            # 华为专题沿用其「第一阶段仅收录直接作用于推理执行路径的官方证据」政策，
            # 因此强制 official_source。其余专题在 head 线已扩展到 20 个、覆盖 374 条
            # 带 topic 的记录，其中含迁移期导入的 legacy_import，故只要求来源等级已
            # 显式标注（不做"全部官方源"的强断言）。
            level = record["evidence"]["verification_level"]
            if topic == "huawei-ascend-ai-systems":
                self.assertEqual(level, "official_source")
            else:
                self.assertIn(level, {"official_source", "legacy_import"})

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

