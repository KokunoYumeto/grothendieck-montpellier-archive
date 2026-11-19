#!/usr/bin/env python3
"""Exact Cartier tensor, Pfaffians and finite-field probes for ss E x E.

E/F2: y^2+y=x^3, basis (1,x,y), differential dx.
This is a certificate of identities, not a claimed monodromy computation.
"""
import itertools,json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
s=sp.symbols('s0:9')
def mod2(f):return sp.Poly(sp.expand(f),*s,modulus=2).as_expr()
def mm(A):return A.applyfunc(mod2)
x,y,z=sp.symbols('x y z')
Me=sp.Matrix([[y,x,0],[z,0,x],[0,z,y]])
R=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
Re=sp.kronecker_product(R,R)
Mc=[Me.diff(t) for t in (x,y,z)]
M=sum((s[3*i+j]*sp.kronecker_product(Mc[i],Mc[j])
       for i,j in itertools.product(range(3),repeat=2)),sp.zeros(9))
A=mm(Re*M)
S=sp.Matrix(3,3,s)
D=mod2(S.det())
assert mm(A-A.T)==sp.zeros(9)
assert all(A[i,i]==0 for i in range(9))
assert mm(A-sp.hessian(D,s))==sp.zeros(9)
assert mm(M*sp.Matrix(s))==sp.zeros(9,1)
def pf(indices):
 if not indices:return sp.Integer(1)
 i=indices[0]
 return mod2(sum(A[i,j]*pf(tuple(k for k in indices[1:] if k!=j))
                 for j in indices[1:]))
pfv=[pf(tuple(j for j in range(9) if j!=i)) for i in range(9)]
assert all(mod2(pfv[i]-D*s[i])==0 for i in range(9))
P=mod2((sp.Matrix([v*v for v in s]).T*Re*sp.Matrix(s))[0])
assert mm(sp.Matrix([sp.diff(P,v) for v in s])-Re*sp.Matrix([v*v for v in s]))==sp.zeros(9,1)
assert sp.Poly(P,*s,modulus=2).total_degree()==3
assert mod2(P.subs(dict(zip(s,(1,0,0,0,1,0,0,0,1)))))==1
assert mod2(P.subs(dict(zip(s,(0,0,0,0,1,0,0,0,1)))))==1

def rank2(rows,n=9):
 rows=rows[:];r=0
 for j in range(n):
  q=next((i for i in range(r,len(rows)) if rows[i]>>j&1),None)
  if q is None:continue
  rows[r],rows[q]=rows[q],rows[r]
  for i in range(len(rows)):
   if i!=r and rows[i]>>j&1:rows[i]^=rows[r]
  r+=1
 return r
def mul2(A,B):
 return [sum((sum((A[i]>>j&1)*(B[j]>>k&1) for j in range(len(B)))%2)<<k
             for k in range(9)) for i in range(len(A))]
Ms=[M.diff(v) for v in s]
coeff=[[[int(T[i,j]) for j in range(9)] for i in range(9)] for T in Ms]
hist={};examples=[];t=sp.symbols('t')
for sv in itertools.product(range(2),repeat=9):
 if not any(sv):continue
 vals={v:c for v,c in zip(s,sv)}
 full=sp.Matrix(9,9,lambda i,j:sum(sv[k]*coeff[k][j][i] for k in range(9))%2)
 # F=M^t. Full stable rank equals relative stable rank because F on the
 # one-dimensional full/relative quotient is zero.
 rows=[sum(int(full[i,j])<<j for j in range(9)) for i in range(9)]
 cur=rows
 for _ in range(8):cur=mul2(cur,rows)
 rank=rank2(cur);hist[rank]=hist.get(rank,0)+1
 h=int(mod2((D*D*P).subs(vals)))
 assert (rank==8)==(h==1)
 if rank==8:
  f=sp.Poly(full.charpoly(t).as_expr(),t,modulus=2).exquo(sp.Poly(t,t,modulus=2))
  if f.is_irreducible:
   cs=[int(f.nth(i))%2 for i in range(9)]
   examples.append({'section':list(sv),'relative_charpoly':str(f.as_expr()),
                    'irreducible':True,'reciprocal':cs==cs[::-1]})
out={'curve':'y^2+y=x^3 over F2','degree':1,
     'one_factor_root_removed_M':[[str(v) for v in row] for row in Me.tolist()],
     'tensor_symmetrizer':'J3 tensor J3',
     'symmetric_pencil':'Hessian(det(S)) in characteristic two',
     'pfaffian_vector':'det(S) * vec(S)',
     'determinantal_cubic':str(D),'Hermitian_cubic':str(P),
     'relative_Hasse_polynomial':'det(S)^2 * (s^[2]^t (J3 tensor J3) s)',
     'projective_F2_sections_checked':511,'stable_rank_histogram':hist,
     'irreducible_rank8_examples':examples,
     'all_assertions_passed':True,'runtime_seconds':time.perf_counter()-started}
op=Path(__file__).resolve().parents[1]/'outputs'/'supersingular_product_degree_one.json'
op.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
