"""Minimal offline regression tests for the curated Markdown checker."""
import unittest

from scripts.check_catalog import anchors, first_source_id


class CatalogIdentityTests(unittest.TestCase):
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
