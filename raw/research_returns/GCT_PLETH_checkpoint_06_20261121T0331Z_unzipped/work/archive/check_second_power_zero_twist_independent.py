"""G030 exact normal table, unexpanded restriction traces and literal evaluator matrices."""
from pathlib import Path
from collections import defaultdict
from math import comb
import sys,json,hashlib
HERE=Path(__file__).resolve().parent
ns={'__file__':str(HERE/'check_fat_arrangement_independent.py')}
raw=(HERE/'check_fat_arrangement_independent.py').read_text()
exec(compile(raw.split('totals={};rows=[];')[0],ns['__file__'],'exec'),ns)
arrangement_trace=ns['arrangement_trace'];character=ns['character'];z=ns['z']
sys.path.insert(0,str(HERE.parent/'root'))
import zero_twist_arrangement as direct
import second_power_zero_twist_positive as positive
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
TABLE={():{(0,0):1},(1,):{(0,0):1,(1,0):1},
 (1,1):{(0,0):1,(1,0):2,(2,0):1,(1,1):1},
 (2,):{(0,0):1,(2,0):1,(1,1):-1},
 (1,1,1):{(0,0):1,(1,0):3,(2,0):3,(1,1):3,(3,0):1,(2,1):2},
 (2,1):{(0,0):1,(1,0):1,(2,0):1,(1,1):-1,(3,0):1},
 (3,):{(0,0):1,(3,0):1,(2,1):-1}}
for cycles,expected in TABLE.items():
    expansion=defaultdict(int)
    for (p,q),value in expected.items():
        for i in range(q,p+1):expansion[(i,p+q-i)]+=value
    expansion={e:c for e,c in expansion.items() if c}
    product={(0,0):1}
    for ell in cycles:
        nxt=defaultdict(int)
        for (i,j),value in product.items():
            for di,dj in ((0,0),(ell,0),(0,ell)):nxt[i+di,j+dj]+=value
        product=dict(nxt)
    assert expansion==product
    assert dict(direct.normal_schur(cycles,2))==expected

tracecases=[]
for b in range(11):
    for x in range(13):
        if 2*b+x<10:continue
        tracecases.append((x,b))
continuation=((10,0),(8,1),(6,2),(4,3),(2,4),(0,5),(61,5),(0,65),
              (63,67),(122,124),(251,4),(251,307))
tracecases+=list(continuation)
tracecases=sorted(set(tracecases))
traces={};total=0
for x,b in tracecases:
    vals=tuple(arrangement_trace(5,2,(b+x,b),cyc) for cyc in CLASSES)
    assert vals==direct.traces(x,b,2)
    traces[x,b]=vals;total+=7
coeffchecks=matrixchecks=witnesschecks=0
for x,b in continuation:
    vals=traces[x,b]
    for d in (0,1):
        for label,mu in enumerate(LABELS):
            effective=6-label if (d+b+x)%2 else label
            numerator=sum(120//z(cyc)*character(LABELS[effective],cyc)*v for cyc,v in zip(CLASSES,vals))
            assert numerator%120==0
            expected=numerator//120
            got=positive.coefficient(x,b,d,mu)
            assert got==expected
            coeffchecks+=1
            polys=positive.polytopes(x,b,d,mu)
            assert len(polys)<=17 if b>=5 else len(polys)<=4
            lookup={tuple(p['order']):p for p in polys}
            decoded=0
            for poly in polys:
                count=2 if b>=5 else 1
                qs=[]
                for index,(row,rhs) in enumerate(poly['equalities']):
                    assert row[index]==60 and sum(abs(v) for v in row)==60
                    assert rhs%60==0 and rhs>=0
                    qs.append(rhs//60)
                term=poly['constant']
                for q,order in zip(qs,poly['order']):term*=comb(q,order)
                decoded+=term
                assert len(poly['variables'])<=8 if b>=5 else len(poly['variables'])<=5
                matrixchecks+=1
            assert decoded==got
            for witness in positive.witnesses(x,b,d,mu,limit=7):
                poly=lookup[tuple(witness['order'])];coords=witness['coordinates']
                assert len(coords)==len(poly['variables'])
                assert all(sum(a*c for a,c in zip(row,coords))==rhs for row,rhs in poly['equalities'])
                assert all(sum(a*c for a,c in zip(row,coords))<=rhs for row,rhs in poly['inequalities'])
                witnesschecks+=1
receipt=dict(statement='G030 independent rank-two and evaluator checks',status='PASS',
 normal_polynomial_identities=len(TABLE),parameter_cases=len(tracecases),class_trace_comparisons=total,
 evaluator_coefficients=coeffchecks,literal_polytope_matrices=matrixchecks,witnesses=witnesschecks,
 method='unexpanded truncated cycle monomials with two Weyl shifts and selected-cycle Euler orientation; no skew-Schur expansion used for independent traces; character rows recomputed by MN',
 maximum_x=max(x for x,b in tracecases),maximum_b=max(b for x,b in tracecases),
 note='Does not repeat the separate512400-constant reconstruction assigned to the rectangular agent.',
 trace_sha256=hashlib.sha256(json.dumps([(x,b,traces[x,b]) for x,b in tracecases],separators=(',',':')).encode()).hexdigest())
(HERE/'SECOND_POWER_ZERO_TWIST_INDEPENDENT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
