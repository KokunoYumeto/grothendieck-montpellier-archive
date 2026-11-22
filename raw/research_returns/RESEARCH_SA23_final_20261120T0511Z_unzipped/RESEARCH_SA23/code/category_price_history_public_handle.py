"""Retrieve one explicitly advertised public repository link; no endpoint probing."""
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib, json, requests

ROOT = Path(__file__).resolve().parents[1]
URL = "https://kuscholarworks.ku.edu/handle/1808/29639"

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.parts = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("a", "link", "meta"):
            self.links.append({"tag": tag, "attrs": d})
    def handle_data(self, data):
        if data.strip(): self.parts.append(data.strip())

record = {"url": URL, "utc": datetime.now(timezone.utc).isoformat()}
try:
    response = requests.get(URL, timeout=35)
    payload = response.content
    dest = ROOT / "sources/category_price_history_handle.html"
    dest.write_bytes(payload)
    page = Page(); page.feed(response.text)
    (ROOT / "sources/category_price_history_handle.txt").write_text("\n".join(page.parts) + "\n")
    record.update(status=response.status_code, final_url=response.url,
                  history=[{"status": x.status_code, "url": x.url} for x in response.history],
                  size=len(payload), sha256=hashlib.sha256(payload).hexdigest(),
                  path=str(dest.relative_to(ROOT)), advertised_links=page.links)
except Exception as exc:
    record["error"] = repr(exc)
(ROOT / "logs/category_price_history_public_handle.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
