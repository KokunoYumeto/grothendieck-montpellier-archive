"""Retrieve or inventory primary sources considered for F13.5/F13.6.

Run without arguments to inventory the already retrieved files; pass --fetch
to reproduce the public PDF downloads and their pdftotext extraction. The
JSTOR entry is deliberately marked unavailable; no PDF was obtained.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess
import time
import urllib.request

WORK = Path(__file__).resolve().parents[1]
SOURCES = [
    ("Yatagawa2020", "https://arxiv.org/pdf/1712.09234", "Opened arXiv v1, 26 December 2017; pp8–9 used in F13g; geometric results finite-type only."),
    ("Oi2014", "https://www.jstage.jst.go.jp/article/jsiaml/6/0/6_33/_pdf", "Opened full primary PDF, JSIAM Letters6(2014)33–36; algorithm and local r_x invariant, not used as a complete-local Betti theorem."),
    ("Oi2015III", "https://arxiv.org/pdf/1507.00097", "Opened full arXiv v1, 1 July 2015; Theorem5.1 p4 gives local order-p Kato invariant upper bounds, finite-type surface setting."),
    ("ArtinSchreierCoveringsThesis", "https://ir.library.osaka-u.ac.jp/repo/ouka/all/3328/09050_Dissertation.pdf", "Opened university scan of Yoshifumi Takeda, J.Math.Soc.Japan41(1989)415–435; complete local calculations in section2, globally smooth projective surface assumptions."),
]
parser = argparse.ArgumentParser()
parser.add_argument("--fetch", action="store_true")
args = parser.parse_args()
start = time.perf_counter()
records = []
for stem, url, note in SOURCES:
    path = WORK / "sources" / (stem + ".pdf")
    if args.fetch:
        blob = urllib.request.urlopen(url, timeout=30).read()
        if not blob.startswith(b"%PDF"):
            raise RuntimeError("Expected a PDF at " + url)
        path.write_bytes(blob)
        subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], check=True)
    blob = path.read_bytes()
    records.append(dict(path=str(path), url=url, bytes=len(blob), sha256=hashlib.sha256(blob).hexdigest(), extracted_text=path.with_suffix(".txt").exists(), status=note))
records.append(dict(url="https://www.jstor.org/stable/pdf/2375001.pdf", title="Kato1994 Class field theory, D-modules, and ramification on higher-dimensional schemes I", status="Full primary text NOT opened: web redirected to empty metadata and urllib returned 3038-byte HTML rather than PDF. Later papers' citations do not count as opening Kato's text."))
result = dict(timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(), mode="fetch" if args.fetch else "inventory", runtime_seconds=time.perf_counter()-start, records=records)
(WORK / "output" / "cleanup_sources.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
