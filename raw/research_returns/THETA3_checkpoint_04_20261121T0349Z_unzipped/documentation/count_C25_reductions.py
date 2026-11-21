"""Exact vectorized finite-field counts; every arithmetic operation modulo 41."""
import numpy as np
from pathlib import Path
import json,time,sys
import sympy as sp
p=int(sys.argv[1]) if len(sys.argv)>1 else 41
d=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
assert p%4==1
leg=np.array([0]+[1 if pow(x,(p-1)//2,p)==1 else -1 for x in range(1,p)],dtype=np.int64)
cub=next(c for c in range(1,p) if all((x**3-x-c)%p for x in range(p)))
def character_sum(coeff,r,chunk=90000):
 total=0
 for start in range(0,p**r,chunk):
  code=np.arange(start,min(start+chunk,p**r),dtype=np.int64)
  xs=[]
  for _ in range(r):xs.append(code%p);code=code//p
  fs=[np.zeros_like(xs[0]) for _ in range(r)];fs[0]+=coeff[-1]
  for value in reversed(coeff[:-1]):
   if r==1:fs=[(fs[0]*xs[0]+value)%p]
   elif r==2:
    a,b=fs;x,y=xs
    fs=[(a*x+d*b*y+value)%p,(a*y+b*x)%p]
   elif r==3:
    a,b,c=fs;x,y,z=xs
    v3=b*z+c*y;v4=c*z
    fs=[(a*x+cub*v3+value)%p,(a*y+b*x+v3+cub*v4)%p,(a*z+b*y+c*x+v4)%p]
   else:
    a,b,c,e=fs;x,y,z,w=xs
    fs=[(a*x+d*(b*w+c*z+e*y)+value)%p,(a*y+b*x+d*(c*w+e*z))%p,(a*z+b*y+c*x+d*e*w)%p,(a*w+b*z+c*y+e*x)%p]
  if r==1:norm=fs[0]
  elif r==2:
   a,b=fs;norm=(a*a-d*b*b)%p
  elif r==3:
   a,b,c=fs
   norm=(a*((a+c)**2-b*(b+cub*c))-cub*c*(b*(a+c)-c*(b+cub*c))+cub*b*(b*b-c*(a+c)))%p
  else:
   a,b,c,e=fs
   u=(a*a+d*c*c-2*d*b*e)%p;v=(2*a*c-b*b-d*e*e)%p
   norm=(u*u-d*v*v)%p
  total+=int(leg[norm].sum())
 return total
curves=json.loads(Path(f'work/C25_candidates_{p}.json').read_text())['curves']
T=sp.symbols('T')
results=[]
for idx,curve in enumerate(curves):
 if len(sys.argv)>2 and idx!=int(sys.argv[2]):continue
 if p!=41 and not curve.get('split_T',False):continue
 began=time.time();coef=curve['poly']
 if any(x['poly']==coef for x in results):continue
 counts=[]
 for r in [1,2,3,4]:
  n=p**r+2+character_sum(coef,r);counts.append(n)
  print('curve',idx,'r',r,'count',n,'seconds',round(time.time()-began,2),flush=True)
 s=[None]+[p**r+1-counts[r-1] for r in range(1,5)]
 a=[1]
 for k in range(1,5):
  num=-sum(a[k-j]*s[j] for j in range(1,k+1));assert num%k==0;a.append(num//k)
 aa=a+[p*a[3],p*p*a[2],p**3*a[1],p**4]
 poly=sp.Poly(sum(aa[j]*T**(8-j) for j in range(9)),T)
 fac=sp.factor_list(poly)[1]
 record=dict(curve,index=idx,counts=counts,frob=aa,irreducible=len(fac)==1 and fac[0][0].degree()==8,ordinary=a[4]%p!=0)
 results.append(record)
 Path(f"work/C25_counts_{p}"+(f"_{sys.argv[2]}" if len(sys.argv)>2 else '')+'.json').write_text(json.dumps(results,indent=2))
 print('RESULT',record,flush=True)
 if record['irreducible'] and record['ordinary']:break
