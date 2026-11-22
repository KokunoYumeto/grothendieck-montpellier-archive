from pathlib import Path
from html.parser import HTMLParser
import urllib.request,urllib.parse,hashlib,json,time,subprocess
from concurrent.futures import ThreadPoolExecutor
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
class Links(HTMLParser):
    def __init__(self):super().__init__();self.urls=[];self.playback=None
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t=='a' and 'href' in a:self.urls.append(a['href'])
        if t=='iframe' and a.get('id')=='playback':self.playback=a.get('src')
class ArchiveOnly(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        if urllib.parse.urlsplit(newurl).hostname!='web.archive.org':raise RuntimeError('Stopped non-archive redirect: '+newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)
def fetch(name,url,pdfexpected=False):
    start=time.monotonic()
    try:
        for attempt in range(2):
            assert urllib.parse.urlsplit(url).hostname=='web.archive.org'
            with urllib.request.build_opener(ArchiveOnly()).open(url,timeout=40) as response:
                data=response.read();final=response.url;typ=response.headers.get('Content-Type');status=response.status
            pdf=data.startswith(b'%PDF-');suffix='pdf' if pdf else 'html'
            p=r/f'sources/category_bourbaki_congress_{name}_{attempt}.{suffix}';p.write_bytes(data)
            print(json.dumps({'url':url,'final_url':final,'status':status,'type':typ,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'saved':str(p),'seconds':time.monotonic()-start}),flush=True)
            if pdf:
                for cmd in [['pdfinfo',str(p)],['pdftotext','-layout',str(p),str(r/f'notes/category_bourbaki_congress_{name}_native.txt')]]:
                    proc=subprocess.run(cmd,capture_output=True,timeout=40)
                    print(json.dumps({'command':cmd,'status':proc.returncode,'stdout':proc.stdout.decode(errors='replace'),'stderr':proc.stderr.decode(errors='replace')}),flush=True)
                return
            parser=Links();parser.feed(data.decode(errors='replace'))
            if not pdfexpected:
                pdfs=list(dict.fromkeys(urllib.parse.urljoin(final,u) for u in parser.urls if '/files/original/' in u and '.pdf' in u))
                print(json.dumps({'record':name,'advertised_pdfs':pdfs}),flush=True)
                for index,link in enumerate(pdfs):fetch(name+f'_pdf{index}',link,True)
                return
            if not parser.playback:return
            url=urllib.parse.urljoin(final,parser.playback)
    except Exception as e:print(json.dumps({'url':url,'error_type':type(e).__name__,'error':str(e),'seconds':time.monotonic()-start}),flush=True)
h=Links();h.feed((r/'sources/category_bourbaki_r230_item664_0.html').read_text())
with ThreadPoolExecutor(max_workers=2) as pool:
    futures=[]
    for number in [802,805]:
        link=next(u for u in h.urls if u.endswith(f'/items/show/{number}'))
        futures.append(pool.submit(fetch,str(number),urllib.parse.urljoin('http://web.archive.org',link)))
    for future in futures:future.result()
