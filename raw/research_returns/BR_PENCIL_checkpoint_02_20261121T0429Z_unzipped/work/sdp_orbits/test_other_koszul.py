from pathlib import Path
import sys, json, math
from itertools import combinations
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'root'))
from coordinate_koszul import slices,koszul,modular_rank

cases={'j5per':[0,1,3,6,7],'j6per':[0,1,3,6,7,9]}
results=[]
for name,subset in cases.items():
 supp,ms=slices(subset,1)
 T=np.array(ms)
 j,m,_=T.shape
 print(name,subset,'shape',T.shape,flush=True)
 # Wedge in the second factor; matrix slices have rows final C and columns original A.
 trans=[T[:,i,:].T for i in range(m)]
 for p in range(m):
  cost=math.comb(m-1,p)
  upper=min(j*math.comb(m,p),m*math.comb(m,p+1))
  if (upper+cost-1)//cost < (11 if j==5 else 12):continue
  K=koszul(trans,p)
  c=modular_rank(K);bound=(c['rank_mod_p']+cost-1)//cost
  print(' p',p,'shape',K.shape,'rank',c['rank_mod_p'],'cost',cost,'bound',bound,flush=True)
  results.append({'case':name,'subset':subset,'wedge_factor':1,'p':p,'shape':list(K.shape),'cost':cost,'bound':bound,'certificate':c})
Path(__file__).with_name('other_koszul.json').write_text(json.dumps(results,indent=2)+'\n')
