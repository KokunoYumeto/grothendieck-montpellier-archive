#!/usr/bin/env python3
"""D23.P16: rebuild the induced quotient and its exact necessary conditions.

This is a finite certificate, not an actual gentle or GT lifting program.
"""
import json,pathlib,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from cubic_descent_iterate import build
ROOT=pathlib.Path(__file__).parent
def pp(a):return Permutation(a.tolist())
def dis(*xs):
 out=[];off=0
 for x in xs:out.extend((x+off).tolist());off+=len(x)
 return np.array(out,dtype=np.int64)
def grp(*xs):return PermutationGroup([pp(a) for a in xs])
def key(a):return tuple(map(int,a))
def elements(G):return sorted([np.array(p.array_form,dtype=np.int64) for p in G.generate_schreier_sims()],key=key)
def mult(*xs):
 a=np.arange(len(xs[0]))
 for x in xs:a=a[x]
 return a
def eq(a,b):return np.array_equal(a,b)
def inv(a):return np.argsort(a)
def graph_order(A,B,A1,B1):return int(grp(dis(A,A1),dis(B,B1)).order())
def run():
 start=time.monotonic();d=build(2)
 S,R,X,Y=[d[k] for k in ['s','r','x','y']];T=mult(S,R,S);I=np.arange(24)
 B,E,F=grp(S,R),grp(R,T),grp(X,Y);M=F.derived_subgroup();ms=elements(M)
 assert [int(g.order()) for g in B.derived_series()]==[3456,576,64,1]
 assert [int(g.order()) for g in E.derived_series()]==[1728,192,64,1]
 assert [int(g.order()) for g in F.derived_series()]==[576,64,1]
 assert F.abelian_invariants()==[3,3]
 assert M.is_abelian and all(eq(a[a],I) for a in ms)
 # The pure s-frame class, using the actual image of F, not all of B.
 frameclass={key(mult(a,S,inv(a))) for a in elements(F)}
 assert len(frameclass)==24
 J=grp(dis(R,X),dis(T,R));JD=J.derived_subgroup()
 J3=grp(dis(R,X,X),dis(T,R,Y));J3D=J3.derived_subgroup()
 # Original B-pair conditions give exactly one possible value per half-bit.
 originals=[]
 for A in ms:
  if int(A[0]) not in [0,1]:continue
  s1=mult(S,A);r1=mult(inv(A),R)
  if not(eq(mult(s1,s1),I) and eq(mult(r1,r1,r1),I)):continue
  go=graph_order(S,R,s1,r1);assert go==3456
  originals.append({'b':int(A[0]),'value':A.tolist(),'graph_order':go})
 assert len(originals)==2 and sorted(v['b'] for v in originals)==[0,1]
 rows=[]
 for C in ms:
  g=mult(S,C,S,R,inv(C),inv(R))
  if key(mult(inv(g),S)) not in frameclass:continue
  f0=mult(R,inv(C),inv(R),C)
  # A.90 and normalization make this the correction to the scalar half-bit.
  bit=int(f0[0]);assert bit in [0,1]
  assert eq(mult(S,g,S),inv(g))
  z=inv(mult(R,T));A=g;BB=inv(mult(S,C,S));CC=mult(R,C,inv(R))
  assert eq(mult(CC,BB,A),I)
  assert eq(mult(CC,inv(z),BB,inv(T),A,inv(R)),I)
  assert JD.contains(pp(dis(g,C)))
  # This kernel-invariance condition is legitimate by the proof in P16.
  go=graph_order(S,R,mult(inv(g),S),R);assert go==3456
  assert int(grp(R,mult(inv(g),T,g)).order())==1728
  assert int(grp(X,mult(inv(C),R,C)).order())==1728
  bs=[]
  for original in originals:
   ff=np.array(original['value']);assert J3D.contains(pp(dis(g,C,ff)))
   bs.append(original['b'])
  rows.append({'C':C.tolist(),'g':g.tolist(),'correction':bit,
               'B_graph_order':go,'common_original_half_bits':bs})
 assert len(rows)==8
 assert [sum(v['correction']==b for v in rows) for b in [0,1]]==[4,4]
 out={'statement':'D23.P16','quotient_orders':{'B':3456,'E':1728,'F':576,'H':64},
      'pure_s_frame_class_size':24,
      'two_pair_joint_order':int(J.order()),'two_pair_joint_derived_order':int(JD.order()),
      'three_pair_joint_order':int(J3.order()),'three_pair_joint_derived_order':int(J3D.order()),
      'original_values':originals,'surviving_C_values':rows,
      'checks':'PASS','elapsed_seconds':time.monotonic()-start,
      'scope':'Necessary finite conditions only; no actual gentle or GT lift, and no assertion that the correction vanishes.'}
 (ROOT/'cubic_descent_iterate_check.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['original_values','surviving_C_values']},indent=2))
if __name__=='__main__':run()
