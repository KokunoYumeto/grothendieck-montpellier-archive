"""Score-bounded extension of G019 to positive rational constant ratios.

Writes only this task directory. This is exploratory until its finite
range and coefficient minimization proof receive independent review.
All arithmetic is integer Laurent dictionaries; no supplied imports.
"""
from pathlib import Path
from math import gcd
from functools import reduce
import json,time


def plus(a,b):
    o=dict(a)
    for e,v in b.items():o[e]=o.get(e,0)+v
    return {e:v for e,v in o.items() if v}
def times(a,b):
    o={}
    for e,u in a.items():
        for f,v in b.items():o[e+f]=o.get(e+f,0)+u*v
    return {e:v for e,v in o.items() if v}
def smul(a,c):return {e:c*v for e,v in a.items() if c*v}
def div(a,c):
    if any(v%c for v in a.values()):return None
    return {e:v//c for e,v in a.items() if v}
def dominates(a,b):
    return all(a.get(e,0)>=abs(b.get(e,0)) and (a.get(e,0)-b.get(e,0))%2==0 for e in set(a)|set(b))
def pal(a):
    o={0:a[0]} if a[0] else {}
    for e,v in enumerate(a[1:],1):
        if v:o[e]=o[-e]=v
    return o
def mass(a):return sum(a.values())
def ppoly(co):
    o={};p={0:1}
    for c in co:o=plus(o,smul(p,c));p=times(p,D)
    return o

D=pal([2,1]);DT=ppoly([4,-5,1])
GT1=ppoly([0,-4,4]);GT2=ppoly([0,0,-1,1])
ST=ppoly([0,0,4,-8,4]);KT1=ppoly([-4,5]);KT2=ppoly([4,-5,2])
LT1=D;LT2=pal([2,0,1])


def optimum_lambda(ai,aj,g,W0,target,K,d):
    DW=times(D,W0);aj_reduced=aj//gcd(g,aj);mod=2*aj_reduced
    slope=14*d*aj-20*g
    out={};ranges=[]
    for e in set(DW)|set(target)|set(K):
        low=target.get(e,0)
        residue=ai*DW.get(e,0)-aj_reduced*K.get(e,0)
        if (residue-low)%2:return None
        upper=(g*ai*DW.get(e,0)-aj*K.get(e,0))//g
        first=low+(residue-low)%mod
        last=upper-(upper-residue)%mod
        if last<first:return None
        value=first if slope>=0 else last
        if value:out[e]=value
        if slope==0 and last>first:ranges.append((e,first,last,mod))
    V=div(smul(plus(smul(DW,ai),smul(out,-1)),g),aj)
    assert V is not None and dominates(out,target) and dominates(V,K)
    return out,V,slope,ranges


def main():
    start=time.monotonic();CAP=18976
    deltas=[];ws=[]
    for a in range(6):
        for b in range(12):
            d=4+4*a+2*b
            if d<=26:deltas.append((d,a,b,pal([2*b,1+2*a,1])))
    for c2 in range(0,18,2):
        for c1 in range(1,18,2):
            for c0 in range(2,37,2):
                w0=c0+2*c1+2*c2
                if w0<=36 and reduce(gcd,(c0,c1,c2))==1:
                    ws.append((w0,(c0,c1,c2),pal([c0,c1,c2])))
    tested=0;kept=[];negative_slopes=0;zero_slopes=0
    for a1 in range(2,52,2):
        for a2 in range(1,52,2):
            if a1+a2>52:continue
            for g in range(1,24,2):
                if (a1*a2)%g:continue
                for d,a,b,delta in deltas:
                    for w0,coords,W0 in ws:
                        lower=(a1*a2//g)*w0*d*d+20*w0*d*(a1+a2)+200*g*w0+800+164*d
                        if lower>CAP:continue
                        tested+=1
                        U1=div(smul(plus(smul(W0,a1),smul(D,-1)),g),a2)
                        U2=div(smul(plus(smul(W0,a2),smul(D,-1)),g),a1)
                        if U1 is None or U2 is None or not dominates(U1,D) or not dominates(U2,D):continue
                        WD=times(W0,delta);G1=smul(WD,a1);G2=smul(WD,a2)
                        S=smul(times(W0,times(delta,delta)),a1*a2//g)
                        if not dominates(G1,GT1) or not dominates(G2,GT2) or not dominates(S,ST):continue
                        r1=optimum_lambda(a1,a2,g,W0,LT1,KT1,d)
                        r2=optimum_lambda(a2,a1,g,W0,LT2,KT2,d)
                        if r1 is None or r2 is None:continue
                        L1,V1,slope1,ranges1=r1;L2,V2,slope2,ranges2=r2
                        negative_slopes+=int(min(slope1,slope2)<0)
                        zero_slopes+=int(slope1==0 or slope2==0)
                        bottom=mass(S)+20*(mass(G1)+mass(G2))+200*g*w0+20*(mass(U1)+mass(U2)+mass(V1)+mass(V2))
                        cell=d*(52+14*(mass(L1)+mass(L2)))
                        assert (bottom+cell-4424)%2==0
                        pairs=(bottom+cell-4424)//2
                        row={'a1':a1,'a2':a2,'g':g,'delta_ab':[a,b],
                             'W0_q012':coords,'Lambda1_q':L1,'Lambda2_q':L2,
                             'slope_numerators':[slope1,slope2],'zero_slope_ranges':[ranges1,ranges2],
                             'bottom_mass':bottom,'cell_mass':cell,'pairs':pairs}
                        kept.append(row)
                        if pairs<7276:print('IMPROVEMENT',json.dumps(row),flush=True)
    kept.sort(key=lambda r:(r['pairs'],r['g'],r['a1'],r['a2'],r['delta_ab'],r['W0_q012']))
    minimum=min(r['pairs'] for r in kept);minima=[r for r in kept if r['pairs']==minimum]
    result={'seconds':time.monotonic()-start,'tested_after_score_bound':tested,
            'valid_endpoint_tables':len(kept),'negative_slope_tables':negative_slopes,
            'zero_slope_tables':zero_slopes,'minimum_pairs':minimum,
            'minimizers':minima,'all_survivors':kept,
            'scope':'common monic quadratic delta,degreeW<=2,positive rational constant ratios,Lambda-domination; proof review pending'}
    Path('work/gct/dimension_rational_ratio_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('all_survivors','minimizers')},indent=2))
    print('MINIMIZERS',json.dumps(minima,indent=2))


if __name__=='__main__':main()
