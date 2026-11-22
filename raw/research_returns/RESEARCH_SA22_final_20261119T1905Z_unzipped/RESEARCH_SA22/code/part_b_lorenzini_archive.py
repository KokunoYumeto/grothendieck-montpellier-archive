#!/usr/bin/env python3
"""Search only the observed former author prefix and the exact cited catalogue."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import json,time,gzip
root=Path(__file__).resolve().parents[1];start=time.monotonic()
queries=[('missing_page_prefix',[('url','alpha.math.uga.edu/~lorenz/'),('matchType','prefix'),('filter','original:.*[Rr]aynaud.*'),('filter','statuscode:200'),('output','json'),('collapse','urlkey'),('limit','30'),('fl','timestamp,original,mimetype,statuscode')]),('exact_author_catalogue',[('url','http://alpha.math.uga.edu/~lorenz/paper.html'),('matchType','exact'),('filter','statuscode:200'),('output','json'),('limit','5'),('fl','timestamp,original,mimetype,statuscode')])]
def run(item):
 name,params=item;u='https://web.archive.org/cdx/search/cdx?'+urlencode(params);t=time.monotonic();r={'name':name,'url':u,'scope':'Public metadata within the old author prefix actually cited by Lorenzini2017, not an unrestricted university-domain scan'}
 try:
  with urlopen(u,timeout=30) as f:raw=f.read(1048577);r.update(http_status=f.status,bytes=len(raw))
  if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
  if len(raw)>1048576:r['status']='Response cap reached; no complete metadata result'
  else:r.update(status='Metadata read',records=json.loads(raw))
 except Exception as e:r.update(status='error',error=str(e))
 r['elapsed_seconds']=time.monotonic()-t;return r
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(run,queries))
out={'results':results,'elapsed_seconds':time.monotonic()-start}
(root/'code/part_b_lorenzini_archive_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
