from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urljoin


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def _child_text(element: ET.Element, names: tuple[str, ...]) -> str:
    for child in element:
        if _local_name(child.tag) in names:
            return " ".join("".join(child.itertext()).split())
    return ""


def parse_feed(body: bytes, source_id: str = "") -> list[dict[str, str]]:
    root = ET.fromstring(body)
    items: list[dict[str, str]] = []
    for element in root.iter():
        if _local_name(element.tag) not in {"entry", "item"}:
            continue
        title = _child_text(element, ("title",))
        summary = _child_text(element, ("summary", "description", "content"))
        published = _child_text(element, ("published", "updated", "pubdate", "date"))
        url = _child_text(element, ("link", "id", "guid"))
        for child in element:
            if _local_name(child.tag) == "link" and child.attrib.get("href"):
                rel = child.attrib.get("rel", "alternate")
                if rel in {"alternate", ""}:
                    url = child.attrib["href"]
                    break
        if title and url:
            items.append(
                {
                    "title": title,
                    "url": url,
                    "published": published,
                    "summary": summary,
                    "source_id": source_id,
                }
            )
    return items


class _IndexParser(HTMLParser):
    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.current_href = ""
        self.current_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        values = dict(attrs)
        self.current_href = values.get("href") or ""
        self.current_text = []

    def handle_data(self, data: str) -> None:
        if self.current_href:
            self.current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or not self.current_href:
            return
        title = " ".join("".join(self.current_text).split())
        if title and not self.current_href.lower().startswith(("javascript:", "mailto:")):
            self.items.append(
                {
                    "title": title,
                    "url": urljoin(self.base_url, self.current_href),
                    "published": "",
                    "summary": "",
                }
            )
        self.current_href = ""
        self.current_text = []


class _ProgramParser(HTMLParser):
    """Extract paper cards and event anchors from conference program pages."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.depth = 0
        self.capture_kind = ""
        self.capture_depth = 0
        self.capture_text: list[str] = []
        self.pending_title = ""
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        values = dict(attrs)
        if tag.lower() == "a" and values.get("data-event-modal"):
            title = ""
            self.capture_kind = "event"
            self.capture_depth = self.depth
            self.capture_text = []
            self._event_id = values["data-event-modal"]
            return
        if tag.lower() != "div":
            return
        classes = set((values.get("class") or "").split())
        if "paper-title" in classes:
            self.capture_kind = "title"
            self.capture_depth = self.depth
            self.capture_text = []
        elif "paper-authors" in classes:
            self.capture_kind = "authors"
            self.capture_depth = self.depth
            self.capture_text = []

    def handle_data(self, data: str) -> None:
        if self.capture_kind:
            self.capture_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.capture_kind and self.depth == self.capture_depth:
            text = " ".join("".join(self.capture_text).split())
            if self.capture_kind == "title" and text:
                self.pending_title = text
                self.items.append(
                    {
                        "title": text,
                        "url": f"{self.base_url}#{_program_slug(text)}",
                        "published": "",
                        "summary": "",
                    }
                )
            elif self.capture_kind == "authors" and text and self.items:
                self.items[-1]["summary"] = f"Authors: {text}"
            elif self.capture_kind == "event" and text:
                self.items.append(
                    {
                        "title": text,
                        "url": f"{self.base_url}#{self._event_id}",
                        "published": "",
                        "summary": "",
                    }
                )
            self.capture_kind = ""
            self.capture_depth = 0
            self.capture_text = []
        self.depth = max(0, self.depth - 1)


class _BoldProgramParser(HTMLParser):
    """Extract paper titles rendered as bold text inside program blocks."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.stack: list[str] = []
        self.capture = False
        self.capture_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_name = tag.lower()
        parent = self.stack[-1] if self.stack else ""
        self.stack.append(tag_name)
        if tag_name in {"b", "strong"} and parent in {"td", "li", "p"}:
            self.capture = True
            self.capture_text = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.capture_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if tag_name in {"b", "strong"} and self.capture:
            title = " ".join("".join(self.capture_text).split())
            if title:
                self.items.append(
                    {
                        "title": title,
                        "url": f"{self.base_url}#{_program_slug(title)}",
                        "published": "",
                        "summary": "",
                    }
                )
            self.capture = False
            self.capture_text = []
        if self.stack:
            self.stack.pop()


class _HeadingProgramParser(HTMLParser):
    """Extract paper titles rendered as third-level headings."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.depth = 0
        self.capture = False
        self.capture_depth = 0
        self.capture_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        if tag.lower() == "h3":
            self.capture = True
            self.capture_depth = self.depth
            self.capture_text = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.capture_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.capture and tag.lower() == "h3" and self.depth == self.capture_depth:
            title = " ".join("".join(self.capture_text).split())
            if title:
                self.items.append(
                    {
                        "title": title,
                        "url": f"{self.base_url}#{_program_slug(title)}",
                        "published": "",
                        "summary": "",
                    }
                )
            self.capture = False
            self.capture_depth = 0
            self.capture_text = []
        self.depth = max(0, self.depth - 1)


class _ParagraphAnchorParser(HTMLParser):
    """Extract paper titles from anchors contained in paragraph records."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.stack: list[str] = []
        self.capture = False
        self.capture_depth = 0
        self.capture_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_name = tag.lower()
        parent = self.stack[-1] if self.stack else ""
        self.stack.append(tag_name)
        if tag_name == "a" and parent == "p":
            self.capture = True
            self.capture_depth = len(self.stack)
            self.capture_text = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.capture_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if self.capture and tag_name == "a" and len(self.stack) == self.capture_depth:
            title = " ".join("".join(self.capture_text).split())
            if title:
                self.items.append(
                    {
                        "title": title,
                        "url": f"{self.base_url}#{_program_slug(title)}",
                        "published": "",
                        "summary": "",
                    }
                )
            self.capture = False
            self.capture_depth = 0
            self.capture_text = []
        if self.stack:
            self.stack.pop()


class _AuthorParagraphProgramParser(HTMLParser):
    """Extract titles printed as author citations inside paragraph blocks."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.depth = 0
        self.capture = False
        self.capture_depth = 0
        self.capture_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        if tag.lower() == "p":
            self.capture = True
            self.capture_depth = self.depth
            self.capture_text = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.capture_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "p" and self.capture and self.depth == self.capture_depth:
            text = " ".join("".join(self.capture_text).split()).lstrip()
            if text.startswith("<br>"):
                text = text[4:].lstrip()
            if ". " in text:
                title = text.rsplit(". ", 1)[-1].strip()
                if title and title not in {item["title"] for item in self.items}:
                    self.items.append(
                        {
                            "title": title,
                            "url": f"{self.base_url}#{_program_slug(title)}",
                            "published": "",
                            "summary": "",
                        }
                    )
            self.capture = False
            self.capture_depth = 0
            self.capture_text = []
        self.depth = max(0, self.depth - 1)


class _ClassedTitleParser(HTMLParser):
    """Extract titles from elements carrying a configured CSS class."""

    def __init__(self, base_url: str, class_name: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.class_name = class_name
        self.depth = 0
        self.capture = False
        self.capture_depth = 0
        self.capture_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if self.class_name in classes:
            self.capture = True
            self.capture_depth = self.depth
            self.capture_text = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.capture_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.capture and self.depth == self.capture_depth:
            title = " ".join("".join(self.capture_text).split())
            if title and title not in {item["title"] for item in self.items}:
                self.items.append(
                    {
                        "title": title,
                        "url": f"{self.base_url}#{_program_slug(title)}",
                        "published": "",
                        "summary": "",
                    }
                )
            self.capture = False
            self.capture_depth = 0
            self.capture_text = []
        self.depth = max(0, self.depth - 1)


class _LinklingsProgramParser(HTMLParser):
    """Extract presentation titles from Linklings ``ttip_object_info`` slots."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.depth = 0
        self.capture_depth = 0
        self.capture_text: list[str] = []
        self.seen_titles: set[str] = set()
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if (
            tag.lower() == "span"
            and "ttip_object_info" in classes
            and not self.capture_depth
        ):
            self.capture_depth = self.depth
            self.capture_text = []

    def handle_data(self, data: str) -> None:
        if self.capture_depth:
            self.capture_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.capture_depth and self.depth == self.capture_depth:
            title = " ".join("".join(self.capture_text).split())
            if title and title not in self.seen_titles:
                self.seen_titles.add(title)
                self.items.append(
                    {
                        "title": title,
                        "url": f"{self.base_url}#{_program_slug(title)}",
                        "published": "",
                        "summary": "",
                    }
                )
            self.capture_depth = 0
            self.capture_text = []
        self.depth = max(0, self.depth - 1)


class _ICDCSProgramParser(HTMLParser):
    """Extract numbered paper rows from the ICDCS 2026 HTML program tables."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.in_row = False
        self.in_cell = False
        self.cells: list[str] = []
        self.cell_text: list[str] = []
        self.items: list[dict[str, str]] = []
        self.seen_titles: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_name = tag.lower()
        if tag_name == "tr" and not self.in_row:
            self.in_row = True
            self.cells = []
        elif self.in_row and tag_name in {"td", "th"} and not self.in_cell:
            self.in_cell = True
            self.cell_text = []

    def handle_data(self, data: str) -> None:
        if self.in_cell:
            self.cell_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if self.in_cell and tag_name in {"td", "th"}:
            self.cells.append(" ".join("".join(self.cell_text).split()))
            self.in_cell = False
            self.cell_text = []
        if self.in_row and tag_name == "tr":
            self._finish_row()
            self.in_row = False
            self.cells = []

    def _finish_row(self) -> None:
        if len(self.cells) < 3 or not self.cells[1].isdigit():
            return
        source_text = self.cells[2]
        parts = source_text.rsplit(". ", maxsplit=1)
        title = parts[1].strip() if len(parts) == 2 else source_text
        if not title or title in self.seen_titles:
            return
        self.seen_titles.add(title)
        item = {
            "title": title,
            "url": f"{self.base_url}#{_program_slug(title)}",
            "published": "",
            "summary": "",
        }
        if len(parts) == 2 and parts[0].strip():
            item["summary"] = f"Authors: {parts[0].strip()}"
        self.items.append(item)


class _PrefixedProgramParser(HTMLParser):
    """Extract paper titles from tagged program entries such as ``CLD_REG_1``."""

    def __init__(self, base_url: str, prefix: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.prefix = prefix
        self.capture = False
        self.text: list[str] = []
        self.items: list[dict[str, str]] = []
        self.seen_titles: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "em" and not self.capture:
            self.capture = True
            self.text = []

    def handle_data(self, data: str) -> None:
        if self.capture:
            self.text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "em" or not self.capture:
            return
        value = " ".join("".join(self.text).split())
        self.capture = False
        self.text = []
        if not value.startswith(self.prefix):
            return
        title = re.sub(r"^[^:]+:\s*", "", value).strip()
        if not title or title in self.seen_titles:
            return
        self.seen_titles.add(title)
        self.items.append(
            {
                "title": title,
                "url": f"{self.base_url}#{_program_slug(title)}",
                "published": "",
                "summary": "",
            }
        )


class _PaperIdListParser(HTMLParser):
    """Extract titles from list items marked with paper-id and paper-authors spans."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.depth = 0
        self.li_depth = 0
        self.paper_id_depth = 0
        self.authors_depth = 0
        self.saw_paper_id = False
        self.title_text: list[str] = []
        self.author_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag.lower() == "li" and not self.li_depth:
            self.li_depth = self.depth
            self.paper_id_depth = 0
            self.authors_depth = 0
            self.saw_paper_id = False
            self.title_text = []
            self.author_text = []
        elif self.li_depth and "paper-id" in classes:
            self.saw_paper_id = True
            self.paper_id_depth = self.depth
        elif self.li_depth and "paper-authors" in classes:
            self.authors_depth = self.depth

    def handle_data(self, data: str) -> None:
        if not self.li_depth or not self.saw_paper_id:
            return
        if self.authors_depth:
            self.author_text.append(data)
        elif not self.paper_id_depth:
            self.title_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if self.li_depth and tag_name == "span":
            if self.paper_id_depth == self.depth:
                self.paper_id_depth = 0
            if self.authors_depth == self.depth:
                self.authors_depth = 0
        if self.li_depth and tag_name == "li" and self.depth == self.li_depth:
            title = " ".join("".join(self.title_text).split())
            title = re.sub(r"\s+\u2014\s*$", "", title)
            if title and title not in {item["title"] for item in self.items}:
                item = {
                    "title": title,
                    "url": f"{self.base_url}#{_program_slug(title)}",
                    "published": "",
                    "summary": "",
                }
                authors = " ".join("".join(self.author_text).split())
                if authors:
                    item["summary"] = f"Authors: {authors}"
                self.items.append(item)
            self.li_depth = 0
            self.paper_id_depth = 0
            self.authors_depth = 0
            self.saw_paper_id = False
            self.title_text = []
            self.author_text = []
        self.depth = max(0, self.depth - 1)


class _PaperBlockProgramParser(HTMLParser):
    """Extract strong titles from conference blocks carrying the ``paper`` class."""

    def __init__(self, base_url: str):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.depth = 0
        self.paper_depth = 0
        self.title_depth = 0
        self.title_text: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag.lower() == "div" and "paper" in classes and not self.paper_depth:
            self.paper_depth = self.depth
        elif self.paper_depth and tag.lower() == "strong":
            self.title_depth = self.depth
            self.title_text = []

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if self.title_depth and tag_name == "strong" and self.depth == self.title_depth:
            title = " ".join("".join(self.title_text).split())
            if title and title not in {item["title"] for item in self.items}:
                self.items.append(
                    {
                        "title": title,
                        "url": f"{self.base_url}#{_program_slug(title)}",
                        "published": "",
                        "summary": "",
                    }
                )
            self.title_depth = 0
            self.title_text = []
        if self.paper_depth and tag_name == "div" and self.depth == self.paper_depth:
            self.paper_depth = 0
        self.depth = max(0, self.depth - 1)


class _TableTitleProgramParser(HTMLParser):
    """Extract titles from numbered accepted-paper table rows."""

    def __init__(self, base_url: str, title_column: int = 1):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.title_column = title_column
        self.depth = 0
        self.row_depth = 0
        self.cell_depth = 0
        self.cell_text: list[str] = []
        self.cell_href = ""
        self.cells: list[str] = []
        self.cell_links: list[str] = []
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        tag_name = tag.lower()
        if tag_name == "tr" and not self.row_depth:
            self.row_depth = self.depth
            self.cells = []
            self.cell_links = []
        elif tag_name == "td" and self.row_depth and not self.cell_depth:
            self.cell_depth = self.depth
            self.cell_text = []
            self.cell_href = ""
        elif tag_name == "a" and self.cell_depth:
            self.cell_href = dict(attrs).get("href") or ""

    def handle_data(self, data: str) -> None:
        if self.cell_depth:
            self.cell_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if self.cell_depth and tag_name == "td" and self.depth == self.cell_depth:
            self.cells.append(" ".join("".join(self.cell_text).split()))
            self.cell_links.append(self.cell_href)
            self.cell_depth = 0
            self.cell_text = []
            self.cell_href = ""
        if self.row_depth and tag_name == "tr" and self.depth == self.row_depth:
            if (
                len(self.cells) > self.title_column
                and re.fullmatch(r"\d+", self.cells[0])
            ):
                title = self.cells[self.title_column]
                if title and title not in {item["title"] for item in self.items}:
                    href = self.cell_links[self.title_column] if len(self.cell_links) > self.title_column else ""
                    self.items.append(
                        {
                            "title": title,
                            "url": urljoin(self.base_url, href) if href else f"{self.base_url}#{_program_slug(title)}",
                            "published": "",
                            "summary": "",
                        }
                    )
            self.row_depth = 0
            self.cells = []
            self.cell_links = []
        self.depth = max(0, self.depth - 1)


def _program_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:96] or "paper"


def parse_html_index(
    body: bytes, base_url: str, link_prefixes: tuple[str, ...] = ()
) -> list[dict[str, str]]:
    parser = _IndexParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    if not link_prefixes:
        return parser.items
    return [
        item
        for item in parser.items
        if any(item["url"].split("#", 1)[0].startswith(prefix) for prefix in link_prefixes)
    ]


def parse_html_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _ProgramParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_bold_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _BoldProgramParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_heading_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _HeadingProgramParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_paragraph_anchor_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _ParagraphAnchorParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_author_paragraph_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _AuthorParagraphProgramParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_classed_title_program(body: bytes, base_url: str, class_name: str) -> list[dict[str, str]]:
    parser = _ClassedTitleParser(base_url, class_name)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_linklings_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _LinklingsProgramParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_icdcs_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _ICDCSProgramParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_prefixed_program(
    body: bytes, base_url: str, prefix: str
) -> list[dict[str, str]]:
    parser = _PrefixedProgramParser(base_url, prefix)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_paper_id_list(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _PaperIdListParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_dblp_titles(body: bytes, base_url: str) -> list[dict[str, str]]:
    """Extract DBLP titles without traversing the page's navigation lists."""
    text = body.decode("utf-8", errors="replace")
    entry_pattern = re.compile(
        r'<li\b[^>]*class=["\']([^"\']*\bentry\b[^"\']*)["\'][^>]*\bid=["\']([^"\']+)["\'][^>]*>',
        re.IGNORECASE,
    )
    title_pattern = re.compile(
        r'<span\b[^>]*class=["\'][^"\']*\btitle\b[^"\']*["\'][^>]*>(.*?)</span>',
        re.IGNORECASE | re.DOTALL,
    )
    entries = list(entry_pattern.finditer(text))
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, entry in enumerate(entries):
        if not re.search(r"\b(?:inproceedings|incollection|article)\b", entry.group(1)):
            continue
        segment_end = entries[index + 1].start() if index + 1 < len(entries) else len(text)
        title_match = title_pattern.search(text, entry.end(), segment_end)
        if not title_match:
            continue
        title = re.sub(r"<[^>]+>", "", title_match.group(1))
        title = " ".join(unescape(title).split()).rstrip(".")
        if not title or title in seen:
            continue
        seen.add(title)
        fragment = re.sub(r"[^A-Za-z0-9_-]+", "-", entry.group(2)).strip("-")
        items.append(
            {
                "title": title,
                "url": f"{base_url}#{fragment or _program_slug(title)}",
                "published": "",
                "summary": "",
            }
        )
    return items


def parse_html_paper_block_program(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _PaperBlockProgramParser(base_url)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_table_title_program(body: bytes, base_url: str, title_column: int = 1) -> list[dict[str, str]]:
    parser = _TableTitleProgramParser(base_url, title_column)
    parser.feed(body.decode("utf-8", errors="replace"))
    return parser.items


def parse_html_embedded_full_papers(body: bytes, base_url: str) -> list[dict[str, str]]:
    """Extract full-paper titles embedded as escaped HTML in a Next.js page."""
    text = body.decode("utf-8", errors="replace")
    text = re.sub(r"\\u([0-9a-fA-F]{4})", lambda match: chr(int(match.group(1), 16)), text)
    pattern = re.compile(r"<p>\s*\[fp\]\s*<i>(.*?)</i>\s*<br", re.IGNORECASE | re.DOTALL)
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for match in pattern.finditer(text):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = unescape(" ".join(title.split()))
        if not title or title in seen:
            continue
        seen.add(title)
        items.append(
            {
                "title": title,
                "url": f"{base_url}#{_program_slug(title)}",
                "published": "",
                "summary": "",
            }
        )
    return items


def parse_github_releases(body: bytes) -> list[dict[str, str]]:
    payload = json.loads(body.decode("utf-8"))
    items = []
    for release in payload:
        if release.get("draft"):
            continue
        title = release.get("name") or release.get("tag_name") or "Release"
        items.append(
            {
                "title": str(title),
                "url": str(release.get("html_url") or ""),
                "published": str(
                    release.get("published_at") or release.get("created_at") or ""
                ),
                "summary": re.sub(r"\s+", " ", str(release.get("body") or "")).strip(),
            }
        )
    return [item for item in items if item["url"]]


def parse_openreview(body: bytes) -> list[dict[str, str]]:
    payload = json.loads(body.decode("utf-8"))
    notes = payload.get("notes", payload if isinstance(payload, list) else [])
    items = []
    for note in notes:
        content = note.get("content", {})

        def value(name: str) -> str:
            raw = content.get(name, "")
            if isinstance(raw, dict):
                raw = raw.get("value", "")
            return str(raw)

        note_id = note.get("forum") or note.get("id") or ""
        title = value("title")
        if title and note_id:
            items.append(
                {
                    "title": title,
                    "url": f"https://openreview.net/forum?id={note_id}",
                    "published": str(note.get("pdate") or note.get("cdate") or ""),
                    "summary": value("abstract"),
                    "venue": value("venue"),
                }
            )
    return items


def parse_source(source: dict, body: bytes) -> list[dict[str, str]]:
    source_type = source["type"]
    if source_type == "feed":
        return parse_feed(body, source.get("id", ""))
    if source_type == "html_index":
        return parse_html_index(
            body,
            source["url"],
            tuple(source.get("link_prefixes", ())),
        )
    if source_type == "html_program":
        return parse_html_program(body, source["url"])
    if source_type == "html_bold_program":
        return parse_html_bold_program(body, source["url"])
    if source_type == "html_heading_program":
        return parse_html_heading_program(body, source["url"])
    if source_type == "html_paragraph_anchor_program":
        return parse_html_paragraph_anchor_program(body, source["url"])
    if source_type == "html_author_paragraph_program":
        return parse_html_author_paragraph_program(body, source["url"])
    if source_type == "html_classed_title_program":
        return parse_html_classed_title_program(body, source["url"], source.get("title_class", "paper-title"))
    if source_type == "html_linklings_program":
        return parse_html_linklings_program(body, source["url"])
    if source_type == "html_icdcs_program":
        return parse_html_icdcs_program(body, source["url"])
    if source_type == "html_prefixed_program":
        return parse_html_prefixed_program(body, source["url"], source.get("entry_prefix", ""))
    if source_type == "html_paper_id_list":
        return parse_html_paper_id_list(body, source["url"])
    if source_type == "html_dblp_titles":
        return parse_html_dblp_titles(body, source["url"])
    if source_type == "html_paper_block_program":
        return parse_html_paper_block_program(body, source["url"])
    if source_type == "html_table_title_program":
        return parse_html_table_title_program(body, source["url"], int(source.get("title_column", 1)))
    if source_type == "html_embedded_full_papers":
        return parse_html_embedded_full_papers(body, source["url"])
    if source_type == "github_releases":
        return parse_github_releases(body)
    if source_type == "openreview":
        return parse_openreview(body)
    raise ValueError(f"unsupported source type: {source_type}")
