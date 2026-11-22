"""Download only public file links actually advertised on the IA item page."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import time
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parents[1]
HTML = BASE / "literature/B_Gabriel_IA_volume_details.html"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href", "")
            if href.startswith("/download/"):
                self.links.append(href)


parser = Links()
parser.feed(HTML.read_text())
targets = {}
for href in parser.links:
    if href.endswith(".pdf"):
        targets["pdf"] = urllib.parse.urljoin("https://archive.org", href)
    if href.endswith("_djvu.txt"):
        targets["text"] = urllib.parse.urljoin("https://archive.org", href)


def fetch(item):
    label, url = item
    result = {"label": label, "url": url,
              "started_utc": datetime.now(timezone.utc).isoformat(),
              "provenance": "Observed download anchor in saved ordinary item HTML; "
                            "public metadata marks no file private and "
                            "item page has no restriction/borrow requirement"}
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=50) as response:
            data = response.read()
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"))
        result.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        if label == "pdf" and not data.startswith(b"%PDF"):
            result["accepted"] = False
            result["reason"] = "Not PDF bytes; not saved as original."
        else:
            path = BASE / ("literature/B_Gabriel1932_volume.pdf" if label == "pdf"
                           else "literature/B_Gabriel1932_volume.txt")
            path.write_bytes(data)
            result.update(accepted=True, local_path=str(path.relative_to(BASE)))
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
    result["elapsed_seconds"] = time.perf_counter() - started
    result["completed_utc"] = datetime.now(timezone.utc).isoformat()
    return result


with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(fetch, targets.items()))
report = {"completed_utc": datetime.now(timezone.utc).isoformat(),
          "observed_download_links": targets, "results": results}
(BASE / "logs/B_Gabriel_IA_volume_fetch.json").write_text(
    json.dumps(report, indent=2) + "\n"
)
print(json.dumps(report, indent=2))
