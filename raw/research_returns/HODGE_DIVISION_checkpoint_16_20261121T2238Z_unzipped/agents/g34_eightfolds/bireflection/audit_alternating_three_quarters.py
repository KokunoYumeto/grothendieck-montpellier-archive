#!/usr/bin/env python3
"""Independent exact arithmetic for HD-ALT04; no author program imported."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, time
import sympy as s

started = time.monotonic()
def partitions(n, cap=None):
    if not n:
        yield ()
        return
    for first in range(min(n, n if cap is None else cap), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,)+rest

n,t=s.symbols('n t')
p=9*n*n-109*n+118
assert p.subs(n,15)==508
assert s.expand(p.subs(n,n+1)-p)==18*n-100
assert s.simplify(F(9,16)-(9*(n-2)/(16*(n-1))+4/((n-2)*(n-3)))-p/(16*(n-3)*(n-2)*(n-1))) == 0
assert s.simplify(4*(t*t+n*(n-1)-3*t*t/n)/(n*(n-1)*(n-2)*(n-3))
                  -(4*t*t/(n*n*(n-1)*(n-2))+4/((n-2)*(n-3))))==0
assert s.simplify((F(3,4)*n*(F(3,2)*n-1)-3*n)/(2*n*(n-2))-(9*n-30)/(16*(n-2)))==0
assert s.simplify(n*(F(3,4)*n-1)/2-(n-F(3,4)*n)-3*n*(n-2)/8)==0
assert F(2*1,2)+10*F(7,64)-2==F(3,32)
assert F(6,1)/F(3,32)==64
assert F(15**3,27)==125
assert (n-2-F(3,4)*n).subs(n,15)>0

counts={'all_partitions':0,'eligible_partitions':0,'self_conjugate_eligible':0}
maximum_u=(F(-1000),None)
maximum_v=(F(-1000),None)
for N in range(15,31):
    for lam in partitions(N):
        counts['all_partitions']+=1
        k=max(lam[0],len(lam))
        if 4*k>3*N: continue
        counts['eligible_partitions']+=1
        conjugate=tuple(sum(r>=j for r in lam) for j in range(1,lam[0]+1))
        if conjugate==lam:
            counts['self_conjugate_eligible']+=1
            assert k<=(N+1)//2
        contents=[j-i for i,r in enumerate(lam) for j in range(r)]
        tsum=sum(contents); squares=sum(x*x for x in contents)
        assert squares<=F(k*(2*k-1)*(N-1),6)
        assert abs(tsum)<=F(N*(k-1),2)-(N-k)<=F(3*N*(N-2),8)
        assert squares>=F(tsum*tsum,N)
        u=F(3*(squares-N*(N-1)//2),N*(N-1)*(N-2))
        v=F(4*(tsum*tsum+N*(N-1)-3*squares),N*(N-1)*(N-2)*(N-3))
        assert u<=F(9*N-30,16*(N-2))<F(9,16)
        assert v<=F(9*(N-2),16*(N-1))+F(4,(N-2)*(N-3))<F(9,16)
        assert min((1-u)/3,(1-v)/4)>F(7,64)
        if u>maximum_u[0]: maximum_u=(u,lam)
        if v>maximum_v[0]: maximum_v=(v,lam)

proof=Path(__file__).resolve().parents[3]/'research/ordinary_alternating_three_quarters.tex'
out={'status':'PASS','reviewed_proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'scope':'independent symbolic identities and exhaustive partitions n=15..30; universal proof audited separately',
     'author_code_imported':False,'n_range':[15,30],**counts,
     'maximum_observed_u':{'value':str(maximum_u[0]),'shape':maximum_u[1]},
     'maximum_observed_v':{'value':str(maximum_v[0]),'shape':maximum_v[1]},
     'source_degree_upper_bound':64,'factor_degree_lower_bound':125,
     'elapsed_seconds':round(time.monotonic()-started,6)}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
