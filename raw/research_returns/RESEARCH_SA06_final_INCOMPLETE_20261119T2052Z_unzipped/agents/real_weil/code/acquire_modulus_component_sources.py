"""Acquire exact primary sources for the post-C.3bt family-scope audit.

This program acquires sources; it does not validate their theorems.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parents[1] / "output"
items = [
    ("binda_krishna2018_modulus_published", "https://epub.uni-regensburg.de/41077/1/zero_cycles_with_modulus_and_zero_cycles_on_singular_varieties.pdf"),
    ("friedlander_walker2002_function_complexes_author", "https://dornsife.usc.edu/ericmfriedlander/wp-content/uploads/sites/233/2023/06/24.pdf"),
]
started = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()
records = []
for stem, url in items:
    item_tick = time.perf_counter()
    row = {"name": stem, "url": url, "started_utc": datetime.now(timezone.utc).isoformat()}
    pdf = root / "sources" / (stem + ".pdf")
    txt = pdf.with_suffix(".txt")
    try:
        if not pdf.exists():
            with urllib.request.urlopen(url, timeout=30) as response:
                data = response.read()
            assert data.startswith(b"%PDF"), "Response is not a PDF"
            pdf.write_bytes(data)
            row["acquisition"] = "downloaded"
        else:
            data = pdf.read_bytes()
            row["acquisition"] = "reused_existing_file"
        result = subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], capture_output=True, text=True)
        row.update({"pdf": str(pdf.relative_to(root)), "text": str(txt.relative_to(root)),
                    "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                    "pdftotext_exit_code": result.returncode, "pdftotext_stdout": result.stdout,
                    "pdftotext_stderr": result.stderr, "success": result.returncode == 0})
    except Exception as exc:
        row.update({"success": False, "error": repr(exc)})
    row["finished_utc"] = datetime.now(timezone.utc).isoformat()
    row["runtime_seconds"] = time.perf_counter() - item_tick
    records.append(row)
record = {"started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
          "runtime_seconds": time.perf_counter() - tick, "sources": records,
          "scope": "Acquisition and text extraction only; exact mathematical read scopes are recorded separately."}
encoded = json.dumps(record, indent=2)
(out / "modulus_component_sources_acquisition.json").write_text(encoded + "\n")
print(encoded)
