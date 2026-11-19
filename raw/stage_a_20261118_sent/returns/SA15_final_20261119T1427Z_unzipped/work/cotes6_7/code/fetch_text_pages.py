#!/usr/bin/env python3
"""Read exact, already selected primary-text pages; no browsing or enumeration."""
import json,urllib.request,hashlib
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
class TextParser(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'):self.skip+=1
  elif tag in ('p','div','h1','h2','h3','li','br'):self.out.append('\n')
 def handle_endtag(self,tag):
  if tag in ('script','style'):self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip:self.out.append(data)
W=Path('/workspace/scratch/26604d0a9a98/work/cotes6_7')
pages={
 'sga1_I8':'https://grothendiecksga.com/read/sga1/fr/I-8.html',
 'sga1_III7':'https://grothendiecksga.com/read/sga1/fr/III-7.html',
 'sga4_XIX5':'https://grothendiecksga.com/read/sga4/fr/XIX-5.html',
 'sga4_XVI4':'https://grothendiecksga.com/read/sga4/fr/XVI-4.html',
 'sga7_IX5':'https://grothendiecksga.com/read/sga7/fr/9-5.html',
}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(url,timeout=40) as r: data=r.read()
  parser=TextParser();parser.feed(data.decode('utf-8'))
  text='\n'.join(s.strip() for s in ''.join(parser.out).splitlines() if s.strip())
  path=W/'outputs'/f'{name}.txt';path.write_text(text)
  return {'name':name,'utc':datetime.now(timezone.utc).isoformat(),'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'output':str(path),'status':'opened full text'}
 except Exception as e:return {'name':name,'url':url,'status':'failed','error':str(e)}
with ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(fetch,pages.items()))
(W/'outputs/fetch_text_pages.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False))
