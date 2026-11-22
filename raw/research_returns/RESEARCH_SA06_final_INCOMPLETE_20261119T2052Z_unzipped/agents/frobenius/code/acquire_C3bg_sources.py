"""Reproduce the primary downloads used in C.3bg; each execution records fresh timing/hash."""
from pathlib import Path
from urllib.request import urlopen, Request
from datetime import datetime, timezone
import time, hashlib, json, subprocess
base=Path(__file__).resolve().parents[1]; records=[]
for name,url in [('hacon_patakfalvi2014v2','https://arxiv.org/pdf/1310.2996v2'),('brion_coherent2012v2','https://arxiv.org/pdf/1204.2628v2')]:
 rec={'name':name,'url':url,'started_utc':datetime.now(timezone.utc).isoformat()};start=time.perf_counter()
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:
   data=response.read();rec.update(status_code=response.status,bytes=len(data))
  if data.startswith(b'%PDF'):
   pdf=base/'sources'/(name+'.pdf');pdf.write_bytes(data);rec['sha256']=hashlib.sha256(data).hexdigest()
   sub=subprocess.run(['pdftotext','-layout',str(pdf),str(pdf.with_suffix('.txt'))],capture_output=True,text=True);rec['pdftotext_returncode']=sub.returncode
  else:rec['error']='No PDF retrieved'
 except Exception as e:rec['error']=str(e)
 rec['runtime_seconds']=time.perf_counter()-start;records.append(rec)
(base/'output'/'C3bg_source_acquisition.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
