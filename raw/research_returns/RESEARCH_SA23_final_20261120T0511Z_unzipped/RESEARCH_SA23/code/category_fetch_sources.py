from pathlib import Path
from urllib.request import urlopen, Request
import hashlib, time
items = [('kisin_2006.dvi','https://people.math.harvard.edu/~kisin/dvifiles/wam.dvi')]
for name,url in items:
    start=time.perf_counter()
    try:
        data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
        p=Path('RESEARCH_SA23/sources')/name;p.write_bytes(data)
        print(name,len(data),hashlib.sha256(data).hexdigest(),'seconds',time.perf_counter()-start)
    except Exception as e: print(name,type(e).__name__,str(e))
