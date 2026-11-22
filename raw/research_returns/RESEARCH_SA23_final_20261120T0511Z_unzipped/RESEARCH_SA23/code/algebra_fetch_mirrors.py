from pathlib import Path
import urllib.request,time,hashlib
items=[('algebra_EGA0IV.pdf','https://geotoppos.org/divers/ega41.pdf'),('algebra_EGAIV4.pdf','https://geotoppos.org/divers/ega44.pdf'),('algebra_EGAIII1.pdf','https://geotoppos.org/divers/ega31.pdf')]
start=time.perf_counter()
for name,url in items:
    print('START',name,flush=True)
    try:
        with urllib.request.urlopen(url,timeout=25) as r: data=r.read()
        Path('RESEARCH_SA23/sources',name).write_bytes(data)
        print(name,len(data),hashlib.sha256(data).hexdigest(),url,flush=True)
    except Exception as e:print(name,type(e).__name__,str(e),flush=True)
print('seconds',time.perf_counter()-start,flush=True)
