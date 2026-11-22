"""Read actual advertised pagination links for the public Mathematical search.
Starts from the already fetched first page; discovers every next URL from
anchors actually returned. At most two simultaneous ordinary metadata GETs.
Stops scheduling on an access denial. No book file or guessed ID is fetched.
"""
import concurrent.futures
import datetime
import hashlib
import html.parser
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

root=pathlib.Path(__file__).resolve().parents[1]
base='https://tamildigitallibrary.in/search/Mathematical'
class Links(html.parser.HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.current=None
    def handle_starttag(self,tag,attrs):
        at=dict(attrs)
        if tag=='a':self.current={'url':at.get('href',''),'text':''}
    def handle_data(self,data):
        if self.current is not None:self.current['text']+=data
    def handle_endtag(self,tag):
        if tag=='a' and self.current is not None:self.links.append(self.current);self.current=None
def parse(text):
    parser=Links();parser.feed(text);return parser.links
def fetch(url):
    tick=time.monotonic();item={'url':url,'method':'GET'};text=''
    try:
        with urllib.request.urlopen(url,timeout=35) as response:
            body=response.read();text=body.decode('utf-8','replace')
            page=urllib.parse.parse_qs(urllib.parse.urlsplit(url).query).get('page',['1'])[0]
            dest=root/'sources'/('part_c_pfluger_tdl_page_'+page+'.html');dest.write_bytes(body)
            item.update(status=response.status,final_url=response.url,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),saved_path=str(dest))
    except Exception as error:
        item['error']=type(error).__name__+': '+str(error)
        if isinstance(error,urllib.error.HTTPError):item['status']=error.code
    item['seconds']=time.monotonic()-tick;return item,parse(text)

started=datetime.datetime.now(datetime.timezone.utc).isoformat();clock=time.monotonic()
seen={base,base+'?page=1'};queued=[];records={};results=[];denied=False
def consume(links):
    for item in links:
        url=item['url']
        if url.startswith(base+'?page=') and url not in seen and url not in queued:
            queued.append(url)
        if url.startswith('https://tamildigitallibrary.in/Articles/'):
            records[url]={'url':url,'decoded_url':urllib.parse.unquote(url),'title':item['text'].strip()}
consume(parse((root/'sources/part_c_pfluger_tdl_mathematical.html').read_text()))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    pending={}
    while queued or pending:
        while queued and len(pending)<2 and not denied and len(seen)<25:
            url=queued.pop(0);seen.add(url);pending[pool.submit(fetch,url)]=url
        if not pending:break
        done,_=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
        for future in done:
            pending.pop(future);item,links=future.result();results.append(item);consume(links)
            print(json.dumps({'page':item['url'],'status':item.get('status'),'seconds':item['seconds'],'article_records_so_far':len(records)}),flush=True)
            if item.get('status') in (401,403,429):denied=True
        if denied:queued=[]
payload={'started_utc':started,'elapsed_seconds':time.monotonic()-clock,'requests':len(results),'cached_first_page':'sources/part_c_pfluger_tdl_mathematical.html','stopped_on_access_denial':denied,'results':results,'records':list(records.values()),'remaining_advertised_pages':queued}
out=root/'code/part_c_pfluger_tdl_inventory_output.json';out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');out.with_suffix('.txt').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
jims=[r for r in records.values() if 'mathematical society' in r['decoded_url'].lower()]
recent=[r for r in jims if re.search(r'19[6-9][0-9]|Golden|Jubilee',r['decoded_url'],re.I)]
print(json.dumps({'completed_requests':len(results),'elapsed_seconds':payload['elapsed_seconds'],'records':len(records),'jims_records':len(jims),'possible_post_1959_or_jubilee':recent},ensure_ascii=False,indent=2))
