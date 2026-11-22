"""Independent finite supplement to the whole proof audit of D-OL06--08.

The author's code was read first; no author code, matrices, or output is
imported. Orthogonal matrices are built from all hyperbolic bases, not
from the author's generator closure. Universal arguments are audited in prose.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import time
import sympy as sp

start = time.perf_counter()
out = {'status': 'PASS', 'scope': 'Independent exact finite supplement; not a proof by extrapolation'}

# Generic quadratic polynomial: diagonal terms are retained, so no division
# by two or characteristic restriction is hidden in the symbolic identities.
c = sp.symbols('c0:6')
pairs = [(i,j) for i in range(3) for j in range(i,3)]
def Qw(z): return sum(a*z[i]*z[j] for a,(i,j) in zip(c,pairs))
def Bw(z,w): return sp.expand(Qw(z+w)-Qw(z)-Qw(w))
def U(v):
    A=sp.eye(5)
    for j in range(3):
        ej=sp.zeros(3,1);ej[j]=1
        A[0,j+1]=-Bw(v,ej)
        A[j+1,4]=v[j]
    A[0,4]=-Qw(v)
    return A
v=sp.Matrix(sp.symbols('v0:3')); w=sp.Matrix(sp.symbols('w0:3'))
x=sp.Matrix(sp.symbols('x0:5'))
def Q(z): return z[0]*z[4]+Qw(z[1:4,0])
assert all(sp.expand(t)==0 for t in U(v)*U(w)-U(v+w))
assert sp.expand(Q(U(v)*x)-Q(x))==0
xx,yy=sp.symbols('xx yy',nonzero=True)
z=sp.Matrix([xx,*w,yy])
expected=sp.Matrix([(xx*yy+Qw(w))/yy,0,0,0,yy])
assert all(sp.cancel(t)==0 for t in U(-w/yy)*z-expected)
out['generic_quadratic_radical']={'dimension':5,'quadratic_coefficients':6,'identities':3}

# Independent complete O6+(2): columns are all ordered hyperbolic bases.
dim=6; ident=tuple(1<<i for i in range(dim))
def qb(x): return sum(((x>>i)&1)*((x>>(i+1))&1) for i in (0,2,4))%2
def bb(x,y): return qb(x^y)^qb(x)^qb(y)
def mv(A,x):
    ans=0
    for i in range(dim):
        if (x>>i)&1: ans^=A[i]
    return ans
def mm(A,B): return tuple(mv(A,x) for x in B)
def rk(A):
    piv={}
    for x in A:
        while x:
            i=x.bit_length()-1
            if i in piv: x^=piv[i]
            else: piv[i]=x;break
    return len(piv)
def bases(space,columns=()):
    if len(columns)==dim:
        yield columns; return
    singular=[x for x in space if x and not qb(x)]
    for e in singular:
        for f in singular:
            if not bb(e,f): continue
            perp=[x for x in space if not bb(e,x) and not bb(f,x)]
            yield from bases(perp,columns+(e,f))
roots=[x for x in range(64) if qb(x)]
ref={v:tuple(x^(v if bb(x,v) else 0) for x in ident) for v in roots}
count=generic=exceptional=0; ranks=Counter(); seen=set()
for H in bases(list(range(64))):
    assert H not in seen; seen.add(H);count+=1
    v=next((x for x in roots if bb(x,mv(H,x))),None)
    if v is None:
        exceptional+=1
        assert mm(H,H)==ident
        assert all(bb(x,mv(H,x))==0 for x in range(64))
        r=rk(tuple(x^y for x,y in zip(H,ident)))
        assert r%2==0; ranks[r]+=1
    else:
        generic+=1
        K=mm(ref[mv(H,v)],ref[v])
        assert K!=ident and mm(mm(K,K),K)==ident
        assert rk(tuple(x^y for x,y in zip(K,ident)))==2
assert count==40320 and generic+exceptional==count
out['complete_hyperbolic_basis_enumeration']={
 'O6plus2_matrices':count,'generic_rank_two_rotations':generic,
 'exceptional_selfadjoint_involutions':exceptional,'exceptional_ranks':dict(ranks)}

# Field tables built from polynomial quotients. F9 deliberately uses
# X^2+X+2, different from the author's X^2+1.
class Field:
    def __init__(self,p,f,mod):
        self.p=p;self.f=f;self.q=p**f
        digits=[tuple((a//p**i)%p for i in range(f)) for a in range(self.q)]
        encode=lambda a:sum((z%p)*p**i for i,z in enumerate(a))
        self.add=[[encode([x+y for x,y in zip(A,B)]) for B in digits] for A in digits]
        self.neg=[encode([-x for x in A]) for A in digits]
        self.mul=[]
        for A in digits:
            row=[]
            for B in digits:
                t=[0]*(2*f-1)
                for i,x in enumerate(A):
                    for j,y in enumerate(B):t[i+j]+=x*y
                for k in range(2*f-2,f-1,-1):
                    z=t[k]%p
                    for j in range(f):t[k-f+j]-=z*mod[j]
                row.append(encode(t[:f]))
            self.mul.append(row)
        self.frob=[self.power(a,p) for a in range(self.q)]
        self.inv=[0]+[self.power(a,self.q-2) for a in range(1,self.q)]
        assert all(self.mul[a][self.inv[a]]==1 for a in range(1,self.q))
    def power(self,a,k):
        z=1
        for _ in range(k):z=self.mul[z][a]
        return z

field_results=[]
for p,f,poly in [(2,2,[1,1]),(2,3,[1,1,0]),(3,2,[2,1])]:
    K=Field(p,f,poly);q=K.q;add=K.add;mul=K.mul;neg=K.neg;fr=K.frob
    I=(1,0,0,1)
    def matmul(A,B):
        a,b,c,d=A;e,g,h,j=B
        return (add[mul[a][e]][mul[b][h]],add[mul[a][g]][mul[b][j]],
                add[mul[c][e]][mul[d][h]],add[mul[c][g]][mul[d][j]])
    def matvec(A,x):
        a,b,c,d=A;u,v=x
        return (add[mul[a][u]][mul[b][v]],add[mul[c][u]][mul[d][v]])
    def quad(coeff,x):
        a,b,c=coeff;u,v=x
        return add[add[mul[a][mul[u][u]]][mul[b][mul[u][v]]]][mul[c][mul[v][v]]]
    vectors=list(product(range(q),repeat=2))
    matrices=vector_checks=projective_checks=0; distinct=set()
    for A in product(range(q),repeat=4):
        a,b,c,d=A;det=add[mul[a][d]][neg[mul[b][c]]]
        if not det:continue
        z=K.inv[det]
        Ai=tuple(mul[z][x] for x in (d,neg[b],neg[c],a))
        assert matmul(A,Ai)==I
        H=matmul(A,tuple(fr[x] for x in Ai));distinct.add(H)
        coeff=(mul[Ai[0]][Ai[2]],add[mul[Ai[0]][Ai[3]]][mul[Ai[1]][Ai[2]]],mul[Ai[1]][Ai[3]])
        prodH=I; powerH=H
        for _ in range(f):
            prodH=matmul(prodH,powerH);powerH=tuple(fr[x] for x in powerH)
        assert prodH==I
        fixed=0
        for x in vectors:
            hx=matvec(H,tuple(fr[t] for t in x))
            assert quad(coeff,hx)==fr[quad(coeff,x)]
            fixed+=hx==x;vector_checks+=1
        assert fixed==p*p
        for scalar in range(1,q):
            M=tuple(mul[scalar][x] for x in H);acc=I;cur=M
            for _ in range(f):
                acc=matmul(acc,cur);cur=tuple(fr[x] for x in cur)
            norm=K.power(scalar,(q-1)//(p-1))
            assert acc==(norm,0,0,norm);projective_checks+=1
        matrices+=1
    assert matrices==(q*q-1)*(q*q-q)
    field_results.append({'q':q,'all_GL2_bases':matrices,'distinct_cocycles':len(distinct),
                          'quadratic_vector_identities':vector_checks,'scalar_projective_cocycles':projective_checks})
out['semilinear_descent_from_all_bases']=field_results

# Universal monotonic estimates are reduced in the proof to these endpoint
# rational comparisons. Finite calculations do not supply monotonicity.
def orbit_bound(q):return (F(1,q*q)+F(1,q**9))/(1-F(1,q**9)-F(1,q**19))
assert orbit_bound(3)<F(1,8) and orbit_bound(2)<F(1,3)
field_bounds={}
for q,p,f in [(4,2,2),(8,2,3),(9,3,2)]:
    z=F(q,p**(20*(f-1)))/(1-F(1,q**9)-F(1,q**19))
    assert z<F(1,4);field_bounds[str(q)]=str(z)
delta=F(7,64)
assert F(1,2)*F(1,2)*F(7,8)/2==delta
assert F(1,2)*F(2,3)*F(2,3)/2>delta
assert F(1,8)>delta and F(3,16)>delta
assert 6/(1+10*delta-2)==64 and 2**18>64
out['exact_constants']={'odd_orbit_bound':str(orbit_bound(3)),'even_orbit_bound':str(orbit_bound(2)),
 'field_bounds':field_bounds,'normalizer_support':str(delta),'source_degree_ceiling':64}

proof=Path(__file__).resolve().parents[2]/'imprimitive'/'orthogonal_lowlevels'/'orthogonal_support_section.tex'
out['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
assert out['proof_sha256']=='fefeade2dbdf99e8c7ce67fc78eaa0a26c178f2711a7162229fab9573065f8a1'
out['actual_utc']=datetime.now(timezone.utc).isoformat()
out['elapsed_seconds']=time.perf_counter()-start
out['reviewer']='/root/g34_eightfolds';out['model']='GPT-6 Astra Pro';out['effort']='inherited/unexposed'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
