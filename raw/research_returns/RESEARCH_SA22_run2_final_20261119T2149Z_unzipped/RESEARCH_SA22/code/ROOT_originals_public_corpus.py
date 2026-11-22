#!/usr/bin/env python3
"""Inspect the public corpus catalogue/tree for the two exact original papers.

This is a bounded filename/catalogue search, not a search of PDF contents and
not evidence of global absence. No authenticated endpoint is used.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib,json,re,time,urllib.request
root=Path(__file__).resolve().parents[1]
urls=[
 'https://raw.githubusercontent.com/xhc144/algebraic-geometry-corpus/main/catalog.json',
 'https://api.github.com/repos/xhc144/algebraic-geometry-corpus/git/trees/main?recursive=1',
]
def fetch(url):
 start=time.perf_counter(); r={'url':url,'requested_utc':datetime.now(timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research-source-audit'}),timeout=30) as response:
   body=response.read();r.update(http_status=response.status,final_url=response.url,bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
  data=json.loads(body)
  if 'tree' in data:
   paths=[x['path'] for x in data['tree'] if x['type']=='blob']
   r.update(file_count=len(paths),truncated=data.get('truncated'),matches=[p for p in paths if re.search(r'gabber|fujiwara|tubular|proper.base|affine.analog',p,re.I)],extra_files=[p for p in paths if p.startswith('extra/')])
  else:
   r['catalogue']=data
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-start,3);return r
with ThreadPoolExecutor(max_workers=2) as pool:records=list(pool.map(fetch,urls))
(root/'logs/ROOT_originals_public_corpus.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
for r in records:print(json.dumps({k:v for k,v in r.items() if k!='catalogue'},ensure_ascii=False))
