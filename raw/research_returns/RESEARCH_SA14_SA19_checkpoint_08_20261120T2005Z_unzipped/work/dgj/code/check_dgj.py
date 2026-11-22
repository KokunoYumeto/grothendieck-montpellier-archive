#!/usr/bin/env python3
"""Finite and symbolic certificates for D/G/J. No external data required."""
import itertools, json, time
from pathlib import Path
import sympy as s

start=time.perf_counter()
out={}

# D: integral endomorphism-matrix identities, with f a commuting symbol.
f=s.symbols('f')
g=s.Matrix([[-1,f],[0,1]])
h=-s.eye(2)
out['involution']={'g_squared':str(g*g),'commutator':str(g*h-h*g)}

# The Weierstrass family y^2+t*x*y+y=x^3 has discriminant 1+t^3 mod 2.
t,z=s.symbols('t z')
a1,a2,a3,a4,a6=t,0,1,0,0
b2=a1*a1+4*a2; b4=2*a4+a1*a3; b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
disc=s.Poly(-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6,t,modulus=2).as_expr()
out['elliptic_discriminant']=str(disc)

# Formal parameter z=x/y, w=1/y satisfies w+t*z*w+w^2=z^3.
# All arithmetic is in F_2[t][[z]], truncated at a fixed precision.
prec=18
def tr(x):
    x=s.Poly(s.expand(x),z,t,modulus=2)
    return s.expand(sum(int(c)%2*z**i*t**j for (i,j),c in x.terms() if i<prec))
w=0
for _ in range(prec):w=tr(z**3+t*z*w+w*w)
D=tr(w*(t*z+w)); N=tr(z*z+t*w)
num=tr(w*D*N*(N+t*D))
den=tr(w*N*(N+t*D)**2+(1+w)*D**3+N*z*D**2)
num=tr(num/z**9); den=tr(den/z**9)
assert s.Poly(den,z).coeff_monomial(1)==1
inv=1
for _ in range(prec): inv=tr(1+(1+den)*inv)
double=tr(num*inv)
double4=sum(c*z**i for (i,),c in s.Poly(double,z).terms() if i<4)
assert s.Poly(double4-t*z*z,t,z,modulus=2).is_zero
out['formal_double_mod_z4']=str(double4)
out['H_local_ring']='F_2[[t]][z]/(z^4,t*z^2)'
out['H_fibre_lengths']={'generic':2,'special':4}
out['V4_fixed_group_lengths']={'generic':8,'special':16}
out['cyclic_shear_delta']={'F_ordinary':-1,'V_ordinary':1,'F_supersingular':0,'V_supersingular':0}

# G: all quadratic refinements q=q0+linear in dimensions up to six.
def bit(v,i):return (v>>i)&1
def pairing(v,w,r):
    return sum(bit(v,2*i)*bit(w,2*i+1)+bit(v,2*i+1)*bit(w,2*i) for i in range(r))%2
def quadratic(v,ell,r):
    return (sum(bit(v,2*i)*bit(v,2*i+1) for i in range(r))+(v&ell).bit_count())%2
rows=[]
for r,rad in [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2),(3,0)]:
    n=2*r+rad; points=range(1<<n); good=[]
    for ell in points:
        q=lambda v:quadratic(v,ell,r)
        ok=True
        for v in points:
            if not any(pairing(v,w,r) for w in points):continue
            if any(q(w^(v if pairing(w,v,r) else 0))!=q(w) for w in points):
                ok=False;break
        # GL(rad,2) elementary changes, keeping the symplectic part fixed.
        if ok:
            for i in range(2*r,n):
                for j in range(2*r,n):
                    if i!=j and any(q(w^((1<<i) if bit(w,j) else 0))!=q(w) for w in points):
                        ok=False
        if ok:good.append(ell)
    rows.append({'symplectic_rank':2*r,'radical_dimension':rad,'fixed_refinements':len(good),'linear_parts':good})
out['quadratic_refinements']=rows

# J: cup-intersection matrix of P1 x P1, and diagonal/anti-diagonal tests.
Q=s.Matrix([[0,1],[1,0]])
P=s.Matrix([[1,1],[1,-1]])
out['J_intersection']={'Q':[[int(x) for x in row] for row in Q.tolist()],'determinant':int(Q.det()),'signed_basis':[[int(x) for x in row] for row in (P.T*Q*P).tolist()],'eigenvalues':{str(k):int(v) for k,v in Q.eigenvals().items()}}
# Explicit smooth elliptic curve over F3: y^2*z=x^3-x*z^2.
sing=[]
for x,y,zz in itertools.product(range(3),repeat=3):
    if (x,y,zz)==(0,0,0):continue
    F=(y*y*zz-x**3+x*zz*zz)%3
    grad=(zz*zz%3,2*y*zz%3,(y*y+2*x*zz)%3)
    if F==0 and grad==(0,0,0):sing.append((x,y,zz))
assert not sing
out['E_over_F3']={'equation':'y^2*z=x^3-x*z^2','projective_singular_points':sing,'geometric_smoothness_reason':'F_x=z^2 forces z=0; F=-x^3 then forces x=0; F_z=y^2 then forces y=0.'}
out['runtime_seconds']=round(time.perf_counter()-start,6)
dest=Path(__file__).with_name('check_dgj_output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
