"""Preserve the targeted retrievals used after the first source pass."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,time,json,subprocess
out=Path(__file__).resolve().parents[2]/'part_c'/'sources';out.mkdir(exist_ok=True)
urls={
 'andre1996':'https://www.numdam.org/item/PMIHES_1996__83__5_0.pdf',
 'bbm_preview':'https://page-one.springer.com/pdf/preview/10.1007/BFb0093029',
 'lan_revision':'https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision-dense.pdf',
 'gdz_bloch_p103':'https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0350/00000109?_format=xml',
 'gdz_bloch_p104':'https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0350/00000110?_format=xml',
 'gdz_bloch_p102':'https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0350/00000108?_format=xml',
}
def run(z):
 name,url=z;t=time.perf_counter()
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=55).read()
  pdf=data.startswith(b'%PDF'); path=out/(name+('.pdf' if pdf else '.html'));path.write_bytes(data)
  if pdf:subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
  return {'name':name,'url':url,'bytes':len(data),'pdf':pdf,'elapsed':round(time.perf_counter()-t,3)}
 except Exception as e:return {'name':name,'url':url,'error':str(e),'elapsed':round(time.perf_counter()-t,3)}
with ThreadPoolExecutor(max_workers=6) as ex:res=list(ex.map(run,urls.items()))
p=Path(__file__).with_name('fetch_extra_sources_output.json');p.write_text(json.dumps(res,indent=2));print(json.dumps(res,indent=2))
