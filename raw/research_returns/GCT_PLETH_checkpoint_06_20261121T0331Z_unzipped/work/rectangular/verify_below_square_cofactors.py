"""R026: literal minors and truncated polynomial coefficient audit.

The actual side multiplies the determinant and individual cofactor
linear forms with exact integer coefficients. It does not use the
two-group product formulas of BS17/BS18 to calculate the coefficient.
"""
from pathlib import Path
from math import comb,factorial
from collections import defaultdict
import csv
import sympy as s

HERE=Path(__file__).resolve().parent


def literal_forms(r,group_size,distinguished):
    n=r+1
    I=list(range(group_size-1))+[r]
    J=[i for i in range(n) if i not in I]
    q=r;p=distinguished;j0=J[0]
    omitted={j0} if p is None else {j0,p}
    rows=[]
    for i in range(r):
        if i not in omitted:rows.append([int(j==i) for j in range(r)])
    if p is not None:rows.append([int(j==p) for j in range(r)])
    rows.append([int(j in J) for j in range(r)])
    A=s.Matrix(rows)
    assert abs(A.det())==1
    B0=s.Matrix([[int(j==i)-int(j==q) for j in range(n)] for i in range(r)])
    B=A.inv().T*B0
    xs=s.symbols(f'x0:{r}')
    X=s.Matrix([list(xs)+[0]]+B.tolist())
    def linear(expr):
        expr=s.Poly(expr,xs)
        assert expr.total_degree()<=1 and expr.coeff_monomial((0,)*r)==0
        return tuple(int(expr.coeff_monomial(tuple(int(i==j) for i in range(r)))) for j in range(r))
    D=linear(X.det(method='domain-ge'))
    y=[linear((-1)**(n-1+j)*X.minor_submatrix(n-1,j).det(method='domain-ge')) for j in range(n)]
    z=None if p is None else [linear((-1)**(n-2+j)*X.minor_submatrix(n-2,j).det(method='domain-ge')) for j in range(n)]
    return D,y,z


def multiply(poly,linear,r):
    out=defaultdict(int)
    entries=[(i,v) for i,v in enumerate(linear) if v]
    for alpha,c in poly.items():
        for i,v in entries:
            if alpha[i]<r:
                beta=alpha[:i]+(alpha[i]+1,)+alpha[i+1:]
                out[beta]+=c*v
    return {a:c for a,c in out.items() if c}


def multiply_many(poly,factors,r):
    for factor in factors:poly=multiply(poly,factor,r)
    return poly


def actual(r,k,kind):
    n=r+1;H=r*r
    sg=(r//2+1) if kind=='G' else (3 if r==3 else (r+1)//2)
    D,y,z=literal_forms(r,sg,None if kind=='G' else 0)
    unit={(0,)*r:1}
    if kind=='G':
        factors=[form for form in y for _ in range(k)]+[D]*(H-n*k)
        poly=multiply_many(unit,factors,r)
    else:
        poly=defaultdict(int)
        for j in range(r):
            xj=tuple(int(i==j) for i in range(r))
            factors=[xj,z[j],z[j]]+[y[i] for i in range(n) if i!=j]
            for alpha,c in multiply_many(unit,factors,r).items():poly[alpha]+=c
        poly={a:c for a,c in poly.items() if c}
        factors=[form for form in y for _ in range(k-2)]+[D]*(H-n*(k-1)-2)
        poly=multiply_many(poly,factors,r)
    return poly.get((r,)*r,0)


def formula(r,k,kind):
    if kind=='G':
        sg=r//2+1;h=r*r-k*(r+1);u=r*(r-k)//2
        numerator=(-1)**(sg*k)*comb(h,u)*factorial(r*r//2)**2
        denominator=factorial(r)**r
    else:
        sg=3 if r==3 else (r+1)//2
        tg=r+1-sg
        h=r*r-(k-1)*(r+1)
        dI=r*(sg-1);dJ=r*tg;u=dI-tg*(k-1)-1
        numerator=(-1)**(sg*(k-1)+1)*comb(h,u)*comb(dI-2,r-1)
        numerator*=factorial(dI-r)*factorial(dJ)
        denominator=factorial(r)**(r-1)
    assert numerator%denominator==0
    return numerator//denominator


def main():
    cases=[('G',4,2),('G',6,2),('G',6,3),('G',6,4),
           ('F',3,2),('F',5,2),('F',5,3),('F',5,4),('F',7,6)]
    rows=[]
    for kind,r,k in cases:
        value=actual(r,k,kind);expected=formula(r,k,kind)
        assert value==expected and value!=0,(kind,r,k,value,expected)
        rows.append(dict(family=kind,r=r,k=k,a=r+1,b=r*r-k,
            literal_minor_coefficient=value,closed_formula=expected,status='PASS'))
        print('PASS',rows[-1],flush=True)
    with (HERE/'BELOW_SQUARE_COFACTOR_INDEPENDENT_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS all',len(rows),'literal coefficient comparisons')


if __name__=='__main__':main()
