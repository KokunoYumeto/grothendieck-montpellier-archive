from pathlib import Path
import urllib.request, urllib.error, urllib.parse
from html.parser import HTMLParser
import concurrent.futures, datetime, time, hashlib, json

base = Path('/workspace/scratch/9c53b536a97f/RESEARCH_SA22')
targets = [('mit_general','https://search.libraries.mit.edu/'),
           ('princeton_general','https://catalog.princeton.edu/')]
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.forms=[]; self.current=None
    def handle_starttag(self,tag,attrs):
        attr=dict(attrs)
        if tag=='a' and attr.get('href'): self.links.append(attr['href'])
        if tag=='form':
            self.current={'form':attr,'controls':[]};self.forms.append(self.current)
        if tag in ['input','button','select'] and self.current is not None:
            self.current['controls'].append({'tag':tag,**attr})
    def handle_endtag(self,tag):
        if tag=='form': self.current=None
def fetch(target):
    label,url=target;t=time.perf_counter();record={'label':label,'url':url}
    try:
        with urllib.request.urlopen(url,timeout=35) as r:
            data=r.read();record.update(http_status=r.status,final_url=r.url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        path=base/f'sources/part_c_lieberman_{label}.html';path.write_bytes(data)
        text=data.decode('utf-8',errors='replace');p=Links();p.feed(text)
        record.update(saved=str(path),forms=p.forms,links=p.links)
    except Exception as e:record.update(error=repr(e))
    record['elapsed_seconds']=time.perf_counter()-t
    return record
started=datetime.datetime.now(datetime.timezone.utc).isoformat();t0=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results=list(pool.map(fetch,targets))
report={'started_utc':started,'elapsed_seconds':time.perf_counter()-t0,'scope':'Two ordinary public catalogue homepages; inspect advertised search forms, no login or source downloads.','results':results}
payload=json.dumps(report,indent=2)
(base/'code/part_c_lieberman_catalogue_output.json').write_text(payload+'\n')
(base/'code/part_c_lieberman_catalogue_output.txt').write_text(payload+'\n')
print(payload)
