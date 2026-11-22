"""Ordinary public retrieval of two advertised Schwartz retrospectives."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import urllib.request
import urllib.error
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
SOURCES=[
 ('historical_roots1982','https://sites.mathdoc.fr/OCLS/pdf/OCLS_1982__63__11_0.pdf'),
 ('souvenirs_dieudonne1994','https://sites.mathdoc.fr/OCLS/pdf/OCLS_1994c.pdf')]

class PublicRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if urlparse(newurl).hostname != 'sites.mathdoc.fr':
            raise ValueError('Unadvertised cross-host redirect: '+newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)

opener=urllib.request.build_opener(PublicRedirect)
rows=[]
for name,url in SOURCES:
    start=time.monotonic()
    row={'name':name,'url':url,'started_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with opener.open(url,timeout=30) as response:
            data=response.read()
            row.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
        row.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        if data.startswith(b'%PDF'):
            path=ROOT/'sources'/f'category_schwartz_{name}.pdf'
            path.write_bytes(data)
            row.update(path=str(path.relative_to(ROOT)),pdf=True)
        else:
            path=ROOT/'sources'/f'category_schwartz_{name}_response.txt'
            path.write_bytes(data)
            row.update(path=str(path.relative_to(ROOT)),pdf=False)
    except Exception as error:
        row.update(error=repr(error))
    row['elapsed_seconds']=time.monotonic()-start
    rows.append(row)
    print(json.dumps(row,ensure_ascii=False),flush=True)
    (ROOT/'logs/category_schwartz_firstperson_fetch.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
