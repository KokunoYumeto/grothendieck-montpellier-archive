#!/usr/bin/env python3
"""Download the article identified by the official volume METS record."""
from pathlib import Path
import hashlib,json,time,urllib.request,subprocess
R=Path(__file__).resolve().parents[1]
out=R/'sources'/'bloch_gdz';out.mkdir(exist_ok=True)
u='https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0037/LOG_0017.pdf'
t=time.perf_counter();rec={'url':u,'mets_log':'LOG_0017','mets_title':'Some Elementary Theorem about Algebraic Cycles on Abelian Varieties.'}
try:
 with urllib.request.urlopen(u,timeout=45) as r:data=r.read();rec.update(status=r.status,content_type=r.headers.get('Content-Type'))
 rec.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 if not data.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
 path=out/'bloch1976.pdf';path.write_bytes(data)
 import fitz
 doc=fitz.open(path);rec['pages']=len(doc)
 (out/'bloch1976_extracted.txt').write_text('\n'.join(p.get_text() for p in doc))
 rec['outcome']='downloaded; original scan, text extraction may be empty'
except Exception as e:rec['error']=str(e)
rec['runtime_seconds']=time.perf_counter()-t
(R/'code'/'fetch_bloch_gdz_article_output.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
