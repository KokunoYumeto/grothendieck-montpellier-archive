import importlib.util,time,json
from pathlib import Path
from collections import Counter
s=importlib.util.spec_from_file_location('m',Path(__file__).with_name('A_cosimplicial_pd_cotangent.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def rankmod_sparse(cols,p):
 piv={}
 for col in cols:
  d={r:v%p for r,v in col.items() if v%p}
  while d:
   r=min(d);a=d[r]
   if r not in piv:
    inv=pow(a,-1,p);piv[r]={j:v*inv%p for j,v in d.items()};break
   for j,v in piv[r].items():
    z=(d.get(j,0)-a*v)%p
    if z:d[j]=z
    elif j in d:del d[j]
 return len(piv)
def sparse(W, max_n, verbose=False):
 start=time.perf_counter();BB={};D={}
 for n in range(max_n+1):
  BB[n]=[(a,t) for a in range(2) for t in m.bases(n,W-a) if m.wt(t)+a==W and m.nondeg(t)] if n else []
  if verbose:print('basis',W,n,len(BB[n]),time.perf_counter()-start,flush=True)
  if n:
   rows={x:i for i,x in enumerate(BB[n-1])};cols=[]
   for a,t in BB[n]:
    col={}
    for b,c,v in m.first(t):
     if a+b<2 and (a+b,c) in rows:
      row=rows[(a+b,c)];col[row]=col.get(row,0)+v
    for k in range(n-1):
     v,c=m.collapse(t,k)
     if (a,c) in rows:
      row=rows[(a,c)];col[row]=col.get(row,0)+(-1)**(k+1)*v
    cols.append({r:v for r,v in col.items() if v})
   D[n]=cols
 return BB,D
if __name__=='__main__':
 start=time.perf_counter()
 B,D=sparse(9,5)
 d2checks=0
 for n in range(2,6):
  for col in D[n]:
   result=Counter()
   for j,v in col.items():
    for k,a in D[n-1][j].items():result[k]+=v*a
   assert all(v==0 for v in result.values())
   d2checks+=1
 ranks={p:{n:rankmod_sparse(cols,p) for n,cols in D.items()} for p in [3,101]}
 assert [len(B[n]) for n in range(1,6)]==[2,48,497,2417,6018]
 assert [ranks[3][n] for n in range(2,6)]==[2,46,450,1966]
 assert [ranks[101][n] for n in range(2,6)]==[2,46,451,1966]
 a=((m.LEAF,1),);b=((m.LEAF,2),);c=((m.LEAF,3),)
 v=m.normalize(Counter({a:1,b:1}))
 alpha=((v,3),)
 beta=m.normalize(Counter({((a,3),):1,((b,3),):1}))
 gamma=m.normalize(Counter({((c,1),):1,((c,2),):1}))
 indices=[B[3].index((0,x)) for x in [alpha,beta,gamma]]
 cycle=dict(zip(indices,[1,-6,9]))
 bd=Counter()
 for j,vv in cycle.items():
  for k,cc in D[3][j].items():bd[k]+=vv*cc
 assert all(vv==0 for vv in bd.values())
 detector=indices[0]
 assert all(col.get(detector,0)%3==0 for col in D[4])
 assert cycle[detector]%3==1
 ans={'passed':True,'weight':9,'scope':'R_2 relative special PD cotangent, degrees 1 through 5',
      'dimensions':{n:len(v) for n,v in B.items()},'ranks':ranks,
      'homology_mod_p':{p:{n:len(B[n])-r[n]-r[n+1] for n in range(1,5)} for p,r in ranks.items()},
      'integer_d_squared_columns_checked':d2checks,
      'cycle':cycle,'cycle_words':{i:m.pretty(B[3][i][1]) for i in cycle},
      'detector':{'index':detector,'modulus':3,'degree4_columns_checked':len(D[4])},
      'basis':{n:[('T*' if aa else '')+m.pretty(t) for aa,t in bb] for n,bb in B.items()},
      'sparse_integer_differential_columns':D,'runtime_seconds':time.perf_counter()-start}
 dest=Path(__file__).resolve().parents[1]/'logs'/'A_cosimplicial_pd_slope.json'
 dest.write_text(json.dumps(ans,indent=2)+'\n')
 print(json.dumps({k:v for k,v in ans.items() if k not in ['basis','sparse_integer_differential_columns']},indent=2))
