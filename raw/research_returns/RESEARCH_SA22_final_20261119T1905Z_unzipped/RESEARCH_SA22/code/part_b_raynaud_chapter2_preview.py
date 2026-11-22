#!/usr/bin/env python3
"""Follow a normal publisher landing and its explicitly advertised free preview.

The exact chapter DOI is supplied by the opened public mathematical catalogue.
No subscription full-text endpoint is fetched and no preview limit is altered.
"""
from pathlib import Path
from urllib.request import urlopen,Request
from urllib.parse import urljoin
from html.parser import HTMLParser
import json,time,gzip,hashlib
root=Path(__file__).resolve().parents[1];start=time.monotonic();results=[]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.text=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='a' and a.get('href'):self.links.append(a['href'])
 def handle_data(self,s):
  if s.strip():self.text.append(s.strip())
def get(url,kind):
 t=time.monotonic();r={'url':url,'kind':kind}
 try:
  with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as f:raw=f.read(5*1024*1024+1);r.update(http_status=f.status,bytes=len(raw),final_url=f.url,content_type=f.headers.get('Content-Type',''))
  if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
  if len(raw)>5*1024*1024:r['status']='Response cap reached';raw=None
  else:r['status']='Received public response'
 except Exception as e:r.update(status='error',error=str(e));raw=None
 r['elapsed_seconds']=time.monotonic()-t;results.append(r);return r,raw
landing,raw=get('https://doi.org/10.1007/BFb0059508','Public chapter metadata landing')
if raw is not None:
 h=raw.decode('utf8','replace');p=Page();p.feed(h)
 (root/'sources/part_b_raynaud_chapter2_landing.html').write_text(h)
 links=sorted(set(urljoin(landing['final_url'],u) for u in p.links if 'page-one.springer.com/pdf/preview/' in u))
 landing['advertised_public_preview_links']=links
 if not links:landing['status']='No advertised public preview found; no full-text request made'
 else:
  preview,data=get(links[0],'Explicitly advertised public preview; unchanged URL')
  if data is not None:
   if not data.startswith(b'%PDF'):preview['status']='Not a PDF; no original mathematical page read'
   else:
    path=root/'sources/part_b_raynaud_chapter2_preview.pdf';path.write_bytes(data)
    import fitz
    doc=fitz.open(path);s='\n'.join(page.get_text() for page in doc)
    (root/'sources/part_b_raynaud_chapter2_preview.txt').write_text(s)
    preview.update(status='Original public-preview PDF fetched; requires visual reading',pages=len(doc),sha256=hashlib.sha256(data).hexdigest(),text_characters=len(s))
out={'results':results,'elapsed_seconds':time.monotonic()-start}
(root/'code/part_b_raynaud_chapter2_preview_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
