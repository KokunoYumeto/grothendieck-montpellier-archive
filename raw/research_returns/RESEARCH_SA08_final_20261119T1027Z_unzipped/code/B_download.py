"""Fetch primary sources used by the B investigation; preserve receipts."""
from pathlib import Path
from urllib.request import Request, urlopen
from datetime import datetime,timezone
import hashlib,json,time
base=Path(__file__).resolve().parents[1]
items=[
('B_may1970.pdf','https://www.math.uchicago.edu/~may/BOOKS/Algebraic.pdf'),
('B_steenrod_epstein1962.pdf','https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/steenrod-epstein.pdf'),
('B_pursuing_stacks_source.tar','https://arxiv.org/src/2111.01000'),
]
receipts=[]
for name,url in items:
    dest=base/'sources'/name
    t=time.monotonic()
    try:
        r=urlopen(Request(url,headers={'User-Agent':'SA08 mathematical-source-verification'}),timeout=35)
        data=r.read()
        dest.write_bytes(data)
        item={'file':name,'url':url,'bytes':len(data),'content_type':r.headers.get('Content-Type'),'sha256':hashlib.sha256(data).hexdigest(),'seconds':time.monotonic()-t}
    except Exception as e:item={'file':name,'url':url,'error':str(e),'seconds':time.monotonic()-t}
    receipts.append(item)
    print(json.dumps(item),flush=True)
(base/'logs'/'B_source_downloads.json').write_text(json.dumps(receipts,indent=2))
