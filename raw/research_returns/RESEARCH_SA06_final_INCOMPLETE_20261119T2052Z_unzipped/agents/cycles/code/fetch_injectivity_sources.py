"""Recover the five primary PDFs; retain fresh download runtimes and hashes."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess
import time
import urllib.request

base=Path(__file__).resolve().parents[1];src=base/'sources';out=base/'output'
src.mkdir(exist_ok=True);out.mkdir(exist_ok=True)
sources=[('Kerz2009Milnor','https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf'),
 ('Braunling2013','https://nyjm.albany.edu/j/2013/19-28p.pdf'),
 ('PatelRavindraInfinitesimal','https://www.math.purdue.edu/~patel471/inflift.pdf'),
 ('PatelRavindraNoetherLefschetz','https://www.math.purdue.edu/~patel471/inltv21Feb.pdf'),
 ('Saito2002BlochDeligne','https://arxiv.org/pdf/math/9910113')]
def fetch(item):
    name,url=item;start=time.perf_counter()
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 research-primary-source-verification'})
        with urllib.request.urlopen(req,timeout=50) as response:data=response.read()
        if not data.startswith(b'%PDF'):raise ValueError('not a PDF')
        p=src/(name+'.pdf');p.write_bytes(data)
        result=subprocess.run(['pdftotext','-layout',str(p),str(src/(name+'.txt'))],capture_output=True,text=True)
        if result.returncode:raise RuntimeError(result.stderr)
        return {'name':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                'runtime_seconds':time.perf_counter()-start,'status':'downloaded and text extracted'}
    except Exception as error:
        return {'name':name,'url':url,'runtime_seconds':time.perf_counter()-start,'status':'failed','error':str(error)}
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,sources))
record={'utc':datetime.now(timezone.utc).isoformat(),'recovery_rerun':True,
        'sources':rows,'runtime_seconds':time.perf_counter()-start}
data=json.dumps(record,indent=2)+'\n';(out/'fetch_injectivity_sources.json').write_text(data)
(out/'fetch_injectivity_sources.out').write_text(data);print(data)
