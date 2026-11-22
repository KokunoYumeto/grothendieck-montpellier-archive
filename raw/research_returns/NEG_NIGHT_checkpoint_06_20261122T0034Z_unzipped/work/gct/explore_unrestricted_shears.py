"""Exploratory even elementary basis changes, not an optimum certificate.
First checks the necessary ordinary-mass table conditions for constant
unimodular shears of the verified 2744 realization.
"""
from pathlib import Path
import json
import numpy as np

src=json.loads(Path('work/gct/dimension_certificate_2744.json').read_text())
names=['mu','Sigma']+[f'g{i}_{w}' for i in (1,2) for w in ('1','12','2','21')]
ix={s:i for i,s in enumerate(names)}
D=np.zeros((10,10,10),dtype=np.int64)
A=np.zeros_like(D)
for r in src['constants']:
    key=tuple(ix[x] for x in r['key'])
    D[key]=sum(r['dimension_q'].values())
    A[key]=sum(abs(v) for v in r['trace_q'].values())
assert int(D.sum()-A.sum())//2==2744
def shear(tab,i,j,t):
    left=tab.copy()
    left[i,:,:]=tab[i,:,:]+t*tab[j,:,:]
    both=left.copy()
    both[:,i,:]=left[:,i,:]+t*left[:,j,:]
    out=both.copy()
    out[:,:,j]=both[:,:,j]-t*both[:,:,i]
    return out
valid=[];smaller=[];attempted=0
for i in range(1,10):
 for j in range(10):
  if i==j:continue
  for t in range(-40,42,2):
   if t==0:continue
   attempted+=1
   new=shear(D,i,j,t)
   if np.any(new<A):continue
   assert np.all((new-A)%2==0)
   score=int((new-A).sum())//2
   valid.append({'i':names[i],'j':names[j],'t':t,'mass_score':score})
   if score<2744:smaller.append(valid[-1])
out={'attempted_constant_shears':attempted,
     'necessary_mass_valid':valid,'strict_improvements_in_mass_relaxation':smaller,
     'scope':'Finite exploratory basis-shear search only; no general impossibility or polynomial-character validity claimed.'}
Path('work/gct/unrestricted_shear_exploration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'attempted':attempted,'valid_mass_count':len(valid),'smaller':smaller},indent=2))
