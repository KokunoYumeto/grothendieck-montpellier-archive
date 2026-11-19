"""Retain the primary bigonal source and actual download timing."""
from pathlib import Path
import hashlib
import json
import subprocess
import time
import urllib.request
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "recillas_rodriguez2003_fourfold.pdf"
OUT = ROOT / "output" / "fetch_bigonal_source.json"
URL = "https://arxiv.org/pdf/math/0303155"
started = time.perf_counter()
data = urllib.request.urlopen(URL, timeout=60).read()
SOURCE.parent.mkdir(parents=True, exist_ok=True)
SOURCE.write_bytes(data)
subprocess.run(["pdftotext", "-layout", str(SOURCE), str(SOURCE.with_suffix(".txt"))], check=True)
record = {
    "completed_utc": datetime.now(timezone.utc).isoformat(),
    "url": URL,
    "path": str(SOURCE),
    "bytes": len(data),
    "sha256": hashlib.sha256(data).hexdigest(),
    "runtime_seconds": time.perf_counter() - started,
    "opened_scope": "Web primary read: section 7.1, printed pages 35--37; Proposition 2.1 and Theorem 2.5. The remaining 78-page manuscript has not been claimed fully read.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
