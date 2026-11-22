#!/usr/bin/env python3
"""Independently enumerate all torus quotient supports for 20 BR_PENCIL cases.
No input certificates or original checker imports. Uses only Python stdlib.
For each extension, both wedge kernels must have dimension >= r=13.
Run: python check_twodim_extensions.py --prime 0 --output result.json
"""
import argparse,json,time
from itertools import combinations
from br_linear import setup,saturation_rank,line_minimum

CASES=[
 ('P09_A',-1,[0,1,3,6,7,9,12]),('P09_B',-1,[0,1,3,6,7,12,13]),
 ('P12_C',-1,[0,1,2,3,6,7,8]),('P12_D',-1,[0,1,2,3,4,6,12]),
 ('P14_E',-1,[0,1,2,3,6,7,9]),('P14_F',-1,[0,1,2,3,6,7,18]),
 ('P13_1',1,[0,1,2,3,4,6,12]),('P13_2',1,[0,1,2,3,6,7,8]),
 ('P13_3',1,[0,1,2,6,7,8,18]),('P13_4',1,[0,1,2,6,7,18,20]),
 ('P13_5',1,[0,1,3,6,7,9,14]),
 ('P16_1',1,[0,1,2,3,6,7,9]),('P16_2',1,[0,1,2,3,6,7,18]),
 ('P16_3',1,[0,1,3,6,7,15,21]),
 ('P19',1,[0,1,2,6,7,18,19])]


def run(name,sign,S,p):
 start=time.time();D=setup(S,sign,p);m=len(D['support']);q=13-m
 assert q in (1,2)
 dims=[len(c) for w,c in D['blocks']];N=len(dims)
 choices=[(i,) for i,d in enumerate(dims) if d>=q]
 if q==2:choices+=list(combinations(range(N),2))
 survivors=[];counts={'saturation':0,'increment':0,'conditional':0}
 limits={o:(d-1)*13 for o,d in D['factor_dims'].items()}
 for S0 in choices:
  ell=m+sum(dims[i] for i in S0)
  if any(ell*D['factor_dims'][o]-saturation_rank(D,S0,o)<13 for o in ('A','B')):
   counts['saturation']+=1
  else:survivors.append(S0)
 mins={};remaining=[]
 def inc(i,o):
  if (i,o) not in mins:mins[i,o]=line_minimum(D,i,o)
  return mins[i,o]
 for S0 in survivors:
  excluded=False
  if len(S0)==q:
   for o in ('A','B'):
    overlap=0
    if len(S0)==2:
     sets=[{w for w,cols,cond in D['maps'][o][i]} for i in S0]
     overlap=len(sets[0]&sets[1])
    if D['base_ranks'][o]+sum(inc(i,o) for i in S0)-overlap>limits[o]:
     excluded=True;break
  if excluded:counts['increment']+=1
  else:remaining.append(S0)
 final=[];conditioned={}
 for S0 in remaining:
  excluded=False
  if len(S0)==2:
   for fix,var in (S0,S0[::-1]):
    if dims[fix]!=1:continue
    extra=D['blocks'][fix][1]
    if fix not in conditioned:conditioned[fix]=setup(S,sign,p,extra)
    C=conditioned[fix]
    if any(C['base_ranks'][o]+line_minimum(C,var,o)>limits[o] for o in ('A','B')):
     excluded=True;break
  if excluded:counts['conditional']+=1
  else:final.append(S0)
 out={'case':name,'subset':S,'sign':sign,'prime':p,'support_dim':m,
      'quotient_weights':N,'quotient_choices':len(choices),'base_ranks':D['base_ranks'],
      'exclusions':counts,'survivors':final,'seconds':round(time.time()-start,3),
      'status':'PASS' if not final else 'OPEN'}
 print(json.dumps(out),flush=True)
 return out


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prime',type=int,default=0)
 ap.add_argument('--case');ap.add_argument('--output');args=ap.parse_args()
 if args.prime:assert args.prime>=2 and all(args.prime%d for d in range(2,int(args.prime**.5)+1))
 results=[run(n,s,S,args.prime) for n,s,S in CASES if args.case is None or n==args.case]
 if args.output:
  with open(args.output,'w') as f:json.dump(results,f,indent=2);f.write('\n')

if __name__=='__main__':main()
