"""Read publicly advertised institutional endpoints to locate the complete inventory."""
from pathlib import Path
import urllib.request,json,time,hashlib,concurrent.futures,re
root=Path(__file__).resolve().parents[1]
urls={
 'montpellier_public_api':'https://grothendieck.umontpellier.fr/wp-json/',
 'imag_grothendieck':'https://imag.umontpellier.fr/?page_id=211',
}
def fetch(item):
 key,url=item;t=time.perf_counter();r={'key':key,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=25) as f:data=f.read();r.update(status=f.status,final_url=f.geturl(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  ext='.json' if key.endswith('_api') else '.html'
  p=root/'sources'/('algebra_history_'+key+ext);p.write_bytes(data);r['file']=str(p.relative_to(root))
  if ext=='.json':
   obj=json.loads(data)
   r['namespaces']=obj.get('namespaces',[])
   r['candidate_routes']={k:v for k,v in obj.get('routes',{}).items() if k in ['/wp/v2/media','/wp/v2/search','/wp/v2/pages']}
  else:r['links']=[m.group(1) for m in re.finditer(r'href=[\"\x27]([^\"\x27]+)[\"\x27]',data.decode(errors='replace')) if re.search(r'groth|archive|\.pdf|inventaire',m.group(1),re.I)]
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-t,6);return r
t=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:records=list(pool.map(fetch,urls.items()))
out={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-t,6)}
(root/'logs/algebra_history_fetch13.json').write_text(json.dumps(out,indent=2,ensure_ascii=False));print(json.dumps(out,indent=2,ensure_ascii=False))
