from pathlib import Path
from urllib.request import urlopen,Request
import hashlib,time,subprocess
url='https://math.bu.edu/people/jsweinst/AWS/Files/TatePDivisibleGroups.pdf'
t=time.monotonic()
try:
 b=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
 assert b.startswith(b'%PDF')
 p=Path('RESEARCH_SA23/sources/category_Tate1967.pdf');p.write_bytes(b)
 print(url,len(b),hashlib.sha256(b).hexdigest(),time.monotonic()-t)
 subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
except Exception as e:print(type(e).__name__,str(e),'seconds',time.monotonic()-t)
