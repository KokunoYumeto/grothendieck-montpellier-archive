#!/usr/bin/env python3
"""Exact arithmetic and finite symbolic checks for D-OC2-02--04.

The universal arguments are in the proof.  The F27 test is an independent
finite witness for the characteristic-equals-Galois-order descent step;
it is not represented as a proof for all finite fields.
"""
from pathlib import Path
from fractions import Fraction as Q
import itertools, json, hashlib, time
import sympy as s

B=Path(__file__).resolve().parent
start=time.monotonic()
x,q=s.symbols('x q')
def positive_at(poly,n,strict=True):
    cs=s.Poly(s.expand(poly.subs(q,n+x)),x).all_coeffs()
    assert all(c>=0 for c in cs)
    if strict: assert cs[-1]>0
    return [str(c) for c in reversed(cs)]
polys={
 'elliptic_vs_inner':positive_at(q*q-4*q-1,7),
 'heisenberg_vs_inner':positive_at(q**3-4,7),
 'large_q_degree_vs_selfdual_budget':positive_at(q**3-5*q*q-49*q+5,11),
 'nonselfdual_budget_at_most_21_over_2':positive_at(9*q-63,7,False),
}
assert Q(1,2)*(1-Q(1,3))*(1-Q(1,9))==Q(8,27)>Q(1,4)
endpoints={}
for v in (7,9):
    degree=Q(v*v-1,2); budget=Q(24*v,v-5)
    assert degree**2>budget
    endpoints[str(v)]={'degree_floor':str(degree),'selfdual_budget':str(budget),
                      'two_factor_degree':str(degree**2)}
assert Q(7*(7-1)**2,2)==126>84
assert Q(9*(9-1)**2,2)==288>54

# Universal polynomial matrix identities for the symplectic line radical.
v1,v2,w1,w2,z,t=s.symbols('v1 v2 w1 w2 z t')
J=s.Matrix([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]])
def heis(a,b,c):
    return s.Matrix([[1,-b,a,2*c],[0,1,0,a],[0,0,1,b],[0,0,0,1]])
H=heis(v1,v2,z)
assert s.simplify(H.T*J*H-J)==s.zeros(4)
assert s.simplify(H*heis(w1,w2,t)-heis(v1+w1,v2+w2,z+t+(v1*w2-v2*w1)/2))==s.zeros(4)
a,b,c=s.symbols('a b c')
Jstd=s.Matrix([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])
shear=s.eye(4);shear[0,2]=a;shear[0,3]=b;shear[1,2]=b;shear[1,3]=c
assert shear.T*Jstd*shear==Jstd
A=s.Matrix([[0,-1],[1,0]])
S=s.Matrix([[a,b],[b,c]])
assert s.expand((A*S*A.T+S)[0,1])==0
assert A*s.diag(1,-1)*A.T==-s.diag(1,-1)

# F27 = F3[t]/(t^3-t-1), represented by base-three coefficient triples.
digits=[(i%3,(i//3)%3,i//9) for i in range(27)]
def encode(v):return sum((v[i]%3)*3**i for i in range(3))
add=[[encode([a[k]+b[k] for k in range(3)]) for b in digits] for a in digits]
neg=[encode([-c for c in a]) for a in digits]
def mul0(a,b):
    r=[0]*5
    for i in range(3):
        for j in range(3):r[i+j]+=a[i]*b[j]
    for k in range(4,2,-1):
        r[k-2]+=r[k];r[k-3]+=r[k]
    return encode(r)
mul=[[mul0(a,b) for b in digits] for a in digits]
def power(a,n):
    r=1
    while n:
        if n&1:r=mul[r][a]
        a=mul[a][a];n//=2
    return r
inv=[0]+[power(i,25) for i in range(1,27)]
assert all(mul[i][inv[i]]==1 for i in range(1,27))
assert all(power(i,27)==i for i in range(27))
frob=[power(i,3) for i in range(27)]
trace=[add[add[i][frob[i]]][frob[frob[i]]] for i in range(27)]
assert set(trace)=={0,1,2}
def sm(xs):
    z=0
    for i in xs:z=add[z][i]
    return z
def mm(A,B):
    return tuple(tuple(sm(mul[A[i][k]][B[k][j]] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))
def tr(A):return tuple(zip(*A))
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def matinv(A):
    n=len(A);R=[list(A[i])+list(eye(n)[i]) for i in range(n)]
    for i in range(n):
        r=next(r for r in range(i,n) if R[r][i]);R[i],R[r]=R[r],R[i]
        u=inv[R[i][i]];R[i]=[mul[u][v] for v in R[i]]
        for j in range(n):
            if j!=i:
                u=R[j][i];R[j]=[add[v][neg[mul[u][w]]] for v,w in zip(R[j],R[i])]
    assert tuple(tuple(r[:n]) for r in R)==eye(n)
    return tuple(tuple(r[n:]) for r in R)
def mv(A,v):return tuple(sm(mul[a][b] for a,b in zip(row,v)) for row in A)
def sigmaM(A):return tuple(tuple(frob[a] for a in r) for r in A)
Jf=tuple(tuple(int(Jstd[i,j])%3 for j in range(4)) for i in range(4))
U=[list(r) for r in eye(4)]
U[0][2]=3;U[0][3]=9;U[1][2]=9;U[1][3]=4
L=[list(r) for r in eye(4)]
L[2][0]=5;L[2][1]=10;L[3][0]=10;L[3][1]=7
P=mm(tuple(map(tuple,U)),tuple(map(tuple,L)))
assert mm(mm(tr(P),Jf),P)==Jf
Pi=matinv(P)
h=mm(P,sigmaM(Pi))
assert mm(mm(tr(h),Jf),h)==Jf
assert mm(mm(h,sigmaM(h)),sigmaM(sigmaM(h)))==eye(4)
def semilinear(v):return mv(h,tuple(frob[a] for a in v))
fixed=0
for v in itertools.product(range(27),repeat=4):
    if semilinear(v)==v:fixed+=1
assert fixed==3**4
for w in itertools.product(range(3),repeat=4):
    assert semilinear(mv(P,w))==mv(P,w)
trace_pairings=0
for a in range(1,27):
    assert any(trace[mul[a][z]] for z in range(27));trace_pairings+=27
moore=tuple(tuple(power(z,3**j) for j in range(3)) for z in (1,3,9))
assert mm(moore,matinv(moore))==eye(3)
assert mm(tuple(tuple(row[j] for j in (0,2,1)) for row in moore),
          matinv(tuple(tuple(row[j] for j in (0,2,1)) for row in moore)))==eye(3)
for v in [tuple(int(i==j) for i in range(4)) for j in range(4)]:
    orbit=[v,semilinear(v),semilinear(semilinear(v))]
    for z in range(27):
        coeff=[z,frob[z],frob[frob[z]]]
        pz=tuple(sm(mul[coeff[j]][orbit[j][i]] for j in range(3)) for i in range(4))
        assert semilinear(pz)==pz
dual_fixed=sum(frob[a]==a for a in range(27))
assert dual_fixed==3
dual_orbits=[];left=set(range(27))
while left:
    a=min(left);orb={a,frob[a],frob[frob[a]]};left-=orb;dual_orbits.append(len(orb))
assert sorted(dual_orbits)==[1]*3+[3]*8

out={'status':'PASS','universal_polynomial_certificates':polys,
     'endpoint_inequalities':endpoints,'symbolic_matrix_identities':5,
     'F27':{'tested_vectors':27**4,'fixed_vectors':fixed,'trace_pairings':trace_pairings,
             'fixed_dual_weights':dual_fixed,'dual_orbit_lengths':sorted(dual_orbits),
             'descent_order_equals_characteristic':3},
     'source_checker_sha256':hashlib.sha256((B/'check_unipotent.py').read_bytes()).hexdigest(),
     'seconds':round(time.monotonic()-start,6)}
(B/'all_fields_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
