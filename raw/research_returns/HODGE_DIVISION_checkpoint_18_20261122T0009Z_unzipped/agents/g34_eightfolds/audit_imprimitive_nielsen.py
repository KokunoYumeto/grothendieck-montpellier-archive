#!/usr/bin/env python3
"""Independent basis-image verification of the D-IM-08 monomial words.
Does not import the author's implementation or enumerate the full groups.
"""
from fractions import Fraction
from pathlib import Path
from math import gcd
import json

def case(d,e):
    def compose(A,B):
        return [(A[j][0],(c+A[j][1])%d) for j,c in B]
    def inverse(A):
        B=[None]*12
        for j,(k,c) in enumerate(A): B[k]=(j,-c%d)
        return B
    identity=[(j,0) for j in range(12)]
    def power(A,n):
        B=identity
        for _ in range(n): B=compose(B,A)
        return B
    k=7 if e==d else 6
    a=[((j+1)%12, e if e<d and j==11 else 0) for j in range(12)]
    b=[((j+1)%k if j<k else j, 1 if j==0 else -1 if j==(k-1 if e==d else 1) else 0) for j in range(12)]
    b=[(j,c%d) for j,c in b]
    aa,bb=inverse(a),inverse(b)
    assert compose(compose(compose(a,aa),b),bb)==identity
    c=compose(aa,b)
    D=power(c,6 if e==d else 7)
    expected=([6]+[0]*5+[-1]*6) if e==d else ([7,-7]+[0]*3+[-e]*7)
    assert D==[(j,v%d) for j,v in enumerate(expected)]
    i,j=(1,6) if e==d else (0,2)
    s=identity[:];s[i],s[j]=s[j],s[i]
    comm=compose(compose(compose(D,s),inverse(D)),s)
    colors=[v for q,v in comm if v]
    assert len(colors)==2 and sum(colors)%d==0 and gcd(colors[0],d)==1
    def invariants(A):
        visited=set(); fixed=0; age=Fraction()
        for j in range(12):
            if j in visited: continue
            n=0; color=0; q=j
            while q not in visited:
                visited.add(q); n+=1; q2,c=A[q]; color+=c; q=q2
            color%=d
            fixed+=not color
            age+=Fraction(n-1,2)+Fraction(color,d)
        return fixed,age
    facts=[invariants(g) for g in [a,aa,b,bb]]
    assert sum(age for fixed,age in facts)-12==5
    assert 12-facts[0][0]-facts[2][0]==5
    return {'d':d,'e':e,'diagonal_power':[v for q,v in D],
            'primitive_commutator':[v for q,v in comm],
            'fixed_dimensions':[fixed for fixed,age in facts],
            'ages':[str(age) for fixed,age in facts],
            'graph_multiplicity':5,'chevalley_weil_each_embedding':5}

if __name__=='__main__':
    out={'independent_method':__doc__,'cases':[case(d,e) for d in [3,4,6] for e in range(1,d+1) if d%e==0]}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: nine cases, exact diagonal powers, primitive commutators, ages and graph multiplicity')
