"""Construct the exact degree-15 divisor identity by Taylor linear algebra.
Adapts theta13_direct.py; the separate SymPy verifier uses no producer code.
"""
from pathlib import Path
import json

DEG=3
MOD=0b1011
Q=1<<DEG
def mul(a,b):
 z=0
 while b:
  if b&1:z^=a
  b>>=1;a<<=1
  if a&Q:a^=MOD
 return z
def powf(a,n):
 z=1
 while n:
  if n&1:z=mul(z,a)
  a=mul(a,a);n>>=1
 return z
def inv(a):
 assert a
 z=powf(a,Q-2);assert mul(a,z)==1
 return z
def trim(a):
 while a and a[-1]==0:a.pop()
 return a
def add(a,b):return trim([(a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def pmul(a,b):
 c=[0]*max(0,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]^=mul(x,y)
 return trim(c)
def peval(a,x):
 z=0
 for c in reversed(a):z=mul(z,x)^c
 return z
def translate(a,r):
 z=[]
 for c in reversed(a):z=add(pmul(z,[r,1]),[c])
 return z
def ppow(a,n):
 z=[1]
 for _ in range(n):z=pmul(z,a)
 return z
def nullvector(a):
 a=[r[:] for r in a];width=len(a[0]);piv=[];j=0
 for c in range(width):
  rr=next((i for i in range(j,len(a)) if a[i][c]),None)
  if rr is None:continue
  a[j],a[rr]=a[rr],a[j];v=inv(a[j][c]);a[j]=[mul(v,x) for x in a[j]]
  for i in range(len(a)):
   if i!=j and a[i][c]:
    v=a[i][c];a[i]=[x^mul(v,y) for x,y in zip(a[i],a[j])]
  piv.append(c);j+=1
 free=[i for i in range(width) if i not in piv]
 if not free:return None
 z=[0]*width;z[free[-1]]=1
 for rr,c in enumerate(piv):z[c]=a[rr][free[-1]]
 return z
f=[0,1,0,1,1,1];h=[0,0,1]
def torsion_function(r,s,n):
 ka=n//2;kb=(n-5)//2
 if kb<0:return None
 ft=translate(f,r);ys=[s]
 for i in range(1,n):
  v=ft[i] if i<len(ft) else 0
  if i%2==0:v^=mul(ys[i//2],ys[i//2])
  if i>=2:v^=ys[i-2]
  ys.append(mul(v,inv(mul(r,r))))
 matrix=[[ys[i-j] if i>=j else 0 for j in range(kb+1)] for i in range(ka+1,n)]
 bt=nullvector(matrix)
 if bt is None:return None
 at=[]
 for i in range(ka+1):
  v=0
  for j in range(min(i,kb)+1):v^=mul(bt[j],ys[i-j])
  at.append(v)
 a,b=translate(at,r),translate(bt,r)
 norm=add(add(pmul(a,a),pmul(h,pmul(a,b))),pmul(f,pmul(b,b)))
 if not norm:raise AssertionError('zero norm for nonzero function')
 scalar=norm[-1]
 assert norm==[mul(scalar,c) for c in ppow([r,1],n)]
 assert peval(a,r)^mul(peval(b,r),s)==0
 assert peval(a,r)^mul(peval(b,r),s^mul(r,r))
 return dict(n=n,A=a,B=b,norm_scalar=scalar)

if __name__=='__main__':
 f=[0,1,0,3,0,1]
 r,s=4,2
 assert mul(s,s)^mul(mul(r,r),s)==peval(f,r)
 certificate=torsion_function(r,s,15)
 assert certificate and torsion_function(r,s,5) is None
 result=dict(field='F2[z]/(z^3+z+1)',encoding='binary coefficients in z',
             curve='Y^2+X^2Y=X^5+(z+1)X^3+X',point=[r,s],certificate=certificate,
             exact_order15='Divisor identity; nonzero class; RR excludes3; norm X coefficient excludes5.')
 Path(__file__).with_name('theta15_constructed.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
