#!/usr/bin/env python3
"""Exact certificate for the characteristic-two principal-surface rank proof.

Formal polynomials are sets of exponent vectors over F2.  The Pfaffian
identity is checked symbolically, not by specialization.  The geometric
proof classifies every exceptional coefficient point over an algebraic
closure; its normalized representatives all lie in F4 and are enumerated
here.  The relative-determinant numerical checks are supplementary; the
rank-one determinant calculation is proved in the accompanying TeX.
"""
from collections import Counter
from itertools import product, permutations
from pathlib import Path
from random import Random
from time import perf_counter
import json

started = perf_counter()
pts = list(product(range(3), repeat=2))
index = {p:i for i,p in enumerate(pts)}
directions = [(1,0),(1,1),(1,2),(0,1)]

def direction(a,b):
    x=(a[0]-b[0])%3
    y=(a[1]-b[1])%3
    return 3 if x==0 else y*pow(x,-1,3)%3

lines=[]
for d,(vx,vy) in enumerate(directions):
    for c in range(3):
        line=tuple(i for i,(x,y) in enumerate(pts) if (vx*y-vy*x)%3==c)
        assert len(line)==3
        lines.append((d,line))
assert len({line for d,line in lines})==12

def matchings(xs):
    if not xs:
        yield []
        return
    x=xs[0]
    for j,y in enumerate(xs[1:],1):
        for rest in matchings(xs[1:j]+xs[j+1:]):
            yield [(x,y)]+rest

def toggle(out,m):
    if m in out:out.remove(m)
    else:out.add(m)

def monomial(alpha_powers,section_powers):
    return tuple(alpha_powers+section_powers)

q=set()
for a in range(9):
    ss=[0]*9;ss[a]=3
    toggle(q,monomial([1]*4,ss))
for d,line in lines:
    ss=[0]*9
    for a in line:ss[a]=1
    for other in range(4):
        if other==d:continue
        aa=[0]*4;aa[d]=1;aa[other]=3
        toggle(q,monomial(aa,ss))
assert len(q)==45

pfaffian_terms=[]
matching_count=0
for removed in range(9):
    pf=set()
    for pairs in matchings([a for a in range(9) if a!=removed]):
        matching_count+=1
        aa=[0]*4;ss=[0]*9
        for i,j in pairs:
            aa[direction(pts[i],pts[j])]+=1
            k=index[((-pts[i][0]-pts[j][0])%3,(-pts[i][1]-pts[j][1])%3)]
            ss[k]+=1
        toggle(pf,monomial(aa,ss))
    expected=set()
    for term in q:
        term=list(term);term[4+removed]+=1
        expected.add(tuple(term))
    assert pf==expected
    pfaffian_terms.append(len(pf))
assert matching_count==945

# Independently expand the explicit 3x3 specialization in seven variables.
# First four are alpha0..alpha3; last three are x0,x1,x2.
B=[[(0,0),(1,2),(2,1)],[(2,2),(0,1),(1,0)],[(1,1),(2,0),(0,2)]]
detB=set()
for perm in permutations(range(3)):
    powers=[0]*7
    for i,j in enumerate(perm):
        a,x=B[i][j];powers[a]+=1;powers[4+x]+=1
    toggle(detB,tuple(powers))
predictedB=set()
for i in range(3):
    powers=[0]*7;powers[i]=3;powers[4:]=[1,1,1]
    predictedB.add(tuple(powers))
for i in range(3):
    powers=[1,1,1,0,0,0,0];powers[4+i]=3
    predictedB.add(tuple(powers))
assert detB==predictedB

# F4=F2[zeta]/(zeta^2+zeta+1), encoded by integers0..3.
mul=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
inv=(None,1,3,2)
def power(a,n):
    out=1
    while n:
        if n&1:out=mul[out][a]
        a=mul[a][a];n>>=1
    return out

def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def matmul(A,B):
    n=len(A);m=len(B[0]);l=len(B)
    C=[[0]*m for _ in range(n)]
    for i in range(n):
        for k in range(l):
            if A[i][k]:
                for j in range(m):C[i][j]^=mul[A[i][k]][B[k][j]]
    return C
def rank(A):
    A=[row[:] for row in A];r=0
    for j in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][j]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        scale=inv[A[r][j]]
        A[r]=[mul[scale][x] for x in A[r]]
        for i in range(r+1,len(A)):
            a=A[i][j]
            if a:A[i]=[x^mul[a][y] for x,y in zip(A[i],A[r])]
        r+=1
    return r
def inverse(A):
    n=len(A);B=[row[:]+eye for row,eye in zip(A,ident(n))]
    for j in range(n):
        p=next(i for i in range(j,n) if B[i][j])
        B[j],B[p]=B[p],B[j]
        scale=inv[B[j][j]];B[j]=[mul[scale][x] for x in B[j]]
        for i in range(n):
            if i==j:continue
            a=B[i][j]
            if a:B[i]=[x^mul[a][y] for x,y in zip(B[i],B[j])]
    assert [row[:n] for row in B]==ident(n)
    return [row[n:] for row in B]
def determinant(A):
    A=[row[:] for row in A];out=1;n=len(A)
    for j in range(n):
        p=next((i for i in range(j,n) if A[i][j]),None)
        if p is None:return 0
        A[j],A[p]=A[p],A[j]
        pivot=A[j][j];out=mul[out][pivot]
        scale=inv[pivot];A[j]=[mul[scale][x] for x in A[j]]
        for i in range(j+1,n):
            a=A[i][j]
            if a:A[i]=[x^mul[a][y] for x,y in zip(A[i],A[j])]
    return out

def tensor(alpha):
    T=[[[0]*9 for _ in range(9)] for _ in range(9)]
    for d,line in lines:
        for a,b,c in permutations(line):T[a][b][c]=alpha[d]
    return T
def transformed(T,U):
    n=len(U)
    first=[[[0]*n for _ in range(n)] for _ in range(n)]
    for i,j,k in product(range(n),repeat=3):
        for a in range(n):first[i][j][k]^=mul[U[a][i]][T[a][j][k]]
    second=[[[0]*n for _ in range(n)] for _ in range(n)]
    for i,j,k in product(range(n),repeat=3):
        for b in range(n):second[i][j][k]^=mul[U[b][j]][first[i][b][k]]
    third=[[[0]*n for _ in range(n)] for _ in range(n)]
    for i,j,k in product(range(n),repeat=3):
        for c in range(n):third[i][j][k]^=mul[U[c][k]][second[i][j][c]]
    return third

F=[[0]*9 for _ in range(9)]
for i,(x,y) in enumerate(pts):
    for j,(xx,u) in enumerate(pts):
        if x==xx:F[i][j]=power(2,(u*y)%3)
Finv=inverse(F)
Th=tensor([1,0,0,0])
Tthree=tensor([1,1,1,0])
assert transformed(Th,F)==Tthree

GL2=[]
for a,b,c,d in product(range(3),repeat=4):
    if (a*d-b*c)%3:GL2.append((a,b,c,d))
assert len(GL2)==48

def qcoeff(alpha):
    lead=1
    for a in alpha:lead=mul[lead][a]
    coeff=[]
    for i,a in enumerate(alpha):
        rest=0
        for j,b in enumerate(alpha):
            if i!=j:rest^=power(b,3)
        coeff.append(mul[a][rest])
    return [lead]+coeff

projective=set()
for alpha in product(range(4),repeat=4):
    first=next((a for a in alpha if a),None)
    if first is not None:projective.add(tuple(mul[inv[first]][a] for a in alpha))
assert len(projective)==85
bad=sorted(alpha for alpha in projective if not any(qcoeff(alpha)))
assert len(bad)==40
assert Counter(sum(a!=0 for a in alpha) for alpha in bad)=={1:4,3:36}

projectors=[]
phase_checks=0
log={1:0,2:1,3:2}
for alpha in bad:
    support=[i for i,a in enumerate(alpha) if a]
    T=tensor(alpha)
    if len(support)==1:
        vx,vy=directions[support[0]]
        D=[[0]*9 for _ in range(9)]
        for i,(x,y) in enumerate(pts):D[i][i]=int((vx*y-vy*x)%3==0)
        descriptor={'type':'one_direction','direction':support[0]}
    else:
        coeff=next((u,v,w) for u,v,w in product(range(3),repeat=3)
                   if all((u*x*x+v*x*y+w*y*y)%3==log[alpha[i]]
                          for i in support for x,y in [directions[i]]))
        u,v,w=coeff
        H=[[0]*9 for _ in range(9)]
        for i,(x,y) in enumerate(pts):H[i][i]=power(2,(u*x*x+v*x*y+w*y*y)%3)
        missing=next(i for i in range(4) if not alpha[i])
        target=directions[missing]
        G=next(g for g in GL2 if (g[1]*target[1]-g[3]*target[0])%3==0)
        a,b,c,d=G
        S=[[0]*9 for _ in range(9)]
        for j,(x,y) in enumerate(pts):S[index[((a*x+b*y)%3,(c*x+d*y)%3)]][j]=1
        U=matmul(matmul(H,S),Finv)
        assert transformed(T,U)==Th
        P=[[0]*9 for _ in range(9)]
        for i,(x,y) in enumerate(pts):P[i][i]=int(y==0)
        D=matmul(matmul(U,P),inverse(U))
        descriptor={'type':'three_directions','quadratic':coeff,'index_GL2':G}
        phase_checks+=1
    assert matmul(D,D)==D and rank(D)==3
    for i,j,k in product(range(9),repeat=3):
        left=right=0
        for a in range(9):
            left^=mul[D[a][i]][T[a][j][k]]
            right^=mul[D[a][j]][T[i][a][k]]
        assert left==right
    projectors.append({'alpha':alpha,'basis_change':descriptor,'projector_rows':D})
assert phase_checks==36

# Supplementary exact values of the relative determinant on s0=1.
rng=Random(202611191030)
determinant_checks=0
for alpha in sorted(projective):
    coeff=qcoeff(alpha)
    for _ in range(20):
        s=[1]+[rng.randrange(4) for _ in range(8)]
        M=[[0]*9 for _ in range(9)]
        for i,j in product(range(9),repeat=2):
            if i==j:continue
            k=index[((-pts[i][0]-pts[j][0])%3,(-pts[i][1]-pts[j][1])%3)]
            M[i][j]=mul[alpha[direction(pts[i],pts[j])]][s[k]]
        R=[[M[i][j]^mul[power(s[j],2)][M[i][0]] for j in range(1,9)] for i in range(1,9)]
        cubes=0
        for x in s:cubes^=power(x,3)
        qvalue=mul[coeff[0]][cubes]
        for direction_index,line in lines:
            value=1
            for i in line:value=mul[value][s[i]]
            qvalue^=mul[coeff[1+direction_index]][value]
        assert determinant(R)==mul[power(qvalue,2)][cubes]
        determinant_checks+=1

dimension_checks=0
for f in range(3):
    for d in range(1,10001):
        g=9*d*d+1
        defect=(2-f)*(1 if d%2 else 2)
        r=g-defect-f
        assert r==9*d*d-(1 if d%2 else 3-f)
        if d%2:
            nodes=9*(d*d-1)
            assert 10+nodes==g and 8+f+nodes==r+f
        else:
            intersection=18*(d-1)
            assert 10+(9*(d-1)**2+1)+intersection-1==g
            assert (8+f)+(9*(d-1)**2-1+f)+intersection-1==r+f
        dimension_checks+=1

result={'status':'PASS',
        'symbolic_pfaffian_principal_minors':9,'perfect_matchings_expanded':matching_count,
        'terms_in_each_pfaffian':pfaffian_terms,'pfaffian_cubic_terms':len(q),
        'pfaffian_cubic_exponents_alpha_then_section':sorted(q),
        'specialized_3x3_determinant_terms':sorted(detB),
        'projective_F4_coefficients_checked':len(projective),
        'exceptional_points':len(bad),'exceptional_support_counts':{'1':4,'3':36},
        'quadratic_phase_cases':phase_checks,'Fourier_identity':True,
        'orthogonal_idempotents':projectors,
        'supplementary_relative_determinant_values':determinant_checks,
        'dimension_identities_checked':dimension_checks,
        'elapsed_seconds':perf_counter()-started}
Path(__file__).with_name('A3_ppav_rank_checks_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in
                 ('pfaffian_cubic_exponents_alpha_then_section','orthogonal_idempotents',
                  'specialized_3x3_determinant_terms')},indent=2))
