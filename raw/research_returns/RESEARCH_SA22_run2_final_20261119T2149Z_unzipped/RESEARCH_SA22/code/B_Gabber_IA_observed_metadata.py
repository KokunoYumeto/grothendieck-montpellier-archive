"""Read two observed public IA catalogue records; never request item files."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
inventory = json.loads((root/'logs/B_Gabber_IA_collection_inventory.json').read_text())
observed = {x['identifier'] for x in inventory['response']['response']['docs']}
targets = ['israel-journal-of-mathematics_1993_84_contents',
           'israel-journal-of-mathematics_1963-1997_1-100_cumulative-index']
assert all(x in observed for x in targets)

def fetch(identifier):
    url = 'https://archive.org/metadata/' + identifier
    entry = {'identifier': identifier, 'observed_in': 'logs/B_Gabber_IA_collection_inventory.json',
             'requested_url': url, 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    start = time.monotonic()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (public scholarly catalogue audit)'}), timeout=40) as r:
            body = r.read()
            entry.update({'http_status':r.status, 'final_url':r.url, 'bytes':len(body),
                          'sha256':hashlib.sha256(body).hexdigest(), 'response':json.loads(body)})
    except Exception as error:
        entry['error'] = repr(error)
        if isinstance(error, urllib.error.HTTPError):entry['http_status'] = error.code
    entry.update({'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'elapsed_seconds':time.monotonic()-start, 'item_files_requested':False})
    return entry

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    result = list(pool.map(fetch, targets))
(root/'logs/B_Gabber_IA_observed_metadata.json').write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
for entry in result:
    response = entry.get('response', {})
    metadata = response.get('metadata', {})
    selected = {k:v for k,v in metadata.items() if any(t in k.lower() for t in ['next','prev','restrict','dark','title','volume','date','collection','identifier'])}
    print(json.dumps({'identifier':entry['identifier'], 'status':entry.get('http_status'),
                      'error':entry.get('error'), 'top_level_is_dark':response.get('is_dark'),
                      'metadata_selected':selected, 'completed_utc':entry['completed_utc']},ensure_ascii=False))
