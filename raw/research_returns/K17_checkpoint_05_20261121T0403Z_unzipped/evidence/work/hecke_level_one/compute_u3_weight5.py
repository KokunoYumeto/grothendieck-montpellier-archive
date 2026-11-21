"""Exploratory exact Hecke calculation, not yet an arithmetic coverage theorem.

Standard Eisenstein Hermitian lattice, maximal lattice level, weight (5,0,-5).
Every matrix and neighbor is checked with exact integer arithmetic.
The representation/transfer and source-level comparisons are separate gates.
"""
from pathlib import Path
from itertools import product,permutations
from collections import defaultdict
import json, math
import sympy as sp

OUT=Path(__file__).resolve().parent

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return (a*c-b*d,a*d+b*c-b*d)
def conj(x):return (x[0]-x[1],-x[1])
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def smul(x,v):return tuple(mul(x,y) for y in v)
def dot(u,v):
 z=(0,0)
 for x,y in zip(u,v):z=add(z,mul(conj(x),y))
 return z
UNITS=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
def phase(v):return min(smul(z,v) for z in UNITS)
def line(v,p,root):
 w=tuple((a+b*root)%p for a,b in v)
 if not any(w):return (0,0,0)
 z=pow(next(a for a in w if a),-1,p)
 return tuple(a*z%p for a in w)
def det3(cols):
 a,b,c=cols
 return add(sub(mul(a[0],sub(mul(b[1],c[2]),mul(b[2],c[1]))),mul(a[1],sub(mul(b[0],c[2]),mul(b[2],c[0])))),mul(a[2],sub(mul(b[0],c[1]),mul(b[1],c[0]))))

x=sp.symbols('x:3')
parts=[t for t in product(range(6),repeat=3) if sum(t)==5 and t[0]>=t[1]>=t[2]]
mon=[sum(sp.prod(x[i]**t[i] for i in range(3)) for t in set(permutations(s))) for s in parts]
lower=[t for t in product(range(5),repeat=3) if sum(t)==4]
lap=[sp.Poly(sum(x[i]*sp.diff(f,x[i],2)+sp.diff(f,x[i]) for i in range(3)),*x) for f in mon]
A=sp.Matrix([[g.coeff_monomial(t) for g in lap] for t in lower])
ns=A.nullspace();assert len(ns)==1
c=ns[0];den=sp.ilcm(*[a.q for a in c]);c=[int(a*den) for a in c]
g=math.gcd(*c);c=[a//g for a in c]
f=sp.Poly(sum(a*b for a,b in zip(c,mon)),*x)
assert sum(x[i]*sp.diff(f.as_expr(),x[i],2)+sp.diff(f.as_expr(),x[i]) for i in range(3)).expand()==0
f1=int(f.eval({x[0]:1,x[1]:0,x[2]:0}));assert f1
def feval(n):return sum(int(co)*math.prod(n[i]**t[i] for i in range(3)) for t,co in f.terms())

def calc(p,pi):
 assert norm(pi)==p
 root=(-pi[0]*pow(pi[1],-1,p))%p
 B=math.ceil(2*math.sqrt(p/3))+1
 by=defaultdict(list)
 for a,b in product(range(-B,B+1),repeat=2):
  n=norm((a,b))
  if n<=p:by[n].append((a,b))
 allv=set()
 for i in range(p+1):
  for j in range(p-i+1):
   k=p-i-j
   for v in product(by[i],by[j],by[k]):allv.add(phase(v))
 classes=defaultdict(list)
 for v in sorted(allv):classes[line(v,p,root)].append(v)
 zero=classes.pop((0,0,0))
 # Enumerate Fp lines directly.
 lines=set()
 for v in product(range(p),repeat=3):
  if not any(v):continue
  z=pow(next(a for a in v if a),-1,p);lines.add(tuple(a*z%p for a in v))
 assert set(classes)==lines and len(lines)==p*p+p+1
 records=[];total=0
 for ell in sorted(lines):
  basis=list(classes[ell])
  # A zero reduction vector is pi times a coordinate unit; its inclusion is
  # decided by orthogonality against the nonzero reduction vectors.
  for v in zero:
   if all(dot(v,w)==(0,0) for w in basis):basis.append(v)
  assert len(basis)==3,(p,ell,len(basis))
  assert all(dot(u,v)==((p,0) if i==j else (0,0)) for i,u in enumerate(basis) for j,v in enumerate(basis))
  d=det3(basis);assert norm(d)==p**3
  # Rank one modulo pi plus unitary Gram ensures the desired elementary divisors.
  assert {line(v,p,root) for v in basis}<={ell,(0,0,0)}
  vals=[norm(v[0]) for v in basis]
  assert sum(vals)==p
  fv=feval(vals);total+=fv
  records.append({'line':ell,'columns':basis,'determinant':d,'first_row_norms':vals,'polynomial_value':fv})
 assert total%f1==0
 return {'p':p,'pi':pi,'norm_vectors_up_to_units':len(allv),'neighbor_count':len(records),'scaled_trace':total//f1,'unscaled_eigenvalue':str(sp.Rational(total,f1*p**5)),'evaluation_point':p**12+p**6+1,'evaluation_difference':p**12+p**6+1-total//f1,'neighbors':records}

if __name__=='__main__':
 result={'status':'EXPLORATORY arithmetic comparison not verified','weight':[5,0,-5],'harmonic_polynomial':str(f.as_expr()),'f_at_100':f1,'coefficients':list(zip(parts,c)),'results':[]}
 for p,pi in [(7,(3,1)),(13,(4,1))]:
  r=calc(p,pi);result['results'].append(r)
  print({k:v for k,v in r.items() if k!='neighbors'},flush=True)
 result['gcd']=math.gcd(*(r['evaluation_difference'] for r in result['results']))
 (OUT/'u3_weight5_exact_exploration.json').write_text(json.dumps(result,indent=2))
 print('gcd',result['gcd'],'f',f.as_expr())
