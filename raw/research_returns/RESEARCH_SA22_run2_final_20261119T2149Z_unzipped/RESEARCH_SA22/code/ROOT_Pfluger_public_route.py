"""Bounded ordinary public DOI/Crossref retrieval for requested Pfluger1960."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "doi": "https://doi.org/10.18311/JIMS/1960/16922",
    "crossref": "https://api.crossref.org/works/10.18311/JIMS/1960/16922",
}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.links = [], []
        self.current_link = None
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.current_link = {"text": "", "href": href}
                self.links.append(self.current_link)
    def handle_endtag(self, tag):
        if tag == "a":
            self.current_link = None
    def handle_data(self, data):
        self.parts.append(data)
        if self.current_link is not None:
            self.current_link["text"] += data


def fetch(item):
    label, url = item
    result = {"label": label, "url": url,
              "started_utc": datetime.now(timezone.utc).isoformat()}
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("content-type"),
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        suffix = ".json" if label == "crossref" else ".html"
        path = ROOT / "literature" / ("ROOT_Pfluger1960_" + label + suffix)
        path.write_bytes(data)
        result["local_path"] = str(path.relative_to(ROOT))
        if label == "crossref":
            result["record"] = json.loads(data)
        else:
            parser = PageParser()
            parser.feed(data.decode("utf-8", "replace"))
            result["text"] = " ".join(part.strip() for part in parser.parts if part.strip())
            result["links"] = parser.links
    except urllib.error.HTTPError as error:
        data = error.read()
        result.update(status=error.code, final_url=error.url, error=str(error),
                      bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                      response_text=data.decode("utf-8", "replace"))
    except Exception as error:
        result["error"] = repr(error)
    result["seconds"] = time.perf_counter() - start
    result["completed_utc"] = datetime.now(timezone.utc).isoformat()
    return result


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows = list(pool.map(fetch, TARGETS.items()))
    (ROOT / "logs/ROOT_Pfluger_public_route.json").write_text(json.dumps(rows, indent=2) + "\n")
    for row in rows:
        brief = {k: v for k, v in row.items() if k not in {"record", "response_text", "text", "links"}}
        if "record" in row:
            record = row["record"].get("message", {})
            brief["primary_resource"] = record.get("resource")
            brief["content_links"] = record.get("link")
            brief["title"] = record.get("title")
        if "text" in row:
            brief["text"] = row["text"]
            brief["links"] = row["links"]
        print(json.dumps(brief, indent=2))
