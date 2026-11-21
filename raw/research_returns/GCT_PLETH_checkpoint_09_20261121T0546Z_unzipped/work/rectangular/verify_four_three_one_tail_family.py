"""R040 literal weighted-minor canonical maps and independent plethysms."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, comb
import csv
from verify_rectangular import sign
from verify_outer4_chambers import actual
from verify_two_column_tail_unit_family import det
from verify_second_row_two_rank_law import product_form

HERE=Path(__file__).resolve().parent


def literal_pairing(a,n,m,vectors):
    pair={}
    for beta,value in product_form(vectors).items():
        norm=Fraction(value,factorial(n))
        for e in beta:norm*=factorial(e)
        pair[beta]=norm
    def moment(lower):
        degree=sum(lower)
        assert degree<=n
        return pair.get((n-degree,)+tuple(lower),0)
    zero=(0,)*m;p0=moment(zero)
    p1=moment((1,)+(0,)*(m-1))
    p2=moment((0,1)+(0,)*(m-2))
    perms=tuple((p,sign(p)) for p in permutations(range(m+1)))
    answer=Fraction(0)
    for sigma,s1 in perms:
        for tau,s2 in perms:
            quad=tau.index(m)
            normal=[[],[]]
            extra=[[],[]]
            for tag in (0,1):
                for i in range(m+1):
                    e=[0]*m
                    if sigma[i]:e[sigma[i]-1]+=1
                    if tau[i]==m:
                        e[0]+=1;e[tag]+=1
                    elif tau[i]:e[tau[i]-1]+=1
                    normal[tag].append(moment(e))
                    if i==quad:
                        extra[tag].append(0)
                    else:
                        e[1-tag]+=1
                        extra[tag].append(moment(e))
            internal=[Fraction(0),Fraction(0)]
            external=[Fraction(1),Fraction(1)]
            for tag in (0,1):
                for v in normal[tag]:external[tag]*=v
                for i in range(m+1):
                    if i==quad:continue
                    term=extra[tag][i]
                    for j in range(m+1):
                        if i!=j:term*=normal[tag][j]
                    internal[tag]+=term
            value=(a-m-1)*p0**(a-m-1)*(internal[0]-internal[1])
            value-=(m+1)*(a-m-1)*p0**(a-m-2)*(p2*external[0]-p1*external[1])
            answer+=s1*s2*value
    return comb(a,m+1)*answer


def weighted_minor(vectors):
    a=len(vectors);m=len(vectors[0])-1
    w=[tuple(Fraction(v,row[0]) for v in row[1:]) for row in vectors]
    answer=Fraction(0)
    for I in combinations(range(a),m+1):
        R=[(1,)+w[i] for i in I]
        B1=[row[:m]+(row[1]**2,) for row in R]
        B2=[row[:m]+(row[1]*row[2],) for row in R]
        weight=[(a-m-1)*sum(w[i][p] for i in I)-
                (m+1)*sum(w[i][p] for i in range(a) if i not in I) for p in (0,1)]
        answer+=det(R)*(weight[1]*det(B1)-weight[0]*det(B2))
    return answer


def cofactor_tensor(vectors):
    a=len(vectors);m=len(vectors[0])-1
    w=[tuple(Fraction(v,row[0]) for v in row[1:]) for row in vectors]
    mean=[sum(r[p] for r in w)/a for p in range(m)]
    zs=[tuple(r[p]-mean[p] for p in range(m)) for r in w]
    S=[[sum(r[p]*r[q] for r in zs) for q in range(m)] for p in range(m)]
    C=lambda p,q,t:sum(r[p]*r[q]*r[t] for r in zs)
    F=Fraction(0);l=m-1
    for i,j,k in product(range(m),repeat=3):
        if i==j or k==l:continue
        rows=[p for p in range(m) if p not in (k,l)]
        cols=[p for p in range(m) if p not in (i,j)]
        A=(-1)**(i+j+k+l)*(1 if i<j else -1)*det([[S[p][q] for q in cols] for p in rows])
        F+=(C(0,0,i)*C(1,j,k)-C(0,1,i)*C(0,j,k))*A
    return F


def sample(n,m,tag):
    if tag==0 and n>=m+2:
        lower=[tuple(int(i==p) for i in range(m)) for p in range(m)]
        lower += [(1,2)+(0,)*(m-2),(-2,-3)+(-1,)*(m-2)]
        lower += [(0,)*m]*(n-m-2)
    else:
        lower=[tuple((i+1)**(p+1)+tag*(p+1) for p in range(m)) for i in range(n)]
    return [(i+2,)+tuple((i+2)*v for v in row) for i,row in enumerate(lower)]


def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)


def main():
    rows=[]
    for a in (5,6):
        for n in range(3,7):
            for m in range(3,min(a-1,5)):
                for tag in (0,1):
                    vectors=sample(n,m,tag)
                    B=weighted_minor(vectors);F=cofactor_tensor(vectors)
                    assert B==-n*n*F,(a,n,m,tag,B,F)
                    if tag==0 and n>=m+2:assert F==-20
                    u=1
                    for r in vectors:u*=r[0]
                    target=u**a*B
                    left=literal_pairing(a,n,m,vectors)
                    scalar=Fraction(4*(-1)**(m-2)*factorial(a),
                        factorial(a-m-2)*n**(m+2)*(n-1)**m*(n-2)**2)
                    assert left==scalar*target,(a,n,m,tag,left,scalar,target)
                    if tag==0:assert bool(left)==(n>=m+2)
                    rows.append(dict(a=a,n=n,m=m,sample=tag,literal_pairing=str(left),
                        scalar=str(scalar),target_polynomial=str(target),
                        weighted_minor_equals_minus_n_squared_tensor=True,status='PASS'))
        print('completed literal weighted-minor a',a,flush=True)
    write('FOUR_THREE_ONE_TAIL_CANONICAL_CHECK.tsv',rows)
    print('PASS literal weighted-minor cases',len(rows),flush=True)
    rows=[]
    for a in range(4,9):
        for n in range(3,6):
            for m in range(3,a):
                lam=(a*n-2*m-2,4,3)+(2,)*(m-3)+(1,)
                if lam[0]<4:continue
                target=actual((a,),n,lam);source=actual((n,),a,lam)
                assert target==int(a>=m+2),(a,n,m,target)
                assert source==int(n>=m+2),(a,n,m,source)
                rows.append(dict(a=a,n=n,m=m,output=','.join(map(str,lam)),
                    target_actual_MN=target,source_actual_MN=source,status='PASS'))
        print('completed family MN a',a,'cases',len(rows),flush=True)
    write('FOUR_THREE_ONE_TAIL_MN_CHECK.tsv',rows)
    print('PASS target/source actual MN pairs',len(rows),flush=True)


if __name__=='__main__':main()
