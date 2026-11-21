#!/usr/bin/env python3
"""Exact F9 affine detector for the cubic modular frame parity."""
from collections import deque
import json,pathlib
A=[[((x%3+y%3)%3)+3*((x//3+y//3)%3) for y in range(9)] for x in range(9)]
N=[(-x%3)+3*((-x//3)%3) for x in range(9)]
# negation must act on each digit, not floor(-x/3)
N=[(-(x%3)%3)+3*((-(x//3))%3) for x in range(9)]
M=[[((x%3*(y%3)-x//3*(y//3))%3)+3*((x%3*(y//3)+x//3*(y%3))%3) for y in range(9)] for x in range(9)]
D=[0]+[next(y for y in range(1,9) if M[x][y]==1) for x in range(1,9)]
def add(x,y):return A[x][y]
def sub(x,y):return A[x][N[y]]
def mul(x,y):return M[x][y]
I=(1,0,0,1)
def mm(a,b):return (add(mul(a[0],b[0]),mul(a[1],b[2])),add(mul(a[0],b[1]),mul(a[1],b[3])),add(mul(a[2],b[0]),mul(a[3],b[2])),add(mul(a[2],b[1]),mul(a[3],b[3])))
def mi(a):
 det=sub(mul(a[0],a[3]),mul(a[1],a[2])); assert det
 return tuple(mul(D[det],v) for v in (a[3],N[a[1]],N[a[2]],a[0]))
def mv(a,v):return (add(mul(a[0],v[0]),mul(a[1],v[1])),add(mul(a[2],v[0]),mul(a[3],v[1])))
def am(a,b):
 t=mv(a[2:],b[:2]);return (add(a[0],t[0]),add(a[1],t[1]))+mm(a[2:],b[2:])
def ai(a):
 b=mi(a[2:]);t=mv(b,tuple(N[v] for v in a[:2]));return t+b
ID=(0,0)+I
def ap(a,n):
 if n<0:return ap(ai(a),-n)
 out=ID
 while n:
  if n&1:out=am(out,a)
  a=am(a,a);n//=2
 return out
def gp(gs,limit=100000):
 seen={ID};todo=deque([ID])
 while todo:
  a=todo.popleft()
  for g in gs:
   b=am(a,g)
   if b not in seen:
    seen.add(b);todo.append(b)
    if len(seen)>limit:raise RuntimeError('group limit')
 return seen
S=(0,1,2,0);R=(0,2,1,2); U=(1,1,0,1);i=3
s=(0,0)+tuple(mul(i,x) for x in S);r=(1,0)+R
assert ap(s,2)==ID and ap(r,3)==ID
E=gp([s,r]);tau=am(s,r);x=ap(tau,-2);y=am(am(s,x),s);EF=gp([x,y]);H={a[2:] for a in E};HF={a[2:] for a in EF}
assert len(E)==3888 and len(EF)==1944 and len(H)==48 and len(HF)==24
C={a for a in E if am(a,r)==am(r,a)}; CF=C&EF
assert len(C)==27 and len(CF)==27
assert {a[2:] for a in C}=={ap(r,j)[2:] for j in range(3)}
# Identity input has cubic sign +1. Verify scalar -I cannot lift into C_E(r).
assert (2,0,0,2) not in {a[2:] for a in C}
# Every q3(A) centralizing R has R^k times +/-I; conjugating r records that sign
# in the coinvariant functional ell=(1,1).
for eps in [1,2]:
 for j in range(3):
  T=tuple(mul(eps,v) for v in ap(r,j)[2:])
  for t0 in range(9):
   for t1 in range(9):
    af=(t0,t1)+T
    rr=am(am(af,r),ai(af))
    assert add(rr[0],rr[1])==eps
out={'field':'F3[i], i^2=-1, encoding a+3b','s':s,'r':r,'x':x,'y':y,'order_E':len(E),'order_pure_image':len(EF),'order_linear_image':len(H),'order_pure_linear_image':len(HF),'r_centralizer_order':len(C),'r_centralizer_linear_order':len({a[2:] for a in C}),'all_frame_coinvariant_checks':2*3*81,'result':'PASS'}
print(json.dumps(out,indent=2));pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
# Exact possible f-images from the s-torsion equation and cubic coinvariant sign.
rows=[]
for rho in range(3):
 mat=(1,rho,rho,(1+rho*rho)%3)
 for eps in [1,2]:
  good=[]
  for d0 in range(9):
   for d1 in range(9):
    f=(d0,d1)+mat
    sign=sub(mul((1-rho)%3,sub(1,d0)),d1)
    if ap(am(s,f),2)==ID and sign==eps:good.append(f)
  assert len(good)==1
  rows.append({'rho':rho,'a3':0 if eps==1 else 1,'f':good[0]})
out['gentle_f_images']=rows
print(json.dumps(rows,indent=2));pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
# Modulus-four character, fixing the global signed lift used in the proof.
def mm4(a,b):return ((a[0]*b[0]+a[1]*b[2])%4,(a[0]*b[1]+a[1]*b[3])%4,(a[2]*b[0]+a[3]*b[2])%4,(a[2]*b[1]+a[3]*b[3])%4)
U4=(1,1,0,1);L4=(1,0,3,1); S4=mm4(mm4(U4,L4),U4);R4=(0,3,1,3)
vals={I:1};todo=deque([I]);minus_i=N[i]
while todo:
 a=todo.popleft()
 for g in [U4,L4]:
  b=mm4(a,g);value=mul(vals[a],minus_i)
  if b in vals:assert vals[b]==value
  else:vals[b]=value;todo.append(b)
assert len(vals)==48
assert vals[S4]==i and vals[R4]==1 and vals[(3,0,0,3)]==2
out['mod4_character_group_order']=len(vals)
out['mod4_character_values']={'U':minus_i,'L':minus_i,'S':vals[S4],'R':vals[R4],'-I':vals[(3,0,0,3)]}
print('PASS modulus-four character, all 96 Cayley edges')
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
