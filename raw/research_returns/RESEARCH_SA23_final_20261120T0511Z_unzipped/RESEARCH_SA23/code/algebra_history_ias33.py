"""Download the exact public Princeton C1245 EAD linked by its catalogue index."""
import hashlib
import json
from pathlib import Path
import time
import urllib.request
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parents[1]
url = "https://findingaids.princeton.edu/pacscl/production/C1245.xml"
start = time.monotonic()
result = {"url": url}
try:
    with urllib.request.urlopen(url, timeout=25) as response:
        data = response.read()
        path = BASE / "sources" / "algebra_history_princeton_vonneumann_C1245.xml"
        path.write_bytes(data)
        result.update(status=response.status, final_url=response.url,
                      content_type=response.headers.get("Content-Type"),
                      bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                      file=str(path))
        root = ET.fromstring(data)
        text = "\n".join(" ".join(x.itertext()).strip() for x in root.iter()
                         if x.tag.rsplit("}",1)[-1] in ["unittitle","unitdate","scopecontent","bioghist","accessrestrict","dao"])
        (BASE / "sources" / "algebra_history_princeton_vonneumann_C1245.txt").write_text(text + "\n")
        result["extracted_text_file"] = str(BASE / "sources" / "algebra_history_princeton_vonneumann_C1245.txt")
except Exception as error:
    result["error"] = repr(error)
result["seconds"] = time.monotonic() - start
report = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "result": result}
text = json.dumps(report, indent=2, ensure_ascii=False)
(BASE / "logs" / "algebra_history_ias33.json").write_text(text + "\n")
print(text)
