#!/usr/bin/env python3
"""Follow the actual ordinary GET search form observed on MIT's homepage."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin,urlencode
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import json,time
root=Path(__file__).resolve().parents[1];began=time.monotonic()
home=json.loads((root/'code/part_b_mit_thesis_catalogue_output.json').read_text())['results'][0]
forms=[f for f in home['forms'] if any(c.get('name')=='query' for c in f['controls'])]
assert len(forms)==1 and forms[0]['form'].get('method','get').lower()=='get'
action=urljoin(home['url'],forms[0]['form']['action'])
class Page(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.links=[];self.skip=0
 def handle_starttag(self,t,a):
  a=dict(a)
  if t in ['script','style']:self.skip+=1
  if t=='a' and a.get('href'):self.links.append(urljoin(action,a['href']))
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
 def handle_data(self,s):
  if not self.skip and s.strip():self.text.append(s.strip())
def fetch(x):
 name,query=x;t=time.monotonic();url=action+'?'+urlencode({'query':query});r={'name':name,'query':query,'url':url}
 try:
  with urlopen(url,timeout=45) as f:raw=f.read();r.update(http_status=f.status,final_url=f.url,bytes=len(raw))
  h=raw.decode('utf8','replace');p=Page();p.feed(h)
  (root/'sources'/('part_b_mit_search_'+name+'.html')).write_text(h)
  (root/'sources'/('part_b_mit_search_'+name+'.txt')).write_text('\n'.join(p.text)+'\n')
  r.update(status='Public search HTML read' if raw else 'Empty response; no search results read',advertised_links=list(dict.fromkeys(p.links)),text='\n'.join(p.text))
 except Exception as e:r.update(status='error',error=str(e))
 r['elapsed_seconds']=time.monotonic()-t;return r
with ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(fetch,[('author','"Lieberman, David"'),('title','"Algebraic cycles"')]))
out={'results':rows,'elapsed_seconds':time.monotonic()-began}
(root/'code/part_b_mit_thesis_search_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'results':[{k:v for k,v in r.items() if k not in ['text','advertised_links']} for r in rows]},indent=2))
