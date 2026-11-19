#!/usr/bin/env python3
"""Keep requests, URLs and hashes; exclude third-party full-text caches from deliverables."""
from pathlib import Path
import json,re,hashlib,shutil,datetime
root=Path(__file__).resolve().parents[2];cache=root/'external_cache/root_earlier_web';cache.mkdir(parents=True,exist_ok=True)
for p in sorted((root/'work/outputs').glob('web_*.json')):
    # Immutable original retrieval bodies are retained only as transient research cache.
    target=cache/p.name
    if target.exists():
        if target.read_bytes()!=p.read_bytes():raise ValueError('Conflicting retrieval cache')
        p.unlink()
    else:shutil.move(str(p),str(target))
files=sorted(cache.glob('web_*.json'))+sorted((root/'external_cache').glob('root_web_*.json'))
records=[]
for p in files:
    raw=p.read_bytes();d=json.loads(raw);res=d.get('result',d)
    s=json.dumps(res,ensure_ascii=False)
    urls=sorted({u.rstrip('.,);]\\') for u in re.findall(r'https?://[^\s<>"\\]+',s)})
    refs=sorted(set(re.findall(r'turn\d+(?:search|view|fetch)\d+',s)))
    num=re.search(r'web_(\d+)',p.name).group(1)
    records.append({'id':'S63-'+num,'recorded_date':d.get('date','2026-11-19; exact request timestamp was not retained'),
       'request':d.get('args'), 'request_scope':'exact saved tool arguments' if 'args' in d else 'Only response metadata survives in this file; original exact arguments are not reconstructed.',
       'response_sha256':hashlib.sha256(raw).hexdigest(),'source_urls':urls,'source_refs':refs,
       'cache_excluded_from_delivery':True})
records.sort(key=lambda x:x['id'])
out=root/'work/parts/cote63/search_requests.json';out.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'retrieval_batches':len(records),'with_exact_arguments':sum(r['request'] is not None for r in records),'output':str(out)}))
