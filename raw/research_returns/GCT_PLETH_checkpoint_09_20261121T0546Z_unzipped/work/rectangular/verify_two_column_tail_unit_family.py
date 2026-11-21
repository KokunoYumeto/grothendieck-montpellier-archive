"""R033: literal exterior maps and independent actual plethysm checks."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from collections import defaultdict
from math import factorial
import csv
from verify_outer4_chambers import actual

HERE=Path(__file__).resolve().parent


def det(matrix):
    a=[list(map(Fraction,row)) for row in matrix]
    result=Fraction(1)
    for i in range(len(a)):
        p=next((p for p in range(i,len(a)) if a[p][i]),None)
        if p is None:return Fraction(0)
        if p!=i:a[p],a[i]=a[i],a[p];result=-result
        pivot=a[i][i];result*=pivot
        for row in range(i+1,len(a)):
            ratio=a[row][i]/pivot
            for col in range(i+1,len(a)):a[row][col]-=ratio*a[i][col]
    return result


def exterior_checks():
    rows=[]
    for a in range(2,9):
        r=a-1
        inv=[[Fraction(i==j)-Fraction(1,a) for j in range(r)] for i in range(r)]
        proj=[[Fraction(i==j)-Fraction(1,a) for j in range(a)] for i in range(r)]
        for j in range(1,a):
            basis=tuple(combinations(range(r),j))
            omega={(I,J):det([[inv[i][l] for l in J] for i in I])
                   for I in basis for J in basis}
            assert any(omega.values())
            image=defaultdict(Fraction)
            for (I,J),value in omega.items():
                for pos,t in enumerate(J):
                    if t in I:continue
                    sign=(-1)**(pos+sum(i>t for i in I))
                    image[tuple(sorted(I+(t,))),J[:pos]+J[pos+1:]]+=sign*value
            assert not any(image.values()),(a,j,image)
            # The ordered matching sum has exactly j! copies of each subset.
            for I in basis:
                for J in basis:
                    matching=sum(det([[proj[i][l] for l in S] for i in I])*
                                 det([[proj[i][l] for l in S] for i in J])
                                 for S in combinations(range(a),j))*factorial(j)
                    assert matching==factorial(j)*omega[I,J],(a,j,I,J)
            rows.append(dict(a=a,j=j,dimension=len(basis),
                             literal_kernel='PASS',matching_scalar=factorial(j),status='PASS'))
    with (HERE/'TWO_COLUMN_TAIL_EXTERIOR_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS literal exterior and projected matching checks',len(rows),flush=True)


def main():
    exterior_checks()
    rows=[]
    for a in range(2,7):
        for n in range(2,5):
            for j in range(1,a):
                lam=(a*n-2*j,)+(2,)*j
                value=actual((a,),n,lam)
                assert value==1,(a,n,j,lam,value)
                rows.append(dict(a=a,n=n,j=j,output=','.join(map(str,lam)),
                                 actual_MN=value,status='PASS'))
        print('completed outer',a,'cases',len(rows),flush=True)
    with (HERE/'TWO_COLUMN_TAIL_UNIT_MN_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS actual MN unit coefficients',len(rows),flush=True)


if __name__=='__main__':main()
