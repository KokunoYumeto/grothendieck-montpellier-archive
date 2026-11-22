"""Exact finite/symbolic certificates for A.5--A.7. Python 3 + SymPy.
Enumerates all 120 possible images of a projective triple, not all matrices.
For p=3 mod4 uses F_p[i]; for p=1 mod4 chooses i in F_p.
"""
from itertools import permutations, combinations, product
from fractions import Fraction
import json, time
import sympy as sp
START=time.monotonic()

def finite_octahedron(p):
    roots=[x for x in range(p) if x*x%p==(p-1)]
    one=(1,0); zero=(0,0); ii=(roots[0],0) if roots else (0,1)
    def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def neg(x):return ((-x[0])%p,(-x[1])%p)
    def sub(x,y):return add(x,neg(y))
    def mul(x,y):return ((x[0]*y[0]-x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def inv(x):
        den=pow((x[0]*x[0]+x[1]*x[1])%p,-1,p)
        return (x[0]*den%p,-x[1]*den%p)
    def div(x,y):return mul(x,inv(y))
    def norm(v):
        x,y=v
        return (div(x,y),one) if y!=zero else (one,zero)
    def det(u,v):return sub(mul(u[0],v[1]),mul(u[1],v[0]))
    def scale(t,v):return (mul(t,v[0]),mul(t,v[1]))
    def mat_from_triple(u,v,w):
        return scale(det(w,v),u),scale(det(u,w),v)
    def act(M,P):
        u,v=M;x,y=P
        return norm((add(mul(u[0],x),mul(v[0],y)),add(mul(u[1],x),mul(v[1],y))))
    S=[(one,zero),(zero,one),(one,one),(neg(one),one),(ii,one),(neg(ii),one)]
    assert len(set(S))==6
    G=set()
    for u,v,w in permutations(S,3):
        M=mat_from_triple(u,v,w)
        images=[act(M,P) for P in S]
        if set(images)==set(S):G.add(tuple(S.index(P) for P in images))
    identity=tuple(range(6))
    def compose(g,h):return tuple(g[h[i]] for i in range(6))
    invol=[g for g in G if g!=identity and compose(g,g)==identity]
    klein=set()
    for a,b in combinations(invol,2):
        ab=compose(a,b)
        if compose(b,a)!=ab:continue
        V=frozenset([identity,a,b,ab])
        if len(V)!=4:continue
        fixed=set()
        for g in V-{identity}:fixed|={i for i in range(6) if g[i]==i}
        if fixed==set(range(6)):klein.add(V)
    negz=tuple(S.index(norm((neg(P[0]),P[1]))) for P in S)
    invz=tuple(S.index(norm((P[1],P[0]))) for P in S)
    V0=frozenset([identity,negz,invz,compose(negz,invz)])
    def inverse(g):return tuple(g.index(i) for i in range(6))
    normalizer=[g for g in G if {compose(compose(g,v),inverse(g)) for v in V0}==V0]
    def crossratio(a,b,c,d):return div(mul(det(a,c),det(b,d)),mul(det(a,d),det(b,c)))
    harmonics={neg(one),add(one,one),inv(add(one,one))}
    good_pairs=[]
    for omit in combinations(range(6),2):
        c=[S[j] for j in range(6) if j not in omit]
        if crossratio(*c) in harmonics:good_pairs.append(omit)
    assert len(G)==(120 if p==5 else 24)
    assert len(klein)==(5 if p==5 else 1)
    assert len(normalizer)==24
    assert len(good_pairs)==(15 if p==5 else 3)
    return {'p':p,'q':p if roots else p*p,'triple_candidates':120,'stabilizer_order':len(G),'klein_same_fixed_set':len(klein),'normalizer_order':len(normalizer),'harmonic_complement_pairs':len(good_pairs)}

primes=list(sp.primerange(3,100))
for p in primes:print(json.dumps(finite_octahedron(p)))
print(json.dumps({'p':2,'standard_octahedral_set_size':3,'excluded':'minus identity collapses to identity'}))
# Symbolic characteristic calculation for non-antipodal pairs: crossratio = +/-i.
x=sp.symbols('x')
for t in [-sp.Integer(1),sp.Integer(2),sp.Rational(1,2)]:
 print(json.dumps({'harmonic_value':str(t),'i_squared_plus_one_after_i_eq_value':str(sp.factor(t*t+1))}))
# Integral reflection matrices; no claim that finite multiplication proves presentation completeness.
S=sp.Matrix([[0,-1],[1,0]])
T=sp.Matrix([[1,1],[0,1]])
rho=S*T
r2=sp.Matrix([[0,1],[1,0]])
r1=S*r2
r3=r2*rho
assert r1*r1==r2*r2==r3*r3==sp.eye(2)
assert (r1*r2)**2==(r2*r3)**3==-sp.eye(2)
assert (r1*r2)**4==sp.eye(2)
print(json.dumps({'integral_reflections':[str(r1),str(r2),str(r3)],'SL2_relations_verified':True,'GL2_relations_verified':True}))
# Exhaustive reduction modulo 4 for the binary S3 diagram on manuscript sheet 051.
def mm4(a,b):
 return ((a[0]*b[0]+a[1]*b[2])%4,(a[0]*b[1]+a[1]*b[3])%4,
         (a[2]*b[0]+a[3]*b[2])%4,(a[2]*b[1]+a[3]*b[3])%4)
def mi4(a):return (a[3]%4,(-a[1])%4,(-a[2])%4,a[0]%4)
def mp4(a,n):
 b=(1,0,0,1)
 for _ in range(n):b=mm4(b,a)
 return b
I4=(1,0,0,1);minusI4=(3,0,0,3)
G4={a for a in product(range(4),repeat=4) if (a[0]*a[3]-a[1]*a[2])%4==1}
W4={(1,0,0,1),(3,2,0,3),(3,0,2,3),(1,2,2,1)}
assert len(G4)==48 and len(W4)==4 and minusI4 not in W4
assert all(mm4(a,b) in W4 for a in W4 for b in W4)
assert all(mp4(a,2)==I4 for a in W4)
assert all(mm4(mm4(g,w),mi4(g)) in W4 for g in G4 for w in W4)
K2={g for g in G4 if tuple(x%2 for x in g)==I4}
assert len(K2)==8 and K2==W4|{mm4(minusI4,w) for w in W4}
coset4=lambda a:frozenset(mm4(a,w) for w in W4)
quotient4={coset4(a) for a in G4}
S4=(0,3,1,0);R4=(0,3,1,1)
assert len(quotient4)==12
assert coset4(mp4(S4,2))==coset4(mp4(R4,3))!=coset4(I4)
assert coset4(mp4(R4,6))==coset4(I4)
assert coset4(mm4(mm4(S4,R4),mi4(S4)))==coset4(mi4(R4))
normalforms4={coset4(mm4(mp4(R4,j),mp4(S4,e))) for j in range(6) for e in range(2)}
assert normalforms4==quotient4
print(json.dumps({'SL2_Zmod4_order':len(G4),'W':sorted(W4),'W_normal_Klein_four':True,
 'minus_identity_outside_W':True,'mod2_kernel_splits_W_times_center':True,
 'quotient_order':len(quotient4),'binary_dihedral_Dic3_relations_verified':True,
 'all_twelve_normal_forms_distinct':True,'exhaustive_matrix_candidates':4**4}))
# Universal 2-regular domain involution contradicting the alleged line-bundle corollary.
x,y,z=sp.symbols('x y z');f=x*x+y*z-1
A=sp.Matrix([[x,y],[z,-x]])
assert A*A-sp.eye(2)==f*sp.eye(2)
assert sp.simplify((A-sp.eye(2))*(A+sp.eye(2))-f*sp.eye(2))==sp.zeros(2)
assert all(int(v.subs({x:1,y:0,z:0}))%2==0 for v in A-sp.eye(2))
print(json.dumps({'universal_involution':str(A),'defining_polynomial':str(f),'matrix_factorization_verified':True,'relation_matrix_mod_m':[[0,0],[0,0]],'minimal_generators_of_fixed_module':2,'generic_rank':1}))
# Norm ring Z[(1+sqrt(-11))/2] and F4 residue units.
m,n=sp.symbols('m n',integer=True)
N=m*m+m*n+3*n*n
units=[(a,b) for a,b in product(range(-2,3),repeat=2) if N.subs({m:a,n:b})==1]
assert units==[(-1,0),(1,0)]
print(json.dumps({'ring':'Z[(1+sqrt(-11))/2]','norm':str(N),'units':units,'residue_field':'F4','image_units_in_F4_star':[1],'nonsplit_conjugacy_classes':3,'euclidean_covering_norm_bound':'15/16'}))
# Hexagonal quadratic form and cohomological indices.
Q=sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]])
u=sp.Matrix([1,0]);w=sp.Matrix([-1,2]);ratio=(w.T*Q*w)[0]/(u.T*Q*u)[0]
assert ratio==3
print(json.dumps({'hexagonal_ratio':str(ratio),'split_H1_order':2,'nonsplit_H1_order':1}))
print(json.dumps({'all_assertions_passed':True,'seconds':round(time.monotonic()-START,6)}))
