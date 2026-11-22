"""Bounded public catalogue lookups, using an actually observed GDZ GET form.

No restricted file downloads, accounts, credentials, purchases, or challenges.
Metadata responses are saved as source material; the log records exact requests.
"""
import concurrent.futures
import datetime
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "literature" / "C_Fujiwara_catalogue_responses"
OUT.mkdir(exist_ok=True)


class PublicHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.words = []
        self.links = []
        self.forms = []
        self.form = None
        self.anchor = None
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "form":
            self.form = dict(attrs, inputs=[])
            self.forms.append(self.form)
        if tag in ("input", "select") and self.form is not None:
            self.form["inputs"].append(attrs)
        if tag == "a":
            self.anchor = {"href": attrs.get("href"), "text": ""}
            self.links.append(self.anchor)

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
        if tag == "form":
            self.form = None
        if tag == "a":
            self.anchor = None

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.words.append(data.strip())
            if self.anchor is not None:
                self.anchor["text"] += data.strip() + " "


def fetch(item):
    name, url = item
    start = time.perf_counter()
    result = {"name": name, "requested_url": url}
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"))
    except urllib.error.HTTPError as error:
        data = error.read()
        result.update(status=error.code, final_url=error.url,
                      content_type=error.headers.get("Content-Type"))
    except Exception as error:
        result.update(error=type(error).__name__ + ": " + str(error),
                      elapsed_seconds=time.perf_counter()-start)
        return result
    result.update(byte_count=len(data), sha256=hashlib.sha256(data).hexdigest(),
                  elapsed_seconds=time.perf_counter()-start)
    path = OUT / (name + ".html")
    path.write_bytes(data)
    result["response_path"] = str(path.relative_to(ROOT))
    parser = PublicHTML()
    parser.feed(data.decode("utf-8", errors="replace"))
    result.update(text="\n".join(parser.words), forms=parser.forms,
                  links=parser.links)
    return result


jobs = [
    ("gdz_journal", "https://gdz.sub.uni-goettingen.de/suche?" +
     urllib.parse.urlencode({"search[q]": '"Duke Mathematical Journal"',
                            "search[searchType]": "metadata"})),
    ("gdz_author", "https://gdz.sub.uni-goettingen.de/suche?" +
     urllib.parse.urlencode({"search[q]": "Fujiwara",
                            "search[searchType]": "metadata"})),
    ("gdz_title", "https://gdz.sub.uni-goettingen.de/suche?" +
     urllib.parse.urlencode({"search[q]": '"tubular neighborhood"',
                            "search[searchType]": "metadata"})),
    ("eudml_home", "https://eudml.org/"),
    ("zvdd_home", "https://www.zvdd.de/"),
    ("wdml_journals", "https://www.math.uni-bielefeld.de/~rehmann/DML/dml_links.html"),
]
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, jobs))
    record = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "form_provenance": "GDZ homepage HTTP200, GET /suche; observed names search[q] and search[searchType], default metadata.",
              "results": results}
    log = ROOT / "logs" / "C_Fujiwara_catalogues_1943.json"
    log.write_text(json.dumps(record, ensure_ascii=False, indent=2))
    for result in results:
        text = result.get("text", "")
        relevant = [line for line in text.splitlines()
                    if any(word in line.lower() for word in
                           ("treffer", "gefunden", "duke", "fujiwara", "tubular", "maintenance", "forbidden"))]
        print(json.dumps({key: result.get(key) for key in
                          ("name", "status", "final_url", "error", "byte_count", "elapsed_seconds")}
                         | {"relevant_lines": relevant[:25], "forms": result.get("forms", [])},
                         ensure_ascii=False))
    print(str(log))
