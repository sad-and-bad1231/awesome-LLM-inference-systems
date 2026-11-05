#!/usr/bin/env python3
"""Offline Markdown quality checks. No crawler, generated bibliography, or dependencies.

Usage: python3 scripts/check_catalog.py [--root .]
"""
import argparse
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

TOPICS = ("kernels-compilers", "kv-cache-memory", "decoding-acceleration",
          "quantization-compression", "moe-sparse-execution", "runtime-scheduling",
          "distributed-serving", "benchmarking-analysis")
ROW = re.compile(r"^\|\s*(?:19|20)\d\d\s*\|")
GROUP = re.compile(r"^### .+? \((\d+)\)\s*$", re.M)
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^\n]+?)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")


def anchors(markdown):
    seen = Counter()
    result = set()
    for line in markdown.splitlines():
        match = HEADING.match(line)
        if not match:
            continue
        title = re.sub(r"!?\[([^]]+)\]\([^)]+\)", r"\1", match.group(1))
        title = re.sub(r"<[^>]+>|[\x60*_~]", "", title).lower().strip()
        title = "".join(c for c in title if c in "-_ " or unicodedata.category(c)[0] not in "PS")
        slug = title.replace(" ", "-")
        idx = seen[slug]
        result.add(slug if idx == 0 else f"{slug}-{idx}")
        seen[slug] += 1
    return result


def section(text, start, end=None):
    a = text.index(start)
    b = text.find(end, a + len(start)) if end else -1
    return text[a:] if b == -1 else text[a:b]


def first_source_id(row):
    match = LINK.search(row)
    if not match:
        return None
    url = urlsplit(match.group(1).strip().split(' "')[0])
    path = unquote(url.path).rstrip("/")
    arxiv = re.search(r"/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?$", path)
    if url.hostname and url.hostname.endswith("arxiv.org") and arxiv:
        return "arxiv:" + arxiv.group(1)
    if url.hostname in ("doi.org", "dx.doi.org"):
        return "doi:" + path.lower().lstrip("/")
    return "url:" + url.netloc.lower() + path.lower()


def check(root):
    issues = []
    docs = {p.relative_to(root).as_posix(): p.read_text(encoding="utf-8")
            for p in sorted(root.rglob("*.md")) if ".git" not in p.parts}
    required = ["README.md", "topics/README.md", "organizations/README.md", "communities/README.md"]
    for path in required:
        if path not in docs:
            issues.append(f"missing {path}")
    if issues:
        return issues
    topic_index = docs["topics/README.md"]
    aliases = defaultdict(list)
    total = 0
    n_groups = 0
    for name in TOPICS:
        path = f"topics/{name}.md"
        if path not in docs:
            issues.append(f"missing {path}")
            continue
        content = docs[path]
        rows = [line for line in content.splitlines() if ROW.match(line)]
        total += len(rows)
        stated = re.search(r"^## Papers \((\d+)\)$", content, re.M)
        if not stated or int(stated.group(1)) != len(rows):
            issues.append(f"{path}: paper heading != {len(rows)} rows")
        groups = [int(n) for n in GROUP.findall(content)]
        n_groups += len(groups)
        if sum(groups) != len(rows):
            issues.append(f"{path}: {sum(groups)} subgroup papers != {len(rows)} rows")
        item = re.search(r"^\| \[[^\]]+\]\(" + re.escape(name) +
                         r"\.md\) \|\s*(\d+)\s*\|", topic_index, re.M)
        if not item or int(item.group(1)) != len(rows):
            issues.append(f"{path}: topic index count != {len(rows)} rows")
        for row in rows:
            uid = first_source_id(row)
            if uid:
                aliases[uid].append(path)
    index_total = re.search(r"^\| \*\*Total\*\* \| \*\*(\d+)\*\*", topic_index, re.M)
    if not index_total or int(index_total.group(1)) != total:
        issues.append(f"topic index total != {total}")
    if n_groups != 44:
        issues.append(f"expected 44 topic directions, got {n_groups}")
    for uid, where in sorted(aliases.items()):
        if len(where) > 1:
            issues.append(f"duplicate first-source identity: {uid} ({', '.join(where)})")

    foundations = section(docs["README.md"], "## Foundational and influential papers", "## Contributing")
    n_found = sum(x.startswith("| [") for x in foundations.splitlines())
    if n_found != 30:
        issues.append(f"expected 30 foundation rows, got {n_found}")
    org = docs["organizations/README.md"]
    cn = sum(x.startswith("| [") for x in section(org, "## China", "## United States").splitlines())
    us = sum(x.startswith("| [") for x in section(org, "## United States", "## November").splitlines())
    if (cn, us) != (19, 30):
        issues.append(f"organization index expected 19/30, got {cn}/{us}")
    community = docs["communities/README.md"]
    expected = (24, 11, 9, 23, 9)
    observed = []
    for i in range(1, 6):
        match = re.search(rf"^### {i}\. .+$", community, re.M)
        if not match:
            issues.append(f"missing OSS execution group {i}")
            continue
        remainder = community[match.end():]
        stop = re.search(r"^#{2,3} ", remainder, re.M)
        group = remainder[:stop.start()] if stop else remainder
        observed.append(sum(x.startswith("| [") for x in group.splitlines()))
    if tuple(observed) != expected:
        issues.append(f"OSS groups expected {expected}, got {observed}")

    lookup = {p: anchors(s) for p, s in docs.items()}
    for origin, content in docs.items():
        for match in LINK.finditer(content):
            raw = match.group(1).strip().split(' "')[0].strip("<>")
            if not raw or raw.startswith(("https://", "http://", "mailto:", "data:")):
                continue
            url = urlsplit(raw)
            if url.scheme or url.netloc:
                continue
            dest = (root / origin).parent / unquote(url.path) if url.path else root / origin
            resolved = dest.resolve()
            try:
                target = resolved.relative_to(root).as_posix()
            except ValueError:
                issues.append(f"{origin}: link outside repository: {raw}")
                continue
            if target not in docs:
                if resolved.is_dir():
                    continue
                issues.append(f"{origin}: missing internal link target: {raw}")
            elif url.fragment and unquote(url.fragment).lower() not in lookup[target]:
                issues.append(f"{origin}: invalid internal heading anchor: {raw}")
    print(f"Checked {len(docs)} Markdown files, {total} papers, {n_groups} directions, "
          f"{n_found} foundations, {cn+us} organizations, {sum(observed)} OSS repos")
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    root = parser.parse_args().root.resolve()
    errors = check(root)
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    print("PASS" if not errors else f"FAIL ({len(errors)} issues)")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
