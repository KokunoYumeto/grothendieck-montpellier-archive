"""One ordinary anonymous search in ETH's public archival catalogue.

The endpoint, enum values and payload structure are read from its public client:
Qg.createSearchModelFromSimple, simple-search._search and searchService.search.
If access, rate-limit or captcha restrictions appear, this script records them
and does not retry or request any protected archive material.
"""
import hashlib
import json
from pathlib import Path
import time
import urllib.request

BASE = Path(__file__).resolve().parents[1]
url = "https://vls.hsa.ethz.ch/client/api/Data/Search?language=de"
payload = {
    "query": {"searchGroups": [{"searchFields": [
        {"key": "allData", "value": "Grothendieck"},
        {"key": "creationPeriod", "value": None}], "fieldOperator": 1}],
        "groupOperator": 1},
    "paging": {"skip": 0, "take": 20, "orderBy": "relevanz", "sortOrder": ""},
    "options": {"enableExplanations": False, "enableHighlighting": True,
                "enableAggregations": True},
    "facetsFilters": None,
    "advancedSearch": False,
}
start = time.monotonic()
result = {"url": url, "method": "POST", "payload": payload}
try:
    request = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=25) as response:
        data = response.read()
        path = BASE / "sources" / "algebra_history_eth_grothendieck_search.json"
        path.write_bytes(data)
        result.update(status=response.status, final_url=response.url,
                      content_type=response.headers.get("Content-Type"),
                      bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                      file=str(path))
except Exception as error:
    result["error"] = repr(error)
    if hasattr(error, "read"):
        data = error.read()
        path = BASE / "sources" / "algebra_history_eth_grothendieck_search_error.txt"
        path.write_bytes(data)
        result["error_body_file"] = str(path)
result["seconds"] = time.monotonic() - start
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "result": result}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_weyl25.json").write_text(text + "\n")
print(text)
