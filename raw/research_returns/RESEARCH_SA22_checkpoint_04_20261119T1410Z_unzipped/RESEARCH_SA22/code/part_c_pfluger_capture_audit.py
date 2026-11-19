"""Read only public captures advertised by the successful CDX catalogue."""
import concurrent.futures
import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import time
import urllib.error
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
TARGETS=[
    ('landing_2017','https://web.archive.org/web/20171204062844id_/http://informaticsjournals.com/index.php/jims/article/view/16922'),
    ('view_redirect_2018','https://web.archive.org/web/20180923020804id_/http://www.informaticsjournals.com:80/index.php/jims/article/view/16922/14139'),
    ('download_redirect_2018','https://web.archive.org/web/20180923020034id_/http://www.informaticsjournals.com:80/index.php/jims/article/download/16922/14139'),
]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        return None

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and 'href' in a:
            self.links.append(a['href'])

def fetch(item):
    label,url=item
    row={'label':label,'url':url}
    begin=time.perf_counter()
    opener=urllib.request.build_opener(NoRedirect())
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'})
        try:
            response=opener.open(request,timeout=35)
        except urllib.error.HTTPError as error:
            response=error
        with response:
            data=response.read()
            row.update(status=response.status,location=response.headers.get('Location'),content_type=response.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        path=ROOT/'sources'/('part_c_pfluger_'+label+'.html')
        path.write_bytes(data)
        row['saved']=str(path.relative_to(ROOT))
        parser=Links()
        parser.feed(data.decode('utf-8','replace'))
        row['links']=parser.links
        row['text_prefix']=data[:1200].decode('utf-8','replace')
    except Exception as error:
        row['error']=repr(error)
    row['elapsed_seconds']=time.perf_counter()-begin
    return row

begin=time.perf_counter()
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    rows=list(pool.map(fetch,TARGETS))
result={'started_utc':started,'elapsed_seconds':time.perf_counter()-begin,'scope':'Three advertised public archived captures. Redirects are recorded without following, so no current publisher endpoint is contacted.','results':rows}
text=json.dumps(result,indent=2)
(ROOT/'code'/'part_c_pfluger_capture_audit_output.json').write_text(text+'\n')
print(text)
