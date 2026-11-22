"""Retrieve public DOI metadata for the ETH Weyl inventory and its linked description."""
import concurrent.futures, hashlib, json, time, urllib.request
from pathlib import Path
root=Path('RESEARCH_SA23')
items=[
 ('weyl_datacite','https://api.datacite.org/dois/10.3929/ethz-a-000310478','.json'),
 ('weyl_eth_description','https://library.ethz.ch/sammlungen-und-archive/kurzportraets/hermann-weyl--1885-1955-.html','.html'),
]
def fetch(item):
 name,url,ext=item
 tick=time.monotonic(); row={'name':name,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   data=response.read(); row.update(status=response.status,final_url=response.url)
  out=root/'sources'/('algebra_history_'+name+ext); out.write_bytes(data)
  row.update(file=str(out.relative_to(root)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as exc: row['error']=type(exc).__name__+': '+str(exc)
 row['elapsed_seconds']=round(time.monotonic()-tick,6); return row
tick=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: rows=list(pool.map(fetch,items))
s=json.dumps({'results':rows,'elapsed_seconds':round(time.monotonic()-tick,6)},ensure_ascii=False,indent=2)
(root/'logs/algebra_history_weyl21.json').write_text(s+'\n'); print(s)
