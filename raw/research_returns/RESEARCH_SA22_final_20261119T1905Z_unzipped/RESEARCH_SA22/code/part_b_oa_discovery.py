#!/usr/bin/env python3
"""Read public DOI and repository metadata; no credentials or access-control bypass."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen, Request
import json,time
root=Path(__file__).resolve().parents[1]
dois={'gabber1994':'10.1007/BF02773001','fujiwara1995':'10.1215/S0012-7094-95-08002-8'}
jobs=[]
for name,doi in dois.items():
 jobs += [(name,'crossref','https://api.crossref.org/works/'+doi),
          (name,'openalex','https://api.openalex.org/works/https://doi.org/'+doi),
          (name,'semanticscholar','https://api.semanticscholar.org/graph/v1/paper/DOI:'+doi+'?fields=title,openAccessPdf,url')]
def run(job):
 name,service,url=job;t=time.time();out={'source':name,'service':service,'url':url}
 try:
  with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=35) as r:
   j=json.load(r)
  if service=='crossref':
   j=j['message'];out['metadata']={k:j.get(k) for k in ['title','URL','link','resource','license']}
  elif service=='openalex':out['metadata']={k:j.get(k) for k in ['title','open_access','best_oa_location','locations']}
  else:out['metadata']=j
  out['status']='metadata read'
 except Exception as e:out.update(status='not read',error=str(e))
 out['elapsed_seconds']=round(time.time()-t,2);return out
with ThreadPoolExecutor(max_workers=6) as ex:results=list(ex.map(run,jobs))
(root/'code/part_b_oa_discovery_output.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:print(json.dumps(r))
