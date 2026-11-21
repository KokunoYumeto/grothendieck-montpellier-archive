from pathlib import Path
import sys, json, math
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'root'))
from coordinate_koszul import slices,koszul,modular_rank
rng=np.random.default_rng(11321)
results=[]
for name,subset,target in [('j5per',[0,1,3,6,7],11),('j6per',[0,1,3,6,7,9],12)]:
 supp,ms=slices(subset,1);T=np.array(ms);j,m,_=T.shape
 for d in range(3,m):
  for p in range(d):
   cost=math.comb(d-1,p)
   maxbound=(min(j*math.comb(d,p),m*math.comb(d,p+1))+cost-1)//cost
   if maxbound<target:continue
   best=0;winner=None
   for attempt in range(8):
    L=rng.integers(-2,3,size=(d,m))
    restriction=np.einsum('bi,aic->bac',L,T)
    mats=[M.T for M in restriction]
    K=koszul(mats,p);cert=modular_rank(K);rank=cert['rank_mod_p']
    bound=(rank+cost-1)//cost
    if rank>best:best=rank;winner={'case':name,'d':d,'p':p,'cost':cost,'rank':rank,'bound':bound,'L':L.tolist(),'certificate':cert}
    if bound>=target:break
   results.append(winner)
   print(name,'d',d,'p',p,'maxrank',best,'cost',cost,'bound',winner['bound'],flush=True)
Path(__file__).with_name('restricted_koszul.json').write_text(json.dumps(results,indent=2)+'\n')
