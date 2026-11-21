"""Exact independent audits for R028: binary expansion and literal matrix minors."""
from pathlib import Path
from math import comb,factorial
from fractions import Fraction
import csv
import sympy as sp
from verify_apolar_endpoint import determinant
from verify_next_row_extensions import forms,product

HERE=Path(__file__).resolve().parent


def scalar(r,j):
    H=r*r+j
    return sum((-1)**(r*i+l)*comb(r,i)*comb(r-1,r-i)*comb(j,l)*comb(r-1,j-l)*factorial(r*i+l)*factorial(H-r*i-l)
               for i in range(1,r+1) for l in range(j+1))


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c


def power(a,k):
    out=[1]
    for _ in range(k):out=mul(out,a)
    return out


def expansion(r,j):
    H=r*r+j
    q=[comb(r,d)*(-2)**(r-d) for d in range(r+1)];q[0]+=1
    p=[0]*j+power(q,r)
    rr=[0]*(r-1)+power(q,r-1)
    rr += [0]*(H+1-len(rr))
    pair=sum(v*(-1)**(H-d)*factorial(H-d)*factorial(d)*rr[H-d] for d,v in enumerate(p))
    value=scalar(r,j)
    assert pair==2**(r-1)*value and value>0,(r,j,pair,value)
    if r>=5:
        endpoint=sum((-1)**(r*r+l)*comb(j,l)*comb(r-1,j-l)*factorial(r*r+l)*factorial(j-l) for l in range(j+1))
        endpoint_bound=Fraction(4*(r-1),r*r+r-2)*factorial(H)
        interior_bound=Fraction((r-1)*2**(r-1),r**(r-2))*factorial(H)
        assert endpoint>=endpoint_bound>interior_bound>=abs(value-endpoint)
    return dict(r=r,j=j,degree=H,apolar_pairing=pair,factorial_sum=value,status='PASS')


def literal(r,j):
    H=r*r+j;value=scalar(r,j)
    t=max(1,(H+2*r-1)//(2*r))
    while True:
        prime=2*r*t+1;t+=1
        if prime<=H or not sp.isprime(prime) or value%prime==0:continue
        g=int(sp.primitive_root(prime));step=(prime-1)//(2*r)
        aa=[(2+pow(g,step*(2*i+1),prime))%prime for i in range(r)]
        if all(aa):break
    rows=[[pow(v,e,prime) for v in aa] for e in list(range(2,r+1))+[1]]
    A=sp.Matrix(rows)
    D,y,_=forms(A,r,prime,False)
    n=r+1;maxes=(r,)*r+(j,)
    poly=product({(0,)*n:1},[D]*(j+1)+[form for form in y for _ in range(r-1)],maxes,prime)
    actual=poly.get(maxes,0)
    eta=(-1)**r*pow(determinant(rows,prime),-1,prime)%prime
    expected=(-1)**(r-1)*pow(eta,H,prime)*pow(2,r-1,prime)*value*pow(factorial(j)*factorial(r)**r,-1,prime)%prime
    assert actual==expected and actual!=0,(r,j,prime,actual,expected)
    return dict(r=r,j=j,field='F'+str(prime),actual=actual,formula=expected,status='PASS')


def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)


def main():
    rows=[expansion(r,j) for r in range(2,11) for j in range(r-1) if (r+j)%2==0]
    write('COFACTOR_ENDPOINT_STRIP_BINARY_CHECK.tsv',rows)
    print('PASS exact binary expansions',len(rows),flush=True)
    rows=[]
    for r,j in [(2,0),(3,1),(4,2),(5,3),(6,2),(6,4)]:
        row=literal(r,j);rows.append(row);print('PASS literal',row,flush=True)
    write('COFACTOR_ENDPOINT_STRIP_LITERAL_CHECK.tsv',rows)
    print('PASS literal finite-field matrix checks',len(rows),flush=True)


if __name__=='__main__':main()
