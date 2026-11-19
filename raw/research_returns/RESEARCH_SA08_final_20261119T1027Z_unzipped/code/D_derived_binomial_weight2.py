#!/usr/bin/env python3
"""Integral weight-two counterexample to a naive derived-binomial bridge.
All matrices are constructed over Z.  The finite simplicial set is sk_2 B(C_2),
with one nondegenerate simplex in dimensions 0,1,2.  Its reduced normalized
chains have d_2=2.  This is a certificate for A-022, not a numerical approximation.
"""
import itertools
import json
from pathlib import Path
import time
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

start=time.perf_counter()
checks=0

def chk(c):
    global checks
    assert c
    checks+=1

def kron(A,B):
    if not A.rows or not A.cols or not B.rows or not B.cols:
        return sp.zeros(A.rows*B.rows,A.cols*B.cols)
    return sp.kronecker_product(A,B)

def pairs(r):
    return [(i,j) for i in range(r) for j in range(i,r)]

def gamma2(A):
    m,n=A.shape
    out=sp.zeros(len(pairs(m)),len(pairs(n)))
    for c,(i,j) in enumerate(pairs(n)):
        for r,(a,b) in enumerate(pairs(m)):
            if i==j:
                out[r,c]=A[a,i]*A[b,i]
            elif a==b:
                out[r,c]=2*A[a,i]*A[a,j]
            else:
                out[r,c]=A[a,i]*A[b,j]+A[b,i]*A[a,j]
    return out

def exterior2(A):
    m,n=A.shape
    src=list(itertools.combinations(range(n),2))
    dst=list(itertools.combinations(range(m),2))
    return sp.Matrix(len(dst),len(src),lambda r,c:
        A[dst[r][0],src[c][0]]*A[dst[r][1],src[c][1]]-
        A[dst[r][0],src[c][1]]*A[dst[r][1],src[c][0]])

def face_phi(n,i):
    A=sp.zeros(n,n+1)
    A[0,0]=1
    for j in range(1,n+1):
        if i==0:
            A[0 if j==1 else j-1,j]=1
        elif i==n:
            if j<n: A[j,j]=1
        else:
            A[j if j<=i else j-1,j]=1
    return A

def face_psi(n,i):
    return face_phi(n,i)[1:,1:]

def d_vertical(n):
    return sp.eye(n).row_join(sp.zeros(n,1))[:,[n]+list(range(n))]

def diag_gamma(r):
    A=sp.zeros(r*r,len(pairs(r)))
    for c,(i,j) in enumerate(pairs(r)):
        A[i*r+j,c]=1
        if i!=j:A[j*r+i,c]=1
    return A

def wedge_projection(r):
    ix=list(itertools.combinations(range(r),2))
    A=sp.zeros(len(ix),r*r)
    for a,(i,j) in enumerate(ix):
        A[a,i*r+j]=1;A[a,j*r+i]=-1
    return A

def divided_derivative(n):
    d=d_vertical(n)
    A=sp.zeros((n+1)*n,len(pairs(n+1)))
    for c,(i,j) in enumerate(pairs(n+1)):
        for b in range(n):
            A[i*n+b,c]+=d[b,j]
            if i!=j:A[j*n+b,c]+=d[b,i]
    return A

def basis_vector(kind,n,terms):
    if kind=='G':idx=pairs(n+1)
    elif kind=='P':idx=[(a,b) for a in range(n+1) for b in range(1,n+1)]
    elif kind=='R':idx=pairs(n)
    elif kind=='Q':idx=[(a,b) for a in range(1,n+1) for b in range(1,n+1)]
    elif kind=='E':idx=list(itertools.combinations(range(1,n+1),2))
    out=sp.zeros(len(idx),1)
    for key,val in terms.items():out[idx.index(key),0]+=val
    return out

def B(kind,n):
    # Gamma² Phi =G; Phi tensor Psi=P; Gamma² Psi=R;
    # Psi tensor Psi=Q; exterior² Psi=E.
    terms={
      ('G',0):[{(0,0):1}],
      ('G',1):[{(0,1):1},{(1,1):1}],
      ('G',2):[{(1,2):1,(2,2):-2}],
      ('P',1):[{(0,1):1},{(1,1):1}],
      ('P',2):[{(1,2):1,(2,2):-1},{(2,1):1,(2,2):-1}],
      ('R',1):[{(0,0):1}],
      ('R',2):[{(0,1):1,(1,1):-2}],
      ('Q',1):[{(1,1):1}],
      ('Q',2):[{(1,2):1,(2,2):-1},{(2,1):1,(2,2):-1}],
      ('E',2):[{(1,2):1}],
    }.get((kind,n),[])
    z=basis_vector(kind,n,{})
    return sp.Matrix.hstack(*(basis_vector(kind,n,t) for t in terms)) if terms else sp.zeros(z.rows,0)

def face(kind,n,i):
    f=face_phi(n,i);g=face_psi(n,i)
    return {'G':lambda:gamma2(f),'P':lambda:kron(f,g),
            'R':lambda:gamma2(g),'Q':lambda:kron(g,g),
            'E':lambda:exterior2(g)}[kind]()

def full_kernel(A,K):
    chk(A*K==sp.zeros(A.rows,K.cols))
    chk(A.cols-A.rank()==K.cols)
    if K.cols:
        # A unimodular maximal minor makes the proposed kernel lattice saturated.
        chk(any(abs(K[list(rs),:].det())==1 for rs in itertools.combinations(range(K.rows),K.cols)))

def coefficients(K,V):
    if K.cols==0:
        chk(V==sp.zeros(V.rows,V.cols));return sp.zeros(0,V.cols)
    X=K.gauss_jordan_solve(V)[0]
    chk(all(x.q==1 for x in X));chk(K*X==V)
    return X

normals={}
for kind in 'GPRQE':
    for n in range(1,4):
        A=sp.Matrix.vstack(*(face(kind,n,i) for i in range(1,n+1)))
        full_kernel(A,B(kind,n))
    normals[kind]=[coefficients(B(kind,n-1),face(kind,n,0)*B(kind,n)) for n in (1,2)]

# Vertical maps, normalized in each simplicial degree.
kv={0:[],1:[]};cv={0:[],1:[]}
for n in (0,1,2):
    der=divided_derivative(n);d=d_vertical(n)
    k1=wedge_projection(n)*kron(d,sp.eye(n))
    k0=coefficients(B('P',n),der*B('G',n))
    k1n=coefficients(B('E',n),k1*B('P',n))
    kv[0].append(k0);kv[1].append(k1n)
    c0=sp.Matrix.vstack(k0,coefficients(B('R',n),gamma2(d)*B('G',n)))
    c1=sp.Matrix.hstack(
        coefficients(B('Q',n),kron(d,sp.eye(n))*B('P',n)),
        coefficients(B('Q',n),-diag_gamma(n)*B('R',n)))
    cv[0].append(c0);cv[1].append(c1)
    chk(k1n*k0==sp.zeros(k1n.rows,k0.cols))
    chk(c1*c0==sp.zeros(c1.rows,c0.cols))

# Reduced Hom(sk_2 B(C2),Y): pairs (f1,f2), with df1=0 and df2=2f1.
HG=sp.Matrix([1,-2,2])
HP=sp.Matrix([[1,0],[0,1],[2,0],[-2,-2]])
HR=sp.Matrix([1,-1])
HQ=sp.Matrix([[1,0],[0,1],[-2,-1]])
HE=sp.eye(1)
Hs={'G':HG,'P':HP,'R':HR,'Q':HQ,'E':HE}
for kind,H in Hs.items():
    d1,d2=normals[kind]
    a=B(kind,1).cols;b=B(kind,2).cols
    relation=sp.Matrix.vstack(sp.Matrix.hstack(d1,sp.zeros(d1.rows,b)),
                             sp.Matrix.hstack(-2*sp.eye(a),d2))
    full_kernel(relation,H)

HC1=sp.Matrix([[1,0,0],[0,1,0],[0,0,1],[2,0,0],[-2,-2,0],[0,0,-1]])
KC0=coefficients(HP,sp.diag(kv[0][1],kv[0][2])*HG)
KC1=coefficients(HE,sp.diag(kv[1][1],kv[1][2])*HP)
CC0=coefficients(HC1,sp.diag(cv[0][1],cv[0][2])*HG)
CC1=coefficients(HQ,sp.diag(cv[1][1],cv[1][2])*HC1)
chk(KC0==sp.Matrix([1,-2]));chk(KC1==sp.Matrix([[4,2]]))
chk(CC0==sp.Matrix([1,-2,-2]));chk(CC1==sp.Matrix([[0,1,-1],[2,0,1]]))
full_kernel(KC1,KC0);full_kernel(CC1,CC0)
chk(smith_normal_form(KC1,domain=ZZ)==sp.Matrix([[2,0]]))
SC=smith_normal_form(CC1,domain=ZZ)
chk(sorted(abs(SC[i,i]) for i in range(2))==[1,1])

# X=S²: d2=0.  Exterior projection sends the tensor cycle x-y to 2z.
Q_cycle=sp.Matrix([1,-1])
chk(normals['Q'][1]*Q_cycle==sp.zeros(1,1))
proj2=coefficients(B('E',2),wedge_projection(2)*B('Q',2))
chk(proj2*Q_cycle==sp.Matrix([2]))

def arr(M):return [list(map(int,M.row(i))) for i in range(M.rows)]
result={
 'statement':'A-022',
 'scope':'Exact integral matrices, dimensions <=3, weight 2; all normalization kernels checked as saturated Z-lattices.',
 'finite_simplicial_set':'sk_2 B(C2), one nondegenerate simplex in dimensions 0,1,2',
 'reduced_chain_d2':[[2]],
 'normalized_horizontal_differentials':{k:[arr(v) for v in vs] for k,vs in normals.items()},
 'koszul_reduced_sections':{'d0':arr(KC0),'d1':arr(KC1),'H0':0,'H1':0,'H2':'Z/2'},
 'cosimplicial_gamma_reduced_sections':{'d0':arr(CC0),'d1':arr(CC1),'H0':0,'H1':0,'H2':0},
 'sphere_comparison_on_H2':[[2]],
 'assertions_passed':checks,
 'elapsed_seconds':time.perf_counter()-start,
}
out=Path(__file__).resolve().parents[1]/'logs'/'D_derived_binomial_weight2.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
