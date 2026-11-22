"""Read three relevant public Hs 91a catalogue subdivisions.

Identifiers are copied from the just-retrieved Hs 91a child-list: miscellaneous
manuscripts 1909–1955, excerpts/notes/drawings, and manuscripts by others.
"""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import time
import urllib.request

BASE = Path(__file__).resolve().parents[1]
IDS = {
    "eth_hs91a_manuscripts": "5681f6e0f62b4334aef1f315f45646ab",
    "eth_hs91a_notes": "8dd65990513c462eb1f45dd366c8d26f",
    "eth_hs91a_otherauthors": "a96e1b08172c4ff5a7e1ca3f98251003",
}

def retrieve(item):
    label, record_id = item
    url = f"https://vls.hsa.ethz.ch/client/api/Data/GetArchivplanChildrenHtml?id={record_id}"
    start = time.monotonic()
    result = {"label": label, "url": url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            path = BASE / "sources" / ("algebra_history_" + label + ".json")
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
    results = list(pool.map(retrieve, IDS.items()))
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "seconds": time.monotonic() - start, "results": results}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_weyl30.json").write_text(text + "\n")
print(text)
