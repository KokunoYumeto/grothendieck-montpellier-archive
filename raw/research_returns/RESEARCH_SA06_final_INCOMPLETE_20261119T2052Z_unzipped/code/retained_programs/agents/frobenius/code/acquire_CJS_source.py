"""Acquire the exact CJS author version used in C.3bd."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time
from urllib.request import Request, urlopen

BASE = Path(__file__).resolve().parents[1]
url = "https://arxiv.org/pdf/0905.2191"
path = BASE / "sources/cossart_jannsen_saito2013_arxivv2.pdf"
report = dict(url=url, filename=path.name,
              started_utc=datetime.now(timezone.utc).isoformat())
started = time.perf_counter()
try:
    with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}),
                 timeout=50) as response:
        data = response.read()
    if not data.startswith(b"%PDF"):
        raise ValueError("response is not a PDF")
    path.write_bytes(data)
    subprocess.run(["pdftotext", "-layout", str(path),
                    str(path.with_suffix(".txt"))], check=True)
    report.update(status="saved", bytes=len(data),
                  sha256=hashlib.sha256(data).hexdigest())
except Exception as error:
    report.update(status="failed", error=repr(error))
report["runtime_seconds"] = time.perf_counter()-started
(BASE / "output/acquire_CJS_source.json").write_text(
    json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
