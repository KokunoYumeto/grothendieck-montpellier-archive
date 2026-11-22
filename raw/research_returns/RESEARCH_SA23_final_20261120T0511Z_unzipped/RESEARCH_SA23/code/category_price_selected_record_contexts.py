"""Preserve the targeted Price finding-aid records for actual human reading."""
from pathlib import Path
from html.parser import HTMLParser
import json

ROOT = Path(__file__).resolve().parents[1]
IDS = {127497, 127498, 127500, 127538, 127639, 127648, 127649, 127650, 127651}

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        if data.strip():
            self.parts.append(data.strip())

out = []
for path in sorted((ROOT / "sources").glob("category_aronszajn_price_wp_*.json")):
    for uri, html in json.loads(path.read_text()).items():
        if int(uri.rsplit("/", 1)[1]) in IDS:
            parser = Text()
            parser.feed(html)
            out.append("https://archives.lib.ku.edu" + uri + "\n" + "\n".join(parser.parts))
result = "\n\n".join(out) + "\n"
(ROOT / "notes/category_price_selected_record_contexts.txt").write_text(result)
print(result)
