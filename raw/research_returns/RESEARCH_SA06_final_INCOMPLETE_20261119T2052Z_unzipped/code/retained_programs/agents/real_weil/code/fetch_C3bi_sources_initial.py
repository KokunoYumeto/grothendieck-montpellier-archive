#!/usr/bin/env python3
"""Acquire the three newly opened primary sources, retaining times and hashes."""
from pathlib import Path
from datetime import datetime,timezone
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
import requests,json,hashlib,subprocess
base=Path(__file__).resolve().parents[1];out=base/'sources';out.mkdir(exist_ok=True)
sources=[('iwasa_kai2021_published.pdf','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/42DCFAFEE9CAE2011E983ABFADA02766/S1474748020000055a.pdf/isomorphisms_up_to_bounded_torsion_between_relative_k0groups_and_chow_groups_with_modulus.pdf'),('khan2020_blowup_v3.pdf','https://arxiv.org/pdf/1810.12858v3'),('huybrechts2023_cubics_final.pdf','https://www.math.uni-bonn.de/people/huybrech/Notes.pdf')]
started=datetime.now(timezone.utc).isoformat();tick=perf_counter()
def fetch(pair):
 name,url=pair;t0=perf_counter();rec={'file':name,'url':url,'started_utc':datetime.now(timezone.utc).isoformat()}
 try:
  r=requests.get(url,timeout=45);r.raise_for_status();assert r.content.startswith(b'%PDF'),r.headers.get('Content-Type')
  p=out/name;p.write_bytes(r.content);rec.update({'status':'saved','bytes':len(r.content),'sha256':hashlib.sha256(r.content).hexdigest()})
  q=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,text=True)
  rec['pdftotext_returncode']=q.returncode
 except Exception as e:rec.update({'status':'failed','error':str(e)})
 rec['runtime_seconds']=perf_counter()-t0;return rec
with ThreadPoolExecutor(max_workers=3) as pool: records=list(pool.map(fetch,sources))
record={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':perf_counter()-tick,'sources':records}
(base/'output/C3bi_sources_manifest.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
