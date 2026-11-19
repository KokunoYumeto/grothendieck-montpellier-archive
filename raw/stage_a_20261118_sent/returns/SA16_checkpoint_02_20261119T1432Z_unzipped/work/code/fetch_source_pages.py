#!/usr/bin/env python3
"""Fetch public scholarly page images to the excluded research cache for inspection."""
from pathlib import Path
import urllib.request,hashlib,json,sys,datetime
out=[];root=Path(__file__).resolve().parents[2]/'external_cache/root_pages';root.mkdir(parents=True,exist_ok=True)
for ident in sys.argv[1:]:
 author,page=ident.split(':');url=f'https://wstein.org/Tables/antwerp/{author}/{page}.jpg';p=root/f'{author}_{page}.jpg'
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=45) as r:data=r.read()
  p.write_bytes(data);out.append({'url':url,'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'status':'downloaded'})
 except Exception as e:out.append({'url':url,'status':'failed','error':str(e)})
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sources':out},indent=2))
