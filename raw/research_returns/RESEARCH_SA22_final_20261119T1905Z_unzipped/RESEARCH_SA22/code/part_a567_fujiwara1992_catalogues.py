"""Targeted public metadata queries for the cited 1992 Fujiwara preprint.

No DOI is required, so separately catalogued earlier originals can appear.
The OpenAlex date window is explicit; OpenAIRE has no date restriction.
Neither request fetches journal text or retries a denied endpoint.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ('openaire', 'https://api.openaire.eu/search/publications?' + urlencode({
        'title': 'tubular', 'author': 'Fujiwara', 'format': 'json', 'size': 25,
    }), 'Title keyword and author, no DOI/year/OA restriction; inspect dates and versions individually'),
    ('openalex', 'https://api.openalex.org/works?' + urlencode({
        'search': 'Fujiwara tubular neighborhoods etale topology',
        'filter': 'from_publication_date:1990-01-01,to_publication_date:1994-12-31',
        'per-page': 25,
    }), 'Title/author terms with explicit1990-1994 date window; at most25 records'),
]


def fetch(target):
    service, url, scope = target
    result = {'service': service, 'url': url, 'scope': scope}
    start = time.perf_counter()
    try:
        with urlopen(url, timeout=35) as response:
            data = response.read(2 * 1024 * 1024 + 1)
            result.update(status=response.status, final_url=response.geturl(),
                          bytes=len(data), content_type=response.headers.get('Content-Type'))
        result['sha256'] = hashlib.sha256(data).hexdigest()
        result['truncated'] = len(data) > 2 * 1024 * 1024
        path = ROOT / f'code/part_a567_fujiwara1992_{service}_raw.json'
        path.write_bytes(data)
        result['saved_response'] = str(path.relative_to(ROOT))
        if not result['truncated']:
            metadata = json.loads(data)
            if service == 'openalex':
                result['total'] = metadata.get('meta', {}).get('count')
                result['records'] = [
                    {key: record.get(key) for key in
                     ('id', 'doi', 'title', 'publication_year', 'publication_date',
                      'primary_location', 'best_oa_location', 'locations')}
                    for record in metadata.get('results', [])
                ]
            else:
                result['header'] = metadata.get('response', {}).get('header')
    except Exception as error:
        result['error'] = f'{type(error).__name__}: {error}'
    result['elapsed_seconds'] = time.perf_counter() - start
    return result


started = time.perf_counter()
with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(fetch, TARGETS))
output = {'results': results, 'whole_batch_seconds': time.perf_counter() - started,
          'openaire_documentation': 'https://graph.openaire.eu/docs/10.2.0/apis/search-api/research-products/'}
(ROOT / 'code/part_a567_fujiwara1992_catalogues_output.json').write_text(
    json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
