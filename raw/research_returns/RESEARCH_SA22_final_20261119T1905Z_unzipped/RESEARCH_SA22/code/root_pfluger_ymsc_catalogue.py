"""Follow the public YMSC catalogue form as advertised in its homepage.

The form action and target field IDs were read in
sources/part_a567_ymsc_home.html; no private endpoint is guessed.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
queries=[('author','Pfluger','searchauthor'),('title','Verheftung','searchtitle')]
def fetch(job):
    tag,query,target=job
    url='https://archive.ymsc.tsinghua.edu.cn/pacm_category/01?'+urllib.parse.urlencode(dict(show='time',size=5,**{'from':1},search=query,target=target))
    t=time.perf_counter(); row=dict(query=query,target=target,url=url)
    try:
        with urllib.request.urlopen(url,timeout=25) as response:
            body=response.read(); row['status']=response.status
        dest=ROOT/'sources'/('root_pfluger_ymsc_'+tag+'.html'); dest.write_bytes(body)
        html=body.decode('utf-8','replace')
        row.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),saved=str(dest.relative_to(ROOT)),
                   paper_links=sorted(set(re.findall(r'href=[\"\']([^\"\']*(?:pacm_paperurl|pacm_download)[^\"\']*)',html))),
                   title_matches=len(re.findall('Verheftung|Pfluger',html,re.I)))
    except Exception as exc: row['error']=str(exc)
    row['seconds']=time.perf_counter()-t
    return row
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    rows=list(pool.map(fetch,queries))
out=dict(scope='Two actual public catalogue form searches, not mathematical reading',requests=len(rows),results=rows,seconds=time.perf_counter()-START)
(ROOT/'code/root_pfluger_ymsc_catalogue_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
