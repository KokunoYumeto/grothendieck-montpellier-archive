#!/usr/bin/env python3
"""Exact integral Laurent-polynomial verification of the P-20 eighteen-term curve."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from sympy import Matrix,Symbol,simplify,zeros

t=Symbol('t',nonzero=True)
# Coordinates of the first-factor coefficients, one column per pure summand.
star_A=[Matrix([-1/t,-1/t]),Matrix([1/t,0]),Matrix([0,1/t])]
star_V=[Matrix([1,0,0]),Matrix([1,t,0]),Matrix([1,0,t])]
graph_A=[Matrix([-1/t,-1/t,-1/t,1/t**2,1/t**2]),
         Matrix([1/t,0,0,-1/t**2,-1/t**2]),
         Matrix([0,1/t,0,-1/t**2,0]),
         Matrix([0,0,1/t,0,-1/t**2]),
         Matrix([0,0,0,1/t**2,0]),Matrix([0,0,0,0,1/t**2])]
graph_V=[Matrix([1,0,0,0]),Matrix([1,t,0,0]),Matrix([1,0,t,0]),
         Matrix([1,0,0,t]),Matrix([1,t,t,0]),Matrix([1,t,0,t])]


def curve(A,V):
    return [sum((a[q]*(v*v.T) for a,v in zip(A,V)),zeros(V[0].rows)) for q in range(A[0].rows)]


def matching(n,edge):
    M=zeros(n);i,j=edge;M[i,j]=M[j,i]=1;return M


def main():
    star=curve(star_A,star_V);graph=curve(graph_A,graph_V)
    S=[matching(3,(0,1)),matching(3,(0,2))]
    edges=[(0,1),(0,2),(0,3),(1,2),(1,3)];G=[matching(4,e) for e in edges]
    for q,M in enumerate(star):
        D=zeros(3);D[q+1,q+1]=1
        assert (M-S[q]-t*D).applyfunc(simplify)==zeros(3)
    for q,M in enumerate(graph):
        D=zeros(4)
        if q<3:D[q+1,q+1]=1
        assert (M-G[q]-t*D).applyfunc(simplify)==zeros(4)
    # Check the exact identification with the ten indicated permanent minors.
    rectangles=[((0,i),e) for i in [1,2] for e in edges]
    for q,(I,J) in enumerate(rectangles):
        r,s=I;c,d=J;a,b,x,y=4*r+c,4*r+d,4*s+c,4*s+d
        direct=zeros(12)
        for i,j in [(a,y),(y,a),(b,x),(x,b)]:direct[i,j]=1
        product=Matrix.kronecker_product(S[q//5],G[q%5]) if hasattr(Matrix,'kronecker_product') else None
        if product is None:
            from sympy import kronecker_product
            product=kronecker_product(S[q//5],G[q%5])
        assert product==direct
    out={'status':'PASS','finding':'P-20','subset':[0,1,2,3,4,6,7,8,9,10],
         'tensor_format':[10,12,12],'pure_summands':len(star_A)*len(graph_A),
         'star_identity':'S(t)=S+t sum_{i=1,2} alpha_i tensor e_i tensor e_i',
         'graph_identity':'G(t)=G+t sum_{i=1,2,3} gamma_0i tensor e_i tensor e_i',
         'arithmetic':'exact Laurent-polynomial identities with integer coefficients; valid after base change to every field',
         'utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
         'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('per10_upper18_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
