"""Check the public NUMiR entry and inspect exhibition brochure thesis references."""
import datetime, hashlib, json, pathlib, re, time, urllib.request
import fitz
from html.parser import HTMLParser
base=pathlib.Path(__file__).resolve().parents[1]
out={'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
class Parser(HTMLParser):
 def __init__(self): super().__init__(convert_charrefs=True);self.parts=[];self.links=[];self.forms=[];self.curr=None
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='a':self.curr={'href':d.get('href'),'label':''}
  if tag in ('form','input','select'):self.forms.append({'tag':tag,**d})
 def handle_data(self,s):
  if s.strip():self.parts.append(s.strip())
  if self.curr is not None:self.curr['label']+=s
 def handle_endtag(self,tag):
  if tag=='a' and self.curr is not None:self.links.append(self.curr);self.curr=None
url='https://www.numir.org/accueil/accueil.php'
record={'url':url};start=time.monotonic()
try:
 with urllib.request.urlopen(url,timeout=25) as response:raw=response.read();record.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
 (base/'sources/algebra_history_numir_home.html').write_bytes(raw)
 p=Parser();p.feed(raw.decode('utf-8',errors='replace'))
 text='\n'.join(p.parts);(base/'sources/algebra_history_numir_home.txt').write_text(text)
 record.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),text=text,links=p.links,forms=p.forms)
except Exception as exc:record['error']=repr(exc)
record['elapsed_seconds']=time.monotonic()-start
out['numir']=record
doc=fitz.open(base/'sources/algebra_history_thesis_exhibition_livret.pdf')
hits=[]
for i,page in enumerate(doc):
 text=page.get_text()
 if re.search(r'1953\s*:\s*Thèse|sources iconographiques',text,re.I):
  image=base/f'sources/algebra_history_thesis_exhibition_p{i+1:03}.png'
  page.get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(image)
  hits.append({'physical_page':i+1,'text':text,'render':str(image.relative_to(base))})
out['brochure_selected_pages']=hits
out['utc_completed']=datetime.datetime.now(datetime.timezone.utc).isoformat()
payload=json.dumps(out,ensure_ascii=False,indent=2)
(base/'logs/algebra_history_thesis46.json').write_text(payload+'\n');print(payload)
