#!/usr/bin/env python3
"""Retrieve publicly indexed GDZ source evidence; no mathematical inference."""
from pathlib import Path
import concurrent.futures, hashlib, json, time
import urllib.request
from PIL import Image
R=Path(__file__).resolve().parents[1]
out=R/'sources'/'bloch_gdz';out.mkdir(exist_ok=True)
t=time.perf_counter()
urls={
'volume.html':'https://gdz.sub.uni-goettingen.de/id/PPN356556735_0037',
'volume_mets.xml':'https://gdz.sub.uni-goettingen.de/mets/PPN356556735_0037.xml',
'scan225.tif':'https://wwwuser.gwdguser.de/~subtypo3/digizeit/tiff/PPN356556735_0037/00000225.tif'}
def get(item):
 name,url=item
 try:
  with urllib.request.urlopen(url,timeout=35) as r:
   data=r.read();status=r.status;ctype=r.headers.get('Content-Type','')
  rec={'name':name,'url':url,'status':status,'bytes':len(data),'content_type':ctype}
  if status==200:
   (out/name).write_bytes(data)
   rec['sha256']=hashlib.sha256(data).hexdigest()
   if name.endswith('.tif'):
    im=Image.open(out/name);im.thumbnail((1450,2200));im.convert('RGB').save(out/name.replace('.tif','.png'))
  return rec
 except Exception as e:return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(get,urls.items()))
result={'records':records,'runtime_seconds':time.perf_counter()-t}
(R/'code'/'fetch_bloch_gdz_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
