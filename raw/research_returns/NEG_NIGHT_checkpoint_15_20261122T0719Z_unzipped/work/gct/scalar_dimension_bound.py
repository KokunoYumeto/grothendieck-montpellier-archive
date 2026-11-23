"""Complete finite scalar relaxation used in NN-G023.

This deliberately does not bound outer support locations. The three
remaining arbitrary-location families are eliminated algebraically in
the written proof. A relaxation row is not a dimension-ring construction.
"""
from pathlib import Path
from math import gcd,lcm
import json

CAP=18552
def scalar_u(ai,aj,g,c,target):
    num=g*(ai*c-target)
    return num%aj==0 and num//aj>=target and (num//aj-target)%2==0

def optimum_mass(ai,aj,g,w,d,target):
    ar=aj//gcd(g,aj);mod=2*ar;res=4*ai*w
    low=(target+d-1)//d
    first=low+(res-low)%mod
    upper=(4*g*ai*w-16*aj)//g
    last=upper-(upper-res)%mod
    if last<first:return None
    val=first if 14*d*aj-20*g>=0 else last
    v=g*(4*ai*w-val)//aj
    assert g*(4*ai*w-val)%aj==0 and v>=16 and v%2==0
    return val,v

rows=[];seen=set()
for a1 in range(2,52,2):
 for a2 in range(1,52,2):
  if a1+a2>52:continue
  for g in range(1,24,2):
   if (a1*a2)%g:continue
   step=lcm(2*a2//gcd(g*a1,2*a2),2*a1//gcd(g*a2,2*a1))
   for c1 in range(1,18,2):
    if not scalar_u(a1,a2,g,c1,1) or not scalar_u(a2,a1,g,c1,1):continue
    for c0 in range(2,37,2):
     if not scalar_u(a1,a2,g,c0,2) or not scalar_u(a2,a1,g,c0,2):continue
     base=c0+2*c1
     for h in range(max(-1,(36-base)//(2*step))+1):
      w=base+2*step*h
      if (h==0 and gcd(c0,c1)>1) or (h>0 and gcd(gcd(c0,c1),step)>1):continue
      for a in range(7):
       for b in range(14):
        d=4+4*a+2*b
        if d>30:continue
        S=(a1*a2//g)*w*d*d;G1=a1*w*d;G2=a2*w*d
        if S<576 or G1<48 or G2<48:continue
        U1=g*(a1*w-4)//a2;U2=g*(a2*w-4)//a1
        z1=optimum_mass(a1,a2,g,w,d,8);z2=optimum_mass(a2,a1,g,w,d,16)
        if z1 is None or z2 is None:continue
        L1,V1=z1;L2,V2=z2
        T=S+20*(G1+G2)+200*g*w+20*(U1+U2+V1+V2)+d*(52+14*(L1+L2))
        if T<CAP:
         row={'a1':a1,'a2':a2,'g':g,'delta_ab':[a,b],'c0':c0,'c1':c1,
              'outer_coefficient_step':step,'outer_unit_mass':h,'w0':w,'d':d,
              'Lambda1_mass_relaxation':L1,'Lambda2_mass_relaxation':L2,
              'mass_lower_bound':T,'pairs_lower_bound':(T-4424)//2}
         rows.append(row)
rows.sort(key=lambda r:(r['pairs_lower_bound'],r['a1'],r['a2'],r['g'],r['delta_ab'],r['c0'],r['c1'],r['outer_unit_mass']))
outer=[r for r in rows if r['outer_unit_mass']]
assert len(rows)==42 and len(outer)==3
assert {(tuple(r['delta_ab']),r['c0'],r['c1'],r['outer_coefficient_step'],r['outer_unit_mass']) for r in outer} == {((0,0),6,3,4,1),((0,0),10,3,4,1),((0,1),6,3,4,1)}
assert all((r['a1'],r['a2'],r['g'])==(2,1,1) for r in outer)
Path('work/gct/scalar_dimension_relaxation.json').write_text(json.dumps(rows,indent=2)+'\n')
print('ROWS',len(rows))
for r in rows:print(json.dumps(r))
