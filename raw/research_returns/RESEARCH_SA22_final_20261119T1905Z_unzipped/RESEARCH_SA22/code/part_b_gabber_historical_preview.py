#!/usr/bin/env python3
"""Inspect an actual public historical landing for advertised first-page links.

The current article URL has already been opened. We query its exact public CDX
record, then follow at most one returned HTML capture. No file endpoint is
guessed and no subscription PDF is requested.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode, urljoin
from html.parser import HTMLParser
import gzip, json, re, time

root = Path(__file__).resolve().parents[1]
started = time.monotonic()
results = []

def fetch(url, purpose):
    start = time.monotonic(); record = {'url':url,'purpose':purpose}; data = None
    try:
        with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:
            data=response.read(2*1024*1024+1)
            record.update(http_status=response.status,final_url=response.url,
                          bytes=len(data),content_type=response.headers.get('Content-Type',''))
        if data[:2]==b'\x1f\x8b': data=gzip.decompress(data)
        if len(data)>2*1024*1024:
            record['status']='Response cap reached; not inspected';data=None
        else: record['status']='Public response read'
    except Exception as error:
        record.update(status='Request failed; no retry or bypass',error=str(error))
    record['elapsed_seconds']=time.monotonic()-start;results.append(record)
    return record,data

params=[('url','https://link.springer.com/article/10.1007/BF02773001'),
        ('matchType','exact'),('output','json'),('filter','statuscode:200'),
        ('filter','mimetype:text/html'),('collapse','digest'),('limit','3'),
        ('fl','timestamp,original,statuscode,mimetype')]
metadata,raw=fetch('https://web.archive.org/cdx/search/cdx?'+urlencode(params),
                   'Exact article landing metadata; at most three distinct historical HTML captures')
if raw is not None:
    try: rows=json.loads(raw);metadata['response']=rows
    except Exception as error: rows=[];metadata['parse_error']=str(error)
    if len(rows)>1:
        values=dict(zip(rows[0],rows[1]))
        url='https://web.archive.org/web/'+values['timestamp']+'id_/'+values['original']
        landing,raw=fetch(url,'Read the first actual returned public HTML capture')
        if raw is not None:
            text=raw.decode('utf8','replace')
            (root/'sources/part_b_gabber_historical_preview_landing.html').write_text(text)
            class Page(HTMLParser):
                def __init__(self):super().__init__();self.links=[];self.text=[]
                def handle_starttag(self,tag,attrs):
                    for key,value in attrs:
                        if value and key in ['href','src','data-src'] and re.search(r'preview|page.one|lookinside|look.inside',value,re.I):
                            self.links.append({'tag':tag,'attribute':key,'url':urljoin(landing['final_url'],value)})
                def handle_data(self,data):
                    if data.strip():self.text.append(data.strip())
            page=Page();page.feed(text)
            (root/'sources/part_b_gabber_historical_preview_landing.txt').write_text('\n'.join(page.text)+'\n')
            landing['actually_advertised_preview_candidates']=page.links
            landing['preview_context']=[text[max(0,m.start()-120):m.end()+200] for m in list(re.finditer(r'preview|page.one|lookinside|look.inside',text,re.I))[:20]]
            landing['status']='Historical landing read; candidate links require separate inspection; no original content fetched'

output={'results':results,'elapsed_seconds':time.monotonic()-started}
(root/'code/part_b_gabber_historical_preview_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
