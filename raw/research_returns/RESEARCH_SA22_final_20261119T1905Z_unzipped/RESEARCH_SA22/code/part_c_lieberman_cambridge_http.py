"""One ordinary public Cambridge homepage GET; no retries or content probing."""
import datetime,hashlib,json,pathlib,time,urllib.parse,urllib.request
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).resolve().parents[1]
URL='https://www.dpmms.cam.ac.uk/~ajs1005/'
START=datetime.datetime.now(datetime.timezone.utc).isoformat();T=time.perf_counter()
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.current=None;self.words=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a' and 'href' in a:self.current={'href':urllib.parse.urljoin(URL,a['href']),'text':''}
 def handle_data(self,text):
  self.words.append(text)
  if self.current is not None:self.current['text']+=text
 def handle_endtag(self,tag):
  if tag=='a' and self.current is not None:self.links.append(self.current);self.current=None
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):return None
out={'started_utc':START,'url':URL,'ordinary_http_requests':1,'automatic_redirects':False,'retries':0,'mathematical_checks':0}
try:
 with urllib.request.build_opener(NoRedirect).open(URL,timeout=20) as r:
  raw=r.read(2097153);assert len(raw)<=2097152
  out.update(status=r.status,content_type=r.headers.get('Content-Type'),response_bytes=len(raw),response_sha256=hashlib.sha256(raw).hexdigest())
  cache=ROOT.parent/'source_reading/lieberman_cambridge';cache.mkdir(parents=True,exist_ok=True)
  dest=cache/'scholl_home.html';dest.write_bytes(raw);out['raw_cache_path']=str(dest)
  parser=Parser();parser.feed(raw.decode('utf-8',errors='replace'))
  out['advertised_links']=parser.links
  text=' '.join(parser.words).lower();out['target_literal_hits']={w:text.count(w.lower()) for w in ['Lieberman','Hodge manifolds','2373533']}
except Exception as e:
 out.update(status=getattr(e,'code',None),error_type=type(e).__name__,error=str(e))
out['runtime_seconds']=time.perf_counter()-T
(ROOT/'code/part_c_lieberman_cambridge_http_output.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2))
