"""Submit the ordinary public archive and digital-collection search forms."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode, urlparse
from html.parser import HTMLParser
from http.cookiejar import CookieJar
import hashlib, json, urllib.request
ROOT=Path(__file__).resolve().parents[1]
class FormReader(HTMLParser):
 def __init__(self):super().__init__();self.active=False;self.fields={};self.action=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='form' and a.get('id')=='islandora-collection-search-form':self.active=True;self.action=a['action']
  if self.active and tag in ['input','button'] and a.get('name'):self.fields[a['name']]=a.get('value','')
 def handle_endtag(self,tag):
  if tag=='form':self.active=False
def search(job):
 service,term=job;host='archives.lib.ku.edu' if service=='archives' else 'digital.lib.ku.edu'
 row={'service':service,'term':term,'utc':datetime.now(timezone.utc).isoformat()}
 class PublicRedirect(urllib.request.HTTPRedirectHandler):
  def redirect_request(self,req,fp,code,msg,headers,newurl):
   if urlparse(newurl).hostname!=host:raise ValueError('Unexpected redirect host')
   return super().redirect_request(req,fp,code,msg,headers,newurl)
 opener=urllib.request.build_opener(PublicRedirect,urllib.request.HTTPCookieProcessor(CookieJar()))
 try:
  if service=='archives':
   url='https://'+host+'/search?'+urlencode({'utf8':'✓','op[]':'','q[]':term,'limit':'','field[]':'','from_year[]':'','to_year[]':'','commit':'Search'})
   request=urllib.request.Request(url);row['method']='GET'
  else:
   root='https://'+host+'/islandora/root'
   with opener.open(root,timeout=25) as r:form_html=r.read()
   formfile=ROOT/'sources'/f'category_aronszajn_digital_search_form_{term}.html';formfile.write_bytes(form_html)
   parser=FormReader();parser.feed(form_html.decode(errors='replace'))
   if parser.action!='/islandora/root':raise ValueError('Advertised form changed')
   parser.fields['islandora_simple_search_query']=term
   parser.fields['op']='search'
   request=urllib.request.Request(root,data=urlencode(parser.fields).encode())
   row.update(method='POST',form_path=str(formfile.relative_to(ROOT)),fields=parser.fields)
  row['url']=request.full_url
  with opener.open(request,timeout=35) as r:
   data=r.read();row.update(status=r.status,final_url=r.url)
  file=ROOT/'sources'/f'category_aronszajn_{service}_search_{term}.html';file.write_bytes(data)
  row.update(path=str(file.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as error:row['error']=repr(error)
 return row
rows=[]
with ThreadPoolExecutor(max_workers=4) as pool:
 for future in as_completed([pool.submit(search,(s,t)) for s in ['archives','digital'] for t in ['Grothendieck','Aronszajn']]):
  row=future.result();rows.append(row);print(json.dumps(row,ensure_ascii=False),flush=True)
  (ROOT/'logs/category_aronszajn_public_searches.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
