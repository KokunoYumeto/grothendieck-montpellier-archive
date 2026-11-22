from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from time import perf_counter
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parents[1]
items = [
    ("Rost1996_chow_coefficients.pdf", "https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf"),
    ("Rost1996_author_corrections.html", "https://www.math.uni-bielefeld.de/~rost/chowcoeff.html"),
]
start = datetime.now(timezone.utc)
tic = perf_counter()
records = []
for name, url in items:
    each = perf_counter()
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as response:
            data = response.read()
        path = root / "sources" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        records.append({"url": url, "file": str(path), "bytes": len(data),
                        "sha256": sha256(data).hexdigest(), "status": "downloaded",
                        "runtime_seconds": perf_counter()-each})
    except Exception as exc:
        records.append({"url": url, "status": "failed", "error": repr(exc),
                        "runtime_seconds": perf_counter()-each})
payload = {"started_utc": start.isoformat(),
           "finished_utc": datetime.now(timezone.utc).isoformat(),
           "runtime_seconds": perf_counter()-tic, "records": records}
out = root / "output" / "k2_cohomology_source_fetch.json"
out.write_text(json.dumps(payload, indent=2)+"\n")
print(json.dumps(payload, indent=2))
