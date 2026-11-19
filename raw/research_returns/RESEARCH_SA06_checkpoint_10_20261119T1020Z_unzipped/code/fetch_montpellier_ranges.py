"""Retrieve the official cote 15 scan using verified HTTP byte ranges.

The source PDF is excluded from the research deliverables.  The exact URL,
range checks, final digest, timing and outcome are retained as provenance.
This script does not establish any reading of the manuscript by itself.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib
import json
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = "https://grothendieck.umontpellier.fr/15.pdf"
SIZE = 89504936
CHUNK = 4 * 1024 * 1024
DEST = ROOT / "sources" / "montpellier_cote15_ranges.pdf"
OUT = ROOT / "code" / "fetch_montpellier_ranges_output.json"
start = time.perf_counter()
record = {"url": URL, "expected_bytes": SIZE, "chunk_bytes": CHUNK,
          "workers": 6, "ranges": [], "outcome": "Running"}

def fetch(begin):
    end = min(SIZE - 1, begin + CHUNK - 1)
    req = urllib.request.Request(URL, headers={"Range": f"bytes={begin}-{end}"})
    with urllib.request.urlopen(req, timeout=55) as response:
        body = response.read(end - begin + 2)
        actual_range = response.headers.get("Content-Range")
        assert response.status == 206, response.status
        assert actual_range == f"bytes {begin}-{end}/{SIZE}", actual_range
        assert len(body) == end - begin + 1, len(body)
    return begin, end, body

try:
    with DEST.open("wb") as target:
        target.truncate(SIZE)
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = [executor.submit(fetch, begin) for begin in range(0, SIZE, CHUNK)]
            for future in as_completed(futures):
                begin, end, body = future.result()
                target.seek(begin)
                target.write(body)
                record["ranges"].append({"begin": begin, "end": end,
                                         "bytes": len(body), "verified": True})
                record["runtime_seconds"] = time.perf_counter() - start
                OUT.write_text(json.dumps(record, indent=2))
    digest = hashlib.file_digest(DEST.open("rb"), "sha256").hexdigest()
    record.update(outcome="Retrieved and verified all byte ranges", bytes=DEST.stat().st_size,
                  sha256=digest, local=str(DEST))
except Exception as error:
    record.update(outcome="Incomplete retrieval; PDF must not be treated as inspected",
                  error=repr(error))
record["ranges"].sort(key=lambda item: item["begin"])
record["runtime_seconds"] = time.perf_counter() - start
OUT.write_text(json.dumps(record, indent=2))
print(json.dumps(record, indent=2))
