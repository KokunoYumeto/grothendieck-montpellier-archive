"""Retrieve only independently public collection/finding-aid pages for Memoir16 route."""
import concurrent.futures, datetime, hashlib, json, pathlib, re, time, urllib.request
from html.parser import HTMLParser
base = pathlib.Path(__file__).resolve().parents[1]
class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts=[]; self.links=[]; self.current=None
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            self.current={'href':dict(attrs).get('href'), 'label':''}
    def handle_data(self, data):
        if data.strip(): self.parts.append(data.strip())
        if self.current is not None: self.current['label'] += data
    def handle_endtag(self, tag):
        if tag=='a' and self.current is not None:
            self.links.append(self.current); self.current=None
targets=[
 ('chicago_findingaids','https://www.lib.uchicago.edu/e/scrc/findingaids/'),
 ('chicago_select','https://www.lib.uchicago.edu/e/spcl/select.html'),
 ('brown_ams_collection','https://library.brown.edu/collatoz/info.php?id=675'),
 ('texas_maclane_findingaid','https://txarchives.org/utcah/finding_aids/00353.xml'),
]
def retrieve(target):
    name,url=target
    start=time.monotonic(); rec={'name':name,'url':url,'utc_started':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url,timeout=25) as response:
            raw=response.read(); rec.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
        rec.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
        path=base/f'sources/algebra_history_{name}.html'; path.write_bytes(raw)
        p=PageParser();p.feed(raw.decode('utf-8',errors='replace')); text='\n'.join(p.parts)
        (base/f'sources/algebra_history_{name}.txt').write_text(text)
        rec['links']=p.links
        rec['relevant_lines']=[s for s in p.parts if re.search(r'mac\s*lane|grothendieck|memoir|begle|dieudonn|bastien',s,re.I)]
    except Exception as exc:
        rec['error']=repr(exc)
        rec['scope']='No original source examined on this failed route; no restricted endpoint retried.'
    rec['elapsed_seconds']=time.monotonic()-start
    rec['utc_completed']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    return rec
start=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(retrieve,targets))
out={'records':records,'elapsed_seconds':time.monotonic()-start}
payload=json.dumps(out,ensure_ascii=False,indent=2)
(base/'logs/algebra_history_editorial43.json').write_text(payload+'\n')
print(payload)
