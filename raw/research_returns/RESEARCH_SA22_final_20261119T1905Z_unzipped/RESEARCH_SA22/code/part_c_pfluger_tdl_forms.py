"""Inspect the ordinary public TDL catalogue form supplied by the parent.
No submission, account operation, private endpoint, or content request.
"""
import datetime
import hashlib
import html.parser
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

class Forms(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms=[]; self.current=None; self.scripts=[]; self.links=[]
    def handle_starttag(self, tag, attrs):
        at=dict(attrs)
        if tag=='form':
            self.current={'attributes':at, 'controls':[]}; self.forms.append(self.current)
        if tag in ('input','select','button','textarea') and self.current is not None:
            self.current['controls'].append({'tag':tag, 'attributes':at})
        if tag=='script' and at.get('src'):
            self.scripts.append(at['src'])
        if tag=='a' and at.get('href'):
            self.links.append(at['href'])
    def handle_endtag(self, tag):
        if tag=='form': self.current=None

root=pathlib.Path(__file__).resolve().parents[1]
url='https://tamildigitallibrary.in/index-search'
payload={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'requests':1, 'url':url, 'web_ref':'turn497349532view0'}
tick=time.monotonic()
try:
    with urllib.request.urlopen(url,timeout=35) as response:
        body=response.read(); text=body.decode('utf-8','replace')
        dest=root/'sources/part_c_pfluger_tdl_index_search.html'; dest.write_bytes(body)
        parser=Forms(); parser.feed(text)
        payload.update(status=response.status, final_url=response.url, bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), saved_html=str(dest), forms=parser.forms, scripts=parser.scripts, links=parser.links)
except Exception as error:
    payload['error']=type(error).__name__+': '+str(error)
    if isinstance(error,urllib.error.HTTPError): payload['status']=error.code
payload['elapsed_seconds']=time.monotonic()-tick
out=root/'code/part_c_pfluger_tdl_forms_output.json'; out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
out.with_suffix('.txt').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(payload,ensure_ascii=False,indent=2))
