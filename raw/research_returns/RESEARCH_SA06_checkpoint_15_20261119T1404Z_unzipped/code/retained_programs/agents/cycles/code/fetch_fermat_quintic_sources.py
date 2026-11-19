from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import urllib.request,hashlib,json,time,subprocess
b=Path(__file__).resolve().parents[1]
sources=[('ElZein1974','https://webusers.imj-prg.fr/~fouad.elzein/fondamentale.pdf'),('ElZein1978','https://www.numdam.org/item/MSMF_1978__58__1_0.pdf')]
start=time.perf_counter()
def get(pair):
 name,url=pair;t=time.perf_counter()
 try:
  data=urllib.request.urlopen(url,timeout=45).read()
  if not data.startswith(b'%PDF'):raise ValueError('Not a PDF')
  path=b/'sources'/f'{name}.pdf';path.write_bytes(data)
  p=subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],capture_output=True,text=True)
  return {'name':name,'url':url,'path':str(path),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'pdftotext_returncode':p.returncode,'runtime_seconds':time.perf_counter()-t}
 except Exception as e:return {'name':name,'url':url,'error':repr(e),'runtime_seconds':time.perf_counter()-t}
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(get,sources))
report={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'results':results}
text=json.dumps(report,indent=2);(b/'output'/'fetch_fermat_quintic_sources.json').write_text(text+'\n');print(text)
