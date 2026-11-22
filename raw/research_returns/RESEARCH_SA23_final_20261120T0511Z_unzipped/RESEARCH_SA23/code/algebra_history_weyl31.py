"""Read the descriptive metadata for three generically titled Weyl note folders.

These ids are in the public Hs 91a notes list. Uses the public GetEntities
function so that uninformative catalogue titles are not mistaken for absence
of an unindexed enclosure. No physical document or restricted download is read.
"""
import hashlib
import json
from pathlib import Path
import time
import urllib.request

BASE = Path(__file__).resolve().parents[1]
IDS = ["246bc452c2cc474bb1999e68ac0e3fb3", "aa3c31bc250b4bdf816b845a9b29f85d", "7373bfafd1864e35a4d0f5d68d85ad12"]
url = "https://vls.hsa.ethz.ch/client/api/Data/GetEntities?ids=" + ",".join(IDS) + "&language=de"
start = time.monotonic()
result = {"url": url}
try:
    with urllib.request.urlopen(url, timeout=25) as response:
        data = response.read()
        path = BASE / "sources" / "algebra_history_eth_weyl_note_records.json"
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
(BASE / "logs" / "algebra_history_weyl31.json").write_text(text + "\n")
print(text)
