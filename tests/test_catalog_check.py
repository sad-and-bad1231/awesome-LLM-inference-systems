"""Minimal offline regression tests for the curated Markdown checker."""
import tempfile
import unittest
from pathlib import Path

from scripts.check_catalog import anchors, first_source_id, is_existing_non_markdown_target


class CatalogIdentityTests(unittest.TestCase):
    def test_existing_code_and_directory_links_are_valid_but_missing_are_not(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            code = root / "checker.py"
            code.write_text("print('ok')", encoding="utf-8")
            markdown = root / "readme.md"
            markdown.write_text("# Heading", encoding="utf-8")
            self.assertTrue(is_existing_non_markdown_target(code))
            self.assertTrue(is_existing_non_markdown_target(root))
            self.assertFalse(is_existing_non_markdown_target(root / "missing.py"))
            self.assertFalse(is_existing_non_markdown_target(markdown))

    def test_openreview_forum_and_pdf_are_one_paper(self):
        forum = "| 2026 | [One](https://openreview.net/forum?id=AbC_12) | Venue | ..."
        pdf = "| 2026 | [One](https://openreview.net/pdf?id=AbC_12) | Venue | ..."
        other = "| 2026 | [Two](https://openreview.net/forum?id=Different) | Venue | ..."
        self.assertEqual(first_source_id(forum), "openreview:AbC_12")
        self.assertEqual(first_source_id(forum), first_source_id(pdf))
        self.assertNotEqual(first_source_id(forum), first_source_id(other))

    def test_arxiv_versions_alias(self):
        abstract = "| 2026 | [Paper](https://arxiv.org/abs/2611.00967) | Preprint | ..."
        pdf = "| 2026 | [Paper](https://arxiv.org/pdf/2611.00967v2.pdf) | Preprint | ..."
        self.assertEqual(first_source_id(abstract), "arxiv:2611.00967")
        self.assertEqual(first_source_id(abstract), first_source_id(pdf))

    def test_doi_identity(self):
        row = "| 2026 | [Paper](https://doi.org/10.1145/123.456) | Venue | ..."
        self.assertEqual(first_source_id(row), "doi:10.1145/123.456")

    def test_github_heading_slug_and_duplicate(self):
        heads = "## Surveys — start here\n## Sample Title\n## Sample Title\n"
        self.assertEqual(
            anchors(heads),
            {"surveys--start-here", "sample-title", "sample-title-1"},
        )


if __name__ == "__main__":
    unittest.main()
