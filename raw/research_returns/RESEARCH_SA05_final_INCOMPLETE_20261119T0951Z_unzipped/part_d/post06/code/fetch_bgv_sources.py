"""Fetch exact primary sources for the compact-rigid/pure-motive scope audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import urllib.request

BASE = Path(__file__).resolve().parents[1]
RAW = BASE.parents[2] / "pending_post06_sources_d"
TEXT = BASE / "sources"
OUT = BASE / "output"
for directory in (RAW, TEXT, OUT):
    directory.mkdir(parents=True, exist_ok=True)
sources = [
    ("BindaGallauerVezzani2024V2", "https://arxiv.org/pdf/2306.05099v2", "pdf"),
    ("BindaGallauerVezzaniCurrentMetadata", "https://arxiv.org/abs/2306.05099", "html"),
]
records = []
for name, url, kind in sources:
    record = {"name": name, "url": url, "checked_utc": datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 primary-source research"})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
            record["resolved_url"] = response.url
        path = (RAW if kind == "pdf" else TEXT) / (name + "." + kind)
        path.write_bytes(data)
        record.update(status="obtained", path=str(path), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        if kind == "pdf":
            target = TEXT / (name + ".txt")
            subprocess.run(["pdftotext", "-layout", str(path), str(target)], check=True)
            record["text_path"] = str(target)
    except Exception as error:
        record.update(status="not_obtained", error=f"{type(error).__name__}: {error}")
    records.append(record)
result = {"created_utc": datetime.now(timezone.utc).isoformat(), "sources": records}
(OUT / "bgv_fetch_output.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
