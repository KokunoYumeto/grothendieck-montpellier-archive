"""Follow newly identified public author-archive and broader journal catalogues.

Reads only public finding aids/search metadata. It never requests private files.
"""
from pathlib import Path
import urllib.request, urllib.error, urllib.parse
import json, time, concurrent.futures, hashlib

ROOT = Path(__file__).resolve().parents[1]
started = time.perf_counter()
jobs = [('pfluger_eth_finding_aid', 'https://www.research-collection.ethz.ch/bitstreams/9e27aeb7-c9ad-41a2-8a4a-b90fd22e5c78/download')]
for name, query in [
    ('indian_mathematical_broad', 'title:(Indian Mathematical Society)'),
    ('indian_mathematical_golden', '"Indian Mathematical" AND ("1960" OR "1961" OR "Golden Jubilee")'),
]:
    params = [('q', query), ('rows', '500'), ('output', 'json')]
    params += [('fl[]', key) for key in ['identifier', 'title', 'creator', 'date', 'year', 'volume', 'description', 'collection', 'access-restricted-item']]
    jobs.append((name, 'https://archive.org/advancedsearch.php?' + urllib.parse.urlencode(params)))

def fetch(job):
    name, url = job
    start = time.perf_counter()
    try:
        try:
            response = urllib.request.urlopen(url, timeout=45)
        except urllib.error.HTTPError as error:
            response = error
        data = response.read()
        suffix = '.pdf' if data.startswith(b'%PDF') else '.json' if 'json' in response.headers.get('content-type', '') else '.html'
        target = ROOT / 'sources' / (name + suffix)
        target.write_bytes(data)
        result = dict(name=name, url=url, final_url=response.url, status=response.status,
                      content_type=response.headers.get('content-type'), bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest(), saved=str(target.relative_to(ROOT)),
                      seconds=time.perf_counter()-start)
        if suffix == '.json' and response.status == 200:
            records = json.loads(data).get('response', {})
            result['found'] = records.get('numFound')
            result['returned'] = len(records.get('docs', []))
        return result
    except Exception as error:
        return dict(name=name, url=url, error=str(error), seconds=time.perf_counter()-start)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch, jobs))
output = dict(requests=len(jobs), seconds=time.perf_counter()-started, results=results)
(ROOT/'code/root_pfluger_author_archive_output.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
