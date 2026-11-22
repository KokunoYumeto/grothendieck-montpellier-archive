#!/usr/bin/env python3
"""Independent D-HOS03--06 numerical/descent certificate.

No author code or arithmetic is imported. F9 uses t^2+t+2, different
from the author's coordinate presentation. The finite descent witness is
not a substitute for the universal trace-form and fixed-space proofs.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,time
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
PEER=ROOT.parent/'g34_eightfolds'/'bireflection'
OUT=Path(__file__).resolve().parent
start=time.perf_counter()

# Rational reconstruction, with polynomial positivity at the endpoint.
d=(1-F(1,7))*(1-F(1,7**3))*(1-F(14,23))/2
assert d==F(9234,55223)>F(1,6)
assert F(37,14)**2<7
assert F(1,4)*(1-F(1,25))*(1-F(1,25**3))*F(3,4)>d
assert F(1,4)*(1-F(1,27))==F(13,54)>d
assert F(6)/(12*d-2)==F(165669,181)<916<1029
assert d<F(1,4)
x=sp.Symbol('x',nonnegative=True)
q=x+7
elliptic=sp.Poly(sp.expand((q-1)*q*q-2*(q+1)**2),x)
growth=sp.Poly(sp.expand(q*q-(q+1)),x)
assert all(c>0 for c in elliptic.all_coeffs())
assert all(c>0 for c in growth.all_coeffs())

# Independent matrix layout: paired e,f first, then the six-dimensional W.
Jw=sp.zeros(6);Jw[:3,3:]=sp.eye(3);Jw[3:,:3]=-sp.eye(3)
J=sp.diag(sp.Matrix([[0,1],[-1,0]]),Jw)
v=sp.Matrix(sp.symbols('v0:6'));w=sp.Matrix(sp.symbols('w0:6'))
z,t=sp.symbols('z t')
def H(v,z):
    M=sp.eye(8)
    M[0,2:]=(v.T*Jw)
    M[2:,1]=v
    M[0,1]=2*z
    return M
def zero(M):return all(sp.expand(u)==0 for u in M)
assert zero(H(v,z).T*J*H(v,z)-J)
assert zero(H(v,z)*H(w,t)-H(v+w,z+t+(v.T*Jw*w)[0]/2))
# A genuinely nondiagonal symplectic G: upper symmetric shear times torus.
a,b,c=sp.symbols('a b c',nonzero=True)
u0,u1,u2,u3,u4,u5=sp.symbols('u0:6')
C=sp.Matrix([[u0,u1,u2],[u1,u3,u4],[u2,u4,u5]])
G=sp.eye(6);G[:3,3:]=C
G=G*sp.diag(a,b,c,1/a,1/b,1/c)
assert zero(G.T*Jw*G-Jw)
for sign in [1,-1]:
    hh=sp.diag(sign,sign,G)
    assert zero(hh*H(v,z)-H(sign*G*v,z)*hh)

# Quadratic companion and both normalized symmetric-square actions.
k=sp.symbols('k',nonzero=True)
A=sp.Matrix([[0,k],[1,0]])
s0,s1,s2=sp.symbols('s0 s1 s2')
Cs=sp.Matrix([[s0,s1],[s1,s2]])
quadratic_ranks=[]
for mu in [k,-k]:
    image=sp.expand(A*Cs*A.T/mu)
    assert zero(A*image*A.T/mu-Cs)
    vec=sp.Matrix([image[0,0],image[0,1],image[1,1]])
    action=vec.jacobian(sp.Matrix([s0,s1,s2]))
    quadratic_ranks.append((action-sp.eye(3)).rank())
    assert (action-sp.eye(3)).rank()>0

# F9=F3[t]/(t^2+t+2), represented by a+bt with 0<=a,b<3.
def plus(u,v):return ((u%3+v%3)%3)+3*((u//3+v//3)%3)
def neg(u):return (-u%3)+3*((-(u//3))%3)
def times(u,v):
    a,b=u%3,u//3;c,d=v%3,v//3
    return (a*c+b*d)%3+3*((a*d+b*c+2*b*d)%3)
def power(u,n):
    v=1
    while n:
        if n&1:v=times(v,u)
        u=times(u,u);n//=2
    return v
def inverse(u):
    assert u
    return power(u,7)
def sig(u):return power(u,3)
def norm(u):return times(u,sig(u))
def sub(u,v):return plus(u,neg(v))
assert power(3,2)==7  # t^2=1+2t
assert all(times(u,inverse(u))==1 for u in range(1,9))
assert {norm(u) for u in range(1,9)}=={1,2}
theta=5  # 2+t has square -1 and sigma(theta)=-theta.
assert times(theta,theta)==2 and sig(theta)==neg(theta)

def mm(A,B):
    return tuple(plus(times(A[2*i],B[j]),times(A[2*i+1],B[2+j]))
                 for i in range(2) for j in range(2))
def mv(A,v):return (plus(times(A[0],v[0]),times(A[1],v[1])),
                       plus(times(A[2],v[0]),times(A[3],v[1])))
def scale(z,A):return tuple(times(z,u) for u in A)
def frob(A):return tuple(sig(u) for u in A)
def det(A):return sub(times(A[0],A[3]),times(A[1],A[2]))
def pair(v,w):return sub(times(v[0],w[1]),times(v[1],w[0]))
def va(v,w):return tuple(plus(a,b) for a,b in zip(v,w))
def vs(v,w):return tuple(sub(a,b) for a,b in zip(v,w))

vectors=list(product(range(9),repeat=2))
gl=0;cocycles=0;identities=0
center_counts={1:0,2:0}
for h in product(range(9),repeat=4):
    mu=det(h)
    if not mu:continue
    gl+=1
    sq=mm(h,frob(h))
    if sq[1]!=0 or sq[2]!=0 or sq[0]!=sq[3] or not sq[0]:continue
    central=sq[0]
    assert central in [1,2]
    assert norm(mu)==times(central,central)==1
    assert mu in {times(u,u) for u in range(1,9)}
    zz=min(u for u in range(1,9) if norm(u)==inverse(central))
    sm=scale(zz,h)
    assert mm(sm,frob(sm))==(1,0,0,1)
    mup=times(times(zz,zz),mu)
    dd=min(u for u in range(1,9) if times(sig(u),inverse(u))==mup)
    action=lambda v:mv(sm,frob(v))
    fixed=[v for v in vectors if action(v)==v]
    assert len(fixed)==9
    first=next(v for v in fixed if v!=(0,0))
    second=next(w for w in fixed if times(dd,pair(first,w))==1)
    P=(first[0],second[0],first[1],second[1])
    assert mm(sm,frob(P))==P
    assert times(dd,det(P))==1
    for v in vectors:
        sv=action(v)
        v0=scale(2,va(v,sv))
        v1=scale(inverse(times(2,theta)),vs(v,sv))
        assert action(v0)==v0 and action(v1)==v1
        assert va(v0,scale(theta,v1))==v
        identities+=1
    for v in fixed:
        for w in fixed:assert times(dd,pair(v,w)) in [0,1,2]
    center_counts[central]+=1;cocycles+=1
assert gl==5760 and cocycles>0

# Independent row-weight counts in ranks4,5,6 by F3-coordinate Frobenius.
weight_counts={}
for dim in [3,4,5]:
    fixed=sum(1 for v in product(range(9),repeat=dim) if frob(v)==v)
    assert fixed==3**dim
    weight_counts[dim]={'total':9**dim,'fixed':fixed,
                        'support_fraction':str(F(9**dim-fixed,4*9**dim))}

result={
 'status':'PASS',
 'proof_sha256':hashlib.sha256((PEER/'higher_odd_symplectic_section.tex').read_bytes()).hexdigest(),
 'scope':'independent exact constants, symbolic matrices, exhaustive F9 projective descent and weight counts; no author arithmetic imported',
 'delta_star':str(d),'degree_upper_bound':str(F(6)/(12*d-2)),
 'degree_lower_bound':1029,
 'elliptic_polynomial_coefficients':[int(v) for v in reversed(elliptic.all_coeffs())],
 'quadratic_action_moving_ranks':quadratic_ranks,
 'F9':{'GL2_matrices':gl,'projective_semilinear_cocycles':cocycles,
       'scalar_square_counts':center_counts,'vector_descent_identities':identities,
       'weight_counts':weight_counts},
 'limits':'The universal primary-space classification, all-rank descent and actual Hurwitz factorization were checked mathematically; finite examples are not substitutes.',
 'seconds':round(time.perf_counter()-start,6)
}
(OUT/'independent_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
