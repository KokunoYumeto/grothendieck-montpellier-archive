"""Failed initial attempt: requests was unavailable; no network call executed."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,time,requests
from bs4 import BeautifulSoup

R=Path(__file__).resolve().parents[1]
targets=[('mpim','https://archive.mpim-bonn.mpg.de/cgi/search/advanced'),
         ('ndli','https://ndl.iitkgp.ac.in/'),
         ('google1961','https://books.google.com/books/about/The_Journal_of_the_Indian_Mathematical_S.html?id=6k4_AQAAIAAJ')]
def get(item):
 name,url=item; before=time.perf_counter()
 out=dict(name=name,url=url,started_utc=datetime.now(timezone.utc).isoformat())
 try:
  res=requests.get(url,timeout=30)
  out.update(status=res.status_code,final_url=res.url,bytes=len(res.content),sha256=hashlib.sha256(res.content).hexdigest())
  (R/'sources'/('root_public_catalogue_'+name+'.html')).write_bytes(res.content)
  if res.status_code==200:
   soup=BeautifulSoup(res.text,'html.parser')
   out['forms']=[dict(action=f.get('action'),method=f.get('method'),inputs=[dict(name=x.get('name'),type=x.get('type'),value=x.get('value')) for x in f.find_all(['input','select'])]) for f in soup.find_all('form')]
   out['scripts']=[x.get('src') for x in soup.find_all('script') if x.get('src')]
   text=soup.get_text(' ',strip=True)
   out['text_excerpt']=text[:16000]
 except Exception as e:out['error']=repr(e)
 out['seconds']=time.perf_counter()-before
 return out
started=time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(get,targets))
out=dict(scope='Three public landing/form pages at exact observed URLs; no account, no content-file request, no retries.',requests=len(targets),results=results,seconds=time.perf_counter()-started)
(R/'code/root_public_catalogue_forms_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
