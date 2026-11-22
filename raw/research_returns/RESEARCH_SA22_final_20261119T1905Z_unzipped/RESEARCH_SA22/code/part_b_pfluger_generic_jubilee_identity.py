#!/usr/bin/env python3
"""Inspect the one unqualified Commemoration Volume title and access metadata.

The identifier is an actual result of the new title-only catalogue query.
No item file is downloaded. The metadata identifies an unrelated1937volume.
"""
from pathlib import Path
from urllib.request import Request,urlopen
import gzip,json,time

root=Path(__file__).resolve().parents[1];start=time.monotonic()
identifier='in.ernet.dli.2015.402019'
url='https://archive.org/metadata/'+identifier
record={'identifier':identifier,'url':url,'scope':'Public item identity/access metadata only; no content-file request'}
try:
    with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:
        raw=response.read(2*1024*1024+1);record.update(http_status=response.status,bytes=len(raw))
    if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
    if len(raw)>2*1024*1024:record['status']='Response cap reached; not inspected'
    else:
        data=json.loads(raw)
        (root/'sources/part_b_pfluger_generic_jubilee_metadata.json').write_text(json.dumps(data,indent=2)+'\n')
        metadata=data.get('metadata',{})
        record.update(status='Public identity and file-access metadata read',
                      metadata={key:metadata[key] for key in ['identifier','title','creator','publisher','date','year','language','description','collection','access-restricted-item','is_access_restricted','isbn','oclc-id'] if key in metadata},
                      files=[{key:f.get(key) for key in ['name','format','size','private']} for f in data.get('files',[]) if f.get('format') in ['DjVuTXT','Text PDF','Image Container PDF','DjVu','JPEG Thumb'] or f.get('private')])
except Exception as error:record.update(status='Request failed; no retry/bypass',error=str(error))
record['elapsed_seconds']=time.monotonic()-start
output={'results':[record],'elapsed_seconds':record['elapsed_seconds']}
(root/'code/part_b_pfluger_generic_jubilee_identity_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(record,indent=2))
