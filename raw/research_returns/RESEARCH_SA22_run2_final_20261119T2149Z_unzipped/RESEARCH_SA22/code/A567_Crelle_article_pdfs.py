#!/usr/bin/env python3
"""Download article PDFs from rendering links actually present in GDZ manifests."""
import concurrent.futures,hashlib,json,re,subprocess,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError
import fitz
ROOT=Path(__file__).resolve().parents[1]
specs=[('0405','Rigidity of the arithmetic','A567_Nakamura1990_405'),
       ('0411','Galois rigidity','A567_Nakamura1990_411'),
       ('0487','On deformation','A567_IharaNakamura1997')]
def fetch(spec):
 vol,stem,name=spec;d=json.loads((ROOT/f'literature/A567_Crelle_manifest_{vol}.json').read_text())
 s=next(s for s in d['structures'] if s.get('label','').startswith(stem))
 url=next(x['@id'] for x in s['rendering'] if x.get('format')=='application/pdf')
 t=time.perf_counter();r={'name':name,'volume':vol,'title':s['label'],'url':url,'started_at_utc':datetime.now(timezone.utc).isoformat(),'manifest_canvas_count':len(s['ranges'])}
 try:
  with urlopen(url,timeout=40) as f:
   b=f.read();r.update(http_status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type'))
  r.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),is_pdf=b.startswith(b'%PDF-'))
  p=ROOT/'literature'/(name+('.pdf' if b.startswith(b'%PDF-') else '.html'));p.write_bytes(b);r['saved']=str(p.relative_to(ROOT))
  if b.startswith(b'%PDF-'):
   doc=fitz.open(p);r['pdf_pages']=len(doc);txt='\n\n'.join(f'PDF PAGE {i+1}\n'+pg.get_text() for i,pg in enumerate(doc));p.with_suffix('.txt').write_text(txt);r['text_characters']=len(txt)
 except HTTPError as e:r.update(http_status=e.code,error=type(e).__name__,message=str(e))
 except Exception as e:r.update(error=type(e).__name__,message=str(e))
 r.update(finished_at_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-t);return r
t=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,specs))
(ROOT/'logs/A567_Crelle_article_pdfs.json').write_text(json.dumps({'requests_count':3,'elapsed_seconds':time.perf_counter()-t,'scope':'Observed article-specific rendering URLs from publicly served GDZ IIIF manifests; no login or closed publisher endpoint','results':rows},indent=2)+'\n')
for r in rows:print(json.dumps(r,ensure_ascii=False))
