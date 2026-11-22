#!/usr/bin/env python3
"""Exact author supplement for D-OL06--08; universal proof is separate.

No character table, GAP output, or external numerical input is imported.
Finite group witnesses do not substitute for the all-dimension arguments.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import deque, Counter
import json, time, hashlib, sys
import sympy as s

START=time.perf_counter()
BASE=Path(__file__).resolve().parent
OUT={'status':'PASS','scope':'Exact finite supplement, not the universal proof'}

# All-field inequalities: the proof reduces every N>=20 to these rational
# expressions, so this check is not an extrapolation from the displayed range.
def fixed_bound(q):
    return (F(1,q**2)+F(1,q**9))/(1-F(1,q**9)-F(1,q**19))
assert fixed_bound(3)<F(1,8) and fixed_bound(2)<F(1,3)
assert F(1,2)*F(1,2)*F(7,8)==F(7,32)
assert F(1,2)*F(2,3)*F(2,3)==F(2,9)
assert F(1,9)>F(7,64) and F(1,8)>F(7,64)
assert 625<648 and F(1,2)*F(1,2)*F(3,4)==F(3,16)>F(7,64)
field_bounds={}
for q,p,f in [(4,2,2),(8,2,3),(9,3,2)]:
    b=F(q,p**(20*(f-1)))/(1-F(1,q**9)-F(1,q**19))
    assert b<F(1,4)
    field_bounds[str(q)]=str(b)
assert F(6)/(1+10*F(7,64)-2)==64 and 2**18>64
J=10**30
assert 4*(J-1)+2==4*J-2 and 4*J-2>=22
OUT['universal_constants']={'odd_fixed_fraction':str(fixed_bound(3)),
 'even_fixed_fraction':str(fixed_bound(2)),'field_fixed_fractions':field_bounds,
 'normalizer_support':'7/64','inducing_degree_ceiling':64,
 'natural_dimension_cutoff':str(4*J-3)}

# Symbolic radical law over Z, hence valid in every characteristic after
# reduction. Coordinates are e, x1,y1,x2,y2, f.
N=4; d=6
v=s.Matrix(s.symbols('v0:4')); w=s.Matrix(s.symbols('w0:4'))
Gram=s.zeros(4)
for i in (0,2):Gram[i,i+1]=Gram[i+1,i]=1
def quad(z):return z[0]*z[1]+z[2]*z[3]
def radical(z):
    M=s.eye(d)
    for j in range(4):M[0,j+1]=-(z.T*Gram)[j]
    for j in range(4):M[j+1,5]=z[j]
    M[0,5]=-quad(z)
    return M
def zero(M):return all(s.expand(x)==0 for x in M)
Uv,Uw=radical(v),radical(w)
assert zero(Uv*Uw-radical(v+w))
z=s.Matrix(s.symbols('z0:6'))
Q=lambda z:z[0]*z[5]+z[1]*z[2]+z[3]*z[4]
assert s.expand(Q(Uv*z)-Q(z))==0
a,b=s.symbols('a b',nonzero=True)
z0=s.Matrix([a,*w,b]); cleared=radical(-w/b)*z0
assert zero(cleared-s.Matrix([(a*b+quad(w))/b,0,0,0,0,b]))
OUT['symbolic_radical']={'dimension':6,'group_law':True,
 'quadratic_preservation':True,'reflection_reduction':True}

def rank_mod(rows,p):
    A=[list(row) for row in rows];n=len(A);m=len(A[0]) if n else 0;r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if A[i][j]%p),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        u=pow(A[r][j]%p,-1,p);A[r]=[(u*x)%p for x in A[r]]
        for i in range(n):
            if i!=r:
                c=A[i][j]%p
                if c:A[i]=[(x-c*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==n:break
    return r

# Every homogeneous quadratic form in the listed finite spaces. Counts,
# polar rank and the squared rational bound are computed independently.
quadratic_cases=0
for p,m in [(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]:
    ij=[(i,j) for i in range(m) for j in range(i,m)]
    vecs=list(product(range(p),repeat=m))
    for coeff in product(range(p),repeat=len(ij)):
        G=[[0]*m for _ in range(m)]
        for (i,j),c in zip(ij,coeff):
            if i==j:G[i][i]=2*c%p
            else:G[i][j]=G[j][i]=c
        r=rank_mod(G,p)
        counts=Counter(sum(c*x[i]*x[j] for (i,j),c in zip(ij,coeff))%p for x in vecs)
        for t in range(p):assert (counts[t]-p**(m-1))**2<=p**(2*m-r)
        quadratic_cases+=1
OUT['quadratic_count_checks']={'forms':quadratic_cases,
 'spaces':[[2,2],[2,3],[2,4],[3,2],[3,3],[5,2]]}

# Complete O6+(2), generated from rank-one symmetries; all linear matrices
# are six exact bit columns. No imported group generators are used.
def Q2(x):return ((x&7)&(x>>3)).bit_count()%2
def B2(x,y):return (((x&7)&(y>>3))^((y&7)&(x>>3))).bit_count()%2
def act2(M,x):
    out=0
    while x:
        bit=x&-x;out^=M[bit.bit_length()-1];x^=bit
    return out
def mul2(A,B):return tuple(act2(A,b) for b in B)
I2=tuple(1<<i for i in range(6))
roots=[v for v in range(1,64) if Q2(v)]
symmetries={v:tuple(x^(v if B2(v,x) else 0) for x in I2) for v in roots}
def close2(gens):
    tabs=[[act2(g,x) for x in range(64)] for g in gens]
    found={I2};todo=deque([I2])
    while todo:
        g=todo.popleft()
        for tab in tabs:
            h=tuple(tab[x] for x in g)
            if h not in found:found.add(h);todo.append(h)
    return found
whole=close2(list(symmetries.values()))
assert len(whole)==40320
e,f=1,8;parameters=[v for v in range(64) if not(v&(e|f))]
def ue(v,x):
    b=bool(x&f)
    return x^(v if b else 0)^(e if B2(v,x)^(b and Q2(v)) else 0)
def uf(v,x):
    a=bool(x&e)
    return x^(v if a else 0)^(f if B2(v,x)^(a and Q2(v)) else 0)
Ue=[tuple(ue(v,x) for x in I2) for v in parameters]
Uf=[tuple(uf(v,x) for x in I2) for v in parameters]
assert len(set(Ue))==len(set(Uf))==16
for A in Ue+Uf:assert all(Q2(act2(A,x))==Q2(x) for x in range(64))
opposite=close2(Ue+Uf)
assert len(opposite)==20160
def rank2cols(M):
    basis={}
    for col in M:
        while col:
            i=col.bit_length()-1
            if i in basis:col^=basis[i]
            else:basis[i]=col;break
    return len(basis)
generic=exceptional=0;exceptional_ranks=Counter()
for h in whole:
    v=next((v for v in roots if B2(v,act2(h,v))),None)
    if v is not None:
        k=mul2(symmetries[act2(h,v)],symmetries[v])
        assert k!=I2 and mul2(mul2(k,k),k)==I2
        assert rank2cols(tuple(x^y for x,y in zip(k,I2)))==2
        generic+=1
    else:
        assert mul2(h,h)==I2
        assert all(B2(x,act2(h,x))==0 for x in range(64))
        r=rank2cols(tuple(x^y for x,y in zip(h,I2)))
        assert r%2==0 and h in opposite
        exceptional+=1;exceptional_ranks[r]+=1
assert generic+exceptional==40320
OUT['complete_even_matrix_check']={'O6plus2':len(whole),
 'opposite_radical_group':len(opposite),'generic':generic,
 'exceptional':exceptional,'exceptional_ranks':dict(sorted(exceptional_ranks.items()))}

# Complete GO4+(3), including nonsquare multipliers, to check the odd
# reflection commutator and every chosen prime-order power directly.
p=3;n=4
vectors=list(product(range(p),repeat=n))
def q3(x):return (x[0]*x[2]+x[1]*x[3])%p
def b3(x,y):return (x[0]*y[2]+x[1]*y[3]+x[2]*y[0]+x[3]*y[1])%p
I3=tuple(tuple(int(i==j) for i in range(n)) for j in range(n))
def act3(M,x):return tuple(sum(x[j]*M[j][i] for j in range(n))%p for i in range(n))
def mul3(A,B):return tuple(act3(A,b) for b in B)
def reflection3(v):
    den=pow(q3(v),-1,p)
    return tuple(tuple((x[i]-den*b3(x,v)*v[i])%p for i in range(n)) for x in I3)
R3={v:reflection3(v) for v in vectors if q3(v)}
G3gens=sorted(set(R3.values()))
tabs3=[{x:act3(g,x) for x in vectors} for g in G3gens]
O3={I3};todo=deque([I3])
while todo:
    A=todo.popleft()
    for tab in tabs3:
        C=tuple(tab[x] for x in A)
        if C not in O3:O3.add(C);todo.append(C)
assert len(O3)==1152
h0=((2,0,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,1))
GO3=O3|{mul3(h0,g) for g in O3}
assert len(GO3)==2304
scalars={I3,tuple(tuple(2*x%3 for x in col) for col in I3)}
orders3=Counter()
for h in GO3-scalars:
    v=next(v for v in R3 if mul3(h,R3[v])!=mul3(R3[v],h))
    k=mul3(R3[act3(h,v)],R3[v])
    columns=tuple(tuple((x-y)%p for x,y in zip(col,i)) for col,i in zip(k,I3))
    assert rank_mod(list(zip(*columns)),p)==2
    powers=[I3,k]
    while powers[-1]!=I3:
        powers.append(mul3(powers[-1],k));assert len(powers)<20
    order=len(powers)-1;orders3[order]+=1
    prime=next(l for l in (2,3,5,7,11,13) if order%l==0)
    g=powers[order//prime]
    cols=tuple(tuple((x-y)%p for x,y in zip(col,i)) for col,i in zip(g,I3))
    assert g!=I3 and rank_mod(list(zip(*cols)),p)==2
OUT['complete_odd_matrix_check']={'O4plus3':len(O3),'GO4plus3':len(GO3),
 'nonscalar_matrices':len(GO3-scalars),'commutator_orders':dict(sorted(orders3.items()))}

# Finite fields implemented as polynomials over the prime field; this
# checks norm rescaling and non-pure diagonal semilinear cocycles.
class Field:
    def __init__(self,p,f,mod):
        self.p,self.f,self.mod=p,f,mod;self.q=p**f
    def coeff(self,a):
        out=[]
        for _ in range(self.f):out.append(a%self.p);a//=self.p
        return out
    def val(self,a):return sum((x%self.p)*self.p**i for i,x in enumerate(a))
    def add(self,a,b):return self.val([x+y for x,y in zip(self.coeff(a),self.coeff(b))])
    def neg(self,a):return self.val([-x for x in self.coeff(a)])
    def mul(self,a,b):
        A=self.coeff(a);B=self.coeff(b);C=[0]*(2*self.f-1)
        for i,x in enumerate(A):
            for j,y in enumerate(B):C[i+j]+=x*y
        for i in range(2*self.f-2,self.f-1,-1):
            c=C[i]%self.p
            for j in range(self.f):C[i-self.f+j]-=c*self.mod[j]
        return self.val(C[:self.f])
    def power(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def inv(self,a):assert a;return self.power(a,self.q-2)
    def norm(self,a):return self.power(a,(self.q-1)//(self.p-1))
field_checks=[]
for p,f,mod in [(2,2,[1,1]),(2,3,[1,1,0]),(3,2,[1,0])]:
    K=Field(p,f,mod);q=K.q
    for a in range(1,q):assert K.mul(a,K.inv(a))==1
    assert {K.norm(a) for a in range(1,q)}==set(range(1,p))
    normone=[a for a in range(1,q) if K.norm(a)==1]
    assert set(normone)=={K.mul(K.power(b,p),K.inv(b)) for b in range(1,q)}
    fixedlines={}
    for a in normone:
        fixed=[x for x in range(q) if K.mul(a,K.power(x,p))==x]
        assert len(fixed)==p and any(fixed)
        fixedlines[a]=fixed
        for x in range(q):
            y=x
            for _ in range(f):y=K.mul(a,K.power(y,p))
            assert y==x
    # Tensor two hyperbolic semilinear blocks. They need not equal pure
    # Frobenius in this initial basis; each has an explicit descended basis.
    cases=identities=0
    for a,b in product(normone,repeat=2):
        scalars=[a,b,K.inv(a),K.inv(b)]
        H=lambda x:tuple(K.mul(c,K.power(t,p)) for c,t in zip(scalars,x))
        Qk=lambda x:K.add(K.mul(x[0],x[2]),K.mul(x[1],x[3]))
        fixed=[]
        for x in product(range(q),repeat=4):
            hx=H(x)
            assert Qk(hx)==K.power(Qk(x),p)
            if hx==x:fixed.append(x)
            identities+=1
        assert len(fixed)==p**4
        # Each first-coordinate fixed line pairs nondegenerately with its
        # opposite; rescale over the fixed field to make hyperbolic pairs.
        for j in (0,1):
            x=next(t for t in fixedlines[scalars[j]] if t)
            y=next(t for t in fixedlines[scalars[j+2]] if t)
            paired=K.mul(x,y)
            assert paired in range(1,p)
        cases+=1
    field_checks.append({'q':q,'norm_one_elements':len(normone),
      'nonpure_cocycles':cases,'vector_identities':identities})
OUT['semilinear_fields']=field_checks

proof=BASE/'orthogonal_support_section.tex'
raw=proof.read_text()
assert raw.count('\\[')==raw.count('\\]')
assert not any(ord(c)<32 and c not in '\n\t\r' for c in raw)
OUT['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
OUT['seconds']=round(time.perf_counter()-START,9)
dest=BASE/'orthogonal_support_checked.json'
dest.write_text(json.dumps(OUT,indent=2,sort_keys=True)+'\n')
print(json.dumps(OUT,indent=2,sort_keys=True))
