from pathlib import Path
from urllib.request import Request,urlopen
import time,hashlib,json
base=Path(__file__).resolve().parents[1]
u='https://grothendieck.umontpellier.fr/136.pdf'
p=base/'sources'/'B_original_cote136.pdf'
t=time.monotonic();h=hashlib.sha256();total=0
with urlopen(Request(u,headers={'User-Agent':'SA08 source verification'}),timeout=55) as r,p.open('wb') as out:
    while True:
        chunk=r.read(1<<20)
        if not chunk:break
        out.write(chunk);h.update(chunk);total+=len(chunk)
        if total%(32<<20)==0:print('downloaded',total,flush=True)
receipt={'url':u,'path':str(p),'bytes':total,'sha256':h.hexdigest(),'seconds':time.monotonic()-t}
print(json.dumps(receipt),flush=True)
(base/'logs'/'B_cote136_receipt.json').write_text(json.dumps(receipt,indent=2))
