"""Check the explicit seed exponents at the proved range boundaries.

This finite arithmetic check supplements, and does not replace,
Nagura's theorem and the symbolic conductor proof in R021.
"""
from pathlib import Path
from math import isqrt
import csv

HERE=Path(__file__).resolve().parent


def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def main():
    small=(3,5,7,11,11,13,17,17,19,23,23)
    for a,p in zip(range(4,25,2),small):
        assert prime(p) and abs(p-a)==1
        assert (a-2)*a==a*(a-2)
    rows=[]
    for a in range(26,101):
        p=a+1
        while not prime(p):p+=1
        assert 5*p<6*a
        widths=[2*((9*a*a+24)//25)]
        if a%2==0:widths.append(a*(a-2))
        for B in sorted(set(widths)):
            g=(p-1)//2;N=B//2;y=N%g;x=N//g-y
            assert B%2==0 and x>=0 and y>=0
            assert x*(p-1)+y*(p+1)==B
            assert 2*g*(g-1)<B
            rows.append(dict(a=a,p=p,B=B,x=x,y=y,
                             conductor=2*g*(g-1),status='PASS'))
    with (HERE/'NAGURA_IMAGE_EXPONENT_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'seed exponent checks and11 small prime-adjacent widths')


if __name__=='__main__':main()
