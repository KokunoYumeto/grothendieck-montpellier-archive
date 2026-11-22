"""Read-only public catalogue probes for the exact Gabber 1994 article."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = 'https://api.openaire.eu/search/publications?'
QUERIES = {
    'doi': {'doi': '10.1007/BF02773001', 'format': 'json'},
    'title': {'title': 'Affine analog of the proper base change theorem', 'format': 'json'},
}

def fetch(item):
    key, query = item
    url = BASE + urllib.parse.urlencode(query)
    started = time.perf_counter()
    row = {'query': key, 'url': url}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Public-source-research/1.0'})
        with urllib.request.urlopen(request, timeout=35) as response:
            raw = response.read()
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get('Content-Type'),
                       bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
            try:
                row['response'] = json.loads(raw)
            except ValueError:
                row['response_text'] = raw.decode('utf-8', errors='replace')
    except Exception as exc:
        row['error'] = str(exc)
    row['elapsed_seconds'] = time.perf_counter() - started
    return row

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(fetch, QUERIES.items()))
data = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'purpose': 'Exact original-source discovery; metadata is not original text',
        'results': results}
path = ROOT / 'logs' / 'B_Gabber_OpenAIRE.json'
path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
for row in results:
    print(row['query'], row.get('status'), row.get('bytes'), row.get('error', ''))
print(path)
