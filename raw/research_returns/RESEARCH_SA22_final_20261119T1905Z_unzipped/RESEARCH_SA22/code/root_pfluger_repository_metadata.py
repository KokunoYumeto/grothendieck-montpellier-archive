"""Bounded public metadata searches for the missing Pfluger original.

No credentials, private content requests, or subscription bypasses are used.
The output records availability metadata, never a claim of reading an article.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
started = time.perf_counter()
title = 'Ueber die Konstruktion Riemannscher Flachen durch Verheftung'
jobs = [
    ('openalex_pfluger_title', 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': title, 'per-page': 10})),
    ('semanticscholar_pfluger_doi', 'https://api.semanticscholar.org/graph/v1/paper/DOI:10.18311/jims/1960/16922?' + urllib.parse.urlencode({'fields': 'title,year,authors,openAccessPdf,url,externalIds'})),
    ('hal_pfluger_title', 'https://api.archives-ouvertes.fr/search/?' + urllib.parse.urlencode({'q': 'title_t:"Konstruktion Riemannscher"', 'wt': 'json', 'rows': 20})),
    ('openaire_pfluger_title', 'https://api.openaire.eu/search/publications?' + urllib.parse.urlencode({'title': title, 'format': 'json', 'size': 10})),
    ('ia_pfluger_creator', 'https://archive.org/advancedsearch.php?' + urllib.parse.urlencode({'q': 'creator:(Pfluger) AND mediatype:texts', 'output': 'json', 'rows': 200})),
]

def read(job):
    name, url = job
    before = time.perf_counter()
    result = {'name': name, 'url': url}
    try:
        try:
            response = urllib.request.urlopen(url, timeout=30)
        except urllib.error.HTTPError as exc:
            response = exc
        data = response.read()
        target = ROOT / 'sources' / (name + '.json')
        target.write_bytes(data)
        result.update(status=response.status, bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest(),
                      saved=str(target.relative_to(ROOT)))
        try:
            payload = json.loads(data)
            if name.startswith('openalex'):
                result['count'] = payload.get('meta', {}).get('count')
                result['matches'] = [dict(id=x.get('id'), title=x.get('title'), year=x.get('publication_year'),
                                          open_access=x.get('open_access'), locations=x.get('locations'))
                                     for x in payload.get('results', [])]
            elif name.startswith('semanticscholar'):
                result['metadata'] = payload
            elif name.startswith('hal') or name.startswith('ia'):
                result['count'] = payload.get('response', {}).get('numFound')
                result['matches'] = payload.get('response', {}).get('docs', [])
            else:
                result['response_keys'] = list(payload) if isinstance(payload, dict) else []
        except (ValueError, TypeError):
            result['json_parse'] = 'response not JSON'
    except Exception as exc:
        result['error'] = str(exc)
    result['seconds'] = time.perf_counter() - before
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    rows = list(executor.map(read, jobs))
out = dict(requests=len(jobs), seconds=time.perf_counter()-started, results=rows)
target = ROOT / 'code/root_pfluger_repository_metadata_output.json'
target.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
