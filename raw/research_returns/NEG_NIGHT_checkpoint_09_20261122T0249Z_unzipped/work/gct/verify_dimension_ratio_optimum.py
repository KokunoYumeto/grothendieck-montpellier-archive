"""Independent exhaustive certificate for a stated dimension-ring subclass.

All arithmetic is integer Laurent dictionaries. No supplied search or
dimension-table code is imported. The finite range is derived from the
7276 incumbent and positivity; see NN-G019 (when written).
"""
from pathlib import Path
import json

def plus(a,b):
    out=dict(a)
    for e,v in b.items():out[e]=out.get(e,0)+v
    return {e:v for e,v in out.items() if v}
def times(a,b):
    out={}
    for e,u in a.items():
        for f,v in b.items():out[e+f]=out.get(e+f,0)+u*v
    return {e:v for e,v in out.items() if v}
def smul(a,c):return {e:c*v for e,v in a.items() if c*v}
def divide_integer(a,c):
    if any(v%c for v in a.values()):return None
    return {e:v//c for e,v in a.items() if v}
def dominates(a,b):
    return all(a.get(e,0)>=abs(b.get(e,0)) and (a.get(e,0)-b.get(e,0))%2==0 for e in set(a)|set(b))
def pal(a):
    out={0:a[0]} if a[0] else {}
    for i,v in enumerate(a[1:],1):
        if v:out[i]=v;out[-i]=v
    return out
def mass(a):return sum(a.values())
def ppoly(a):
    out={};power={0:1}
    for v in a:
        out=plus(out,smul(power,v));power=times(power,D)
    return out
def minimum_lambda(ki,kj,W,target,K):
    upper=plus(smul(times(D,W),ki),smul(K,-kj))
    es=set(upper)|set(target)
    out={}
    for e in es:
        a=target.get(e,0);b=upper.get(e,0)
        if (b-a)%2:return None
        x=a+(b-a)%(2*kj)
        if x>b:return None
        if x:out[e]=x
    V=divide_integer(plus(smul(times(D,W),ki),smul(out,-1)),kj)
    assert V is not None and dominates(out,target) and dominates(V,K)
    return out,V

D=pal([2,1]); DT=ppoly([4,-5,1])
GT1=ppoly([0,-4,4]);GT2=ppoly([0,0,-1,1])
ST=ppoly([0,0,4,-8,4]);KT1=ppoly([-4,5]);KT2=ppoly([4,-5,2])
LT1=D;LT2=pal([2,0,1])
CAP=18976
kept=[]; tested=0
for k1 in range(2,54,2):
 for k2 in range(1,54,2):
  for a in range(6):
   for b in range(12):
    d=4+4*a+2*b
    if d>26:continue
    delta=pal([2*b,1+2*a,1])
    assert dominates(delta,DT)
    for c2 in range(0,18,2):
     for c1 in range(1,18,2):
      for c0 in range(2,37,2):
       w=c0+2*c1+2*c2
       if w>36:continue
       lower=k1*k2*w*d*d+20*w*d*(k1+k2)+200*w+800+164*d
       if lower>CAP:continue
       tested+=1;W=pal([c0,c1,c2])
       U1=divide_integer(plus(smul(W,k1),smul(D,-1)),k2)
       U2=divide_integer(plus(smul(W,k2),smul(D,-1)),k1)
       if U1 is None or U2 is None or not dominates(U1,D) or not dominates(U2,D):continue
       G1=smul(times(W,delta),k1);G2=smul(times(W,delta),k2)
       S=smul(times(W,times(delta,delta)),k1*k2)
       if not dominates(G1,GT1) or not dominates(G2,GT2) or not dominates(S,ST):continue
       l1=minimum_lambda(k1,k2,W,LT1,KT1)
       l2=minimum_lambda(k2,k1,W,LT2,KT2)
       if l1 is None or l2 is None:continue
       La1,V1=l1;La2,V2=l2
       bottom=mass(S)+20*(mass(G1)+mass(G2))+200*w+20*(mass(U1)+mass(U2)+mass(V1)+mass(V2))
       cell=d*(52+14*(mass(La1)+mass(La2)))
       score=(bottom+cell-4424)//2
       assert (bottom+cell-4424)%2==0
       kept.append({'k1':k1,'k2':k2,'delta_parameters_ab':[a,b],'W_q_coefficients_0_1_2':[c0,c1,c2],'Lambda1_q':La1,'Lambda2_q':La2,'bottom_mass':bottom,'cell_mass':cell,'pairs':score})
kept.sort(key=lambda x:(x['pairs'],x['k1'],x['k2'],x['delta_parameters_ab'],x['W_q_coefficients_0_1_2']))
minimum=min(r['pairs'] for r in kept)
minima=[r for r in kept if r['pairs']==minimum]
assert tested==1744 and len(kept)==21 and minimum==7276 and len(minima)==2
result={'cutoff_total_mass':CAP,'tested_after_score_lower_bound':tested,'valid_minimal_lambda_tables':len(kept),'minimum_pairs':minimum,'number_of_minimizers':len(minima),'minimizers':minima,'all_surviving_tables':kept,'scope':'common monic quadratic delta; deg W<=2; positive integral k_i; Lambda_i dominates true lambda_i, all with coefficientwise parity. No global optimum assertion outside this class.'}
Path('work/gct/dimension_ratio_optimum_certificate.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ('minimizers','all_surviving_tables')},indent=2))
print('k1 k2 delta_a delta_b W_c0 W_c1 W_c2 pairs')
for r in kept: print(r['k1'],r['k2'],*r['delta_parameters_ab'],*r['W_q_coefficients_0_1_2'],r['pairs'])
