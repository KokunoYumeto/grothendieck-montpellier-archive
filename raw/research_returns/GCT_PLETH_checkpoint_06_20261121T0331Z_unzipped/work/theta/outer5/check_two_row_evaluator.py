#!/usr/bin/env python3
"""Nontrivial continuation, branch and literal constraint checks for T044/45."""
from pathlib import Path
from itertools import product,combinations
from two_row_positive import coefficient,polytope_tags,constraints,coin_count,_trace,_line_correction,_three_correction,ROWS,SIZES
from five_point_positive import LABELS,transpose

HERE=Path(__file__).resolve().parent
counts=0;witness_count=0

def expected(ray,x,b,k,d,mu):
    nu=transpose(mu) if (d+b+x)%2 else mu
    row=ROWS[LABELS.index(nu)];c=2*k-{'quadratic':0,'below':1,'line':2,'three':3}[ray]
    corr=(_line_correction if ray=='line' else _three_correction if ray=='three' else lambda g,x,b:0)
    total=sum(size*chi*(_trace(g,x,b,k,c)+corr(g,x,b))
              for g,(size,chi) in enumerate(zip(SIZES,row)))
    assert total%120==0
    return total//120

for ray in ('quadratic','below','line','three'):
    points=list(product(range(3),repeat=3))+[(60,61,62),(121,60,63),(3,2,181)]
    if ray=='below':points += [(a,0,1) for a in (2,3,5,9,60,121)]
    if ray=='line':points=[(x,b,k+5) for x,b,k in points]
    if ray=='three':points=[(x,b,k+8) for x,b,k in points]
    for x,b,k in points:
        if ray=='below' and (k<1 or 2*b+x+k<3):continue
        if ray=='line' and 2*b+x+k<6:continue
        if ray=='three' and 2*b+x+k<9:continue
        for d in (0,1):
            for mu in LABELS:
                got=coefficient(ray,x,b,k,d,mu);want=expected(ray,x,b,k,d,mu)
                assert got==want,(ray,x,b,k,d,mu,got,want)
                counts+=1

for weights in ((2,3,4,5),(2,3,5)):
    values=[1]+[0]*359
    for w in weights:
        for i in range(w,len(values)):values[i]+=values[i-w]
    for R,value in enumerate(values):
        assert coin_count(weights,R)==value
        counts+=1

for ray,x,b,k,d,mu in [('quadratic',60,61,62,0,(5,)),('below',61,60,63,1,(3,2)),('line',60,61,66,1,(2,2,1)),
                       ('three',60,61,69,0,(3,2)),('three',60,0,69,1,(1,1,1,1,1)),
                       ('below',60,61,1,0,(3,1,1)),('below',9,0,1,1,(5,))]:
    for tag in polytope_tags(ray,x,b,k,d,mu):
        matrix=constraints(tag)
        if tag['kind']=='coins':
            weights=tag['weights'];R=tag['R']
            if R<0:continue
            for point in product(*(range(R//w+1) for w in weights)):
                if sum(w*v for w,v in zip(weights,point))!=R:continue
                assert all(sum(a*v for a,v in zip(row,point))==rhs for row,rhs in zip(matrix['A_eq'],matrix['b_eq']))
                assert all(sum(a*v for a,v in zip(row,point))<=rhs for row,rhs in zip(matrix['A_ub'],matrix['b_ub']))
                witness_count+=1
        else:
            C=tag['constant'];q=tag['quotient'];order=tag['order']
            if not C or any(v<j for v,j in zip(q,order)):continue
            choices=[tuple(combinations(range(v),j)) for v,j in zip(q,order)]
            for chains in product(*choices):
                for y in sorted({0,C-1}):
                    point=tuple(q)+(y,)+tuple(v for chain in chains for v in chain)
                    assert all(sum(a*v for a,v in zip(row,point))==rhs for row,rhs in zip(matrix['A_eq'],matrix['b_eq']))
                    assert all(sum(a*v for a,v in zip(row,point))<=rhs for row,rhs in zip(matrix['A_ub'],matrix['b_ub']))
                    witness_count+=1

message=f'PASS: {counts} positive-evaluator/character and fixed-coin comparisons; {witness_count} literal matrix witnesses.\n'
(HERE/'TWO_ROW_EVALUATOR_CHECK.txt').write_text(message);print(message,flush=True)
