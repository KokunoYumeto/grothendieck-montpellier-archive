"""Acquire exact primary PDFs for the intrinsic proper-family source audit.

This is source acquisition, not a mathematical certificate.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from time import perf_counter
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[4]
SOURCES = ROOT / "research" / "sources"
OUTPUT = Path(__file__).resolve().parents[1] / "output"
SPECS = [
    ("kohrita2024_algebraic_part_v3", "https://arxiv.org/pdf/1512.02320v3"),
    ("binda_krishna2022_zero_cycles", "https://www.numdam.org/item/10.5802/jep.183.pdf"),
]


def fetch(spec):
    stem, url = spec
    started = datetime.now(timezone.utc).isoformat()
    t0 = perf_counter()
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=40) as response:
        data = response.read()
        final_url = response.url
    if not data.startswith(b"%PDF"):
        raise ValueError(f"Non-PDF response for {stem}")
    path = SOURCES / f"{stem}.pdf"
    path.write_bytes(data)
    text_path = path.with_suffix(".txt")
    subprocess.run(["pdftotext", "-layout", str(path), str(text_path)], check=True)
    return {
        "stem": stem, "url": url, "final_url": final_url,
        "started_utc": started, "completed_utc": datetime.now(timezone.utc).isoformat(),
        "runtime_seconds": perf_counter() - t0, "bytes": len(data),
        "sha256": sha256(data).hexdigest(), "pdf": str(path), "text": str(text_path),
        "scope": "Primary-source acquisition only; reading scope is recorded separately.",
    }


if __name__ == "__main__":
    SOURCES.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    t0 = perf_counter()
    started = datetime.now(timezone.utc).isoformat()
    with ThreadPoolExecutor(max_workers=2) as pool:
        records = list(pool.map(fetch, SPECS))
    result = {"started_utc": started, "completed_utc": datetime.now(timezone.utc).isoformat(),
              "runtime_seconds": perf_counter() - t0, "sources": records}
    (OUTPUT / "intrinsic_quotient_source_manifest.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
