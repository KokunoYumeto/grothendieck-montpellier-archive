"""One ordinary public retrieval after web-reader timeout/redirect errors; no auth."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import re
import time
import urllib.request
from html.parser import HTMLParser
import fitz
base=pathlib.Path(__file__).resolve().parents[1]
targets=[
 ('dunford1958_survey','https://pages.mtu.edu/~struther/Courses/OLD/5630/Refs/Dunford_BullAMS_1958_SpectralOperators.pdf','pdf'),
 ('schatten1970_google_landing','https://books.google.com/books?id=3bn5MQEACAAJ','html'),
]
class Parser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.parts=[];self.links=[];self.link=None
 def handle_data(self,value):
  if value.strip():self.parts.append(value.strip())
  if self.link is not None:self.link['text']+=value
 def handle_starttag(self,tag,attrs):
  if tag=='a':self.link={'href':dict(attrs).get('href'),'text':''}
 def handle_endtag(self,tag):
  if tag=='a' and self.link is not None:self.links.append(self.link);self.link=None
def fetch(target):
 name,url,extension=target;start=time.monotonic()
 rec={'name':name,'url':url,'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   raw=response.read();rec.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
  path=base/f'sources/algebra_spectral_{name}.{extension}';path.write_bytes(raw)
  rec.update(path=str(path.relative_to(base)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
  if raw.startswith(b'%PDF'):
   doc=fitz.open(path);texts=[p.get_text() for p in doc];path.with_suffix('.txt').write_text('\n\f\n'.join(texts))
   rec['pdf_pages']=len(doc)
   rec['keyword_contexts']=[]
   pattern=re.compile(r'groth|lidsk|schatten|trace|genus|communicat|unpublish|letter|acknowledg',re.I)
   for i,t in enumerate(texts):
    matches=list(pattern.finditer(t))
    if matches:rec['keyword_contexts'].append({'physical_page':i+1,'contexts':[t[max(0,m.start()-220):m.end()+380] for m in matches]})
  else:
   parser=Parser();parser.feed(raw.decode('utf-8',errors='replace'))
   text='\n'.join(parser.parts);path.with_suffix('.txt').write_text(text)
   rec.update(links=parser.links,text=text)
 except Exception as error:rec['error']=repr(error)
 rec['elapsed_seconds']=time.monotonic()-start
 rec['utc_completed']=datetime.datetime.now(datetime.timezone.utc).isoformat();return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:records=list(pool.map(fetch,targets))
payload=json.dumps({'records':records},ensure_ascii=False,indent=2)
(base/'logs/algebra_spectral_fetch50.json').write_text(payload+'\n');print(payload)
