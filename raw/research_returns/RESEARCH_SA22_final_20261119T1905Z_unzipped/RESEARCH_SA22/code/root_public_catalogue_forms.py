"""Read three observed public catalogue pages with the Python standard library."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib,json,time,urllib.request,urllib.error

R=Path(__file__).resolve().parents[1]
targets=[('mpim','https://archive.mpim-bonn.mpg.de/cgi/search/advanced'),
         ('ndli','https://ndl.iitkgp.ac.in/'),
         ('google1961','https://books.google.com/books/about/The_Journal_of_the_Indian_Mathematical_S.html?id=6k4_AQAAIAAJ')]
class Inspect(HTMLParser):
 def __init__(self):super().__init__();self.forms=[];self.current=None;self.scripts=[];self.text=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ['script','style']:self.skip+=1
  if tag=='form':self.current=dict(action=a.get('action'),method=a.get('method'),inputs=[]);self.forms.append(self.current)
  if tag in ['input','select'] and self.current is not None:self.current['inputs'].append({k:a.get(k) for k in ['name','type','value','id']})
  if tag=='script' and a.get('src'):self.scripts.append(a['src'])
 def handle_endtag(self,tag):
  if tag=='form':self.current=None
  if tag in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip and data.strip():self.text.append(data.strip())
def get(item):
 name,url=item;before=time.perf_counter()
 out=dict(name=name,url=url,started_utc=datetime.now(timezone.utc).isoformat())
 try:
  try:
   res=urllib.request.urlopen(url,timeout=30)
  except urllib.error.HTTPError as e:res=e
  body=res.read();out.update(status=res.status,final_url=res.url,bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
  (R/'sources'/('root_public_catalogue_'+name+'.html')).write_bytes(body)
  if res.status==200:
   parser=Inspect();parser.feed(body.decode('utf-8','replace'))
   out.update(forms=parser.forms,scripts=parser.scripts,text_excerpt=' '.join(parser.text)[:16000])
 except Exception as e:out['error']=repr(e)
 out['seconds']=time.perf_counter()-before
 return out
started=time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(get,targets))
out=dict(scope='Three public landing/form pages at exact observed URLs; no account, no content-file request, no retries.',requests=len(targets),results=results,seconds=time.perf_counter()-started)
(R/'code/root_public_catalogue_forms_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
