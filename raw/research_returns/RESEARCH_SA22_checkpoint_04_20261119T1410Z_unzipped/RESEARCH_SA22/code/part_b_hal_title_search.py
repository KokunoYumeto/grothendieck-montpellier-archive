#!/usr/bin/env python3
"""Bounded HAL title discovery, allowing preprints/theses without journal DOIs."""
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
queries = [
    ('gabber1994', 'title_t:"Affine analog"'),
    ('fujiwara1995', 'title_t:"Theory of tubular neighborhood"'),
    ('lieberman1968', 'title_t:"Numerical and homological equivalence"'),
    ('raynaud_thesis1968', 'title_t:"Faisceaux amples"'),
]

def run(job):
    work, query = job
    request_started = time.monotonic()
    url = 'https://api.archives-ouvertes.fr/search/?' + urlencode({
        'q': query,
        'fl': 'title_s,authFullName_s,producedDate_s,uri_s,fileMain_s,linkExtUrl_s,doiId_s',
        'wt': 'json', 'rows': 25,
    })
    result = {'work': work, 'query': query, 'url': url}
    try:
        with urlopen(url, timeout=20) as response:
            raw = response.read()
            result.update(http_status=response.status, bytes=len(raw))
        data = json.loads(raw)
        result.update(status='metadata read', metadata=data,
                      hits=data.get('response', {}).get('numFound'))
    except Exception as exc:
        result.update(status='error', error=str(exc))
    result['elapsed_seconds'] = time.monotonic() - request_started
    print(json.dumps({key: val for key, val in result.items() if key != 'metadata'}), flush=True)
    return result

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(run, queries))
output = {'started_utc': started_utc, 'results': results,
          'elapsed_seconds': time.monotonic() - started,
          'scope': 'Four public title searches; no DOI restriction and no restricted file request.'}
(root / 'code/part_b_hal_title_search_output.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({'requests': len(results), 'elapsed_seconds': output['elapsed_seconds']}))
