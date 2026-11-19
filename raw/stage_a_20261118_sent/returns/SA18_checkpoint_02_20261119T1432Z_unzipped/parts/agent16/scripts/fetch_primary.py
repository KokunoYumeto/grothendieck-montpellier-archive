"""Fetch an actually requested primary source for local reading when web preview is size limited.
Downloaded PDFs are review inputs, not final dossier attachments.
"""
import urllib.request,sys,json,hashlib
from pathlib import Path
out=Path(__file__).resolve().parents[1]
url,name=sys.argv[1:3]
try:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (scholarly source verification)'})
    with urllib.request.urlopen(req,timeout=30) as response:
        data=response.read();status=response.status;final=response.url
    path=out/'research'/'downloaded_inputs'/name;path.parent.mkdir(exist_ok=True)
    path.write_bytes(data)
    print(json.dumps({'requested':url,'resolved':final,'status':status,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'path':str(path)}))
except Exception as exc:
    print(json.dumps({'requested':url,'error':str(exc)}));sys.exit(1)
