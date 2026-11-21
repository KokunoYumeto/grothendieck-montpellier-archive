#!/usr/bin/env python3
"""Exact order216 cubic f-detector and order5184 joint source; DELTA23."""
from collections import deque
from pathlib import Path
import json
from sympy.combinatorics import Permutation,PermutationGroup

def mm(a,b):return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))%3 for i in range(3) for j in range(3))
I=(1,0,0,0,1,0,0,0,1)
def mp(a,n):
 out=I
 while n:
  if n&1:out=mm(out,a)
  a=mm(a,a);n//=2
 return out
X=(2,1,0,0,2,0,0,0,1);Y=(2,0,1,2,2,0,0,0,1)
def group(gs):
 seen={I};todo=[I];c=0
 while c<len(todo):
  a=todo[c];c+=1
  for g in gs:
   b=mm(a,g)
   if b not in seen:seen.add(b);todo.append(b)
 return seen
E=group([X,Y]);assert len(E)==216
tx=mm(mm(mm(mp(X,3),Y),mp(X,3)),mp(Y,5))
assert tx==(1,0,1,0,1,0,0,0,1)
def affine_perm(a):
 return [3*((a[0]*(v//3)+a[1]*(v%3)+a[2])%3)+(a[3]*(v//3)+a[4]*(v%3)+a[5])%3 for v in range(9)]
xp,yp=affine_perm(X),affine_perm(Y)
p=[1,2,0,3];t=[1,2,3,0]
gp=PermutationGroup([Permutation(xp),Permutation(yp)])
joint=PermutationGroup([Permutation(xp+[9+j for j in p]),Permutation(yp+[9+j for j in t])])
assert gp.order()==216 and joint.order()==5184
eds=[int(g.order()) for g in gp.derived_series()];jds=[int(g.order()) for g in joint.derived_series()]
assert eds==[216,72,18,9,1] and jds==[5184,864,72,9,1]
# Verify the projection and origin shift from the already proved F9 detector.
source=json.loads(Path(__file__).with_name('affine_cubic_detector.json').read_text())
rows=[]
for row in source['gentle_f_images']:
 rho,e=row['rho'],row['a3'];f=row['f'];d=[f[0]%3,f[1]%3]
 mat=f[2:];assert all(0<=j<3 for j in mat)
 shifted=[(d[0]-(0-2*mat[1]))%3,(d[1]-(2-2*mat[3]))%3]
 assert shifted==[e,(rho+(rho+1)*e)%3]
 affine=(mat[0],mat[1],shifted[0],mat[2],mat[3],shifted[1],0,0,1)
 assert affine in E
 rows.append({'rho':rho,'a3':e,'f_matrix':affine})
out={'statement':'D23.P10','field':'F3','x':X,'y':Y,'x3_y_commutator':tx,'order_source':216,'derived_orders':eds,'order_joint_with_S4':5184,'joint_derived_orders':jds,'six_actual_gentle_residues':rows,'result':'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
