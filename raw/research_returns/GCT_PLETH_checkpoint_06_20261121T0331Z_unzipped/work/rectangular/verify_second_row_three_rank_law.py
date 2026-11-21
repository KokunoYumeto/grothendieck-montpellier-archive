"""Literal cubic-minor canonical pairings and full small three-row-width band."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations,permutations
from math import factorial,comb
import csv
from verify_rectangular import sign
from verify_outer4_chambers import actual
from verify_two_column_tail_unit_family import det
from verify_second_row_two_rank_law import product_form

HERE=Path(__file__).resolve().parent


def literal_pairing(a,n,s,vectors):
    q=product_form(vectors)
    pairing={}
    for beta,value in q.items():
        value=Fraction(value,factorial(n))
        for b in beta:value*=factorial(b)
        pairing[beta]=value
    p0=pairing.get((n,)+(0,)*s,0)
    p1=pairing.get((n-1,1)+(0,)*(s-1),0)
    result=Fraction(0)
    perms=tuple((p,sign(p)) for p in permutations(range(s+1)))
    for sigma,sign1 in perms:
        for tau,sign2 in perms:
            normal=[];extra=[]
            for i in range(s+1):
                beta=[n-3]+[0]*s
                beta[sigma[i]]+=1;beta[tau[i]]+=1
                bx=beta[:];bx[0]+=1
                by=beta[:];by[1]+=1
                normal.append(pairing.get(tuple(bx),0))
                extra.append(pairing.get(tuple(by),0))
            internal=Fraction(0)
            for i in range(s+1):
                term=extra[i]
                for t in range(s+1):
                    if t!=i:term*=normal[t]
                internal+=term
            external=Fraction(1)
            for v in normal:external*=v
            value=(a-s-1)*p0**(a-s-1)*internal
            value-=(s+1)*(a-s-1)*p1*p0**(a-s-2)*external
            result+=sign1*sign2*value
    return comb(a,s+1)*result


def target_polynomial(a,n,s,vectors):
    u=1
    for row in vectors:u*=row[0]
    affine=[(Fraction(1),)+tuple(Fraction(y,row[0]) for y in row[1:]) for row in vectors]
    answer=Fraction(0)
    for I in combinations(range(n),s+1):
        inside=sum(affine[i][1] for i in I)
        outside=sum(affine[i][1] for i in range(n) if i not in I)
        answer+=((n-s-1)*inside-(s+1)*outside)*det([affine[i] for i in I])**2
    return u**a*answer


def sample(n,s):
    if n>=s+2:
        lower=[(1,)+(0,)*(s-1)]*2
        lower += [tuple(int(i==p) for i in range(s)) for p in range(1,s)]
        lower += [(-2,)+(-1,)*(s-1)]
        lower += [(0,)*s]*(n-s-2)
    else:
        lower=[tuple((i+1)**(p+1) for p in range(s)) for i in range(n)]
    return [(i+1,)+tuple((i+1)*v for v in row) for i,row in enumerate(lower)]


def scalar_checks():
    rows=[]
    for a in range(3,7):
        for n in range(3,7):
            for s in range(1,a-1):
                vectors=sample(n,s)
                left=literal_pairing(a,n,s,vectors)
                target=target_polynomial(a,n,s,vectors)
                scalar=Fraction(2*(-1)**(s-1)*factorial(a),
                                factorial(a-s-2)*n**(s+2)*(n-1)**s*(n-2))
                assert left==scalar*target,(a,n,s,left,scalar,target)
                assert bool(left)==(n>=s+2),(a,n,s,left)
                rows.append(dict(a=a,n=n,s=s,literal_pairing=str(left),
                                 scalar=str(scalar),target_polynomial=str(target),status='PASS'))
        print('literal cubic-minor pairings completed a',a,flush=True)
    with (HERE/'SECOND_ROW_THREE_CANONICAL_SCALAR_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS literal cubic-minor pairings',len(rows),flush=True)


def expected(a,n,p,q,k):
    if k:return 0
    if p==0:return int(q<=a-1)
    if p==1:return int(n>=3 and q<=a-3)
    return 0


def main():
    scalar_checks()
    rows=[]
    for a in range(2,7):
        for n in range(2,5):
            for p in range(a):
                for q in range(a-p):
                    for k in range(a-p-q):
                        lam=(a*n-3*p-2*q-k,)+(3,)*p+(2,)*q+(1,)*k
                        if tuple(sorted(lam,reverse=True))!=lam:continue
                        target=actual((a,),n,lam)
                        source=actual((n,),a,lam)
                        want_target=expected(a,n,p,q,k)
                        want_source=expected(n,a,p,q,k)
                        assert target==want_target,(a,n,p,q,k,target,want_target)
                        assert source==want_source,(a,n,p,q,k,source,want_source)
                        rows.append(dict(a=a,n=n,p=p,q=q,k=k,output=','.join(map(str,lam)),
                                         target_actual_MN=target,source_actual_MN=source,status='PASS'))
        print('full second-row-three MN completed a',a,'shapes',len(rows),flush=True)
    with (HERE/'SECOND_ROW_THREE_BAND_MN_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS full-band target and source coefficient pairs',len(rows),flush=True)


if __name__=='__main__':main()
