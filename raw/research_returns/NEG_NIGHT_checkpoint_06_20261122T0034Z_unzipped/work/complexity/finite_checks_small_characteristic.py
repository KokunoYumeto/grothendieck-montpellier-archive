"""Finite checks for C033. These do not verify E or its asymptotic theorem."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

stats={'integral_matrix_parameter_cases':0,'individual_integral_coefficients':0,
       'integer_eigenvector_identities':0,'characteristic_two_fiber_comparisons':0,
       'hasse_crt_matrix_cases':0,'hasse_crt_basis_recoveries':0}

def shifted(a,mask):
    return [a[i^mask] for i in range(len(a))]

def swap_matrix(q,R,A):
    N=1<<q
    coeff=[[0]*N for _ in range(R)]
    coeff[0][0]=1
    for s in range(q):
        for j in range(R-1,0,-1):
            prev=coeff[j-1]
            coeff[j]=[a+b-c for a,b,c in zip(coeff[j],shifted(prev,1<<s),prev)]
    gen=[]
    for j in range(R):
        out=[0]*N
        for l in range(j+1):
            scalar=(2**l*comb(A+l-1,l)) if A else int(l==0)
            out=[x+scalar*y for x,y in zip(out,coeff[j-l])]
        gen.append(out)
    direct=[Fraction(int(i==0)) for i in range(N)]
    total=[Fraction(0) for _ in range(N)]
    for j in range(R):
        if j:
            new=[(2*A+2*j-2-q)*x for x in direct]
            for s in range(q):
                new=[x+y for x,y in zip(new,shifted(direct,1<<s))]
            direct=[x/j for x in new]
        assert direct==gen[j]
        assert all(x.denominator==1 for x in direct)
        stats['individual_integral_coefficients']+=N
        total=[x+y for x,y in zip(total,direct)]
    m=[int(x)*((-1)**A) for x in shifted(total,N-1)]
    for mask in range(N):
        j=mask.bit_count()
        if A<=j<A+R:
            eigen=sum(a*((-1)**((mask&t).bit_count())) for t,a in enumerate(m))
            assert eigen==1
            stats['integer_eigenvector_identities']+=1
    return m

for q in range(1,9):
    for R in range(1,q+1):
        for A in range(q-R+2):
            swap_matrix(q,R,A)
            stats['integral_matrix_parameter_cases']+=1

# F8 = F2[z]/(z^3+z+1).
def mul(a,b):
    out=0
    while b:
        if b&1: out^=a
        b>>=1
        a<<=1
        if a&8: a^=11
    return out

def power(a,k):
    out=1
    while k:
        if k&1: out=mul(out,a)
        a=mul(a,a);k>>=1
    return out

def inv(a):
    assert a
    return power(a,6)

q,R,A=4,3,1
m=swap_matrix(q,R,A)
nodes=[1,2,3,4]
for t,alpha in enumerate(nodes):
    rows=[]
    for u in range(16):
        row=[]
        for y in range(16):
            phi=1
            for s,beta in enumerate(nodes):
                if ((u>>s)&1)==((y>>s)&1):
                    phi=mul(phi,1^mul(alpha,inv(beta)))
            row.append(int(y==u)^mul(m[u^y]%2,1^phi))
        rows.append(row)
    for g in range(2):
        group=[y for y in range(16) if ((y>>t)&1)==g]
        off_target_rows=[u for u in range(16) if ((u>>t)&1)==g]
        seen={}
        for assignment in range(1<<len(group)):
            selected=[y for j,y in enumerate(group) if (assignment>>j)&1]
            measurement=(len(selected),sum((-1)**y.bit_count() for y in selected))
            outputs=[]
            for u in off_target_rows:
                value=0
                for y in selected: value^=rows[u][y]
                outputs.append(value)
            outputs=tuple(outputs)
            if measurement in seen:
                assert outputs==seen[measurement]
                stats['characteristic_two_fiber_comparisons']+=len(outputs)
            else: seen[measurement]=outputs

for J in (2,3,4):
    M=4*J
    V=[]
    for alpha in nodes:
        for j in range(J):
            V.append([mul(comb(u,j)%2,power(alpha,u-j)) if u>=j else 0 for u in range(M)])
    aug=[row[:]+[int(i==j) for j in range(M)] for i,row in enumerate(V)]
    for col in range(M):
        pivot=next(i for i in range(col,M) if aug[i][col])
        aug[col],aug[pivot]=aug[pivot],aug[col]
        scale=inv(aug[col][col]);aug[col]=[mul(scale,x) for x in aug[col]]
        for i in range(M):
            if i!=col and aug[i][col]:
                scale=aug[i][col]
                aug[i]=[x^mul(scale,y) for x,y in zip(aug[i],aug[col])]
    inverse=[row[M:] for row in aug]
    for u in range(M):
        jet=[row[u] for row in V]
        recovered=[]
        for row in inverse:
            x=0
            for a,b in zip(row,jet):x^=mul(a,b)
            recovered.append(x)
        assert recovered==[int(i==u) for i in range(M)]
        stats['hasse_crt_basis_recoveries']+=1
    stats['hasse_crt_matrix_cases']+=1

stats['status']='PASS'
stats['scope']='Finite arithmetic checks only; not a proof of E, asymptotic bounds, or all symbolic instances.'
path=Path(__file__).with_name('FINITE_CHECK_SMALL_CHARACTERISTIC_RESULTS.json')
path.write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps(stats,indent=2))
