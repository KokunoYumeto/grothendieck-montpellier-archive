"""Single ordinary retrievals of actually discovered public URLs; no access bypass."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,hashlib,json,time,datetime
from html.parser import HTMLParser
R=Path('RESEARCH_SA23')
targets=[
 ('finna_marc','https://kansalliskirjasto.finna.fi/Record/vaari.1573717/Export?style=MARCXML','xml'),
 ('unesdoc_home','https://unesdoc.unesco.org/','html'),
 ('koranyi_review','https://acta.bibl.u-szeged.hu/13816/1/math_017_261-268.pdf','pdf'),
 ('csg_works','https://csg.igrothendieck.org/published-works/','html')]
def fetch(item):
 name,url,ext=item; t=time.monotonic();d={'name':name,'url':url,'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=25) as r:b=r.read();d.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
  p=R/'sources'/('algebra_mendoza_'+name+'.'+ext);p.write_bytes(b)
  d.update(path=str(p.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
  if ext!='pdf': d['text_prefix']=b.decode('utf-8',errors='replace')[:1800]
 except Exception as e:d['error']=type(e).__name__+': '+str(e)
 d.update(elapsed_seconds=time.monotonic()-t,utc_completed=datetime.datetime.now(datetime.timezone.utc).isoformat());return d
with ThreadPoolExecutor(max_workers=4) as ex:records=list(ex.map(fetch,targets))
s=json.dumps({'records':records},ensure_ascii=False,indent=2);(R/'logs/algebra_mendoza_fetch57.json').write_text(s+'\n');print(s)
