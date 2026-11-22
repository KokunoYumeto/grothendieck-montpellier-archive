"""Exact mixed-character rank-four cancellation sequences in finite cyclotomic rings."""
from pathlib import Path
from itertools import product
from time import perf_counter
import numpy as np
import json
start=perf_counter();runs=[]
for p in (3,5,7):
 e=p-1;mod=p*p;n=4
 eye=np.eye(n,dtype=np.int64);zero=np.zeros((n,n),dtype=np.int64)
 Aeye=np.zeros((e,n,n),dtype=np.int64);Aeye[0]=eye
 I=(Aeye,zero)
 def mul(x,y):
  A,B=x[0],y[0]
  c=np.zeros((2*e-1,n,n),dtype=np.int64)
  for i in range(e):
   for j in range(e):c[i+j]+=A[i]@B[j]
  for j in range(2*e-2,e-1,-1):
   top=c[j].copy();c[j]=0
   for i in range(e):c[j-e+i]-=top
  nil=(sum(A)%p@y[1]+x[1]@(sum(B)%p))%p
  return c[:e]%mod,nil
 def power(T,a):
  B=I
  for _ in range(a):B=mul(B,T)
  return B
 def same(A,B):return np.array_equal(A[0],B[0]) and np.array_equal(A[1],B[1])
 def zcoeff(a):
  a%=p
  v=np.zeros(e,dtype=np.int64)
  if a<e:v[a]=1
  else:v[:]=-1
  return v%mod
 Ss=[np.zeros((2,2),dtype=np.int64)]
 coeffs=range(1,p) if p==3 else (1,)
 for i,j,c in product(range(2),range(2),coeffs):
  S=np.zeros((2,2),dtype=np.int64);S[i,j]=c;Ss.append(S)
 cases=actions=0
 for a,b in product(range(p),repeat=2):
  Base=np.zeros((e,n,n),dtype=np.int64)
  Base[:,0,0]=zcoeff(a);Base[:,1,1]=zcoeff(b)
  Base[:,2,2]=zcoeff(a+1);Base[:,3,3]=zcoeff(b+1)
  Base[0,0,2]=1;Base[0,1,3]=1
  for S in Ss:
   nil=np.zeros((n,n),dtype=np.int64);nil[:2,:2]=S
   Ts=(Base,nil)
   assert same(power(Ts,p),I);actions+=1
   for T in Ss:
    pn=np.zeros((n,n),dtype=np.int64);pn[2:,:2]=(T-S)%p
    P=(Aeye,pn);Pi=(Aeye,-pn%p)
    assert same(mul(P,Pi),I)
    en=np.zeros((n,n),dtype=np.int64);en[:2,:2]=T;en[2:,2:]=(S-T)%p
    assert same(mul(mul(Pi,Ts),P),(Base,en))
    cases+=1
 runs.append({'p':p,'all_ordered_character_pairs':p*p,
              'nil_matrices_in_stated_basis_sample':len(Ss),'rank_four_order_p_actions':actions,
              'rank_four_exact_sequences':cases})
report={'status':'PASS','scope':'Actual finite cyclotomic semidirect-ring matrix multiplication; all ordered pairs of characters, stated nil-matrix basis samples, order-p powers, inverse free-basis changes and triangular quotient identities. Trace reduction is the written additivity/flag proof.',
        'runs':runs,'total_actions':sum(r['rank_four_order_p_actions'] for r in runs),
        'total_exact_sequences':sum(r['rank_four_exact_sequences'] for r in runs),
        'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_cyclotomic_matrix.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
