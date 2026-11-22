"""Bounded Gabber/Israel catalogue check using the observed public GDZ form.

Prior C catalogue logs cover Duke/Fujiwara, not these three queries.
No publisher retries, account actions, protected downloads or challenges.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "literature/B_Gabber_GDZ_catalogue"
OUT.mkdir(exist_ok=True)


class PublicHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.words, self.links, self.forms = [], [], []
        self.anchor = self.form = None
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
    name, query = item
    url = "https://gdz.sub.uni-goettingen.de/suche?" + urllib.parse.urlencode(
        {"search[q]": query, "search[searchType]": "metadata"})
    row = {"name": name, "query": query, "requested_url": url,
           "started_utc": datetime.now(timezone.utc).isoformat()}
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get("Content-Type"))
    except urllib.error.HTTPError as error:
        data = error.read()
        row.update(status=error.code, final_url=error.url, error=str(error))
    except Exception as error:
        row.update(error=repr(error), elapsed_seconds=time.perf_counter()-started,
                   finished_utc=datetime.now(timezone.utc).isoformat())
        return row
    destination = OUT / (name + ".html")
    destination.write_bytes(data)
    parser = PublicHTML()
    parser.feed(data.decode("utf-8", errors="replace"))
    row.update(byte_count=len(data), sha256=sha256(data).hexdigest(),
               response_path=str(destination.relative_to(BASE)),
               text="\n".join(parser.words), links=parser.links, forms=parser.forms,
               elapsed_seconds=time.perf_counter()-started,
               finished_utc=datetime.now(timezone.utc).isoformat())
    return row


if __name__ == "__main__":
    jobs = [("journal", '"Israel Journal of Mathematics"'),
            ("exact_article", '"Affine analog of the proper base change theorem"'),
            ("author_control", "Gabber")]
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, jobs))
    wdml_path = BASE / "literature/C_Fujiwara_catalogue_responses/wdml_journals.html"
    wdml = wdml_path.read_bytes()
    record = {"completed_utc": datetime.now(timezone.utc).isoformat(),
              "form_provenance": "Actual GDZ GET /suche form with search[q] and search[searchType]=metadata, inspected in C_Fujiwara_catalogues_1943.json and current GDZ homepage.",
              "prior_scope": "C actual forms used Duke, Fujiwara and tubular neighborhood; earlier B GDZ appearances were external search-engine citation hits, not these catalogue submissions.",
              "results": results,
              "wdml_existing_response": {
                  "source": "https://www.math.uni-bielefeld.de/~rehmann/DML/dml_links.html",
                  "path": str(wdml_path.relative_to(BASE)),
                  "sha256": sha256(wdml).hexdigest(),
                  "byte_count": len(wdml),
                  "case_insensitive_Israel_occurrences": wdml.lower().count(b"israel"),
                  "scope": "Reused complete public response fetched by C today, and independently opened/find-checked by B; no claim of exhaustive global holdings."}}
    (BASE / "logs/B_Gabber_GDZ_catalogue.json").write_text(json.dumps(record, indent=2, ensure_ascii=False))
    for row in results:
        print(json.dumps({k: row.get(k) for k in ("name", "query", "status", "byte_count", "elapsed_seconds", "error")} | {"text": row.get("text", "")}, ensure_ascii=False))
