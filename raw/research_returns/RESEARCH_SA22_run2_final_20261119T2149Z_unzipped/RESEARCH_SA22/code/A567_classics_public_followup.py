#!/usr/bin/env python3
"""Bounded public source discovery and exact-edition metadata check."""
import concurrent.futures,hashlib,json,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen

ROOT=Path(__file__).resolve().parents[1]
targets=[
 ('LehtoVirtanen_SciSpace.html','https://scispace.com/papers/quasiconformal-mappings-in-the-plane-4hgdgoprrd'),
 ('LehtoVirtanen_DOI_65513.json','https://api.crossref.org/works/10.1007/978-3-642-65513-5'),
 ('LehtoVirtanen_DOI_65515.json','https://api.crossref.org/works/10.1007/978-3-642-65515-9'),
]
def fetch(t):
 name,url=t;start=time.perf_counter()
 r={'name':name,'url':url,'started_at_utc':datetime.now(timezone.utc).isoformat()}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as f:
   data=f.read();p=ROOT/'literature'/('A567_'+name);p.write_bytes(data)
   r.update(http_status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'),
            bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),saved=str(p.relative_to(ROOT)))
 except Exception as e:r.update(error=type(e).__name__,message=str(e))
 r.update(finished_at_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-start)
 return r
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,targets))
out={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Public discovered source page and exact DOI registration checks; no authentication','requests_count':len(targets),'elapsed_seconds':time.perf_counter()-start,'results':rows}
(ROOT/'logs/A567_classics_public_fetch.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
