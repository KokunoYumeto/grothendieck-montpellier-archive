"""Retrieve only independently public early-spectral sources and actual preview links."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import time
import urllib.request
import fitz
from html.parser import HTMLParser

base = pathlib.Path(__file__).resolve().parents[1]
targets = [
 ('schatten1960_front', 'https://link.springer.com/content/pdf/bfm:978-3-642-87652-3/1', 'pdf'),
 ('schatten1960_back', 'https://link.springer.com/content/pdf/bbm:978-3-642-87652-3/1', 'pdf'),
 ('schatten1960_preview', 'https://page-one.springer.com/pdf/preview/10.1007/978-3-642-87652-3_4', 'pdf'),
 ('horn1950_p374', 'https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7ea1/1063207/65f5296ad911/pnas01556-0014.png', 'png'),
 ('horn1950_p375', 'https://cdn.ncbi.nlm.nih.gov/pmc/blobs/7ea1/1063207/39cec84aeb62/pnas01556-0015.png', 'png'),
 ('horn1954_doi', 'https://doi.org/10.1090/S0002-9939-1954-0061573-6', 'html'),
 ('horn_bibliography', 'https://store.fmi.uni-sofia.bg/fmi/logic/skordev/ln/lp/ahornpbl.htm', 'html'),
 ('dunford_schwartz_I_public_ocr', 'https://djvu.online/file/2fKOsgZV9iOOd', 'html'),
]
class Parser(HTMLParser):
 def __init__(self): super().__init__(convert_charrefs=True); self.parts=[]; self.links=[]
 def handle_data(self, value):
  if value.strip(): self.parts.append(value.strip())
 def handle_starttag(self,tag,attrs):
  if tag=='a': self.links.append(dict(attrs).get('href'))
def fetch(target):
 name,url,extension=target
 start=time.monotonic()
 rec={'name':name,'url':url,'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   raw=response.read(); rec.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
  path=base/f'sources/algebra_spectral_{name}.{extension}'
  path.write_bytes(raw)
  rec.update(path=str(path.relative_to(base)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
  if raw.startswith(b'%PDF'):
   doc=fitz.open(path); texts=[page.get_text() for page in doc]
   text='\n\f\n'.join(texts)
   path.with_suffix('.txt').write_text(text)
   rec.update(pdf_pages=len(doc),page_text_lengths=list(map(len,texts)),texts=texts)
  elif extension=='html':
   parser=Parser();parser.feed(raw.decode('utf-8',errors='replace'))
   text='\n'.join(parser.parts);path.with_suffix('.txt').write_text(text)
   rec.update(text_characters=len(text),links=parser.links)
 except Exception as error:
  rec['error']=repr(error)
 rec['elapsed_seconds']=time.monotonic()-start
 rec['utc_completed']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 return rec
started=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 records=list(pool.map(fetch,targets))
output={'records':records,'elapsed_seconds':time.monotonic()-started}
payload=json.dumps(output,ensure_ascii=False,indent=2)
(base/'logs/algebra_spectral_fetch48.json').write_text(payload+'\n')
print(payload)
