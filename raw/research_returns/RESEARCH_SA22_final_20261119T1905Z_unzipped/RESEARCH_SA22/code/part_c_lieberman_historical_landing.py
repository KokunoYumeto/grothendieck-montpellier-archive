from pathlib import Path
import urllib.request, urllib.error
from html.parser import HTMLParser
import datetime,time,json,hashlib
base=Path('/workspace/scratch/9c53b536a97f/RESEARCH_SA22')
url='https://web.archive.org/web/20160610110212id_/http://www.jstor.org/stable/2373533'
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.text=[];self.skip=0;self.images=[];self.meta=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ['style','script']:self.skip+=1
  if tag=='a' and a.get('href'):self.links.append(a)
  if tag=='img':self.images.append(a)
  if tag=='meta':self.meta.append(a)
 def handle_endtag(self,tag):
  if tag in ['style','script']:self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip and s.strip():self.text.append(s.strip())
t=time.perf_counter();report={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'scope':'One actual public2016 landing-page capture, redirects disabled; no subscription PDF or account operation.'}
try:
 with urllib.request.build_opener(NoRedirect).open(url,timeout=40) as f:
  body=f.read();report.update(status=f.status,headers=dict(f.headers),bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
 path=base/'sources/part_c_lieberman_jstor2016.html';path.write_bytes(body)
 p=Parse();p.feed(body.decode('utf-8',errors='replace'));report.update(saved=str(path),links=p.links,images=p.images,metadata=p.meta,visible_text='\n'.join(p.text))
except urllib.error.HTTPError as e:report.update(status=e.code,headers=dict(e.headers),error=str(e))
except Exception as e:report['error']=repr(e)
report['elapsed_seconds']=time.perf_counter()-t
payload=json.dumps(report,indent=2);(base/'code/part_c_lieberman_historical_landing_output.json').write_text(payload+'\n');(base/'code/part_c_lieberman_historical_landing_output.txt').write_text(payload+'\n');print(payload)
