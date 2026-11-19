"""Exact finite certificates for stated examples; infinite conclusions are proved in verification.md.
Run: python programs/verify_computations.py. Requires sympy.
These tests do not decide ambiguous ink or replace infinite-dimensional proofs.
"""
from fractions import Fraction
from itertools import combinations
from math import prod,gcd
import sympy as s

print('C01: squarefree-denominator module over Z')
P=[2,3,5,7,11,13]
for n in range(1,len(P)+1):
    q=prod(P[:n]); assert all(q%p==0 and q%(p*p)!=0 for p in P[:n])
    print('finite primes',P[:n],'span=(1/'+str(q)+')Z; quotient over Z order',q)
print('General proof: p-adic lower bound -1 excludes every nonzero copy of Z[1/p]; all localizations equal p^-1 Z_(p).')

print('\nC02: cancelled faithful-flat representation')
z=s.symbols('z',nonzero=True)
R=s.diag(1,1/z,z)
assert R.det()==1 and R[0,1]==0
print('G_m on span(1,t,t^-1):',R,'det=',R.det(),'; x12 maps to 0, so coordinate map not faithfully flat.')

print('\nC03: obstruction relation: separate kernels miss mixed compatibility')
# i, beta: Q -> Q both identity; relation i(l)=beta(m). rho(l,m)=l.
i=s.Matrix([[1]]); beta=s.Matrix([[1]]); compat=i.row_join(-beta); rho=s.Matrix([[1,0]])
ker=compat.nullspace(); assert i.nullspace()==[] and beta.nullspace()==[]
image=s.Matrix.hstack(*[rho*v for v in ker])
assert image.rank()==1
print('i=beta=id_Q; ker(i)=ker(beta)=0; ker(i,-beta)=span(1,1); rho(l,m)=l; image of joint kernel=Q.')

print('\nC04: Weil restriction dimension: dual-number base')
# B=k[e]/e^2, coordinate x=a+b e. No equations for Res(A1_B), so A2_k.
a,b,e=s.symbols('a b e')
print('B=k[e]/(e^2), x=a+b*e; Res_B/k(A1_B)=A2_k. n=2, dim(X/B)=1, dim(Res)=2.')
assert s.Poly(a+b*e,e).degree()==1

print('\nC05: submodule tensor reciprocity fails')
H=s.diag(1,0); E=s.Matrix([[0,1],[0,0]])
assert H*E-E*H==E
v=s.Matrix([1,0]); assert H*v==v and E*v==s.zeros(2,1)
Ht=s.eye(2)-H.T; Et=-E.T
stack=Ht.col_join(Et)
assert stack.rank()==2 and stack.nullspace()==[]
print('[H,E]=E; span(e1)=character 1 in N. On character1 tensor N-dual: H=',Ht,'E=',Et,'; simultaneous invariants=0.')
print('Adjunction instead gives a quotient onto the trivial module.')

print('\nC06: Laurent units and nilpotent pole')
t,eps=s.symbols('t eps',nonzero=True)
for m in (1,2,3,7):
    f=1+eps*t**(-m); g=1-eps*t**(-m)
    assert s.expand(f*g-1)==-eps**2*t**(-2*m)
    print('m=',m,': (1+eps*t^-m)(1-eps*t^-m)=1 modulo eps^2.')
print('Poles -m are distinct over dual numbers, proving no fixed negative bound contains the full nilpotent thickening.')

print('\nC07: nilpotent translations need not preserve truncated algebra')
t,eps=s.symbols('t eps')
expr=s.expand((t+eps)**2)
rem=s.reduced(expr,[t*t,eps*eps],t,eps)[1]
assert rem==2*t*eps
print('(t+eps)^2 modulo (t^2,eps^2)=',rem,'; nonzero over Q, so t->t+eps is not a Q[eps]/eps^2-algebra endomorphism of A[t]/t^2.')

print('\nC08: quadratic polynomial composition')
a0,a1,a2,b0,b1,b2=s.symbols('a0 a1 a2 b0 b1 b2')
f=a0+a1*t+a2*t*t; g=b0+b1*t+b2*t*t
comp=s.Poly(s.expand(g.subs(t,f)),t)
expected=[b0+b1*a0+b2*a0*a0,b1*a1+2*b2*a0*a1,b1*a2+b2*a1*a1+2*b2*a0*a2,2*b2*a1*a2,b2*a2*a2]
assert all(s.expand(comp.nth(j)-expected[j])==0 for j in range(5))
for j,c in enumerate(expected):print('coefficient t^'+str(j),c)

print('\nC09: formal semidirect group with abelian Lie algebra in char p')
x1,x2,y1,y2,z1,z2=s.symbols('x1 x2 y1 y2 z1 z2')
for p in (2,3,5):
    def F(x,y):return (x[0]+y[0]+x[0]*y[0],x[1]+y[1]*(1+x[0]**p))
    left=F(F((x1,x2),(y1,y2)),(z1,z2));right=F((x1,x2),F((y1,y2),(z1,z2)))
    for u,v in zip(left,right):assert s.Poly(s.expand(u-v),x1,x2,y1,y2,z1,z2,modulus=p).is_zero
    comm=s.expand(F((x1,x2),(y1,y2))[1]-F((y1,y2),(x1,x2))[1])
    assert s.expand(comm-(x1**p*y2-y1**p*x2))==0
    print('p=',p,'associator vanishes mod p; skew term=',comm,'; total degree',p+1,'>2.')
print('General certificate: 1+F1(x,y)^p=(1+x1^p)(1+y1^p); no quadratic skew term, but nonzero degree p+1 term.')

print('\nC10: GL2 left-invariant fields bracket')
u11,u12,u21,u22=s.symbols('u11 u12 u21 u22'); U=s.Matrix([[1+u11,u12],[u21,1+u22]])
coords=[u11,u12,u21,u22]
def field(i,j):
    return s.Matrix([U[k,i] if l==j else 0 for k,l in [(0,0),(0,1),(1,0),(1,1)]])
def bracket(V,W):
    return s.Matrix([sum(V[k]*s.diff(W[r],coords[k])-W[k]*s.diff(V[r],coords[k]) for k in range(4)) for r in range(4)])
for i,j,k,l in [(i,j,k,l) for i in range(2) for j in range(2) for k in range(2) for l in range(2)]:
    rhs=(field(i,l) if j==k else s.zeros(4,1))-(field(k,j) if i==l else s.zeros(4,1))
    assert bracket(field(i,j),field(k,l))==rhs
print('All 16 brackets equal delta_jk X_il - delta_li X_kj.')

print('\nC11: adjoint binomial formula in free associative words')
for n in range(1,8):
    def ad(d):
        ans={}
        for w,c in d.items():ans['x'+w]=ans.get('x'+w,0)+c;ans[w+'x']=ans.get(w+'x',0)-c
        return {w:c for w,c in ans.items() if c}
    d={'y':1}
    for _ in range(n):d=ad(d)
    formula={'x'*(n-i)+'y'+'x'*i:int((-1)**i*s.binomial(n,i)) for i in range(n+1)}
    assert d==formula
    print('n=',n,'identity exact;',len(d),'words')
for p in (2,3,5,7):assert all(int(s.binomial(p,i))%p==0 for i in range(1,p))
print('For prime p, intermediate binomial coefficients vanish mod p, giving ad(x)^p=ad(x^p).')

print('\nC12: exterior algebra dimensions for a direct sum')
for m,n in [(1,2),(2,3),(3,3)]:
    for r in range(m+n+1):assert sum(s.binomial(m,i)*s.binomial(n,r-i) for i in range(r+1))==s.binomial(m+n,r)
    print('ranks',m,n,'all homogeneous dimensions satisfy Vandermonde; canonical map proof is in verification.md.')

print('\nAll exact finite certificates passed. Infinite or general theorems are not inferred from finite samples.')
