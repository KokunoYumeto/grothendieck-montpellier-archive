"""Independent exact audits of the new R027 coefficient formulas."""
from pathlib import Path
from math import factorial,comb
from collections import defaultdict
import csv
import sympy as sp
from verify_apolar_endpoint import determinant,positive_sum

HERE=Path(__file__).resolve().parent


def odd_sum(r):
    ds=[comb(r,i)**2*factorial(r*i)*factorial(r*(r-i)) for i in range(r+1)]
    U=sum((-1)**i*(r-2*i)*ds[i] for i in range(r+1))
    value=2**(r-1)*(r*r-r+2)*U
    assert value%(2*r)==0 and U>0
    return value//(2*r)


def forms(A,q,pmod,need_z):
    r=A.rows;n=r+1;coords=[i for i in range(n) if i!=q]
    B0=sp.Matrix([[int(j==i)-int(j==q) for j in range(n)] for i in coords])
    inverse=A.inv() if pmod is None else A.inv_mod(pmod)
    B=(inverse.T*B0).tolist()
    if pmod is None:
        assert all(v.q==1 for row in B for v in row)
        B=[[int(v) for v in row] for row in B]
        det=lambda rows:int(sp.Matrix(rows).det(method='domain-ge'))
    else:
        B=[[int(v)%pmod for v in row] for row in B]
        det=lambda rows:determinant(rows,pmod)
    D=[];y=[[] for _ in range(n)];z=[[] for _ in range(n)] if need_z else None
    for j in range(n):
        X=[[int(j==i) for i in range(n)]]+B
        D.append(det(X))
        for col in range(n):
            for rowidx,arr in [(n-1,y)]+([(n-2,z)] if need_z else []):
                minor=[[row[k] for k in range(n) if k!=col] for i,row in enumerate(X) if i!=rowidx]
                v=(-1)**(rowidx+col)*det(minor)
                arr[col].append(v if pmod is None else v%pmod)
    return D,y,z


def multiply(poly,linear,maxes,pmod):
    out=defaultdict(int)
    for a,c in poly.items():
        for i,v in enumerate(linear):
            if v and a[i]<maxes[i]:
                b=a[:i]+(a[i]+1,)+a[i+1:]
                out[b]+=c*v
                if pmod:out[b]%=pmod
    return {a:c for a,c in out.items() if c}


def product(poly,factors,maxes,pmod):
    for factor in factors:poly=multiply(poly,factor,maxes,pmod)
    return poly


def coefficient(r,k,kind,A,q,pmod=None):
    n=r+1;H=r*r+1;D,y,z=forms(A,q,pmod,kind=='F')
    maxes=(r,)*r+(1,);unit={(0,)*n:1}
    if kind=='G':
        poly=product(unit,[form for form in y for _ in range(k)]+[D]*(H-n*k),maxes,pmod)
    else:
        poly=defaultdict(int)
        for j in range(n):
            xj=[int(i==j) for i in range(n)]
            term=product(unit,[xj,z[j],z[j]]+[y[i] for i in range(n) if i!=j],maxes,pmod)
            for a,c in term.items():
                poly[a]+=c
                if pmod:poly[a]%=pmod
        poly={a:c for a,c in poly.items() if c}
        poly=product(poly,[form for form in y for _ in range(k-2)]+[D]*(H-n*(k-1)-2),maxes,pmod)
    return poly.get(maxes,0)


def group_A(r,sg,kind):
    n=r+1;I=list(range(sg-1))+[r];J=[i for i in range(n) if i not in I]
    q=I[0];p=r if kind=='F' else None
    coords=[i for i in range(n) if i!=q];j0=J[0]
    omitted={j0} if p is None else {j0,p}
    rows=[[int(j==i) for j in coords] for i in coords if i not in omitted]
    if p is not None:rows.append([int(j==p) for j in coords])
    rows.append([int(j in J) for j in coords])
    return sp.Matrix(rows),q


def interior(r,k,kind):
    H=r*r+1
    if kind=='F':
        sg=r//2+1;h=H-(r+1)*(k-1);u=r*(r-k+1)//2
        expected=(-1)**(sg*(k-1)+1)*comb(h,u)*factorial(r*r//2)**2
    else:
        sg=(r+1)//2;h=H-(r+1)*k;dI=r*(sg-1)+1;dJ=r*sg;u=dI-k*sg
        expected=(-1)**(sg*k)*comb(h,u)*factorial(dI)*factorial(dJ)
    denominator=factorial(r)**r
    assert expected%denominator==0;expected//=denominator
    A,q=group_A(r,sg,kind);value=coefficient(r,k,kind,A,q)
    assert value==expected and value!=0
    return dict(kind=kind,r=r,k=k,field='Q',actual=value,formula=expected,status='PASS')


def endpoint(r,kind):
    H=r*r+1;target=positive_sum(r) if kind=='F' else odd_sum(r)
    c=1 if kind=='F' else 2
    t=(H+2*r-1)//(2*r)
    while True:
        prime=2*r*t+1;t+=1
        if prime<=H or not sp.isprime(prime) or target%prime==0:continue
        g=int(sp.primitive_root(prime));step=(prime-1)//(2*r)
        av=[(c+pow(g,step*(2*i+1),prime))%prime for i in range(r)]
        if all(av):break
    if kind=='F':
        av.append(0);q=0;coords=list(range(1,r+1))
        rows=[[(pow(av[i],j,prime)-pow(av[0],j,prime))%prime for i in coords] for j in range(2,r)]
        rows.append([int(i==r) for i in coords])
        rows.append([(av[i]-av[0])%prime for i in coords])
        A=sp.Matrix(rows);eta=pow(determinant(rows,prime),-1,prime);k=r
        expected=pow(eta,r*r,prime)*target*pow(factorial(r)**r,-1,prime)%prime
    else:
        q=r;rows=[[pow(v,j,prime) for v in av] for j in list(range(2,r+1))+[1]]
        A=sp.Matrix(rows);eta=-pow(determinant(rows,prime),-1,prime)%prime;k=r-1
        expected=pow(eta,H,prime)*target*pow(factorial(r)**r,-1,prime)%prime
    value=coefficient(r,k,kind,A,q,prime)
    assert value==expected and value!=0,(r,kind,prime,value,expected)
    return dict(kind=kind,r=r,k=k,field='F'+str(prime),actual=value,formula=expected,status='PASS')


def main():
    x,z=sp.symbols('x z');notes=[]
    for r in (2,4,6,8):
        Q=(z-x)**r+x**r;P=sp.Poly(Q**r,x,z);R=sp.Poly(x*x*z**(r-2)*Q**(r-1),x,z)
        value=sum(int(v)*(-1)**i*factorial(i)*factorial(j)*int(R.coeff_monomial((j,i))) for (i,j),v in P.terms())
        assert value==positive_sum(r)
        notes.append(f'PASS F endpoint full binary expansion r={r}: pairing={value}')
    for r in (3,5,7,9):
        Q=(z-2*x)**r+x**r;P=sp.Poly(z*Q**r,x,z);R=sp.Poly(x*x*z**(r-1)*Q**(r-1),x,z)
        value=sum(int(v)*(-1)**i*factorial(i)*factorial(j)*int(R.coeff_monomial((j,i))) for (i,j),v in P.terms())
        assert value==odd_sum(r)>0
        notes.append(f'PASS G endpoint full binary expansion r={r}: pairing={value}')
    (HERE/'NEXT_ROW_APOLAR_EXPANSION_CHECK.txt').write_text('\n'.join(notes)+'\n')
    print('PASS all8 exact biform expansions',flush=True)
    rows=[]
    for case in [(4,3,'F'),(6,5,'F'),(5,3,'G')]:
        row=interior(*case);rows.append(row);print('PASS',row,flush=True)
    for r,kind in [(2,'F'),(4,'F'),(6,'F'),(3,'G'),(5,'G')]:
        row=endpoint(r,kind);rows.append(row);print('PASS',row,flush=True)
    with (HERE/'NEXT_ROW_EXTENSION_COEFFICIENT_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS3 literal integer evaluations and5 literal finite-field matrix evaluations')


if __name__=='__main__':main()
