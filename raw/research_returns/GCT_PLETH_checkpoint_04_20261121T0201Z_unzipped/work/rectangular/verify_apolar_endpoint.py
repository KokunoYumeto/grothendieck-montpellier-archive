"""Independent biform and finite-field literal-minor audits of BS24--31."""
from pathlib import Path
from math import factorial,comb
from collections import defaultdict
import csv
import sympy as s

HERE=Path(__file__).resolve().parent


def positive_sum(r):
    return sum(comb(r,i)*comb(r-1,i)*factorial(r*i)*factorial(r*(r-i)) for i in range(r))


def apolar_audit(r):
    x,z=s.symbols('x z');N=r*r
    Q=(z-x)**r+x**r
    P=s.Poly(Q**r,x,z)
    R=s.Poly(x*z**(r-1)*Q**(r-1),x,z)
    value=sum(int(c)*(-1)**i*factorial(i)*factorial(j)*int(R.coeff_monomial((j,i)))
              for (i,j),c in P.terms())
    assert value==positive_sum(r) and value>0
    return value


def determinant(rows,p):
    A=[list(row) for row in rows];n=len(A);d=1
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]%p),None)
        if pivot is None:return 0
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];d=-d
        v=A[j][j]%p;d=d*v%p;inv=pow(v,-1,p)
        for i in range(j+1,n):
            t=A[i][j]*inv%p
            for k in range(j+1,n):A[i][k]=(A[i][k]-t*A[j][k])%p
    return d%p


def literal_forms(r,p):
    g=int(s.primitive_root(p));step=(p-1)//(2*r)
    a=[(1+pow(g,step*(2*i+1),p))%p for i in range(r)]
    assert len(set(a))==r and all(a)
    A=s.Matrix([[pow(v,j,p) for v in a] for j in list(range(2,r+1))+[1]])
    detA=determinant(A.tolist(),p);eta=pow(detA,-1,p)
    B0=s.Matrix([[int(i==j)-int(j==r) for j in range(r+1)] for i in range(r)])
    B=(A.inv_mod(p).T*B0).applyfunc(lambda v:int(v)%p).tolist()
    n=r+1;D=[];ys=[[] for _ in range(n)]
    for coordinate in range(r):
        X=[[int(j==coordinate) for j in range(n)]]+B
        D.append(determinant(X,p))
        for col in range(n):
            minor=[[row[j] for j in range(n) if j!=col] for row in X[:-1]]
            ys[col].append((-1)**(n-1+col)*determinant(minor,p)%p)
    assert D==[eta]*r
    for col in range(n):
        ai=a[col] if col<r else 0
        assert ys[col]==[eta*(ai-aj)%p for aj in a]
    return D,ys,eta,a


def multiply(poly,linear,r,p):
    out=defaultdict(int)
    entries=[(i,v) for i,v in enumerate(linear) if v%p]
    for alpha,c in poly.items():
        for i,v in entries:
            if alpha[i]<r:
                beta=alpha[:i]+(alpha[i]+1,)+alpha[i+1:]
                out[beta]=(out[beta]+c*v)%p
    return {a:c for a,c in out.items() if c}


def finite_field_audit(r,p):
    assert p>r*r and (p-1)%(2*r)==0 and s.isprime(p)
    D,ys,eta,a=literal_forms(r,p)
    poly={(0,)*r:1}
    for form in ys:
        for _ in range(r-1):poly=multiply(poly,form,r,p)
    poly=multiply(poly,D,r,p)
    actual=poly.get((r,)*r,0)
    expected=-pow(eta,r*r,p)*positive_sum(r)*pow(factorial(r)**r,-1,p)%p
    assert actual==expected and actual!=0,(r,p,actual,expected)
    return dict(r=r,prime=p,cofactor_parameters=','.join(map(str,a)),eta=eta,
                literal_minor_coefficient=actual,apolar_formula=expected,status='PASS')


def main():
    messages=[]
    for r in (2,4,6,8,10):
        value=apolar_audit(r)
        messages.append(f'PASS exact expanded binary apolar identity r={r}: positive sum={value}')
        print(messages[-1],flush=True)
    rows=[]
    for r,primes in [(4,(41,73,89)),(6,(73,97,109))]:
        prime=next(p for p in primes if positive_sum(r)%p)
        row=finite_field_audit(r,prime);rows.append(row)
        print('PASS actual matrix/minor endpoint',row,flush=True)
    with (HERE/'APOLAR_ENDPOINT_LITERAL_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    (HERE/'APOLAR_ENDPOINT_BINARY_CHECK.txt').write_text('\n'.join(messages)+'\n')
    print('PASS 5 exact biform identities and2 literal matrix finite-field checks')


if __name__=='__main__':main()
