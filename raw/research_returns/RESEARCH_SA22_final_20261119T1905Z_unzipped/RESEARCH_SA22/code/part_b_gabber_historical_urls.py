#!/usr/bin/env python3
"""Check public archive catalogues for historical Gabber URL variants.

These prefix queries extend the previous single exact publisher-PDF lookup
to encoded DOI paths, historical SpringerLink URLs, and the public IHES
author page. They do not request restricted current publisher content.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic()
queries=[('springer_doi_variants','link.springer.com/*BF02773001*'),('historic_springerlink','*.springerlink.com/*BF02773001*'),('ihes_author_prefix','www.ihes.fr/~gabber/*')]
def fetch(x):
 name,query=x;t=time.monotonic();url='https://web.archive.org/cdx/search/cdx?'+urlencode({'url':query,'output':'json','filter':'statuscode:200','collapse':'urlkey'})
 r={'name':name,'url':url,'scope':'Public historical URL metadata only'}
 try:
  with urlopen(url,timeout=35) as f:raw=f.read();r.update(http_status=f.status,bytes=len(raw))
  r.update(status='Public CDX response read',response=json.loads(raw))
 except Exception as e:r.update(status='error',error=str(e))
 r['elapsed_seconds']=time.monotonic()-t;return r
with ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(fetch,queries))
out={'results':rows,'elapsed_seconds':time.monotonic()-start}
(root/'code/part_b_gabber_historical_urls_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'results':[{k:v for k,v in r.items() if k!='response'} for r in rows]},indent=2))
