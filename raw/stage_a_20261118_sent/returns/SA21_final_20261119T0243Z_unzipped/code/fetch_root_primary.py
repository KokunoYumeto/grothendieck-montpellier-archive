"""Fetch public primary sources for inspection, logging status and SHA256.
Downloaded third-party full texts stay outside the delivered archive.
"""
from pathlib import Path
import urllib.request,json,hashlib,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'references_cache';CACHE.mkdir(exist_ok=True)
SOURCES={
 'clader2016.pdf':'https://www.intlpress.com/site/pub/files/_fulltext/journals/hha/2016/0018/0001/HHA-2016-0018-0001-a002.pdf',
 'ega1_1960.pdf':'https://www.numdam.org/item/PMIHES_1960__4__5_0.pdf',
 'stone1934.pdf':'https://pmc.ncbi.nlm.nih.gov/articles/PMC1076376/pdf/pnas01743-0055.pdf',
 'Folder156_1.lean':'https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/lean/Grothendieck/Folder156_1.lean',
 'Folder156_2.lean':'https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/lean/Grothendieck/Folder156_2.lean',
}
def fetch(kv):
 name,url=kv
 try:
  request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research source verification)'})
  with urllib.request.urlopen(request,timeout=25) as response:
   data=response.read();meta={'name':name,'url':url,'status':response.status,'content_type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
  (CACHE/name).write_bytes(data)
  return meta
 except Exception as e:return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(fetch,SOURCES.items()))
out=ROOT/'outputs'/'primary_fetch.json';out.write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
