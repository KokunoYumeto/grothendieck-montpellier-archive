"""R041 literal determinant-square pairings and full low-degree coefficients."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations
from math import factorial,comb
import csv,random
import sympy as sp
from verify_rectangular import sign
from verify_outer4_chambers import actual
from verify_two_column_tail_unit_family import det
from verify_second_row_two_rank_law import product_form

HERE=Path(__file__).resolve().parent


def row_contractions(n,m,vectors):
    pair={}
    for beta,value in product_form(vectors).items():
        norm=F(value,factorial(n))
        for e in beta:norm*=factorial(e)
        pair[beta]=norm
    def moment(e):
        assert sum(e)<=n
        return pair.get((n-sum(e),)+tuple(e),0)
    p=[moment((j,)+(0,)*(m-1)) for j in range(3)]
    sums=[F(0)]*4
    perms=tuple((p,sign(p)) for p in permutations(range(m+1)))
    for sigma,s1 in perms:
        for tau,s2 in perms:
            block=[]
            for i in range(m+1):
                e=[0]*m
                if sigma[i]:e[sigma[i]-1]+=1
                if tau[i]:e[tau[i]-1]+=1
                row=[]
                for q in range(3):
                    z=e[:];z[0]+=q;row.append(moment(z))
                block.append(row)
            base=F(1)
            for row in block:base*=row[0]
            first=F(0);second=F(0);square=F(0)
            for i in range(m+1):
                prod=F(1)
                for j in range(m+1):
                    if i!=j:prod*=block[j][0]
                first+=block[i][1]*prod
                second+=block[i][2]*prod
            square=second
            for i,j in combinations(range(m+1),2):
                prod=2*block[i][1]*block[j][1]
                for q in range(m+1):
                    if q not in (i,j):prod*=block[q][0]
                square+=prod
            for q,value in enumerate((base,first,second,square)):
                sums[q]+=s1*s2*value
    return p,sums


def literal(a,m,p,sums):
    k=m+1;l=a-k;p0,p1,p2=p;f0,f1,f2,f11=sums
    outside1=l*p1*p0**(l-1) if l else 0
    outside2=l*p2*p0**(l-1) if l else 0
    if l>=2:outside2+=l*(l-1)*p1*p1*p0**(l-2)
    whole_U=p0**l*f2+(l*p2*p0**(l-1)*f0 if l else 0)
    whole_T2=p0**l*f11+2*outside1*f1+outside2*f0
    whole_T_TI=p0**l*f11+outside1*f1
    A=whole_U-whole_T2/a
    B=p0**l*f2-2*whole_T_TI/a+k*whole_T2/(a*a)
    C=p0**l*(f11-f2)/2-(k-1)*whole_T_TI/a+F(k*(k-1),2*a*a)*whole_T2
    scale=comb(a,k)
    P1=scale*A/a
    return (P1,scale*B/a-P1/a,scale*C/a+P1/a)


def generators(vectors):
    n=len(vectors);m=len(vectors[0])-1
    w=[tuple(F(v,row[0]) for v in row[1:]) for row in vectors]
    mean=[sum(row[j] for row in w)/n for j in range(m)]
    z=[tuple(row[j]-mean[j] for j in range(m)) for row in w]
    S=sp.Matrix([[sum(row[i]*row[j] for row in z) for j in range(m)] for i in range(m)])
    C=sp.Matrix([[sum(row[0]*row[i]*row[j] for row in z) for j in range(m)] for i in range(m)])
    D=sp.Matrix([[sum(row[0]**2*row[i]*row[j] for row in z) for j in range(m)] for i in range(m)])
    ds=S.det()
    P1=S[0,0]*ds
    P2=sp.trace(S.adjugate()*D)
    # Literal coefficient of det(S+tC), valid also at singular S.
    t=sp.Symbol('t')
    P3=sp.Poly((S+t*C).det(),t).coeff_monomial(t*t)
    return tuple(F(int(v.p),int(v.q)) for v in (P1,P2,P3))


def coefficient_rows(a,n,m):
    C=[
        [F(a*a-a*m-a+m+2,a*a),F(a-1,a*a),F(-2,a*a)],
        [F((m+2)*(2*a-m-2),a**3),F(a*a-3*a+m+2,a**3),F(-2*(2*a-m-2),a**3)],
        [F((m-1)*(m+2)*(a-m-2),2*a**3),F(-(m-1)*(2*a-m-2),2*a**3),F(a*a-2*a*m+m*m+m-2,a**3)]
    ]
    U=F(n*(n-1),(n-2)*(n-3));V=F(n*(n-1),(n-2)**2)
    D=[[1,0,0],[(m+2)*U,-6*U,0],[0,0,-4*V]]
    scale=F((-1)**(m-1)*factorial(a),factorial(a-m-1)*(n*(n-1))**(m+1))
    return [[scale*sum(C[i][k]*D[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)


def main():
    rng=random.Random(41041);rows=[]
    configurations=[(n,m) for m in (2,3) for n in (4,5,6)]
    configurations +=[(5,4),(6,4),(7,4)]
    for n,m in configurations:
        expected_rank=min(3,max(0,n-m))
        count=max(1,expected_rank)
        old=[]
        for tag in range(count):
            for trial in range(100):
                w=[[rng.randrange(-3,5) for j in range(m)] for i in range(n)]
                vectors=[(i+2,)+tuple((i+2)*v for v in row) for i,row in enumerate(w)]
                vals=generators(vectors)
                if expected_rank==0 or sp.Matrix(old+[vals]).rank()==len(old)+1:break
            else:raise AssertionError(('no independent sample',n,m,tag))
            old.append(vals)
            p,sums=row_contractions(n,m,vectors)
            u=1
            for row in vectors:u*=row[0]
            for a in range(m+1,8):
                left=literal(a,m,p,sums)
                mat=coefficient_rows(a,n,m)
                right=[u**a*sum(mat[i][j]*vals[j] for j in range(3)) for i in range(3)]
                assert tuple(right)==left,(a,n,m,tag,left,right)
                for i in range(3):
                    rows.append(dict(a=a,n=n,m=m,sample=tag,generator=i+1,
                        literal_pairing=str(left[i]),matrix_value=str(right[i]),status='PASS'))
        print('completed literal matrix n,m',n,m,'cases',len(rows),flush=True)
    write('FOUR_EVEN_TAIL_CANONICAL_MATRIX_CHECK.tsv',rows)
    print('PASS literal matrix generator pairings',len(rows),flush=True)
    rows=[]
    for a in range(3,9):
        for n in (4,5):
            for m in range(2,a):
                lam=(a*n-2*m-2,4)+(2,)*(m-1)
                target=actual((a,),n,lam)
                want=min(3,a-m)
                assert target==want,(a,n,m,target,want)
                rows.append(dict(a=a,n=n,m=m,output=','.join(map(str,lam)),
                    actual_MN=target,expected=want,status='PASS'))
        print('completed target coefficients a',a,'cases',len(rows),flush=True)
    write('FOUR_EVEN_TAIL_MN_CHECK.tsv',rows)
    print('PASS independent target coefficients',len(rows),flush=True)


if __name__=='__main__':main()
