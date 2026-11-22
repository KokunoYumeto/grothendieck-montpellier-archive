"""Read Hs 91a, the manuscript branch named in the public Weyl search results."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import time
import urllib.request

BASE = Path(__file__).resolve().parents[1]
ID = "4511846b9bd34adba98356cda7a42e59"
URLS = {
    "eth_hs91a_record": f"https://vls.hsa.ethz.ch/client/api/Data/GetEntity?id={ID}&language=de",
    "eth_hs91a_children": f"https://vls.hsa.ethz.ch/client/api/Data/GetArchivplanChildrenHtml?id={ID}",
}

def retrieve(item):
    label, url = item
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
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(retrieve, URLS.items()))
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
          "seconds": time.monotonic() - start, "results": results}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_weyl29.json").write_text(text + "\n")
print(text)
