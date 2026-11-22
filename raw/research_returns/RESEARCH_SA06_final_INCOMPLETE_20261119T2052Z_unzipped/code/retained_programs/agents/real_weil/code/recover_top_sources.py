#!/usr/bin/env python3
"""Recover the two opened Mukai primary preprints with fresh hashes and timings."""
from pathlib import Path
from time import perf_counter
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,urllib.request
started=perf_counter();base=Path(__file__).resolve().parents[1];dest=base/'sources';dest.mkdir(exist_ok=True)
jobs=[('mukai2011_raynaud','https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1736.pdf'),
      ('mukai2005_raynaud','https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1505.pdf')]
def get(job):
    name,url=job;t0=perf_counter()
    with urllib.request.urlopen(url,timeout=45) as response:content=response.read()
    assert content.startswith(b'%PDF'),name
    path=dest/(name+'.pdf');path.write_bytes(content)
    subprocess.run(['pdftotext','-layout',str(path),str(dest/(name+'.txt'))],check=True,capture_output=True)
    return {'name':name,'url':url,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),'runtime_seconds':perf_counter()-t0}
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(get,jobs))
record={'utc':datetime.now(timezone.utc).isoformat(),'recovered_after_reset':True,'sources':results,'runtime_seconds':perf_counter()-started}
(dest/'recovered_top_source_hashes.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
