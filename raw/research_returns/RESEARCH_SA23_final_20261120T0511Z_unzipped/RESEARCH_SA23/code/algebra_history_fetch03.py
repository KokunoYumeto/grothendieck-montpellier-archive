"""Public catalogue and book-search routes; no authentication or restricted content."""
from pathlib import Path
import urllib.request,urllib.parse,json,hashlib,time,concurrent.futures
root=Path(__file__).resolve().parents[1]
tasks=[]
for name,query in [
 ('archive_memoir_broad','grothendieck AND tensoriels'),
 ('archive_lidskii_broad','lidskii AND trace'),
 ('archive_translations','title:translations AND creator:"American Mathematical Society"'),
 ('archive_doklady','title:doklady AND year:1959')]:
 tasks.append((name,'https://archive.org/advancedsearch.php?'+urllib.parse.urlencode({'q':query,'output':'json','rows':100})))
tasks.append(('books_lidskii_publicsearch','https://books.google.com/books?'+urllib.parse.urlencode({'id':'KY7qQKZ-3GYC','jscmd':'SearchWithinVolume2','q':'Grothendieck'})))
def fetch(task):
 name,url=task;start=time.perf_counter();r={'name':name,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=30) as f:
   data=f.read();r.update(status=f.status,final_url=f.geturl(),content_type=f.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  ext='.json' if data.lstrip().startswith(b'{') else '.html'
  p=root/'sources'/('algebra_history_'+name+ext);p.write_bytes(data);r['file']=str(p.relative_to(root))
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-start,6);return r
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:rs=list(p.map(fetch,tasks))
out={'retrievals':rs,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs'/'algebra_history_fetch03.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

