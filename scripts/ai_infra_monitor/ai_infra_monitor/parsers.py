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


def parse_html_index(body: bytes, base_url: str) -> list[dict[str, str]]:
    parser = _IndexParser(base_url)
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
        return parse_html_index(body, source["url"])
    if source_type == "github_releases":
        return parse_github_releases(body)
    if source_type == "openreview":
        return parse_openreview(body)
    raise ValueError(f"unsupported source type: {source_type}")
