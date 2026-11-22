from pathlib import Path
import urllib.request, urllib.parse, json, hashlib, time
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
target_url='http://sites.mathdoc.fr/archives-bourbaki/'
url='https://archive.org/wayback/available?'+urllib.parse.urlencode({'url':target_url})
started=time.monotonic()
try:
 with urllib.request.urlopen(url,timeout=30) as response:
  data=response.read()
  record={'url':url,'final_url':response.url,'status':response.status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 target=root/'notes/category_bourbaki_catalogue_available.json';target.write_bytes(data)
 record.update(saved=str(target),seconds=time.monotonic()-started);print(json.dumps(record),flush=True)
 metadata=json.loads(data);snapshot=metadata.get('archived_snapshots',{}).get('closest',{}).get('url')
 if snapshot:
  started=time.monotonic()
  with urllib.request.urlopen(snapshot,timeout=30) as response:
   data=response.read()
   record={'url':snapshot,'final_url':response.url,'status':response.status,'type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
  target=root/'sources/category_bourbaki_archived_catalogue.html';target.write_bytes(data)
  record.update(saved=str(target),seconds=time.monotonic()-started);print(json.dumps(record),flush=True)
except Exception as error: print(json.dumps({'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}),flush=True)
