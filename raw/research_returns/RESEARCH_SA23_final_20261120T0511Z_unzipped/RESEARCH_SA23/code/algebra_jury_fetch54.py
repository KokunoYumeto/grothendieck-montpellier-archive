"""Retrieve distinct public thesis-list and exact Cartan-report metadata routes."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser
base=pathlib.Path(__file__).resolve().parents[1]
targets=[
 ('imo_paris_theses','https://bibliotheque.imo.universite-paris-saclay.fr/bibliotheques-numeriques/theses/Paris/?critere=auteur','html'),
 ('calames_HC12_8','https://calames.abes.fr/prod/EadSearch.aspx?'+urllib.parse.urlencode({'Query':'Rech','fullText':'HC 12/8','from':1,'to':50}),'xml'),
 ('persee_schwartz','https://www.persee.fr/authority/416864','html'),
]
class Parser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.parts=[];self.links=[];self.link=None
 def handle_data(self,value):
  if value.strip():self.parts.append(value.strip())
  if self.link is not None:self.link['text']+=value
 def handle_starttag(self,tag,attrs):
  if tag=='a':self.link={'href':dict(attrs).get('href'),'text':''}
 def handle_endtag(self,tag):
  if tag=='a' and self.link is not None:self.links.append(self.link);self.link=None
def fetch(target):
 name,url,extension=target;start=time.monotonic()
 rec={'name':name,'url':url,'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   raw=response.read();rec.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
  path=base/f'sources/algebra_jury_{name}.{extension}';path.write_bytes(raw)
  rec.update(path=str(path.relative_to(base)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
  decoded=raw.decode('utf-8',errors='replace')
  if extension=='html':
   parser=Parser();parser.feed(decoded);text='\n'.join(parser.parts)
   path.with_suffix('.txt').write_text(text)
   rec.update(text_characters=len(text),matching_links=[x for x in parser.links if re.search(r'HC 12|Rapports|calames|groth|tensor',str(x),re.I)])
   rec['keyword_counts']={p:len(re.findall(p,text,re.I)) for p in ['groth','tensor','HC 12/8','CNRS','jury']}
  else:rec['xml']=decoded
 except Exception as error:rec['error']=repr(error)
 rec['elapsed_seconds']=time.monotonic()-start;rec['utc_completed']=datetime.datetime.now(datetime.timezone.utc).isoformat();return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,targets))
payload=json.dumps({'records':records},ensure_ascii=False,indent=2)
(base/'logs/algebra_jury_fetch54.json').write_text(payload+'\n');print(payload)
