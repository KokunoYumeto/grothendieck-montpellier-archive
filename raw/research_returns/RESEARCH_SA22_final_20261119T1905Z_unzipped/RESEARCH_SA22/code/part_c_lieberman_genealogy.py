"""Follow an actually advertised public genealogy link, without access workarounds."""
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from time import perf_counter
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import urlopen
import json

BASE = Path(__file__).resolve().parent

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.texts = []
        self.active = None
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.active = [dict(attrs).get("href", ""), ""]
    def handle_data(self, data):
        self.texts.append(data)
        if self.active is not None:
            self.active[1] += data
    def handle_endtag(self, tag):
        if tag == "a" and self.active is not None:
            self.links.append(self.active)
            self.active = None

def fetch(url):
    start = perf_counter()
    row = {"url": url}
    try:
        with urlopen(url, timeout=45) as response:
            raw = response.read()
            row.update(status=response.status, final_url=response.url,
                       bytes=len(raw), sha256=sha256(raw).hexdigest())
        parser = Page()
        parser.feed(raw.decode("utf-8", errors="replace"))
        text = " ".join(" ".join(parser.texts).split())
        row["text"] = text[:14000]
        row["links"] = parser.links
        row["blocked"] = any(term in text.lower() for term in
                             ("verify you are human", "access denied", "captcha", "turnstile"))
    except (HTTPError, URLError, TimeoutError) as exc:
        row.update(error=repr(exc), status=getattr(exc, "code", None))
    row["elapsed_seconds"] = perf_counter() - start
    return row

started = datetime.now(timezone.utc).isoformat()
t0 = perf_counter()
rows = [fetch("https://www.mathgenealogy.org/id.php?id=36820")]
if rows[0].get("status") == 200 and not rows[0].get("blocked"):
    matches = [href for href, label in rows[0].get("links", [])
               if "Lieberman" in label]
    if matches:
        rows.append(fetch(urljoin(rows[0]["final_url"], matches[0])))
result = {"started_utc": started, "elapsed_seconds": perf_counter() - t0,
          "scope": "At most two ordinary public metadata pages, using an actually observed genealogy link and then an advertised advisor link; stop on access denial.",
          "requests": rows}
out = json.dumps(result, ensure_ascii=False, indent=2)
(BASE / "part_c_lieberman_genealogy_output.json").write_text(out + "\n")
(BASE / "part_c_lieberman_genealogy_output.txt").write_text(out + "\n")
print(out)
