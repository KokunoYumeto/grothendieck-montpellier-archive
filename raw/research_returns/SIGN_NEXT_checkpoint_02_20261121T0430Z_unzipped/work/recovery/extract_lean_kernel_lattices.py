from pathlib import Path
import tarfile,io,hashlib,json
root=Path(__file__).resolve().parents[3]
class Parts:
 def __init__(self):self.i=1;self.f=(root/'lean_parts/part01').open('rb')
 def read(self,n=-1):
  out=[];remaining=n
  while self.i<=14 and (remaining>0 or n<0):
   x=self.f.read(remaining)
   if x:
    out.append(x)
    if n>=0:remaining-=len(x)
   else:
    self.f.close();self.i+=1
    if self.i<=14:self.f=(root/f'lean_parts/part{self.i:02d}').open('rb')
  return b''.join(out)
prefixes=['lean/src/Formalism/LocalToGlobal/KernelLattices/','lean/src/Formalism/LocalToGlobal/KernelEntries/','lean/src/Formalism/GlobalSchurBounds/','lean/src/Formalism/DividedPowers/','lean/src/Formalism/SchurWeyl/']
dest=root/'lean_selected';dest.mkdir(exist_ok=True)
manifest=[];count=0
with tarfile.open(fileobj=Parts(),mode='r|gz') as tf:
 for m in tf:
  count+=1
  if m.isfile() and any(m.name.startswith(pre) for pre in prefixes):
   b=tf.extractfile(m).read();p=dest/m.name.removeprefix('lean/src/');p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
   manifest.append({'path':m.name.removeprefix('lean/src/'),'size':len(b),'sha256':hashlib.sha256(b).hexdigest()})
print('members',count,'selected',len(manifest),'bytes',sum(m['size'] for m in manifest),flush=True)
(root/'SIGN_NEXT/work/integral_fock/lean_kernel_lattices_manifest.json').write_text(json.dumps(manifest,indent=2))
