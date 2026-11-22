"""Execute Foli@'s exact public metadata AJAX search, as exposed by its client JS."""
import hashlib, json, time, urllib.request
from pathlib import Path
root=Path('RESEARCH_SA23')
url='https://folia.scdi-montpellier.fr/call/ajax/api_flora/search'
payload={'sortBy':'1','search':'Grothendieck','filters':[],'sortType':'','firstLoad':True,'currentPage':'1','searchInText':''}
tick=time.monotonic()
record={'url':url,'method':'POST','payload':payload,'source':'sources/algebra_history_folia_search_client.js; exact public search JSON schema'}
try:
 request=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={'Content-Type':'application/json; charset=utf-8'})
 with urllib.request.urlopen(request,timeout=25) as response:
  content=response.read()
  record.update(status=response.status,final_url=response.url)
 out=root/'sources/algebra_history_folia_grothendieck_results.json'
 out.write_bytes(content)
 record.update(file=str(out.relative_to(root)),bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
 result=json.loads(content)
 record['nbResults']=result.get('nbResults')
 record['html']=result.get('html')
except Exception as exc:
 record['error']=type(exc).__name__+': '+str(exc)
record['elapsed_seconds']=round(time.monotonic()-tick,6)
s=json.dumps(record,ensure_ascii=False,indent=2)
(root/'logs/algebra_history_catalog20.json').write_text(s+'\n')
print(s)
