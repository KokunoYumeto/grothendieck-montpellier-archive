"""Retain the primary six-page Nevins v2 source; no theorem test."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

root = Path(__file__).resolve().parents[3]
out = Path(__file__).resolve().parents[1] / "output"
url = "https://arxiv.org/pdf/math/0008190"
record = {"url": url, "started_utc": datetime.now(timezone.utc).isoformat()}
tick = time.perf_counter()
try:
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read()
    assert data.startswith(b"%PDF"), "Response is not a PDF"
    pdf = root / "sources" / "nevins2002_framed_sheaves_v2.pdf"
    pdf.write_bytes(data)
    txt = pdf.with_suffix(".txt")
    result = subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], capture_output=True, text=True)
    record.update({"pdf": str(pdf.relative_to(root)), "text": str(txt.relative_to(root)),
                   "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                   "pdftotext_exit_code": result.returncode, "pdftotext_stdout": result.stdout,
                   "pdftotext_stderr": result.stderr, "success": result.returncode == 0})
except Exception as exc:
    record.update({"success": False, "error": repr(exc)})
record["finished_utc"] = datetime.now(timezone.utc).isoformat()
record["runtime_seconds"] = time.perf_counter() - tick
encoded = json.dumps(record, indent=2)
(out / "nevins_source_acquisition.json").write_text(encoded + "\n")
print(encoded)
