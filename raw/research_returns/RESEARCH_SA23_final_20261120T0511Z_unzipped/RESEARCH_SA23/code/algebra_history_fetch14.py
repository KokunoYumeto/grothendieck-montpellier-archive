"""Search the institutional site's publicly advertised GET catalogue only."""
from pathlib import Path
import urllib.request,urllib.parse,json,time,hashlib,concurrent.futures
root=Path(__file__).resolve().parents[1]
base='https://grothendieck.umontpellier.fr/wp-json/wp/v2/'
queries={
 'public_media_inventory':('media',{'search':'inventaire','context':'view','per_page':100}),
 'public_media_pdf':('media',{'mime_type':'application/pdf','context':'view','per_page':100}),
 'public_pages_inventory':('pages',{'search':'inventaire','context':'view','per_page':100}),
 'public_pages_index':('pages',{'search':'index','context':'view','per_page':100}),
}
def fetch(item):
 key,(route,args)=item;url=base+route+'?'+urllib.parse.urlencode(args);t=time.perf_counter();r={'key':key,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=25) as f:data=f.read();r.update(status=f.status,final_url=f.geturl(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),total=f.headers.get('X-WP-Total'),total_pages=f.headers.get('X-WP-TotalPages'))
  p=root/'sources'/('algebra_history_'+key+'.json');p.write_bytes(data);r['file']=str(p.relative_to(root))
  obj=json.loads(data)
  r['items']=[{'id':x.get('id'),'title':x.get('title'),'source_url':x.get('source_url'),'link':x.get('link'),'mime_type':x.get('mime_type')} for x in obj] if isinstance(obj,list) else obj
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-t,6);return r
t=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(fetch,queries.items()))
out={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-t,6)}
(root/'logs/algebra_history_fetch14.json').write_text(json.dumps(out,indent=2,ensure_ascii=False));print(json.dumps(out,indent=2,ensure_ascii=False))
