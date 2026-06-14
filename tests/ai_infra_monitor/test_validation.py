import tempfile
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.validation import validate_workspace


class ValidationTests(unittest.TestCase):
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

