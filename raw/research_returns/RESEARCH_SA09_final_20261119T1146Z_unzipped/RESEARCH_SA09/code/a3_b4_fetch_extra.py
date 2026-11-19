from pathlib import Path
from urllib.request import urlopen
from time import perf_counter
import json
root=Path(__file__).resolve().parents[1]
urls=[('schinzel','https://matwbn.icm.edu.pl/ksiazki/aa/aa32/aa3235.pdf'),('schinzel_corr','https://matwbn.icm.edu.pl/ksiazki/aa/aa36/aa3619.pdf'),('torikummer','https://www.numdam.org/item/10.5802/pmb.51.pdf')]
rows=[]
for name,url in urls:
 t=perf_counter()
 try:
  with urlopen(url,timeout=30) as r:data=r.read()
  (root/'sources'/(name+'.pdf')).write_bytes(data)
  rows.append({'name':name,'url':url,'bytes':len(data),'seconds':perf_counter()-t})
 except Exception as e:rows.append({'name':name,'url':url,'error':str(e),'seconds':perf_counter()-t})
(root/'logs/a3_b4_fetch_extra.json').write_text(json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
