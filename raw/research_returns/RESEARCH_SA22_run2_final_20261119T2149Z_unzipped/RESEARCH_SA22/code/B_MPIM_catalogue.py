"""Bounded public MPIM catalogue check using observed Advanced Search fields.

No sign-in, author contact, or restricted-file request.  This searches
catalogue metadata; it does not treat records as original theorem text.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import time
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parents[1]
ENDPOINT = "https://archive.mpim-bonn.mpg.de/cgi/search/advanced"

class TextLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.links = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "a" and "href" in d:
            self.links.append(d["href"])
    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(" ".join(data.split()))

def fetch(item):
    name, creator, date = item
    query = {"screen": "Search", "dataset": "archive",
             "creators_name": creator, "date": date,
             "_action_search": "Search"}
    url = ENDPOINT + "?" + urllib.parse.urlencode(query)
    out = {"name": name, "utc": datetime.now(timezone.utc).isoformat(),
           "query": query, "url": url}
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            out.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get("Content-Type"),
                       bytes=len(data), sha256=sha256(data).hexdigest())
        html_path = BASE / "logs" / ("B_MPIM_" + name + ".html")
        html_path.write_bytes(data)
        parser = TextLinks()
        parser.feed(data.decode("utf-8", errors="replace"))
        out["text"] = "\n".join(parser.parts)
        out["links"] = sorted(set(parser.links))
        out["response_path"] = str(html_path.relative_to(BASE))
    except Exception as error:
        out["error"] = repr(error)
    out["elapsed_seconds"] = time.perf_counter() - started
    return out

queries = [("gabber_1981", "Gabber", "1981"),
           ("fujiwara_1992_1995", "Fujiwara", "1992-1995"),
           ("gabber_all_dates", "Gabber", ""),
           ("fujiwara_all_dates", "Fujiwara", "")]
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, queries))
record = {"scope": "Two-author bounded historical catalogue check; no original-text claim",
          "form_fields_record": "logs/B_MPIM_form.json", "results": results}
(BASE / "logs/B_MPIM_catalogue.json").write_text(
    json.dumps(record, indent=2, ensure_ascii=False))
for result in results:
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("text", "links")}, ensure_ascii=False))
    print(result.get("text", "")[:13000])
