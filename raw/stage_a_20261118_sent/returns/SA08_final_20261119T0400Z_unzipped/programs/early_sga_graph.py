"""Exact finite witnesses for the SGA IX12.3 incidence-target defect.

These matrices check the mathematical reconstruction; they do not alter ink.
"""
import json
from sympy import Matrix

def check(nodes,components,branches):
    # The literal Z^(h) sends each branch to the one basis vector (point,component).
    product=Matrix(len(nodes)*len(components),len(branches),lambda i,j:
                   int(i==nodes.index(branches[j][0])*len(components)+components.index(branches[j][1])))
    # Correct boundary of the bipartite incidence graph.
    incidence=Matrix(len(nodes)+len(components),len(branches),lambda i,j:
                    (-1 if i==nodes.index(branches[j][0]) else
                     1 if i==len(nodes)+components.index(branches[j][1]) else 0))
    return dict(branches=branches,literal_product_matrix=product.tolist(),
                correct_incidence_matrix=incidence.tolist(),
                literal_kernel_rank=len(branches)-product.rank(),
                correct_kernel_rank=len(branches)-incidence.rank(),
                correct_kernel_basis=[list(v) for v in incidence.nullspace()])
triangle=check(['a','b','c'],['A','B','C'],[('a','A'),('a','B'),('b','B'),('b','C'),('c','C'),('c','A')])
triplepoint=check(['s'],['A','B','C'],[('s','A'),('s','B'),('s','C')])
assert triangle['literal_kernel_rank']==0 and triangle['correct_kernel_rank']==1
assert triplepoint['correct_kernel_rank']==0
out={'nodal_triangle':triangle,'one_triple_point':triplepoint,
     'triple_point_pairwise_complete_graph_H1_rank':3-3+1,
     'scope':'The complete-graph triple-point discrepancy concerns dropping the preceding at-most-two-branches hypothesis; no unconditional source theorem is refuted.'}
print(json.dumps(out,indent=2,default=str))
