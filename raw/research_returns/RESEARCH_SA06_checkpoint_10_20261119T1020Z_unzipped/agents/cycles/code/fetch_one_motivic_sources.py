"""Retrieve opened primary sources for the one-motivic quotient audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "AyoubBarbieriViale2009": "https://arxiv.org/pdf/math/0607738v2",
    "BarbieriViale2007Theory": "https://arxiv.org/pdf/math/0502476v3",
    "ACMV2026Twist": "https://www.math.colostate.edu/~achter/math/torsor0625.pdf",
}

def fetch(item):
    name, url = item
    start = time.perf_counter()
    record = {"name": name, "url": url, "utc": datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read()
        if not data.startswith(b"%PDF"):
            raise ValueError("The response is not a PDF")
        pdf = ROOT / "sources" / (name + ".pdf")
        pdf.write_bytes(data)
        txt = pdf.with_suffix(".txt")
        process = subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], capture_output=True, text=True)
        record.update(status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pdf=str(pdf), text=str(txt), pdftotext_exit=process.returncode)
    except Exception as exc:
        record.update(status="failed", error=f"{type(exc).__name__}: {exc}")
    record["elapsed_seconds"] = time.perf_counter() - start
    return record

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, SOURCES.items()))
(ROOT / "output/fetch_one_motivic_sources.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
