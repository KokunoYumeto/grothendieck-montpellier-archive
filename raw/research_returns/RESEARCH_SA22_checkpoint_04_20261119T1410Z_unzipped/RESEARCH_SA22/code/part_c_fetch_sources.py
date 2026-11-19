#!/usr/bin/env python3
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,time,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
SOURCES=[
('c_EGA_IV4.pdf','https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf'),
('c_HLP_Inequalities.pdf','https://mathematicalolympiads.wordpress.com/wp-content/uploads/2012/08/inequalities-hardy-littlewood-polya.pdf'),
('c_Milne_AGS.pdf','https://www.jmilne.org/math/CourseNotes/AGS.pdf')]
def fetch(item):
 name,url=item; dest=ROOT/'sources'/name; start=time.perf_counter()
 rec={'name':name,'url':url,'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
 try:
  if not dest.exists():
   with urllib.request.urlopen(url,timeout=45) as r, dest.with_suffix('.part').open('wb') as f:
    while True:
     b=r.read(1024*1024)
     if not b: break
     f.write(b)
   dest.with_suffix('.part').rename(dest)
  b=dest.read_bytes()
  rec.update(status='downloaded',bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
 except Exception as e: rec.update(status='failed',error=type(e).__name__+': '+str(e))
 rec['runtime_seconds']=time.perf_counter()-start
 print(json.dumps(rec),flush=True)
 return rec
with ThreadPoolExecutor(max_workers=3) as pool:
 results=list(pool.map(fetch,SOURCES))
(ROOT/'code'/'part_c_fetch_sources_output.json').write_text(json.dumps(results,indent=2)+'\n')
