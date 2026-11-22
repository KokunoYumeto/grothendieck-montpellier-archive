"""Bounded ordinary public BASE landing-page inspection; stop on denial.

This script never switches endpoints, solves a challenge, or invents a search
API. Any later search must be based on an actually observed public form.
"""
import datetime
import hashlib
import html.parser
import json
import pathlib
import time
import urllib.error
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
url = 'https://www.base-search.net/'
entry = {'requested_url':url,
         'purpose':'Inspect the public BASE catalogue landing page and actual search forms',
         'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
start=time.monotonic()
try:
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (public scholarly catalogue audit)'}),timeout=40) as r:
        body=r.read()
        entry.update({'http_status':r.status,'final_url':r.url,'content_type':r.headers.get('Content-Type'),
                      'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest()})
        text=body.decode('utf-8','replace')
        path=root/'literature/B_BASE_public_landing.html'
        path.write_text(text)
        entry['saved_response']=str(path.relative_to(root))
        class Parser(html.parser.HTMLParser):
            def __init__(self):super().__init__();self.forms=[];self.active=None;self.visible=[]
            def handle_starttag(self,tag,attrs):
                a=dict(attrs)
                if tag=='form':self.active={'attributes':a,'controls':[]};self.forms.append(self.active)
                elif tag in ('input','select','button') and self.active is not None:self.active['controls'].append({'tag':tag,**a})
            def handle_endtag(self,tag):
                if tag=='form':self.active=None
            def handle_data(self,data):
                if data.strip():self.visible.append(data.strip())
        p=Parser();p.feed(text)
        entry['observed_forms']=p.forms
        entry['visible_text_excerpt']=' '.join(p.visible)[:12000]
        if 'Making sure you\'re not a bot!' in text or 'anubis_challenge' in text or 'anubis-main' in text:
            entry['classification']='anti-bot challenge, not catalogue content'
            entry['stopped_on_challenge']=True
            entry['catalogue_query_submitted']=False
except urllib.error.HTTPError as e:
    body=e.read()
    entry.update({'http_status':e.code,'final_url':e.url,'content_type':e.headers.get('Content-Type'),
                  'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),
                  'response_excerpt':body.decode('utf-8','replace')[:2000],
                  'stopped_on_denial':True})
except Exception as e:entry['error']=repr(e)
entry.update({'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'elapsed_seconds':time.monotonic()-start})
(root/'logs/B_BASE_public_catalogue.json').write_text(json.dumps(entry,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(entry,ensure_ascii=False))
