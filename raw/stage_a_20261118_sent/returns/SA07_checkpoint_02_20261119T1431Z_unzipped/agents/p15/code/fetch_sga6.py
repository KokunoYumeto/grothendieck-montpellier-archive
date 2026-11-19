from pathlib import Path
import urllib.request
url='https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf'
dest=Path('/workspace/scratch/9c0c54a66f6c/agents/p15/evidence/SGA6_original.pdf')
try:
 data=urllib.request.urlopen(url,timeout=55).read()
 dest.write_bytes(data)
 print(url,len(data),data[:5],flush=True)
except Exception as e: print(type(e).__name__,str(e),flush=True)
