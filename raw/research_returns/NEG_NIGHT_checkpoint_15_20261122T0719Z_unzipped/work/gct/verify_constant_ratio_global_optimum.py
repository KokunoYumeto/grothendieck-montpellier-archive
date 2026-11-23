"""Complete necessary scalar relaxation for NN-G026.
All parameter bounds and endpoint choices are proved in chapter.tex.
Only masses are enumerated; no support index or polynomial degree is bounded.
"""
from math import gcd
from pathlib import Path
import json,time
CAP=13464

def content(ai,aj,g,w,di,dj):
 vals=[]
 for c in range(1,min(125,ai*w//4)+1,2):
  num=g*di*(ai*w-4*c);den=aj*dj
  if num%den==0 and num//den>=4 and (num//den)%2==0:vals.append((c,num//den))
 if not vals:return
 return vals[0] if 26*aj*dj-80*g>=0 else vals[-1]

def cell_mass(ai,aj,g,w,di,dj,target):
 den=aj*dj;mod=2*den//gcd(g,2*den);res=4*ai*w*di
 first=target+(res-target)%mod
 upper=(4*g*ai*w*di-16*den)//g
 last=upper-(upper-res)%mod
 if first>last:return
 val=first if 14*den-20*g>=0 else last
 vv=g*(4*ai*w*di-val)//den
 assert vv>=16 and vv%2==0
 return val,vv

start=time.monotonic();rows=[];pre=0
for a1 in range(2,34,2):
 for a2 in range(1,34,2):
  if a1+a2>33:continue
  for g in range(1,16,2):
   if a1*a2%g:continue
   for w in range(4,25,2):
    for d1 in range(4,51,2):
     for d2 in range(4,79,2):
      S=a1*a2//g*w*d1*d2;G1=a1*w*d1;G2=a2*w*d2
      if S<576 or G1<48 or G2<48:continue
      lower=S+20*(G1+G2)+200*g*w+1136+26*(d1+d2)
      if lower>=CAP:continue
      pre+=1
      v1=content(a1,a2,g,w,d1,d2);v2=content(a2,a1,g,w,d2,d1)
      if not v1 or not v2:continue
      z1=cell_mass(a1,a2,g,w,d1,d2,8);z2=cell_mass(a2,a1,g,w,d2,d1,16)
      if not z1 or not z2:continue
      c1,U1=v1;c2,U2=v2;A1,V1=z1;A2,V2=z2
      T=S+20*(G1+G2)+200*g*w+20*(U1+U2+V1+V2)+26*(c1*d1+c2*d2)+14*(A1+A2)
      if T<CAP:rows.append({'a1':a1,'a2':a2,'g':g,'w':w,'d1':d1,'d2':d2,'c1':c1,'c2':c2,'A1':A1,'A2':A2,'T':T,'score':(T-4424)//2})
rows.sort(key=lambda r:r['score'])
assert len(rows)==55
assert len([r for r in rows if r['w']==4])==31
assert all((r['a1'],r['g'])==(2,1) and r['a2'] in (1,3) for r in rows if r['w']>4)
expected={(1,8):{(4,12),(6,12),(6,18),(8,16)},(1,10):{(4,8),(6,8),(6,12),(4,16),(6,16)},(1,12):{(4,6),(4,8),(4,10),(6,6),(4,12),(6,12)},(1,14):{(4,8)},(1,16):{(4,8)},(3,8):{(4,4),(6,4),(6,6),(10,4)},(3,10):{(6,4)},(3,12):{(4,4),(6,4)}}
actual={}
for r in rows:
 if r['w']>4:actual.setdefault((r['a2'],r['w']),set()).add((r['d1'],r['d2']))
assert actual==expected
out={'seconds':time.monotonic()-start,'pre':pre,'rows':rows}
Path('work/gct/constant_ratio_optimum_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('seconds',out['seconds'],'pre',pre,'rows',len(rows))
print('mass_pairs',sorted({(r['d1'],r['d2']) for r in rows}))
print('nontrivial_w',len([r for r in rows if r['w']>4]))
for r in rows[:20]:print(r)
