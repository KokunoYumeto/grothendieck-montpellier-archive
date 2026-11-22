"""Inspect the ordinary public SciSpace landing page for advertised PDF links."""
import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
url='https://scispace.com/papers/quasiconformal-mappings-in-the-plane-4hgdgoprrd'
begin=time.perf_counter()
result={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'scope':'One ordinary public HTML request only; no service APIs, login, or PDF endpoints.'}
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for key in ('href','src'):
            if key in a and any(s in a[key].lower() for s in ('pdf','4hgdgoprrd','65513')):
                self.links.append({'tag':tag,'attribute':key,'url':a[key]})
try:
    request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'})
    with urllib.request.urlopen(request,timeout=30) as response:
        data=response.read()
        result.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    path=ROOT/'sources'/'part_c_lehto_scispace_public.html'
    path.write_bytes(data)
    result['saved']=str(path.relative_to(ROOT))
    content=data.decode('utf-8','replace')
    parser=Links()
    parser.feed(content)
    result['advertised_links']=parser.links
    result['pdf_field_contexts']=[content[max(0,m.start()-100):m.end()+200] for m in re.finditer(r'pdf_url|pdfUrl|pdf_link|pdfLink',content)]
except Exception as error:
    result['error']=repr(error)
result['elapsed_seconds']=time.perf_counter()-begin
text=json.dumps(result,indent=2)
(ROOT/'code'/'part_c_lehto_public_page_output.json').write_text(text+'\n')
print(text)
