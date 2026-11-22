#!/usr/bin/env python3
"""Read-only public search API explicitly used by the archive's public JS."""
import concurrent.futures,datetime,hashlib,json,time,urllib.parse,urllib.request
from pathlib import Path
r=Path(__file__).resolve().parents[1];u='https://reciprocity-archive.imj-prg.fr/ajax/autocompleteall/update/data'
def query(s):
 t=time.monotonic();req=urllib.request.Request(u,data=urllib.parse.urlencode({'input':s}).encode(),headers={'Content-Type':'application/x-www-form-urlencoded'})
 try:
  a=urllib.request.urlopen(req,timeout=22);b=a.read();return {'input':s,'status':a.status,'final_url':a.geturl(),'sha256':hashlib.sha256(b).hexdigest(),'response':json.loads(b),'seconds':round(time.monotonic()-t,3)}
 except Exception as e:return {'input':s,'error':type(e).__name__+': '+str(e),'seconds':round(time.monotonic()-t,3)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3)as ex:out=list(ex.map(query,['','Gabber','Fujiwara']))
d={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'public_endpoint_observed_at':'https://reciprocity-archive.imj-prg.fr/js/autocompleteall.js','request_url':u,'results':out}
(r/'logs/B_reciprocity_public_search.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
for a in out:print(json.dumps(a,ensure_ascii=False))
