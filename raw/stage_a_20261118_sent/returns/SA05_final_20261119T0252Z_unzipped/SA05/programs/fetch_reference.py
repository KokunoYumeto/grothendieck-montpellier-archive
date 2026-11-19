#!/usr/bin/env python3
"""Fetch an already identified public primary source for targeted text reading.
The copyrighted source cache is excluded from deliverable ZIPs.
"""
import sys,json,urllib.request,hashlib,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2]
name,url=sys.argv[1:3]
cache=root/'evidence_cache';cache.mkdir(exist_ok=True)
out=cache/(name+'.pdf')
r={'name':name,'url':url}
try:
    if not out.exists():
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=25) as src: out.write_bytes(src.read())
    data=out.read_bytes()
    if not data.startswith(b'%PDF'): raise ValueError('response is not a PDF')
    txt=out.with_suffix('.txt')
    p=subprocess.run(['pdftotext','-layout',str(out),str(txt)],capture_output=True,text=True)
    r.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),returncode=p.returncode,text_path=str(txt),stderr=p.stderr)
except Exception as e:r['error']=str(e)
target=Path(__file__).resolve().parent/'outputs'/('fetch_'+name+'.json')
target.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
