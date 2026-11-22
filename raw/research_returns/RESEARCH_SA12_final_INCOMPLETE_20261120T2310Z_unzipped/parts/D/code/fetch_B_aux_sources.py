"""Retain the two primary sources used for the B.2r cross-audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, time, urllib.request, subprocess

root = Path(__file__).resolve().parents[1]
targets = [
    ("Tanaka1502.01381", "https://arxiv.org/pdf/1502.01381"),
    ("Kelly2018_UH", "https://www.ms.u-tokyo.ac.jp/~kelly/pdfs/uh%20non-fp.pdf"),
]

def fetch(target):
    name, url = target
    started = time.monotonic()
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Research source verification"})
        with urllib.request.urlopen(request, timeout=50) as response:
            data = response.read()
            status = response.status
        path = root / "sources" / (name + ".pdf")
        path.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], check=True)
        return {"name": name, "url": url, "http_status": status,
                "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                "elapsed_seconds": time.monotonic() - started}
    except Exception as exc:
        return {"name": name, "url": url, "error": repr(exc),
                "elapsed_seconds": time.monotonic() - started}

with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(fetch, targets))
output = root / "code" / "fetch_B_aux_sources_output.json"
output.write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
