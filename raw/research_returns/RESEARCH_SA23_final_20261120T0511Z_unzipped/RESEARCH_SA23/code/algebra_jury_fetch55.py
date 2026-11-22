"""Fetch only public, actually linked institutional catalogue pages.

Calames record URLs were supplied by Persée authority 416864 and the
Sorbonne archives page, respectively.  No authentication or challenge retry.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, hashlib, json, time, datetime
from html.parser import HTMLParser
class Parser(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.parts=[];self.links=[];self.scripts=[];self.link=None;self.intitle=False;self.title=''
 def handle_data(self,value):
  if value.strip():self.parts.append(value.strip())
  if self.link is not None:self.link['text']+=value
  if self.intitle:self.title+=value
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='a':self.link={'href':d.get('href',''),'text':''}
  if tag=='script' and d.get('src'):self.scripts.append(d['src'])
  if tag=='title':self.intitle=True
 def handle_endtag(self,tag):
  if tag=='a' and self.link is not None:self.links.append(self.link);self.link=None
  if tag=='title':self.intitle=False
R=Path('RESEARCH_SA23')
sources=[
 ('sorbonne_archives','https://www.sorbonne-universite.fr/universite/archives'),
 ('calames_cartan_reports','https://calames.abes.fr/pub/ms/Calames-2025061317113412349'),
 ('calames_science_dean','https://calames.abes.fr/pub/ms/FileId-5518'),
]
def fetch(item):
 name,url=item; tick=time.monotonic(); d={'name':name,'url':url,'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=25) as r:
   b=r.read(); d.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
  p=R/'sources'/('algebra_jury_'+name+'.html'); p.write_bytes(b)
  soup=Parser();soup.feed(b.decode('utf-8',errors='replace'));text='\n'.join(soup.parts)
  p.with_suffix('.txt').write_text(text)
  d.update(path=str(p.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),text_characters=len(text))
  d['title']=soup.title
  d['links']=[a for a in soup.links if any(k in (a['href']+' '+a['text']).lower() for k in ['xml','ead','pdf','5518','groupes','rapports'])]
  d['scripts']=soup.scripts
  d['keyword_counts']={k:text.lower().count(k.lower()) for k in ['Grothendieck','Hilbert','genre','trace','doctorat','rapports','1953','Lie','CNRS']}
 except Exception as e: d['error']=type(e).__name__+': '+str(e)
 d['elapsed_seconds']=time.monotonic()-tick;d['utc_completed']=datetime.datetime.now(datetime.timezone.utc).isoformat(); return d
with ThreadPoolExecutor(max_workers=3) as ex: records=list(ex.map(fetch,sources))
s=json.dumps({'records':records},ensure_ascii=False,indent=2)
(R/'logs/algebra_jury_fetch55.json').write_text(s+'\n'); print(s)
