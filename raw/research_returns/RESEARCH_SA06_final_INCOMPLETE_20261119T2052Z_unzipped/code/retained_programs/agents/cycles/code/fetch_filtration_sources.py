#!/usr/bin/env python3
"""Preserve primary PDFs opened for the late cycle/parameter-space audit."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

BASE = Path(__file__).resolve().parents[1]
SOURCES = [
    ("Saito1992", "https://www.numdam.org/item/CM_1992__84_3_289_0.pdf"),
    ("HernandezPelaez2025", "https://arxiv.org/pdf/2509.15920"),
    ("Pelaez2026", "https://arxiv.org/pdf/2602.06185"),
    ("BarbieriViale2001", "https://sites.unimi.it/barbieri/MHCPro.pdf"),
]

def fetch(item):
    name, url = item
    rec = {"name": name, "url": url, "utc": datetime.now(timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "research-source-audit/1.0"})
        with urllib.request.urlopen(req, timeout=25) as response:
            data = response.read()
            rec["final_url"] = response.geturl()
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        path = BASE / "sources" / (name + ".pdf")
        path.write_bytes(data)
        rec.update(status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        proc = subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))],
                              capture_output=True, text=True, timeout=20)
        rec.update(pdftotext_exit=proc.returncode, pdftotext_stderr=proc.stderr)
    except Exception as error:
        rec.update(status="failed", error=f"{type(error).__name__}: {error}")
    return rec

with ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(fetch, SOURCES))
result = {"purpose": "Primary-source preservation; theorem applications are audited separately", "records": records}
(BASE / "output" / "fetch_filtration_sources.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
