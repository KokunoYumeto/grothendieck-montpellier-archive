"""A feasible q=1-only relaxation, not a Laurent dimension ring.

It proves that evaluating associativity, coefficientwise lower bounds and
parity at q=1 cannot alone certify the current Laurent upper bound4194.
The input absolute coefficient masses are from the already audited trace
table. No claim of a Laurent lift or of optimum in this relaxation.
"""
from pathlib import Path
from itertools import product
import json
import dimension_two_scales as T

par={'H':{1:[4],2:[4]},'delta':{1:[6],2:[6]},'Lam':{1:[4],2:[4]},
     'G':{1:[72],2:[72]},'S':[864],'W':[6]}
labels,polys=T.make_table(par)
table={key:p[0] for key,p in polys.items()}
assert all(len(p)==1 for p in polys.values())
lower={key:sum(map(abs,p)) for key,p in T.M.TRUEq.items()}
for b in labels:lower['mu',b,b]=lower[b,'mu',b]=1
for key in set(table)|set(lower):
    d,c=table.get(key,0),lower.get(key,0)
    assert d>=c and (d-c)%2==0,(key,d,c)
def multiply(X,Y):
    out={}
    for a,p in X.items():
        for b,q in Y.items():
            for k in labels:
                z=table.get((a,b,k),0)
                if z:out[k]=out.get(k,0)+p*q*z
    return {k:v for k,v in out.items() if v}
for a,b,c in product(labels,repeat=3):
    assert multiply(multiply({a:1},{b:1}),{c:1})==multiply({a:1},multiply({b:1},{c:1}))
score=sum(table.get(k,0)-lower.get(k,0) for k in set(table)|set(lower))//2
assert score==1272
out={'status':'PASS_Q1_RELAXATION_ONLY','pair_score_relaxation':score,
     'nonunit_dimension_mass':sum(table.values())-19,
     'nonunit_absolute_trace_mass':sum(lower.values())-19,
     'associativity_triples':1000,'parameters':par,
     'table':[{'inputs':[a,b],'output':c,'dimension':v} for (a,b,c),v in sorted(table.items())]}
Path(__file__).with_name('dimension_q1_relaxation_verified.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ['table','parameters']})
