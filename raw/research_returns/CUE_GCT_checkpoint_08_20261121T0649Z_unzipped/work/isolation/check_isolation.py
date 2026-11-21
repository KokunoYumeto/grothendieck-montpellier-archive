#!/usr/bin/env python3
"""Exact small-case checks of deductions, not a formal proof certificate."""
from itertools import product, combinations, permutations
from pathlib import Path
import sympy as s

out=[]
def note(msg):
    out.append(msg)
    print(msg)

def rank_mod(rows,p):
    a=[list(map(lambda x:int(x)%p,row)) for row in rows]
    if not a:return 0
    r=0
    for c in range(len(a[0])):
        q=next((j for j in range(r,len(a)) if a[j][c]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r]
        z=pow(a[r][c],-1,p)
        a[r]=[(z*x)%p for x in a[r]]
        for j in range(len(a)):
            if j!=r and a[j][c]:
                z=a[j][c]
                a[j]=[(x-z*y)%p for x,y in zip(a[j],a[r])]
        r+=1
        if r==len(a):break
    return r

# I-03 and I-04: check against every functional over F_5 for two examples.
exponents=[(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)]
examples=[[(1,0),(0,1),(1,1),(1,2),(2,1),(0,0)],
          [(1,0),(1,0),(0,1),(0,1),(1,1),(1,1)]]
case_count=0
for coeffs in examples:
    bases=[B for B in combinations(range(6),2)
           if rank_mod([coeffs[j] for j in B],5)==2]
    for weight in product(range(-3,4),repeat=2):
        wt=[sum(x*y for x,y in zip(a,weight)) for a in exponents]
        biwa=False
        for B in bases:
            if wt[B[0]]==wt[B[1]]:continue
            good=True
            for j in range(6):
                if j in B:continue
                lower=[coeffs[b] for b in B if wt[b]<wt[j]]
                if rank_mod(lower+[coeffs[j]],5)!=rank_mod(lower,5):
                    good=False;break
            if good:biwa=True;break
        all_projections=True
        for lam in product(range(5),repeat=2):
            if lam==(0,0):continue
            nonzero=[j for j,v in enumerate(coeffs)
                     if sum(x*y for x,y in zip(v,lam))%5]
            low=min(wt[j] for j in nonzero)
            if sum(wt[j]==low for j in nonzero)!=1:
                all_projections=False;break
        assert biwa==all_projections,(coeffs,weight)
        total={B:sum(wt[j] for j in B) for B in bases}
        best=min(total.values())
        minimizers=[B for B in bases if total[B]==best]
        images={tuple(sum(exponents[j][i] for j in B) for i in range(2))
                for B in minimizers}
        if len(images)==1:assert len(minimizers)==1
        case_count+=1
note(f'I-03/I-04: {case_count} exact F_5 cases checked; BIWA dual equivalence and unique exposed-image fiber passed.')

# I-06 actual Hoza base-six digit property.
codes=list(product([0,1],repeat=3)); count=0
for triple in permutations(codes,3):
    for seed in codes:
        h=[sum(6**(2-j)*c[j]*seed[j] for j in range(3)) for c in triple]
        assert (h[0]+h[2]==2*h[1])==(h[0]==h[1]==h[2])
        count+=1
note(f'I-06: {count} three-codeword/seed cases checked exactly; arithmetic-progression criterion passed.')
for d,nmax in [(1,5),(2,3),(3,2)]:
    H=s.Matrix([[2**((a+b)**2) for b in range(d+1)] for a in range(d+1)])
    assert H.rank()==d+1
    for n in range(1,nmax+1):
        K=H
        for i in range(n-1):K=s.kronecker_product(K,H)
        assert K.rank()==(d+1)**n
note('I-06: exact rational Hankel/tensor ranks passed for (d,n)=(1,1..5),(2,1..3),(3,1..2).')

# I-05 counterexample.
x,y,t=s.symbols('x y t')
D=s.Matrix([x,y]); G=s.det(s.diag(x,y))
assert G.subs({x:t,y:t})==t*t
assert s.Matrix.hstack(s.Matrix([1,0]),s.Matrix([0,1])).rank()==2
assert s.Matrix([1,1]).rank()==1
note('I-05: Gram determinant t^2 survives while coefficient span drops from 2 to 1.')

# I-09 exact complex transfer contraction.
I=s.I
u=s.Matrix([1,I]);v=s.Matrix([2,-I])
A=[
 [s.Matrix([[1,2],[0,1]]),s.Matrix([[I,0],[1,-1]]),s.Matrix([[0,1],[2,I]])],
 [s.Matrix([[0,1],[1,0]]),s.Matrix([[2,I],[1,1]]),s.Matrix([[1,0],[0,-I]])],
 [s.Matrix([[1,1],[I,0]]),s.Matrix([[0,2],[-1,1]]),s.Matrix([[I,1],[0,1]])]
]
norm=0
for word in product(range(3),repeat=3):
    q=s.eye(2)
    for i,a in enumerate(word):q=q*A[i][a]
    c=s.expand((u.T*q*v)[0])
    norm+=s.expand(c*s.conjugate(c))
T=s.eye(4)
for layer in A:
    T=T*sum((s.kronecker_product(a,s.conjugate(a)) for a in layer),s.zeros(4))
contract=s.expand((s.kronecker_product(u,s.conjugate(u)).T*T*
                   s.kronecker_product(v,s.conjugate(v)))[0])
assert s.simplify(norm-contract)==0
note(f'I-09: exact 3-variable width-2 degree-2 complex example passed; squared norm={norm}.')

note('These computations supplement, and do not replace, the full proof readings recorded separately.')
Path(__file__).with_name('computation_checks.txt').write_text('\n'.join(out)+'\n')
