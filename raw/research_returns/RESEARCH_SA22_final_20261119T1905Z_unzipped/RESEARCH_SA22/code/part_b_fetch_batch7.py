#!/usr/bin/env python3
"""Opened/verified primary sources; retrieval failures retained, bounded wall time."""
import concurrent.futures, hashlib, json, subprocess, time
from pathlib import Path
root=Path(__file__).resolve().parents[1]
jobs=[('lipman_neeman2007.pdf', 'https://www.math.purdue.edu/~jlipman/papers/quasiperfect.pdf'), ('christensen_scoccola2023.pdf', 'https://arxiv.org/pdf/2007.05833')]

def fetch(job):
 name,url=job;p=root/'sources'/name;t=time.perf_counter()
 try:
  status='existing'
  if not p.exists():
   tmp=p.with_suffix('.download')
   r=subprocess.run(['curl','-L','--fail','--max-time','100','-A','Mozilla/5.0','-o',str(tmp),url],capture_output=True,timeout=110)
   if r.returncode:return {'file':name,'url':url,'status':'error','error':r.stderr.decode()[-500:]}
   if not tmp.read_bytes().startswith(b'%PDF'):return {'file':name,'url':url,'status':'non-PDF','bytes':tmp.stat().st_size}
   tmp.rename(p);status='downloaded'
  b=p.read_bytes();subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,check=True,timeout=45)
  return {'file':name,'url':url,'status':status,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'seconds':time.perf_counter()-t}
 except Exception as e:return {'file':name,'url':url,'status':'error','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 out=[]
 for r in ex.map(fetch,jobs):out.append(r);print(r['file'],r['status'],r.get('bytes',r.get('error')),flush=True)
(root/'code'/'part_b_fetch_batch7_output.json').write_text(json.dumps(out,indent=2)+'\n')
