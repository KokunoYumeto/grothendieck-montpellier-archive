#!/usr/bin/env python3
"""Read the public author-index snapshot actually advertised by CDX."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic()
url='https://web.archive.org/web/20221104052203id_/https://www.ihes.fr/~gabber/'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.text=[];self.skip=0
 def handle_starttag(self,t,a):
  a=dict(a)
  if t in ['script','style']:self.skip+=1
  if t=='a' and a.get('href'):self.links.append(a['href'])
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
 def handle_data(self,s):
  if not self.skip and s.strip():self.text.append(s.strip())
r={'url':url,'scope':'Public archived author catalogue only; no files or personal correspondence requested'}
try:
 with urlopen(url,timeout=30) as f:raw=f.read(1048577);r.update(http_status=f.status,bytes=len(raw),final_url=f.url)
 if len(raw)>1048576:r['status']='Response cap reached; page not completely read'
 else:
  h=raw.decode('utf8','replace');p=Page();p.feed(h)
  (root/'sources/part_b_gabber_archived_author_index.html').write_text(h)
  (root/'sources/part_b_gabber_archived_author_index.txt').write_text('\n'.join(p.text)+'\n')
  r.update(status='Public archived HTML read',text='\n'.join(p.text),advertised_links=p.links)
except Exception as e:r.update(status='error',error=str(e))
r['elapsed_seconds']=time.monotonic()-start
(root/'code/part_b_gabber_archived_index_output.json').write_text(json.dumps({'results':[r],'elapsed_seconds':r['elapsed_seconds']},indent=2)+'\n')
print(json.dumps(r,indent=2))
