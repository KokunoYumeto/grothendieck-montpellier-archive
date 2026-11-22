from pathlib import Path
from urllib.request import urlopen,Request
from urllib.parse import urlencode
import concurrent.futures,json,time,datetime,hashlib
root=Path(__file__).resolve().parents[1];start=time.monotonic()
queries=['title:(Математика) AND year:1958','title:(Matematika) AND year:1958','"сборник переводов" AND year:1958','"Теория Фредгольма"']
def get(item):
 n,q=item; st=time.monotonic();url='https://archive.org/advancedsearch.php?'+urlencode({'q':q,'fl[]':['identifier','title','year','collection'],'rows':50,'page':1,'output':'json'},doseq=True)
 rec={'query':q,'url':url}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Research source retrieval'}),timeout=45) as res:
   data=res.read();rec.update(status=res.status,final_url=res.url,content_type=res.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  p=root/f'notes/geometry_russian_ia_query{n:02}.json';p.write_bytes(data);rec['path']=str(p.relative_to(root));j=json.loads(data);rec['numFound']=j.get('response',{}).get('numFound');rec['docs']=j.get('response',{}).get('docs',[])
 except Exception as e: rec['error']=repr(e)
 rec['elapsed_seconds']=time.monotonic()-st;return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(get,enumerate(queries,1)))
log={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'queries':rows,'elapsed_seconds':time.monotonic()-start,'scope':'public Internet Archive metadata search only; no account or blocked source requests'}
(root/'logs/geometry_russian_ia_search.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n');print(json.dumps(log,ensure_ascii=False,indent=2))
