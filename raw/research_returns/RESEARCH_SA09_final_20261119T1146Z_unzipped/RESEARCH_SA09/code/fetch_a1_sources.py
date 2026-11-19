"""Fetch exact primary-source URLs used for A.1; save byte hashes and timings."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, time, urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'krause_1203.0311_source': 'https://arxiv.org/src/1203.0311',
    'touze_2607.00631_source': 'https://arxiv.org/src/2607.00631',
    'touze_2607.00631.pdf': 'https://arxiv.org/pdf/2607.00631',
    'roby1963.pdf': 'https://www.numdam.org/article/ASENS_1963_3_80_3_213_0.pdf',
    'friedlander_suslin1997.pdf': 'https://dornsife.usc.edu/ericmfriedlander/wp-content/uploads/sites/233/2023/06/10.pdf',
}

def fetch(item):
    name, url = item
    start = time.monotonic()
    target = ROOT / 'sources' / name
    try:
        data = target.read_bytes() if target.exists() else urllib.request.urlopen(url, timeout=50).read()
        target.write_bytes(data)
        return dict(name=name, url=url, bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), elapsed=round(time.monotonic()-start,3))
    except Exception as exc:
        return dict(name=name, url=url, error=repr(exc), elapsed=round(time.monotonic()-start,3))

with ThreadPoolExecutor(max_workers=5) as pool:
    records = list(pool.map(fetch, SOURCES.items()))
text=json.dumps(records, indent=2)
(ROOT/'logs'/'fetch_a1_sources.json').write_text(text)
print(text)
