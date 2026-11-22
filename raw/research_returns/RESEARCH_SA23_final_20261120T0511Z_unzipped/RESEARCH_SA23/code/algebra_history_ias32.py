"""Read public Princeton/IAS catalogue pages for the new correspondence route.

LOC's finding aid returned 403 in the web reader and is deliberately not retried.
All URLs here were opened or returned by the web search/official collections page.
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
    "princeton_collection_index": "https://findingaids.princeton.edu/pacscl/production",
    "ias_ecp_findingaid": "https://www.ias.edu/sites/default/files/library/page/ECP.html",
    "ias_albert_home": "https://albert.ias.edu/",
}

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = None
        self.links = []
        self.forms = []
        self.scripts = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "a" and data.get("href"):
            self.active = {"href": data["href"], "text": ""}
        if tag in ["form", "input"]:
            self.forms.append({"tag": tag, "attrs": data})
        if tag == "script" and data.get("src"):
            self.scripts.append(data["src"])
    def handle_data(self, data):
        if self.active is not None:
            self.active["text"] += data
    def handle_endtag(self, tag):
        if tag == "a" and self.active is not None:
            self.active["text"] = " ".join(self.active["text"].split())
            self.links.append(self.active)
            self.active = None

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
                          file=str(path), scripts=parser.scripts, forms=parser.forms,
                          relevant_links=[x for x in parser.links if any(t in (x["href"]+" "+x["text"]).lower() for t in ["neumann", "groth", "search", "find", "correspond", "member"])])
    except Exception as error:
        result["error"] = repr(error)
    result["seconds"] = time.monotonic() - start
    return result

start = time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(retrieve, URLS.items()))
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "seconds": time.monotonic() - start, "results": results}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_ias32.json").write_text(text + "\n")
print(text)
