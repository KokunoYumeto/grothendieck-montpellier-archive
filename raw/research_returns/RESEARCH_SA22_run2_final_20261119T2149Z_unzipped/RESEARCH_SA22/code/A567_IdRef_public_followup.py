#!/usr/bin/env python3
"""Bounded public IdRef retrieval; observed catalogue/API endpoints only."""
import concurrent.futures
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]

def retrieve(name, url):
    start = time.perf_counter()
    stamp = datetime.now(timezone.utc).isoformat()
    row = {'name': name, 'url': url, 'started_at_utc': stamp}
    try:
        with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=25) as r:
            data = r.read()
            dest = ROOT / 'literature' / ('A567_IdRef_' + name)
            dest.write_bytes(data)
            row.update(http_status=r.status, final_url=r.url,
                       content_type=r.headers.get('Content-Type'), bytes=len(data),
                       sha256=hashlib.sha256(data).hexdigest(),
                       saved=str(dest.relative_to(ROOT)))
    except Exception as e:
        row.update(error=type(e).__name__, message=str(e))
    row.update(finished_at_utc=datetime.now(timezone.utc).isoformat(),
               elapsed_seconds=time.perf_counter()-start)
    return row

if __name__ == '__main__':
    targets = [
      ('Gabber_authority.html', 'https://www.idref.fr/076074897'),
      ('Gabber_authority.rdf', 'https://www.idref.fr/076074897.rdf'),
      ('public_sparql_form.html', 'https://data.idref.fr/sparql'),
    ]
    start=time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(lambda t: retrieve(*t), targets))
    out={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),
         'scope':'Three observed public endpoints; no login or restricted-resource workaround.',
         'requests_count':len(targets), 'elapsed_seconds':time.perf_counter()-start,
         'results':results}
    (ROOT/'logs/A567_IdRef_initial_fetch.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
