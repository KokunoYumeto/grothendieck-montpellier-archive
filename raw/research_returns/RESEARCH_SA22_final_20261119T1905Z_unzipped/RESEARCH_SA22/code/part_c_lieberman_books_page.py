"""Read the indexed public Google Books volume's actual forms/links once."""
import datetime,hashlib,json,pathlib,time,urllib.parse,urllib.request
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).resolve().parents[1]
URL='https://books.google.com/books/about/American_Journal_of_Mathematics.html?id=Q5k0AAAAIAAJ'
START=datetime.datetime.now(datetime.timezone.utc).isoformat();T=time.perf_counter()
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.forms=[];self.form=None;self.links=[];self.link=None;self.text=[]
 def handle_starttag(self,t,aa):
  a=dict(aa)
  if t=='form':self.form={'action':urllib.parse.urljoin(URL,a.get('action','')),'method':a.get('method','get'),'inputs':[]}
  if t=='input' and self.form is not None:self.form['inputs'].append(a)
  if t=='a' and a.get('href'):self.link={'url':urllib.parse.urljoin(URL,a['href']),'text':''}
 def handle_data(self,s):
  self.text.append(s)
  if self.link is not None:self.link['text']+=s
 def handle_endtag(self,t):
  if t=='form' and self.form is not None:self.forms.append(self.form);self.form=None
  if t=='a' and self.link is not None:self.links.append(self.link);self.link=None
class NoRedirect(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,*a,**k):return None
out={'started_utc':START,'url':URL,'ordinary_requests':1,'automatic_redirects':False,'retries':0,'mathematical_checks':0}
try:
 with urllib.request.build_opener(NoRedirect).open(URL,timeout=20) as r:
  raw=r.read(2097153);assert len(raw)<=2097152
  out.update(status=r.status,response_bytes=len(raw),response_sha256=hashlib.sha256(raw).hexdigest(),content_type=r.headers.get('Content-Type'))
  cache=ROOT.parent/'source_reading/lieberman_books';cache.mkdir(parents=True,exist_ok=True);dest=cache/'indexed_volume_page.html';dest.write_bytes(raw);out['raw_cache_path']=str(dest)
  p=Parser();p.feed(raw.decode('utf-8',errors='replace'));out['advertised_forms']=p.forms;out['advertised_links']=p.links
  text=' '.join(p.text).lower();out['access_label_presence']={s:s in text for s in ['snippet view','limited preview','no preview','preview unavailable','preview not available','captcha','unusual traffic','sign in']}
except Exception as e:out.update(status=getattr(e,'code',None),error_type=type(e).__name__,error=str(e))
out['runtime_seconds']=time.perf_counter()-T
(ROOT/'code/part_c_lieberman_books_page_output.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='advertised_links'},ensure_ascii=False,indent=2))
