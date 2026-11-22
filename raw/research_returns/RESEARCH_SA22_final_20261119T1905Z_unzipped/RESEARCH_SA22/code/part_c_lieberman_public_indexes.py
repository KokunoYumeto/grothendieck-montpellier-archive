from pathlib import Path
import urllib.request,urllib.parse,datetime,time,json,concurrent.futures,hashlib
from html.parser import HTMLParser
base=Path('/workspace/scratch/9c53b536a97f/RESEARCH_SA22')
targets=[
 ('semantic_scholar','https://api.semanticscholar.org/graph/v1/paper/DOI:10.2307/2373533?fields=title,url,openAccessPdf'),
 ('public_book_title','https://libcats.org/g/'+urllib.parse.quote('Numerical and Homological'))
]
class Parse(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.text=[];self.skip=0
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='a' and a.get('href'):self.links.append(a['href'])
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(0,self.skip-1)
 def handle_data(self,s):
  if not self.skip and s.strip():self.text.append(s.strip())
def fetch(pair):
 label,url=pair;t=time.perf_counter();r={'label':label,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=35) as f:body=f.read();r.update(status=f.status,bytes=len(body),final_url=f.url,sha256=hashlib.sha256(body).hexdigest())
  if label=='semantic_scholar':r['response']=json.loads(body)
  else:
   path=base/'sources/part_c_lieberman_libcats_title.html';path.write_bytes(body)
   p=Parse();p.feed(body.decode('utf-8',errors='replace'));r.update(saved=str(path),links=p.links,visible_text='\n'.join(p.text))
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=time.perf_counter()-t;return r
t=time.perf_counter();started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(fetch,targets))
report={'started_utc':started,'elapsed_seconds':time.perf_counter()-t,'scope':'Two new public index metadata queries; no headers/auth changes or retries; stop on any challenge/denial.','results':results}
payload=json.dumps(report,indent=2);(base/'code/part_c_lieberman_public_indexes_output.json').write_text(payload+'\n');(base/'code/part_c_lieberman_public_indexes_output.txt').write_text(payload+'\n');print(payload)
