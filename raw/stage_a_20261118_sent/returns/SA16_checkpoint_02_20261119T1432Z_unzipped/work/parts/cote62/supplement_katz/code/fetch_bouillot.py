"""The failed local retrieval attempted in this run, preserved for reproducibility."""
from pathlib import Path
import urllib.request,time,json
p=Path('external_cache/cote62/katz');p.mkdir(parents=True,exist_ok=True)
u='https://www-igm.univ-mlv.fr/~bouillot/OB_memoireM2.pdf'
t=time.time()
try:
    r=urllib.request.urlopen(u,timeout=40)
    b=r.read();(p/'Bouillot_M2.pdf').write_bytes(b)
    print(json.dumps({'url':u,'bytes':len(b),'seconds':time.time()-t}))
except Exception as e:
    print(json.dumps({'url':u,'error':str(e),'seconds':time.time()-t}))
