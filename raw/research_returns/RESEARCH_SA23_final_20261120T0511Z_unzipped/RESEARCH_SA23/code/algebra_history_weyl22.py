"""Read public DOI/handle/OAI metadata for the documented Weyl inventory.

No credentialed, internal, or restricted endpoint is requested.
The OAI endpoint is published in ETH's current Research Collection manual.
"""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import time
import urllib.request

BASE = Path(__file__).resolve().parents[1]
URLS = {
    "weyl_handle_metadata": "https://hdl.handle.net/api/handles/20.500.11850/138043",
    "weyl_datacite_media": "https://api.datacite.org/dois/10.3929/ethz-a-000310478/media",
    "eth_oai_identify": "https://research-collection.ethz.ch/server/oai/request?verb=Identify",
}

def retrieve(item):
    label, url = item
    start = time.monotonic()
    result = {"label": label, "url": url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            path = BASE / "sources" / ("algebra_history_" + label + ".txt")
            path.write_bytes(data)
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"),
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                          file=str(path))
    except Exception as error:
        result["error"] = repr(error)
    result["seconds"] = time.monotonic() - start
    return result

start = time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(retrieve, URLS.items()))
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "seconds": time.monotonic() - start, "results": results}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_weyl22.json").write_text(text + "\n")
print(text)
