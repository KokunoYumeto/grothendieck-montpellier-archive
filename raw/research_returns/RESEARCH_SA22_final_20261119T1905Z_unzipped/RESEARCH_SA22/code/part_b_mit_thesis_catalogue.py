#!/usr/bin/env python3
"""Inspect the ordinary MIT repository homepage for its public search route.

This preserves page links/form controls and visible repository configuration.
No login or restricted original file is requested.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import json,time,re
root=Path(__file__).resolve().parents[1]
url='https://dspace.mit.edu/home';began=time.monotonic()
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.forms=[];self.current=None;self.controls=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t in ['a','script','link'] and (a.get('href') or a.get('src')):self.links.append(urljoin(url,a.get('href',a.get('src'))))
  if t=='form':self.current={'form':a,'controls':[]};self.forms.append(self.current)
  if t in ['input','button','select'] and self.current is not None:self.current['controls'].append(a)
 def handle_endtag(self,t):
  if t=='form':self.current=None
r={'url':url,'scope':'Public repository search metadata; no restricted content'}
try:
 with urlopen(url,timeout=40) as f:
  raw=f.read();r.update(http_status=f.status,final_url=f.url,bytes=len(raw))
 h=raw.decode('utf8','replace');p=Page();p.feed(h)
 (root/'sources/part_b_mit_repository_home.html').write_text(h)
 r.update(status='Public HTML read',advertised_links=list(dict.fromkeys(p.links)),forms=p.forms)
 r['search_fragments']=[h[max(0,m.start()-150):m.end()+250] for m in re.finditer(r'(?:server/api|rest:|rest&quot;|search\?query|api/discover)',h)][:20]
except Exception as e:r.update(status='error',error=str(e))
r['elapsed_seconds']=time.monotonic()-began
(root/'code/part_b_mit_thesis_catalogue_output.json').write_text(json.dumps({'results':[r],'elapsed_seconds':r['elapsed_seconds']},indent=2)+'\n')
print(json.dumps(r,indent=2))
