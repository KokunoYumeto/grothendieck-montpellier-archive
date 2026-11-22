#!/usr/bin/env python3
"""Follow the exact public preview advertised by the opened 2018 landing."""
from pathlib import Path
from urllib.request import Request,urlopen
import gzip,hashlib,json,time

root=Path(__file__).resolve().parents[1]
url='https://page-one.live.cf.public.springer.com/pdf/preview/10.1007/BF02773001'
start=time.monotonic()
record={'url':url,'scope':'Exact public Download preview PDF href in the actual 2018 publisher landing; no URL/preview parameter change'}
try:
    with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:
        raw=response.read(5*1024*1024+1)
        record.update(http_status=response.status,final_url=response.url,bytes=len(raw),content_type=response.headers.get('Content-Type',''))
    if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
    if len(raw)>5*1024*1024:record['status']='Response cap reached; no source read'
    elif raw.startswith(b'%PDF'):
        import fitz
        path=root/'sources/part_b_gabber_original_preview.pdf';path.write_bytes(raw)
        doc=fitz.open(path)
        text='\n'.join(p.get_text() for p in doc)
        (root/'sources/part_b_gabber_original_preview.txt').write_text(text)
        record.update(status='Original preview PDF fetched; visual reading still required',pages=len(doc),sha256=hashlib.sha256(raw).hexdigest(),text_characters=len(text))
    else:
        (root/'sources/part_b_gabber_original_preview_nonpdf.html').write_bytes(raw)
        record['status']='Response is not PDF; no mathematical source read; no bypass/retry'
except Exception as error:record.update(status='Request failed; no bypass/retry',error=str(error))
record['elapsed_seconds']=time.monotonic()-start
output={'results':[record],'elapsed_seconds':record['elapsed_seconds']}
(root/'code/part_b_gabber_original_preview_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
