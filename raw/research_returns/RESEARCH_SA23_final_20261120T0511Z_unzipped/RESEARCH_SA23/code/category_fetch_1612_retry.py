from urllib.request import urlopen,Request
from pathlib import Path
import time,hashlib
url='https://grothendieck.umontpellier.fr/161-2.pdf'
p=Path('RESEARCH_SA23/sources/category_manuscript_161-2.pdf')
t=time.monotonic();h=hashlib.sha256();total=0
try:
 with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=90) as r,p.open('wb') as f:
  while True:
   block=r.read(1024*1024)
   if not block:break
   f.write(block);h.update(block);total+=len(block)
   if total%(5*1024*1024)==0:print('bytes',total,'seconds',time.monotonic()-t,flush=True)
 print('SAVED',url,'bytes',total,'sha256',h.hexdigest(),'seconds',time.monotonic()-t,flush=True)
except Exception as e:print('FAILED',type(e).__name__,str(e),total,'seconds',time.monotonic()-t,flush=True)
