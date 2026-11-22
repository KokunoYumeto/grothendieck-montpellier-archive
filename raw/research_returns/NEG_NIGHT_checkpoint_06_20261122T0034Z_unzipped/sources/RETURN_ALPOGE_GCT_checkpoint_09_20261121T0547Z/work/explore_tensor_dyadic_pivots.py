"""Exact one-edge pivots from the known dyadic axial-array vertex.

This is a bounded exploration, not a classification theorem.  All arithmetic
on arrays is rational; full product stabilizers are not computed.
"""
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path
import sympy as sp

OUT=Path(__file__).with_name('tensor_dyadic_pivots.json')
report={'status':'exploratory exact pivots','by_n':[]}

def linear(es):
    return all(len({(e[a],e[b]) for e in es})==len(es)
               for a,b in [(0,1),(0,2),(1,2)])

for n in range(4,13):
    M=2**(n-1)
    basis=[(0,0,0)]
    X=[1]
    for i in range(1,n):
        basis.extend([(i,0,i),(i,i,0),(i-1,i,i)])
        X.extend([2**(i-1),2**(i-1),M-2**(i-1)])
    all_edges=list(product(range(n),repeat=3))
    def col(e):
        i,j,k=e
        v=[0]*(3*n-2);v[i]=1
        if j<n-1:v[n+j]=1
        if k<n-1:v[2*n-1+k]=1
        return v
    B=sp.Matrix.hstack(*(sp.Matrix(col(e)) for e in basis))
    assert abs(B.det())==M
    assert B*sp.Matrix(X)==M*sp.ones(3*n-2,1)
    invM=M*B.inv()
    assert all(x.q==1 for x in invM)
    inv=[[int(invM[i,j]) for j in range(3*n-2)] for i in range(3*n-2)]
    stats={'n':n,'base_denominator':M,'pivots':0,'max_two_part':0,
           'max_linear_two_part':0,'same_order_count':0,'same_order_linear_count':0,'counterexamples':[]}
    for e in all_edges:
        if e in basis:continue
        rows=[i for i,v in enumerate(col(e)) if v]
        V=[sum(inv[i][j] for j in rows) for i in range(3*n-2)]
        positive=[i for i,v in enumerate(V) if v>0]
        assert positive
        leave=min(positive,key=lambda i:Fraction(X[i],V[i]))
        tau=Fraction(X[leave],V[leave])
        weights=[Fraction(X[i],M)-tau*Fraction(V[i],M) for i in range(len(X))]
        assert all(x>=0 for x in weights)
        edges=[b for b,x in zip(basis,weights) if x>0]+[e]
        weights=[x for x in weights if x>0]+[tau]
        den=math.lcm(*(x.denominator for x in weights));d2=den&-den
        islinear=linear(edges)
        stats['pivots']+=1
        if d2==M:
            stats['same_order_count']+=1
            stats['same_order_linear_count']+=int(islinear)
        stats['max_two_part']=max(stats['max_two_part'],d2)
        if islinear:stats['max_linear_two_part']=max(stats['max_linear_two_part'],d2)
        if d2>M:
            assert all(sum(x for edge,x in zip(edges,weights) if edge[part]==j)==1
                       for part in range(3) for j in range(n))
            C=sp.Matrix.hstack(*(sp.Matrix(col(edge)) for edge in edges))
            assert C.rank()==len(edges)
            cert={'entering_edge':[v+1 for v in e], 'denominator':den,'two_part':d2,
                  'no_two_slot_overlap':islinear,
                  'support':[[v+1 for v in edge] for edge in edges],
                  'weights':[[v.numerator,v.denominator] for v in weights],
                  'exact_all_marginals_one':True,'exact_columns_independent':True}
            stats['counterexamples'].append(cert)
            print('counterexample',n,den,d2,'linear',islinear,flush=True)
    report['by_n'].append(stats)
    OUT.write_text(json.dumps(report,indent=2))
    print('summary',{k:v for k,v in stats.items() if k!='counterexamples'},flush=True)
