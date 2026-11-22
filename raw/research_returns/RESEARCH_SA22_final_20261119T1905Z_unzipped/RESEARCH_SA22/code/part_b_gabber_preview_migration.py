#!/usr/bin/env python3
"""Check a dead advertised public preview on the current preview service.

The 2018 landing explicitly advertises /pdf/preview/10.1007/BF02773001 on the
old page-one.live.cf.public.springer.com host, which now returns ordinary404.
The current publisher's page-one.springer.com public preview host was actually
opened for Raynaud. This is an expressly logged stale-host repair, not a claim
that the current Gabber landing advertises this URL. The path is unchanged;
no subscription route, authentication, page range or preview limit is changed.
An independent exact old-URL archive metadata query is also recorded.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import gzip,hashlib,json,time

root=Path(__file__).resolve().parents[1];started=time.monotonic()
old='https://page-one.live.cf.public.springer.com/pdf/preview/10.1007/BF02773001'
params=[('url',old),('matchType','exact'),('output','json'),
        ('filter','statuscode:200'),('collapse','digest'),('limit','3'),
        ('fl','timestamp,original,statuscode,mimetype')]
jobs=[('old_preview_archive','https://web.archive.org/cdx/search/cdx?'+urlencode(params)),
      ('current_public_preview_host','https://page-one.springer.com/pdf/preview/10.1007/BF02773001')]

def fetch(job):
    kind,url=job;begin=time.monotonic();record={'kind':kind,'url':url}
    try:
        with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:
            raw=response.read(5*1024*1024+1)
            record.update(http_status=response.status,final_url=response.url,bytes=len(raw),content_type=response.headers.get('Content-Type',''))
        if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
        if len(raw)>5*1024*1024:record['status']='Response cap reached; not inspected'
        elif kind=='old_preview_archive':
            record.update(status='Exact public metadata read',response=json.loads(raw))
        elif raw.startswith(b'%PDF'):
            import fitz
            path=root/'sources/part_b_gabber_current_preview.pdf';path.write_bytes(raw)
            doc=fitz.open(path);text='\n'.join(p.get_text() for p in doc)
            (root/'sources/part_b_gabber_current_preview.txt').write_text(text)
            record.update(status='Public original preview PDF fetched; visual reading required',pages=len(doc),sha256=hashlib.sha256(raw).hexdigest(),text_characters=len(text))
        else:
            (root/'sources/part_b_gabber_current_preview_nonpdf.html').write_bytes(raw)
            record['status']='Response is not PDF; no original mathematics read; stopped'
    except Exception as error:record.update(status='Request failed; no retry/bypass',error=str(error))
    record['elapsed_seconds']=time.monotonic()-begin;return record

with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(fetch,jobs))
output={'results':results,'elapsed_seconds':time.monotonic()-started}
(root/'code/part_b_gabber_preview_migration_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
