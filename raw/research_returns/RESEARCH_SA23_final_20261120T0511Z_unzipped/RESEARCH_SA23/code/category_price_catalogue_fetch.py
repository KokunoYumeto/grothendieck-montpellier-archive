"""Retrieve advertised Price finding aid and public tree implementation."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import hashlib,json,urllib.request
ROOT=Path(__file__).resolve().parents[1]
jobs=[('price3239','https://archives.lib.ku.edu/repositories/3/resources/3239'),
 ('price_organization','https://archives.lib.ku.edu/repositories/3/resources/3239/collection_organization'),
 ('public_application','https://archives.lib.ku.edu/assets/application-589dd4e86c691634ac2aec1683b4c758133e463261a6795a9e45d0f75b93fad7.js')]
def get(job):
 name,url=job;row={'name':name,'url':url,'utc':datetime.now(timezone.utc).isoformat()}
 class SameHost(urllib.request.HTTPRedirectHandler):
  def redirect_request(self,req,fp,code,msg,headers,newurl):
   if urlparse(newurl).hostname!='archives.lib.ku.edu':raise ValueError('Unexpected redirect host')
   return super().redirect_request(req,fp,code,msg,headers,newurl)
 try:
  with urllib.request.build_opener(SameHost).open(url,timeout=30) as r:
   data=r.read();row.update(status=r.status,final_url=r.url)
  extension='.js' if name=='public_application' else '.html'
  path=ROOT/'sources'/f'category_aronszajn_{name}{extension}';path.write_bytes(data)
  row.update(path=str(path.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as error:row['error']=repr(error)
 return row
rows=[]
with ThreadPoolExecutor(max_workers=3) as pool:
 for future in as_completed([pool.submit(get,j) for j in jobs]):
  row=future.result();rows.append(row);print(json.dumps(row),flush=True)
  (ROOT/'logs/category_price_catalogue_fetch.json').write_text(json.dumps(rows,indent=2)+'\n')
