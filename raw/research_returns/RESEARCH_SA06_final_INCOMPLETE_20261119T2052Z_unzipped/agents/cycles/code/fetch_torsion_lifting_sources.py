"""Fetch exact primary PDFs used in the local torsion-lifting source audit."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import json
import urllib.request

BASE = Path(__file__).resolve().parents[1]
SOURCES = {
    "AlexandrouSchreieder2023_bloch.pdf": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/65A5FB842FB89629FED3B7BB8D603CA8/S2050509423000518a.pdf/on_blochs_map_for_torsion_cycles_over_nonclosed_fields.pdf",
    "ACMV_bloch0720_author.pdf": "https://www.math.colostate.edu/~achter/math/bloch0720.pdf",
}

def fetch(item):
    filename, url = item
    start = perf_counter()
    record = {"filename": filename, "url": url}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=35) as response:
            payload = response.read()
        if not payload.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        path = BASE / "sources" / filename
        path.write_bytes(payload)
        record.update(status="saved", bytes=len(payload), sha256=sha256(payload).hexdigest(), path=str(path))
    except Exception as error:
        record.update(status="failed", error=f"{type(error).__name__}: {error}")
    record["runtime_seconds"] = perf_counter() - start
    return record

if __name__ == "__main__":
    start = perf_counter()
    started = datetime.now(timezone.utc).isoformat()
    (BASE / "sources").mkdir(exist_ok=True)
    (BASE / "output").mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=2) as executor:
        records = list(executor.map(fetch, SOURCES.items()))
    result = {"started_utc": started, "files": records, "runtime_seconds": perf_counter() - start}
    output = json.dumps(result, indent=2)
    (BASE / "output" / "torsion_lifting_source_fetch.json").write_text(output + "\n")
    print(output)
