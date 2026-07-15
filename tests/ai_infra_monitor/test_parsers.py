import json
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.parsers import (
    parse_feed,
    parse_github_releases,
    parse_html_bold_program,
    parse_html_index,
    parse_html_program,
)


FIXTURES = Path(__file__).parent / "fixtures"


class ParserTests(unittest.TestCase):
    def test_parse_atom_feed(self):
        items = parse_feed((FIXTURES / "feed.xml").read_bytes(), "fixture")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Efficient LLM Serving with KV Cache Transfer")
        self.assertEqual(items[0]["published"], "2026-06-14T10:00:00Z")

    def test_parse_html_index_resolves_links(self):
        items = parse_html_index(
            (FIXTURES / "index.html").read_bytes(),
            "https://conference.example/program/",
        )
        self.assertEqual(items[0]["url"], "https://conference.example/paper/one")
        self.assertEqual(items[1]["url"], "https://conference.example/about")

    def test_parse_html_index_can_filter_link_prefixes(self):
        items = parse_html_index(
            (FIXTURES / "index.html").read_bytes(),
            "https://conference.example/program/",
            ("https://conference.example/paper/",),
        )
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Efficient Agent Serving with Program Scheduling")

    def test_parse_html_program_extracts_unlinked_papers_and_event_titles(self):
        body = b"""
        <div class='paper'><div class='paper-title'>Program LLM Serving</div>
        <div class='paper-authors'>A. Author (Example University)</div></div>
        <strong><a href='#' data-event-modal='event-42'>HPCA LLM Inference</a></strong>
        """
        items = parse_html_program(body, "https://conference.example/program/")
        self.assertEqual([item["title"] for item in items], ["Program LLM Serving", "HPCA LLM Inference"])
        self.assertEqual(items[0]["url"], "https://conference.example/program/#program-llm-serving")
        self.assertIn("Example University", items[0]["summary"])
        self.assertEqual(items[1]["url"], "https://conference.example/program/#event-42")

    def test_parse_github_releases(self):
        payload = json.dumps(
            [
                {
                    "name": "v1.2.0",
                    "tag_name": "v1.2.0",
                    "html_url": "https://github.com/org/repo/releases/tag/v1.2.0",
                    "published_at": "2026-06-14T01:00:00Z",
                    "body": "Adds KV cache transfer.",
                    "draft": False,
                    "prerelease": False,
                }
            ]
        ).encode()
        items = parse_github_releases(payload)
        self.assertEqual(items[0]["title"], "v1.2.0")
        self.assertIn("KV cache", items[0]["summary"])

    def test_parse_html_bold_program_extracts_table_and_list_titles(self):
        body = b"""
        <table><tr><td><b>AIDA: LLM Root Cause Analysis</b><br>Authors</td></tr></table>
        <ul><li><b>AI Query Approximation for Serving</b><br>Authors</li></ul>
        <nav><a><b>Navigation</b></a></nav>
        """
        items = parse_html_bold_program(body, "https://conference.example/accepted/")
        self.assertEqual(
            [item["title"] for item in items],
            ["AIDA: LLM Root Cause Analysis", "AI Query Approximation for Serving"],
        )
        self.assertEqual(
            items[0]["url"],
            "https://conference.example/accepted/#aida-llm-root-cause-analysis",
        )

    def test_parse_html_bold_program_extracts_paragraph_titles(self):
        body = b"<td><p><b>STAR: Decode-Phase Rescheduling for LLM Inference</b></p><p><i><b>Authors:</b></i> A. Author</p></td>"
        items = parse_html_bold_program(body, "https://conference.example/program/")
        self.assertEqual(
            [item["title"] for item in items],
            ["STAR: Decode-Phase Rescheduling for LLM Inference"],
        )

    def test_parse_html_bold_program_extracts_strong_titles(self):
        body = b"<p><strong>LongSpec: Long-Context Lossless Speculative Decoding</strong><br><em>A. Author</em></p>"
        items = parse_html_bold_program(body, "https://conference.example/program/")
        self.assertEqual(items[0]["title"], "LongSpec: Long-Context Lossless Speculative Decoding")


if __name__ == "__main__":
    unittest.main()
