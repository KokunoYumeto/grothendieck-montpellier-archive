#!/usr/bin/env python3
"""Fetch and inventory primary sources consulted in the continuation of B."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,time,urllib.request

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'references/B_finish_sources'
SOURCES={
 'LauDivided.texsrc':'https://arxiv.org/src/1811.09439v2',
 'LauDivided.pdf':'https://arxiv.org/pdf/1811.09439v2',
 'ALB.texsrc':'https://arxiv.org/src/1907.10525v4',
 'deJongMessing.pdf':'https://www.numdam.org/article/BSMF_1999__127_2_333_0.pdf',
 'LauSheared.texsrc':'https://arxiv.org/src/2601.12565v2',
 'GardnerMadapusi.texsrc':'https://arxiv.org/src/2412.10226',
 'LauRelations.pdf':'https://arxiv.org/pdf/1006.2720v4',
 'LauSmoothness.pdf':'https://arxiv.org/pdf/1006.2723v1',
 'deJong1995.pdf':'https://www.numdam.org/item/PMIHES_1995__82__5_0.pdf',
 'Kisin.dvi':'https://people.math.harvard.edu/~kisin/dvifiles/wam.dvi',
 'Breuil.pdf':'https://arxiv.org/pdf/math/0009252',
 'BMS2.pdf':'https://people.mpim-bonn.mpg.de/scholze/bms2.pdf',
}
def fetch(item):
 name,url=item;t=time.monotonic();path=DEST/name
 try:
  reused=path.exists()
  if not reused:
   request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0',
        'Referer':'https://people.math.harvard.edu/~kisin/preprints.html'})
   path.write_bytes(urllib.request.urlopen(request,timeout=40).read())
  data=path.read_bytes()
  return {'name':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
          'reused':reused,'seconds':round(time.monotonic()-t,4),'ok':True}
 except Exception as e:
  return {'name':name,'url':url,'error':repr(e),'seconds':round(time.monotonic()-t,4),'ok':False}
if __name__=='__main__':
 DEST.mkdir(exist_ok=True,parents=True)
 with ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(fetch,SOURCES.items()))
 (ROOT/'logs/B_finish_source_inventory.json').write_text(json.dumps(results,indent=2)+'\n')
 print(json.dumps(results,indent=2))
