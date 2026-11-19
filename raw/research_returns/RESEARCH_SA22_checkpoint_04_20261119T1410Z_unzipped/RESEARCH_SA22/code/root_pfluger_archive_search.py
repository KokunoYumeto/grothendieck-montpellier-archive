"""Read public Internet Archive catalogue fields and public journal landing pages."""
from pathlib import Path
import urllib.request,urllib.error,urllib.parse,json,time,concurrent.futures,re
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
query='title:(Journal Indian Mathematical Society)'
params=[('q',query),('rows','250'),('output','json')]+[('fl[]',x) for x in ['identifier','title','date','description','volume','year']]
jobs=[('indian_math_full_catalogue','https://archive.org/advancedsearch.php?'+urllib.parse.urlencode(params)),
 ('pfluger_informatics','https://www.informaticsjournals.com/index.php/jims/article/view/16922'),
 ('pfluger_ischolar','https://www.i-scholar.in/index.php/JIMSIMS/article/view/16922')]
def run(job):
 name,url=job;t=time.perf_counter()
 try:
  try:r=urllib.request.urlopen(url,timeout=40)
  except urllib.error.HTTPError as e:r=e
  data=r.read();s=data.decode('utf-8','replace')
  path=R/'sources'/(name+('.json' if 'json' in r.headers.get('content-type','') else '.html'))
  path.write_bytes(data)
  row=dict(name=name,url=url,status=r.status,final=r.url,bytes=len(data),seconds=time.perf_counter()-t,saved=str(path.relative_to(R)))
  if name=='indian_math_full_catalogue' and r.status==200:
   results=json.loads(s)['response'];row['found']=results['numFound'];row['returned']=len(results['docs'])
   row['candidate_records']=[d for d in results['docs'] if re.search(r'196[01]|\b24\b|xxiv',str(d),re.I)]
   row['sample_metadata']=results['docs'][:2]
  else:row['links']=[x for x in re.findall(r'href=["\']([^"\']+)',s) if any(k in x.lower() for k in ['pdf','download','article','jims'])]
  return row
 except Exception as e:return dict(name=name,url=url,error=str(e),seconds=time.perf_counter()-t)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(run,jobs))
out=dict(requests=len(jobs),seconds=time.perf_counter()-start,results=rows)
(R/'code/root_pfluger_archive_search_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
