from pathlib import Path
from urllib.request import urlopen,Request
import hashlib,time
u='https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-1.pdf'
p=Path('RESEARCH_SA23/sources/category_sga4_1.pdf')
t=time.perf_counter()
try:
 data=urlopen(Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=50).read();p.write_bytes(data)
 print('URL',u,'bytes',len(data),'sha256',hashlib.sha256(data).hexdigest(),'seconds',time.perf_counter()-t)
except Exception as e:print(type(e).__name__,str(e),'seconds',time.perf_counter()-t)
