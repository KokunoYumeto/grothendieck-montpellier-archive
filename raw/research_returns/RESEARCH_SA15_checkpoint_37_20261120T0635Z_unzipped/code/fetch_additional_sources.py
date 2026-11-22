"""Acquire primary scans for source checking; never package these third-party files."""
from pathlib import Path
import concurrent.futures,urllib.request,time,json
w=Path(__file__).resolve().parents[1];out=w/'references';out.mkdir(exist_ok=True)
sources={
 'SGA4half.pdf':'https://www.wstein.org/sga/sga/pdf/sga4h.pdf',
 'SGA7I.pdf':'https://www.wstein.org/sga/sga/pdf/sga7-1.pdf',
 'Serre1968Abelian.pdf':'https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf',
 'BhattDeJong2013.pdf':'https://arxiv.org/pdf/1302.3189',
}
def fetch(pair):
 name,url=pair;start=time.monotonic();p=out/name
 try:
  if not p.exists():
   with urllib.request.urlopen(url,timeout=35) as r:b=r.read()
   if not b.startswith(b'%PDF'):raise ValueError('Not a PDF response')
   p.write_bytes(b)
  return dict(name=name,url=url,status='obtained',bytes=p.stat().st_size,seconds=round(time.monotonic()-start,3))
 except Exception as e:return dict(name=name,url=url,status='failed',error=str(e),seconds=round(time.monotonic()-start,3))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(fetch,sources.items()))
(w/'outputs/additional_source_fetch.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(json.dumps(r))
