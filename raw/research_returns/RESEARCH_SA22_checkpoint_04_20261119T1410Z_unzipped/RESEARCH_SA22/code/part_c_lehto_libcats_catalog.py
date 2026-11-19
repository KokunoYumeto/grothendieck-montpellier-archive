"""Ordinary public catalogue search, using the site's documented /g/ route."""
import concurrent.futures
import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
TARGETS=[('lehto','https://libcats.org/g/Lehto'),('virtanen','https://libcats.org/g/Virtanen')]

class Parse(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
        self.parts=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='a' and 'href' in d:
            self.links.append(d['href'])
    def handle_data(self,data):
        if data.strip():
            self.parts.append(data.strip())

def one(item):
    label,url=item
    begin=time.perf_counter()
    row={'label':label,'url':url}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'})
        with urllib.request.urlopen(request,timeout=55) as response:
            data=response.read()
            row.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        path=ROOT/'sources'/('part_c_lehto_libcats_'+label+'.html')
        path.write_bytes(data)
        row['saved']=str(path.relative_to(ROOT))
        parser=Parse()
        parser.feed(data.decode('utf-8','replace'))
        row['links']=parser.links
        row['text']='\n'.join(parser.parts)
    except Exception as error:
        row['error']=repr(error)
    row['elapsed_seconds']=time.perf_counter()-begin
    return row

started=datetime.datetime.now(datetime.timezone.utc).isoformat()
begin=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    rows=list(pool.map(one,TARGETS))
result={'started_utc':started,'elapsed_seconds':time.perf_counter()-begin,'scope':'Two ordinary public catalogue pages only. No book file, mirror, login, or challenge workaround.','results':rows}
text=json.dumps(result,indent=2)
(ROOT/'code'/'part_c_lehto_libcats_catalog_output.json').write_text(text+'\n')
print(text)
