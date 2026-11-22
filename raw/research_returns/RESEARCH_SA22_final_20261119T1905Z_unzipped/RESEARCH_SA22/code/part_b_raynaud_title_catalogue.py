#!/usr/bin/env python3
"""Use a public catalogue's actual GET form for a new Raynaud title query.

The earlier author-route /g/Raynaud is not retried. The actual form is read
from the independently opened C-agent catalogue HTML; no headers or access
parameters are changed and no book is downloaded by this utility.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlencode
from urllib.request import urlopen
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic()
class Page(HTMLParser):
 def __init__(self):super().__init__();self.base=None;self.forms=[];self.current=None;self.links=[];self.text=[];self.skip=0
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='base':self.base=a.get('href')
  if t=='form':self.current={'form':a,'controls':[]};self.forms.append(self.current)
  if t=='input' and self.current is not None:self.current['controls'].append(a)
  if t=='a' and a.get('href'):self.links.append(a['href'])
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t=='form':self.current=None
  if t in ['script','style']:self.skip-=1
 def handle_data(self,s):
  if not self.skip and s.strip():self.text.append(s.strip())
source=root/'sources/part_c_lehto_libcats_lehto.html'
p=Page();p.feed(source.read_text())
forms=[f for f in p.forms if f['form'].get('id')=='searchForm']
assert len(forms)==1 and forms[0]['form'].get('method')=='get'
assert {'q','e','t'} <= {a.get('name') for a in forms[0]['controls']}
base=urljoin('https://libcats.org/g/Lehto',p.base or '')
action=urljoin(base,forms[0]['form']['action'])
url=action+'?'+urlencode({'q':'Faisceaux amples','e':'1','t':'0'})
r={'url':url,'form_source':'sources/'+source.name,'query':'Faisceaux amples','scope':'New actual-form title query; earlier denied author route not repeated'}
try:
 with urlopen(url,timeout=55) as response:raw=response.read();r.update(http_status=response.status,final_url=response.url,bytes=len(raw))
 h=raw.decode('utf8','replace');p=Page();p.feed(h)
 (root/'sources/part_b_raynaud_title_catalogue.html').write_text(h)
 (root/'sources/part_b_raynaud_title_catalogue.txt').write_text('\n'.join(p.text)+'\n')
 r.update(status='Public catalogue HTML read' if raw else 'Empty response; no catalogue read',advertised_links=list(dict.fromkeys(urljoin(url,x) for x in p.links)),text='\n'.join(p.text))
except Exception as e:r.update(status='error',error=str(e))
r['elapsed_seconds']=time.monotonic()-start
(root/'code/part_b_raynaud_title_catalogue_output.json').write_text(json.dumps({'results':[r],'elapsed_seconds':r['elapsed_seconds']},indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k not in ['text','advertised_links']},indent=2))
