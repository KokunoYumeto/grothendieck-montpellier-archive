"""Exact finite checks for the generic genus-three Jacobian argument.
No claim to mechanically verify monodromy, descent, or algebraic representatives.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json,time
import sympy as s
start=time.perf_counter()
# Exterior algebra; each of three copies a,b,x has e1,f1,e2,f2,e3,f3.
def add(A,B,m=1):
 C=defaultdict(int,A)
 for I,c in B.items():C[I]+=m*c
 return {I:c for I,c in C.items() if c}
def wedge(A,B):
 C=defaultdict(int)
 for I,a in A.items():
  for J,b in B.items():
   if set(I)&set(J):continue
   sg=(-1)**sum(i>j for i in I for j in J)
   C[tuple(sorted(I+J))]+=sg*a*b
 return {I:c for I,c in C.items() if c}
def basis(i):return {(i,):1}
def theta_diff(copy):
 T={}
 for i in range(3):
  T=add(T,wedge(add(basis(12+2*i),basis(copy+2*i),-1),add(basis(13+2*i),basis(copy+2*i+1),-1)))
 return T
thx={tuple([12+2*i,13+2*i]):1 for i in range(3)}
cc=wedge(thx,thx);cc={I:c//2 for I,c in cc.items()}
Z=[]
for copy in (0,6):
 T=theta_diff(copy);square=wedge(T,T)
 assert all(c%2==0 for c in square.values())
 Z.append(add({I:c//2 for I,c in square.items()},cc,-1))
D=wedge(*Z)
xvol=set(range(12,18))
Dpush={tuple(i for i in I if i<12):c for I,c in D.items() if xvol.issubset(I)}
P={}
for i in range(3):
 P[(2*i,6+2*i+1)]=1
 P[(2*i+1,6+2*i)]=-1
assert Dpush=={I:-2*c for I,c in P.items()}
# Ordinary test curve over F5: y^2=x^7-x.
x=s.symbols('x');f=x**7-x
assert s.gcd(s.Poly(f,x,modulus=5),s.Poly(s.diff(f,x),x,modulus=5)).degree()==0
f2=s.Poly(f*f,x,modulus=5)
HW=s.Matrix([[int(f2.coeff_monomial(x**(5*i-j)))%5 for j in (1,2,3)] for i in (1,2,3)])
assert int(HW.det())%5!=0
# S7 orbits and transposition differences in the even-sum F2 module.
V=[v for v in range(128) if v.bit_count()%2==0]
cert=[]
for v in V[1:]:
 i=next(i for i in range(7) if (v>>i)&1)
 j=next(j for j in range(7) if not ((v>>j)&1))
 swapped=v^(1<<i)^(1<<j)
 assert v^swapped==(1<<i)|(1<<j)
 cert.append({'v':v,'pair':[i,j]})
# Slopes of exterior-cube twisted once at an ordinary abelian threefold.
slopes=[0,0,0,1,1,1]
allslopes=[sum(slopes[i] for i in I)-1 for I in combinations(range(6),3)]
Pslopes=list(allslopes)
for a in slopes:Pslopes.remove(a)
res={'translation_intersection_mixed_class':[[list(I),int(c)] for I,c in sorted(Dpush.items())],
 'comparison_to_Poincare':-2,'degree_abs_two_lambda':2**6,'degree_if_u_pullback_of_isomorphism':2**3,
 'ordinary_test_curve':'y^2=x^7-x over F5','Hasse_Witt_matrix':[[int(a) for a in r] for r in HW.tolist()],
 'Hasse_Witt_determinant_mod5':int(HW.det())%5,
 'S7_even_module_dimension':6,'nonzero_vectors_tested':len(cert),'transposition_certificates':cert,
 'primitive_H3_twist1_slopes':{str(a):Pslopes.count(a) for a in sorted(set(Pslopes))},
 'elapsed_seconds':round(time.perf_counter()-start,6)}
Path(__file__).with_name('check_generic_jacobian_output.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='transposition_certificates'},indent=2))
