#!/usr/bin/env python3
"""Fail when a local Markdown or HTML link in the root README is missing."""

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"


class HtmlLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"} and value:
                self.links.append(value)


text = README.read_text(encoding="utf-8")
html = HtmlLinks()
html.feed(text)
links = html.links + re.findall(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)", text)

missing = []
for link in links:
    parsed = urlsplit(link)
    if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
        continue
    path = ROOT / unquote(parsed.path)
    if not path.exists():
        missing.append(link)

if missing:
    for link in missing:
        print(f"Missing README link: {link}")
    raise SystemExit(1)

print(f"Checked {len(links)} README links")
