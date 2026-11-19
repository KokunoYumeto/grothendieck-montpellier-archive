"""Retrieve the official cote14 PDF with verified byte ranges.

Only the code and provenance record are deliverables.  The raw scan is an
excluded research input; downloading it alone establishes no reading.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib
import json
import re
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = "https://grothendieck.umontpellier.fr/14.pdf"
DEST = ROOT / "sources" / "montpellier_cote14_ranges.pdf"
OUT = ROOT / "code" / "fetch_montpellier_cote14_output.json"
CHUNK = 4 * 1024 * 1024
start = time.perf_counter()
record = {"url": URL, "chunk_bytes": CHUNK, "workers": 6,
          "ranges": [], "outcome": "Running"}

try:
    req = urllib.request.Request(URL, headers={"Range": "bytes=0-0"})
    with urllib.request.urlopen(req, timeout=45) as response:
        content_range = response.headers.get("Content-Range", "")
        match = re.fullmatch(r"bytes 0-0/(\d+)", content_range)
        assert response.status == 206 and match, (response.status, content_range)
        assert len(response.read(2)) == 1
        size = int(match.group(1))
    record["expected_bytes"] = size
    OUT.write_text(json.dumps(record, indent=2))

    def fetch(begin):
        end = min(size - 1, begin + CHUNK - 1)
        req = urllib.request.Request(URL, headers={"Range": f"bytes={begin}-{end}"})
        with urllib.request.urlopen(req, timeout=55) as response:
            body = response.read(end - begin + 2)
            actual = response.headers.get("Content-Range")
            assert response.status == 206, response.status
            assert actual == f"bytes {begin}-{end}/{size}", actual
            assert len(body) == end - begin + 1, len(body)
        return begin, end, body

    with DEST.open("wb") as target:
        target.truncate(size)
        with ThreadPoolExecutor(max_workers=6) as executor:
            futures = [executor.submit(fetch, begin) for begin in range(0, size, CHUNK)]
            for future in as_completed(futures):
                begin, end, body = future.result()
                target.seek(begin)
                target.write(body)
                record["ranges"].append({"begin": begin, "end": end,
                                         "bytes": len(body), "verified": True})
                record["runtime_seconds"] = time.perf_counter() - start
                OUT.write_text(json.dumps(record, indent=2))
    with DEST.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    record.update(outcome="Retrieved and verified all byte ranges",
                  bytes=DEST.stat().st_size, sha256=digest, local=str(DEST))
except Exception as error:
    record.update(outcome="Incomplete retrieval; PDF must not be treated as inspected",
                  error=repr(error))
record["ranges"].sort(key=lambda item: item["begin"])
record["runtime_seconds"] = time.perf_counter() - start
OUT.write_text(json.dumps(record, indent=2))
print(json.dumps(record, indent=2))
