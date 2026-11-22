from pathlib import Path
from html.parser import HTMLParser
import urllib.request,urllib.parse,hashlib,json,time
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
class Links(HTMLParser):
    def __init__(self): super().__init__();self.urls=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t=='a' and 'href' in a:self.urls.append(a['href'])
h=Links();h.feed((r/'sources/category_bourbaki_r230_archived_portal.html').read_text())
url=urllib.parse.urljoin('http://web.archive.org',next(x for x in h.urls if x.endswith('/redactions')))
assert urllib.parse.urlsplit(url).hostname=='web.archive.org'
start=time.monotonic()
try:
    with urllib.request.urlopen(url,timeout=35) as response:
        data=response.read();final=response.url;typ=response.headers.get('Content-Type');status=response.status
    p=r/'sources/category_bourbaki_r230_redactions.html';p.write_bytes(data)
    print(json.dumps({'url':url,'final_url':final,'status':status,'type':typ,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'saved':str(p),'seconds':time.monotonic()-start}),flush=True)
except Exception as e:print(json.dumps({'url':url,'error_type':type(e).__name__,'error':str(e),'seconds':time.monotonic()-start}),flush=True)
