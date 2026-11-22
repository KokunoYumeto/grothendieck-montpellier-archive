"""Read public catalogue waypoints advertised in saved KU organization HTML/JS."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode, urlparse
from html.parser import HTMLParser
import hashlib,json,re,urllib.request
ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'sources/category_aronszajn_price_organization.html').read_text()
waypoints=re.findall(r'data-waypoint-number="(\d+)"\s+data-uris="([^"]+)"',html)
if not waypoints:raise ValueError('No advertised waypoints')
base='https://archives.lib.ku.edu'
jobs=[('aronszajn_root',base+'/repositories/3/resources/11/tree/root')]
jobs.extend((f'price_wp_{int(n):02d}',base+'/repositories/3/resources/3239/infinite/waypoints?'+urlencode([('urls[]',u) for u in uris.split(';')])) for n,uris in waypoints)
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.text=[]
 def handle_data(self,data):
  if data.strip():self.text.append(data.strip())
def get(job):
 name,url=job;row={'name':name,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
 class SameHost(urllib.request.HTTPRedirectHandler):
  def redirect_request(self,req,fp,code,msg,headers,newurl):
   if urlparse(newurl).hostname!='archives.lib.ku.edu':raise ValueError('Unexpected redirect host')
   return super().redirect_request(req,fp,code,msg,headers,newurl)
 try:
  with urllib.request.build_opener(SameHost).open(url,timeout=35) as r:
   data=r.read();row.update(status=r.status,final_url=r.url)
  parsed=json.loads(data)
  file=ROOT/'sources'/f'category_aronszajn_{name}.json';file.write_bytes(data)
  row.update(path=str(file.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  if name.startswith('price_wp_'):
   text_records={}
   for uri,markup in parsed.items():
    p=Plain();p.feed(markup);text_records[uri]='\n'.join(p.text)
   file.with_suffix('.txt').write_text('\n\n'.join(uri+'\n'+t for uri,t in text_records.items())+'\n')
   row['record_count']=len(parsed)
 except Exception as error:row['error']=repr(error)
 return row
rows=[]
with ThreadPoolExecutor(max_workers=4) as pool:
 for future in as_completed([pool.submit(get,j) for j in jobs]):
  row=future.result();rows.append(row);print(json.dumps(row,ensure_ascii=False),flush=True)
  (ROOT/'logs/category_price_public_inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
