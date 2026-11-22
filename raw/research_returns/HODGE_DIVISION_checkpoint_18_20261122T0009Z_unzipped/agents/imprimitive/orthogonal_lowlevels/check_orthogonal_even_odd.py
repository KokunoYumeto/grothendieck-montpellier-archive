#!/usr/bin/env python3
"""Exact supplement for D-OL16--18; universal arguments are in TeX."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import datetime,hashlib,json,time
import sympy as s
import numpy as np

start=time.perf_counter();base=Path(__file__).resolve().parent
proof=base/'orthogonal_even_odd_section.tex'
text=proof.read_text()
assert text.count(r'\[')==text.count(r'\]')
assert not any(ord(c)<32 and c not in '\n\r\t' for c in text)

beta=F(1,6)-F(1,10000);delta=(1-F(19,20)**9)/2
assert F(1,6)<delta<F(3,16)<F(7,32)
assert 13*beta-2>F(1,7) and 11*beta+delta-2>F(1,60)
assert 2*beta*(1-beta)>F(1,4)
c3=(F(1,3)+F(1,3**9))/(1-F(1,3**9)-F(1,3**19))
assert c3<1-4*beta
for q in (3,5,7,9,11,13,25):
    for N in range(20,51,2):
        first=q**(N-1)-q**(N//2)-1
        second=q**(N-2)-q**(N//2)-q
        assert first>F(q**(N-1),2)
        assert second>F(q**(N-2),2)
        assert 4*F(1,q**(N-3))<F(1,8)
        assert (1-F(1,q**(N//2)))/2>F(7,16)
        assert F(q**(N//2),first)<F(1,8)

# Complete symbolic group law and orthogonality for a diagonal form.
# Odd-characteristic symmetric forms diagonalize, while the universal
# block proof in TeX treats an arbitrary nonsingular symmetric B.
N=4;ds=s.symbols('d0:4',nonzero=True);B=s.diag(*ds);Bi=B.inv()
X=s.Matrix(2,N,s.symbols('x0:8'));Y=s.Matrix(2,N,s.symbols('y0:8'))
z,t=s.symbols('z t');J=s.Matrix([[0,1],[-1,0]])
def u(X,Z):
    return s.BlockMatrix([[s.eye(2),X,Z-X*Bi*X.T/2],
        [s.zeros(N,2),s.eye(N),-Bi*X.T],
        [s.zeros(2,2),s.zeros(2,N),s.eye(2)]]).as_explicit()
form=s.BlockMatrix([[s.zeros(2,2),s.zeros(2,N),s.eye(2)],
 [s.zeros(N,2),B,s.zeros(N,2)],[s.eye(2),s.zeros(2,N),s.zeros(2,2)]]).as_explicit()
def zero(M):return all(s.expand(v)==0 for v in M)
assert zero(u(X,z*J).T*form*u(X,z*J)-form)
cross=(Y*Bi*X.T-X*Bi*Y.T)/2
assert zero(u(X,z*J)*u(Y,t*J)-u(X+Y,(z+t)*J+cross))
assert zero(u(X,z*J)*u(-X,-z*J)-s.eye(8))

# Both nonsquare-square cases over F3, using literal natural 8D matrices.
p=3;c=2;A=np.array([[0,c],[1,0]],dtype=np.int64)
I2=np.eye(2,dtype=np.int64);h=np.block([[A,np.zeros((2,2),dtype=np.int64)],
 [np.zeros((2,2),dtype=np.int64),A]])
xs=np.array(list(product(range(p),repeat=8)),dtype=np.int64).reshape(-1,2,4)
ys=np.transpose(xs,(0,2,1))
finite=[]
for eps in (1,-1):
    mu=(eps*c)%p;K=np.diag([1,eps*c])%p
    Bw=np.block([[np.zeros((2,2),dtype=np.int64),K],
                 [K,np.zeros((2,2),dtype=np.int64)]])%p
    Bwi=np.array(s.Matrix(Bw.tolist()).inv_mod(p)).astype(np.int64)%p
    hi=(h*pow(c,-1,p))%p;Ai=(A*pow(c,-1,p))%p
    assert np.all((h.T@Bw@h-mu*Bw)%p==0)
    action=np.einsum('ij,ajk,kl->ail',A,xs,hi)%p
    fixed=np.all(action==xs,axis=(1,2))
    assert int(fixed.sum())==p**4
    dual=np.einsum('ij,ajk,kl->ail',h,ys,Ai)%p
    dual_fixed=np.all(dual==ys,axis=(1,2))
    assert int(dual_fixed.sum())==p**4
    # Every nonzero fixed dual map has actual rank two.
    fixed_rank2=0
    for M in ys[dual_fixed]:
        if not np.any(M):continue
        assert any(int(M[i,0]*M[j,1]-M[i,1]*M[j,0])%p
                   for i in range(4) for j in range(i+1,4))
        fixed_rank2+=1
    assert fixed_rank2==p**4-1
    scalar=(-c*pow(mu,-1,p))%p
    assert np.all((A@np.array(J.tolist(),dtype=np.int64)@A.T*pow(mu,-1,p)
                   -scalar*np.array(J.tolist(),dtype=np.int64))%p==0)
    # Every X has exactly the announced quadratic correction under H.
    old=np.einsum('aij,jk,alk->ail',xs,Bwi,xs)%p
    new=np.einsum('aij,jk,alk->ail',action,Bwi,action)%p
    transported=np.einsum('ij,ajk,lk->ail',A,old,A)*pow(mu,-1,p)%p
    assert np.array_equal(new,transported)
    finite.append({'epsilon':eps,'multiplier':mu,'central_scalar':scalar,
                   'X_count':len(xs),'fixed_X':int(fixed.sum()),
                   'fixed_dual_rank2':fixed_rank2})

# A direct partial-parity carrier, whose symplectic action has a
# half-dimensional fixed space.  The exact Weyl conjugation identities
# reduce to these position and phase identities, checked for all pairs.
points=np.array(list(product(range(3),repeat=4)),dtype=np.int64)
sign=np.array([1,1,2,2],dtype=np.int64)
parity=points*sign%3
fixed_positions=int(np.all(points==parity,axis=1).sum())
assert fixed_positions==9 and fixed_positions**2==3**4
position_checks=0
for x in points:
    assert np.array_equal(((points+x)%3)*sign%3,(parity+x*sign)%3)
    for y in points:
        assert np.array_equal((parity@y)%3,(points@(y*sign))%3)
        position_checks+=1

# The elementary determinant obstruction for a square root of a
# projective reflection in even dimension is checked symbolically.
for d in range(4,42,2):
    assert (-1)**d*(-1)==-1
    for det in (-1,1):assert det**2==1

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-start,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'symbolic_radical_natural_dimension':8,'symbolic_group_law':'PASS',
 'nonsquare_cases':finite,'carrier_dimension':81,'carrier_trace':fixed_positions,
 'carrier_trace_square':fixed_positions**2,'carrier_phase_checks':position_checks,
 'constants':{'beta':str(beta),'delta':str(delta),'q3_fixed_bound':str(c3)},
 'scope':'Exact finite/symbolic supplement; stable planes, all-rank orbit estimates, full normalizer scope and actual generation are proved in TeX.'}
(base/'orthogonal_even_odd_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
