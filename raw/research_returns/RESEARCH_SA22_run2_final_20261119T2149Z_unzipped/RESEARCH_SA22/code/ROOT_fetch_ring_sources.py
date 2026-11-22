#!/usr/bin/env python3
"""Fetch three publicly opened primary exploratory sources; preserve hashes.

Downloaded literature is excluded from deliverable ZIPs. No authentication or
access-control bypass is attempted. A failed response remains a failed fetch.
"""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import time
import urllib.request

root = Path(__file__).resolve().parents[1]
sources = [
    ("ROOT_Picavet1976.pdf", "https://www.numdam.org/article/PSMIR_1976___4_A7_0.pdf"),
    ("ROOT_Gilmer1966.pdf", "https://msp.org/pjm/1966/19-2/pjm-v19-n2-p10-s.pdf"),
    ("ROOT_GilmerHeinzer1966.pdf", "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5FEB2C61491EA6208EC7D07E9713C960/S1446788700004304a.pdf/on-the-complete-integral-closure-of-an-integral-domain.pdf"),
]

def fetch(item):
    name, url = item
    started = time.perf_counter()
    record = {"file": "literature/" + name, "url": url,
              "requested_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=40) as response:
            body = response.read()
            record.update(http_status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"))
        if not body.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF; no literature file written")
        target = root / "literature" / name
        target.write_bytes(body)
        record.update(status="downloaded", bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest())
    except Exception as error:
        record.update(status="failed", error=repr(error))
    record["elapsed_seconds"] = time.perf_counter() - started
    return record

def main(items=sources, output_name="ROOT_ring_sources_fetch.json", purpose="Exploratory primary-source search for the unresolved normal Goldman/localization construction; no example inferred from metadata"):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        records = list(executor.map(fetch, items))
    output = {"purpose": purpose, "sources": records}
    (root / "logs" / output_name).write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
