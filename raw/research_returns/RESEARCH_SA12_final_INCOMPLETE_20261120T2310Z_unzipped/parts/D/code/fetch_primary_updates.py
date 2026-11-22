from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import urllib.request, hashlib, json, subprocess, time
root=Path(__file__).resolve().parents[1];dest=root/'sources';start=time.perf_counter()
items=[('SGA4_IX','https://www.normalesup.org/~forgogozo/SGA4/09/09.pdf'),('SGA4_XVII','https://www.normalesup.org/~forgogozo/SGA4/17/17.pdf'),('SGA4_XVIII','https://www.normalesup.org/~forgogozo/SGA4/18/18.pdf'),('Raynaud1972','https://www.numdam.org/item/CM_1972__24_1_11_0.pdf'),('Schroer1999','https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/on_non_proj.pdf')]
def fetch(item):
    name,url=item;out={'name':name,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
    try:
        r=urllib.request.urlopen(url,timeout=35);out['status']=r.status;content=r.read();assert content.startswith(b'%PDF')
        p=dest/(name+'.pdf');p.write_bytes(content);out.update(bytes=len(content),sha256=hashlib.sha256(content).hexdigest(),path=str(p))
        z=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,text=True);out['pdftotext_exit']=z.returncode
    except Exception as e:out['error']=str(e)
    return out
with ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(fetch,items))
out={'results':results,'elapsed_seconds':time.perf_counter()-start};(root/'code/fetch_primary_updates_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
