#!/usr/bin/env python3
"""Preserve the three primary PDFs opened for E.3g--i, with exact fetch outcomes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.request

BASE = Path(__file__).resolve().parents[1]
SOURCES = [
    ("Suzuki2021", "https://epiga.episciences.org/8881/pdf"),
    ("OttemSuzuki2020", "https://arxiv.org/pdf/1906.08994"),
    ("ACMVWalker2022", "https://www.math.uni-bielefeld.de/~vial/WalkerAJmap.pdf"),
]

def fetch(item):
    name, url = item
    rec = {"name": name, "url": url, "utc": datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "research-source-audit/1.0"})
        with urllib.request.urlopen(request, timeout=25) as response:
            data = response.read()
            rec["final_url"] = response.geturl()
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        path = BASE / "sources" / (name + ".pdf")
        path.write_bytes(data)
        rec.update(status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        proc = subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))],
                              text=True, capture_output=True, timeout=20)
        rec["pdftotext_exit"] = proc.returncode
        rec["pdftotext_stderr"] = proc.stderr
    except Exception as error:
        rec.update(status="failed", error=f"{type(error).__name__}: {error}")
    return rec

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(fetch, SOURCES))
result = {"purpose": "Primary-source preservation; mathematical claims checked separately in prose", "records": records}
(BASE / "output" / "fetch_walker_sources.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
