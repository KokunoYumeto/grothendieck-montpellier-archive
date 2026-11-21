"""Independent determinant/minor and exact coefficient checks for R025."""
from pathlib import Path
from math import factorial,comb,prod
import csv
import sympy as s

HERE=Path(__file__).resolve().parent


def cofactor_data(n,group_size,distinguished):
    variables=s.symbols(f"x0:{n}")
    I=list(range(group_size-1))+[n-1]
    J=[i for i in range(n) if i not in I]
    p=distinguished
    q=next(i for i in I if i!=p) if p is not None else I[0]
    coords=[i for i in range(n) if i!=q]
    j0=J[0]
    rows=[]
    omitted={j0} if p is None else {j0,p}
    for i in coords:
        if i not in omitted:rows.append([int(j==i) for j in coords])
    if p is not None:rows.append([int(j==p) for j in coords])
    rows.append([int(j in J) for j in coords])
    A=s.Matrix(rows)
    assert abs(A.det())==1
    B0=s.Matrix([[int(j==i)-int(j==q) for j in range(n)] for i in coords])
    B=A.inv().T*B0
    X=s.Matrix([list(variables)]+B.tolist())
    D=s.expand(X.det(method="domain-ge"))
    S=sum(variables)
    eta=int(D.coeff(variables[0]))
    assert eta in (-1,1) and D==eta*S
    y=[s.expand((-1)**(n-1+j)*X.minor_submatrix(n-1,j).det(method="domain-ge")) for j in range(n)]
    XI=sum(variables[i] for i in I);YJ=sum(variables[j] for j in J)
    assert all(s.expand(y[i]-eta*(-YJ if i in I else XI))==0 for i in range(n))
    if p is None:
        base=s.Poly(s.prod(q*q for q in y),variables)
    else:
        z=[s.expand((-1)**(n-2+j)*X.minor_submatrix(n-2,j).det(method="domain-ge")) for j in range(n)]
        assert all(s.expand(z[i]-eta*(S*int(i==p)-variables[p]))==0 for i in range(n))
        numerator=sum(variables[j]*z[j]**2*s.prod(y[i] for i in range(n) if i!=j) for j in range(n))
        quotient,remainder=s.div(s.Poly(numerator,variables),s.Poly(D,variables))
        assert remainder.is_zero
        base=quotient
    return variables,eta,base


def coefficient(eta,base,power,alpha):
    result=0
    for beta,c in base.terms():
        residual=tuple(a-b for a,b in zip(alpha,beta))
        if min(residual)<0:continue
        assert sum(residual)==power
        result+=int(c)*(factorial(power)//prod(factorial(v) for v in residual))
    return eta**power*result


def main():
    rows=[]
    even_cases=[(3,2),(3,4),(4,1),(4,2),(4,4),(5,2),(6,1),(6,2),(6,6),(7,2),(8,1)]
    for r,L in even_cases:
        sgroup=(r+1)//2;tgroup=r//2
        xs,eta,base=cofactor_data(r,sgroup,0)
        alpha=(L+1,)+(L,)*(r-1)
        actual=(L+1)*coefficient(eta,base,r*(L-1),alpha)
        expected=(-1)**(sgroup+1)*(L+1)
        expected*=factorial((sgroup-1)*L)*factorial(tgroup*L)
        expected*=comb(r*(L-1)+1,sgroup*L-tgroup)*comb(sgroup*L-1,L)
        denominator=factorial(L)**(r-1)
        assert expected%denominator==0
        expected//=denominator
        assert actual==expected and actual!=0
        rows.append(dict(family="common_F",slots=r,L=L,H=r*L+1,actual=actual,formula=expected,status="PASS"))
    for r,L in [(3,3),(3,5),(5,3),(7,3)]:
        sg=(r-1)//2;tg=(r+1)//2
        xs,eta,base=cofactor_data(r,sg,None)
        p=r-1 # I may be the singleton last slot when r=3.
        alpha=tuple(L+int(i==p) for i in range(r))
        actual=(L+1)*coefficient(eta,base,r*L+1-2*r,alpha)
        expected=comb(r*L+1-2*r,sg*L+1-2*tg)*factorial(sg*L+1)*factorial(tg*L)
        denominator=factorial(L)**r
        assert expected%denominator==0
        expected//=denominator
        assert actual==expected and actual!=0
        rows.append(dict(family="common_G",slots=r,L=L,H=r*L+1,actual=actual,formula=expected,status="PASS"))
    for r in [2,4,6]:
        n=r+1;H=r*r+1;sg=(r+2)//2
        xs,eta,base=cofactor_data(n,sg,n-1)
        actual=coefficient(eta,base,H-n-1,(r,)*r+(1,))
        expected=(-1)**(sg+1)*comb(r*r-r,r*(r-1)//2)*factorial(r*r//2)**2
        denominator=factorial(r)**r
        assert expected%denominator==0
        expected//=denominator
        assert actual==expected and actual!=0
        rows.append(dict(family="canonical_F",slots=n,L=r,H=H,actual=actual,formula=expected,status="PASS"))
    for r in [3,5,7]:
        n=r+1;H=r*r+1;sg=(r+1)//2
        xs,eta,base=cofactor_data(n,sg,None)
        actual=coefficient(eta,base,H-2*n,(r,)*r+(1,))
        expected=comb(r*r-2*r-1,r*(r-3)//2)*factorial(r*(r-1)//2+1)*factorial(r*(r+1)//2)
        denominator=factorial(r)**r
        assert expected%denominator==0
        expected//=denominator
        assert actual==expected and actual!=0
        rows.append(dict(family="canonical_G",slots=n,L=r,H=H,actual=actual,formula=expected,status="PASS"))
    with (HERE/"NEXT_COFACTOR_COEFFICIENT_CHECK.tsv").open("w",newline="") as out:
        w=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter="\t")
        w.writeheader();w.writerows(rows)
    print("PASS",len(rows),"actual determinant/cofactor coefficient checks")
    for row in rows:print(row)


if __name__=="__main__":main()
