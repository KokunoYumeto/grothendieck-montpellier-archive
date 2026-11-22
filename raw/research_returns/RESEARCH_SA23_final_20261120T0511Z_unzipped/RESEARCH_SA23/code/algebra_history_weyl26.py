"""Two bounded public catalogue queries for the independently documented Weyl fonds.

Uses the public search and SearchBySignatur functions of the downloaded client.
No requests for orders, authorization, downloads or nonpublic records are made.
"""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import time
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parents[1]
payload = {
    "query": {"searchGroups": [{"searchFields": [
        {"key": "allData", "value": '"Hermann Weyl"'},
        {"key": "creationPeriod", "value": None}], "fieldOperator": 1}],
        "groupOperator": 1},
    "paging": {"skip": 0, "take": 20, "orderBy": "relevanz", "sortOrder": ""},
    "options": {"enableExplanations": False, "enableHighlighting": True,
                "enableAggregations": True},
    "facetsFilters": None, "advancedSearch": False,
}
REQUESTS = [
    ("eth_weyl_search", "https://vls.hsa.ethz.ch/client/api/Data/Search?language=de", payload),
    ("eth_hs91_search", "https://vls.hsa.ethz.ch/client/api/Data/SearchBySignatur?signatur=" + urllib.parse.quote("Hs 91"), None),
]

def retrieve(item):
    label, url, body = item
    start = time.monotonic()
    result = {"label": label, "url": url, "payload": body}
    try:
        req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                     headers={"Content-Type": "application/json"} if body else {})
        with urllib.request.urlopen(req, timeout=25) as response:
            data = response.read()
            path = BASE / "sources" / ("algebra_history_" + label + ".json")
            path.write_bytes(data)
            result.update(status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"),
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                          file=str(path))
    except Exception as error:
        result["error"] = repr(error)
        if hasattr(error, "read"):
            data = error.read()
            path = BASE / "sources" / ("algebra_history_" + label + "_error.txt")
            path.write_bytes(data)
            result["error_body_file"] = str(path)
    result["seconds"] = time.monotonic() - start
    return result

start = time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(retrieve, REQUESTS))
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "seconds": time.monotonic() - start, "results": results}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_weyl26.json").write_text(text + "\n")
print(text)
