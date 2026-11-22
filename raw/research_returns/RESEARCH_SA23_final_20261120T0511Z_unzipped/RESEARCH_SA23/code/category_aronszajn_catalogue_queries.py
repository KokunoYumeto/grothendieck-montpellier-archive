"""Follow only public search forms and tree script advertised in saved KU HTML."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode, urlparse
import hashlib, json, urllib.request
ROOT=Path(__file__).resolve().parents[1]
base='https://archives.lib.ku.edu'
jobs=[
 ('collection_Grothendieck',base+'/repositories/3/resources/11/search?'+urlencode({'utf8':'✓','filter_q[]':'Grothendieck','op[]':'','field[]':'','limit':'','q[]':'*','filter_from_year':'','filter_to_year':'','commit':'Search'})),
 ('all_Grothendieck',base+'/search?'+urlencode({'utf8':'✓','op[]':'','q[]':'Grothendieck','limit':'','field[]':'','from_year[]':'','to_year[]':''})),
 ('tree',base+'/repositories/3/resources/11/tree'),
 ('tree_script',base+'/assets/largetree-72b4229592416085346cda5f0ac7f94abffb7a26be4058aaf1cbe79e03a1118b.js'),
 ('digital_home','https://digital.lib.ku.edu/islandora/root')]
def fetch(job):
 name,url=job;host=urlparse(url).hostname;row={'name':name,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
 class PublicRedirect(urllib.request.HTTPRedirectHandler):
  def redirect_request(self,req,fp,code,msg,headers,newurl):
   if urlparse(newurl).hostname!=host:raise ValueError('Unexpected redirect host')
   return super().redirect_request(req,fp,code,msg,headers,newurl)
 try:
  with urllib.request.build_opener(PublicRedirect).open(url,timeout=35) as r:
   data=r.read();row.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
  extension='.js' if name=='tree_script' else '.html'
  if 'json' in (row.get('content_type') or ''):extension='.json'
  path=ROOT/'sources'/f'category_aronszajn_{name}{extension}';path.write_bytes(data)
  row.update(path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as error:row['error']=repr(error)
 return row
rows=[]
with ThreadPoolExecutor(max_workers=5) as pool:
 for future in as_completed([pool.submit(fetch,j) for j in jobs]):
  row=future.result();rows.append(row);print(json.dumps(row,ensure_ascii=False),flush=True)
  (ROOT/'logs/category_aronszajn_catalogue_queries.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
