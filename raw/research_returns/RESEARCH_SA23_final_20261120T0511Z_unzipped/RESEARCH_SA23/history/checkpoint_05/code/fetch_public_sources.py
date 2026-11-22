"""Fetch an explicit batch of public source URLs and retain exact access records.

Input is one JSON object on stdin, with log_tag and items[{name,url}].
This utility supplies no credentials and does not circumvent gated access.
"""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, re, sys, time, urllib.request
import fitz
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
request = json.load(sys.stdin)
tag = request['log_tag']
assert re.fullmatch(r'[a-zA-Z0-9_-]+', tag)
def fetch(item):
    name, url = item['name'], item['url']
    assert re.fullmatch(r'[a-zA-Z0-9_-]+', name)
    assert url.startswith(('http://', 'https://'))
    begin = time.perf_counter(); record = {'name': name, 'url': url}
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
            record.update({'status': response.status, 'final_url': response.url,
                           'content_type': response.headers.get('Content-Type'),
                           'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        suffix = '.pdf' if data.startswith(b'%PDF') else '.html'
        path = root / 'sources' / (name + suffix)
        if path.exists() and path.read_bytes() != data:
            raise RuntimeError('Refusing to overwrite a distinct source cache')
        path.write_bytes(data); record['saved'] = str(path.relative_to(root))
        if suffix == '.pdf':
            document = fitz.open(path)
            texts = [page.get_text() for page in document]
            record['pages'] = len(document)
            record['native_text_characters'] = sum(map(len, texts))
            (root / 'sources' / (name + '_full.txt')).write_text('\n\f\n'.join(texts))
    except Exception as error:
        record['error'] = str(error)
    record['elapsed_seconds'] = time.perf_counter() - begin
    return record
with concurrent.futures.ThreadPoolExecutor(max_workers=min(4, len(request['items']))) as pool:
    results = list(pool.map(fetch, request['items']))
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'request': request, 'results': results,
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs' / (tag + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
