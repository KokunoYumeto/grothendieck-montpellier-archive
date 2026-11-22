"""Fetch only the actual archived congress803/804 links advertised by item664."""
from pathlib import Path
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.parse,hashlib,json,time
from datetime import datetime,timezone
b=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.text=[];self.skip=0
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='a' and d.get('href'):self.links.append(d['href'])
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip and s.strip():self.text.append(s.strip())
class ArchiveOnly(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  if urllib.parse.urlsplit(newurl).hostname!='web.archive.org':raise RuntimeError('Stopped redirect outside public archive: '+newurl)
  return super().redirect_request(req,fp,code,msg,headers,newurl)
p=Links();p.feed((b/'sources/category_bourbaki_r230_item664_0.html').read_text())
def fetch(n):
 link=next(u for u in p.links if u.endswith('/items/show/'+str(n)))
 url=urllib.parse.urljoin('http://web.archive.org',link);t=time.perf_counter()
 row={'record':n,'advertised_link':link,'url':url}
 try:
  if urllib.parse.urlsplit(url).hostname!='web.archive.org':raise ValueError('Non-archive initial URL')
  with urllib.request.build_opener(ArchiveOnly()).open(url,timeout=40) as r:
   data=r.read();row.update(final_url=r.url,status=r.status,content_type=r.headers.get('Content-Type'))
  path=b/f'sources/geometry_bourbaki_congress_{n}.html';path.write_bytes(data)
  z=Links();z.feed(data.decode('utf-8',errors='replace'))
  tx=b/f'notes/geometry_bourbaki_congress_{n}_text.txt';tx.write_text('\n'.join(z.text))
  row.update(path=str(path.relative_to(b)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),links=z.links,text_path=str(tx.relative_to(b)))
 except Exception as e:row.update(error_type=type(e).__name__,error=str(e))
 row['elapsed_seconds']=time.perf_counter()-t
 return row
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=2) as ex:rows=list(ex.map(fetch,[803,804]))
log={'utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'elapsed_seconds':time.perf_counter()-start,'no_live_AHP_request':True}
(b/'logs/geometry_bourbaki_congress_records.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps(log,indent=2))
