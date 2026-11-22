"""One public IA collection inventory, without the previously tested year filter.

No item files are requested. If a record is discovered, its public metadata must
be inspected for restrictions before any separate download decision.
"""
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

base = pathlib.Path(__file__).resolve().parents[1]
query = 'collection:pub_israel-journal-of-mathematics'
params = [('q', query), ('output', 'json'), ('rows', '1000'), ('page', '1')]
params += [('fl[]', key) for key in ['identifier', 'title', 'date', 'year', 'volume', 'access-restricted-item']]
url = 'https://archive.org/advancedsearch.php?' + urllib.parse.urlencode(params)
record = {
    'route': 'full public journal collection inventory without a year filter',
    'previously_completed_distinct_queries': [
        'collection:pub_israel-journal-of-mathematics AND year:1994',
        'title:(Israel Journal of Mathematics) AND year:1994',
        'title:(Israel Journal of Mathematics) AND (87 OR 1994)',
        'identifier:sim_israel-journal-of-mathematics_1994*',
    ],
    'query': query,
    'requested_url': url,
    'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
}
start = time.monotonic()
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (public scholarly catalogue audit)'})
    with urllib.request.urlopen(req, timeout=40) as response:
        data = response.read()
        record.update({'http_status': response.status, 'final_url': response.url,
                       'content_type': response.headers.get('Content-Type'),
                       'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                       'response': json.loads(data)})
except Exception as error:
    record['error'] = repr(error)
    if isinstance(error, urllib.error.HTTPError):
        record['http_status'] = error.code
record.update({'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'elapsed_seconds': time.monotonic() - start,
               'item_downloads_requested': False})
out = base / 'logs/B_Gabber_IA_collection_inventory.json'
out.write_text(json.dumps(record, indent=2, ensure_ascii=False) + '\n')
result = record.get('response', {}).get('response', {})
print(json.dumps({key: record.get(key) for key in ['http_status', 'error', 'completed_utc', 'elapsed_seconds']}))
print(json.dumps({'numFound': result.get('numFound'), 'docs': result.get('docs', [])}, ensure_ascii=False))
