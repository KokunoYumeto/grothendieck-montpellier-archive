"""Read public catalogue landing pages and report their documented HTML forms.
No private/login endpoint or correspondence image is requested.
"""
import concurrent.futures, hashlib, json, time, urllib.request
from pathlib import Path
from html.parser import HTMLParser

class PublicFormParser(HTMLParser):
 def __init__(self):
  super().__init__()
  self.forms=[]
  self.scripts=[]
  self.current=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='form':
   self.current={'action':a.get('action'),'method':a.get('method'),'id':a.get('id'),'fields':[]}
   self.forms.append(self.current)
  elif tag in ('input','select','button') and self.current is not None:
   self.current['fields'].append({'tag':tag,**{k:a.get(k) for k in ('name','id','type','value')}})
  elif tag=='script' and a.get('src'):
   self.scripts.append(a['src'])
 def handle_endtag(self,tag):
  if tag=='form': self.current=None

root = Path('RESEARCH_SA23')
items = [
 ('calames_public', 'https://calames.abes.fr/pub/'),
 ('folia_public', 'https://folia.scdi-montpellier.fr/'),
]
def fetch(item):
 name, url = item
 tick = time.monotonic()
 row = {'name':name,'url':url}
 try:
  with urllib.request.urlopen(url, timeout=25) as response:
   data = response.read()
   row.update(status=response.status, final_url=response.url)
  out = root/'sources'/('algebra_history_'+name+'.html')
  out.write_bytes(data)
  row.update(file=str(out.relative_to(root)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  parser=PublicFormParser()
  parser.feed(data.decode('utf-8',errors='replace'))
  row['forms']=parser.forms
  row['scripts']=parser.scripts
 except Exception as exc:
  row.update(error=type(exc).__name__+': '+str(exc))
 row['elapsed_seconds']=round(time.monotonic()-tick,6)
 return row
started=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 results=list(pool.map(fetch,items))
record={'purpose':'Public metadata catalogue search route discovery','results':results,'elapsed_seconds':round(time.monotonic()-started,6)}
out=json.dumps(record,ensure_ascii=False,indent=2)
(root/'logs/algebra_history_catalog17.json').write_text(out+'\n')
print(out)
