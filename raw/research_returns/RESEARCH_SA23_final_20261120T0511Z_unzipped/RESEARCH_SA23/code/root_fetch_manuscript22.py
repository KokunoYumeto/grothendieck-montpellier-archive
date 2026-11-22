from pathlib import Path
import urllib.request,hashlib,time
url='https://grothendieck.umontpellier.fr/22.pdf'
dest=Path(__file__).resolve().parents[1]/'sources'/'manuscript22.pdf'
start=time.perf_counter()
try:
    with urllib.request.urlopen(url,timeout=40) as r:
        b=r.read()
        print('HTTP',r.status,'content type',r.headers.get('Content-Type'))
    dest.write_bytes(b)
    print('Bytes',len(b),'SHA256',hashlib.sha256(b).hexdigest())
except Exception as e:
    print(type(e).__name__,str(e))
print('Elapsed seconds',time.perf_counter()-start)
