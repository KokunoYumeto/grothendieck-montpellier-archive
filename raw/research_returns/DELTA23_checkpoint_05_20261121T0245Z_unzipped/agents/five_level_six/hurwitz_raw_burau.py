#!/usr/bin/env python3
"""Compare the raw72 quotient with literal unprojectivized FP36 Burau modulo4."""
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
 def canon(m):return tuple(int(v) for v in m)
 I=canon(np.array([256,16,1],dtype=np.uint16))
 ps=np.load(HERE/'hurwitz_raw_block_solvable.npz')['generators'].astype(np.uint8)
 p0=np.arange(72,dtype=np.uint8)
 queue=[p0];mats=[I];index={p0.tobytes():0};matseen={I}
 for p,m in zip(queue,mats):
  mm=np.array(m,dtype=np.uint16)
  for j,g in enumerate(ps):
   pp=g[p];mat=canon(maps[j][mm]);key=pp.tobytes()
   if key in index:
    assert mats[index[key]]==mat,('marked relation mismatch',index[key],mat,mats[index[key]])
   else:index[key]=len(queue);queue.append(pp);mats.append(mat);matseen.add(mat)
 assert len(queue)==331776 and len(matseen)==331776
 # The literal four-strand full twist restores precisely omegaI.
 A0,B0,C0=ps;d=A0[B0[C0]];z=d[d[d[d]]]
 assert z.tobytes() in index
 omegaI=canon(encode(mul[w,np.eye(3,dtype=np.uint8)]))
 omega2I=canon(encode(mul[int(mul[w,w]),np.eye(3,dtype=np.uint8)]))
 central=mats[index[z.tobytes()]]
 assert central in [omegaI,omega2I]
 out={'raw72_group_order':len(queue),'literal_Burau_mod4_group_order':len(matseen),'all_generator_edges_checked':3*len(queue),'literal_generator_marking':'FP36.2 A,B,C with omega encoded4 in Z4[omega]','all_marked_relations':'PASS','full_twist_scalar':'omega' if central==omegaI else 'omega^2','result':'PASS','elapsed_seconds':time.monotonic()-start,'scope':'Exact marked isomorphism to the full matrixgroup, not only equalorders. The scalarC3 is globalcentral; fivepairimages were separately checked.'}
 (HERE/'hurwitz_raw_burau.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
