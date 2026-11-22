"""Fetch public pages, preserve outcomes, and list advertised links only."""
from pathlib import Path
import urllib.request,urllib.error,json,time,concurrent.futures,re,sys
R=Path(__file__).resolve().parents[1];T=time.perf_counter()
jobs=[s.split('=',1) for s in sys.argv[1:]]
def run(job):
 name,url=job;t=time.perf_counter()
 try:
  try:r=urllib.request.urlopen(url,timeout=35)
  except urllib.error.HTTPError as e:r=e
  b=r.read();p=R/'sources'/(name+'.html');p.write_bytes(b)
  s=b.decode('utf-8','replace')
  links=list(dict.fromkeys(re.findall(r'(?:href|src)=["\']([^"\']+)',s)))
  return dict(name=name,url=url,status=r.status,final=r.url,seconds=time.perf_counter()-t,bytes=len(b),path=str(p.relative_to(R)),links=links)
 except Exception as e:return dict(name=name,url=url,error=str(e),seconds=time.perf_counter()-t)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(run,jobs))
out=dict(requests=len(rows),seconds=time.perf_counter()-T,results=rows)
name='_'.join(x[0] for x in jobs)
(R/'code'/('root_public_page_links_'+name+'_output.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
