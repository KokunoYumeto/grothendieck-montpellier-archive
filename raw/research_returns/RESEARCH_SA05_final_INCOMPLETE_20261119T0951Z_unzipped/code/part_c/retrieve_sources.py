from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,subprocess,time,json
root=Path(__file__).resolve().parents[2]/'part_c'/'sources';root.mkdir(exist_ok=True)
SOURCES={
 'gross_schoen.pdf':'https://www.numdam.org/item/10.5802/aif.1469.pdf',
 'tavakol.pdf':'https://arxiv.org/pdf/1406.7403',
 'kisin_zhou2025.pdf':'https://arxiv.org/pdf/2505.02165',
 'floccari_fu2026.pdf':'https://arxiv.org/pdf/2607.07528',
 'commelin.pdf':'https://www.numdam.org/item/10.5802/aif.3290.pdf',
 'bbm_chapter3.pdf':'https://link.springer.com/content/pdf/10.1007/BFb0093029.pdf',
 'beauville_voisin.pdf':'https://arxiv.org/pdf/math/0111146',
 'vasiu_zink.pdf':'https://arxiv.org/pdf/0909.0969',
 'yin.pdf':'https://arxiv.org/pdf/1404.0171',
 'osullivan.pdf':'https://arxiv.org/pdf/0908.0626',
}
def get(item):
 name,url=item;t=time.perf_counter();p=root/name
 try:
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=45) as r:b=r.read()
   if not b.startswith(b'%PDF'):return {'name':name,'url':url,'status':'not_pdf','bytes':len(b),'elapsed':time.perf_counter()-t}
   p.write_bytes(b)
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,capture_output=True)
  return {'name':name,'url':url,'status':'obtained','bytes':p.stat().st_size,'elapsed':round(time.perf_counter()-t,4)}
 except Exception as e:return {'name':name,'url':url,'status':str(e),'elapsed':round(time.perf_counter()-t,4)}
with ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(get,SOURCES.items()))
Path(__file__).with_name('retrieve_sources_output.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
