from pathlib import Path
import sys,json,time,math
from itertools import combinations
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'root'))
from coordinate_koszul import slices,koszul,modular_rank
x=json.load(open(Path(__file__).resolve().parents[1]/'root/j7_target14.json'))
subsets=[s for s in x['per_unresolved'] if s in [[0,1,3,6,7,9,18],[0,1,3,6,7,18,21]]]
allrec=[];st=time.time()
for subset in subsets:
 support,mats=slices(subset,1);T=np.stack(mats);m=len(support)
 for k in range(2,m):
  target=14-m+k
  minlower=100;fails=[];rankdata=[]
  for S in combinations(range(m),k):
   M=[T[:,i,:] for i in S]
   lower=max(modular_rank(np.stack(M).reshape(k,-1))['rank_mod_p'],modular_rank(np.stack(M).transpose(1,0,2).reshape(7,-1))['rank_mod_p'],modular_rank(np.stack(M).transpose(2,0,1).reshape(m,-1))['rank_mod_p'])
   ranks=[]
   for p in range(1,k//2+1):
    if lower>=target:break
    r=modular_rank(koszul(M,p))['rank_mod_p'];cost=math.comb(k-1,p)
    lower=max(lower,(r+cost-1)//cost);ranks.append([p,r,cost])
   minlower=min(minlower,lower)
   if lower<target:fails.append(list(S))
   rankdata.append({'S':list(S),'lower':lower,'ranks':ranks})
  rec={'subset':subset,'k':k,'target':target,'minimum_certified':minlower,'unresolved':fails,'records':rankdata};allrec.append(rec)
  print({a:v for a,v in rec.items() if a not in ['records','unresolved']},'unresolved',len(fails),fails[:4],flush=True)
Path(__file__).with_name('j7_secondary_substitution_probe.json').write_text(json.dumps({'records':allrec,'seconds':time.time()-st},indent=2)+'\n')
