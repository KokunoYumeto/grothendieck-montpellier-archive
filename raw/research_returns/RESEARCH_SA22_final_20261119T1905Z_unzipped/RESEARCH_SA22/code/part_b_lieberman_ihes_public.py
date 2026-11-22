#!/usr/bin/env python3
"""Two new Lieberman queries through the previously inspected public IHES form.

No hidden endpoint, credential, challenge, retry, or content-file request.
The exact form evidence is retained in part_b_ihes_archive_search_output.json.
"""
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

root = Path(__file__).resolve().parents[1]
began = time.monotonic()
started_utc = datetime.now(timezone.utc).isoformat()
previous = json.loads((root/'code/part_b_ihes_archive_search_output.json').read_text())
form = next(r for r in previous['results'] if r['name'] == 'form')
forms = [f for f in form['forms'] if {'query','query_type','record_types[]'} <= {a.get('name') for a in f['controls']}]
assert len(forms) == 1 and forms[0]['method'].lower() == 'get'
action = urljoin('https://archives.ihes.fr/items/search', forms[0]['action'])

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.hidden=0; self.parts=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.hidden += 1
        a=dict(attrs)
        if tag=='a' and a.get('href'): self.links.append(a['href'])
    def handle_endtag(self,tag):
        if tag in ('script','style') and self.hidden: self.hidden -= 1
    def handle_data(self,data):
        if not self.hidden and data.strip(): self.parts.append(data.strip())

def fetch(item):
    slug, query = item
    params=[('query',query),('query_type','exact_match'),('record_types[]','Item'),('record_types[]','File')]
    url=action+'?'+urlencode(params)
    start=time.monotonic()
    record={'slug':slug,'query':query,'url':url}
    try:
        with urlopen(url,timeout=25) as response:
            raw=response.read()
            record.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('content-type'))
        record.update(bytes=len(raw),sha256=sha256(raw).hexdigest())
        html=raw.decode('utf-8','replace')
        parser=Page(); parser.feed(html)
        body='\n'.join(parser.parts)
        record.update(text=body,advertised_links=list(dict.fromkeys(urljoin(url,h) for h in parser.links)))
        counts=re.findall(r'Recherche\s*\((\d+)\s+total\)',body)
        record['displayed_result_counts']=list(dict.fromkeys(counts))
        record['semantic_status']='public search HTML; inspect text before judging results'
        (root/'sources'/f'part_b_lieberman_ihes_{slug}.html').write_text(html)
        (root/'sources'/f'part_b_lieberman_ihes_{slug}.txt').write_text(body+'\n')
    except Exception as exc:
        record.update(semantic_status='request failed; not an absence result',error=repr(exc))
    record['elapsed_seconds']=time.monotonic()-start
    return record

queries=[('author','Lieberman'),('title','Numerical and Homological')]
with ThreadPoolExecutor(max_workers=2) as pool:
    results=list(pool.map(fetch,queries))
out={'started_utc':started_utc,'elapsed_seconds':time.monotonic()-began,
     'scope':'Two new public IHES Item/File catalogue queries; no mathematical content requested',
     'request_count':len(queries),'results':results}
(root/'code/part_b_lieberman_ihes_public_output.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(out,indent=2,ensure_ascii=False))
