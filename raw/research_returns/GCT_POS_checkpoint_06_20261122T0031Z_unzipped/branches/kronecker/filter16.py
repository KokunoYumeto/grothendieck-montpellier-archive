from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
import json,time,sys
p=Path(__file__).resolve().parent
target=int(sys.argv[1]);start=time.time();counts=Counter();good=[]
lines=(p/f'm16_chi{target}_spectra.txt').read_text().splitlines()
fout=(p/f'm16_chi{target}_certificates.jsonl').open('w')
for idx,line in enumerate(lines):
 v=list(map(int,line.split()));W=[v[i:i+4] for i in (0,4,8)];sets=[sorted(set(X)) for X in W]; mult=[Counter(X) for X in W]
 E=[e for e in product(*sets) if sum(e)%16==0];rows=[(j,v) for j in range(3) for v in sets[j]]
 mat=[[int(e[j]==v) for e in E] for j,v in rows];rhs=[mult[j][v] for j,v in rows]
 aeq=np.array(mat,dtype=float);beq=np.array(rhs,dtype=float)
 dual=linprog(beq,A_ub=-aeq.T,b_ub=np.zeros(len(E)),bounds=[(-1,1)]*len(rows),method='highs')
 assert dual.success,(idx,dual.message)
 if dual.fun < -1e-8:
  y=[Fraction(float(a)).limit_denominator(10**6) for a in dual.x]
  assert all(sum(y[i]*mat[i][j] for i in range(len(rows)))>=0 for j in range(len(E)))
  assert sum(y[i]*rhs[i] for i in range(len(rows)))<0
  counts['negative']+=1
  fout.write(json.dumps({'W':W,'y':[str(a) for a in y]},separators=(',',':'))+'\n')
 else:
  cvec=np.zeros(len(E)+1);cvec[-1]=-1
  primal=linprog(cvec,A_ub=np.c_[-np.eye(len(E)),np.ones(len(E))],b_ub=np.zeros(len(E)),A_eq=np.c_[aeq,np.zeros(len(rows))],b_eq=beq,bounds=[(0,None)]*(len(E)+1),method='highs')
  assert primal.success
  x=[Fraction(float(a)).limit_denominator(10**6) for a in primal.x[:-1]]
  assert all(a>=0 for a in x)
  assert all(sum(mat[i][j]*x[j] for j in range(len(E)))==rhs[i] for i in range(len(rows)))
  rec={'W':W,'E':E,'x':[str(a) for a in x],'strict':all(a>0 for a in x)};good.append(rec)
  counts['positive']+=1
  fout.write(json.dumps(rec,separators=(',',':'))+'\n')
  print('POSITIVE',target,rec,flush=True)
 if idx%5000==0: print(target,idx,'/',len(lines),dict(counts),'seconds',round(time.time()-start,2),flush=True)
fout.close()
obj={'target_character_order':target,'modulus':16,'counts':dict(counts),'feasible':good,'seconds':time.time()-start}
(p/f'm16_chi{target}_result.json').write_text(json.dumps(obj,indent=2));print(json.dumps(obj),flush=True)
