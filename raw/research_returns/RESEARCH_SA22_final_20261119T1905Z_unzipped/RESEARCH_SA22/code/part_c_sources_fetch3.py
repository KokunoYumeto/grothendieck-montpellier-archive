#!/usr/bin/env python3
"""Ordinary requests to public primary-source and archive catalogue URLs."""
import concurrent.futures
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import urllib.request

root = Path(__file__).resolve().parents[1]
tasks = [
    ("ShiodaKatsura1979", "https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf/-char/ja", root / "sources/shioda_katsura1979.pdf", "pdf"),
    ("Gabriel1932_archive_catalog", "https://archive.org/advancedsearch.php?q=title%3A%28Proceedings%20London%20Mathematical%20Society%29%20AND%20year%3A1932&output=json", root / "sources/gabriel1932_archive_catalog.json", "json"),
]
started = time.perf_counter()

def one(task):
    name, url, target, expected = task
    begin = time.perf_counter()
    entry = {"name": name, "url": url, "started_utc": datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            content = r.read()
            status = r.status
            entry.update(status=status, final_url=r.url, content_type=r.headers.get("Content-Type"), bytes=len(content))
        valid = status == 200 and (content.startswith(b"%PDF") if expected == "pdf" else content.lstrip().startswith(b"{"))
        if valid:
            target.write_bytes(content)
            entry.update(saved=str(target.relative_to(root)), sha256=hashlib.sha256(content).hexdigest())
        else:
            entry["note"] = "No source content saved; response did not match requested public content."
    except Exception as e:
        entry["error"] = f"{type(e).__name__}: {e}"
    entry["runtime_seconds"] = time.perf_counter() - begin
    return entry

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(one, tasks))
out = {"total_runtime_seconds": time.perf_counter() - started, "results": results}
Path(__file__).with_name("part_c_sources_fetch3_output.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
