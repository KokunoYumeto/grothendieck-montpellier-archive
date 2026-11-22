"""Exploratory scalar relaxation for delta_i=c_i*delta0,arbitrary degrees.
This does not constitute a theorem until its scope and survivors are proved.
"""
from pathlib import Path
from math import gcd,lcm
import json,time
CAP=16288

def utest(ai,aj,g,c,weight,target):
 z=g*(ai*weight-c*target)
 return z%aj==0 and z//aj>=target and (z//aj-target)%2==0

def pmin(ai,aj,g,w,d,target):
 ar=aj//gcd(g,aj);mod=2*ar;res=4*ai*w
 low=(target+d-1)//d;first=low+(res-low)%mod
 upper=(4*g*ai*w-16*aj)//g;last=upper-(upper-res)%mod
 if last<first:return
 v=first if 14*d*aj-20*g>=0 else last
 return v,g*(4*ai*w-v)//aj

def leadpass(a1,a2,g,b1):
 ar=a1//gcd(g,a1);mod=2*ar;res=a2*b1-2*ar
 first=1+(res-1)%mod;upper=(g*a2*b1-2*a1)//g
 return first<=upper

start=time.monotonic();rows=[]
for a1 in range(2,52,2):
 for a2 in range(1,52,2):
  if a1+a2>52:continue
  for g in range(1,24,2):
   if a1*a2%g:continue
   M=lcm(2*a2//gcd(g*a1,2*a2),2*a1//gcd(g*a2,2*a1))
   for b1 in range(1,18,2):
    ca=[c for c in range(1,min(125,a1*b1)+1,2) if utest(a1,a2,g,c,b1,1)]
    cb=[c for c in range(1,min(125,a2*b1)+1,2) if utest(a2,a1,g,c,b1,1)]
    if not ca or not cb:continue
    for b0 in range(2,37,2):
     ca0=[c for c in ca if utest(a1,a2,g,c,b0,2)]
     cb0=[c for c in cb if utest(a2,a1,g,c,b0,2)]
     if not ca0 or not cb0:continue
     base=b0+2*b1
     for h in range(max(-1,(36-base)//(2*M))+1):
      w=base+2*M*h
      if (h==0 and gcd(b0,b1)>1) or (h>0 and gcd(gcd(b0,b1),M)>1):continue
      if h==0 and not leadpass(a1,a2,g,b1):continue
      for d in range(4,31,2):
       S=a1*a2//g*w*d*d;G1=a1*w*d;G2=a2*w*d
       if S<576 or G1<48 or G2<48:continue
       p1=pmin(a1,a2,g,w,d,8);p2=pmin(a2,a1,g,w,d,16)
       if not p1 or not p2:continue
       ci1=min(ca0) if 26*d*a2-80*g>=0 else max(ca0)
       ci2=min(cb0) if 26*d*a1-80*g>=0 else max(cb0)
       U1=g*(a1*w-4*ci1)//a2;U2=g*(a2*w-4*ci2)//a1
       P1,V1=p1;P2,V2=p2
       T=S+20*(G1+G2)+200*g*w+20*(U1+U2+V1+V2)+26*(ci1+ci2)*d+14*d*(P1+P2)
       if T<CAP:rows.append({'a1':a1,'a2':a2,'g':g,'cell_contents':[ci1,ci2],'d':d,'b0':b0,'b1':b1,'M':M,'h':h,'w':w,'p1':P1,'p2':P2,'T':T,'score':(T-4424)//2})
rows.sort(key=lambda r:r['score'])
Path('work/gct/proportional_cells_relaxation.json').write_text(json.dumps(rows,indent=2)+'\n')
print('rows',len(rows),'seconds',time.monotonic()-start)
for r in rows:print(json.dumps(r))
