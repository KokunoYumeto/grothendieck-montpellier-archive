#!/usr/bin/env python3
"""Retrieve explicitly listed public scholarly sources; log bytes and SHA256."""
import urllib.request, pathlib, time, json, hashlib, concurrent.futures
root=pathlib.Path(__file__).resolve().parent.parent
jobs={
 'manuscript154.pdf':'https://grothendieck.umontpellier.fr/154.pdf',
 'manuscript156-4.pdf':'https://grothendieck.umontpellier.fr/156-4.pdf',
 'SZ1993.pdf':'https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/020PREPRINT.pdf',
}
def get(job):
 name,url=job; t=time.perf_counter(); p=root/'sources'/name
 try:
  if not p.exists():
   with urllib.request.urlopen(url,timeout=45) as response:
    p.write_bytes(response.read())
  data=p.read_bytes()
  return dict(name=name,url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),seconds=time.perf_counter()-t,status='downloaded')
 except Exception as e:return dict(name=name,url=url,seconds=time.perf_counter()-t,status='failed',error=repr(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: ans=list(pool.map(get,jobs.items()))
(root/'audit'/'root_fetch_sources.json').write_text(json.dumps(ans,indent=2)+'\n')
print(json.dumps(ans,indent=2))
