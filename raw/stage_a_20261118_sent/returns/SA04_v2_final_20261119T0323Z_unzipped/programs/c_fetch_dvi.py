"""Open a public author's DVI source, preserving provenance without redistribution."""
from pathlib import Path
from urllib.request import Request,urlopen
import hashlib,subprocess
url='https://www.math.columbia.edu/~dejong/papers/ErratumTate.dvi'
p=Path('/tmp/sa04_c_primary_cache/deJongErratum.dvi')
data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 scholarly audit'}),timeout=30).read()
p.write_bytes(data)
r=subprocess.run(['dvi2tty','-w','100',str(p)],capture_output=True,text=True,check=True)
p.with_suffix('.txt').write_text(r.stdout)
print(url,'bytes',len(data),'sha256',hashlib.sha256(data).hexdigest(),'text',p.with_suffix('.txt'))
