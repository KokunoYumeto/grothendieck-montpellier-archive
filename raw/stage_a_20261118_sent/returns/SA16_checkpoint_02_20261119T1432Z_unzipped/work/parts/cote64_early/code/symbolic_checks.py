"""Exact rational identities, multiplicities and norm signs, cote 64/064--077."""
import sympy as s
import json
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]/'outputs'
z,t,x,u,y=s.symbols('z t x u y')
A=z*z-2*z+t;B=z*z-2*t*z+t;C=z*z-t;F=t*A*A/(B*B)
assert s.expand(t*A*A-B*B-(t-1)*C*C)==0
assert s.factor(s.resultant(A,B,z))==4*t*(t-1)**2
sig=[(z-t)/(z-1),t/z,t*(z-1)/(z-t)]
for g in sig:assert s.cancel(F.subs(z,g)-F)==0
assert s.cancel(sig[0].subs(z,sig[1])-sig[2])==0
assert [s.cancel((A/B).subs(z,v)) for v in [0,1,t]]==[1,-1,-1]
assert s.limit(A/B,z,s.oo)==1
assert [s.cancel(F.subs(z,v)) for v in [0,1,t]]==[t,t,t]
assert s.limit(F,z,s.oo)==t
# Wrong and right radical substituting w^2 instead of unsafe square-root rewriting.
w=s.symbols('w')
poly=(z*z-2*t*z+t).subs(z,t+w)
wrong=s.rem(poly,s.Poly(w*w-t*(1-t),w).as_expr(),w)
right=s.rem(poly,s.Poly(w*w-t*(t-1),w).as_expr(),w)
assert s.factor(wrong)==-2*t*(t-1) and right==0
# A/B at a root zeta^2=t: leading normalization ratio = -zeta/t.
assert s.rem(s.together(A+z*B/t).as_numer_denom()[0],z*z-t,z)==0
# Degree16 homogeneous second iterate at t=2, including the point at infinity.
X,Z=s.symbols('X Z')
N=2*(X*X-2*X*Z+2*Z*Z)**2;D=(X*X-4*X*Z+2*Z*Z)**2
N2=s.expand(2*(N*N-2*N*D+2*D*D)**2)
D2=s.expand((N*N-4*N*D+2*D*D)**2)
fib=s.factor(N2-2*D2)
assert s.Poly(N2,X,Z).total_degree()==16
coef,factors=s.factor_list(fib)
assert sum(s.Poly(f,X,Z).total_degree()*m for f,m in factors)==16
assert sum(s.Poly(f,X,Z).total_degree() for f,m in factors)==10
assert s.Poly(N2,X,Z,domain=s.QQ).gcd(s.Poly(D2,X,Z,domain=s.QQ)).total_degree()==0
# Norm of y in the rank-n algebra y^n=x/u.
norms=[]
for n in range(2,9):
 M=s.zeros(n)
 for j in range(n-1):M[j+1,j]=1
 M[0,n-1]=x/u
 norm=s.factor(M.det())
 assert norm==(-1)**(n-1)*x/u
 norms.append({'n':n,'norm':str(norm)})
# Klein invariant normalization in cited earlier-run comparison.
q=z*z+z**-2;g2=-(z*z-1)**2/(4*z*z)
assert s.cancel(g2-(2-q)/4)==0
out={'assumptions':'2,t,t-1 invertible; rational identities first in Q(t,z), then integral homogeneous identities descend',
 'branch_identity':str(s.factor(t*A*A-B*B)), 'resultant_A_B':str(s.factor(s.resultant(A,B,z))),
 'invariance_under_three_Klein_maps':True,'ratio_at_0_1_infinity_t':['1','-1','1','-1'],
 'wrong_radical_substitution':str(s.factor(wrong)),'correct_radical_substitution':str(right),
 'second_iterate_at_t2':{'fiber_factorization_homogeneous':str(fib),'degree':16,'geometric_support_count':10,'factor_multiplicities':[(str(f),int(m)) for f,m in factors]},
 'norms':norms,'norm_vs_jet_factor':'(-1)^(n-1)','Klein_invariant_relation':'g2=(2-q)/4'}
(OUT/'symbolic_checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
