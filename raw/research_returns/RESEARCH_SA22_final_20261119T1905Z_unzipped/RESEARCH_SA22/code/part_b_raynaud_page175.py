#!/usr/bin/env python3
"""Follow the actual public replacement-page link from the opened2017 catalogue.
Visual inspection after the first run identifies a modern scholarly retyping,
not an original publisher scan. The complete book is not supplied by this link.
"""
from pathlib import Path
from urllib.request import urlopen
import json,time,gzip,hashlib
root=Path(__file__).resolve().parents[1];start=time.monotonic()
url='https://web.archive.org/web/20170821032054id_/http://alpha.math.uga.edu:80/~lorenz/RaynaudFaisceauxAmplesPage175.pdf'
r={'url':url,'scope':'Single scholarly replacement page advertised by the actually opened catalogue; not an original publisher scan or a whole book retrieval'}
try:
 with urlopen(url,timeout=30) as f:raw=f.read(5*1024*1024+1);r.update(http_status=f.status,bytes=len(raw),final_url=f.url,content_type=f.headers.get('Content-Type',''))
 if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
 if len(raw)>5*1024*1024:r['status']='Response cap reached; not read'
 elif not raw.startswith(b'%PDF'):r['status']='Not a PDF; no original page read';r['response_prefix']=raw[:200].decode('utf8','replace')
 else:
  p=root/'sources/part_b_raynaud_page175.pdf';p.write_bytes(raw)
  import fitz
  d=fitz.open(p);text='\n'.join(x.get_text() for x in d)
  (root/'sources/part_b_raynaud_page175.txt').write_text(text)
  r.update(status='Replacement-page PDF fetched; requires visual reading',pages=len(d),sha256=hashlib.sha256(raw).hexdigest(),text_characters=len(text))
except Exception as e:r.update(status='error',error=str(e))
r['elapsed_seconds']=time.monotonic()-start
(root/'code/part_b_raynaud_page175_output.json').write_text(json.dumps({'results':[r],'elapsed_seconds':r['elapsed_seconds']},indent=2)+'\n');print(json.dumps(r,indent=2))
