from pathlib import Path
from urllib.request import urlopen
import time, hashlib
start=time.perf_counter()
base=Path('RESEARCH_SA23/sources');base.mkdir(exist_ok=True)
items=[('EGA0IV.pdf','https://www.numdam.org/article/PMIHES_1964__20__5_0.pdf'),('EGAIV4.pdf','https://www.numdam.org/article/PMIHES_1967__32__5_0.pdf'),('EGAIII1.pdf','https://www.numdam.org/article/PMIHES_1961__11__5_0.pdf')]
for name,url in items:
    try:
        data=urlopen(url,timeout=40).read()
        (base/name).write_bytes(data)
        print(name,len(data),hashlib.sha256(data).hexdigest(),url,flush=True)
    except Exception as e: print(name,type(e).__name__,str(e),flush=True)
print('seconds',time.perf_counter()-start)
