from pathlib import Path
import concurrent.futures, hashlib, json, time, urllib.request
from datetime import datetime, timezone
start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
sources=root/'sources'; sources.mkdir(exist_ok=True)
items=[
 ('morrow2019_formal_hodge_witt.pdf','https://www.numdam.org/item/ASENS_2019__52_6_1537_0.pdf'),
 ('morrow_variational_tate_author.pdf','https://www.imo.universite-paris-saclay.fr/~matthew.morrow/Morrow,%20M.,%20Variational%20Tate.pdf')
]
def get(item):
 name,url=item;t=time.perf_counter()
 try:
  data=urllib.request.urlopen(url,timeout=25).read()
  assert data.startswith(b'%PDF'), 'not a PDF'
  dest=sources/name;dest.write_bytes(data)
  return {'file':str(dest),'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'runtime_seconds':time.perf_counter()-t,'status':'saved'}
 except Exception as exc:
  return {'file':name,'url':url,'error':str(exc),'runtime_seconds':time.perf_counter()-t,'status':'failed'}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 result=list(pool.map(get,items))
manifest={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'items':result,'runtime_seconds':time.perf_counter()-start}
out=root/'output/higher_restriction_sources_manifest.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
