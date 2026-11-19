"""Download a public primary-source PDF for local text inspection; no credentials."""
from pathlib import Path
import urllib.request, hashlib, json, sys
root=Path('/workspace/scratch/a5176e5b5d45/SA06_work/parts/cote15_middle/research')
url,name=sys.argv[1:]
try:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req,timeout=30) as response:
        data=response.read()
    if not data.startswith(b'%PDF'):
        raise ValueError('Response is not a PDF; did not save it')
    (root/name).write_bytes(data)
    print(json.dumps({'url':url,'file':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}))
except Exception as exc:
    print(json.dumps({'url':url,'error':str(exc)}))
    sys.exit(1)
