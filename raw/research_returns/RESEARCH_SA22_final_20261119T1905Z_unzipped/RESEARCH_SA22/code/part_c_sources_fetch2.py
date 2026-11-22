#!/usr/bin/env python3
"""Fetch publicly exposed original-source URLs; save truthful content metadata."""
from pathlib import Path
import datetime, hashlib, json, subprocess, time, urllib.request

ROOT = Path(__file__).resolve().parents[1]
items = [
    ("knudsen_mumford1976", "https://pnp.mathematik.uni-stuttgart.de/lexmath/kuenzer/knudsen_mumford.pdf"),
    ("raynaud1970_frontmatter", "https://link.springer.com/content/pdf/bfm:978-3-540-36249-4/1"),
]
records = []
start = time.perf_counter()
for name, url in items:
    record = {"name": name, "url": url, "utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    then = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            payload = response.read()
            record.update(status=response.status, final_url=response.url, content_type=response.headers.get("Content-Type"))
        record.update(bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest(), is_pdf=payload.startswith(b"%PDF"))
        target = ROOT / "sources" / (name + (".pdf" if record["is_pdf"] else ".html"))
        target.write_bytes(payload)
        record["saved"] = str(target.relative_to(ROOT))
        if record["is_pdf"]:
            text_target = target.with_suffix(".txt")
            completed = subprocess.run(["pdftotext", "-layout", str(target), str(text_target)], capture_output=True, text=True)
            record.update(pdftotext_returncode=completed.returncode, text_bytes=text_target.stat().st_size if text_target.exists() else 0)
    except Exception as exc:
        record["error"] = str(exc)
    record["seconds"] = time.perf_counter()-then
    records.append(record)
result = {"records": records, "total_seconds": time.perf_counter()-start, "scope": "Public-source retrieval only; no mathematical computation or theorem verification."}
(ROOT / "code" / "part_c_sources_fetch2_output.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
