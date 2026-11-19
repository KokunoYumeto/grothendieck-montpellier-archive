#!/usr/bin/env python3
"""Independent exact degree-four/free-Lie certificate for LM6 A.20 audit.
Source arithmetic nonvanishing is not inferred from this finite calculation.
"""
from time import perf_counter
_started=perf_counter()
from itertools import product
from functools import lru_cache
import sympy as s

def add(a,b):
    c=dict(a)
    for w,k in b.items():
        c[w]=c.get(w,0)+k
        if c[w]==0: del c[w]
    return c

def scale(a,k): return {w:k*v for w,v in a.items() if k*v}
def mul(a,b):
    c={}
    for u,j in a.items():
        for v,k in b.items(): c[u+v]=c.get(u+v,0)+j*k
    return {w:k for w,k in c.items() if k}
def bracket(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def derive(a,dx,dy):
    c={}
    for w,k in a.items():
        for i,ch in enumerate(w):
            c=add(c,{w[:i]+v+w[i+1:]:k*j for v,j in (dx if ch=='x' else dy).items()})
    return c

def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def standard(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return bracket(standard(w[:i]),standard(w[i:]))
def words(n):return [''.join(w) for w in product('xy',repeat=n)]
def lb(n):return [w for w in words(n) if lyndon(w)]
def col(a,rows):return s.Matrix([a.get(w,0) for w in rows])

x={'x':1};y={'y':1};omega=bracket(x,y)
a1=omega;a2=bracket(x,a1);a3=bracket(x,a2);a4=bracket(x,a3)
eps=(a4,add(bracket(y,a3),scale(bracket(a1,a2),-1)))
def lower(D):return (add(derive(D[0],y,{}),scale(D[1],-1)),derive(D[1],y,{}))
T=lower(eps);T2=lower(T)
for name,D in [('epsilon4',eps),('T4',T),('F0^2 epsilon4',T2)]:
    assert not derive(omega,*D)
    print('PASS:',name,'preserves [x,y]')

r5=words(5);r6=words(6)
L5=[standard(w) for w in lb(5)];L6=[standard(w) for w in lb(6)]
assert len(L5)==6 and len(L6)==9
special_map=s.Matrix.hstack(*[col(bracket(a,y),r6) for a in L5],*[col(bracket(x,a),r6) for a in L5])
assert special_map.rank()==9 and len(special_map.nullspace())==3
pair_columns=[col(D[0],r5).col_join(col(D[1],r5)) for D in [eps,T,T2]]
assert s.Matrix.hstack(*pair_columns).rank()==3
print('PASS: dim L5=6, dim L6=9, special derivation dimension=3; displayed basis has rank3')

X,Y=s.symbols('X Y')
def ma(A,B):return tuple(s.expand(a+b) for a,b in zip(A,B))
def ms(A,c):return tuple(s.expand(c*a) for a in A)
def mb(A,B):
    a,b,P=A;c,d,Q=B
    return (0,0,s.expand(a*d-b*c+(a*X+b*Y)*Q-(c*X+d*Y)*P))
@lru_cache(None)
def meta_word(w):
    if w=='x':return (1,0,0)
    if w=='y':return (0,1,0)
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return mb(meta_word(w[:i]),meta_word(w[i:]))
L5matrix=s.Matrix.hstack(*[col(a,r5) for a in L5])
def meta_poly(a):
    cs=L5matrix.gauss_jordan_solve(col(a,r5))[0]
    out=(0,0,0)
    for c,w in zip(cs,lb(5)):out=ma(out,ms(meta_word(w),c))
    return out[2]
expected=[X*X,2*X*Y,2*Y*Y]
for name,D,beta in zip(['epsilon4','T4','F0^2 epsilon4'],[eps,T,T2],expected):
    p,q=meta_poly(D[0]),meta_poly(D[1])
    assert s.expand(p-X*beta)==0 and s.expand(q-Y*beta)==0
    print('PASS: metabelian beta('+name+') =',beta)
assert s.Matrix([[s.Poly(b,X,Y).coeff_monomial(m) for b in expected] for m in [X*X,X*Y,Y*Y]]).det()==4
print('PASS: degree4 comparison determinant=4, so an isomorphism over Q at every prime')

for ch,target,counts in [('x',T[0],(3,2)),('y',T[1],(2,3))]:
    inner=[bracket({'%s'%ch:1},standard(w)) for w in lb(4) if w.count('x')==2]
    rows=[w for w in r5 if w.count('x')==counts[0]]
    M=s.Matrix.hstack(*[col(a,rows) for a in inner])
    assert M.rank()==1 and M.row_join(col(target,rows)).rank()==2
    print('PASS: T4('+ch+') is outside ['+ch+',L4]; ranks1 and2')
for p,trace in [(5,-2),(13,6)]:
    n=1+sum((j*j-i*i*i+i)%p==0 for i in range(p) for j in range(p))
    assert p+1-n==trace
    alpha=trace/s.Integer(2)+2*s.I
    assert s.expand(alpha*s.conjugate(alpha))==p
    ratio=s.simplify(alpha/s.conjugate(alpha))
    assert all(s.simplify(ratio-z)!=0 for z in [1,-1,s.I,-s.I])
    print('PASS: E0/F_'+str(p)+' trace='+str(trace)+'; eigenvalue ratio='+str(ratio)+' is not a root of unity in Q(i)')
print('LIMIT: Ishii nonvanishing and Nakamura comparison formulas are source/theorem dependencies, not outputs of this script.')
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-_started,'.9f'))
