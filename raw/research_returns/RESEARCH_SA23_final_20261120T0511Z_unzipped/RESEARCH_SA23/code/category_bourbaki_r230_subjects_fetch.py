from pathlib import Path
from html.parser import HTMLParser
import urllib.request,urllib.parse,hashlib,json,time
from concurrent.futures import ThreadPoolExecutor
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
class Links(HTMLParser):
    def __init__(self):super().__init__();self.urls=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t=='a' and 'href' in a:self.urls.append(a['href'])
class ArchiveOnly(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        if urllib.parse.urlsplit(newurl).hostname!='web.archive.org':raise RuntimeError('Stopped non-archive redirect: '+newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)
h=Links();h.feed((r/'sources/category_bourbaki_r230_redactions.html').read_text())
def fetch(name,needle):
    link=next(x for x in h.urls if needle in x)
    original=urllib.parse.urljoin('https://archives-bourbaki.ahp-numerique.fr/',link)
    url='http://web.archive.org/web/20251102030112/'+original;s=time.monotonic()
    try:
        with urllib.request.build_opener(ArchiveOnly()).open(url,timeout=35) as response:
            data=response.read();final=response.url;typ=response.headers.get('Content-Type');status=response.status
        p=r/f'sources/category_bourbaki_r230_subject_{name}.html';p.write_bytes(data)
        print(json.dumps({'url':url,'final_url':final,'status':status,'type':typ,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'saved':str(p),'seconds':time.monotonic()-s}),flush=True)
    except Exception as e:print(json.dumps({'url':url,'error_type':type(e).__name__,'error':str(e),'seconds':time.monotonic()-s}),flush=True)
with ThreadPoolExecutor(max_workers=2) as pool:
    fs=[pool.submit(fetch,'spectral','Th%C3%A9ories+spectrales'),pool.submit(fetch,'evt','Espaces+vectoriels+topologiques')]
    for f in fs:f.result()
