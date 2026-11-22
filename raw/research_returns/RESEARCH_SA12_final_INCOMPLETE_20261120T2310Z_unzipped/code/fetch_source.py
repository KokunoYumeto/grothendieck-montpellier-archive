"""Download a named public research source and record provenance and digest."""
from pathlib import Path
from datetime import datetime, timezone
import sys, urllib.request, hashlib, json, time
root=Path(__file__).resolve().parents[1]
url,name=sys.argv[1:3]
dest=root/'sources'/name
dest.parent.mkdir(parents=True,exist_ok=True)
t=time.perf_counter()
req=urllib.request.Request(url,headers={'User-Agent':'SA12 research source retrieval'})
with urllib.request.urlopen(req,timeout=45) as r:
    data=r.read(); final_url=r.url; content_type=r.headers.get('Content-Type')
dest.write_bytes(data)
meta={'requested_url':url,'final_url':final_url,'path':str(dest.relative_to(root)),'utc':datetime.now(timezone.utc).isoformat(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'content_type':content_type,'seconds':time.perf_counter()-t}
dest.with_name(dest.name+'.provenance.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
