#!/usr/bin/env python3
"""Finite checks for Part B. No computational claim about Chow nonvanishing."""
from itertools import product
from time import perf_counter
import json
from pathlib import Path
import sympy as s

started=perf_counter()
x=s.symbols('x0:5')
exponents=[a for a in product(range(6),repeat=5) if sum(a)==5]
allowed=[a for a in exponents if sum(a[2:])>0 and a[0]+a[1]+a[4]>0]
assert len(exponents)==126 and len(allowed)==114
F=x[0]**4*x[2]+x[0]*x[2]**4+x[1]**4*x[3]+x[1]*x[3]**4+x[4]**5
assert F.subs({x[2]:0,x[3]:0,x[4]:0})==0
assert F.subs({x[0]:0,x[1]:0,x[4]:0})==0
derivatives=[s.diff(F,v) for v in x]
charts=[]
for i in range(5):
    gens=[v for j,v in enumerate(x) if i!=j]
    equations=[p.subs(x[i],1) for p in derivatives]
    G=s.groebner(equations,*gens,domain=s.QQ)
    assert list(G)==[1]
    charts.append({'chart':str(x[i])+'=1','groebner_basis':[str(p) for p in G]})
a,b=s.symbols('a b')
square=s.Poly((a+b)**2,a,b)
surviving=sum(c*a**i*b**j for (i,j),c in square.terms() if i<2 and j<2)
assert surviving==2*a*b
Q=s.diag(1,0)
assert Q.rank()==1 and Q.nullspace()==[s.Matrix([0,1])]
lam,t=s.symbols('lambda t')
u=s.symbols('u')
hasse=s.Poly(u*(u-1)*(u-lam),u).coeff_monomial(u**2)
assert s.Poly(hasse.subs(lam,2+t),t,modulus=3).as_expr()==-t
A7,B7=s.symbols('A7 B7')
hasse7=s.Poly((u**3+A7*u+B7)**3,u).coeff_monomial(u**6)
assert s.expand(hasse7)==3*B7
disc7=[int((4*(-1)**3+27*c*c)%7) for c in [0,1]]
assert disc7==[3,2]
U=s.Matrix([1,0,1,0]);V=s.Matrix([1,0,0,1])
X=s.Matrix([0,1,0,1]);Y=s.Matrix([0,1,1,0])
toric=s.Matrix.hstack(U,V,X,Y)
assert toric.rank()==3 and U+X==V+Y
n=s.symbols('n',integer=True,nonnegative=True)
en=n*X-U-(n+1)*V
assert en==s.Matrix([-n-2,n,-1,-1])
assert en+U==n*X-(n+1)*V
assert en+V==n*Y-(n+1)*U
assert en+X==(n+1)*Y-(n+2)*U
assert en+Y==(n+1)*X-(n+2)*V
result={
 'scope':'B.1(c) quintic monomial count, containment and smoothness; B.2 square; B.1(b) radical; B.3.3/B.3.16 Hasse coefficients; SGA2 counterexample monomial identities',
 'not_verified':'Nontriviality modulo rational or algebraic equivalence is proved geometrically in the manuscript, not by this computation.',
 'quintic_monomials':len(exponents),'monomials_vanishing_on_both_lines':len(allowed),
 'F0':str(F),'partial_derivatives':[str(p) for p in derivatives],
 'smoothness_affine_charts_over_Q':charts,'square_mod_a2_b2':str(surviving),
 'radical_model':{'matrix':str(Q),'rank':Q.rank(),'kernel':[str(v) for v in Q.nullspace()]},
 'legendre_hasse_p3':str(hasse),'legendre_hasse_at_lambda_2_plus_t_mod3':str(s.Poly(hasse.subs(lam,2+t),t,modulus=3).as_expr()),
 'elliptic_p7_hasse_coefficient':str(hasse7),'elliptic_p7_discriminants_without_minus16':disc7,
 'sga2_toric_exponent_rank':toric.rank(),'sga2_socle_exponents':[str(v) for v in en],
 'sga2_socle_symbolic_annihilator_identities':True,
 'elapsed_seconds':perf_counter()-started,
}
out=Path(__file__).with_name('part_b_finite_checks_output.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
