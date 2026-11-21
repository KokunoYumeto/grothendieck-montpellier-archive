#!/usr/bin/env python3
"""Exact necessary Enriquez tests in the non-normally-generated iterate target.

Only ordinary common-word membership is claimed.  Left permutation arrays are
used throughout; SymPy generates the same subgroup and tests membership.
"""
import json,pathlib,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=pathlib.Path(__file__).parent
def dis(*xs):
 out=[];off=0
 for x in xs:out.extend((np.asarray(x)+off).tolist());off+=len(x)
 return np.array(out,dtype=np.int64)
def perm(x):return Permutation(np.asarray(x).tolist())
def powp(x,n):
 if n<0:x=np.argsort(x);n=-n
 out=np.arange(len(x))
 while n:
  if n&1:out=out[x]
  x=x[x];n//=2
 return out
def induced(N,a,b):
 d=len(a);x=np.empty(N*d,dtype=np.int64);y=np.arange(N*d)
 for j in range(N):
  x[j*d:(j+1)*d]=((j+1)%N)*d+(a if j==N-1 else np.arange(d))
 y[:d]=b
 assert np.array_equal(powp(x,N)[:d],a)
 for j in range(1,N):
  q=powp(x,j)[y[powp(x,-j)]]
  assert np.array_equal(q[:d],np.arange(d))
 return x,y
def run(N,full=False):
 st=time.monotonic();data=np.load(ROOT/'cubic_descent_iterate_mod2.npz')
 R,T,X,Y=data['r'],data['t'],data['x'],data['y'];eye=np.arange(24)
 cyc=np.roll(np.arange(12),-1);i12=np.arange(12)
 a,b=(dis(R,X,X,i12),dis(T,R,Y,cyc)) if full else (dis(R,X,i12),dis(T,R,cyc))
 d=len(a);base_x,base_y=(dis(R,X,X),dis(T,R,Y)) if full else (dis(R,X),dis(T,R))
 ix,iy=induced(N,a,b)
 gx,gy=dis(ix,base_x),dis(iy,base_y)
 G=PermutationGroup([perm(gx),perm(gy)]);D=G.derived_subgroup()
 selected=list(range(d))+list(range(N*d,N*d+len(base_x)));index={v:i for i,v in enumerate(selected)}
 gens=[]
 for g in D.generators:
  assert all(g(v) in index for v in selected)
  gens.append(Permutation([index[g(v)] for v in selected]))
 J=PermutationGroup(gens)
 order=int(J.order());rows=[]
 probe=json.loads((ROOT/'cubic_descent_iterate_check.json').read_text())
 for j,row in enumerate(probe['surviving_C_values']):
  C,g=np.array(row['C']),np.array(row['g'])
  for original in (probe['original_values'] if full else [None]):
   passing=[]
   for k in (range(2*original['b'],12,4) if full else range(0,12,2)):
    if full:
     ff=np.array(original['value'])
     goal=dis(powp(T,k)[g],powp(R,k)[C],powp(Y,k)[ff],powp(cyc,k),g,C,ff)
    else:goal=dis(powp(T,k)[g],powp(R,k)[C],powp(cyc,k),g,C)
    if J.contains(perm(goal)):passing.append(k)
   rr={'C_index':j,'correction':row['correction'],'passing_c_mod12':passing}
   if full:rr['b']=original['b']
   rows.append(rr)
 out={'N':N,'projected_Fprime_order':order,'rows':rows,
      'elapsed_seconds':time.monotonic()-st,
      'scope':'Finite common-word test of both correlated targets. No actual GT lift.'}
 kind='full_' if full else ''
 (ROOT/f'cubic_descent_iterate_distribution_{kind}N{N}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 3,'--full' in sys.argv)
