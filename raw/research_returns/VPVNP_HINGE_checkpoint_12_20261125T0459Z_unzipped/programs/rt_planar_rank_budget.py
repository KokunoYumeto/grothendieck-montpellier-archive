#!/usr/bin/env python3
"""Exact conservative planar cut-capacity relaxation for a finite cable width.

The lower cost is 2L+(H-L)sqrt(2), from Crofton plus cut submodularity.
Integer arithmetic supplies outward rational bounds on sqrt(2),log2(A).
No floating infeasibility or tensor realizability is asserted.
"""
import argparse,itertools,json,math
from pathlib import Path
from fractions import Fraction

def run(cfg):
 m=cfg['width'];D=2;q=2**m;Q=q*q
 den=cfg['log_denominator'];sd=cfg['sqrt_denominator']
 sl=Fraction(math.isqrt(2*sd*sd),sd)
 results=[]
 for A in cfg['summands']:
  z=A**den;lo=z.bit_length()-1;ll=Fraction(lo,den)
  # Exact inequality 2^lo <= A^den < 2^(lo+1).
  assert (1<<lo)<=z<(1<<(lo+1))
  upper_budget=4*m-4*ll
  profiles=[]
  for x in range(2*m+1):
   for y in range(2*m+1):
    H=max(x,y);L=min(x,y)
    if 2*L+(H-L)*sl<upper_budget:profiles.append((x,y))
  frontier=[p for p in profiles if not any(p!=r and p[0]<=r[0] and p[1]<=r[1] for r in profiles)]
  tested=0;feasible=[]
  for multiset in itertools.combinations_with_replacement(range(len(frontier)),A):
   tested+=1;pp=[frontier[i] for i in multiset]
   sums=[sum(2**p[j] for p in pp) for j in range(2)]
   mixed=sum(2**min(p) for p in pp)
   if sums[0]>=Q and sums[1]>=Q and mixed>=q:
    feasible.append({'profiles':pp,'same_cut_upper_rank_sums':sums,'mixed_slice_upper_rank_sum':mixed})
  results.append({'A':A,'log_lower_bound':str(ll),'budget_upper_bound':str(upper_budget),
   'allowed_profiles':len(profiles),'pareto_frontier':frontier,'multisets_tested':tested,
   'feasible_multisets':len(feasible),'feasible_examples':feasible[:20]})
 return {'config':cfg,'sqrt2_lower_bound':str(sl),'results':results,
  'scope':'Exact conservative necessary rank/cut relaxation only; feasible cases do not assert a tensor identity or network.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');a=ap.parse_args()
 cfg=json.loads(Path(a.input).read_text());out=run(cfg)
 Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({r['A']:{'frontier':r['pareto_frontier'],'tested':r['multisets_tested'],'feasible':r['feasible_multisets']} for r in out['results']}))
