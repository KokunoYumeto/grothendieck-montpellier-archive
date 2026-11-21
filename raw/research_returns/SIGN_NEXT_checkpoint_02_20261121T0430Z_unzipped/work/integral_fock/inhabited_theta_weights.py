#!/usr/bin/env python3
"""IF-11: exact data of the genuine m=2 ColIn.Ok + JetsIn constructor.

This is a source-formula arithmetic check, not an evaluation of the actual
analytic theta jets, a DivInputs witness, or a new Lean compilation.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
from collections import Counter
import json
import sympy as S

ROOT=Path(__file__).resolve().parent
k,m,t,f=8,2,15,8
uF,uL,Del,hh,b1=24,-1,1,18,1
v=[(k-2-i)*4*Del for i in range(k-1)]
u=[Q(uF)+Q(1,2)]+[Q(v[i])-Q(1,2)-Del for i in range(k-2)]+[Q(uL)+Q(1,2)]
b=[b1+2*hh*j for j in range(m)]
ee=[bb+hh for bb in b]
ranks=[k+j*(t+1) for j in range(m+1)]
lam0=[x-Q(k-1-2*i,2) for i,x in enumerate(u)]
assert all(x.denominator==1 for x in lam0)
lam0=list(map(int,lam0))
wg=[ee[j]-Q(k,2)-(j+Q(1,2))*(t+1) for j in range(m)]
assert wg==[7,27]
wg=list(map(int,wg))
lamN=[lam0+sum(([-wg[j]]*(t+1) for j in range(stage)),[]) for stage in range(3)]
lamTrue=[[x-stage*(t+1)//2 for x in row] for stage,row in enumerate(lamN)]
shifts=[row[-1] for row in lamTrue]
alpha=[[x-row[-1] for x in row] for row in lamTrue]
sharp=[wg[j]+j*(t+1)//2 for j in range(2)]
div=[wg[j]+(j+1)*(t+1)//2 for j in range(2)]
ins=[shifts[j]+sharp[j] for j in range(2)]
nu=[[x+ins[j] for x in alpha[j]] for j in range(2)]
assert [row+[0]*16 for row in nu]==alpha[1:]
assert shifts==[3,-15,-43] and ins==[10,20]

# Independent source HC parameter / nu formula, avoiding the determinant shift route.
independent=[]
for j in (1,2):
    a=ranks[j-1]; target=ranks[j]; row=[]
    for i in range(a):
        if i<k:src=u[i]
        else:
            block=(i-k)//(t+1); pos=(i-k)%(t+1)
            src=-ee[block]+Q(t-2*pos,2)
        q=src+ee[j-1]-Q(a+target-1-2*i,2)
        assert q.denominator==1
        row.append(int(q))
    independent.append(row)
assert independent==nu

def dim_factors(a):
    c=Counter()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            c.update(S.factorint(a[i]-a[j]+j-i))
            c.subtract(S.factorint(j-i))
    assert all(x>=0 for x in c.values())
    return {str(p):int(e) for p,e in sorted(c.items()) if e}

gaps=sorted(set(x-y for row in alpha for x,y in zip(row,row[1:]) if x!=y))
roots=[{'gap':d,'F2_Weyl':2,'F2_dual':d*(d-1),'divided2_Weyl':1,'divided2_dual':comb(d,2)} for d in gaps if d>=2]
flag_powers=[[row[h]-(row[h+1] if h+1<len(row) else 0) for h in range(len(row))] for row in nu]
assert flag_powers[0]==[1,3,3,3,3,3,2,10]
assert flag_powers[1]==[1,3,3,3,3,3,2,10]+[0]*15+[20]
degrees=[sum(row) for row in alpha]
ws=[sum(row) for row in lamTrue]
assert degrees==[75,155,635] and ws==[99,-205,-1085]
out={
    'kind':'exact Python/SymPy source-formula check; no Lean execution',
    'scope':'genuine ColIn.Ok + degree-restricted JetsIn family; not full SizeData2 or a nonzero period',
    'rank_data':{'k':k,'m':m,'t':t,'f':f,'ranks':ranks},
    'parameters':{'u':[str(x) for x in u],'v':v,'b':b,'e':ee},
    'lambda0':lam0,'wG':wg,'unshifted':lamN,'true_weights':lamTrue,
    'det_shifts':shifts,'polynomial_parts':alpha,'kernel_shapes':nu,
    'sSharp':sharp,'sDiv':div,'det_insertions':ins,
    'det_inserted_degrees_per_embedding':[ranks[j]*ins[j] for j in range(2)],
    'polynomial_degrees_per_embedding':degrees,
    'jet_degrees_per_embedding':[sum(row) for row in nu],
    'jet_total_degrees':[f*sum(row) for row in nu],
    'CM_exponents_per_embedding':ws,'CM_exponents_all_embeddings':[f*w for w in ws],
    'nonzero_root_gaps':gaps,'second_descendant_tests':roots,
    'highest_flag_determinant_powers':flag_powers,
    'coefficient_dimension_prime_factors':[dim_factors(row) for row in alpha],
    'compatible_ThE_common_exterior_n':39*48,
    'full_size_top_weight_obstruction':{'bT':-3,'required':'bT >= sc.bprime > 0'},
}
(ROOT/'inhabited_theta_weights.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
