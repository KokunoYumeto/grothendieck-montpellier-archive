"""R035 actual polynomial pairings and independent full-band multiplicities."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations,permutations
from collections import defaultdict
from math import factorial
import csv
from verify_rectangular import sign
from verify_outer4_chambers import actual
from verify_two_column_tail_unit_family import det

HERE=Path(__file__).resolve().parent


def product_form(vectors):
    q={(0,)*len(vectors[0]):1}
    for vector in vectors:
        nxt=defaultdict(int)
        for beta,value in q.items():
            for i,c in enumerate(vector):
                following=list(beta);following[i]+=1
                nxt[tuple(following)]+=value*c
        q=dict(nxt)
    return q


def literal_pairing(a,n,j,vectors):
    q=product_form(vectors)
    pair={}
    for beta,value in q.items():
        norm=Fraction(value,factorial(n))
        for b in beta:norm*=factorial(b)
        pair[beta]=norm
    perms=tuple((p,sign(p)) for p in permutations(range(j+1)))
    result=Fraction(0)
    base=(n,)+(0,)*j
    for I in combinations(range(a),j+1):
        outside=pair.get(base,0)**(a-j-1)
        for sigma,s1 in perms:
            for tau,s2 in perms:
                term=outside*s1*s2
                for index in range(j+1):
                    beta=[n-2]+[0]*j
                    beta[sigma[index]]+=1;beta[tau[index]]+=1
                    term*=pair.get(tuple(beta),0)
                    if not term:break
                result+=term
    return result


def target_polynomial(a,n,j,vectors):
    # Here n is the number of target slots and a their separate degree.
    u=1
    for row in vectors:u*=row[0]
    answer=Fraction(0)
    for I in combinations(range(n),j+1):
        outside=1
        for index,row in enumerate(vectors):
            if index not in I:outside*=row[0]**2
        answer+=outside*det([vectors[i] for i in I])**2
    return u**(a-2)*answer


def scalar_checks():
    rows=[]
    for a in range(2,6):
        for n in range(2,6):
            for j in range(1,a):
                vectors=[]
                for k in range(n):
                    lower=[int(k==p) for p in range(j)]
                    vectors.append((k+1,)+tuple(lower))
                left=literal_pairing(a,n,j,vectors)
                right=target_polynomial(a,n,j,vectors)
                scalar=Fraction((-1)**j*factorial(a),
                                factorial(a-j-1)*n**(j+1)*(n-1)**j)
                assert left==scalar*right,(a,n,j,left,scalar,right)
                assert bool(left)==(j<n),(a,n,j,left)
                rows.append(dict(a=a,n=n,j=j,literal_pairing=str(left),
                                 scalar=str(scalar),target_polynomial=str(right),status='PASS'))
        print('literal polynomial checks completed a',a,flush=True)
    with (HERE/'SECOND_ROW_TWO_CANONICAL_SCALAR_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS literal determinant-square pairings',len(rows),flush=True)


def main():
    scalar_checks()
    rows=[];source_count=0
    for a in range(2,7):
        for n in range(2,5):
            for j in range(a):
                for k in range(a-j):
                    lam=(a*n-2*j-k,)+(2,)*j+(1,)*k
                    assert tuple(sorted(lam,reverse=True))==lam
                    target=actual((a,),n,lam)
                    expected=int(k==0)
                    assert target==expected,(a,n,j,k,target)
                    source=''
                    if k==0:
                        source=actual((n,),a,lam)
                        assert source==int(j<n),(a,n,j,source)
                        source_count+=1
                    rows.append(dict(a=a,n=n,j=j,k=k,output=','.join(map(str,lam)),
                                     target_actual_MN=target,source_actual_MN=source,status='PASS'))
        print('full-band MN completed a',a,'cases',len(rows),flush=True)
    with (HERE/'SECOND_ROW_TWO_BAND_MN_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS full-band target coefficients',len(rows),'and pure-tail source coefficients',source_count,flush=True)


if __name__=='__main__':main()
