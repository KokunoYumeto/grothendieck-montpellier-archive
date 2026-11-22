#!/usr/bin/env python3
"""Bounded public CDX queries using documented explicit matching and filters.

The official CDX README was opened before this correction. Interior glob
syntax is not used. Each response is capped at2MiB and30 metadata rows.
No original-content URL or access-control mechanism is requested.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import json,time,datetime
root=Path(__file__).resolve().parents[1];start=time.monotonic()
jobs=[
 ('gabber_current','link.springer.com','host','.*[Bb][Ff]02773001.*'),
 ('gabber_historical','springerlink.com','domain','.*[Bb][Ff]02773001.*'),
 ('raynaud_publisher','link.springer.com','host','.*([Bb][Ff][Bb]0059504|978-3-540-36249-4).*'),
 ('raynaud_missing_page','uga.edu','domain','.*[Rr]aynaud[Ff]aisceaux[Aa]mples[Pp]age175[.]pdf.*'),
]
def fetch(job):
 name,host,match,regex=job;t=time.monotonic()
 params=[('url',host),('matchType',match),('filter','original:'+regex),('filter','statuscode:200'),('output','json'),('collapse','urlkey'),('limit','30'),('fl','timestamp,original,mimetype,statuscode')]
 url='https://web.archive.org/cdx/search/cdx?'+urlencode(params)
 r={'name':name,'url':url,'scope':'Public archive metadata with explicit regex filter; response capped'}
 try:
  with urlopen(url,timeout=30) as f:raw=f.read(2097153);r.update(http_status=f.status,bytes_read=len(raw))
  if len(raw)>2097152:r.update(status='Response cap reached; no complete catalogue read')
  else:r.update(status='Public CDX response read',response=json.loads(raw))
 except Exception as e:r.update(status='error',error=str(e))
 r['elapsed_seconds']=time.monotonic()-t
 print(json.dumps({k:v for k,v in r.items() if k!='response'}),flush=True)
 return r
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,jobs))
out={'results':rows,'elapsed_seconds':time.monotonic()-start,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'code/part_b_filtered_cdx_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'requests':len(rows),'elapsed_seconds':out['elapsed_seconds']},indent=2))
