"""Fetch two publicly advertised archival search surfaces.

The ETH archive's official page links to its virtual reading room and to
e-manuscripta. The latter's observed quick-search URL supplies the query schema.
"""
import concurrent.futures
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import time
import urllib.request

BASE = Path(__file__).resolve().parents[1]
URLS = {
    "eth_virtual_reading_public": "https://vls.hsa.ethz.ch/client/",
    "emanuscripta_grothendieck": "https://www.e-manuscripta.ch/search/quick?query=Grothendieck",
}

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.links = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "script" and data.get("src"):
            self.scripts.append(data["src"])
        if tag == "a" and data.get("href"):
            self.links.append(data["href"])

def retrieve(item):
    label, url = item
    start = time.monotonic()
    result = {"label": label, "url": url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            path = BASE / "sources" / ("algebra_history_" + label + ".html")
            path.write_bytes(data)
            parser = Links()
            parser.feed(data.decode("utf-8", errors="replace"))
            result.update(status=response.status, final_url=response.url,
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                          file=str(path), scripts=parser.scripts, links=parser.links)
    except Exception as error:
        result["error"] = repr(error)
    result["seconds"] = time.monotonic() - start
    return result

start = time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(retrieve, URLS.items()))
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "seconds": time.monotonic() - start, "results": results}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_weyl23.json").write_text(text + "\n")
print(text)
