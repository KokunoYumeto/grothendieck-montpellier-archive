"""Bounded public catalogue extension through actually observed RIMS year links."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re
import time
import urllib.request

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "literature" / "B_Fujiwara_RIMS_1993_1995"
OUT.mkdir(parents=True, exist_ok=True)


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.ignored = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.ignored += 1
        if tag in ("p", "br", "div", "dt", "dd", "h1", "h2", "h3", "li"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.ignored = max(0, self.ignored - 1)
        if tag in ("p", "div", "dt", "dd", "li"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.ignored:
            self.parts.append(data)


def fetch(year):
    url = f"https://www.kurims.kyoto-u.ac.jp/preprint/preprint_y{year}.html"
    rec = {
        "year": year,
        "url": url,
        "observed_link_source": "turn347570545view1",
        "observed_link_id": {1993: 34, 1994: 33, 1995: 32}[year],
        "started_utc": datetime.now(timezone.utc).isoformat(),
    }
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            data = response.read()
            rec.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get("Content-Type"))
        rec.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        (OUT / f"{year}.html").write_bytes(data)
        parser = Text()
        parser.feed(data.decode("utf-8", "replace"))
        text = "\n".join(line.strip() for line in "".join(parser.parts).splitlines()
                         if line.strip())
        (OUT / f"{year}.txt").write_text(text)
        body = text.split(f"RIMS Preprints published in {year}", 1)[-1]
        rec["record_ids"] = list(dict.fromkeys(re.findall(r"RIMS-\d+", body)))
        rec["record_count"] = len(rec["record_ids"])
        rec["term_matches"] = {
            term: [line for line in body.splitlines()
                   if term.lower() in line.lower()]
            for term in ("Fujiwara", "藤原", "tubular", "neighborhood",
                         "neighbourhood")
        }
        rec["text_path"] = str((OUT / f"{year}.txt").relative_to(BASE))
    except Exception as exc:
        rec["error"] = f"{type(exc).__name__}: {exc}"
    rec["elapsed_seconds"] = time.perf_counter() - started
    rec["completed_utc"] = datetime.now(timezone.utc).isoformat()
    return rec


with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, (1993, 1994, 1995)))
report = {
    "completed_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Three previously unsubmitted observed official year-list links; "
             "incremental extension of the prior1992 RIMS check, not a new institution",
    "results": results,
    "original_theorem_passage_obtained": False,
}
(BASE / "logs" / "B_Fujiwara_RIMS_1993_1995.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False) + "\n"
)
print(json.dumps(report, indent=2, ensure_ascii=False))
