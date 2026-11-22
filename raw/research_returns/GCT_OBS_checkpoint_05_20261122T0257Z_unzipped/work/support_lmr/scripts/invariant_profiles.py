#!/usr/bin/env python3
"""Exact multidegree inventory for determinant-character ternary jet invariants.
Standard library only. Encoded profile digit j-2 records the number of
Sym^j generators. The computed base is larger than every possible digit.
"""
from itertools import product,permutations
from pathlib import Path
import argparse,json,time

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--tail',type=int,default=8);ap.add_argument('--maxjet',type=int);ap.add_argument('--output',type=Path)
 args=ap.parse_args();c=args.tail;maximum=args.maxjet or c;weight=3*c;base=weight//2+1
 start=time.monotonic();caps=(c+2,c+1,c)
 states=[v for v in product(*(range(x+1) for x in caps)) if sum(v)<=weight]
 index={s:i for i,s in enumerate(states)};values=[{} for _ in states];values[0][0]=1
 generators=[v for v in states if 2<=sum(v)<=maximum]
 for g in generators:
  inc=base**(sum(g)-2)
  for dest in states:
   if all(x>=y for x,y in zip(dest,g)):
    source=tuple(x-y for x,y in zip(dest,g));src=values[index[source]];dst=values[index[dest]]
    for profile,value in src.items():dst[profile+inc]=dst.get(profile+inc,0)+value
 dimensions={};rho=(2,1,0)
 for p in permutations(rho):
  target=tuple(c+rho[i]-p[i] for i in range(3))
  sign=(-1)**sum(p[i]<p[j] for i in range(3) for j in range(i+1,3))
  for profile,value in values[index[target]].items():dimensions[profile]=dimensions.get(profile,0)+sign*value
 assert all(x>=0 for x in dimensions.values())
 if (c,maximum)==(8,8):assert sum(dimensions.values())==804
 if (c,maximum)==(9,9):assert sum(dimensions.values())==2386
 out=[]
 for code,dim in sorted(dimensions.items()):
  if not dim:continue
  profile=tuple(code//base**i%base for i in range(maximum-1))
  assert sum((i+2)*v for i,v in enumerate(profile))==weight
  weightdim=values[index[(c,c,c)]][code]
  out.append(dict(profile=profile,invariant_dimension=dim,weight_space_dimension=weightdim))
 result=dict(profiles=out,total_dimension=sum(dimensions.values()),tail=c,maxjet=maximum,nonzero_profiles=len(out),maximum_block_dimension=max(v['invariant_dimension'] for v in out),maximum_weight_space_dimension=max(v['weight_space_dimension'] for v in out),elapsed_seconds=time.monotonic()-start)
 default_name='invariant_profiles.json' if (c,maximum)==(8,8) else 'invariant_profiles_c%d_j%d.json'%(c,maximum)
 output=args.output or Path('work/support_lmr/results')/default_name
 output.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items() if k!='profiles'}),flush=True)
 for row in sorted(out,key=lambda x:x['invariant_dimension'],reverse=True)[:15]:print(row,flush=True)

if __name__=='__main__':main()
