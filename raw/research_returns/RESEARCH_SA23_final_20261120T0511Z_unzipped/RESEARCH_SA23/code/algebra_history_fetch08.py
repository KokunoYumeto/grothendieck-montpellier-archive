"""Distinct public first-printing searches, with every response preserved."""
from pathlib import Path
import urllib.request,urllib.parse,json,hashlib,time,concurrent.futures
root=Path(__file__).resolve().parents[1]
queries={
 'memoirs1955':'title:memoirs AND year:1955',
 'groth1955':'creator:grothendieck AND year:1955',
 'tensoriels':'title:tensoriels',
 'memoirsvolume16':'title:"memoirs of the american mathematical society" AND volume:16',
}
urls=[(k,'https://archive.org/advancedsearch.php?'+urllib.parse.urlencode({'q':q,'output':'json','rows':100}),'.json') for k,q in queries.items()]
urls += [('ams_old_notices','https://www.ams.org/notices/196308/196308FullIssue.pdf','.pdf')]
def retrieve(item):
 k,url,ext=item;t=time.perf_counter();r={'key':k,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=25) as f:data=f.read();r.update(status=f.status,final_url=f.geturl(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  p=root/'sources'/('algebra_history_firstprint_'+k+ext);p.write_bytes(data);r['file']=str(p.relative_to(root))
  if ext=='.json':
   d=json.loads(data);r['numFound']=d.get('response',{}).get('numFound');r['docs']=d.get('response',{}).get('docs',[])
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-t,6);return r
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p:records=list(p.map(retrieve,urls))
out={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs/algebra_history_fetch08.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
print(json.dumps(out,indent=2,ensure_ascii=False))
