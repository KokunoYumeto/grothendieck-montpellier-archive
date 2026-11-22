#!/usr/bin/env python3
"""Check public archive availability for cited source URLs, without bypasses."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import json,time
root=Path(__file__).resolve().parents[1]
jobs=[
('Gabber Springer publisher PDF','https://link.springer.com/content/pdf/10.1007/BF02773001.pdf'),
('Fujiwara historic Euclid landing','http://projecteuclid.org/euclid.dmj/1077245853'),
('Fujiwara historic Euclid public PDF','http://projecteuclid.org/download/pdf_1/euclid.dmj/1077245853'),
('Fujiwara current Euclid DOI download','https://projecteuclid.org/journalArticle/Download?urlid=10.1215/S0012-7094-95-08002-8')]
def run(job):
 name,source=job;url='https://archive.org/wayback/available?'+urlencode({'url':source});t=time.time();out={'source':name,'source_url':source,'lookup_url':url}
 try:
  with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:out['metadata']=json.load(response)
  out['status']='metadata read'
 except Exception as e:out.update(status='not read',error=str(e))
 out['elapsed_seconds']=round(time.time()-t,2);return out
with ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(run,jobs))
(root/'code/part_b_public_archives_output.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out:print(json.dumps(r))
