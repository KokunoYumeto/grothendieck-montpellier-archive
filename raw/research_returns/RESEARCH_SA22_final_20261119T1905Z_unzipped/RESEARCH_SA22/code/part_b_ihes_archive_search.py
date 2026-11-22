#!/usr/bin/env python3
"""Search the advertised public IHES historical-preprint collection.

Read the actual search form, then use its observed keyword and collection
controls. No hidden endpoint, restricted file or alternate credential is used.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode,urljoin
from html.parser import HTMLParser
import argparse,json,time

root=Path(__file__).resolve().parents[1];start=time.monotonic();records=[]
form_url='https://archives.ihes.fr/items/search'
class Page(HTMLParser):
    def __init__(self):super().__init__();self.forms=[];self.current=None;self.links=[];self.text=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='form':self.current={'action':a.get('action',''),'method':a.get('method','get'),'controls':[]};self.forms.append(self.current)
        if tag in ['input','select'] and self.current is not None:self.current['controls'].append(a)
        if tag=='a' and a.get('href'):self.links.append(a['href'])
    def handle_endtag(self,tag):
        if tag=='form':self.current=None
    def handle_data(self,data):
        if data.strip():self.text.append(data.strip())
def fetch(name,url):
    began=time.monotonic();r={'name':name,'url':url}
    try:
        with urlopen(url,timeout=25) as response:
            raw=response.read();r['http_status']=response.status;r['final_url']=response.url
        r['bytes']=len(raw);r['status']='public HTML read'
        text=raw.decode('utf-8','replace');parser=Page();parser.feed(text)
        (root/'sources'/('ihes_archive_'+name+'.html')).write_text(text)
        (root/'sources'/('ihes_archive_'+name+'.txt')).write_text('\n'.join(parser.text)+'\n')
        r['forms']=parser.forms;r['advertised_links']=list(dict.fromkeys(urljoin(url,x) for x in parser.links))
        r['text']='\n'.join(parser.text)
    except Exception as exc:r['status']='error';r['error']=str(exc)
    r['elapsed_seconds']=time.monotonic()-began;records.append(r)
    return r

parser=argparse.ArgumentParser();parser.add_argument('--global-search',action='store_true');parser.add_argument('--year-search',action='store_true');args=parser.parse_args()
if args.year_search:
    # New bibliographic evidence explicitly dates the affine preprint to1981.
    # Reuse the already opened ordinary collection search form.
    previous=json.loads((root/'code/part_b_ihes_archive_search_output.json').read_text())
    form=next(r for r in previous['results'] if r['name']=='form')
    selected=[f for f in form['forms'] if {'search','collection'} <= {a.get('name') for a in f['controls']}]
    assert len(selected)==1 and selected[0]['method'].lower()=='get'
    action=urljoin(form_url,selected[0]['action'])
    fetch('1981',action+'?'+urlencode({'search':'1981','collection':'59'}))
elif args.global_search:
    # Reuse the actual saved form, rather than make another request for it.
    previous=json.loads((root/'code/part_b_ihes_archive_search_output.json').read_text())
    form=next(r for r in previous['results'] if r['name']=='form')
    selected=[f for f in form['forms'] if {'query','query_type','record_types[]'} <= {a.get('name') for a in f['controls']}]
    assert len(selected)==1 and selected[0]['method'].lower()=='get'
    action=urljoin(form_url,selected[0]['action'])
    for name,query in [('global_affine_analog','Affine analog'),('global_changement_base','changement de base')]:
        params=[('query',query),('query_type','exact_match'),('record_types[]','Item'),('record_types[]','File')]
        fetch(name,action+'?'+urlencode(params))
else:
    form=fetch('form',form_url)
if not args.global_search and not args.year_search and form['status']=='public HTML read':
    selected=[f for f in form['forms'] if {'search','collection'} <= {a.get('name') for a in f['controls']}]
    if len(selected)==1:
        selected=selected[0]
        assert selected['method'].lower()=='get',selected
        action=urljoin(form_url,selected['action'])
        for name,query in [('gabber','Gabber'),('affine','Affine')]:
            fetch(name,action+'?'+urlencode({'search':query,'collection':'59'}))
    else:form['search_not_executed_reason']='No unique observed GET form with search and collection controls; inspect form before proceeding.'

out={'results':records,'elapsed_seconds':time.monotonic()-start}
filename='part_b_ihes_archive_1981_output.json' if args.year_search else 'part_b_ihes_archive_global_output.json' if args.global_search else 'part_b_ihes_archive_search_output.json'
(root/'code'/filename).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'results':[{k:v for k,v in r.items() if k not in ['text','advertised_links','forms']} for r in records]},indent=2))
