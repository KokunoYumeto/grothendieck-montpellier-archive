"""Read public search endpoints exactly exposed by the catalogue client code."""
import concurrent.futures, hashlib, json, time, urllib.request
from pathlib import Path
root=Path('RESEARCH_SA23')
tasks=[
 ('calames_grothendieck_results','https://calames.abes.fr/prod/EadSearch.aspx?Query=Rech&fullText=Grothendieck&from=1&to=50','.xml'),
 ('folia_search_client','https://folia.scdi-montpellier.fr/modules/custom/api_flora/assets/build/scripts.min.js?v=1.1','.js'),
]
def fetch(task):
 name,url,ext=task
 tick=time.monotonic()
 row={'name':name,'url':url,'method':'GET'}
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   content=response.read()
   row.update(status=response.status,final_url=response.url)
  out=root/'sources'/('algebra_history_'+name+ext)
  out.write_bytes(content)
  row.update(file=str(out.relative_to(root)),bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
 except Exception as exc:
  row['error']=type(exc).__name__+': '+str(exc)
 row['elapsed_seconds']=round(time.monotonic()-tick,6)
 return row
tick=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 rows=list(pool.map(fetch,tasks))
s=json.dumps({'results':rows,'elapsed_seconds':round(time.monotonic()-tick,6)},ensure_ascii=False,indent=2)
(root/'logs/algebra_history_catalog19.json').write_text(s+'\n')
print(s)
