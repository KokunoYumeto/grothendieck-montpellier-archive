#!/usr/bin/env python3
"""Fetch the exact public arXiv version and source used in the source audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib,json,time,urllib.request,gzip,tarfile,io,subprocess
root=Path(__file__).resolve().parents[1]
items=[('ROOT_Bhatt_algebraization_v1.pdf','https://arxiv.org/pdf/1404.7483v1'),('ROOT_Bhatt_algebraization_v1.source','https://arxiv.org/src/1404.7483v1')]
def fetch(item):
 name,url=item;start=time.perf_counter();r={'file':'literature/'+name,'url':url,'requested_utc':datetime.now(timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=35) as response:
   body=response.read();r.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
  if name.endswith('.pdf') and not body.startswith(b'%PDF'):raise ValueError('Non-PDF response')
  if name.endswith('.source') and body.lstrip().startswith(b'<!DOCTYPE html'):raise ValueError('HTML response, not source')
  p=root/'literature'/name;p.write_bytes(body);r.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
  if name.endswith('.pdf'):
   subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  else:
   dest=root/'literature/ROOT_Bhatt_algebraization_v1_source';dest.mkdir(exist_ok=True)
   if tarfile.is_tarfile(p):
    with tarfile.open(p) as archive:
     for member in archive.getmembers():
      if not member.isfile():continue
      target=dest/member.name
      if not target.resolve().is_relative_to(dest.resolve()):raise ValueError('unsafe archive path')
      target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(archive.extractfile(member).read())
   else:
    data=gzip.decompress(body) if body[:2]==b'\x1f\x8b' else body
    (dest/'source.tex').write_bytes(data)
   r['source_files']=[str(x.relative_to(root)) for x in dest.rglob('*') if x.is_file()]
  r['outcome']='saved'
 except Exception as e:r.update(outcome='failed',error=repr(e))
 r['elapsed_seconds']=round(time.perf_counter()-start,3);return r
with ThreadPoolExecutor(max_workers=2) as pool:records=list(pool.map(fetch,items))
(root/'logs/ROOT_Bhatt_algebraization_fetch.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
