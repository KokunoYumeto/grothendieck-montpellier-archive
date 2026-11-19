"""Retain newly opened C.3be primary sources, with actual hashes and runtimes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import time
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parents[1]
DEST = BASE / "sources" / "C3be"
DEST.mkdir(parents=True, exist_ok=True)
tasks = [
    ("esser2023.pdf",
     "https://web.math.princeton.edu/~le3339/NonTorsionBrauerGroups.pdf"),
    ("tanaka2014.pdf",
     "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/"
     "3EE226BBE3C17AC014A5745E2469D339/S0027763000022431a.pdf/"
     "minimal-models-and-abundance-for-positive-characteristic-log-surfaces.pdf"),
]
for tag in ["0BGP", "0BFZ", "0BIC", "02OS", "01OF", "0B5V",
            "0C4K", "0FDJ", "0B37", "092X", "02RX", "02S2"]:
    tasks.append(("stacks_"+tag+".html", "https://stacks.math.columbia.edu/tag/"+tag))
retry_failed = "--retry-failed" in sys.argv
semilocal = "--semilocal" in sys.argv
if retry_failed:
    previous = json.loads((BASE / "output" /
                           "C3_surface_reduction_Fpbar_sources.json").read_text())
    tasks = [(r["filename"], r["url"]) for r in previous["sources"]
             if not r["success"]]
elif semilocal:
    tasks = [("stacks_"+tag+".html", "https://stacks.math.columbia.edu/tag/"+tag)
             for tag in ["02M9", "0EBM", "02JW", "02SI"]]

def acquire(item):
    filename, url = item
    row = {"filename": filename, "url": url,
           "started_utc": datetime.now(timezone.utc).isoformat()}
    t = time.perf_counter()
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=35) as response:
            data = response.read()
            row["http_status"] = response.status
            row["final_url"] = response.url
        if filename.endswith(".pdf") and not data.startswith(b"%PDF-"):
            raise ValueError("Response is not a PDF")
        target = DEST / filename
        target.write_bytes(data)
        row.update({"bytes": len(data), "sha256": sha256(data).hexdigest(),
                    "success": True})
        if filename.endswith(".pdf"):
            r = subprocess.run(["pdftotext", "-layout", str(target),
                                str(target.with_suffix(".txt"))],
                               text=True, capture_output=True)
            row["pdftotext_returncode"] = r.returncode
            if r.returncode:
                row["pdftotext_error"] = r.stderr
    except Exception as exc:
        row.update({"success": False, "error": repr(exc)})
    row["runtime_seconds"] = time.perf_counter()-t
    return row

started = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool:
    rows = list(pool.map(acquire, tasks))
report = {"finished_utc": datetime.now(timezone.utc).isoformat(),
          "runtime_seconds": time.perf_counter()-started, "sources": rows}
out = BASE / "output" / ("C3_surface_reduction_Fpbar_sources_retry.json"
                        if retry_failed else
                        "C3_surface_reduction_Fpbar_semilocal_sources.json"
                        if semilocal else
                        "C3_surface_reduction_Fpbar_sources.json")
out.write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
