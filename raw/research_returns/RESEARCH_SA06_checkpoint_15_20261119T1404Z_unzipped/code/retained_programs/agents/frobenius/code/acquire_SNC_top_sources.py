"""Retain the freshly opened SNC/top-Chow primary sources, with true timings."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "sources"
DEST.mkdir(exist_ok=True)
SOURCES = [
    ("levine1994_higher_chow_published.pdf",
     "https://www.numdam.org/article/AST_1994__226__235_0.pdf"),
    ("totaro1992_milnor.pdf",
     "https://www.math.ucla.edu/~totaro/papers/public_html/milnor.pdf"),
    ("burke_popa_shen2026_negativeK.pdf",
     "https://people.math.harvard.edu/~mpopa/papers/NegativeK.pdf"),
]

def fetch(item):
    filename, url = item
    start = time.perf_counter()
    result = {"filename": filename, "url": url,
              "started_utc": datetime.now(timezone.utc).isoformat()}
    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request, timeout=35) as response:
            data = response.read()
        if not data.startswith(b"%PDF"):
            raise ValueError("The returned body is not a PDF.")
        (DEST / filename).write_bytes(data)
        result.update(status="saved", bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        result.update(status="failed", error=str(exc))
    result["runtime_seconds"] = time.perf_counter() - start
    return result

if __name__ == "__main__":
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        rows = list(executor.map(fetch, SOURCES))
    report = {"sources": rows, "total_runtime_seconds": time.perf_counter()-started}
    path = ROOT / "output" / "acquire_SNC_top_sources.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
