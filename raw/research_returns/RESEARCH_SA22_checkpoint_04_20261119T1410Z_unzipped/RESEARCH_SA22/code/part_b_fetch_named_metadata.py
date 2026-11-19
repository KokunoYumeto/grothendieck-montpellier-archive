#!/usr/bin/env python3
"""Bounded public repository discovery for two still-required named originals."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlencode,quote
from urllib.request import urlopen
import json,time
root=Path(__file__).resolve().parents[1];started=time.monotonic()
works=[('lieberman1968','10.2307/2373533','title:"Numerical and homological equivalence"'),
       ('raynaud_thesis1970','10.1007/BFb0059504','title:"Faisceaux amples" AND creator:Raynaud')]
jobs=[]
for name,doi,query in works:
 jobs.extend([
  (name,'openalex','https://api.openalex.org/works/https://doi.org/'+doi),
  (name,'hal','https://api.archives-ouvertes.fr/search/?'+urlencode({'q':f'doiId_s:"{doi}"','fl':'title_s,uri_s,fileMain_s,linkExtUrl_s,doiId_s','wt':'json','rows':10})),
  (name,'openaire','https://api.openaire.eu/search/publications?'+urlencode({'doi':doi,'format':'json','size':10})),
  (name,'internetarchive_catalog','https://archive.org/advancedsearch.php?'+urlencode({'q':query,'rows':15,'output':'json'}))])
def run(job):
 name,service,url=job;t=time.monotonic();r={'work':name,'service':service,'url':url}
 try:
  with urlopen(url,timeout=22) as response:
   raw=response.read();r['http_status']=response.status;r['bytes']=len(raw)
  r['metadata']=json.loads(raw);r['status']='metadata read'
 except Exception as exc:r['status']='error';r['error']=str(exc)
 r['elapsed_seconds']=time.monotonic()-t
 print(json.dumps({k:v for k,v in r.items() if k!='metadata'}),flush=True)
 return r
with ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(run,jobs))
result={'results':out,'elapsed_seconds':time.monotonic()-started}
(root/'code/part_b_fetch_named_metadata_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'requests':len(out),'elapsed_seconds':result['elapsed_seconds']}))
