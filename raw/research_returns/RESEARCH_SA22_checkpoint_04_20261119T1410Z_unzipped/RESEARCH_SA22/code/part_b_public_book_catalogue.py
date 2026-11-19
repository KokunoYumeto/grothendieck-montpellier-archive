#!/usr/bin/env python3
"""Read one publicly advertised author catalogue, without downloading a book.

The /g/ search route was observed on the public site by the companion audit.
This preserves the actual response and visible links. It does not use account
credentials, alternate headers, a challenge solver, or restricted endpoints.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
import json,time

root=Path(__file__).resolve().parents[1]
url='https://libcats.org/g/Raynaud'
started=time.monotonic()
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.text=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href'):self.links.append(urljoin(url,a['href']))
    def handle_data(self,data):
        if data.strip():self.text.append(data.strip())
record={'url':url,'scope':'Public catalogue HTML only; no original book requested'}
try:
    with urlopen(url,timeout=55) as response:
        raw=response.read();record.update(http_status=response.status,final_url=response.url,bytes=len(raw))
    page=raw.decode('utf-8','replace');parser=Page();parser.feed(page)
    (root/'sources/part_b_raynaud_public_catalogue.html').write_text(page)
    (root/'sources/part_b_raynaud_public_catalogue.txt').write_text('\n'.join(parser.text)+'\n')
    record.update(status='Public HTML read',advertised_links=list(dict.fromkeys(parser.links)),text='\n'.join(parser.text))
except Exception as exc:record.update(status='error',error=str(exc))
record['elapsed_seconds']=time.monotonic()-started
out={'results':[record],'elapsed_seconds':record['elapsed_seconds']}
(root/'code/part_b_public_book_catalogue_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ['text','advertised_links']},indent=2))
