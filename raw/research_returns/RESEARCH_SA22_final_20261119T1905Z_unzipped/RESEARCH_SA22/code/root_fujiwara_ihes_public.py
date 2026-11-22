"""Two distinct Fujiwara/tubular queries through the observed IHES public form."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
from urllib.parse import urlencode, urljoin
from urllib.request import urlopen

R=Path(__file__).resolve().parents[1]
target=R/'code/root_fujiwara_ihes_public_output.json'
assert not target.exists()
began=time.monotonic()
started=datetime.now(timezone.utc).isoformat()
previous=json.loads((R/'code/part_b_ihes_archive_search_output.json').read_text())
form=next(r for r in previous['results'] if r['name']=='form')
forms=[f for f in form['forms'] if {'query','query_type','record_types[]'} <= {a.get('name') for a in f['controls']}]
assert len(forms)==1 and forms[0]['method'].lower()=='get'
action=urljoin('https://archives.ihes.fr/items/search',forms[0]['action'])

class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.hidden=0;self.parts=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.hidden+=1
        a=dict(attrs)
        if tag=='a' and a.get('href'):self.links.append(a['href'])
    def handle_endtag(self,tag):
        if tag in ('script','style') and self.hidden:self.hidden-=1
    def handle_data(self,data):
        if not self.hidden and data.strip():self.parts.append(data.strip())

def fetch(item):
    slug,query=item
    params=[('query',query),('query_type','exact_match'),('record_types[]','Item'),('record_types[]','File')]
    url=action+'?'+urlencode(params)
    before=time.monotonic();rec={'slug':slug,'query':query,'url':url}
    try:
        with urlopen(url,timeout=25) as response:
            raw=response.read()
            rec.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('content-type'))
        page=Page();html=raw.decode('utf-8','replace');page.feed(html)
        body='\n'.join(page.parts)
        hp=R/'sources'/f'root_fujiwara_ihes_{slug}.html'
        tp=hp.with_suffix('.txt')
        hp.write_text(html);tp.write_text(body+'\n')
        links=list(dict.fromkeys(urljoin(url,h) for h in page.links))
        rec.update(bytes=len(raw),sha256=sha256(raw).hexdigest(),
          displayed_result_counts=list(dict.fromkeys(re.findall(r'Recherche\s*\((\d+)\s+total\)',body))),
          advertised_record_links=[h for h in links if '/document/' in h or '/items/show/' in h],
          raw_html_cache=str(hp.relative_to(R)),text_cache=str(tp.relative_to(R)),
          semantic_status='Successful catalogue read; inspect actual result identities before any original-source claim.')
    except Exception as exc:
        rec.update(error=repr(exc),semantic_status='Request failed; not a zero-result finding. No retry.')
    rec['elapsed_seconds']=time.monotonic()-before
    return rec

queries=[('author','Fujiwara'),('title','tubular')]
with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(fetch,queries))
out={'started_utc':started,'scope':'Two public Item/File catalogue queries using the previously observed normal GET form. No credentials, hidden endpoint, article-file request or retry.',
     'request_count':2,'results':results,'elapsed_seconds':time.monotonic()-began}
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
