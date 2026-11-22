from pathlib import Path
import urllib.request,urllib.parse,hashlib,json,time
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
original='https://archives-bourbaki.ahp-numerique.fr/'
api='https://archive.org/wayback/available?'+urllib.parse.urlencode({'url':original})
s=time.monotonic()
try:
    with urllib.request.urlopen(api,timeout=35) as response:
        data=response.read()
    p=r/'notes/category_bourbaki_r230_archived_portal_available.json';p.write_bytes(data)
    print(json.dumps({'url':api,'bytes':len(data),'saved':str(p),'response':json.loads(data)}),flush=True)
    snap=json.loads(data).get('archived_snapshots',{}).get('closest',{}).get('url')
    if snap:
        assert urllib.parse.urlsplit(snap).hostname=='web.archive.org'
        with urllib.request.urlopen(snap,timeout=35) as response:
            data=response.read();final=response.url;typ=response.headers.get('Content-Type');status=response.status
        p=r/'sources/category_bourbaki_r230_archived_portal.html';p.write_bytes(data)
        print(json.dumps({'url':snap,'final_url':final,'status':status,'type':typ,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'saved':str(p)}),flush=True)
except Exception as e:
    print(json.dumps({'url':api,'error_type':type(e).__name__,'error':str(e),'seconds':time.monotonic()-s}),flush=True)
