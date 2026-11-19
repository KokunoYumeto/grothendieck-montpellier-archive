"""Search public catalogue for alternate records, then inspect advertised access flags."""
from pathlib import Path
import urllib.request,urllib.parse,json,time,concurrent.futures
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
queries=['title:(quasiconformal mappings plane)','creator:(Lehto) AND creator:(Virtanen)','title:(Quasikonforme Abbildungen)']
def query(q):
 t=time.perf_counter();params=[('q',q),('rows','100'),('output','json')]+[('fl[]',x) for x in ['identifier','title','creator','date','year','access-restricted-item','collection']]
 u='https://archive.org/advancedsearch.php?'+urllib.parse.urlencode(params)
 try:
  with urllib.request.urlopen(u,timeout=35) as r:d=json.load(r)
  return dict(query=q,url=u,seconds=time.perf_counter()-t,response=d.get('response',{}))
 except Exception as e:return dict(query=q,url=u,error=str(e),seconds=time.perf_counter()-t)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(query,queries))
items={d['identifier']:d for row in rows for d in row.get('response',{}).get('docs',[]) if 'leht' in str(d).lower() or 'virtanen' in str(d).lower()}
def meta(item):
 t=time.perf_counter()
 try:
  with urllib.request.urlopen('https://archive.org/metadata/'+item,timeout=35) as r:d=json.load(r)
  (R/'sources'/('lehto_metadata_'+item+'.json')).write_text(json.dumps(d,indent=2)+'\n')
  m=d.get('metadata',{});files=d.get('files',[])
  return dict(item=item,seconds=time.perf_counter()-t,restricted=m.get('access-restricted-item'),collection=m.get('collection'),files=[{k:f.get(k) for k in ['name','format','size','private']} for f in files if f.get('format') in ['Text PDF','Image Container PDF','DjVuTXT']])
 except Exception as e:return dict(item=item,error=str(e),seconds=time.perf_counter()-t)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:records=list(ex.map(meta,items))
out=dict(query_requests=len(queries),metadata_requests=len(items),seconds=time.perf_counter()-start,queries=rows,metadata=records)
(R/'code/root_lehto_catalogue_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
