"""Scalar identities quoted in the GCT VIII errata draft (P5/src/ERRATA_GCT_VIII_DRAFT.tex).
a0805369bae2ebddc (Claude Opus 5.5 at effort high), 25 Nov 2026. Checks only the scalar algebra,
not the structure constants of the algebra H_3 (those were computed by others)."""
import sympy as sp
q=sp.symbols('q',positive=True)
D=(q+1)**2/q; L=(q+1/q)**2
c=(1+q**2)**2*(q**2+q+1)*(q-1)**2/q**4
ok1=sp.simplify(L*(L-D)-c)==0
ok2=sp.simplify(L*(L-D)-(D-2)**2*(D-1)*(D-4))==0
ok3=sp.simplify(D-4-(sp.sqrt(q)-1/sp.sqrt(q))**2)==0 and sp.simplify(D-1-(q+1+1/q))==0
f=sp.expand((q+1/q)**2*(q+1+1/q))
coeffs=[f.coeff(q,k) for k in range(3,-4,-1)]
ok4=coeffs==[1,1,3,2,3,1,1] and sp.simplify(c-(sp.sqrt(q)-1/sp.sqrt(q))**2*f)==0
g=sp.expand((q+1/q)**2*(q**2+q+4+1/q+q**-2))
coeffs2=[g.coeff(q,k) for k in range(4,-5,-1)]
ok5=coeffs2==[1,1,6,3,10,3,6,1,1]
X=sp.symbols('X'); ok6=sp.expand(X*(X-D)-L*(L-D)-(X-L)*(X+L-D))==0
line=f"(errata) c = L(L-D): {ok1}; L(L-D)=(D-2)^2(D-1)(D-4): {ok2}; D-4, D-1 forms: {ok3}; f coefficients 1,1,3,2,3,1,1 and c=(q^1/2-q^-1/2)^2 f: {ok4}; other reading 1,1,6,3,10,3,6,1,1: {ok5}; factorization: {ok6}"
print(line); open('p5_checks_output.txt','a',encoding='utf-8').write(line+'\n')
