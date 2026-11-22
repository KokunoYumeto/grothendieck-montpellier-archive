#!/usr/bin/env python3
"""Public CDX discovery for a named book listed in the 2020 access programme."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import datetime
import json
import time

root = Path(__file__).resolve().parents[1]
started = time.monotonic()
started_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
patterns = [
    'link.springer.com/*BFb0059504*',
    'link.springer.com/*978-3-540-36249-4*',
    'springerlink.com/content/978-3-540-36249-4*',
]

def run(pattern):
    t0 = time.monotonic()
    params = [('url', pattern), ('output', 'json'),
              ('filter', 'statuscode:200'), ('filter', 'mimetype:application/pdf'),
              ('collapse', 'urlkey'), ('fl', 'timestamp,original,mimetype,statuscode'),
              ('limit', '30')]
    url = 'https://web.archive.org/cdx/search/cdx?' + urlencode(params)
    record = {'pattern': pattern, 'url': url}
    try:
        with urlopen(url, timeout=20) as response:
            raw = response.read()
            record.update(http_status=response.status, bytes=len(raw))
        data = json.loads(raw)
        record.update(status='public archive metadata read', metadata=data,
                      snapshot_rows=max(0, len(data)-1))
    except Exception as exc:
        record.update(status='error', error=str(exc))
    record['elapsed_seconds'] = time.monotonic()-t0
    print(json.dumps({k:v for k,v in record.items() if k!='metadata'}), flush=True)
    return record

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(run, patterns))
output = {'started_utc': started_utc, 'results': results,
          'elapsed_seconds': time.monotonic()-started,
          'scope': 'Three public CDX catalogue queries; no original, restricted, encrypted or authenticated content URL requested.'}
(root/'code/part_b_raynaud_public_snapshots_output.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps({'requests': len(results), 'elapsed_seconds': output['elapsed_seconds']}))
