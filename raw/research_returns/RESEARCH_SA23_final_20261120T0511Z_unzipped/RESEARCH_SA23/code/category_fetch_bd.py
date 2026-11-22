from pathlib import Path
from urllib.request import urlopen,Request
import time,hashlib,subprocess
url='https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch1.pdf'
t=time.monotonic();b=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
p=Path('RESEARCH_SA23/sources/category_BD_ch1.pdf');p.write_bytes(b)
print(url,len(b),hashlib.sha256(b).hexdigest(),time.monotonic()-t)
subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
