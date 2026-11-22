"""Fetch original SGA6 scans around the Neron--Severi finiteness theorem."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request, hashlib, json, time
root = Path(__file__).resolve().parents[1]
dest = root / 'parts/D/sources/SGA6_NS'
dest.mkdir(parents=True, exist_ok=True)
def fetch(name):
    url = 'https://wstein.org/sga/sga/6/' + name + '.jpeg'
    t = time.perf_counter()
    try:
        data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=30).read()
        (dest / (name+'.jpeg')).write_bytes(data)
        return dict(url=url, path=str((dest/(name+'.jpeg')).relative_to(root)), bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), seconds=time.perf_counter()-t)
    except Exception as exc:
        return dict(url=url, error=str(exc), seconds=time.perf_counter()-t)
with ThreadPoolExecutor(max_workers=5) as pool:
    records=list(pool.map(fetch, ['6a3i_3','6t_649','6t_650','6t_651','6t_652']))
record=dict(utc=datetime.now(timezone.utc).isoformat(), downloads=records)
(root/'code/output/fetch_sga6_ns_post16.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
