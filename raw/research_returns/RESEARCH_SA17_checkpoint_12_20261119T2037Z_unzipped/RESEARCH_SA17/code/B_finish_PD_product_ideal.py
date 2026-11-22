#!/usr/bin/env python3
"""Exploratory graded presentation for the PD envelope of (xy,xz).

This is a diagnostic, not a proof of the full PD-envelope presentation.
Generators in multidegree (a,b,c) are the divided monomials
x^(a-m-n)y^(b-m)z^(c-n) gamma_m(xy) gamma_n(xz).
We impose the linear divided-power relations and all scalar syzygies
z^q gamma_q(xy)=y^q gamma_q(xz).  A quotient of dimension one
modulo p is evidence of p-flatness in that grade; a larger dimension is
only a candidate torsion class until the universal presentation is proved.
"""
from math import comb
from pathlib import Path
import json, time

def rank(rows,n,p):
    piv={}
    for row in rows:
        row=[x%p for x in row]
        while any(row):
            j=next(j for j,x in enumerate(row) if x)
            if j in piv:
                f=row[j]; row=[(a-f*b)%p for a,b in zip(row,piv[j])]
            else:
                f=pow(row[j],-1,p)
                piv[j]=[(x*f)%p for x in row]
                break
    return len(piv)

def grade(a,b,c,p):
    pts=[(m,n) for m in range(min(a,b)+1) for n in range(min(a-m,c)+1)]
    idx={v:i for i,v in enumerate(pts)}; rows=[]
    def relation(terms):
        row=[0]*len(pts)
        for mn,co in terms:row[idx[mn]]+=co
        rows.append(row)
    for m,n in pts:
        if (m+1,n) in idx:relation([((m+1,n),m+1),((m,n),-1)])
        if (m,n+1) in idx:relation([((m,n+1),n+1),((m,n),-1)])
        for q in range(1,min(a-m-n,b-m,c-n)+1):
            relation([((m+q,n),comb(m+q,q)),((m,n+q),-comb(n+q,q))])
    return len(pts)-rank(rows,len(pts),p)

def main():
    start=time.monotonic(); bound=10; rows=[]
    for p in (2,3,5):
        bad=[]
        for a in range(bound+1):
          for b in range(bound+1):
            for c in range(bound+1):
                d=grade(a,b,c,p)
                if d!=1:bad.append({'grade':[a,b,c],'dimension':d})
        rows.append({'p':p,'bound':bound,'grades':(bound+1)**3,'bad':bad})
    out={'status':'exploratory; presentation not yet proved universal',
         'seconds':round(time.monotonic()-start,4),'results':rows}
    (Path(__file__).resolve().parents[1]/'logs/B_finish_PD_product_ideal.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
