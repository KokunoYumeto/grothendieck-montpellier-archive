from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess
import time
import urllib.request

base = Path(__file__).resolve().parents[1]
items = [
    ("mukai1981_partial_fourier", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf"),
    ("yoshioka2001_partial_fourier", "https://arxiv.org/pdf/math/0009001"),
    ("bps2010_partial_fourier", "https://arxiv.org/pdf/0912.3377"),
    ("kahn2026_divided_powers", "https://arxiv.org/pdf/2602.11135"),
]

def fetch(item):
    name, url = item
    started = time.perf_counter()
    result = {"name": name, "url": url}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            result["final_url"] = response.url
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        destination = base / "sources" / (name + ".pdf")
        destination.write_bytes(data)
        extraction = subprocess.run(["pdftotext", "-layout", str(destination),
                                     str(destination.with_suffix(".txt"))],
                                    capture_output=True, text=True)
        result.update(status="downloaded", bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest(), path=str(destination),
                      pdftotext_returncode=extraction.returncode,
                      pdftotext_stderr=extraction.stderr)
    except Exception as error:
        result.update(status="failed", error=repr(error))
    result["runtime_seconds"] = time.perf_counter() - started
    return result

started = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, items))
report = {"utc": datetime.now(timezone.utc).isoformat(),
          "runtime_seconds": time.perf_counter() - started, "sources": results}
encoded = json.dumps(report, indent=2)
(base / "output" / "fetch_partial_fourier_sources.json").write_text(encoded + "\n")
print(encoded)
