#!/usr/bin/env python3
"""Fetch the primary 2025 stringy-motive paper and its arXiv source.

This is a source-provenance utility, not a mathematical certificate.
All output remains within parts/B.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import json
import subprocess
import tarfile
import urllib.request

base = Path(__file__).resolve().parents[1]
dest = base / "sources" / "CRY2025"
dest.mkdir(exist_ok=True)
items = [
    ("CarvajalRojasYasuda2025.pdf", "https://ems.press/content/serial-article-files/50862?nt=1"),
    ("source.tar", "https://arxiv.org/src/2105.05214v4"),
]

def fetch(item):
    name, url = item
    start = perf_counter()
    record = {"name": name, "url": url, "accessed_utc": datetime.now(timezone.utc).isoformat()}
    path = dest / name
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 academic source audit"})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
        path.write_bytes(data)
        record.update(bytes=len(data), sha256=sha256(data).hexdigest())
        if path.suffix == ".pdf":
            assert data.startswith(b"%PDF"), "Not a PDF response"
            completed = subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], capture_output=True, text=True)
            record["pdftotext_returncode"] = completed.returncode
        else:
            out = dest / "tex"
            out.mkdir(exist_ok=True)
            with tarfile.open(path) as archive:
                for member in archive.getmembers():
                    if not member.isfile():
                        continue
                    relative = Path(member.name)
                    if relative.is_absolute() or ".." in relative.parts:
                        raise ValueError("Unsafe archive member")
                    target = out / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    stream = archive.extractfile(member)
                    assert stream is not None
                    target.write_bytes(stream.read())
            record["tex_files"] = len(list(out.rglob("*.tex")))
        record["status"] = "saved"
    except Exception as error:
        record.update(status="failed", error=repr(error))
    record["elapsed_seconds"] = perf_counter() - start
    return record

start = perf_counter()
with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(fetch, items))
report = {"sources": records, "elapsed_seconds": perf_counter() - start}
(base / "code" / "output" / "fetch_CRY2025B.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
