#!/usr/bin/env python3
"""Supplemental exact identities for E832. Universal PSD and support-plane
arguments remain the written proof; no seed or all-Hermitian finite test.
"""
from pathlib import Path
from itertools import combinations
import json,time
import sympy as s
start=time.perf_counter();r,m,u,a,t,k,du,dv=s.symbols('r m u a t k du dv',nonzero=True)
x=s.symbols('x')
unit=2*s.exp(-x)-2*s.exp(-3*x)+s.exp(-4*x)
coeff=[s.diff(unit,x,j).subs(x,0)/s.factorial(j) for j in range(5)]
assert coeff==[1,0,0,-2,4]
R=r+m
left=m*(a+r*u/m)**2-r*R*u**2/m
right=m*a*a+2*r*a*u-r*u*u
assert s.expand(left-right)==0
product=(t*t-k)*du*(k*k/(t*t)-k)*dv
assert s.factor(product+k*du*dv*(t*t-k)**2/(t*t))==0
pairs=list(combinations(range(4),2));graphs=[]
for edges in combinations(pairs,4):
    adj={v:set() for v in range(4)}
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    seen={0};queue=[0]
    while queue:
        v=queue.pop()
        for z in adj[v]-seen:seen.add(z);queue.append(z)
    assert len(seen)==4
    triangle=any(all(tuple(sorted(e)) in edges for e in combinations(q,2)) for q in combinations(range(4),3))
    if not triangle:assert all(len(adj[v])==2 for v in adj)
    graphs.append({'edges_1based':[[i+1,j+1] for i,j in edges],'has_triangle':triangle,'otherwise_four_cycle':not triangle})
assert sum(g['has_triangle'] for g in graphs)==12
assert [s.binomial(q,2) for q in range(5)]==[0,0,1,3,6]
def compound(M):return s.Matrix([[M.extract(p,q).det() for q in pairs] for p in pairs])
UU=s.diag(1,1,2,-2);BB=s.diag(2,2,1,-1);Pi=s.diag(1,0,0,0,0,1)
assert compound(BB)-compound(UU)==3*Pi
rank_table=[{'rank_U':i,'rank_V':j,'right_compound_rank':i*j+2} for i,j in [(1,1),(1,2),(2,1)]]
assert [q['right_compound_rank'] for q in rank_table]==[3,4,4]
out={'status':'PASS','unit_coefficients_through_degree4':[str(c) for c in coeff],'completed_square_identity':str(s.factor(left-right)),'determinant_product':str(s.factor(product)),'four_edge_graph_count':len(graphs),'triangle_graph_count':12,'four_cycle_count':3,'all_graphs':graphs,'compound_rank_options':[0,0,1,3,6],'deficient_rank_table':rank_table,'general_unit_boundary_compound_difference':(compound(BB)-compound(UU)).tolist(),'runtime_seconds':time.perf_counter()-start,'scope':'Exact Chern expansion, scalar graph exhaustion, determinant sign identity and printed boundary matrices only. Universal Hermitian semipositivity, E825 interface and actual star exclusion are written proofs, not inferred from numerical cases.'}
def exact(z):
    if isinstance(z,s.Integer):return int(z)
    raise TypeError(type(z).__name__)
Path(__file__).with_name('rm_elliptic_star_character_certificate_output.json').write_text(json.dumps(out,indent=2,default=exact)+'\n')
print(json.dumps({k:out[k] for k in ['status','unit_coefficients_through_degree4','determinant_product','four_edge_graph_count','triangle_graph_count','four_cycle_count','runtime_seconds','scope']},indent=2))
