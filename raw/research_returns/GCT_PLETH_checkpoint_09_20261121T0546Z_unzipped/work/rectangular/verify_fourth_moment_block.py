"""R038 direct expanded polynomial pairings for the quartic canonical block."""
from pathlib import Path
from fractions import Fraction
from math import comb,factorial
from collections import defaultdict
import csv
import sympy as sp
from verify_rectangular import partitions
from verify_second_row_two_rank_law import product_form

HERE=Path(__file__).resolve().parent


def polynomials(a):
    w=sp.symbols('w0:'+str(a));mean=sum(w)/a
    p=sp.Poly(sum((v-mean)**4 for v in w),*w)
    k=sp.Poly(sum((v-mean)**2 for v in w)**2,*w)
    def rational(poly):
        return {tuple(e):Fraction(int(c.p),int(c.q)) for e,c in poly.terms()}
    pp,kk=rational(p),rational(k)
    jj={e:a*(a-1)*pp.get(e,0)-(a*a-3*a+3)*kk.get(e,0) for e in pp.keys()|kk.keys()}
    jj={e:c for e,c in jj.items() if c}
    assert all(max(e)<=2 for e in jj)
    return pp,kk,jj


def evaluate(poly,values):
    result=Fraction(0)
    for exponents,c in poly.items():
        for e,v in zip(exponents,values):c*=v**e
        result+=c
    return result


def pair(poly,n,vectors):
    q=product_form(vectors)
    moments=[Fraction(q.get((n-e,e),0),comb(n,e)) for e in range(n+1)]
    result=Fraction(0)
    for exponents,c in poly.items():
        assert max(exponents)<=n
        for e in exponents:c*=moments[e]
        result+=c
    return result


def matrix(a,n):
    C4=Fraction((a-1)*(a*a-3*a+3),a*a)
    C22=Fraction(3*(a-1)*(2*a-3),a*a)
    D4=Fraction((a-1)**2,a)
    D22=Fraction((a-1)*(a*a-2*a+3),a)
    n4=n*(n-1)*(n-2)*(n-3);n22=n*n*(n-1)*(n-1)
    return ((-6*C4/n4,-6*D4/n4),
            (3*C4/n4+C22/n22,3*D4/n4+D22/n22))


def main():
    rows=[];cache={a:polynomials(a) for a in range(2,9)}
    for a in range(2,9):
        P,K,J=cache[a]
        for n in range(4,9):
            M=matrix(a,n)
            determinant=M[0][0]*M[1][1]-M[0][1]*M[1][0]
            formula=Fraction(-6*(a-1)**2*(a-2)*(a-3),
                             a*n**3*(n-1)**3*(n-2)*(n-3))
            assert determinant==formula
            for sample in (0,1):
                values=[Fraction(0)]*n
                values[0]=1
                if sample:values[1]=-1
                vectors=[(i+1,(i+1)*v) for i,v in enumerate(values)]
                padding=factorial(n)**a
                outP=padding*evaluate(cache[n][0],values)
                outK=padding*evaluate(cache[n][1],values)
                for col,poly in enumerate((P,K)):
                    value=pair(poly,n,vectors)
                    expected=M[0][col]*outP+M[1][col]*outK
                    assert value==expected,(a,n,sample,col,value,expected)
                    rows.append(dict(a=a,n=n,sample=sample,generator=('P','K')[col],
                                     literal_pairing=str(value),matrix_value=str(expected),
                                     matrix_determinant=str(determinant),status='PASS'))
        print('quartic matrix checks completed a',a,flush=True)
    for a in range(4,9):
        J=cache[a][2]
        assert J
        for n in (2,3):
            for sample in (0,1):
                values=[Fraction(0)]*n;values[0]=1
                if sample:values[1]=-1
                vectors=[(i+1,(i+1)*v) for i,v in enumerate(values)]
                value=pair(J,n,vectors)
                scalar=Fraction(-a*(a-1)*(a-2)*(a-3),n*n*(n-1)*(n-1))
                expected=scalar*factorial(n)**a*evaluate(cache[n][1],values)
                assert value==expected and value,(a,n,sample,value,expected)
                rows.append(dict(a=a,n=n,sample=sample,generator='J',literal_pairing=str(value),
                                 matrix_value=str(expected),matrix_determinant='',status='PASS'))
    with (HERE/'FOURTH_MOMENT_CANONICAL_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    weights=[]
    for a in range(2,9):
        for n in range(2,9):
            if a*n<8:continue
            count=lambda k:sum(len(p)<=a and max(p,default=0)<=n for p in partitions(k))
            coefficient=count(4)-count(3)
            want=2 if min(a,n)>=4 else int(max(a,n)>=4)
            assert coefficient==want,(a,n,coefficient,want)
            weights.append(dict(a=a,n=n,target_weight_difference=coefficient,status='PASS'))
    with (HERE/'FOURTH_MOMENT_BINARY_WEIGHT_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(weights[0]),delimiter='\t')
        writer.writeheader();writer.writerows(weights)
    print('PASS literal polynomial pairings',len(rows),'and independent binary weight counts',len(weights),flush=True)


if __name__=='__main__':main()
