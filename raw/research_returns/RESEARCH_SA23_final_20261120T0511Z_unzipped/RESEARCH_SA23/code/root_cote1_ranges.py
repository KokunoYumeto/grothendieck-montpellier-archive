"""Resumable parallel byte-range retrieval of the public cote 1 PDF.

The server's checked HEAD response advertises 84,267,714 bytes and byte
ranges. A response which ignores the range is rejected before reading it.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib, json, time, urllib.request

root = Path(__file__).resolve().parents[1]
url = 'https://grothendieck.umontpellier.fr/1.pdf'
length = 84267714
step = 4 * 1024 * 1024
cache = root / 'sources' / 'root_cote1_ranges'
cache.mkdir(exist_ok=True)
started = time.perf_counter()

def fetch(index):
    first, last = index * step, min((index+1)*step, length)-1
    path = cache / f'{index:03d}.part'
    expected = last-first+1
    if path.exists() and path.stat().st_size == expected:
        return {'index':index,'bytes':expected,'cached':True}
    request = urllib.request.Request(url, headers={'Range':f'bytes={first}-{last}'})
    tick = time.perf_counter()
    with urllib.request.urlopen(request, timeout=90) as response:
        if response.status != 206:
            raise RuntimeError(f'Range {index}: expected 206, got {response.status}')
        content_range = response.headers.get('Content-Range')
        if content_range != f'bytes {first}-{last}/{length}':
            raise RuntimeError(f'Unexpected range header: {content_range}')
        data = response.read()
    if len(data) != expected:
        raise RuntimeError(f'Range {index}: expected {expected} bytes, got {len(data)}')
    path.write_bytes(data)
    return {'index':index,'bytes':len(data),'cached':False,
            'elapsed_seconds':time.perf_counter()-tick}

records = []
with ThreadPoolExecutor(max_workers=6) as pool:
    futures = {pool.submit(fetch, index):index for index in range((length+step-1)//step)}
    for future in as_completed(futures):
        try:
            record = future.result()
        except Exception as error:
            record = {'index':futures[future], 'error':str(error)}
        records.append(record)
        print(json.dumps(record), flush=True)
if any('error' in record for record in records):
    failure = {'url':url,'chunks':sorted(records,key=lambda r:r['index']),
               'elapsed_seconds':time.perf_counter()-started}
    (root/'logs'/'root_cote1_ranges_partial.json').write_text(json.dumps(failure,indent=2)+'\n')
    raise SystemExit('Some byte ranges failed; completed ranges were preserved for retry.')
target = root/'sources'/'root_manuscript1_ranged.pdf'
with target.open('wb') as out:
    for index in range((length+step-1)//step):
        out.write((cache/f'{index:03d}.part').read_bytes())
record = {'url':url,'file':str(target.relative_to(root)),
          'bytes':target.stat().st_size,
          'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
          'chunks':sorted(records,key=lambda r:r['index']),
          'elapsed_seconds':time.perf_counter()-started}
(root/'logs'/'root_cote1_ranges.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='chunks'}), flush=True)
