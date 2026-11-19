"""Retrieve the public GDZ article identified in its volume METS record."""
from pathlib import Path
import hashlib
import json
import time
import urllib.request
import xml.etree.ElementTree as ET

base = Path(__file__).resolve().parents[1]
src = base / "sources"
out = base / "output"
start = time.perf_counter()
mets_path = src / "Soule1984_volume_mets.xml"
root = ET.fromstring(mets_path.read_bytes())
matches = [el.attrib for el in root.iter()
           if el.tag.endswith("}div") and "Groupes de Chow" in el.attrib.get("LABEL", "")]
assert len(matches) == 1
log_id = matches[0]["ID"]
url = f"https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0268/{log_id}.pdf"
record = {"mets_url": "https://gdz.sub.uni-goettingen.de/mets/PPN235181684_0268.xml",
          "matched_article": matches[0], "url": url}
try:
    data = urllib.request.urlopen(url, timeout=55).read()
    assert data.startswith(b"%PDF"), "Response is not a PDF"
    path = src / "Soule1984.pdf"
    path.write_bytes(data)
    record.update(status="downloaded", path=str(path), bytes=len(data),
                  sha256=hashlib.sha256(data).hexdigest())
except Exception as error:
    record.update(status="failed", error=repr(error))
record["runtime_seconds"] = time.perf_counter() - start
(out / "fetch_soule1984.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(record, indent=2, ensure_ascii=False))
