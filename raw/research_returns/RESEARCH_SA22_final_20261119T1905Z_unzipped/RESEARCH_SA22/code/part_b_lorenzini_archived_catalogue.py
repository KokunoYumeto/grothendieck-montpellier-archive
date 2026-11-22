#!/usr/bin/env python3
"""Read one actual public author-catalogue capture returned by the exact CDX query."""
from pathlib import Path
from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin
import json,time,gzip
root=Path(__file__).resolve().parents[1];start=time.monotonic()
original='http://alpha.math.uga.edu:80/~lorenz/paper.html'
url='https://web.archive.org/web/20170821032054id_/'+original
class Page(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.links=[]
 def handle_data(self,s):
  if s.strip():self.text.append(s.strip())
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='a' and a.get('href'):self.links.append(urljoin(original,a['href']))
r={'url':url,'scope':'Public archived author bibliography only; no original file requested'}
try:
 with urlopen(url,timeout=30) as f:raw=f.read(1048577);r.update(http_status=f.status,bytes=len(raw),content_encoding=f.headers.get('Content-Encoding',''))
 if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
 if len(raw)>1048576:r['status']='Response cap reached; no complete page reading'
 else:
  h=raw.decode('utf8','replace');p=Page();p.feed(h)
  (root/'sources/part_b_lorenzini_archived_catalogue.html').write_text(h)
  (root/'sources/part_b_lorenzini_archived_catalogue.txt').write_text('\n'.join(p.text)+'\n')
  r.update(status='Public archived catalogue read',advertised_links=p.links,raynaud_links=[x for x in p.links if 'raynaud' in x.lower()],text_lines=len(p.text))
except Exception as e:r.update(status='error',error=str(e))
r['elapsed_seconds']=time.monotonic()-start
(root/'code/part_b_lorenzini_archived_catalogue_output.json').write_text(json.dumps({'results':[r],'elapsed_seconds':r['elapsed_seconds']},indent=2)+'\n');print(json.dumps(r,indent=2))
