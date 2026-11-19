"""Download an already identified public primary source for local text/visual checks."""
import sys,urllib.request
from pathlib import Path
url,name=sys.argv[1:]
out=Path(__file__).resolve().parents[2]/'public_sources'
out.mkdir(exist_ok=True)
dest=out/name
try:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research source verification)'})
    with urllib.request.urlopen(req,timeout=25) as r: raw=r.read()
    if not raw.startswith(b'%PDF'):
        raise ValueError('Response is not a PDF')
    dest.write_bytes(raw)
    print('Downloaded',url,'to',dest,'bytes',len(raw))
except Exception as e:
    print(type(e).__name__+': '+str(e));sys.exit(1)
