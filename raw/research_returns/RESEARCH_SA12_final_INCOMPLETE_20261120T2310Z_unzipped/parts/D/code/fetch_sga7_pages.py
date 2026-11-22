"""Fetch primary scanned pages around SGA7 II, XIII 2.1."""
from pathlib import Path
import concurrent.futures, urllib.request, hashlib, json, time
root=Path(__file__).resolve().parents[1]
def fetch(n):
    url=f'https://wstein.org/sga/sga/7-2/7-2t_{n:03d}.jpeg'
    dest=root/'sources'/f'7-2t_{n:03d}.jpeg'
    t=time.monotonic()
    try:
        data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
        dest.write_bytes(data)
        return {'url':url,'path':str(dest.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'seconds':round(time.monotonic()-t,3)}
    except Exception as e:return {'url':url,'error':str(e),'seconds':round(time.monotonic()-t,3)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    result=list(pool.map(fetch,[99,100,101,102,103,104,105]))
(root/'code/fetch_sga7_pages_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
