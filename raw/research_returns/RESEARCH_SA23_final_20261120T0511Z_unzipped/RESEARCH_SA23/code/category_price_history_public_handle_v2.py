"""Stdlib retrieval of the one advertised KU history handle; no endpoint probing."""
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import urlparse
import hashlib, json, urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = "https://kuscholarworks.ku.edu/handle/1808/29639"

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ("a", "link", "meta"):
            self.links.append({"tag": tag, "attrs": dict(attrs)})
    def handle_data(self, data):
        if data.strip(): self.parts.append(data.strip())

record = {"url": URL, "utc": datetime.now(timezone.utc).isoformat(), "redirects": []}
class PublicKU(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        record["redirects"].append({"status": code, "from": req.full_url, "to": newurl})
        if urlparse(newurl).hostname != "kuscholarworks.ku.edu":
            raise ValueError("Unexpected redirect host; stopped")
        return super().redirect_request(req, fp, code, msg, headers, newurl)

try:
    with urllib.request.build_opener(PublicKU).open(URL, timeout=35) as response:
        payload = response.read()
        record.update(status=response.status, final_url=response.url)
    dest = ROOT / "sources/category_price_history_handle.html"
    dest.write_bytes(payload)
    page = Page(); page.feed(payload.decode("utf-8", errors="replace"))
    (ROOT / "sources/category_price_history_handle.txt").write_text("\n".join(page.parts) + "\n")
    record.update(size=len(payload), sha256=hashlib.sha256(payload).hexdigest(),
                  path=str(dest.relative_to(ROOT)), advertised_links=page.links)
except Exception as exc:
    record["error"] = repr(exc)
(ROOT / "logs/category_price_history_public_handle_v2.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
