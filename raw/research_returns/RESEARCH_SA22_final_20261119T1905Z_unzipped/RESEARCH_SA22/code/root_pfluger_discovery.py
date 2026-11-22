"""Public source discovery; metadata/access outcomes are not original readings."""
from pathlib import Path
import urllib.request,urllib.error,time,json,concurrent.futures,re
R=Path(__file__).resolve().parents[1]
jobs=[
 ('pfluger_doi','https://doi.org/10.18311/JIMS/1960/16922'),
 ('pfluger_crossref','https://api.crossref.org/works/10.18311/JIMS/1960/16922'),
 ('indian_math_archive','https://archive.org/advancedsearch.php?q=title%3A%28Journal%20Indian%20Mathematical%20Society%29&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=year&rows=100&output=json'),
 ('lehto_scispace','https://scispace.com/papers/quasiconformal-mappings-in-the-plane-4hgdgoprrd')]
start=time.perf_counter()
def fetch(job):
 name,url=job;t=time.perf_counter()
 try:
  try:r=urllib.request.urlopen(url,timeout=45)
  except urllib.error.HTTPError as error:r=error
  data=r.read();content=data.decode('utf-8','replace')
  p=R/'sources'/(name+'.json' if 'json' in r.headers.get('content-type','') else name+'.html')
  p.write_bytes(data)
  links=re.findall(r'(?:href|src)=["\']([^"\']+)',content)
  interesting=[s for s in links if any(x in s.lower() for x in ['pdf','download','article/view','fulltext'])]
  out=dict(name=name,url=url,status=r.status,final=r.url,bytes=len(data),seconds=time.perf_counter()-t,saved=str(p.relative_to(R)),links=interesting)
  if name=='indian_math_archive' and r.status==200:
   out['search_results']=json.loads(content).get('response',{})
  if name=='pfluger_crossref' and r.status==200:
   m=json.loads(content)['message'];out['metadata']={k:m.get(k) for k in ['title','URL','link','resource','publisher']}
  return out
 except Exception as e:return dict(name=name,url=url,error=str(e),seconds=time.perf_counter()-t)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(fetch,jobs))
out=dict(requests=len(jobs),seconds=time.perf_counter()-start,results=rows)
(R/'code/root_pfluger_discovery_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
