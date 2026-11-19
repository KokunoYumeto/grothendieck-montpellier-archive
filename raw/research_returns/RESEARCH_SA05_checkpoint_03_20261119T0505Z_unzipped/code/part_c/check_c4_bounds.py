"""Exact finite checks for C.4 optimization and Legendre monodromy.
These verify algebra/combinatorics only, not alteration, purity, or Chow theorems.
"""
from pathlib import Path
import json,time
import sympy as sp
start=time.perf_counter();checks=0
# Enumerate every possible proper-cohomology constituent on the E2 page.
for n in range(0,13):
 for eps in (0,1):
  if eps and n==0: continue
  for i in range(0,2*n+4):
   LL=max(0,i-n+eps);UU=min(i,n)
   possible=[]
   for q in range(n+1):
    a=i-q;d=n-eps if q==0 else n-q
    if a<0 or d<0:continue
    for t in range(max(0,a-d),a//2+1):
     for r in range(a-2*t+1):
      w=r+2*(t+q)
      assert 2*LL<=w<=2*UU,(n,eps,i,q,a,d,r,t,w)
      assert r<=min(w-2*LL,2*UU-w),(n,eps,i,q,r,t,w)
      possible.append((r,w));checks+=1
   if possible:
    expect=min(i,2*n-eps-i)
    assert max(x[0] for x in possible)==expect,(n,eps,i,expect,possible)
   else:
    assert i>2*n-eps,(n,eps,i)
# Coefficient substitution and the two closed forms.
for n in range(1,16):
 for j in range(11):
  for eps in (0,1):
   for i in range(2*n+j+3):
    LL=max(0,i-n+eps);UU=min(i,n)+j
    assert UU-LL==min(i,2*n-eps-i)+j
    assert min(i+j,n+j)==min(i,n)+j
    assert max(0,(i+j)-(n+j)+eps)==LL
    checks+=3
# Legendre integral Weierstrass discriminant, c4 and split node at t=0 over F5.
t=sp.symbols('t');a2=-(1+t);a4=t
b2=4*a2;b4=2*a4;b6=0;b8=-a4**2
Delta=sp.expand(-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6)
c4=sp.expand(b2*b2-24*b4)
assert sp.expand(Delta-16*t*t*(1-t)**2)==0
assert sp.expand(c4-16*(1-t+t*t))==0
assert [x for x in range(5) if (x*x+1)%5==0]==[2,3]
monodromy=[]
for j in range(0,31):
 N=sp.zeros(j+1);Phi=sp.diag(*[sp.Integer(5)**r for r in range(j+1)])
 for r in range(1,j+1):N[r-1,r]=r
 assert N.rank()==j
 assert Phi*N*Phi.inv()==N/5
 # im N is span e0,...,e(j-1); quotient is e_j, Tate(-1) multiplies by 5.
 image_span=sp.Matrix.hstack(*[N[:,r] for r in range(1,j+1)]) if j else sp.zeros(1,0)
 assert image_span.rank()==j
 monodromy.append({'j':j,'rank_N':j,'coinvariant_dimension':1,'H1_inertia_frobenius_eigenvalue':str(5**(j+1)),'weight':2*j+2})
# Exact definitions test: generic point of trait has trdeg0 + closure dimension1.
dimension_tests=[{'map':'Spec K -> Spec DVR','source_Krull_dimension':0,'relative_fibre_dimension':0,'delta_dimension_n':0+1}]
out={'status':'all checks passed','scope':'finite optimization ranges n<=15,j<=30 and polynomial/linear-algebra checks only','optimization_checks':checks,'legendre_discriminant':str(sp.factor(Delta)),'legendre_c4':str(c4),'split_node_slopes_mod5':[2,3],'monodromy':monodromy,'dimension_tests':dimension_tests,'runtime_seconds':round(time.perf_counter()-start,6)}
path=Path(__file__).with_name('check_c4_bounds_output.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='monodromy'},indent=2))
