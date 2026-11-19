"""Fetch publicly exposed original mathematical works; no credentials or access-control workarounds."""
from pathlib import Path
import urllib.request,json,time,hashlib,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
JOBS=[('lavrentiev1934.pdf','https://www.mathnet.ru/php/getFT.phtml?jrnid=tm&option_lang=eng&paperid=873&what=fullt'),('bers1975.pdf','https://journals.msp.org/mscand/article/download/2057/2056/2088')]
def fetch(job):
 name,url=job;t=time.perf_counter();out={'file':name,'url':url}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r:
   b=r.read();out.update(status=r.status,content_type=r.headers.get('Content-Type'),final_url=r.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),pdf=b.startswith(b'%PDF'))
  (ROOT/'sources'/name).write_bytes(b)
 except Exception as e:out['error']=repr(e)
 out['seconds']=time.perf_counter()-t;return out
t=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(fetch,JOBS))
out={'attempts':len(JOBS),'seconds':time.perf_counter()-t,'results':r}
(ROOT/'code'/'root_classic_sources_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
