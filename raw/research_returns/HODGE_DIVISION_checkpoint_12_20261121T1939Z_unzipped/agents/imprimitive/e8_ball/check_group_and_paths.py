#!/usr/bin/env python3
"""Independent exact checks for the target group and polygonal ODE paths.
No rank or truth value from the source archive is used.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,math
import numpy as np
import sympy as S
P=Path(__file__).resolve().parent
H=S.Matrix([[2,0,-1,0,0,0,0,0],[0,2,0,-1,0,0,0,0],[-1,0,2,-1,0,0,0,0],[0,-1,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,0],[0,0,0,0,-1,2,-1,0],[0,0,0,0,0,-1,2,-1],[0,0,0,0,0,0,-1,2]])
Hi=H.inv();assert H.det()==1
D=json.load(open(P/'mtuple.json'));a,b,c=[S.Matrix(x)for x in [D['a'],D['g'][0][0],D['g'][0][1]]]
ss=[]
for i in range(8):
 s=S.eye(8);s[i,:]-=H[i,:];ss.append(s)
def decompose(A):
 M=Hi*A*H;assert M.T*H*M==H
 word=[]
 while M!=S.eye(8):
  for i in range(8):
   if all(x<=0 for x in M[:,i]):M=M*ss[i];word.append(i+1);break
  else:raise AssertionError('no root descent')
  assert len(word)<=120
 return word
def orbit(seed,actions):
 vs=list(seed);keys={tuple(v)for v in vs};parents=[None]*len(vs);j=0
 while j<len(vs):
  for k,A in enumerate(actions):
   v=A*vs[j]
   if tuple(v)not in keys:keys.add(tuple(v));vs.append(v);parents.append([j,k])
  j+=1
 return vs,parents
As=[Hi*A*H for A in [a,b,c]];words=[decompose(A)for A in [a,b,c]]
roots,_=orbit([S.eye(8)[:,i]for i in range(8)],ss)
vs,parents=orbit([S.eye(8)[:,0]],As)
assert len(vs)==len(roots)==240 and {tuple(v)for v in vs}=={tuple(v)for v in roots}
x=S.Symbol('x');assert a.charpoly(x).as_expr()==S.cyclotomic_poly(20,x)
assert b*b==c*c==S.eye(8) and (S.eye(8)-b).rank()==(S.eye(8)-c).rank()==1
assert (a*b*c).inv()==S.Matrix(D['g'][0][2])
h=S.I*a**5;assert h*h==S.eye(8)
U=S.Matrix.hstack(*(S.eye(8)-h).columnspace());moving_gram=S.simplify(U.conjugate().T*Hi*U)
assert U.cols==4 and S.simplify(moving_gram.det())==16
infinity_polynomial=(x-1)**2*S.cyclotomic_poly(3,x)*S.cyclotomic_poly(12,x)
assert S.expand(infinity_polynomial.subs(x,S.I))==6
# Complete list of possible primitive eigenvalue orders in a rational8 representation.
orders=[n for n in range(1,61)if S.totient(n)<=8]
assert orders==[1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,24,30]
angles={Q(k,n)for n in orders for k in range(n)if math.gcd(k,n)==1};angles.add(Q(0))
# For n>60 phi(n)>8 follows directly from phi(n)=prod p^(a-1)(p-1):
# allowable primes are2,3,5,7; bounded powers are2^4,3^2,5,7;
# their allowable products are exactly the displayed list.
allowed=[]
for aa in range(5):
 for bb in range(3):
  for cc in range(2):
   for dd in range(2):
    n=2**aa*3**bb*5**cc*7**dd
    if S.totient(n)<=8:allowed.append(n)
assert sorted(allowed)==orders
z0=.5-1j;poles=[0.,1.,2.+1j]
def loop_path(p):
 phi=np.angle(z0-p)
 return [z0]+[p+.45*np.exp(1j*(phi+2*np.pi*k/12))for k in range(13)]+[z0]
def pair(z):return (Q(float(z.real)),Q(float(z.imag)))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def norm2(a):return sum(x*x for x in a)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def winding(vs,p):
 w=0
 for a,b in zip(vs,vs[1:]):
  aa=sub(a,p);bb=sub(b,p);cr=cross(aa,bb)
  assert not (cr==0 and aa[0]*bb[0]+aa[1]*bb[1]<=0)
  if aa[1]<=0<bb[1] and cr>0:w+=1
  elif bb[1]<=0<aa[1] and cr<0:w-=1
 return w
# A free geometric basis results after shrinking to radius1/10.
# Straight accesses from the base point to distinct poles are disjoint rays.
zbase=pair(z0)
minimum_spoke_distance2=None
for j,p in enumerate(poles):
 v=sub(pair(p),zbase)
 for k,q in enumerate(poles):
  if k==j:continue
  w=sub(pair(q),zbase);u=sum(x*y for x,y in zip(w,v))/norm2(v)
  u=max(Q(0),min(Q(1),u));dist=norm2(tuple(x-u*y for x,y in zip(w,v)))
  assert dist>Q(1,100)
  minimum_spoke_distance2=dist if minimum_spoke_distance2 is None else min(minimum_spoke_distance2,dist)
assert minimum_spoke_distance2==Q(1,25)
pathout=[];maxbits=0
for k,p in enumerate(poles):
 path=loop_path(p);exact=list(map(pair,path));assert exact[0]==exact[-1]
 v=sub(pair(p),zbase)
 for w0 in [exact[1],exact[-2]]:
  w=sub(w0,zbase)
  assert cross(w,v)**2/norm2(v)<Q(1,10**24)
 for vertex in exact[1:-1]:assert norm2(sub(vertex,pair(p)))<Q(46,100)**2
 wind=[winding(exact,pair(q))for q in poles];assert wind==[int(k==i)for i in range(3)]
 steps=[]
 for z1,z2 in zip(path[:-1],path[1:]):
  za=pair(z1);zb=pair(z2)
  while True:
   zc=complex(float(za[0]),float(za[1]));rem=complex(z2)-zc
   if abs(rem)<1e-300:
    assert za==zb
    break
   dmin=min(abs(zc-q)for q in poles)
   final=abs(rem)<=.35*dmin
   if final:h=sub(zb,za)
   else:
    hc=rem/abs(rem)*.35*dmin
    h=pair(complex(round(hc.real*2**50)/2**50,round(hc.imag*2**50)/2**50))
   assert norm2(h)<min(norm2(sub(za,pair(q)))for q in poles)/4
   steps.append([list(za),list(h)])
   za=tuple(v+t for v,t in zip(za,h))
   for v in za+h:
    assert v.denominator&(v.denominator-1)==0
    maxbits=max(maxbits,abs(v.numerator).bit_length())
   if final:assert za==zb;break
 pathout.append({'vertices':[[str(x),str(y)]for x,y in exact],'winding':wind,'step_count':len(steps)})
assert maxbits<256
out={'status':'PASS','cartan':H.tolist(),'weight_matrices':[A.tolist()for A in [a,b,c]],'simple_basis_matrices':[A.tolist()for A in As],
'identity_reduction_words':words,'root_orbit':[list(v)for v in vs],'parents':parents,'root_count':240,
'a_characteristic':'Phi20','ia5_moving_gram_determinant':16,'ia5_moving_rank':4,'infinity_det_one_minus':6,'actual_group':'W(E8)','rational8_eigenvalue_orders':orders,'path_checks':pathout,'dyadic_max_numerator_bits':maxbits,'straight_access_minimum_distance_squared':str(minimum_spoke_distance2),
'mtuple_sha256':hashlib.sha256((P/'mtuple.json').read_bytes()).hexdigest()}
(P/'group_and_path_check.json').write_text(json.dumps(out,default=int,indent=2)+'\n')
print('PASS: root orbit240; exact words; paths',[z['step_count']for z in pathout],'endpoint arithmetic bits',maxbits)
