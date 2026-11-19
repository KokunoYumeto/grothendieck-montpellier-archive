"""Normal downloads of explicitly opened primary PDF URLs."""
from pathlib import Path
import urllib.request,hashlib,json,subprocess
out=Path('work/p2_primary');out.mkdir(parents=True,exist_ok=True)
targets=[('sga4_tome3_original.pdf','https://publications.ias.edu/sites/default/files/Number4.pdf'),('weil2_original.pdf','https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf'),('bbd_original.pdf','https://www.numdam.org/item/AST_1982__100__1_0.pdf')]
for name,url in targets:
 try:
  if not (out/name).exists():
   with urllib.request.urlopen(url,timeout=25) as r: data=r.read()
   (out/name).write_bytes(data)
  data=(out/name).read_bytes()
  print(json.dumps({'file':str(out/name),'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}),flush=True)
  subprocess.run(['pdftotext','-layout',str(out/name),str(out/name.replace('.pdf','.txt'))],check=True)
 except Exception as e:print(json.dumps({'file':name,'url':url,'error':str(e)}),flush=True)
