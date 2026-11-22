"""Fetch linked public Calames search JS and submit Foli@'s public metadata form."""
import concurrent.futures, hashlib, json, time, urllib.parse, urllib.request
from pathlib import Path
root=Path('RESEARCH_SA23')
catalog=json.loads((root/'logs/algebra_history_catalog17.json').read_text())
folia=next(x for x in catalog['results'] if x['name']=='folia_public')
form=next(x for x in folia['forms'] if x['id']=='form-flora')
fields={x['name']:x['value'] for x in form['fields'] if x['type']=='hidden'}
fields.update({'search-text':'Grothendieck','search-in-txt':'','op':'Rechercher'})
tasks=[
 ('calames_config_js','https://calames.abes.fr/pub/javascript/config.js',None),
 ('calames_search_js','https://calames.abes.fr/pub/javascript/calames.js',None),
 ('folia_grothendieck_search','https://folia.scdi-montpellier.fr/',fields),
]
def fetch(task):
 name,url,payload=task
 tick=time.monotonic()
 row={'name':name,'url':url,'method':'POST' if payload else 'GET','payload':payload}
 try:
  data=urllib.parse.urlencode(payload).encode() if payload else None
  req=urllib.request.Request(url,data=data)
  with urllib.request.urlopen(req,timeout=25) as r:
   content=r.read()
   row.update(status=r.status,final_url=r.url)
  out=root/'sources'/('algebra_history_'+name+('.html' if payload else '.js'))
  out.write_bytes(content)
  row.update(file=str(out.relative_to(root)),bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
 except Exception as exc:
  row['error']=type(exc).__name__+': '+str(exc)
 row['elapsed_seconds']=round(time.monotonic()-tick,6)
 return row
start=time.monotonic()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 rows=list(pool.map(fetch,tasks))
record={'purpose':'Read-only public catalogue search; no restricted document requested','results':rows,'elapsed_seconds':round(time.monotonic()-start,6)}
s=json.dumps(record,ensure_ascii=False,indent=2)
(root/'logs/algebra_history_catalog18.json').write_text(s+'\n')
print(s)
