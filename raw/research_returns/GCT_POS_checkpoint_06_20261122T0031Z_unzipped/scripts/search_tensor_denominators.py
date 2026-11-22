"""Exploratory axial-assignment vertex search; every reported mass certificate exact."""
import numpy as np, scipy.optimize as opt, itertools, fractions, math,json,time,argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--n',type=int,required=True);p.add_argument('--trials',type=int,default=10000);p.add_argument('--seed',type=int,default=20261121);p.add_argument('--out',required=True);a=p.parse_args()
n=a.n;edges=list(itertools.product(range(n),repeat=3));A=np.zeros((3*n,n**3))
for e,(i,j,k) in enumerate(edges):A[i,e]=A[n+j,e]=A[2*n+k,e]=1
rng=np.random.default_rng(a.seed);record={};start=time.time();last=time.time()
for trial in range(a.trials):
 c=rng.normal(size=n**3)
 res=opt.linprog(c,A_eq=A,b_eq=np.ones(3*n),bounds=(0,None),method='highs')
 if not res.success:raise RuntimeError(res.message)
 inds=np.flatnonzero(res.x>1e-8);m=[fractions.Fraction(float(res.x[i])).limit_denominator(1000000) for i in inds]
 if any(sum((x for i,x in zip(inds,m) if A[j,i]),fractions.Fraction())!=1 for j in range(3*n)):raise RuntimeError('certificate failure')
 den=math.lcm(*(x.denominator for x in m));v2=(den&-den).bit_length()-1
 if v2 not in record:
  es=[edges[i] for i in inds];free=all(len(set((e[d],e[f]) for e in es))==len(es) for d,f in [(0,1),(0,2),(1,2)])
  record[v2]={'trial':trial,'denominator':den,'support':es,'masses':list(map(str,m)),'free':free}
  print(json.dumps({'n':n,'trial':trial,'v2':v2,'denominator':den,'free':free}),flush=True)
 if trial%500==0:
  Path(a.out).write_text(json.dumps({'n':n,'trials_completed':trial+1,'seed':a.seed,'elapsed':time.time()-start,'records':record,'scope':'random exploratory vertices; mass balances certified exactly; not exhaustive'},indent=2))
Path(a.out).write_text(json.dumps({'n':n,'trials_completed':a.trials,'seed':a.seed,'elapsed':time.time()-start,'records':record,'scope':'random exploratory vertices; mass balances certified exactly; not exhaustive'},indent=2))
