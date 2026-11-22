"""Necessary relaxation for arbitrary common-cell content and degree.
delta=c*delta0,delta0 primitive; all outer locations remain unbounded.
NN-G024 gives the complete range proof. Only necessary conditions are used;
the five surviving rows are excluded coefficientwise for all outer locations.
"""
from pathlib import Path
from math import gcd,lcm
import json,time

CAP=16288
def coeff_u(ai,aj,g,c,weight,target):
    num=g*(ai*weight-c*target)
    return num%aj==0 and num//aj>=target and (num//aj-target)%2==0
def optimum_mass(ai,aj,g,w,d,target):
    ar=aj//gcd(g,aj);mod=2*ar;res=4*ai*w
    low=(target+d-1)//d;first=low+(res-low)%mod
    upper=(4*g*ai*w-16*aj)//g;last=upper-(upper-res)%mod
    if last<first:return None
    val=first if 14*d*aj-20*g>=0 else last
    return val,g*(4*ai*w-val)//aj
def possible_second_leading(a1,a2,g,c1):
    ar=a1//gcd(g,a1);mod=2*ar;res=a2*c1-2*ar
    first=1+(res-1)%mod;upper=(g*a2*c1-2*a1)//g
    return first<=upper

def main():
    start=time.monotonic();rows=[];pre_leading=0
    for a1 in range(2,52,2):
     for a2 in range(1,52,2):
      if a1+a2>52:continue
      for g in range(1,24,2):
       if (a1*a2)%g:continue
       step=lcm(2*a2//gcd(g*a1,2*a2),2*a1//gcd(g*a2,2*a1))
       for content in range(1,74,2):
        for c1 in range(1,18,2):
         if not coeff_u(a1,a2,g,content,c1,1) or not coeff_u(a2,a1,g,content,c1,1):continue
         for c0 in range(2,37,2):
          if not coeff_u(a1,a2,g,content,c0,2) or not coeff_u(a2,a1,g,content,c0,2):continue
          base=c0+2*c1
          for h in range(max(-1,(36-base)//(2*step))+1):
           w=base+2*step*h
           if (h==0 and gcd(c0,c1)>1) or (h>0 and gcd(gcd(c0,c1),step)>1):continue
           for d in range(4,31,2):
            S=(a1*a2//g)*w*d*d;G1=a1*w*d;G2=a2*w*d
            if S<576 or G1<48 or G2<48:continue
            U1=g*(a1*w-4*content)//a2;U2=g*(a2*w-4*content)//a1
            z1=optimum_mass(a1,a2,g,w,d,8);z2=optimum_mass(a2,a1,g,w,d,16)
            if z1 is None or z2 is None:continue
            L1,V1=z1;L2,V2=z2
            T=S+20*(G1+G2)+200*g*w+20*(U1+U2+V1+V2)+52*content*d+14*d*(L1+L2)
            if T>=CAP:continue
            pre_leading+=1
            if not h and not possible_second_leading(a1,a2,g,c1):continue
            rows.append({'a1':a1,'a2':a2,'g':g,'delta_content':content,'delta0_mass':d,
                         'c0':c0,'c1':c1,'outer_step':step,'outer_units':h,'w0':w,
                         'Psi1_mass_lower':L1,'Psi2_mass_lower':L2,
                         'total_mass_lower':T,'score_lower':(T-4424)//2})
    rows.sort(key=lambda r:(r['score_lower'],r['delta_content'],r['a1'],r['a2'],r['g'],r['delta0_mass'],r['c0'],r['c1'],r['outer_units']))
    assert len(rows)==5
    assert {(r['a1'],r['a2'],r['g'],r['delta_content'],r['delta0_mass'],r['c0'],r['c1'],r['outer_units']) for r in rows} == {(6,9,3,3,4,2,1,0),(2,1,1,1,4,6,3,1),(2,1,1,1,4,6,7,0),(10,5,5,3,4,2,1,0),(6,15,3,1,4,2,1,0)}
    result={'seconds':time.monotonic()-start,'rows_before_leading_test':pre_leading,
            'rows_after_leading_test':len(rows),'rows':rows,
            'scope':'necessary conditions only;arbitrary common delta content and degree;outer positions not bounded'}
    Path('work/gct/common_cell_content_optimum_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
    for r in rows:print(json.dumps(r))

if __name__=='__main__':main()
