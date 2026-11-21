"""Direct cofactor Jacobian ranks and graph certificates for O020."""
from __future__ import annotations

import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


def colored_trees(R, n):
    assert R>=1 and n>=2*R
    colors={}
    trees=[]
    for j in range(R):
        cyclic=[j]
        for t in range(1,R):
            cyclic.extend(((j-t)%(2*R),(j+t)%(2*R)))
        cyclic.append((j-R)%(2*R))
        path=cyclic
        assert len(path)==2*R and len(set(path))==2*R
        edges=[tuple(sorted(pair)) for pair in zip(path,path[1:])]
        edges.extend((j,vertex) for vertex in range(2*R,n))
        assert len(edges)==n-1 and len(set(edges))==n-1
        for edge in edges:
            assert edge not in colors
            colors[edge]=j
        adjacency=[set() for _ in range(n)]
        for a,b in edges:
            adjacency[a].add(b);adjacency[b].add(a)
        seen={0};frontier=[0]
        while frontier:
            node=frontier.pop()
            for nxt in adjacency[node]-seen:
                seen.add(nxt);frontier.append(nxt)
        assert len(seen)==n
        trees.append(edges)
    return colors,trees


packing=[]
for R in range(1,9):
    for n in (2*R,2*R+2):
        colors,trees=colored_trees(R,n)
        packing.append({'R':R,'n':n,'trees':len(trees),
                        'distinct_colored_edges':len(colors),'status':'PASS'})

rank_cases=[]
for R,n in [(1,2),(1,3),(1,4),(2,4),(2,5),(2,6),(3,6),(3,7)]:
    colors,trees=colored_trees(R,n)
    t=sp.Symbol('t')
    z=sp.symbols(f'z0:{R}')
    A=sp.diag(*(t-(i+1) for i in range(n)))
    for (i,j),color in colors.items():
        A[i,j]=-z[color]
    assert sp.expand(A.det()-sp.prod(t-(i+1) for i in range(n)))==0
    gammas=sorted((g for g in itertools.product(range(3),repeat=R) if sum(g)<=2),
                  key=lambda g:(sum(g),g))
    basis=[(power,)+g for g in gammas for power in range(n-sum(g)+1)]
    index={monomial:i for i,monomial in enumerate(basis)}
    def vector(poly):
        result=[sp.Integer(0)]*len(basis)
        for exponents,coefficient in sp.Poly(sp.expand(poly),t,*z).terms():
            if sum(exponents[1:])<=2:
                assert exponents in index
                result[index[exponents]]+=coefficient
        return sp.Matrix(result)
    columns=[]
    for i in range(n):
        # Actual minors, not the path expansion used in the mathematical proof.
        cofactor=A.cofactor(i,i)
        for H in (sp.Integer(1),t,*z):
            columns.append(vector(H*cofactor))
    for i,j in colors:
        cofactor=A.cofactor(j,i)
        for H in z:
            columns.append(vector(H*cofactor))
    J=sp.Matrix.hstack(*columns)
    rank=J.to_DM().rank()
    expected=(n+1)+R*n+(R*(R+1)//2)*(n-1)
    assert J.rows==expected and rank==expected
    rank_cases.append({'R':R,'n':n,'target_dimension':expected,
                       'selected_parameter_directions':J.cols,'exact_rank':rank,
                       'method':'direct symbolic cofactors, coefficient truncation, exact DomainMatrix rank'})

record={'finding':'O-020','date_utc':datetime.now(timezone.utc).isoformat(),
        'model':'GPT-6 Astra Pro','effort':'not exposed','run':'GCT_KRON_20261120',
        'packing_checks':packing,'Jacobian_rank_checks':rank_cases,
        'scope':'Finite exact cofactor checks; universal dominance and all-copy theorem are proved in the text.',
        'status':'PASS'}
destination=Path(__file__).with_name('binary_transverse_jet_certificate.json')
destination.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','packing_cases':len(packing),
                  'exact_ranks':[case['exact_rank'] for case in rank_cases],
                  'certificate':str(destination)}))
