"""Independent character-average computation for compact U(3) over Q(sqrt(-3)).

No K17 program, neighbor data, harmonic basis, or operator is imported.
The p=7 neighbors are generated from three rank-one unitary reflections.
All arithmetic is in Z[omega], omega^2+omega+1=0, with Python integers.
"""
from itertools import permutations, product
from math import comb
from pathlib import Path
import json

O=(0,0); I=(1,0); W=(0,1); PI=(3,1); BARPI=(2,-1)
UNITS=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
PERMS=list(permutations(range(3)))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    x,y=a;z,w=b
    return (x*z-y*w,x*w+y*z-y*w)
def scale(n,a): return(n*a[0],n*a[1])
def conj(a): return(a[0]-a[1],-a[1])
def norm(a): return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
def esum(xs):
    z=O
    for x in xs:z=add(z,x)
    return z
def trace(A):return esum(A[i][i] for i in range(3))
def det(A):
    z=O
    for p in PERMS:
        inversions=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term=mul(mul(A[0][p[0]],A[1][p[1]]),A[2][p[2]])
        z=add(z,scale((-1)**inversions,term))
    return z
def symmetrics(A):
    s1=trace(A)
    s2=esum(sub(mul(A[i][i],A[j][j]),mul(A[i][j],A[j][i]))
            for i in range(3) for j in range(i+1,3))
    return s1,s2,det(A)
def h_sequence(A,kmax):
    s1,s2,s3=symmetrics(A)
    hs=[I]
    for k in range(1,kmax+1):
        value=mul(s1,hs[k-1])
        if k>=2:value=sub(value,mul(s2,hs[k-2]))
        if k>=3:value=add(value,mul(s3,hs[k-3]))
        hs.append(value)
    return hs
def gram(A):
    return [[esum(mul(conj(A[t][i]),A[t][j]) for t in range(3))
             for j in range(3)] for i in range(3)]
def gamma_product(A,p,u):
    # Gamma sends standard vector e_j to unit u_j e_{p(j)}.
    return [[mul(A[i][p[j]],u[j]) for j in range(3)] for i in range(3)]
def reflection(r):
    # alpha = omega^(r-1) * bar(pi), and (alpha-pi)/r is integral.
    alpha=BARPI
    for j in range(r-1):alpha=mul(W,alpha)
    d=sub(alpha,PI)
    assert all(x%r==0 for x in d)
    c=tuple(x//r for x in d)
    A=[[add(PI if i==j else O,c if i<r and j<r else O)
        for j in range(3)] for i in range(3)]
    assert gram(A)==[[(7,0) if i==j else O for j in range(3)] for i in range(3)]
    # omega = -3 modulo pi. Nonzero rank-one coefficient on r-support.
    R=[[(a-3*b)%7 for a,b in row] for row in A]
    assert any(x for row in R for x in row)
    assert all((R[i][a]*R[j][b]-R[i][b]*R[j][a])%7==0
               for i in range(3) for j in range(3)
               for a in range(3) for b in range(3))
    return A
def character_averages(A,p,kmax):
    totals=[0]*(kmax+1)
    for perm in PERMS:
        for units in product(UNITS,repeat=3):
            hs=h_sequence(gamma_product(A,perm,units),kmax)
            for k in range(kmax+1):
                totals[k]+=norm(hs[k])-(p*norm(hs[k-1]) if k else 0)
    # These are sums before division by |Gamma|=6^3*6.
    return totals
def full_invariant_count(k):
    if k<0:return 0
    coeff=[0]*16
    for r in product(range(6),repeat=3):coeff[sum(r)]+=1
    identity=sum(c*comb((k-r)//6+2,2)**2 for r,c in enumerate(coeff)
                 if r<=k and (k-r)%6==0)
    n=k//2+1;q,s=divmod(n,6)
    transposition=6*q*q+2*q*s+s
    cycle=int(k%3==0)
    total=identity+3*transposition+2*cycle
    assert total%6==0
    return total//6
def orbit_enumeration_count(k):
    if k<0:return 0
    triples=[(a,b,k-a-b) for a in range(k+1) for b in range(k-a+1)]
    return len({tuple(sorted(zip(a,b))) for a in triples for b in triples
                if all((x-y)%6==0 for x,y in zip(a,b))})
def main():
    kmax=30
    identity=[[I if i==j else O for j in range(3)] for i in range(3)]
    dims_raw=character_averages(identity,1,kmax)
    dims=[]
    for k,value in enumerate(dims_raw):
        assert value%1296==0
        d=value//1296
        assert d==full_invariant_count(k)-full_invariant_count(k-1)
        assert full_invariant_count(k)==orbit_enumeration_count(k)
        dims.append(d)
    rows=[];total=[0]*(kmax+1)
    for r in (1,2,3):
        A=reflection(r)
        multiplicity=comb(3,r)*6**(r-1)
        sums=character_averages(A,7,kmax)
        rows.append({'support_size':r,'matrix':A,'coset_multiplicity':multiplicity,
                     'sum_scaled_characters_by_degree':sums})
        for k in range(kmax+1):total[k]+=multiplicity*sums[k]
    assert sum(row['coset_multiplicity'] for row in rows)==57
    scaled_traces=[]
    for x in total:
        assert x%1296==0
        scaled_traces.append(x//1296)
    assert dims[5]==1 and dims[6]==3
    assert scaled_traces[5]==157899
    out={'method':'finite-group character projector and independently constructed rank-one reflections',
         'group_order':1296,'neighbors':57,'coefficient_weight':['k',0,'-k'],
         'Harish_Chandra_parameter':['k+1',0,'-k-1'],
         'dimensions':dims,'scaled_T7_traces':scaled_traces,
         'reflection_orbits':rows,'degree5_result':{'dimension':dims[5],
            'scaled_eigenvalue':scaled_traces[5],'normalized_Satake_trace':'157899/7^6'},
         'literal_degree6_dimension':dims[6],
         'checks':['all Gram matrices','rank-one mod pi','57 disjoint projective lines by support',
                   'character-average dimensions agree with Burnside formula',
                   'Burnside formula agrees with independent orbit enumeration through degree30']}
    dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('degree5_result','literal_degree6_dimension','dimensions','scaled_T7_traces')},indent=2))
if __name__=='__main__':main()
