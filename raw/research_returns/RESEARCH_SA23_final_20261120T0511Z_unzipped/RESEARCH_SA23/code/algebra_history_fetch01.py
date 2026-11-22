"""Bounded public historical-source retrievals, with exact URLs and preserved outputs."""
from pathlib import Path
import urllib.request, urllib.parse, hashlib, json, time, concurrent.futures
root=Path(__file__).resolve().parents[1]
tasks=[
 ('ams_notices196308','https://www.ams.org/journals/notices/196308/196308FullIssue.pdf'),
 ('zbmath_reprint','https://api.zbmath.org/v1/document/0123.30301'),
 ('zbmath_first','https://api.zbmath.org/v1/document/0064.35501'),
 ('archive_memoir','https://archive.org/advancedsearch.php?'+urllib.parse.urlencode({'q':'title:"Produits tensoriels topologiques"','output':'json','rows':20})),
 ('archive_lidskii_volume','https://archive.org/advancedsearch.php?'+urllib.parse.urlencode({'q':'title:"Thirteen papers on functional analysis"','output':'json','rows':20})),
 ('rsl_doklady_record','https://search.rsl.ru/ru/record/01003386293'),
]
def fetch(task):
 name,url=task; start=time.perf_counter(); record={'name':name,'url':url}
 try:
  with urllib.request.urlopen(url, timeout=35) as response:
   data=response.read(); record.update(status=response.status,final_url=response.geturl(),content_type=response.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  ext='.pdf' if data.startswith(b'%PDF') else '.json' if data.lstrip().startswith(b'{') else '.html'
  path=root/'sources'/('algebra_history_'+name+ext);path.write_bytes(data);record['file']=str(path.relative_to(root))
 except Exception as error: record['error']=repr(error)
 record['elapsed_seconds']=round(time.perf_counter()-start,6)
 return record
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 records=list(pool.map(fetch,tasks))
output={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs'/'algebra_history_fetch01.json').write_text(json.dumps(output,indent=2,ensure_ascii=False))
print(json.dumps(output,indent=2,ensure_ascii=False))

