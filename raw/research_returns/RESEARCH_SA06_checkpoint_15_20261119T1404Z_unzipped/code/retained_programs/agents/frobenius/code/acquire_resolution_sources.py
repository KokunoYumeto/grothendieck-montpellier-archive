"""Acquire exact low-dimensional resolution sources with truthful metadata."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parents[1]
SOURCES = BASE / "sources"
OUTPUT = BASE / "output"
ITEMS = [
    ("kollar_witaszek2021_ample_exceptional.pdf",
     "https://arxiv.org/pdf/2102.03162"),
    ("kollar_witaszek2024_published.pdf",
     "https://www.sciengine.com/cfs/files/pdfs/view/1674-7283/91373F9C5B334F56AAC920078A279387.pdf"),
    ("cossart_piltant2019_arxivv2.pdf",
     "https://arxiv.org/pdf/1412.0868"),
]

def acquire(item):
    filename, url = item
    report = dict(filename=filename, url=url,
                  started_utc=datetime.now(timezone.utc).isoformat())
    started = time.perf_counter()
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=50) as response:
            data = response.read()
        if not data.startswith(b"%PDF"):
            raise ValueError("response is not a PDF")
        path = SOURCES / filename
        path.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(path),
                        str(path.with_suffix(".txt"))], check=True)
        report.update(status="saved", bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:
        report.update(status="failed", error=repr(error))
    report["runtime_seconds"] = time.perf_counter() - started
    return report

if __name__ == "__main__":
    SOURCES.mkdir(exist_ok=True)
    OUTPUT.mkdir(exist_ok=True)
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(acquire, ITEMS))
    report = dict(sources=rows, total_runtime_seconds=time.perf_counter()-started)
    (OUTPUT / "acquire_resolution_sources.json").write_text(
        json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
