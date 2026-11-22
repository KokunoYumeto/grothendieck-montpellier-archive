#!/usr/bin/env python3
"""Retain motive-route primary versions and timings; no theorem check."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("kahn_murre_pedrini_chapter14_layout", "https://webusers.imj-prg.fr/~bruno.kahn/preprints/kmp.pdf"),
    ("kahn_murre_pedrini_2005_chapter7_author", "https://webusers.imj-prg.fr/~bruno.kahn/preprints/surfaces4.pdf"),
    ("kahn2020_albanese_kernels_griffiths", "https://webusers.imj-prg.fr/~bruno.kahn/preprints/surface-and-curvewithYves-Acc.pdf"),
]

def acquire(item):
    stem, url = item
    start = time.perf_counter()
    result = {"name": stem, "url": url,
              "started_utc": datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            result["status_code"] = response.status
            result["content_type"] = response.headers.get("content-type")
            content = response.read()
        if not content.startswith(b"%PDF"):
            raise ValueError("Returned data is not a PDF")
        path = ROOT / "sources" / (stem + ".pdf")
        path.write_bytes(content)
        result.update(path=str(path), bytes=len(content),
                      sha256=hashlib.sha256(content).hexdigest())
        text_path = path.with_suffix(".txt")
        run = subprocess.run(["pdftotext", "-layout", str(path), str(text_path)],
                             capture_output=True, text=True)
        result.update(pdftotext_returncode=run.returncode,
                      pdftotext_output=run.stdout + run.stderr,
                      text_path=str(text_path))
        result["acquired"] = run.returncode == 0
    except Exception as error:
        result.update(acquired=False, error=str(error))
    result.update(finished_utc=datetime.now(timezone.utc).isoformat(),
                  runtime_seconds=time.perf_counter() - start)
    return result

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(acquire, SOURCES))
record = {"scope": "Acquisition and text extraction only; exact reading scopes are separately recorded.",
          "records": records}
encoded = json.dumps(record, indent=2)
(ROOT / "logs" / "motive_route_source_acquisition.json").write_text(encoded + "\n")
print(encoded)
