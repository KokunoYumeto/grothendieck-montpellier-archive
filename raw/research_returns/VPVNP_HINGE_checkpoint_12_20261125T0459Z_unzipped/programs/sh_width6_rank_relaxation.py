#!/usr/bin/env python3
"""Exact feasible abstract profile for the planar width-six rank bounds.

No tensor decomposition or geometric network is constructed or asserted.
The purpose is to delimit the necessary-inequality method used at m<=5.
"""
import json
import sys
from pathlib import Path
import sympy as sp

config=json.loads(Path(sys.argv[1]).read_text())
q=64;m=6;D=2;A=2
assert config=={'dimension':D,'width':m,'terms':A,'terminal_dimension':q}
singleton=[64]*4
term_ranks=[[32,4064],[4064,32]]
ceilings=[[5,12],[12,5]]
opposite=128
w=sp.Rational(199,10)
a=sp.sqrt(2)-1;b=2-sp.sqrt(2)
crofton=24*a+17*b
real_edges=[('a','d',sp.Rational(7,2)),('b','c',sp.Rational(7,2)),
            ('a','c',sp.Rational(5,2)),('b','d',sp.Rational(5,2))]
def cut_capacity(side):
    return sum(cap for u,v,cap in real_edges if (u in side)!=(v in side))
real_cuts={side:str(cut_capacity(side)) for side in ('a','b','c','d','ab','ad','ac')}
checks={}
checks['same_cut_rank_sums']=all(sum(term_ranks[j][s] for j in range(2))==q*q
                                for s in range(2))
checks['mixed_slice_rank_sums']=all(term_ranks[0][s]+term_ranks[1][t]>=q**(2-(s!=t))
                                  for s in range(2) for t in range(2))
checks['ceilings_exact']=all(2**(k-1)<r<=2**k for rs,ks in zip(term_ranks,ceilings)
                            for r,k in zip(rs,ks))
checks['frame_budgets']=all(sum(ks)<=D*(m-1)*2-1 for ks in ceilings)
checks['rank_lipschitz']=all(abs(ks[0]-ks[1])<=2*m for ks in ceilings)
checks['singleton_dimension_bounds']=all(r<=q*q for rs in term_ranks for r in rs)
checks['all_balanced_rank_products']=all(x<=y*z for rs in term_ranks
                                         for x,y,z in [(rs[0],rs[1],opposite),
                                                       (rs[1],rs[0],opposite),
                                                       (opposite,rs[0],rs[1])])
checks['individual_geometric_cut_cost']=bool(w*w>2*max(k for ks in ceilings for k in ks)**2)
checks['integer_crofton_formula']=sp.simplify(crofton-(10+7*sp.sqrt(2)))==0
# w - 10 =99/10>7 sqrt2, because9801>9800 after squaring.
checks['integer_crofton_below_cost_budget']=(99**2>2*70**2)
checks['cost_budget_below_strict_threshold']=bool(w+4<24)
checks['real_capacity_graph_cuts']=(real_cuts=={'a':'6','b':'6','c':'6','d':'6',
                                             'ab':'12','ad':'5','ac':'7'})
checks['real_capacity_graph_cost']=sp.simplify(7*sp.sqrt(2)+10-crofton)==0
assert all(checks.values()),checks
out=dict(config=config,singleton_ranks=singleton,
         adjacent_ranks_by_term=term_ranks,adjacent_ceilings_by_term=ceilings,
         other_balanced_rank_by_term=[opposite,opposite],
         cost_budget=str(w),integer_crofton_lower_bound=str(sp.simplify(crofton)),
         integer_crofton_lower_bound_decimal=float(crofton),
         real_capacity_graph_edges=[(u,v,str(c)) for u,v,c in real_edges],
         real_capacity_graph_cuts=real_cuts,
         checks=checks,
         scope='Feasible abstract necessary rank/Crofton profile only; no tensor identity, network, or shortening is asserted.')
Path(sys.argv[2]).write_text(json.dumps(out,indent=2))
print(json.dumps(out),flush=True)
