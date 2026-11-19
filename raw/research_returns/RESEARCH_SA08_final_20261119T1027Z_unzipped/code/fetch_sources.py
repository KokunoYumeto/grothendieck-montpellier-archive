"""Retrieve explicitly selected public mathematical sources; log success/failure."""
from pathlib import Path
import urllib.request,sys,time,json
dest=Path(__file__).resolve().parents[1]/'sources'
dest.mkdir(exist_ok=True)
for spec in sys.argv[1:]:
    name,url=spec.split('=',1)
    t=time.monotonic()
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'MathematicalResearch/1.0'})
        with urllib.request.urlopen(req,timeout=25) as r:
            data=r.read(); ctype=r.headers.get('content-type'); final=r.url
        (dest/name).write_bytes(data)
        print(json.dumps({'file':name,'url':url,'final_url':final,'bytes':len(data),'content_type':ctype,'seconds':round(time.monotonic()-t,3)}),flush=True)
    except Exception as e:
        print(json.dumps({'file':name,'url':url,'error':str(e),'seconds':round(time.monotonic()-t,3)}),flush=True)
