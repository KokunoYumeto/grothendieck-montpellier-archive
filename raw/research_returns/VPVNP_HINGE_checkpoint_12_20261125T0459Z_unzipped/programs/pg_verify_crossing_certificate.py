#!/usr/bin/env python3
"""Independent exact verification of the n4 crossing-projector certificate.
Rebuilds only the certified 16-vector Gram and projector matrix elements,
using the elementary character sign(pi)*(fixed_points(pi)-1), without
Murnaghan--Nakayama, conjugacy-orbit enumeration, or floating arithmetic.
"""
import itertools,json,sys
from pathlib import Path
import sympy as s
src=Path(sys.argv[1]);out=Path(sys.argv[2]);d=json.loads(src.read_text())
n=d['n'];q=d['q'];assert(n,q)==(4,2)
perms=list(itertools.permutations(range(n)));ident=tuple(range(n))
def mul(p,r):return tuple(p[r[j]] for j in range(n))
def inv(p):return tuple(p.index(j) for j in range(n))
def cyc(p):
 seen=set();z=0
 for a in range(n):
  if a in seen:continue
  z+=1
  while a not in seen:seen.add(a);a=p[a]
 return z
def conj(g,p):return mul(mul(g,p),inv(g))
def ker(a,b):return q**(cyc(mul(inv(a[0]),b[0]))+cyc(mul(inv(a[1]),b[1])) )
reps=[tuple(map(tuple,r)) for r in d['basis_orbit_representatives']]
from functools import lru_cache
@lru_cache(None)
def avg(i,a,b):
 return s.Rational(sum(ker(reps[i],(conj(g,a),conj(g,b))) for g in perms),24)
G=s.Matrix([[avg(i,*v) for v in reps] for i in range(len(reps))])
parse=lambda name:s.Matrix([[s.Rational(x) for x in row] for row in d[name]])
assert G==parse('gram') and G==G.T and G.det()>0
# Sylvester criterion is an exact positive-definiteness check.
assert all(G[:j,:j].det()>0 for j in range(1,G.rows+1))
for typ,name in [('AB','projector_AB'),('AD','projector_AD')]:
 P=parse(name)
 E=s.zeros(G.rows)
 for i in range(G.rows):
  for j,(a,b) in enumerate(reps):
   val=0
   for p in perms:
    chi=(-1)**(n-cyc(p))*(sum(p[k]==k for k in range(n))-1)
    z=(mul(p,a),mul(p,b)) if typ=='AB' else(mul(p,a),mul(b,inv(p)))
    val+=3*chi*avg(i,*z)/24
   E[i,j]=val
 assert E==G*P and P*P==P and G*P==P.T*G,typ
h=s.Matrix([q**(cyc(a)+cyc(b)) for a,b in reps]);assert h==parse('psi_inner_products')
v=parse('common_projection_coordinates');Pb=parse('projector_AB');Pc=parse('projector_AD')
assert Pb*v==v and Pc*v==v
eta=(h.T*v)[0];assert eta==18==(v.T*G*v)[0]
result={'status':'PASS','arithmetic':'exact rational','matrix_dimension':G.rows,'rebuilt_projectors_from_character':'sgn(pi)*(number_of_fixed_points(pi)-1)','gram_positive_definite':True,'projector_idempotent_and_self_adjoint':True,'common_projection_squared_norm':str(eta),'raw_endpoint_lower_bound':'2^(3/2)','scope':'This is NOT a price certificate; it is a finite Schur-copy lower bound before semiring regularization.'}
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
