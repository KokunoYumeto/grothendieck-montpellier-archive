#!/usr/bin/env python3
"""Retain three primary-source acquisitions and exact timings; no theorem check."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import requests

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("friedlander_walker2002_function_complexes", "https://dornsife.usc.edu/ericmfriedlander/wp-content/uploads/sites/233/2023/06/24.pdf"),
    ("achter_casalaina_vial2019_parameters", "https://www.math.uni-bielefeld.de/~vial/abtriv.pdf"),
    ("krishna_park2012_algebraic_cobordism_v2", "https://arxiv.org/pdf/1203.5508v2"),
]

def acquire(item):
    stem, url = item
    start = time.perf_counter()
    result = {"name": stem, "url": url,
              "started_utc": datetime.now(timezone.utc).isoformat()}
    try:
        response = requests.get(url, timeout=25)
        result["status_code"] = response.status_code
        result["content_type"] = response.headers.get("content-type")
        response.raise_for_status()
        if not response.content.startswith(b"%PDF"):
            raise ValueError("Returned data is not a PDF")
        path = ROOT / "sources" / (stem + ".pdf")
        path.write_bytes(response.content)
        result.update(path=str(path), bytes=len(response.content),
                      sha256=hashlib.sha256(response.content).hexdigest())
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
(ROOT / "logs" / "proper_parameter_source_acquisition.json").write_text(encoded + "\n")
print(encoded)
