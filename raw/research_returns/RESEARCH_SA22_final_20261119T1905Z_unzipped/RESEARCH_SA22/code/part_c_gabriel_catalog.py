#!/usr/bin/env python3
"""Search public catalogue metadata only; never request restricted content."""
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
results = []
query = 'title:(Proceedings London Mathematical Society) AND volume:33'
url = 'https://archive.org/advancedsearch.php?' + urllib.parse.urlencode({'q': query, 'output': 'json', 'rows': 20})
entry = {'name': 'volume33_public_search', 'url': url, 'started_utc': datetime.now(timezone.utc).isoformat()}
try:
    with urllib.request.urlopen(url, timeout=30) as r:
        raw = r.read()
    data = json.loads(raw)
    target = root / 'sources/gabriel1932_volume33_catalog.json'
    target.write_bytes(raw)
    docs = data.get('response', {}).get('docs', [])
    entry.update(found=data.get('response', {}).get('numFound'), saved=str(target.relative_to(root)), records=[{k: d.get(k) for k in ('identifier','title','date','volume')} for d in docs])
    results.append(entry)
    for d in docs:
        identifier = d.get('identifier')
        if not identifier:
            continue
        meta_url = 'https://archive.org/metadata/' + urllib.parse.quote(identifier, safe='')
        item = {'name': identifier, 'url': meta_url, 'started_utc': datetime.now(timezone.utc).isoformat()}
        try:
            with urllib.request.urlopen(meta_url, timeout=30) as r:
                mraw = r.read()
            m = json.loads(mraw)
            md = m.get('metadata', {})
            candidates = [{k: f.get(k) for k in ('name','format','private','size')} for f in m.get('files', []) if f.get('name','').lower().endswith(('.pdf','.txt','.djvu','.epub'))]
            meta_target = root / ('sources/gabriel1932_' + identifier + '_metadata.json')
            meta_target.write_bytes(mraw)
            item.update(metadata={k: md.get(k) for k in ('title','date','volume','access-restricted-item','is_dark','collection')}, candidate_files=candidates, saved=str(meta_target.relative_to(root)))
            item['action'] = 'Public metadata inspected only. No PDF, OCR, preview image or encrypted file requested.'
        except Exception as e:
            item['error'] = f'{type(e).__name__}: {e}'
        results.append(item)
except Exception as e:
    entry['error'] = f'{type(e).__name__}: {e}'
    results.append(entry)
out = {'runtime_seconds': time.perf_counter() - start, 'results': results}
Path(__file__).with_name('part_c_gabriel_catalog_output.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
