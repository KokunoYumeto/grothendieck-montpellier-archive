#!/usr/bin/env python3
"""One ordinary retry after an earlier public API rate-limit response.

The earlier attempt was at17:45UTC; this retry is more than90minutes later.
No account, API key, alternate entitlement, or access workaround is used.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,time,urllib.request,urllib.error
root=Path(__file__).resolve().parents[1]
out=[]
for doi in ['10.1007/BF02773001','10.1215/S0012-7094-95-08002-8']:
 url='https://api.semanticscholar.org/graph/v1/paper/DOI:'+doi+'?fields=title,year,openAccessPdf,url,externalIds'
 r={'doi':doi,'url':url,'requested_utc':datetime.now(timezone.utc).isoformat()};start=time.perf_counter()
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Research-source-audit'}),timeout=25) as response:
   body=response.read();r.update(http_status=response.status,body=json.loads(body),bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
 except urllib.error.HTTPError as e:
  body=e.read();r.update(http_status=e.code,body=body.decode('utf-8',errors='replace'))
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-start,3);out.append(r)
(root/'logs/ROOT_originals_semantic_retry.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
