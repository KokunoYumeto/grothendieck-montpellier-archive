#!/usr/bin/env python3
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,time,urllib.request
ROOT=Path(__file__).resolve().parents[1]
SOURCES=[
 ('a2b_AhlforsBers1960.pdf','https://www.cimat.mx/~mmoreno/teaching/fall10/AhlforsBers.pdf'),
 ('a2b_Solynin1999.pdf','https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=1040&what=fullt')]
def fetch(item):
 name,url=item; start=time.perf_counter(); record={'name':name,'url':url}
 try:
  dest=ROOT/'sources'/name
  if not dest.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=40) as reply:
    raw=reply.read()
   if not raw.startswith(b'%PDF'): raise ValueError('Response is not a PDF')
   dest.write_bytes(raw)
  raw=dest.read_bytes()
  record.update(status='downloaded',bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
 except Exception as error:
  record.update(status='failed',error=type(error).__name__+': '+str(error))
 record['runtime_seconds']=time.perf_counter()-start
 print(json.dumps(record),flush=True)
 return record
with ThreadPoolExecutor(max_workers=2) as pool:
 results=list(pool.map(fetch,SOURCES))
(ROOT/'code'/'part_a2b_fetch_sources_output.json').write_text(json.dumps(results,indent=2)+'\n')
