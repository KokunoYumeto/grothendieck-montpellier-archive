#!/usr/bin/env python3
"""Fetch an explicitly selected primary URL and record its retrieval; no site crawling."""
import sys,urllib.request,subprocess,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
w=Path('/workspace/scratch/26604d0a9a98/work/cotes6_7')
name,url=sys.argv[1:3]
p=w/'outputs'/name
with urllib.request.urlopen(url,timeout=50) as r:
    data=r.read(); final=r.url
p.write_bytes(data)
event={'utc':datetime.now(timezone.utc).isoformat(),'url':url,'final_url':final,'file':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
with (w/'outputs/fetch_log.jsonl').open('a') as f:f.write(json.dumps(event)+'\n')
if p.suffix=='.pdf':
    subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
print(json.dumps(event))
