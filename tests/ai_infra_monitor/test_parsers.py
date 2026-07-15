import json
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.parsers import (
    parse_feed,
    parse_github_releases,
    parse_html_bold_program,
    parse_html_author_paragraph_program,
    parse_html_classed_title_program,
    parse_html_heading_program,
    parse_html_embedded_full_papers,
    parse_html_paragraph_anchor_program,
    parse_html_index,
    parse_html_paper_id_list,
    parse_html_paper_block_program,
    parse_html_table_title_program,
    parse_html_dblp_titles,
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

    def test_parse_html_heading_program_extracts_h3_titles(self):
        body = b"<h2>Track</h2><h3>M-LoRA: Efficient Serving for Concurrent LoRA Adapters</h3><h4>Authors</h4>"
        items = parse_html_heading_program(body, "https://conference.example/accepted/")
        self.assertEqual(items[0]["title"], "M-LoRA: Efficient Serving for Concurrent LoRA Adapters")

    def test_parse_html_paragraph_anchor_program_extracts_paper_links(self):
        body = b"<nav><a>Navigation</a></nav><p><a href=''>PreMoE: Proactive Inference for Efficient MoE</a><br><em>A. Author</em></p>"
        items = parse_html_paragraph_anchor_program(body, "https://conference.example/accepted/")
        self.assertEqual(items[0]["title"], "PreMoE: Proactive Inference for Efficient MoE")

    def test_parse_html_embedded_full_papers_decodes_nextjs_fragments(self):
        body = br'<script>\u003cp\u003e[fp] \u003ci\u003eSRAG: A Lightweight RAG Serving System\u003c/i\u003e\u003cbr /\u003eAuthors\u003c/p\u003e</script>'
        items = parse_html_embedded_full_papers(body, "https://conference.example/accepted")
        self.assertEqual(items[0]["title"], "SRAG: A Lightweight RAG Serving System")

    def test_parse_html_author_paragraph_program_strips_author_prefix(self):
        body = b"<div><p>Jane Doe and John Smith. Efficient LLM Serving at the Edge</p></div>"
        items = parse_html_author_paragraph_program(body, "https://conference.example/accepted/")
        self.assertEqual(items[0]["title"], "Efficient LLM Serving at the Edge")

    def test_parse_html_classed_title_program(self):
        body = b'<li><span class="paper-title">Paged KV Cache Serving</span><span class="paper-authors">A. Author</span></li>'
        items = parse_html_classed_title_program(
            body, "https://conference.example/accepted/", "paper-title"
        )
        self.assertEqual(items[0]["title"], "Paged KV Cache Serving")

    def test_parse_html_paper_id_list_extracts_title_without_authors(self):
        body = b"""
        <ul>
          <li><span class='paper-id'>(rfp0001)</span> DeepServe: Efficient LLM Serving
          <span class='paper-authors'>A. Author and B. Author</span></li>
        </ul>
        """
        items = parse_html_paper_id_list(body, "https://conference.example/accepted/")
        self.assertEqual(items[0]["title"], "DeepServe: Efficient LLM Serving")
        self.assertEqual(
            items[0]["url"],
            "https://conference.example/accepted/#deepserve-efficient-llm-serving",
        )

    def test_parse_html_dblp_titles_ignores_navigation(self):
        body = b"""
        <a href='/'>Navigation title</a>
        <li class='entry inproceedings' id='conf/demo/Paper26'>
          <cite><span class='title' itemprop='name'>Paged Serving Systems.</span></cite>
        </li>
        """
        items = parse_html_dblp_titles(body, "https://dblp.org/db/conf/demo/demo2026.html")
        self.assertEqual([item["title"] for item in items], ["Paged Serving Systems"])
        self.assertEqual(
            items[0]["url"],
            "https://dblp.org/db/conf/demo/demo2026.html#conf-demo-Paper26",
        )

    def test_parse_html_paper_block_program_extracts_strong_title(self):
        body = b"""
        <div class='paper'><div><strong>AgentPlan: Planning with LLMs</strong></div>
        <div>A. Author and B. Author</div></div>
        """
        items = parse_html_paper_block_program(body, "https://conference.example/accepted/")
        self.assertEqual(items[0]["title"], "AgentPlan: Planning with LLMs")

    def test_parse_html_table_title_program_extracts_numbered_rows(self):
        body = b"""
        <table><tr><th>Paper Number</th><th>Paper Title</th></tr>
        <tr><td>10540</td><td>Multi-Agent Speech Workflow</td></tr>
        <tr><td>bad</td><td>Navigation Row</td></tr></table>
        """
        items = parse_html_table_title_program(body, "https://conference.example/accepted/")
        self.assertEqual([item["title"] for item in items], ["Multi-Agent Speech Workflow"])

    def test_parse_html_table_title_program_supports_title_column_and_links(self):
        body = b"""
        <table><tr><th>ID</th><th>Session</th><th>Title</th><th>Authors</th></tr>
        <tr><td>1</td><td>Agents</td><td><a href='/papers/1/'>RSS Agent Runtime</a></td><td>A. Author</td></tr></table>
        """
        items = parse_html_table_title_program(
            body, "https://conference.example/accepted/", title_column=2
        )
        self.assertEqual(items[0]["title"], "RSS Agent Runtime")
        self.assertEqual(items[0]["url"], "https://conference.example/papers/1/")


if __name__ == "__main__":
    unittest.main()
