#!/usr/bin/env python3
"""Normal public-URL probes for institutional leads; never authenticate or bypass."""
import concurrent.futures,datetime,hashlib,json,time
from pathlib import Path
import urllib.request,urllib.error,re
r=Path(__file__).resolve().parents[1]
urls=[
 'https://reciprocity-archive.imj-prg.fr/index.php/',
 'https://www.mathematik.uni-osnabrueck.de/K-theory/',
 'https://www.math.uiuc.edu/K-theory/',
 'https://math.illinois.edu/K-theory/',
 'https://www.ms.u-tokyo.ac.jp/library/file/gakui/rdoctor2018.htm',
 'https://sites.unimi.it/ktf/k-theory-links/'
]
def get(u):
 t=time.monotonic()
 try:
  try:
   response=urllib.request.urlopen(u,timeout=22)
  except urllib.error.HTTPError as response_error:
   response=response_error
  raw=response.read();status=response.status;final_url=response.geturl();content_type=response.headers.get('Content-Type')
  d=dict(url=u,status=status,final_url=final_url,content_type=content_type,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),pdf=raw.startswith(b'%PDF'),seconds=round(time.monotonic()-t,3))
  if 'rdoctor2018' in u:
   body=raw.decode('utf-8',errors='replace');d['fujiwara_rows']=[x for x in body.splitlines() if '1994-2' in x or '藤原' in x][:8]
  if 'reciprocity-archive' in u and status==200:
   body=raw.decode('utf-8',errors='replace');d['page_text']=re.sub('<[^>]+>',' ',body)[:12000];d['links']=re.findall(r'href=[\"\']([^\"\']+)',body)
  return d
 except Exception as e:return dict(url=u,error=type(e).__name__+': '+str(e),seconds=round(time.monotonic()-t,3))
start=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as ex:out=list(ex.map(get,urls))
doc={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'policy':'Ordinary unauthenticated public requests only; restricted originals not requested. No original PDF obtained by these archive probes.','results':out,'runtime_seconds':round(time.monotonic()-start,3)}
(r/'logs/B_public_originals_probe.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
for a in out:print(json.dumps({k:v for k,v in a.items()if k not in ['links','page_text','fujiwara_rows']},ensure_ascii=False))
