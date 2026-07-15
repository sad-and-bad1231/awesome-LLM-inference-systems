from __future__ import annotations

import hashlib
import json
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from .models import Candidate


_STOPWORDS = {"a", "an", "and", "by", "for", "in", "of", "on", "the", "to", "with"}
_ARXIV_RE = re.compile(
    r"(?:arxiv\.org/(?:abs|pdf)/|arxiv:)(?P<id>(?:\d{4}\.\d{4,5}|[a-z-]+/\d{7}))(?:v\d+)?",
    re.IGNORECASE,
)
_DOI_RE = re.compile(r"(10\.\d{4,9}/[-._;()/:a-z0-9]+)", re.IGNORECASE)


def normalize_title(title: str) -> str:
    words = re.sub(r"[^a-z0-9]+", " ", title.lower()).split()
    return " ".join(word for word in words if word not in _STOPWORDS)


def canonical_url(url: str, preserve_fragment: bool = False) -> str:
    parsed = urlsplit(url.strip())
    query = [
        (key, value)
        for key, value in parse_qsl(parsed.query, keep_blank_values=True)
        if not key.lower().startswith("utm_")
    ]
    path = parsed.path.rstrip("/")
    fragment = parsed.fragment if preserve_fragment else ""
    return urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), path, urlencode(query), fragment)
    )


def candidate_identity(candidate: Candidate) -> str:
    arxiv = _ARXIV_RE.search(candidate.url)
    if arxiv:
        return f"arxiv:{arxiv.group('id').lower()}"
    doi = _DOI_RE.search(candidate.url)
    if doi:
        return f"doi:{doi.group(1).rstrip('.').lower()}"
    url = canonical_url(candidate.url, preserve_fragment=True)
    if url:
        return f"url:{url}"
    return f"title:{normalize_title(candidate.title)}"


def record_identity(title: str, url: str = "", source_ids: list[str] | None = None) -> str:
    """Return a stable cross-store identity for a paper or project record."""
    for source_id in source_ids or []:
        normalized = str(source_id).strip().lower()
        if normalized.startswith(("arxiv:", "doi:", "openreview:")):
            return normalized
    arxiv = _ARXIV_RE.search(url)
    if arxiv:
        return f"arxiv:{arxiv.group('id').lower()}"
    doi = _DOI_RE.search(url)
    if doi:
        return f"doi:{doi.group(1).rstrip('.').lower()}"
    normalized_url = canonical_url(url, preserve_fragment=True)
    if normalized_url:
        return f"url:{normalized_url}"
    return f"title:{normalize_title(title)}"


def candidate_fingerprint(candidate: Candidate) -> str:
    payload = {
        "title": candidate.title.strip(),
        "url": canonical_url(candidate.url, preserve_fragment=True),
        "published": candidate.published.strip(),
        "summary": candidate.summary.strip(),
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()
