"""Exact reconstruction of Severn 2610.00387v2 Appendix A boundary matrices.

Input: printed ten roots, eight cocycles and seventeen intervals.
Arithmetic: pairs of fractions in Q[w]/(w^2+w+1).
Output is derived by the cocycle/twist and cup formulas in Sections 7-8,
not entered as the advertised nilpotent matrices. A final comparison uses
root's independently transcribed printed blocks from check_severn_printed.py.
This verifies a linear-algebra certificate; it is not a check of the full
geometric transfer or nilpotent-orbit proof.
"""
from fractions import Fraction as F
from pathlib import Path
import json
class K:
    __slots__=('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,K): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=K(o); return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+-K(o)
    def __rsub__(self,o): return K(o)+-self
    def __mul__(self,o):
        o=K(o); return K(self.a*o.a-self.b*o.b,self.a*o.b+self.b*o.a-self.b*o.b)
    __rmul__=__mul__
    def conj(self): return K(self.a-self.b,-self.b)
    def inv(self):
        norm=self.a*self.a-self.a*self.b+self.b*self.b
        if not norm: raise ZeroDivisionError
        c=self.conj(); return K(c.a/norm,c.b/norm)
    def __truediv__(self,o): return self*K(o).inv()
    def __rtruediv__(self,o): return K(o)*self.inv()
    def __eq__(self,o):
        o=K(o); return self.a==o.a and self.b==o.b
    def __bool__(self): return bool(self.a or self.b)
    def __str__(self): return f'{self.a} + ({self.b})w'
    __repr__=__str__
zero=K(); one=K(1); w=K(0,1)
def Z(m,n): return [[K() for j in range(n)] for i in range(m)]
def eye(n):
    M=Z(n,n)
    for i in range(n): M[i][i]=one
    return M
def mat(rows):return [[K(x) for x in row] for row in rows]
def add(A,B): return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def scale(q,A):return [[q*a for a in row] for row in A]
def mul(A,B):
    C=Z(len(A),len(B[0]))
    for i,ar in enumerate(A):
        for k,a in enumerate(ar):
            if a:
                for j,b in enumerate(B[k]):
                    if b:C[i][j]=C[i][j]+a*b
    return C
def trans(A):return [list(row) for row in zip(*A)]
def adj(A): return [[x.conj() for x in row] for row in trans(A)]
def iszero(A):return not any(x for row in A for x in row)
def eq(A,B):return iszero(add(A,scale(K(-1),B)))
def rref(A,ncols=None):
    M=[row[:] for row in A]; m=len(M); n=ncols or len(M[0]); piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]; q=M[r][c].inv();M[r]=[q*x for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]:
                q=M[i][c];M[i]=[x-q*y for x,y in zip(M[i],M[r])]
        piv.append(c);r+=1
        if r==m:break
    return M,piv
def rank(A):return len(rref(A)[1])
def solve(A,B):
    n=len(A[0]);M,piv=rref([ar+br for ar,br in zip(A,B)],n)
    assert piv==list(range(n)),('not full rank',piv)
    assert all(not any(row[n:]) for row in M[n:]),'inconsistent'
    return [row[n:] for row in M[:n]]
def enc(A):return [[[str(x.a),str(x.b)] for x in row] for row in A]
roots=mat([
[1,-1-w,1,w,-1-w,w],
[1,0,0,1+w,0,0],
[0,1,1+w,0,0,0],
[1,w,-1-w,w,-1-w,1],
[1,-1-w,-1-w,-1-w,-1-w,w],
[1,-1-w,w,w,w,w],
[0,0,1,0,0,-1],
[1,w,w,-1-w,1,-1-w],
[1,-w,0,0,0,0],
[0,1,0,0,0,-1]])
vs=[trans([v]) for v in roots]
norms=[mul(adj(v),v)[0][0] for v in vs]
reflections=[add(eye(6),scale(-2/n,mul(v,adj(v)))) for n,v in zip(norms,vs)]
assert all(eq(mul(s,s),eye(6)) and eq(adj(s),s) for s in reflections)
T=[s for s in reflections for _ in range(2)]
V=[v for v in vs for _ in range(2)]
Qs=[];prod=eye(6)
for s in T:Qs.append(prod);prod=mul(prod,s)
assert eq(prod,eye(6))
R=trans([trans(mul(q,v))[0] for q,v in zip(Qs,V)])
C=[row for n,v in zip(norms,vs) for row in (scale(2/n,adj(v))[0],)*2]
B=Z(20,8)
for j in range(4): B[2*j][j]=B[2*j+1][j]=one
indices=[1,3,5,7,10,12,14,16,18,20]
coeff=mat([
[1,0,0,0,1+w,1,0,-1-w,0,-1+w],
[0,1,0,0,1+w,K(F(2,3),-F(2,3)),-1,K(-F(2,3),-F(1,3)),0,1+2*w],
[0,0,1,0,K(-F(1,3),-F(2,3)),K(-F(2,3),-F(1,3)),1+w,0,1+w,-w],
[0,0,0,1,1+w,1,-2-w,-1-w,0,3*w]])
for j,row in enumerate(coeff,4):
    for i,x in zip(indices,row):B[i-1][j]=x
assert iszero(mul(R,B)),('cocycle fails',mul(R,B))
assert iszero(mul(R,C))
M=[br+cr for br,cr in zip(B,C)]
assert rank(R)==6 and rank(C)==6 and rank(M)==14
U=[mul(v,[br]) for v,br in zip(V,B)]
S=Z(8,8);Fprev=Z(6,8)
for i in range(20):
    # Q_i is either I or a reflection, hence its adjoint is its inverse.
    lift=add(mul(adj(Qs[i]),Fprev),scale(K(F(1,2)),U[i]))
    S=add(S,mul(adj(lift),U[i]))
    Fprev=add(Fprev,mul(Qs[i],U[i]))
assert iszero(Fprev)
assert iszero(add(S,adj(S)))
Sprinted=mat([
[0,0,0,0,3,0,0,0],
[0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,3],
[-3,0,0,0,-3-6*w,-3-3*w,4+5*w,-6-6*w],
[0,-1,0,0,-3*w,-1-2*w,1+4*w,-2-4*w],
[0,0,-1,0,1+5*w,3+4*w,-2-4*w,3+6*w],
[0,0,0,-3,-6*w,-2-4*w,3+6*w,-3-6*w]])
intervals=[(1,8,1),(1,18,1),(2,8,2),(3,8,1),(4,8,2),(5,6,1),(5,8,1),(7,8,1),(9,10,1),(9,12,1),(9,16,1),(9,17,2),(9,18,1),(11,12,1),(13,14,1),(13,16,1),(15,16,1)]
# Read root's independent transcription solely for comparison after derivation.
import sympy as sy
ns={}
script=Path(__file__).with_name('check_severn_printed.py').read_text()
exec(script.split('\nD=s.diag')[0],ns)
wp=ns['w']
def cv(expr):
    p=sy.Poly(expr,wp);a,b=p.nth(0),p.nth(1)
    return K(F(int(a.p),int(a.q)),F(int(b.p),int(b.q)))
Xp=[[[cv(A[i,j]) for j in range(4)] for i in range(4)] for A in ns['X']]
records=[];derived=[]
for j,(a,b,k) in enumerate(intervals,1):
    W=Z(6,20);boundary=eye(6)
    for i in range(a-1,b):
        v=mul(boundary,V[i])
        for z in range(6):W[z][i]=v[z][0]
        boundary=mul(boundary,T[i])
    if k==1:
        assert eq(boundary,eye(6))
        Wk=W
    else:
        assert not eq(boundary,eye(6)) and eq(mul(boundary,boundary),eye(6))
        assert any(not eq(mul(boundary,T[i]),mul(T[i],boundary)) for i in range(a-1,b))
        Wk=mul(add(eye(6),boundary),W)
    Clocal=[row if a-1<=i<b else [K() for _ in range(6)] for i,row in enumerate(C)]
    Nlambda=mul(Clocal,Wk)
    assert iszero(mul(R,mul(Nlambda,B)))
    sol=solve(M,mul(Nlambda,B))
    N=sol[:8]
    target=Z(8,8)
    for ii in range(4):
        for jj in range(4):target[ii][jj+4]=Xp[j-1][ii][jj]
    same=eq(N,target)
    derived.append(N)
    records.append({'j':j,'interval':[a,b],'return_power':k,'derived_equals_printed':same,'nilpotence_square_zero':iszero(mul(N,N)),'rank_K':rank(N),'difference':enc(add(N,scale(K(-1),target))) if not same else None})
result={'source':'Severn 2610.00387v2 / weil-qsqrt3-v1.5.tex Appendix A and Section 8.1','arithmetic':'exact Fractions in Q[w]/(w^2+w+1)',
'cocycle_relation_rank':rank(R),'coboundary_rank':rank(C),'basis_plus_coboundary_rank':rank(M),'cocycle_dimension':20-rank(R),'parabolic_dimension':20-rank(R)-rank(C),
'gram_derived_equals_printed':eq(S,Sprinted),'gram_skew_hermitian':iszero(add(S,adj(S))),'gram_derived':enc(S),'boundary_records':records,
'all_17_derived_equal_printed':all(r['derived_equals_printed'] for r in records),'all_pairwise_products_zero':all(iszero(mul(N,L)) for N in derived for L in derived)}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['gram_derived']},indent=2))
