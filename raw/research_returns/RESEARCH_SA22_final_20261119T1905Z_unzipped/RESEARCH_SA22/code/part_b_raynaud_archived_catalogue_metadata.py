#!/usr/bin/env python3
"""Query public historical metadata for the actually advertised author URL.

The current endpoint returned403 and is not retried. This query requests only
an archive's public catalogue of earlier public captures, not a private file.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
import json,time,gzip
root=Path(__file__).resolve().parents[1];start=time.monotonic()
url='https://web.archive.org/cdx/search/cdx?'+urlencode([('url','https://libcats.org/g/Raynaud'),('matchType','exact'),('filter','statuscode:200'),('output','json'),('limit','5'),('fl','timestamp,original,mimetype,statuscode')])
r={'url':url,'scope':'Public historical catalogue metadata for one observed URL; no current denied endpoint retry, source file, credential or private archive requested'}
try:
 with urlopen(url,timeout=25) as f:raw=f.read(1024*1024+1);r.update(http_status=f.status,bytes=len(raw))
 if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
 if len(raw)>1024*1024:r['status']='Response cap reached; no complete result'
 else:r.update(status='Public archive metadata read',records=json.loads(raw))
except Exception as e:r.update(status='error',error=str(e))
r['elapsed_seconds']=time.monotonic()-start
(root/'code/part_b_raynaud_archived_catalogue_metadata_output.json').write_text(json.dumps({'results':[r],'elapsed_seconds':r['elapsed_seconds']},indent=2)+'\n');print(json.dumps(r,indent=2))
