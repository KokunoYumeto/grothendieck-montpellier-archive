"""Extend the bounded search to signed auxiliary Lambda parameters.

Only delta*Lambda is an actual within-cell structure constant. Requiring
Lambda itself to dominate its trace counterpart was an extra restriction.
This search retains common monic quadratic delta, degreeW<=2 and positive
rational constant Gi/(W*delta), and removes that extra restriction.
It reuses only our own integer Laurent arithmetic, not source scripts.
"""
from pathlib import Path
from math import gcd
from functools import reduce
import json,time
import search_dimension_rational_ratios as R


def first_residue(low,residue,mod):return low+(residue-low)%mod
def last_residue(upper,residue,mod):return upper-(upper-residue)%mod
def ceil_div(a,b):return -((-a)//b)


def optimum_lambda(ai,aj,g,W0,delta,target,K):
    DW=R.times(R.D,W0);ar=aj//gcd(g,aj);mod=2*ar
    residue=[ai*DW.get(e,0)-ar*K.get(e,0) for e in range(4)]
    upper=[(g*ai*DW.get(e,0)-aj*K.get(e,0))//g for e in range(4)]
    c=delta[1];b=delta.get(0,0);d=R.mass(delta)
    slope=14*d*aj-20*g
    options=[];best=None;tested=0
    for l3 in range(first_residue(0,residue[3],mod),upper[3]+1,mod):
        low2=target.get(4,0)-c*l3
        for l2 in range(first_residue(low2,residue[2],mod),upper[2]+1,mod):
            low1=target.get(3,0)-c*l2-b*l3
            for l1 in range(first_residue(low1,residue[1],mod),upper[1]+1,mod):
                low0=max(target.get(2,0)-c*l1-b*l2-c*l3,
                         ceil_div(target.get(1,0)-(b+1)*l1-c*l2-l3,c))
                if b:low0=max(low0,ceil_div(target.get(0,0)-2*c*l1-2*l2,b))
                elif 2*c*l1+2*l2<target.get(0,0):continue
                lo=first_residue(low0,residue[0],mod)
                hi=last_residue(upper[0],residue[0],mod)
                if hi<lo:continue
                tested+=1
                l0=lo if slope>=0 else hi
                vals=(l0,l1,l2,l3);mass=l0+2*(l1+l2+l3)
                cost=slope*mass
                if best is not None and cost>best:continue
                la=R.pal(vals)
                V=R.div(R.smul(R.plus(R.smul(DW,ai),R.smul(la,-1)),g),aj)
                assert V is not None
                assert R.dominates(R.times(delta,la),target)
                assert R.dominates(V,K)
                option={'Lambda_q0123':vals,'Lambda_q':la,'V_q':V,'mass':mass,
                        'slope_numerator':slope,'zero_slope_l0_interval':(lo,hi,mod) if slope==0 else None}
                if best is None or cost<best:best=cost;options=[]
                options.append(option)
    return options,tested


def main():
    start=time.monotonic();CAP=18976
    target1={e:abs(v) for e,v in R.times(R.DT,R.LT1).items()}
    target2={e:abs(v) for e,v in R.times(R.DT,R.LT2).items()}
    assert R.mass(target1)==8 and R.mass(target2)==16
    deltas=[];ws=[]
    for a in range(7):
        for b in range(14):
            d=4+4*a+2*b
            if d<=30:deltas.append((d,a,b,R.pal([2*b,1+2*a,1])))
    for c2 in range(0,18,2):
        for c1 in range(1,18,2):
            for c0 in range(2,37,2):
                w0=c0+2*c1+2*c2
                if w0<=36 and reduce(gcd,(c0,c1,c2))==1:
                    ws.append((w0,(c0,c1,c2),R.pal([c0,c1,c2])))
    bounded=0;structural=0;lambda_tested=0;kept=[];best=7276
    for a1 in range(2,52,2):
        for a2 in range(1,52,2):
            if a1+a2>52:continue
            for g in range(1,24,2):
                if (a1*a2)%g:continue
                for d,a,b,delta in deltas:
                    for w0,coords,W0 in ws:
                        lower=(a1*a2//g)*w0*d*d+20*w0*d*(a1+a2)+200*g*w0+800+52*d+336
                        if lower>CAP:continue
                        bounded+=1
                        U1=R.div(R.smul(R.plus(R.smul(W0,a1),R.smul(R.D,-1)),g),a2)
                        U2=R.div(R.smul(R.plus(R.smul(W0,a2),R.smul(R.D,-1)),g),a1)
                        if U1 is None or U2 is None or not R.dominates(U1,R.D) or not R.dominates(U2,R.D):continue
                        WD=R.times(W0,delta);G1=R.smul(WD,a1);G2=R.smul(WD,a2)
                        S=R.smul(R.times(W0,R.times(delta,delta)),a1*a2//g)
                        if not R.dominates(G1,R.GT1) or not R.dominates(G2,R.GT2) or not R.dominates(S,R.ST):continue
                        structural+=1
                        o1,c1=optimum_lambda(a1,a2,g,W0,delta,target1,R.KT1)
                        o2,c2=optimum_lambda(a2,a1,g,W0,delta,target2,R.KT2)
                        lambda_tested+=c1+c2
                        if not o1 or not o2:continue
                        l1=o1[0];l2=o2[0]
                        bottom=R.mass(S)+20*(R.mass(G1)+R.mass(G2))+200*g*w0+20*(R.mass(U1)+R.mass(U2)+R.mass(l1['V_q'])+R.mass(l2['V_q']))
                        cell=d*(52+14*(l1['mass']+l2['mass']))
                        assert (bottom+cell-4424)%2==0
                        pairs=(bottom+cell-4424)//2
                        row={'a1':a1,'a2':a2,'g':g,'delta_ab':[a,b],'W0_q012':coords,
                             'Lambda1_options':o1,'Lambda2_options':o2,
                             'bottom_mass':bottom,'cell_mass':cell,'pairs':pairs}
                        kept.append(row)
                        if pairs<best:
                            best=pairs;print('NEW_BEST',json.dumps(row),flush=True)
    kept.sort(key=lambda r:(r['pairs'],r['g'],r['a1'],r['a2'],r['delta_ab'],r['W0_q012']))
    minimum=min(r['pairs'] for r in kept);minima=[r for r in kept if r['pairs']==minimum]
    result={'seconds':time.monotonic()-start,'tested_after_score_bound':bounded,
            'structural_tuples':structural,'lambda_endpoint_combinations_checked':lambda_tested,
            'valid_optimum_lambda_tuples':len(kept),'minimum_pairs':minimum,
            'minimizers':minima,'all_survivors':kept,
            'scope':'common monic quadratic delta,degreeW<=2,positive rational constant ratios; only actual constants must be effective, arbitrary signed Lambda allowed; full range proof review pending'}
    Path('work/gct/dimension_signed_lambda_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('all_survivors','minimizers')},indent=2))
    print('MINIMIZERS',json.dumps(minima,indent=2))


if __name__=='__main__':main()
