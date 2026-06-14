import tempfile
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.models import Candidate
from scripts.ai_infra_monitor.ai_infra_monitor.output import append_candidates


class OutputTests(unittest.TestCase):
    def test_candidate_pool_is_stable_and_deduplicated(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "candidates.md"
            path.write_text(
                "# Pool\n\n"
                "| Discovered | Tier | Kind | Source | Title | Topics | URL | Status |\n"
                "|---|---|---|---|---|---|---|---|\n",
                encoding="utf-8",
            )
            item = Candidate(
                title="New Runtime",
                url="https://example.org/runtime",
                source_id="source",
                source_name="Source",
                tier="B",
                kind="industry",
                discovered="2026-06-14",
                topics=("runtime",),
            )
            self.assertEqual(append_candidates(path, [item]), 1)
            self.assertEqual(append_candidates(path, [item]), 0)
            self.assertEqual(path.read_text(encoding="utf-8").count("New Runtime"), 1)


if __name__ == "__main__":
    unittest.main()

