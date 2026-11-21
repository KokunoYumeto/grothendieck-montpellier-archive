from pathlib import Path
import tarfile,hashlib,json
root=Path('/workspace/scratch/3c0a202771c9')
dest=root/'SIGN_NEXT/work/critical_lefschetz/pu_source_cache'
class Parts:
 def __init__(self): self.i=1; self.f=(root/'lean_parts/part01').open('rb')
 def read(self,n=-1):
  out=[]; remaining=n
  while self.i<=14 and (remaining>0 or n<0):
   x=self.f.read(remaining)
   if x:
    out.append(x)
    if n>=0: remaining-=len(x)
   else:
    self.f.close(); self.i+=1
    if self.i<=14:self.f=(root/f'lean_parts/part{self.i:02d}').open('rb')
  return b''.join(out)
prefixes=['lean/src/Formalism/LocalToGlobal/HermitianForms/','lean/src/Formalism/LocalToGlobal/GroupLattices/']
manifest=[]; count=0
with tarfile.open(fileobj=Parts(),mode='r|gz') as tf:
 for m in tf:
  count+=1
  if m.isfile() and any(m.name.startswith(x) for x in prefixes):
   data=tf.extractfile(m).read();rel=m.name.removeprefix('lean/src/');p=dest/rel
   p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
   manifest.append({'path':rel,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(root/'SIGN_NEXT/work/critical_lefschetz/pu_forms_manifest.json').write_text(json.dumps(manifest,indent=2))
print({'archive_members':count,'selected_files':len(manifest),'bytes':sum(x['size'] for x in manifest)},flush=True)
