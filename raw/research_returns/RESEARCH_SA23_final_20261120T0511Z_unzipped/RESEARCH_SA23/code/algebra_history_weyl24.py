"""Read the public archive search client's advertised JavaScript.

The landing HTML returned at /client/ contains a client/main... relative URL.
We first resolve it literally against the landing URL. This is metadata-search
client inspection only; no restricted archive item is requested.
"""
import hashlib
import json
from pathlib import Path
import time
import urllib.parse
import urllib.request

BASE = Path(__file__).resolve().parents[1]
url = urllib.parse.urljoin("https://vls.hsa.ethz.ch/client/", "client/main.f10cd73e75c02d20.js")
start = time.monotonic()
result = {"url": url}
try:
    with urllib.request.urlopen(url, timeout=25) as response:
        data = response.read()
        path = BASE / "sources" / "algebra_history_eth_archive_client.js"
        path.write_bytes(data)
        result.update(status=response.status, final_url=response.url,
                      content_type=response.headers.get("Content-Type"),
                      bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                      file=str(path))
except Exception as error:
    result["error"] = repr(error)
result["seconds"] = time.monotonic() - start
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "result": result}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_weyl24.json").write_text(text + "\n")
print(text)
