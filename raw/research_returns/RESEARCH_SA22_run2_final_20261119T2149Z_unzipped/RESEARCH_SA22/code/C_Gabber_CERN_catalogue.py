#!/usr/bin/env python3
"""Bounded ordinary public CERN catalogue check for the requested Gabber original.

The first invocation reads the actually opened Advanced Search form. Queries
are supplied only after its fields have been inspected. No account, hidden
endpoint, restricted full text, challenge-solving, or repeated blocked request.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "literature/C_Gabber_CERN"
LOG = ROOT / "logs/C_Gabber_CERN_catalogue.json"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms, self.text, self.links = [], [], []
        self.form = self.select = None
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "form":
            self.form = {"attributes": a, "controls": []}
            self.forms.append(self.form)
        if tag in ("input", "select", "button") and self.form is not None:
            c = {"tag": tag, **a}
            self.form["controls"].append(c)
            if tag == "select":
                c["options"] = []
                self.select = c
        if tag == "option" and self.select is not None:
            self.select["options"].append(a)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag == "form":
            self.form = None
        if tag == "select":
            self.select = None
    def handle_data(self, text):
        if not self.skip and text.strip():
            self.text.append(" ".join(text.split()))


def get(job):
    name, url = job
    start = time.perf_counter()
    record = {"name": name, "url": url, "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Research-SA22/1.0"}), timeout=25) as response:
            raw = response.read()
            record.update(status=response.status, final_url=response.url, content_type=response.headers.get("Content-Type"))
        DEST.mkdir(exist_ok=True)
        path = DEST / (name + ".html")
        path.write_bytes(raw)
        page = Page()
        page.feed(raw.decode("utf-8", errors="replace"))
        record.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(), saved=str(path.relative_to(ROOT)), text="\n".join(page.text), forms=page.forms, links=sorted(set(page.links)))
    except Exception as error:
        record.update(error=type(error).__name__, message=str(error))
    record.update(finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), elapsed_seconds=time.perf_counter()-start)
    return record


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=("form", "queries"))
    parser.add_argument("--queries-json", help="Exact observed-form query definitions, after inspecting the saved form")
    args = parser.parse_args()
    start = time.perf_counter()
    log = json.loads(LOG.read_text()) if LOG.exists() else {"scope": "Bounded public CERN catalogue metadata; original article reading is not inferred", "phases": []}
    if args.phase == "form":
        assert not any(p["phase"] == "form" for p in log["phases"]), "Form already fetched; no automatic retry"
        jobs = [("advanced_form", "https://cds.cern.ch/?as=1&ln=en")]
    else:
        assert args.queries_json and any(p["phase"] == "form" for p in log["phases"])
        assert not any(p["phase"] == "queries" for p in log["phases"]), "Bounded queries already made; no automatic retry"
        queries = json.loads(Path(args.queries_json).read_text())
        assert len(queries) <= 3
        jobs = [(q["name"], q["url"]) for q in queries]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(get, jobs))
    phase = {"phase": args.phase, "request_count": len(jobs), "results": results, "elapsed_seconds": time.perf_counter()-start, "completed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    log["phases"].append(phase)
    LOG.write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(phase, ensure_ascii=False, indent=2))
