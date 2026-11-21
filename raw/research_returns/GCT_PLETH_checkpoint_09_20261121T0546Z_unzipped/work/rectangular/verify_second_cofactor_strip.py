"""R030 exact biforms, finite factorial bounds, and literal matrix audit."""
from pathlib import Path
from math import factorial,comb
from fractions import Fraction
from collections import defaultdict
import csv
import sympy as sp
from verify_cofactor_endpoint_strip import mul,power
from verify_second_cofactor_endpoint import pairing
from verify_next_row_extensions import forms,product
from verify_apolar_endpoint import determinant

HERE=Path(__file__).resolve().parent


def sums(r,j):
    N=r*r+j-3
    aa=sum((-1)**(r*i+l)*comb(r,i)*comb(r-1,r-i)*comb(j-1,l)*comb(r-2,j-1-l)*(r*i)*(r*i-1)*factorial(r*i-2+l)*factorial(N-r*i+2-l) for i in range(1,r+1) for l in range(j))
    bb=0
    if j>=2:
        for l in range(j-1):
            h=j-1-l;factor=comb(j-2,l)*comb(r-1,h)
            for v in range(r-1):
                p=r*v+r-1+l
                bb+=factor*comb(r-1,v)*comb(r-2,r-2-v)*(-1)**p*factorial(p)*factorial(N-p)
            for v in range(1,r):
                for t in range(1,r):
                    p=r*v+r-1-t+l
                    bb-=factor*comb(r-1,v)*comb(r-2,r-1-v)*(-1)**p*factorial(p)*factorial(N-p)
    total=aa+r*r*(j-1)*bb
    assert total>0,(r,j,total)
    if r>=10:
        scale=r*r*(r*r-1)*factorial(N)
        endpoint=sum((-1)**(r*r+l)*comb(j-1,l)*comb(r-2,j-1-l)*r*r*(r*r-1)*factorial(r*r-2+l)*factorial(j-1-l) for l in range(j))
        assert Fraction(endpoint,scale)>=Fraction(3,r)
        assert Fraction(abs(aa-endpoint),scale)<Fraction(1,r*r)
        assert Fraction(abs(r*r*(j-1)*bb),scale)<Fraction(12,r*r)
    return aa,bb,total


def binary(r,j):
    N=r*r+j-3;aa,bb,total=sums(r,j)
    q=[1]+[0]*(r-1)+[1];qr=power(q,r)
    der=[(d+2)*(d+1)*qr[d+2] for d in range(len(qr)-2)]
    A=pairing(mul(power([2,1],j-1),der),mul(power([2,1],r-2),power(q,r-1)),N)
    B=0
    if j>=2:
        left=mul(power([2,1],j-2),power(q,r-1));right=mul(power([2,1],r-1),power(q,r-2))
        B=r*pairing([0]*(r-1)+left,[0]*(r-1)+right,N)
        for t in range(1,r):B-=r*pairing([0]*(r-1-t)+left,[0]*(t-1)+right,N)
    assert A==2**(r-2)*aa and B==r*2**(r-2)*bb
    coefficient=Fraction(A+r*(j-1)*B,factorial(j-1)*factorial(r)**r)
    assert coefficient.denominator==1 and coefficient>0
    return dict(r=r,j=j,A=aa,beta=bb,positive_total=total,positive_coefficient=int(coefficient),status='PASS')


def literal(r,j):
    H=r*r+j;_,_,target=sums(r,j);t=max(1,(H+2*r-1)//(2*r))
    while True:
        prime=2*r*t+1;t+=1
        if prime<=H or not sp.isprime(prime) or target%prime==0:continue
        g=int(sp.primitive_root(prime));step=(prime-1)//(2*r)
        av=[(2+pow(g,step*(2*i+1),prime))%prime for i in range(r)]+[0]
        if all(av[:r]):break
    coords=list(range(1,r+1))
    rows=[[(pow(av[i],e,prime)-pow(av[0],e,prime))%prime for i in coords] for e in range(2,r)]
    rows.append([int(i==r) for i in coords]);rows.append([(av[i]-av[0])%prime for i in coords])
    A=sp.Matrix(rows);D,y,z=forms(A,0,prime,True)
    maxes=(r,)*r+(j,);unit={(0,)*(r+1):1};poly=defaultdict(int)
    for i in range(r+1):
        xi=[int(t==i) for t in range(r+1)]
        term=product(unit,[xi,z[i],z[i]]+[y[t] for t in range(r+1) if t!=i],maxes,prime)
        for key,v in term.items():poly[key]=(poly[key]+v)%prime
    poly=product({key:v for key,v in poly.items() if v},[D]*(j-1)+[form for form in y for _ in range(r-2)],maxes,prime)
    actual=poly.get(maxes,0);eta=pow(determinant(rows,prime),-1,prime)
    expected=(-1)**(r-2)*pow(eta,H-1,prime)*pow(2,r-2,prime)*target*pow(factorial(j-1)*factorial(r)**r,-1,prime)%prime
    assert actual==expected and actual!=0,(r,j,prime,actual,expected)
    return dict(r=r,j=j,field='F'+str(prime),actual=actual,formula=expected,status='PASS')


def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)


def write_small_certificate(small):
    assert len(small)==20
    lines=['Decimal digits are grouped in blocks of three for readability.','',
           '| r | j | Positive coefficient after removing the nonzero signed eta factor |',
           '|---:|---:|---:|']
    for row in small:
        number=f'{int(row["positive_coefficient"]):,}'.replace(',',' ')
        lines.append(f'| {row["r"]} | {row["j"]} | {number} |')
    (HERE/'SECOND_COFACTOR_STRIP_SMALL_CERTIFICATE.md').write_text('\n'.join(lines)+'\n')


def main():
    rows=[binary(r,j) for r in range(2,13) for j in range(1,r) if (r+j)%2]
    write('SECOND_COFACTOR_STRIP_BINARY_CHECK.tsv',rows)
    small=[row for row in rows if row['r']<10];assert len(small)==20
    write_small_certificate(small)
    print('PASS exact expanded binary checks',len(rows),'including20 exhaustive small cases',flush=True)
    for r in range(13,21):
        for j in range(1,r):
            if (r+j)%2:sums(r,j)
    print('PASS literal factorial inequality audits through r20',flush=True)
    rows=[]
    for r,j in [(4,3),(5,4),(6,3),(6,5)]:
        row=literal(r,j);rows.append(row);print('PASS literal',row,flush=True)
    write('SECOND_COFACTOR_STRIP_LITERAL_CHECK.tsv',rows)


if __name__=='__main__':main()
