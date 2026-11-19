#!/usr/bin/env python3
"""Exact nontrivial frame-algebra certificate for a plane-quartic family.

F=x^4+y^4+z^4+x^2yz+xz^3+txy^3+xyz^2 over F2(t).
Hasse matrix diag(1,[[0,1],[t,1]]).
The rank2 frame algebra has degree6; all six GL2(F2) actions
are verified.  Geometric irreducibility is proved in the TeX
by the equivalent AS equation u^2+u=1/(c+1).
"""
import itertools,json,time
from pathlib import Path
import sympy as sp
from sympy.polys.domains import GF
from sympy.polys.matrices import DomainMatrix

started=time.perf_counter()
t,c,d,x,y,z=sp.symbols('t c d x y z')
K=GF(2).frac_field(t)
F=x**4+y**4+z**4+x*x*y*z+x*z**3+t*x*y**3+x*y*z*z
P=sp.Poly(F,x,y,z,domain=K)
indices=[(2,1,1),(1,2,1),(1,1,2)]
H=[]
for a in indices:
 row=[]
 for b in indices:
  e=tuple(2*b[i]-a[i] for i in range(3))
  row.append(P.coeff_monomial(e) if min(e)>=0 else 0)
 H.append(row)
assert H==[[1,0,0],[0,0,1],[0,t,1]]

smooth=[]
for q in (x,y,z):
 variables=[a for a in (x,y,z) if a!=q]
 equations=[f.subs(q,1) for f in [F]+[sp.diff(F,a) for a in (x,y,z)]]
 G=sp.groebner(equations,*variables,domain=K,order='lex')
 unit=len(G.polys)==1 and G.polys[0].as_expr()==1
 assert unit
 smooth.append({'chart':str(q),'unit_singularity_ideal':unit})

f=c**3+(c+1)/t
h=d*d+c*d+c*c+1/t
G=sp.groebner([f,h],d,c,domain=K,order='lex')
def red(v):return G.reduce(sp.expand(v))[1]
assert red(t*c**4+c*c+c)==0 and red(t*d**4+d*d+d)==0
assert red(c*c*d+c*d*d+1/t)==0
assert red(t*(c*c*d+c*d*d)+1)==0
assert red((c+1)*d*d+(c+1)*c*d+c*c)==0

acts=[]
for a,b,e,f0 in itertools.product((0,1),repeat=4):
 if (a*f0+b*e)%2!=1:continue
 cc=a*c+e*d;dd=b*c+f0*d
 ok=red(f.subs(c,cc))==0 and red(h.subs({c:cc,d:dd},simultaneous=True))==0
 assert ok
 acts.append([[a,b],[e,f0]])
assert len(acts)==6

mons=[c**i*d**j for j in range(2) for i in range(3)]
def vec(v):
 Q=sp.Poly(red(v),c,d,domain=K)
 return [K.from_sympy(Q.coeff_monomial(m)) for m in mons]
theta=c+t*d
cols=[vec(theta*m) for m in mons]
M=DomainMatrix.from_list([[cols[j][i] for j in range(6)] for i in range(6)],K)
cp=M.rep.charpoly()
def field_rank(columns):
 rows=[[columns[j][i] for j in range(len(columns))] for i in range(len(columns[0]))]
 rank=0
 for j in range(len(columns)):
  pivot=next((i for i in range(rank,len(rows)) if rows[i][j]),None)
  if pivot is None:continue
  rows[rank],rows[pivot]=rows[pivot],rows[rank]
  q=rows[rank][j];rows[rank]=[a/q for a in rows[rank]]
  for i in range(len(rows)):
   if i!=rank and rows[i][j]:
    q=rows[i][j];rows[i]=[a-q*b for a,b in zip(rows[i],rows[rank])]
  rank+=1
 return rank
power=sp.Integer(1);powers=[]
for i in range(6):powers.append(vec(power));power=red(power*theta)
assert field_rank(powers)==6
T=sp.symbols('T')
charpoly=sum(K.to_sympy(a)*T**(6-i) for i,a in enumerate(cp))
check=sp.Integer(0)
for a in cp:check=red(check*theta+K.to_sympy(a))
assert check==0
num=sp.together(charpoly).as_numer_denom()[0]
num=sp.Poly(num,T,t,modulus=2).as_expr()

out={'field':'F2(t)','quartic':str(F),'Hasse_matrix':[[str(v) for v in row] for row in H],
 'smoothness_certificates':smooth,'ordinary_determinant':'t',
 'rank2_frame_equations':[str(G.polys[0].as_expr()),str(G.polys[1].as_expr())],
 'frame_dimension':6,'frame_basis':[str(m) for m in mons],
 'inverse_frame_determinant':'t','primitive_element':str(theta),
 'primitive_power_rank':6,'primitive_polynomial':str(charpoly),
 'primitive_polynomial_cleared':str(num),'all_GL2_actions':acts,
 'geometric_irreducibility_certificate':'t=(c+1)/c^3; u=d/c; u^2+u=1/(c+1), simple pole at c=1',
 'geometric_group':'diag(1,GL2(F2))','arithmetic_group':'diag(1,GL2(F2))',
 'group_order':6,'relative_rank':3,'fixed_covector_dimension':1,
 'runtime_seconds':time.perf_counter()-started}
dest=Path(__file__).resolve().parents[1]/'outputs'/'lang_frame_quartic.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
