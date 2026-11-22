from pathlib import Path
from html.parser import HTMLParser
import urllib.request, urllib.parse, hashlib, json, time
from concurrent.futures import ThreadPoolExecutor

ROOT = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.playback=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='a' and 'href' in a: self.links.append(a['href'])
        if tag=='iframe' and a.get('id')=='playback': self.playback=a.get('src')

def retrieve(name, original, expect_pdf=False):
    url='https://archive.org/wayback/available?'+urllib.parse.urlencode({'url':original})
    start=time.monotonic()
    try:
        with urllib.request.urlopen(url,timeout=35) as r: data=r.read()
        (ROOT/f'notes/category_bourbaki_{name}_available.json').write_bytes(data)
        j=json.loads(data); snap=j['archived_snapshots']['closest']['url']
        for attempt in range(2):
            with urllib.request.urlopen(snap,timeout=40) as r:
                data=r.read(); final=r.url; typ=r.headers.get('Content-Type'); status=r.status
            pdf=data.startswith(b'%PDF-')
            suffix='pdf' if pdf else 'html'
            p=ROOT/f'sources/category_bourbaki_{name}_{attempt}.{suffix}';p.write_bytes(data)
            print(json.dumps({'name':name,'url':snap,'final_url':final,'status':status,'type':typ,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'saved':str(p),'seconds':time.monotonic()-start}),flush=True)
            if pdf or not expect_pdf: break
            h=Links();h.feed(data.decode('utf-8',errors='replace'))
            if not h.playback: break
            snap=urllib.parse.urljoin(final,h.playback)
    except Exception as e:
        print(json.dumps({'name':name,'url':url,'error_type':type(e).__name__,'error':str(e),'seconds':time.monotonic()-start}),flush=True)

h=Links();h.feed((ROOT/'sources/category_bourbaki_evt_catalogue.html').read_text())
pdf187=next(x for x in h.links if '/187_' in x and x.endswith('.pdf'))
base='http://sites.mathdoc.fr/archives-bourbaki/'
home=Links();home.feed((ROOT/'sources/category_bourbaki_archived_catalogue.html').read_text())
allhref=next(x for x in home.links if x=='feuilleter.php?chap=2')
with ThreadPoolExecutor(max_workers=2) as pool:
    futures=[pool.submit(retrieve,'r187',urllib.parse.urljoin(base,pdf187),True),pool.submit(retrieve,'all_redactions',urllib.parse.urljoin(base,allhref),False)]
    for f in futures: f.result()
