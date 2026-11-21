#!/usr/bin/env python3
"""Exact ordered-tensor finite differences proving per5 <=11 and per6 <=12."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json


def subsets(S):
    return [frozenset(x) for size in range(len(S)+1) for x in combinations(sorted(S),size)]


def vector_at(R):
    # Parameters 0=u,1=w,2=y,3=z; row/column base coordinate has degree zero.
    rows=[(0,None)]+[(1,0)]*(0 in R)+[(2,1)]*(1 in R)
    cols=[(0,None)]+[(1,2)]*(2 in R)+[(2,3)]*(3 in R)
    return [(3*i+j, int(p is not None)+int(q is not None)) for i,p in rows for j,q in cols]


def add(out,key,v):
    out[key]+=v
    if out[key]==0:del out[key]


def check(count):
    supports=[frozenset(x) for x in [(0,2),(0,3),(0,2,3),(1,2),(1,3),(1,2,3)][:count]]
    rectangles=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(1,2)),
                ((0,2),(0,1)),((0,2),(0,2)),((0,2),(1,2))][:count]
    polynomial=defaultdict(int)
    points=defaultdict(list)
    for q,S in enumerate(supports):
        for R in subsets(S):
            sign=(-1)**(len(S)-len(R))
            points[R].append({'slice':q,'coefficient':sign,'t_power':-len(S)})
            V=vector_at(R)
            for i,p in V:
                for j,r in V:
                    add(polynomial,(p+r-len(S),q,i,j),sign)
    assert all(p>=0 for p,q,i,j in polynomial)
    constant={(q,i,j):c for (p,q,i,j),c in polynomial.items() if p==0}
    expected={}
    for q,((r,s),(c,d)) in enumerate(rectangles):
        a,b,x,y=3*r+c,3*r+d,3*s+c,3*s+d
        for i,j in [(a,y),(y,a),(b,x),(x,b)]:expected[(q,i,j)]=1
    assert constant==expected
    assert len(points)==count+6
    return {'slices':count,'pure_tensor_terms':len(points),'identity_over':'Z[t,t^-1]',
            'points':[{'parameters':sorted(R),'first_factor_coefficients':coeffs}
                      for R,coeffs in sorted(points.items(),key=lambda x:(len(x[0]),sorted(x[0])))],
            'cancelled_polynomial_terms':[[list(k),v] for k,v in sorted(polynomial.items())],
            'status':'PASS'}


def main():
    output=[check(n) for n in (5,6)]
    path=Path(__file__).with_name('finite_difference_certificate.json')
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps([{k:v for k,v in x.items() if k not in ['points','cancelled_polynomial_terms']} for x in output],indent=2))


if __name__=='__main__':main()
