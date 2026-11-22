#!/usr/bin/env python3
"""Four bounded searches through observed public GDZ and EuDML GET forms."""
import concurrent.futures,hashlib,json,time
from datetime import datetime,timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen,Request
from urllib.error import HTTPError

ROOT=Path(__file__).resolve().parents[1]
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.words=[];self.links=[];self.anchor=None;self.skip=0
 def handle_starttag(self,t,a):
  a=dict(a)
  if t in ('script','style'):self.skip+=1
  if t=='a':self.anchor={'href':a.get('href'),'text':''};self.links.append(self.anchor)
 def handle_endtag(self,t):
  if t in ('script','style') and self.skip:self.skip-=1
  if t=='a':self.anchor=None
 def handle_data(self,s):
  if not self.skip and s.strip():
   self.words.append(s.strip())
   if self.anchor is not None:self.anchor['text']+=s.strip()+' '
def fetch(job):
 name,url=job;t=time.perf_counter();r={'name':name,'url':url,'started_at_utc':datetime.now(timezone.utc).isoformat()}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as f:
   b=f.read();r.update(http_status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'))
 except HTTPError as e:
  b=e.read();r.update(http_status=e.code,final_url=e.url,content_type=e.headers.get('Content-Type'))
 except Exception as e:
  r.update(error=type(e).__name__,message=str(e),finished_at_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-t);return r
 p=ROOT/'literature'/('A567_Crelle_'+name+'.html');p.write_bytes(b)
 q=Parser();q.feed(b.decode('utf-8',errors='replace'));p.with_suffix('.txt').write_text('\n'.join(q.words))
 r.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),saved=str(p.relative_to(ROOT)),links=q.links,
          visible_text='\n'.join(q.words),finished_at_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-t)
 return r

if __name__=='__main__':
 jobs=[]
 for name,q in [('gdz_punctured','"punctured projective"'),('gdz_degenerate','"maximally degenerate"')]:
  jobs.append((name,'https://gdz.sub.uni-goettingen.de/suche?'+urlencode({'search[q]':q,'search[searchType]':'metadata'})))
 for name,q in [('eudml_punctured','punctured projective'),('eudml_degenerate','maximally degenerate')]:
  jobs.append((name,'https://eudml.org/searchForm?'+urlencode({'SCHEME':'general','OPERATOR':'AND','expression-1':'EQUALS_names','search-box-1':q})))
 t=time.perf_counter()
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(fetch,jobs))
 out={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'query_count':len(jobs),'elapsed_seconds':time.perf_counter()-t,'form_provenance':'Observed public GDZ/EuDML form fields; exact form snapshots previously recorded in notes/C_Fujiwara_public_catalogues_1948.md and its saved response HTML. No login or restricted endpoint.','results':rows}
 (ROOT/'logs/A567_Crelle_public_catalogues.json').write_text(json.dumps(out,indent=2)+'\n')
 for r in rows:
  print(json.dumps({k:v for k,v in r.items() if k not in ['links','visible_text']},ensure_ascii=False))
  hits=[a for a in r.get('links',[]) if any(x in (a.get('href') or '') for x in ['/id/','/doc/'])]
  print('RESULT_LINKS',json.dumps(hits,ensure_ascii=False))
  if not hits:print('TEXT',r.get('visible_text','')[:4500])
