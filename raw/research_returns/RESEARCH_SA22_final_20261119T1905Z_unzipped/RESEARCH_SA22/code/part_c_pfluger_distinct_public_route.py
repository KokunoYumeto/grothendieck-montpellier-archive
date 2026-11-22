#!/usr/bin/env python3
"""Read explicitly observed public catalogue pages; no authentication or retries."""
import argparse, datetime, hashlib, json, pathlib, time, urllib.error, urllib.request
from html.parser import HTMLParser

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.text=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href'): self.links.append(a['href'])
    def handle_data(self, data):
        if data.strip(): self.text.append(data.strip())

p=argparse.ArgumentParser(); p.add_argument('name'); p.add_argument('url'); a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
start=time.perf_counter(); out={'name':a.name,'url':a.url,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'One ordinary public catalogue request; no retry, login, challenge workaround or content-file guessing.'}
try:
    with urllib.request.urlopen(a.url,timeout=45) as r:
        b=r.read(); out.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
    dest=root/'sources'/('part_c_pfluger_distinct_'+a.name+'.html'); dest.write_bytes(b)
    parser=Links(); parser.feed(b.decode('utf-8','replace'))
    out.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),saved=str(dest.relative_to(root)),links=parser.links,text='\n'.join(parser.text))
except urllib.error.HTTPError as e:
    b=e.read(); out.update(status=e.code,final_url=e.url,error=str(e),bytes=len(b),body=b.decode('utf-8','replace')[:4000])
except Exception as e: out.update(error=type(e).__name__+': '+str(e))
out['elapsed_seconds']=time.perf_counter()-start
path=root/'code'/('part_c_pfluger_distinct_'+a.name+'_output.json'); path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
