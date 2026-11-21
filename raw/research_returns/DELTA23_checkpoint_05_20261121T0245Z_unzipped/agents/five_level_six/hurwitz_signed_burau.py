#!/usr/bin/env python3
"""Compare the signed-block quotient with literal FP36 Burau modulo4."""
from pathlib import Path
import json,time
import numpy as np

HERE=Path(__file__).parent
def run():
 start=time.monotonic()
 add=np.array([[(a%4+b%4)%4+4*((a//4+b//4)%4) for b in range(16)] for a in range(16)],dtype=np.uint8)
 mul=np.array([[((a%4)*(b%4)-(a//4)*(b//4))%4+4*(((a%4)*(b//4)+(a//4)*(b%4)-(a//4)*(b//4))%4) for b in range(16)] for a in range(16)],dtype=np.uint8)
 neg=np.array([(-a%4)%4+4*((-(a//4))%4) for a in range(16)],dtype=np.uint8)
 w=4;one=1;zero=0
 A=np.array([[add[one,neg[w]],w,0],[1,0,0],[0,0,1]],dtype=np.uint8)
 B=np.array([[1,0,0],[0,add[one,neg[w]],w],[0,1,0]],dtype=np.uint8)
 C=np.array([[1,0,neg[one]],[0,1,neg[one]],[0,0,neg[w]]],dtype=np.uint8)
 vec=np.array([[a,b,c] for a in range(16) for b in range(16) for c in range(16)],dtype=np.uint8)
 def encode(a):return 256*a[0].astype(np.uint16)+16*a[1].astype(np.uint16)+a[2].astype(np.uint16)
 maps=[]
 for g in [A,B,C]:
  z=add[add[mul[g[:,0,None],vec.T[0]],mul[g[:,1,None],vec.T[1]]],mul[g[:,2,None],vec.T[2]]]
  maps.append(encode(z))
 scal=[]
 for c in [1,w,int(mul[w,w])]:scal.append(encode(mul[c,vec.T]))
 def canon(m):return min(tuple(int(v) for v in s[m]) for s in scal)
 I=canon(np.array([256,16,1],dtype=np.uint16))
 ps=np.load(HERE/'hurwitz_block_correlations.npz')['signed_generators'].astype(np.uint8)
 p0=np.arange(24,dtype=np.uint8)
 queue=[p0];mats=[I];index={p0.tobytes():0};matseen={I}
 for p,m in zip(queue,mats):
  mm=np.array(m,dtype=np.uint16)
  for j,g in enumerate(ps):
   pp=g[p];mat=canon(maps[j][mm]);key=pp.tobytes()
   if key in index:
    assert mats[index[key]]==mat,('marked relation mismatch',index[key],mat,mats[index[key]])
   else:index[key]=len(queue);queue.append(pp);mats.append(mat);matseen.add(mat)
 assert len(queue)==110592 and len(matseen)==110592
 flip=np.arange(24,dtype=np.uint8)^1
 assert flip.tobytes() in index
 minusI=canon(encode(mul[neg[1],np.eye(3,dtype=np.uint8)]))
 assert mats[index[flip.tobytes()]]==minusI
 # Every scalar quotient here is exactly by <omega I>, of order3.
 out={'signed_group_order':len(queue),'Burau_mod4_quotient_by_omegaI_order':len(matseen),
      'literal_generator_marking':'A,B,C as supplied FP36.2, with omega encoded4 in Z4[omega]',
      'all_marked_relations':'PASS','global_pair_flip_maps_to_minusI':'PASS',
      'projective_quotient_order':len(queue)//2,
      'result':'PASS','elapsed_seconds':time.monotonic()-start,
      'scope':'Exact marked isomorphism, not only equal group orders. No actual GT lift inferred.'}
 (HERE/'hurwitz_signed_burau.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':run()
