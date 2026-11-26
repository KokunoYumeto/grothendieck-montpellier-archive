#!/usr/bin/env python3
"""Independent closed-form check of three searched rank-three candidates.
Only the foundation worker's word-reduction code is reused. The searching
worker's matrix coordinates and exhaustive-search program are not read/imported.
"""
import json
from pathlib import Path
from paper1_rank_three_crosscheck import D,add,sub,mul,power,scale,const,table,uni


def div(n,p):
    assert all(v%n==0 for v in p.values())
    return {j:v//n for j,v in p.items()}

lam2=add(sub(scale(3,power(D,2)),scale(10,D)),const(4))
lamA=add(sub(scale(4,power(D,2)),scale(15,D)),const(12))
candidates={
    'A':(mul(D,sub(D,const(3))),10,15,30,lamA,lam2),
    'B':(mul(D,sub(D,const(3))),14,7,14,D,lam2),
    'C':(mul(sub(D,const(1)),sub(D,const(2))),14,7,14,D,lam2),
}
ct=table('trace')
report={'method':'two-letter word reduction and closed scalar-character formulas; no search/matrix-coordinate code used','candidates':{}}
for name,(d,a1,a2,b,l1,l2) in candidates.items():
    # Character compatibility forces W=G1G2/S, Ui=(Gi^2-d D Gi)/S,
    # and Vi=(D Gi^2-d lambda_i Gi)/S. Cancel symbols before evaluation.
    aa=[a1,a2];ll=[l1,l2]
    p={'delta':[d,d],'lam':ll,'G':[scale(a,mul(D,d)) for a in aa],
       'S':scale(b,mul(D,power(d,2))),
       'W':div(b,scale(a1*a2,D)),
       'U':[div(b,scale(a*(a-1),D)) for a in aa],
       'V':[div(b,scale(a,sub(scale(a,power(D,2)),l))) for a,l in zip(aa,ll)]}
    dt=table(name,parameters=p)
    assert set(dt)==set(ct)
    zeros=[];pairs=0;nonuni=0
    for key,v in dt.items():
        c=ct[key]
        for j in set(c)|set(v):
            cv,dv=c.get(j,0),v.get(j,0)
            assert dv>=abs(cv) and (dv-cv)%2==0,(name,key,j,cv,dv)
            pairs+=(dv-abs(cv))//2
            if cv==0 and dv>0:zeros.append((key,j,dv))
        nonuni+=not uni(v)
    report['candidates'][name]={'nonzero_constants':len(dt),'supported_zero_weights':len(zeros),'bottom_supported_zero_weights':sum(k[2]=='Sigma' for k,j,dv in zeros),'cancelling_pairs':pairs,'nonunimodal_dimension_constants':nonuni,'coefficientwise_effectivity_and_parity':True}
expected={'A':(54,34,7656,44),'B':(38,34,8288,46),'C':(42,34,10804,0)}
for name,(zs,bs,cp,nu) in expected.items():
    r=report['candidates'][name]
    assert (r['supported_zero_weights'],r['bottom_supported_zero_weights'],r['cancelling_pairs'],r['nonunimodal_dimension_constants'])==(zs,bs,cp,nu)
p=Path(__file__).resolve().parents[1]/'checks'/'paper1_rank_three_search_candidates.json'
p.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
