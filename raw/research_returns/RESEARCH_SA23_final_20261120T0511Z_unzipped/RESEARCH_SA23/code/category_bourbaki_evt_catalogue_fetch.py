from pathlib import Path
from html.parser import HTMLParser
import urllib.request,urllib.parse,json,hashlib,time
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag=='a' and 'href' in attrs:self.links.append(attrs['href'])
parser=Links();parser.feed((root/'sources/category_bourbaki_archived_catalogue.html').read_text())
relative=next(u for u in parser.links if 'chap=2_REDAC_EVT' in u)
base=json.loads((root/'notes/category_bourbaki_catalogue_available.json').read_text())['archived_snapshots']['closest']['url']
url=urllib.parse.urljoin(base,relative);started=time.monotonic()
try:
 with urllib.request.urlopen(url,timeout=35) as response:
  data=response.read();record={'url':url,'final_url':response.url,'status':response.status,'type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 target=root/'sources/category_bourbaki_evt_catalogue.html';target.write_bytes(data)
 record.update(saved=str(target),seconds=time.monotonic()-started);print(json.dumps(record),flush=True)
except Exception as error: print(json.dumps({'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}),flush=True)
