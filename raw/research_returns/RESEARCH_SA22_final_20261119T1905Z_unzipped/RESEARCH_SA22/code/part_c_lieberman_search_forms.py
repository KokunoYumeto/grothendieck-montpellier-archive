from pathlib import Path
import urllib.request, urllib.parse
from html.parser import HTMLParser
import concurrent.futures, datetime, time, hashlib, json

base=Path('/workspace/scratch/9c53b536a97f/RESEARCH_SA22')
targets=[
 ('mit_author','https://search.libraries.mit.edu/results?'+urllib.parse.urlencode({'q':'"Lieberman, David Ira"','tab':'all'})),
 ('mit_title','https://search.libraries.mit.edu/results?'+urllib.parse.urlencode({'q':'"Algebraic cycles on" "projective varieties"','tab':'all'})),
 ('princeton_title','https://catalog.princeton.edu/catalog?'+urllib.parse.urlencode({'q':'Algebraic cycles on non singular complex projective varieties','search_field':'title'})),
 ('cdx_jstor','https://web.archive.org/cdx/search/cdx?'+urllib.parse.urlencode({'url':'www.jstor.org/*2373533*','output':'json','filter':'statuscode:200','collapse':'urlkey','fl':'timestamp,original,statuscode,mimetype,digest','filter':'!mimetype:warc/revisit'})),
 ('cdx_bare_jstor','https://web.archive.org/cdx/search/cdx?'+urllib.parse.urlencode({'url':'jstor.org/*2373533*','output':'json','collapse':'urlkey','fl':'timestamp,original,statuscode,mimetype,digest'}))
]
class Parse(HTMLParser):
 def __init__(self):
  super().__init__();self.links=[];self.frames=[];self.text=[];self.hidden=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ['style','script']:self.hidden+=1
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if tag in ['turbo-frame','iframe'] and a.get('src'):self.frames.append({'tag':tag,**a})
 def handle_endtag(self,tag):
  if tag in ['style','script']:self.hidden=max(0,self.hidden-1)
 def handle_data(self,s):
  if not self.hidden and s.strip():self.text.append(s.strip())
def fetch(target):
 label,url=target;t=time.perf_counter();r={'label':label,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=40) as f:data=f.read();r.update(status=f.status,final_url=f.url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  path=base/f'sources/part_c_lieberman_{label}.html';path.write_bytes(data);r['saved']=str(path)
  txt=data.decode('utf-8',errors='replace')
  if label.startswith('cdx'):r['response']=json.loads(txt)
  else:
   p=Parse();p.feed(txt);r.update(links=p.links,frames=p.frames,visible_text='\n'.join(p.text))
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=time.perf_counter()-t
 return r
started=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(fetch,targets))
report={'started_utc':started,'elapsed_seconds':time.perf_counter()-t,'scope':'Five public catalogue requests: three searches using actual observed form actions/fields and two public historical-capture metadata queries. No source/private files requested.','results':results}
payload=json.dumps(report,indent=2)
(base/'code/part_c_lieberman_search_forms_output.json').write_text(payload+'\n')
(base/'code/part_c_lieberman_search_forms_output.txt').write_text(payload+'\n')
print(payload)
