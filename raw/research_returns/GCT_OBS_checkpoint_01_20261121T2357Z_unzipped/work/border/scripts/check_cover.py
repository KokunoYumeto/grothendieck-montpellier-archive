#!/usr/bin/env python3
"""Independent complete determinant ideals/permanent coordinate orbit cover."""
import argparse,json,time
from itertools import combinations,permutations
from br_linear import PAIRS,RECTS
from check_koszul import ideals


def run(detfile,perfile):
 start=time.time();d=json.load(open(detfile));p=json.load(open(perfile))
 stated=[tuple(r['subset']) for r in d['records']]
 actual=ideals(7)
 assert len(stated)==len(set(stated))==25 and sorted(stated)==actual
 rectpos={v:i for i,v in enumerate(RECTS)};actions=[]
 for r in permutations(range(4)):
  for c in permutations(range(4)):
   for transpose in (False,True):
    action=[]
    for I,J in RECTS:
     a,b=tuple(sorted(r[i] for i in I)),tuple(sorted(c[j] for j in J))
     action.append(1<<rectpos[(b,a) if transpose else (a,b)])
    actions.append(action)
 assert len({tuple(a) for a in actions})==1152
 union=set()
 for record in p['records']:
  S=record['subset'];orbit={sum(action[i] for i in S) for action in actions}
  assert len(orbit)==record['orbit_size']
  assert union.isdisjoint(orbit)
  union.update(orbit)
 masks=[sum(1<<(4*r+c) for r in I for c in J) for I,J in RECTS]
 total=low=0
 for S in combinations(range(36),7):
  total+=1;support=0
  for i in S:support|=masks[i]
  if support.bit_count()<14:
   low+=1;assert sum(1<<i for i in S) in union
 assert total==8347680 and low==len(union)==1543608 and len(p['records'])==1517
 out={'status':'PASS','determinant_order_ideals':25,'permanent_subsets':total,'low_support_subsets':low,
      'permanent_orbits':1517,'symmetry_group_order':1152,'seconds':time.time()-start}
 print(json.dumps(out),flush=True);return out

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
 from pathlib import Path
 c=Path(__file__).resolve().parent.parent/'certificates'
 r=run(c/'det7_cases.json',c/'per7_cases.json')
 if args.output:Path(args.output).write_text(json.dumps(r,indent=2)+'\n')
