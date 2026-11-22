"""Follow the two actual public archived congress-PDF links, not live-host URLs."""
from pathlib import Path
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.parse,json,time,hashlib,subprocess
from datetime import datetime,timezone
b=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.playback=None
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='a' and d.get('href'):self.links.append(d['href'])
  if t=='iframe' and d.get('id')=='playback':self.playback=d.get('src')
class ArchiveOnly(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,headers,newurl):
  if urllib.parse.urlsplit(newurl).hostname!='web.archive.org':raise RuntimeError('Stopped redirect outside public archive: '+newurl)
  return super().redirect_request(req,fp,code,msg,headers,newurl)
def fetch(n):
 p=Links();p.feed((b/f'sources/geometry_bourbaki_congress_{n}.html').read_text())
 url=next(x for x in p.links if '/files/original/' in x and x.endswith('.pdf'))
 rows=[]
 for step in range(2):
  row={'record':n,'step':step,'url':url};start=time.perf_counter()
  try:
   if urllib.parse.urlsplit(url).hostname!='web.archive.org':raise ValueError('Non-archive initial URL')
   with urllib.request.build_opener(ArchiveOnly()).open(url,timeout=45) as r:
    data=r.read();row.update(final_url=r.url,status=r.status,content_type=r.headers.get('Content-Type'))
   pdf=data.startswith(b'%PDF-');dest=b/f'sources/geometry_bourbaki_congress_{n}_{step}'+Path('') if False else b/f'sources/geometry_bourbaki_congress_{n}_{step}.{ "pdf" if pdf else "html"}'
   dest.write_bytes(data);row.update(path=str(dest.relative_to(b)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),is_pdf=pdf)
   if pdf:
    cmds=[]
    for argv in [['pdfinfo',str(dest)],['pdftotext','-layout',str(dest),str(b/f'notes/geometry_bourbaki_congress_{n}_native.txt')]]:
     t=time.perf_counter();s=subprocess.run(argv,capture_output=True,text=True);cmds.append({'argv':argv,'exit_code':s.returncode,'stdout':s.stdout,'stderr':s.stderr,'elapsed_seconds':time.perf_counter()-t})
    row['commands']=cmds
   else:
    q=Links();q.feed(data.decode(errors='replace'))
    url=urllib.parse.urljoin(row['final_url'],q.playback) if q.playback else None
   row['elapsed_seconds']=time.perf_counter()-start;rows.append(row)
   if pdf or not url:break
  except Exception as e:
   row.update(error_type=type(e).__name__,error=str(e),elapsed_seconds=time.perf_counter()-start);rows.append(row);break
 return rows
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=2) as ex:rows=[x for group in ex.map(fetch,[803,804]) for x in group]
log={'utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'elapsed_seconds':time.perf_counter()-start,'no_live_AHP_request':True}
(b/'logs/geometry_bourbaki_congress_pdfs.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log,indent=2))
