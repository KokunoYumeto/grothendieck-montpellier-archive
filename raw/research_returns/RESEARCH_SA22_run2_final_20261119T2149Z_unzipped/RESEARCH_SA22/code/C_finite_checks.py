#!/usr/bin/env python3
"""Exact finite certificates for Part C. Standard-library only."""
from fractions import Fraction as Q
from itertools import permutations, combinations
import json,time
start=time.perf_counter()
out={}

def conv(f,g,mul):
 n=len(f);h=[0]*n
 for a in range(n):
  for b in range(n):h[mul(a,b)]+=f[a]*g[b]
 return h

def characteristic(n,s):return [int(i in s) for i in range(n)]
def cyclic(n):return lambda a,b:(a+b)%n

def circle_system(n):
 m=n//2
 E=[set(x%n for x in range(-i,i+1)) for i in range(m)]
 E.append(set(range(n)))
 A=lambda t:[{(t+x)%n for x in s} for s in E]
 rho=lambda t:(2*t)%n
 ker=[t for t in range(n) if rho(t)==0]
 checks={'chain':0,'reflection':0,'cone':0,'kernel_covariance':0,'alignment':0}
 tables=[]
 for t in range(n):
  fam=A(t)
  assert all(fam[i]<=fam[i+1] for i in range(len(fam)-1));checks['chain']+=1
  for a in fam:
   assert a=={(rho(t)-x)%n for x in a};checks['reflection']+=1
  for k in ker:
   assert A((k+t)%n)==[{(k+x)%n for x in a} for a in fam];checks['kernel_covariance']+=1
  for u in range(n):
   s=(t-u)%n
   union=fam+[{(s+x)%n for x in b} for b in A(u)]
   assert all(a<=b or b<=a for a in union for b in union);checks['alignment']+=1
   for i,a in enumerate(fam):
    for j,b in enumerate(A(u)):
     h=conv(characteristic(n,a),characteristic(n,b),cyclic(n))
     c=(t+u)%n
     radial=[h[(c+r)%n] for r in range(m+1)]
     coeff=[radial[r]-radial[r+1] for r in range(m)]+[radial[m]]
     assert all(x>=0 for x in coeff)
     reconstructed=[sum(coef*(x in aset) for coef,aset in zip(coeff,A(c))) for x in range(n)]
     assert reconstructed==h;checks['cone']+=1
     if t==u==0 and i<=j:tables.append({'i':i,'j':j,'coeff':coeff})
 return {'n':n,'kernel':ker,'sets_at_zero':[sorted(x) for x in E],'checks':checks,'cone_coefficients':tables}

out['cyclic_axioms']=[circle_system(n) for n in [6,9]]
for n in [6,9]:
 a=characteristic(n,{0,1,n-1});h=characteristic(n,{0,n//3,2*n//3})
 aa=conv(a,a,cyclic(n));hh=conv(h,h,cyclic(n))
 aaa=conv(aa,a,cyclic(n));hhh=conv(hh,h,cyclic(n))
 assert max(aaa)==7 and max(hhh)==9
 out[f'C{n}_K_counterexample']={'interval':a,'subgroup':h,'square_interval':aa,'square_subgroup':hh,'cube_interval':aaa,'cube_subgroup':hhh,'maxima':[max(aaa),max(hhh)]}

# S3: multiplication p*q means p after q.
G=list(permutations(range(3)));index={g:i for i,g in enumerate(G)}
e=index[(0,1,2)]
mul=lambda a,b:index[tuple(G[a][G[b][j]] for j in range(3))]
a=index[(1,0,2)];s=index[(1,2,0)]
H={e,a};Hs={mul(h,s) for h in H}
f=characteristic(6,H);g=characteristic(6,Hs)
fg=conv(f,g,mul);gf=conv(g,f,mul)
assert max(fg)==2 and max(gf)==1
pairs=0
for A in combinations(range(6),2):
 for B in combinations(range(6),2):
  v=sorted(conv(characteristic(6,A),characteristic(6,B),mul),reverse=True)
  w=sorted(fg,reverse=True)
  assert all(sum(v[:k])<=sum(w[:k]) for k in range(1,7));pairs+=1
out['S3_asymmetry']={'elements':[list(x) for x in G],'H':sorted(H),'s':s,'Hs':sorted(Hs),'f*g':fg,'g*f':gf,'pair_rearrangements_checked':pairs,'all_f*g_majorizes':True}

# Exact matrices for finite-dimensional algebra counterexamples.
U=[[Q(1),Q(0)],[Q(0),Q(2)]]
D=[[Q(0),Q(0),Q(0)],[Q(0),Q(1),Q(0)],[Q(0),Q(0),Q(2)]]
mm=lambda a,b:[[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
N=[[U[i][j]-Q(i==j) for j in range(2)] for i in range(2)]
assert mm(N,N)==N
assert mm(D,D)[1][1]==1
out['finite_dimensional_algebras']={'U_on_Qeps2':[[str(v) for v in row] for row in U],'U_minus_I_idempotent_nonzero':True,'D_on_Qeps3':[[str(v) for v in row] for row in D],'D^2_eps_equals_eps':True}
# Formal differential-functor obstruction on R=Q[eps]/eps^2.
# Basis (1,eps,deps) of R plus Omega_R.
scalar_eps=[[Q(0),Q(0),Q(0)],[Q(1),Q(0),Q(0)],[Q(0),Q(0),Q(0)]]
shear=[[Q(1),Q(0),Q(0)],[Q(0),Q(1),Q(0)],[Q(1),Q(0),Q(1)]]
S=[[shear[i][j]-Q(i==j) for j in range(3)] for i in range(3)]
assert mm(S,S)==[[Q(0)]*3 for _ in range(3)]
assert mm(shear,scalar_eps)==mm(scalar_eps,shear)
assert S[2][0]==1 and all(x==0 for x in scalar_eps[2])
out['formal_functor_obstruction']={'scalar_eps':[[str(v) for v in row] for row in scalar_eps],'rho_eps':[[str(v) for v in row] for row in shear],'R_linear':True,'rho_minus_I_square_zero':True,'image_not_contained_in_eps_M':True}
out['runtime_seconds']=round(time.perf_counter()-start,6)
print(json.dumps(out,indent=2))
