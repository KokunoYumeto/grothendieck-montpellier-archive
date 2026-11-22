"""Retain the historical primary version for a parameter-scope check.

This is a source-access program, not a mathematical certificate.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone
from urllib.request import Request, urlopen

base = Path(__file__).resolve().parents[1]
target = base.parent.parent / "sources" / "kohrita2017_algebraic_part_v2.pdf"
started = datetime.now(timezone.utc).isoformat()
tic = time.perf_counter()
record = {"started_utc": started, "scope": "Primary-source acquisition only", "attempts": []}
for url in ["https://arxiv.org/pdf/1512.02320v2", "https://export.arxiv.org/pdf/1512.02320v2"]:
    before = time.perf_counter()
    try:
        with urlopen(Request(url, headers={"User-Agent": "Research source verification"}), timeout=18) as response:
            data = response.read()
        if not data.startswith(b"%PDF-"):
            raise ValueError("Response is not a PDF")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        text_path = target.with_suffix(".txt")
        extraction = subprocess.run(["pdftotext", "-layout", str(target), str(text_path)], capture_output=True, text=True)
        record["attempts"].append({"url": url, "success": True, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "runtime_seconds": time.perf_counter()-before})
        record.update({"pdf": str(target), "text": str(text_path), "pdftotext_exit_code": extraction.returncode, "pdftotext_stderr": extraction.stderr})
        break
    except Exception as exc:
        record["attempts"].append({"url": url, "success": False, "error": repr(exc), "runtime_seconds": time.perf_counter()-before})
record["completed_utc"] = datetime.now(timezone.utc).isoformat()
record["runtime_seconds"] = time.perf_counter()-tic
out = base / "output" / "kohrita_v2_acquisition.json"
out.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
