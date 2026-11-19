#!/usr/bin/env python3
"""Read one publicly advertised CERN catalogue record, without guessing file paths."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
import json,time

root=Path(__file__).resolve().parents[1]
url='https://cds.cern.ch/record/1690769'
started=time.monotonic()
result={'url':url,'purpose':'Public catalogue lead advertised by OpenAlex for Raynaud LNM119'}
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a' and a.get('href'):self.links.append(urljoin(url,a['href']))
try:
    with urlopen(url,timeout=25) as response:
        raw=response.read();result['http_status']=response.status
        result['content_type']=response.headers.get('Content-Type','')
        result['final_url']=response.url
    result['bytes']=len(raw)
    text=raw.decode('utf-8','replace')
    (root/'sources/raynaud_cern_catalogue.html').write_text(text)
    parser=Links();parser.feed(text)
    result['advertised_links']=list(dict.fromkeys(parser.links))
    result['status']='public response read; content must be inspected before treating as catalogue'
    if 'anubis' in text.lower() and 'challenge' in text.lower():
        result['observed_content']='Anubis automated-access challenge, not the catalogue record; no challenge execution or bypass attempted'
except Exception as exc:
    result['status']='error';result['error']=str(exc)
result['elapsed_seconds']=time.monotonic()-started
(root/'code/part_b_cern_record_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
