"""Reproduce the primary-source acquisition for C.4x.

The default keeps already acquired PDFs; --refresh downloads them again.
All downloads use the original publisher/archive endpoints.  Timings are
wall-clock durations, not a mathematical proof certificate.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import time
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("--refresh", action="store_true")
args = parser.parse_args()
base = Path(__file__).resolve().parents[1]
sources = [
    ("yu_hilbert_blumenthal2003",
     "https://www.numdam.org/article/AIF_2003__53_7_2105_0.pdf"),
    ("yu_basic2015",
     "https://archive.mpim-bonn.mpg.de/id/eprint/819/1/preprint_2015_38.pdf"),
]
start = time.monotonic()
rows = []
for name, url in sources:
    path = base / "sources" / (name + ".pdf")
    acquired = args.refresh or not path.exists()
    if acquired:
        with urllib.request.urlopen(url, timeout=35) as response:
            data = response.read()
        assert data.startswith(b"%PDF")
        path.write_bytes(data)
    data = path.read_bytes()
    assert data.startswith(b"%PDF")
    subprocess.run(
        ["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))],
        check=True,
    )
    rows.append({
        "name": name, "url": url, "downloaded_this_run": acquired,
        "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
    })

path = base / "sources" / "yu_hilbert_blumenthal2003.pdf"
for pdf_page, printed_page in [(14, 2117), (15, 2118)]:
    subprocess.run(
        ["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page),
         "-r", "140", "-png", "-singlefile", str(path),
         str(base / "output" / f"yu_hb_p{printed_page}")],
        check=True,
    )
print(json.dumps({
    "sources": rows,
    "rendered_printed_pages": [2117, 2118],
    "duration_seconds": round(time.monotonic() - start, 6),
}, indent=2))
