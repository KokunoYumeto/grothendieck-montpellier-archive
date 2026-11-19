"""Archive exact current primary sources used in the C6 scope audit.

Raw PDF bytes remain outside the deliverable tree.  Extracted texts and
hash/URL records are retained with the research notes.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import urllib.request

BASE = Path(__file__).resolve().parents[1]
RAW = BASE.parents[2] / "pending_post06_sources_d"
TEXT = BASE / "sources"
OUTPUT = BASE / "output"
for directory in (RAW, TEXT, OUTPUT):
    directory.mkdir(parents=True, exist_ok=True)

SOURCES = [
    ("Jannsen1992Semisimple", "https://epub.uni-regensburg.de/26642/1/jannsen10.pdf", "pdf"),
    ("Cisinski2025CompletionV5", "https://arxiv.org/pdf/2503.24033v5", "pdf"),
    ("Cisinski2025CurrentMetadata", "https://arxiv.org/abs/2503.24033", "html"),
]
records = []
for name, url, kind in SOURCES:
    record = {"name": name, "url": url, "checked_utc": datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 primary-source research"})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
            record["resolved_url"] = response.url
        destination = (RAW if kind == "pdf" else TEXT) / (name + "." + kind)
        destination.write_bytes(data)
        record.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), status="obtained", path=str(destination))
        if kind == "pdf":
            target = TEXT / (name + ".txt")
            subprocess.run(["pdftotext", "-layout", str(destination), str(target)], check=True)
            record["text_path"] = str(target)
            record["text_bytes"] = target.stat().st_size
    except Exception as error:
        record.update(status="not_obtained", error=f"{type(error).__name__}: {error}")
    records.append(record)
result = {"created_utc": datetime.now(timezone.utc).isoformat(), "sources": records}
target = OUTPUT / "c6_closure_fetch_output.json"
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
