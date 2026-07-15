from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
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
    if source_type == "github_releases":
        return parse_github_releases(body)
    if source_type == "openreview":
        return parse_openreview(body)
    raise ValueError(f"unsupported source type: {source_type}")
