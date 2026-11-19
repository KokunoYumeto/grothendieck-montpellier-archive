"""Fetch primary mathematical sources for the C.3r proof and record provenance."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import time
import urllib.request
import fitz

root = Path(__file__).resolve().parents[1]
sources = [
    ("quillen1973", "https://people.math.rochester.edu/faculty/doug/otherpapers/Quillen-Higher-I.pdf"),
    ("skalit2017", "https://arxiv.org/pdf/1710.00303"),
    ("fu_vial_distinguished", "https://irma.math.unistra.fr/~lfu/articles/DistinguishedCycles.pdf"),
]

def fetch(item):
    name, url = item
    start = time.perf_counter()
    record = {"name": name, "url": url}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "ResearchSourceAudit/1.0"})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            record["http_status"] = response.status
        path = root / "sources" / (name+".pdf")
        path.write_bytes(data)
        document = fitz.open(path)
        (root / "sources" / (name+".txt")).write_text(
            "\n\n".join(f"PDF PAGE {i+1}\n"+p.get_text() for i, p in enumerate(document)))
        record.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                      pdf_pages=len(document), path=str(path))
    except Exception as error:
        record["error"] = str(error)
    record["runtime_seconds"] = time.perf_counter()-start
    return record

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, sources))
output = {"sources": results, "runtime_seconds": time.perf_counter()-start}
(root / "code" / "fetch_fermat_boundary_sources_output.json").write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps(output, indent=2))
