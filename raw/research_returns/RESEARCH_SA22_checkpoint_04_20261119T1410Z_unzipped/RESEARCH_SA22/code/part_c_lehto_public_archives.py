"""Bounded public catalogue checks; never requests private book files."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    ('ia_old_identifier_metadata', 'https://archive.org/metadata/quasiconformalma00leht'),
    ('author_publication_list', 'https://www.acadsci.fi/mathematica/Vol10/vol10pp00V-0XI.pdf'),
]
for label, pattern in [
    ('cdx_current_pdf', 'link.springer.com/content/pdf/10.1007/978-3-642-65513-5.pdf'),
    ('cdx_encoded_pdf', 'link.springer.com/content/pdf/10.1007%2F978-3-642-65513-5.pdf'),
    ('cdx_springerlink_isbn', 'www.springerlink.com/content/978-3-642-65513-5/*'),
    ('cdx_link_book', 'link.springer.com/*978-3-642-65513-5*'),
    ('cdx_static_publisher', 'static-content.springer-cdn.com/*978-3-642-65513-5*'),
]:
    query = urllib.parse.urlencode({'url':pattern,'output':'json','filter':'statuscode:200','collapse':'urlkey','fl':'timestamp,original,mimetype,statuscode','limit':'100'})
    TARGETS.append((label,'https://web.archive.org/cdx/search/cdx?'+query))

def request_one(item):
    label,url=item
    begin=time.perf_counter()
    row={'label':label,'url':url}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'})
        with urllib.request.urlopen(request,timeout=35) as response:
            data=response.read()
            row.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        suffix='.pdf' if data.startswith(b'%PDF') else '.json'
        path=ROOT/'sources'/('part_c_lehto_'+label+suffix)
        path.write_bytes(data)
        row['saved']=str(path.relative_to(ROOT))
        if suffix=='.json':
            try:
                parsed=json.loads(data)
                if label=='ia_old_identifier_metadata':
                    metadata=parsed.get('metadata',{})
                    row['title']=metadata.get('title')
                    row['access_restricted_item']=metadata.get('access-restricted-item')
                    row['is_dark']=parsed.get('is_dark')
                    row['files']=[{'name':f.get('name'),'format':f.get('format'),'private':f.get('private')} for f in parsed.get('files',[]) if f.get('format') in ['Text PDF','PDF','DjVuTXT','EPUB']]
                else:
                    row['catalogue_result']=parsed
            except Exception:
                row['text_prefix']=data[:1000].decode('utf-8','replace')
    except Exception as error:
        row['error']=repr(error)
    row['elapsed_seconds']=time.perf_counter()-begin
    return row

begin=time.perf_counter()
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as pool:
    rows=list(pool.map(request_one,TARGETS))
result={'started_utc':started,'elapsed_seconds':time.perf_counter()-begin,'scope':'Seven ordinary public catalogue or bibliographic requests; no full book PDF and no private file request.','results':rows}
text=json.dumps(result,indent=2)
(ROOT/'code'/'part_c_lehto_public_archives_output.json').write_text(text+'\n')
print(text)
