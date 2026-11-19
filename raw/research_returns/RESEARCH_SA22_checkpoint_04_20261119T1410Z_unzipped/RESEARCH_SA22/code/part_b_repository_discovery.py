#!/usr/bin/env python3
"""Bounded public repository/preservation metadata discovery; no credentials."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode,quote
from urllib.request import urlopen,Request
import json,time
root=Path(__file__).resolve().parents[1]
works={'gabber1994':('10.1007/BF02773001','Affine analog of the proper base change theorem'),'fujiwara1995':('10.1215/S0012-7094-95-08002-8','Theory of tubular neighborhood in etale topology')}
jobs=[]
for name,(doi,title) in works.items():
 jobs.append((name,'hal','https://api.archives-ouvertes.fr/search/?'+urlencode({'q':'doiId_s:"'+doi+'"','fl':'title_s,uri_s,fileMain_s,linkExtUrl_s,doiId_s','wt':'json','rows':10})))
 jobs.append((name,'openaire','https://api.openaire.eu/search/publications?'+urlencode({'doi':doi,'format':'json','size':10})))
 jobs.append((name,'fatcat','https://api.fatcat.wiki/v0/release/lookup?'+urlencode({'doi':doi})))
def get(job):
 name,service,url=job;out={'work':name,'service':service,'url':url};t=time.perf_counter()
 try:
  with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0','Accept':'application/json'}),timeout=25) as r:
   data=r.read();out.update(http_status=r.status,content_type=r.headers.get('Content-Type'),bytes=len(data))
   try:out['metadata']=json.loads(data)
   except ValueError:out['body_excerpt']=data[:1000].decode(errors='replace')
 except Exception as e:out['error']=str(e)
 out['elapsed_seconds']=round(time.perf_counter()-t,3);return out
with ThreadPoolExecutor(max_workers=6) as pool:out=list(pool.map(get,jobs))
(root/'code/part_b_repository_discovery_output.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out:
 short={k:v for k,v in r.items() if k!='metadata'}
 if 'metadata' in r:
  if r['service']=='hal':short['response']=r['metadata'].get('response')
  elif r['service']=='openaire':short['metadata_top_keys']=list(r['metadata']);short['total']=r['metadata'].get('response',{}).get('header',{}).get('total')
  else:short['metadata']=r['metadata']
 print(json.dumps(short))
