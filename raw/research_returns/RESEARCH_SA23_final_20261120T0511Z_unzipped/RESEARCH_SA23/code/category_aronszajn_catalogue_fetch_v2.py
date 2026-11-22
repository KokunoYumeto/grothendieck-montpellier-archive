"""Standard-library version; v1 dependency failure is retained separately."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from html.parser import HTMLParser
import hashlib, json, urllib.request

ROOT = Path(__file__).resolve().parents[1]
pages = {
 'resource11':'https://archives.lib.ku.edu/repositories/3/resources/11',
 'publications43':'https://archives.lib.ku.edu/repositories/3/archival_objects/43',
 'notes44':'https://archives.lib.ku.edu/repositories/3/archival_objects/44',
 'homepage':'https://archives.lib.ku.edu/'}
class Inspector(HTMLParser):
    def __init__(self):
        super().__init__(); self.elements=[]; self.text=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag in ['a','form','input','select','option','script'] or any(k.startswith('data-') for k in attrs):
            self.elements.append({'tag':tag,'attrs':attrs})
    def handle_data(self, data):
        if data.strip():self.text.append(data.strip())
def get(job):
    name,url=job; row={'name':name,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
    class PublicRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,req,fp,code,msg,headers,newurl):
            if urlparse(newurl).hostname!='archives.lib.ku.edu':raise ValueError('Unexpected redirect host')
            return super().redirect_request(req,fp,code,msg,headers,newurl)
    try:
        with urllib.request.build_opener(PublicRedirect).open(url,timeout=35) as r:
            data=r.read();row.update(status=r.status,final_url=r.url)
        path=ROOT/'sources'/f'category_aronszajn_{name}.html';path.write_bytes(data)
        row.update(path=str(path.relative_to(ROOT)),sha256=hashlib.sha256(data).hexdigest())
        parser=Inspector();parser.feed(data.decode(errors='replace'))
        row['advertised_elements']=parser.elements
        path.with_suffix('.txt').write_text('\n'.join(parser.text)+'\n')
    except Exception as error:row['error']=repr(error)
    return row
rows=[]
with ThreadPoolExecutor(max_workers=4) as pool:
    for future in as_completed([pool.submit(get,job) for job in pages.items()]):
        row=future.result();rows.append(row)
        print(json.dumps(row,ensure_ascii=False),flush=True)
        (ROOT/'logs/category_aronszajn_catalogue_fetch_v2.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
