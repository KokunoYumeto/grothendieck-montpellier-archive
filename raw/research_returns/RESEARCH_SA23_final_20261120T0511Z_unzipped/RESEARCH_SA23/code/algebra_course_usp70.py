from pathlib import Path
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.parse import urljoin
from html.parser import HTMLParser
import hashlib,json,time
root=Path(__file__).resolve().parents[1]
started=time.monotonic()
url='https://www.ime.usp.br/~acervo/ahv.php'
out={'started_utc':datetime.now(timezone.utc).isoformat(),'requested_url':url,'discovery':'Actual indexed official IME-USP Acervo Histórico Virtual page, web160-163; new route distinct from blocked course links.'}
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.current=None
 def handle_starttag(self,tag,attrs):
  if tag=='a':
   a=dict(attrs)
   if 'href'in a:self.current=[a['href'],'']
 def handle_data(self,data):
  if self.current:self.current[1]+=data
 def handle_endtag(self,tag):
  if tag=='a'and self.current:self.links.append(self.current);self.current=None
try:
 with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (public academic source research)'}),timeout=20) as r:
  data=r.read();out.update(status=r.status,final_url=r.geturl(),content_type=r.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  (root/'sources/algebra_course_usp_index.html').write_bytes(data)
  p=Links();p.feed(data.decode('utf8',errors='replace'));out['links']=[{'url':urljoin(r.geturl(),u),'text':t.strip()} for u,t in p.links]
except Exception as e:out.update(error=repr(e),access_stop='No retry, credential use, or bypass after refusal.')
out['elapsed_seconds']=time.monotonic()-started
(root/'logs/algebra_course_usp70.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
