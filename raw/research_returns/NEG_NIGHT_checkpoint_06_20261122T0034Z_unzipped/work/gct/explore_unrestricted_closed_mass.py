"""Exploratory scalar relaxation for all associative closed tables.
Actual coefficient masses only; no constant-ratio hypothesis.
Not a theorem until its full scope and any polynomial exclusions are written.
"""
from pathlib import Path
from math import gcd,lcm
import json,time
CAP=11128

def dopt(gi,gj,w):
 vals=[]
 for d in range(4,gi//4+1,2):
  num=w*(gi-4*d)
  if num%gj==0 and num//gj>=4 and num//gj%2==0:vals.append((d,num//gj))
 if not vals:return
 return vals[0] if 26*gj-80*w>=0 else vals[-1]

def aopt(gi,gj,w,target):
 mod=lcm(2,2*gj//gcd(w,2*gj));res=4*gi
 first=target+(res-target)%mod
 upper=(4*w*gi-16*gj)//w;last=upper-(upper-res)%mod
 if first>last:return
 a=first if 14*gj-20*w>=0 else last
 vv=w*(4*gi-a)//gj
 assert a%2==0 and vv%2==0 and vv>=16
 return a,vv

start=time.monotonic();rows=[];pre=0
for w in range(6,37,2):
 for g1 in range(48,373,2):
  for g2 in range(48,421-g1,2):
   if (g1*g2)%w:continue
   s=g1*g2//w
   if s<576 or s%2:continue
   low=s+20*(g1+g2)+200*w+800+208+336
   if low>=CAP:continue
   pre+=1
   d1=dopt(g1,g2,w);d2=dopt(g2,g1,w)
   if not d1 or not d2:continue
   a1=aopt(g1,g2,w,8);a2=aopt(g2,g1,w,16)
   if not a1 or not a2:continue
   dd1,u1=d1;dd2,u2=d2;aa1,v1=a1;aa2,v2=a2
   t=s+20*(g1+g2)+200*w+20*(u1+u2+v1+v2)+26*(dd1+dd2)+14*(aa1+aa2)
   if t<CAP:rows.append({'w':w,'g1':g1,'g2':g2,'s':s,'d1':dd1,'d2':dd2,'u1':u1,'u2':u2,'a1':aa1,'a2':aa2,'v1':v1,'v2':v2,'T':t,'score':(t-4424)//2})
rows.sort(key=lambda r:r['score'])
Path('work/gct/unrestricted_closed_mass_relaxation.json').write_text(json.dumps({'seconds':time.monotonic()-start,'pre':pre,'rows':rows},indent=2)+'\n')
print('seconds',time.monotonic()-start,'coarse',pre,'rows',len(rows),'min',rows[0] if rows else None)
print('W_masses',sorted({r['w'] for r in rows}))
for r in rows[:30]:print(r)
