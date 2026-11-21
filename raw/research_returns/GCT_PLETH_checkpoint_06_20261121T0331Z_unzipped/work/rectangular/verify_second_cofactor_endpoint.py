"""Independent binary and literal-minor audits for R029."""
from pathlib import Path
from math import factorial,comb
from fractions import Fraction
import csv
import sympy as sp
from collections import defaultdict
from verify_cofactor_endpoint_strip import mul,power
from verify_next_row_extensions import forms,product
from verify_apolar_endpoint import determinant

HERE=Path(__file__).resolve().parent


def U(r):
    return sum((-1)**i*(r-2*i)*comb(r,i)**2*factorial(r*i)*factorial(r*(r-i)) for i in range(r+1))


def pairing(p,q,N):
    q=q+[0]*(N+1-len(q))
    return sum(v*(-1)**(N-d)*factorial(N-d)*factorial(d)*q[N-d] for d,v in enumerate(p))


def binary(r):
    N=r*r-1;q=[1]+[0]*(r-1)+[1]
    qr=power(q,r);derivative=[(d+2)*(d+1)*qr[d+2] for d in range(len(qr)-2)]
    AA=pairing(mul([2,1],derivative),mul(power([2,1],r-2),power(q,r-1)),N)
    left=power(q,r-1);right=mul(power([2,1],r-1),power(q,r-2))
    BB=r*pairing([0]*(r-1)+left,[0]*(r-1)+right,N)
    for t in range(1,r):
        BB-=r*pairing([0]*(r-1-t)+left,[0]*(t-1)+right,N)
    uu=U(r)
    expectedA=Fraction(2**(r-2)*(r*r-r+1)*uu,2*r)
    expectedB=Fraction(2**(r-2)*(r-1)*uu,2*r*r*(r*r+1))
    assert AA==expectedA and BB==expectedB and AA+r*BB>0,(r,AA,BB,expectedA,expectedB)
    # Independently evaluate the unsimplified finite interval sum SE.15.
    beta=sum(comb(r-1,v)*comb(r-2,r-2-v)*(-1)**(r*v+r-1)*factorial(r*v+r-1)*factorial(N-r*v-r+1) for v in range(r-1))
    beta-=sum(comb(r-1,v)*comb(r-2,r-1-v)*sum((-1)**p*factorial(p)*factorial(N-p) for p in range(r*v,r*v+r-1)) for v in range(1,r))
    assert Fraction(beta)==Fraction(uu,2*r**3*(r*r+1))
    return dict(r=r,A=AA,B=BB,U=uu,beta=beta,status='PASS')


def literal(r):
    H=r*r+2;uu=U(r);t=max(1,(H+2*r-1)//(2*r))
    while True:
        prime=2*r*t+1;t+=1
        if prime<=H or not sp.isprime(prime) or uu%prime==0 or (r*r-r+2)%prime==0:continue
        g=int(sp.primitive_root(prime));step=(prime-1)//(2*r)
        aa=[(2+pow(g,step*(2*i+1),prime))%prime for i in range(r)]+[0]
        if all(aa[:r]):break
    coords=list(range(1,r+1))
    rows=[[(pow(aa[i],e,prime)-pow(aa[0],e,prime))%prime for i in coords] for e in range(2,r)]
    rows.append([int(i==r) for i in coords]);rows.append([(aa[i]-aa[0])%prime for i in coords])
    A=sp.Matrix(rows);D,y,z=forms(A,0,prime,True)
    maxes=(r,)*r+(2,);unit={(0,)*(r+1):1};poly=defaultdict(int)
    for j in range(r+1):
        xj=[int(i==j) for i in range(r+1)]
        term=product(unit,[xj,z[j],z[j]]+[y[i] for i in range(r+1) if i!=j],maxes,prime)
        for key,v in term.items():poly[key]=(poly[key]+v)%prime
    poly=product({key:v for key,v in poly.items() if v},[D]+[form for form in y for _ in range(r-2)],maxes,prime)
    actual=poly.get(maxes,0)
    eta=pow(determinant(rows,prime),-1,prime)
    expected=-pow(eta,r*r+1,prime)*pow(2,r-2,prime)*r*(r*r-r+2)*uu*pow(2*(r*r+1)*factorial(r)**r,-1,prime)%prime
    assert actual==expected and actual!=0,(r,prime,actual,expected)
    return dict(r=r,field='F'+str(prime),actual=actual,formula=expected,status='PASS')


def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)


def main():
    rows=[binary(r) for r in (3,5,7,9,11)]
    write('SECOND_COFACTOR_ENDPOINT_BINARY_CHECK.tsv',rows)
    print('PASS5 exact expanded binary and unsimplified factorial checks',flush=True)
    rows=[]
    for r in (3,5):
        row=literal(r);rows.append(row);print('PASS literal',row,flush=True)
    write('SECOND_COFACTOR_ENDPOINT_LITERAL_CHECK.tsv',rows)


if __name__=='__main__':main()
