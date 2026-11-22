#!/usr/bin/env python3
"""Retain exact primary sources consulted for C.3at, with hashes and timing."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib,json,time,urllib.request,subprocess
started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
items=[
 ('bbe2005_witt_author.pdf','https://page.mi.fu-berlin.de/esnault/preprints/helene/80WittCohomology051014.pdf'),
 ('esnault2003_chow_rigid.pdf','https://page.mi.fu-berlin.de/esnault/preprints/helene/62-chowgroup.pdf'),
 ('huang_lian_yau_yu2018_hasse.pdf','https://archive.ymsc.tsinghua.edu.cn/pacm_download/311/8917-Hasse-Witt3.pdf')]
def fetch(item):
 name,url=item;t=time.perf_counter();p=base/'sources'/name
 try:
  data=urllib.request.urlopen(url,timeout=40).read()
  if not data.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
  p.write_bytes(data)
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  return {'name':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
          'runtime_seconds':time.perf_counter()-t,'status':'downloaded'}
 except Exception as e:
  return {'name':name,'url':url,'error':repr(e),'runtime_seconds':time.perf_counter()-t,'status':'failed'}
with ThreadPoolExecutor(max_workers=3) as pool: rows=list(pool.map(fetch,items))
record={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'sources':rows,
        'runtime_seconds':time.perf_counter()-started}
(base/'sources'/'ordinary_cy_source_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
