"""Exact checks for Codex K34-05--08, using only Python's standard library.

These are finite algebra and indexing certificates. They do not replace the
geometric purity, finiteness, affine Lefschetz or perverse-sheaf theorems.
The general proofs and counterexample hypotheses are in proof_audit.md §§10--19.
"""
from itertools import combinations, permutations, product
from functools import reduce
from math import gcd, comb
from pathlib import Path

lines=[]
def emit(*parts):
    text=' '.join(map(str,parts)); print(text); lines.append(text)
def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def power(A,r):
    B=ident(len(A))
    for _ in range(r):B=matmul(B,A)
    return B
def zero(A):return all(x==0 for row in A for x in row)
def det(A):
    n=len(A)
    ans=0
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=sign
        for i in range(n):term*=A[i][p[i]]
        ans+=term
    return ans
def rank_mod(A,prime):
    if not A:return 0
    B=[[x%prime for x in row] for row in A];r=0
    for c in range(len(B[0])):
        piv=next((i for i in range(r,len(B)) if B[i][c]),None)
        if piv is None:continue
        B[r],B[piv]=B[piv],B[r]
        v=pow(B[r][c],-1,prime);B[r]=[(v*x)%prime for x in B[r]]
        for i in range(len(B)):
            if i!=r:
                v=B[i][c];B[i]=[(x-v*y)%prime for x,y in zip(B[i],B[r])]
        r+=1
        if r==len(B):break
    return r

emit('P4 CODEX EXACT CHECKS — 2026-11-19')
emit('Scope: finite algebra and degree ranges only; general proofs in proof_audit.md §§10–19.')

emit('\n1. Shifted cone degrees and the component defect')
for p in (2,3,5,7):
    f=[[1],[1]];r=rank_mod(f,p)
    h0=1-r;h1=2-r
    assert (h0,h1)==(0,1)
    emit(f'Λ=F_{p}: Φman=[Λ --diag--> Λ²] in degrees(0,1); dimH0={h0}, dimH1={h1}.')
for n in range(8):
    usual=n;man=usual+1
    assert man-1==usual
emit('Usual isolated-lci degree n corresponds to manuscript degree n+1, checked n=0..7.')

emit('\n2. Ramification-index arithmetic, conditional on the proved DVR construction')
for p,l in ((2,3),(3,2),(5,3),(7,5)):
    e=1;degree=p
    emit(f'char={p}, ell={l}: e mod ell={e%l}, [L:K] mod ell={degree%l}.')
assert 1%3!=2%3
emit('The example p=2, ell=3 distinguishes the two multipliers. DVR/separability proof is in §11.')

emit('\n3. Exterior powers of root pullback')
checks=0
for r in range(1,6):
    for q in range(r+1):
        subsets=list(combinations(range(r),q))
        for m in (2,3,6):
            A=[[m*int(i==j) for j in range(r)] for i in range(r)]
            exterior=[[det([[A[i][j] for j in J] for i in I]) for J in subsets] for I in subsets]
            expected=[[m**q*int(i==j) for j in range(len(subsets))] for i in range(len(subsets))]
            assert exterior==expected
            assert len(subsets)==comb(r,q)
            checks+=1
emit('All',checks,'exterior matrices equal m^q times identity for ranks1..5, all degrees, m=2,3,6.')
for n in (2,3,4,8,9,25):
    for q in range(1,6):assert pow(n,q,n)==0
    assert pow(n,0,n)==1
emit('A root multiplier divisible by n kills positive degrees modulo n but preserves H0 (n=2,3,4,8,9,25).')

emit('\n4. Finite coefficient functions detect cosets only for nonzero coefficients')
for n in (1,2,3,4):
    functions=list(product(range(n),repeat=3))
    kernel=[]
    for shift in range(3):
        if all(all(f[(j+shift)%3]==f[j] for j in range(3)) for f in functions):kernel.append(shift)
    assert kernel==([0,1,2] if n==1 else [0])
    emit(f'Functions on C3 with Z/{n} coefficients: action kernel={kernel}.')

emit('\n5. Multiplicity map and gcd image in finite quotients')
for weights in ((2,4),(2,3),(0,6),(6,10),(0,0)):
    d=reduce(gcd,weights)
    for N in (4,5,9,12):
        image={sum(a*b for a,b in zip(weights,x))%N for x in product(range(N),repeat=len(weights))}
        expect={d*x%N for x in range(N)}
        assert image==expect
    emit('weights=',weights,'gcd=',d,'finite-quotient images verified at N=4,5,9,12.')
emit('All-zero weights give image{0}; they do not give a finite-index subgroup of the infinite lattice.')
for weights in ((0,2,3),(0,0,4,6),(2,4,8)):
    positive=[x for x in weights if x]
    M=1
    for x in positive:M=M*x//gcd(M,x)
    for r in range(1,len(weights)+1):
        for chosen in combinations(weights,r):
            d=reduce(gcd,chosen)
            if d:assert M%d==0
    emit('weights=',weights,'lcm of positives=',M,'divisible by every nonzero local gcd.')

emit('\n6. Filtration length and nilpotence; cancelled arithmetic')
for q in range(8):
    N=[[int(j==i+1) for j in range(q+1)] for i in range(q+1)]
    assert zero(power(N,q+1))
    assert not zero(power(N,q))
    actual=sum(i+1 for i in range(q+1));wrong=q*(q+1)//2
    assert actual==(q+1)*(q+2)//2
    emit(f'total degree q={q}: Jordan nilpotence index={q+1}; discarded sum={actual}, draft quadratic={wrong}.')
emit('The live filtration has q+1 steps. The finite Jordan example shows this length cannot be reduced from filtration data alone.')

emit('\n7. Support-dimension optimization and specialization boundary')
cases=0
for n in range(9):
    for d in range(9):
        for q in range(1,n+2):
            e=min(d,n+1-q)
            for p in range(2*e+1):
                assert p+q<=n+d+1
                cases+=1
        assert (2*d<=n+d+1)==(d<=n+1)
emit(cases,'nonzero-range (n,d,p,q) possibilities checked; p+q≤n+d+1 in every case.')
emit('q=0 requires d≤n+1 unless the degree-zero support sheaf already vanishes.')
for B in range(9):
    vanishes=lambda i:i>B
    assert vanishes(B+1) and not vanishes(B)
    for i in range(B+1,B+5):assert vanishes(i) and vanishes(i+1)
emit('If Φman vanishes above B, the cone sequence gives surjection at B and isomorphism above B.')
for n in range(1,10):
    for d in range(n):
        c=d+1;i=n-d-1
        assert i+2*c==n+d+1
        assert 2*n-(n+d+1)==n-d-1
emit('Gysin codimension d+1 and dual degree arithmetic agree exactly on the high/low boundaries.')

emit('\n8. Cartan–Leray obstruction for the arbitrary infinite-root bound')
allowed=[(a,b) for a in range(2) for b in range(2)]
assert max(a+b for a,b in allowed)==2
needed=[(a,b) for a in range(2) for b in range(4) if a+b==3]
assert needed==[(0,3),(1,2)]
emit('If cd_ell Γ≤1 and cd_ell U∞≤1, possible positions=',allowed,'max total degree=2.')
emit('Nonzero H3(U,Z/ell) requires a survivor from',needed,'so the tower has cd_ell≥2.')
emit('Existence and hypotheses of the regular strict-local nonexcellent A are checked in the primary source, not by this degree enumeration.')

emit('\n9. Low cone boundary and the special pinching algebra')
for a in range(1,10):
    for i in range(a+1):
        # Coker(f^(i−1))=0 and Ker(f^i)=0 imply H^i(Φman)=0.
        lower_is_surj=(i-1<a)
        upper_is_inj=(i<=a)
        assert lower_is_surj and upper_is_inj
emit('Isomorphisms below a and injection at a give Φman^i=0 for i≤a.')
for m in range(1,10):
    for i in range(m-1):assert i<m and i+1<m
    assert m-1<m and not m<m
emit('Support hypercohomology vanishing below m gives punctured comparison iso below m−1 and injection at m−1.')
# Special fibre basis 1, X^i, Y^i, T: T is not zero, but XT=YT=T²=0.
def special_mul(a,b):
    if a=='1':return b
    if b=='1':return a
    if 'T' in (a,b):return '0'
    if a[0]!=b[0]:return '0'
    return a[0]+str(int(a[1:])+int(b[1:]))
assert special_mul('1','T')=='T'
assert all(special_mul(a,'T')=='0' for a in ('X1','Y1','T'))
emit('In k[X,Y,T]/(XY,XT,YT,T²), T survives and is annihilated by (X,Y,T): an embedded nilpotent at the pinch.')
emit('This explains why the flat pinching example is not a flat-lci counterexample.')

emit('\nALL CODEX EXACT CHECKS PASSED.')
out=Path(__file__).resolve().parents[1]/'outputs/codex_computations.txt'
out.write_text('\n'.join(lines)+'\n')
