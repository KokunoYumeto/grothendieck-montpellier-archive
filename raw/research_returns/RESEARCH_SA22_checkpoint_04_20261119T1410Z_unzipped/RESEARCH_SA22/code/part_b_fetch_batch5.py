#!/usr/bin/env python3
"""Opened/verified primary sources; retrieval failures retained, bounded wall time."""
import concurrent.futures, hashlib, json, subprocess, time
from pathlib import Path
root=Path(__file__).resolve().parents[1]
jobs=[('bosch_formal2008.pdf', 'https://www.uni-muenster.de/IVV5WS/WebHop/user/weckerm/heft378.pdf'), ('bosch_rigid2014.pdf', 'https://www.math.purdue.edu/~tongliu/seminar/rigid/Bosch.pdf'), ('lurie_htt2017.pdf', 'https://people.math.harvard.edu/~lurie/papers/HTT.pdf'), ('grauert1960.pdf', 'https://www.numdam.org/item/10.1007/BF02684746.pdf')]

def fetch(job):
 name,url=job;p=root/'sources'/name;t=time.perf_counter()
 try:
  status='existing'
  if not p.exists():
   tmp=p.with_suffix('.download')
   r=subprocess.run(['curl','-L','--fail','--max-time','240','-A','Mozilla/5.0','-o',str(tmp),url],capture_output=True,timeout=250)
   if r.returncode:return {'file':name,'url':url,'status':'error','error':r.stderr.decode()[-500:]}
   if not tmp.read_bytes().startswith(b'%PDF'):return {'file':name,'url':url,'status':'non-PDF','bytes':tmp.stat().st_size}
   tmp.rename(p);status='downloaded'
  b=p.read_bytes();subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,check=True,timeout=45)
  return {'file':name,'url':url,'status':status,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'seconds':time.perf_counter()-t}
 except Exception as e:return {'file':name,'url':url,'status':'error','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 out=[]
 for r in ex.map(fetch,jobs):out.append(r);print(r['file'],r['status'],r.get('bytes',r.get('error')),flush=True)
(root/'code'/'part_b_fetch_batch5_output.json').write_text(json.dumps(out,indent=2)+'\n')
