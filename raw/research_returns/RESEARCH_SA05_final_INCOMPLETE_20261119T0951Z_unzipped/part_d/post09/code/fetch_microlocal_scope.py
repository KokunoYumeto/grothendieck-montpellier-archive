"""Archive the exact primary HTML versions consulted in the C6 scope check."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources"
OUTPUT = ROOT / "output"
SOURCE.mkdir(parents=True, exist_ok=True)
OUTPUT.mkdir(parents=True, exist_ok=True)
URLS = [
    ("Saito2021DirectImageV4", "https://arxiv.org/html/1704.04832v4"),
    ("Saito2026MixedSupportV2", "https://arxiv.org/html/2501.07965v2"),
    ("SaitoXiongYang2026MicrolocalV3", "https://arxiv.org/html/2609.06625v3"),
    ("SaitoPublicationList20261119", "https://www.ms.u-tokyo.ac.jp/~t-saito/publ.html"),
]

def fetch(item):
    name, url = item
    record = {"name": name, "url": url,
              "checked_utc": datetime.now(timezone.utc).isoformat()}
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0 (primary-source research audit)"})
        with urlopen(req, timeout=45) as response:
            data = response.read()
            record["resolved_url"] = response.url
        path = SOURCE / f"{name}.html"
        path.write_bytes(data)
        record.update(status="obtained", path=str(path), bytes=len(data),
                      sha256=sha256(data).hexdigest())
    except Exception as exc:
        record.update(status="failed", error=f"{type(exc).__name__}: {exc}")
    return record

with ThreadPoolExecutor(max_workers=4) as executor:
    records = list(executor.map(fetch, URLS))
result = {"created_utc": datetime.now(timezone.utc).isoformat(), "sources": records}
(OUTPUT / "microlocal_source_fetch.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
