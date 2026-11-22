"""Exact finite/algebraic checks for the actual primitive double-cover counterexamples.

This does not replace the geometric smooth-member, global-generation, sheaf,
or Galois-equivariance proofs. Every executed output is retained unchanged.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import permutations
from collections import Counter
from math import factorial, comb
import json, time, traceback
import sympy as s

OUT=Path(__file__).with_suffix('.output.json')
assert not OUT.exists(), 'Preserve previous executed output'
start=time.perf_counter();counts={}

def rank2(cols,n):
 basis={}
 for x in cols:
  while x:
   i=x.bit_length()-1
   if i in basis:x^=basis[i]
   else:basis[i]=x;break
 return len(basis)

def mat_apply(cols,x):
 z=0
 for i,c in enumerate(cols):
  if (x>>i)&1:z^=c
 return z

def run():
 X,Y,Z=s.symbols('X Y Z')
 cubic=s.Poly(Y**2*Z+Y*Z**2+X**3,X,Y,Z,modulus=2)
 derivatives=[cubic.diff(v).as_expr() for v in (X,Y,Z)]
 assert derivatives==[X**2,Z**2,Y**2]
 assert cubic.eval({X:0,Y:1,Z:0})==0
 assert derivatives[2].subs({X:0,Y:1,Z:0})==1
 # The three partials have common zero only at the affine cone origin,
 # so the projective cubic has no singular point over any extension field.
 m,a=s.symbols('m a',integer=True)
 intersection=s.Matrix([[0,1,1],[1,0,1],[1,1,0]])
 coeff=s.Matrix([m,1,1]);v=s.Matrix([1,0,0]);l0=s.Matrix([0,1,1])
 assert s.expand((coeff.T*intersection*coeff)[0])==4*m+2
 assert (coeff.T*intersection*v)[0]==2
 assert s.expand(((l0-a*v).T*intersection*(l0-a*v))[0])==2-4*a
 pol=s.Matrix([[m+1,1],[1,2]])
 U=s.Matrix([[1,0],[-2,1]])
 C=s.Matrix([[0,1],[1,0]])*s.Matrix([[1,-m-1],[0,1]])
 assert U.det()==1 and C.det()==-1
 assert s.simplify(U*pol*C)==s.diag(1,-2*m-1)
 assert pol.det()==2*m+1
 counts['symbolic_curve_partial_checks']=5
 counts['symbolic_intersection_and_Smith_checks']=7

 rows=[];vectors=0;actions=0
 for n in (3,5,7,11,13,17):
  mm=(n-1)//2;P=pol.subs(m,mm)
  assert P.det()==n and (U*P*C.subs(m,mm))==s.diag(1,-n)
  assert s.Rational(1,2)-mm<0
  mask=(1<<n)-1;last=1<<(n-1);hist=Counter()
  for x in range(1,last):
   weight=min(x.bit_count(),n-x.bit_count())
   hist[weight]+=1;vectors+=1
   for i in range(n-1):
    z=x
    if ((x>>i)^(x>>(i+1)))&1:z^=(1<<i)|(1<<(i+1))
    if z&last:z^=mask
    assert 0<z<last
    assert min(z.bit_count(),n-z.bit_count())==weight
    actions+=1
  expected={j:comb(n,j) for j in range(1,(n-1)//2+1)}
  assert dict(hist)==expected
  assert sum(hist.values())==(1<<(n-1))-1
  gl=1
  for j in range(n-1):gl*=2**(n-1)-2**j
  assert factorial(n)<=gl and (n==3 or factorial(n)<gl)
  rows.append({'n':n,'m':mm,'polarization_matrix':[list(map(int,row)) for row in P.tolist()],
   'L_square':4*mm+2,'fibre_degree':2,'generic_genus':n+1,
   'generic_rank_using_proved_geometric_theorem':n-1,
   'permutation_order_bound':factorial(n),'full_linear_order':gl,
   'invariant_subcover_sizes':expected,'strict_nonfull_counterexample':n>=5})
 counts['quotient_nonzero_vectors']=vectors
 counts['adjacent_transposition_vector_checks']=actions

 n=5;perms=list(permutations(range(n)));mask=(1<<(n-1))-1
 matrices={}
 for perm in perms:
  cols=tuple((1<<perm[i]) if perm[i]<n-1 else mask for i in range(n-1))
  assert rank2(cols,n-1)==n-1
  matrices[perm]=cols
 assert len(set(matrices.values()))==120
 pairs=0
 for pi in perms:
  for rho in perms:
   composed=tuple(pi[rho[i]] for i in range(n))
   product=tuple(mat_apply(matrices[pi],c) for c in matrices[rho])
   assert product==matrices[composed]
   pairs+=1
 counts['faithful_S5_matrices']=len(matrices)
 counts['all_S5_multiplication_pairs']=pairs
 assert rows[1]['full_linear_order']==20160
 assert rows[1]['invariant_subcover_sizes']=={1:5,2:10}
 return {'projective_cubic':str(cubic.as_expr()),'partials':[str(d) for d in derivatives],
  'symbolic_polarization_matrix':str(pol),'explicit_Smith_left':str(U),
  'explicit_Smith_right':str(C),'symbolic_Smith_diagonal':str(U*pol*C),
  'rows':rows,'scope':'Exact explicit-curve smoothness, universal intersection/Smith identities, faithful S5 matrix multiplication and exhaustive invariant-subset cardinalities for the certified primes. Ampleness, global generation, generic rank, the wild branch sheaf sequence, and actual monodromy identification are separately proved in the text; they are not inferred from this computation.'}

try:
 result=run();record={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
  'runtime_seconds':time.perf_counter()-start,'counts':counts,**result}
except Exception:
 record={'status':'FAIL','actual_utc':datetime.now(timezone.utc).isoformat(),
  'runtime_seconds':time.perf_counter()-start,'counts':counts,'traceback':traceback.format_exc()}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if record['status']!='PASS':raise SystemExit(1)
