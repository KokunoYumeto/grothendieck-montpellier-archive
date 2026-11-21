#!/usr/bin/env python3
"""Recheck both marked image-group quotients in the degree1344 action."""
import json,pathlib,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=pathlib.Path(__file__).parent
def pg(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def joint(gs,ts):
 n=len(gs[0]);return PermutationGroup([Permutation(g.tolist()+[n+v for v in t])for g,t in zip(gs,ts)])
def run():
 st=time.monotonic();d=np.load(ROOT/'hurwitz_cubic216_four_13.npz');A,B,C=d['generators'];mul=lambda a,b:a[b]
 small=d['detector_generators'];pure=[p[p]for p in small]
 target=json.loads((ROOT/'cubic_detector_216.json').read_text())
 def aff(a):return [3*((a[0]*(v//3)+a[1]*(v%3)+a[2])%3)+(a[3]*(v//3)+a[4]*(v%3)+a[5])%3 for v in range(9)]
 ts=[aff(target[k])for k in ['x','y']]
 assert pg(pure).order()==joint(pure,ts).order()==1944
 mapping={int(v):int(w)for v,w in zip(d['detector_subset'],d['detector_map'])}
 assert len(mapping)==432 and set(mapping.values())==set(range(36))
 for g,t in zip([A,B],small):assert all(int(g[v])in mapping and mapping[int(g[v])]==int(t[w])for v,w in mapping.items())
 x=mul(C,C);s=mul(mul(A,B),A);y=mul(s,s);seen=set();orbs=[]
 for a in range(len(x)):
  if a in seen:continue
  todo=[a];seen.add(a)
  for v in todo:
   for g in [x,y]:
    w=int(g[v])
    if w not in seen:seen.add(w);todo.append(w)
  orbs.append(todo)
 orbit=sorted(orbs,key=len)[9];assert len(orbit)==72;ix={v:j for j,v in enumerate(orbit)}
 mixed=[np.array([ix[int(g[v])]for v in orbit])for g in [x,y]]
 assert np.array_equal(np.array(mixed),np.load(ROOT/'hurwitz_cubic216_four_13_pair34_component9.npz')['generators'])
 assert pg(mixed).order()==joint(mixed,[[1,2,0,3],[1,2,3,0]]).order()==995328
 out={'statement':'D23.P17','B4_orbit_degree':1344,'first_subset_degree':432,
      'first_set_quotient_degree':36,'first_pure_image_order':1944,
      'first_joint_marked216_order':1944,'mixed_component_degree':72,
      'mixed_image_order':995328,'mixed_joint_markedS4_order':995328,
      'first_forgetting_equivariance':'PASS','result':'PASS',
      'scope':'Both final targets are quotients of permutation image groups. No set quotient 36→9 or72→4 is asserted.',
      'elapsed_seconds':time.monotonic()-st}
 (ROOT/'hurwitz_cubic216_markings.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
