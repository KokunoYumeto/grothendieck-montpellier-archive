"""Public-primary-source fallback for PDFs exceeding web reader limits.
Cache is outside the deliverable; stdout records provenance, not copyrighted text.
"""
from pathlib import Path
from urllib.request import urlopen, Request
import hashlib, subprocess, sys
name,url=sys.argv[1:]
cache=Path('/tmp/sa04_c_primary_cache');cache.mkdir(exist_ok=True)
p=cache/(name+'.pdf')
data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 scholarly audit'}),timeout=45).read()
assert data.startswith(b'%PDF'), data[:80]
p.write_bytes(data)
subprocess.run(['pdftotext','-layout',str(p),str(cache/(name+'.txt'))],check=True)
print(name,url,'bytes',len(data),'sha256',hashlib.sha256(data).hexdigest(),'text_cache',cache/(name+'.txt'))
