"""R049 literal Euler-contracted differential-form Vandermonde scalar."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
import csv
HERE=Path(__file__).resolve().parent
def determinant(mat):
    mat=[row[:] for row in mat];value=F(1);n=len(mat)
    for c in range(n):
        p=next((r for r in range(c,n) if mat[r][c]),None)
        if p is None:return F()
        if p!=c:mat[p],mat[c]=mat[c],mat[p];value=-value
        pivot=mat[c][c];value*=pivot
        for j in range(c,n):mat[c][j]/=pivot
        for r in range(c+1,n):
            factor=mat[r][c]
            for j in range(c,n):mat[r][j]-=factor*mat[c][j]
    return value
def main():
    rows=[]
    for r in range(1,11):
        base=r+2
        for a in (base,base+2):
            x=[F(2*i-base-1,2) for i in range(1,base+1)]+[F()]*(a-base)
            assert sum(x)==0
            matrix=[]
            for d in range(2,base+1):
                row=[d*sum(z**d for z in x)]
                row += [d*(x[j]**(d-1)-x[base-1]**(d-1)) for j in range(1,base-1)]
                matrix.append(row)
            got=determinant(matrix)
            expected=F((-1)**base*(base-1)*factorial(base),2)*prod(
               x[j]-x[i] for i in range(base) for j in range(i+1,base))
            assert got==expected and got,(r,a,got,expected)
            rows.append(dict(r=r,a=a,coefficient_degree=(r*r+3*r+4)//2,
                  literal_Euler_form=str(got),Vandermonde_formula=str(expected),status='PASS'))
    with (HERE/'ODD_PART_HOOK_FORM_SCALAR_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS literal Euler form',len(rows),flush=True)
if __name__=='__main__':main()

