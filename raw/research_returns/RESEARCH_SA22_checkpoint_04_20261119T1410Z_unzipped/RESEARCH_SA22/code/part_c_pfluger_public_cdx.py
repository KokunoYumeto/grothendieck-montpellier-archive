"""Public archive catalogue lookup for the historical Pfluger OJS page."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    ('www_landing', 'www.informaticsjournals.com/index.php/jims/article/view/16922'),
    ('bare_landing', 'informaticsjournals.com/index.php/jims/article/view/16922'),
    ('www_view_children', 'www.informaticsjournals.com/index.php/jims/article/view/16922/*'),
    ('bare_view_children', 'informaticsjournals.com/index.php/jims/article/view/16922/*'),
    ('www_download_children', 'www.informaticsjournals.com/index.php/jims/article/download/16922/*'),
    ('bare_download_children', 'informaticsjournals.com/index.php/jims/article/download/16922/*'),
]

def check(item):
    label,pattern=item
    query=urllib.parse.urlencode({'url':pattern,'output':'json','collapse':'urlkey','fl':'timestamp,original,mimetype,statuscode','limit':'100'})
    url='https://web.archive.org/cdx/search/cdx?'+query
    row={'label':label,'pattern':pattern,'url':url}
    begin=time.perf_counter()
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'})
        with urllib.request.urlopen(request,timeout=35) as response:
            data=response.read()
            row.update(status=response.status,final_url=response.url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        path=ROOT/'sources'/('part_c_pfluger_cdx_'+label+'.json')
        path.write_bytes(data)
        row['saved']=str(path.relative_to(ROOT))
        try:
            row['catalogue']=json.loads(data)
        except Exception:
            row['text_prefix']=data[:1000].decode('utf-8','replace')
    except Exception as error:
        row['error']=repr(error)
    row['elapsed_seconds']=time.perf_counter()-begin
    return row

begin=time.perf_counter()
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    rows=list(pool.map(check,PATTERNS))
result={'started_utc':started,'elapsed_seconds':time.perf_counter()-begin,'scope':'Six public Wayback CDX catalogue requests only. No current publisher fulltext, credentials, or private archive files.','results':rows}
text=json.dumps(result,indent=2)
(ROOT/'code'/'part_c_pfluger_public_cdx_output.json').write_text(text+'\n')
print(text)
