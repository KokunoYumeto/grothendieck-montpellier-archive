#!/usr/bin/env python3
"""Search public archive metadata for the advertised missing Raynaud page.

Lorenzini's public page advertises the exact PDF filename; its current link
returned404. This performs only public CDX catalogue lookups, not content
requests or access-control workarounds.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic()
targets=[('current','dinolorenzini.franklinresearch.uga.edu/sites/default/files/inline-files/papers/RaynaudFaisceauxAmplesPage175.pdf'),('uga_hosts','*.uga.edu/*RaynaudFaisceauxAmplesPage175.pdf')]
def fetch(x):
 name,query=x;t=time.monotonic();url='https://web.archive.org/cdx/search/cdx?'+urlencode({'url':query,'output':'json','filter':'statuscode:200','collapse':'urlkey'})
 r={'name':name,'url':url,'scope':'Public archive catalogue; no original-content request'}
 try:
  with urlopen(url,timeout=35) as f:raw=f.read();r.update(http_status=f.status,bytes=len(raw))
  r.update(status='Public CDX response read',response=json.loads(raw))
 except Exception as e:r.update(status='error',error=str(e))
 r['elapsed_seconds']=time.monotonic()-t;return r
with ThreadPoolExecutor(max_workers=2) as pool:rows=list(pool.map(fetch,targets))
out={'results':rows,'elapsed_seconds':time.monotonic()-start}
(root/'code/part_b_raynaud_page175_archive_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
