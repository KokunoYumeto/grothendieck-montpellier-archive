"""Two public catalogue queries through observed search actions; no authentication."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import hashlib,json,time,urllib.request,urllib.error,urllib.parse

R=Path(__file__).resolve().parents[1]
targets=[('mpim_fujiwara','https://archive.mpim-bonn.mpg.de/cgi/search',{'q':'Fujiwara','_action_search':'Search','_order':'bytitle','basic_srchtype':'ALL','_satisfyall':'ALL'}),
         ('ndli_verheftung','https://ndl.iitkgp.ac.in/search',{'key':'Verheftung'})]
class Read(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.links=[];self.scripts=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ['script','style']:self.skip+=1
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag=='script' and a.get('src'):self.scripts.append(a['src'])
 def handle_endtag(self,tag):
  if tag in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip and data.strip():self.text.append(data.strip())
def get(item):
 name,base,params=item;url=base+'?'+urllib.parse.urlencode(params);t=time.perf_counter()
 out=dict(name=name,url=url,parameters=params,started_utc=datetime.now(timezone.utc).isoformat())
 try:
  try:res=urllib.request.urlopen(url,timeout=30)
  except urllib.error.HTTPError as e:res=e
  body=res.read();out.update(status=res.status,final_url=res.url,bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
  (R/'sources'/('root_'+name+'.html')).write_bytes(body)
  if res.status==200:
   p=Read();p.feed(body.decode('utf-8','replace'));out.update(text='\n'.join(p.text),links=list(dict.fromkeys(p.links)),scripts=p.scripts)
 except Exception as e:out['error']=repr(e)
 out['seconds']=time.perf_counter()-t
 return out
started=time.perf_counter()
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(get,targets))
out=dict(scope='Two public metadata catalogue queries. Actions and parameters observed in the saved MPIM basic form and NDLI public landing search() function. No login, content-file request or retry.',requests=2,results=results,seconds=time.perf_counter()-started)
(R/'code/root_mpim_ndli_search_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'results':[{k:v for k,v in x.items() if k not in ['text','links','scripts']} for x in results]},indent=2))
