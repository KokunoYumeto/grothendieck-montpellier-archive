"""Ordinary downloads of publicly linked primary sources; no credentials or bypasses."""
from pathlib import Path
import urllib.request,hashlib,json
targets=[('sga7_original.pdf','https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf'),('sga5_original.pdf','https://wstein.org/sga/sga5/SGA5.pdf')]
out=Path('work/p2_primary');out.mkdir(parents=True,exist_ok=True)
for name,url in targets:
 if (out/name).exists():
  print(json.dumps({'file':name,'status':'existing successful download reused'}));continue
 try:
  with urllib.request.urlopen(url,timeout=25) as r: data=r.read()
  (out/name).write_bytes(data)
  print(json.dumps({'file':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}))
 except Exception as e:print(json.dumps({'file':name,'url':url,'error':str(e)}))
