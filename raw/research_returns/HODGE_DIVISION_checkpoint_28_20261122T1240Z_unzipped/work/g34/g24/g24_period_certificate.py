#!/usr/bin/env python3
"""Exact G24 twelve-branch parabolic-monodromy certificate.

Field: Q[alpha]/(alpha^2+alpha+2). The scalar arithmetic and elementary
linear algebra are adapted from the independent G34 certificate.
The group, tuple words and nine boundary intervals are specified here;
no precomputed cohomology basis or logarithm is used.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from collections import deque
from pathlib import Path
import json, time

@dataclass(frozen=True)
class K:
    a: F = F(0)
    b: F = F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a))
        object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def c(v): return v if isinstance(v,K) else K(v)
    def __add__(s,t):
        t=K.c(t); return K(s.a+t.a,s.b+t.b)
    __radd__=__add__
    def __neg__(s): return K(-s.a,-s.b)
    def __sub__(s,t): return s+-K.c(t)
    def __rsub__(s,t): return K.c(t)+-s
    def __mul__(s,t):
        t=K.c(t); return K(s.a*t.a-2*s.b*t.b,s.a*t.b+s.b*t.a-s.b*t.b)
    __rmul__=__mul__
    def bar(s): return K(s.a-s.b,-s.b)
    def __truediv__(s,t):
        t=K.c(t); n=(t*t.bar()).a
        if not n: raise ZeroDivisionError
        r=s*t.bar(); return K(r.a/n,r.b/n)
    def __rtruediv__(s,t): return K.c(t)/s
    def __bool__(s): return bool(s.a or s.b)
    def __str__(s): return f'({s.a})+({s.b})alpha'
    def pair(s): return [str(s.a),str(s.b)]

z=K(); o=K(1); w=K(0,1)
def zero(m,n): return [[z for _ in range(n)] for _ in range(m)]
def eye(n): return [[K(i==j) for j in range(n)] for i in range(n)]
def transpose(A): return [list(x) for x in zip(*A)]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def neg(A): return [[-x for x in r] for r in A]
def sub(A,B): return add(A,neg(B))
def mul(A,B):
    Bt=transpose(B)
    return [[sum((x*y for x,y in zip(a,b) if x and y),z) for b in Bt] for a in A]
def mv(A,v): return [sum((x*y for x,y in zip(a,v) if x and y),z) for a in A]
def cols(A,js): return [[r[j] for j in js] for r in A]
def hcat(*As): return [sum((list(A[i]) for A in As),[]) for i in range(len(As[0]))]
def iszero(A): return not any(any(r) for r in A)
def rref(A):
    A=[list(r) for r in A]; p=[]; r=0
    for j in range(len(A[0])):
        k=next((i for i in range(r,len(A)) if A[i][j]),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]; c=A[r][j]; A[r]=[x/c for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][j]:
                c=A[i][j]; A[i]=[x-c*y for x,y in zip(A[i],A[r])]
        p.append(j); r+=1
        if r==len(A): break
    return A,p
def rank(A): return len(rref(A)[1])
def det(A):
    A=[list(row) for row in A]; n=len(A); out=o
    assert all(len(row)==n for row in A)
    for j in range(n):
        k=next((i for i in range(j,n) if A[i][j]),None)
        if k is None: return z
        if k!=j: A[j],A[k]=A[k],A[j]; out=-out
        p=A[j][j]; out=out*p
        for i in range(j+1,n):
            c=A[i][j]/p
            for l in range(j+1,n): A[i][l]=A[i][l]-c*A[j][l]
    return out
def null(A):
    R,p=rref(A); free=[i for i in range(len(A[0])) if i not in p]
    out=zero(len(A[0]),len(free))
    for j,f in enumerate(free):
        out[f][j]=o
        for i,pi in enumerate(p): out[pi][j]=-R[i][f]
    return out
def inv(A):
    n=len(A); R,p=rref(hcat(A,eye(n))); assert p[:n]==list(range(n))
    assert cols(R,list(range(n)))==eye(n)
    return cols(R,list(range(n,2*n)))
def rowbasis_inverse(A):
    # A has independent columns. Return J with J A = I.
    piv=rref(transpose(A))[1]; B=[A[i] for i in piv]; Bi=inv(B)
    J=zero(len(piv),len(A))
    for i in range(len(piv)):
        for j,p in enumerate(piv): J[i][p]=Bi[i][j]
    assert mul(J,A)==eye(len(piv)); return J
def hermdot(v,u): return sum((x.bar()*y for x,y in zip(v,u)),z)

alpha=w
H=[[K(2),K(-1),-alpha],[K(-1),K(2),K(-1)],[1+alpha,K(-1),K(2)]]
base=[[[K.c(x) for x in row] for row in A] for A in [
 [[-1,1,alpha],[0,1,0],[0,0,1]],
 [[1,0,0],[1,-1,1],[0,0,1]],
 [[1,0,0],[0,1,0],[-1-alpha,1,-1]]]]
words=[[2,0,2],[2,0,1,2,0,2,1,0,2],[1],
       [0,2,0,1,2,1,0,2,0],[0],[2]]
intervals=[(1,2),(3,4),(1,4),(5,6),(1,6),
           (7,8),(9,10),(7,10),(7,11)]
def conjtrans(A):return [[x.bar() for x in row] for row in transpose(A)]
def serialize(A):return [[x.pair() for x in row] for row in A]
def evalword(word):
 A=eye(3)
 for i in word:A=mul(A,base[i])
 return A
refs=[evalword(word) for word in words]
def vector_beta(s):
 D=sub(eye(3),s)
 j=next(j for j in range(3) if any(D[i][j] for i in range(3)))
 v=[D[i][j] for i in range(3)]
 i=next(i for i,x in enumerate(v) if x)
 b=[x/v[i] for x in D[i]]
 assert [[x*y for y in b] for x in v]==D
 assert sum((x*y for x,y in zip(v,b)),z)==K(2)
 return v,b

def main():
 start=time.time();report={}
 assert det(H)==o
 for s in base+refs:
  assert mul(s,s)==eye(3) and rank(sub(eye(3),s))==1
  assert mul(conjtrans(s),mul(H,s))==H
 assert [refs[i] for i in [4,2,5]]==base
 report['generation_reason']='The six reflections contain s1,s2,s3 at positions5,3,6; exact group order336 is separately certified.'
 report['field']='alpha^2+alpha+2=0; conjugate(alpha)=-1-alpha'
 report['base_reflections']=list(map(serialize,base))
 report['tuple_reflection_words_zero_based']=words
 report['tuple_reflections']=list(map(serialize,refs))
 report['hermitian_form']=serialize(H)
 assert len(intervals)==12-3
 assert all(2<=b-a+1<=10 for a,b in intervals)
 assert all(b<c or d<a or (a<=c and d<=b) or (c<=a and b<=d)
            for a,b in intervals for c,d in intervals)
 report['maximal_laminar_intervals_one_based']=intervals

 vb=[vector_beta(s) for s in refs]
 vr=[v for v,b in vb for _ in range(2)]
 beta=[b for v,b in vb for _ in range(2)]
 gs=[s for s in refs for _ in range(2)]
 P=eye(3);relation=[]
 for v,s in zip(vr,gs):
  relation.append(mv(P,v));P=mul(P,s)
 assert P==eye(3)
 C=transpose(relation);Z=null(C);B=neg(beta)
 assert iszero(mul(C,B)) and rank(C)==3 and rank(B)==3
 assert len(Z[0])==9
 comb=hcat(B,Z);piv=rref(comb)[1]
 assert piv[:3]==[0,1,2] and len(piv)==9
 Q=cols(comb,piv[3:]);E=hcat(B,Q);PJ=rowbasis_inverse(E)[3:]
 assert iszero(mul(PJ,B)) and mul(PJ,Q)==eye(6)
 report['parabolic_dimensions']={'relation_rank':3,'cocycle_dimension':9,'coboundary_rank':3,'quotient_dimension':6}
 report['root_vectors']=serialize([v for v,b in vb])
 report['root_covectors']=serialize([b for v,b in vb])
 report['quotient_basis_scalar_cocycles']=serialize(Q)
 report['quotient_projection']=serialize(PJ)
 logs=[];returns=[];localmon=[]
 for l,r in intervals:
  l-=1;r-=1;c=eye(3);D=zero(3,12)
  for i in range(l,r+1):
   v=mv(c,vr[i])
   for j in range(3):D[j][i]=v[j]
   c=mul(c,gs[i])
  if c==eye(3):k=1;Dk=D
  else:
   assert mul(c,c)==eye(3)
   k=2;Dk=mul(add(eye(3),c),D)
   assert any(mul(c,gs[i])!=mul(gs[i],c) for i in range(l,r+1))
  M=eye(12)
  for i in range(l,r+1):M[i]=[x+y for x,y in zip(M[i],mul([beta[i]],Dk)[0])]
  assert iszero(mul(C,mul(M,Z))) and mul(M,B)==B
  T=mul(PJ,mul(M,Q));N=sub(T,eye(6))
  assert iszero(mul(N,N));logs.append(N);returns.append(k);localmon.append(c)
 assert all(iszero(mul(N,M)) for N in logs for M in logs)
 common=rank(hcat(*logs));S=zero(6,6)
 for N in logs:S=add(S,N)
 assert common==3 and rank(S)==3
 assert all(not N[i][j] for N in logs for i in range(6) for j in range(6)
            if not(i<3 and j>=3))
 sumblock=[row[3:] for row in S[:3]]
 assert det(sumblock)==K(-3160)
 flat=[sum(N,[]) for N in logs]
 assert rank(flat)==9
 qflat=[[K(t) for x in row for t in [x.a,x.b]] for row in flat]
 assert rank(qflat)==9
 piv=rref(flat)[1];minor=cols(flat,piv);md=det(minor);assert md
 report['return_powers']=returns
 report['boundary_monodromies']=list(map(serialize,localmon))
 report['log_ranks']=[rank(N) for N in logs]
 report['all_pairwise_log_products_zero']=True
 report['common_image_dimension']=common
 report['sum_log_rank']=rank(S)
 report['all_log_support_top_right_3x3']=True
 report['sum_top_right_block_determinant']=det(sumblock).pair()
 report['K_span_rank']=9;report['Q_span_rank']=9
 report['span_minor']={'entry_coordinates_one_based':[[i//6+1,i%6+1] for i in piv],
                        'determinant':md.pair(),'matrix':serialize(minor)}
 report['logarithms']=list(map(serialize,logs))
 report['elapsed_seconds']=round(time.time()-start,3)
 Path(__file__).with_name('g24_period_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ['logarithms','quotient_projection','quotient_basis_scalar_cocycles','boundary_monodromies','tuple_reflections','span_minor']},indent=2))
 print('Exact 9x9 minor determinant:',md,flush=True)
 print('All exact parabolic-monodromy assertions PASS',flush=True)

if __name__=='__main__':main()

