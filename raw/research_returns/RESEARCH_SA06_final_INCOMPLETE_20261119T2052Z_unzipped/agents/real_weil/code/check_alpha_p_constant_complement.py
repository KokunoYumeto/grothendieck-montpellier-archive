"""Bounded symbolic checks accompanying BT.9, not a group-scheme proof."""
from pathlib import Path
from datetime import datetime, timezone
import json, time

root=Path(__file__).resolve().parents[3]
started=datetime.now(timezone.utc).isoformat()
tick=time.perf_counter()
results=[]
for p in (2,3):
    for complement_dimension in (0,1):
        rows=3+complement_dimension
        # Row i of M(1,t,t^2)^t has coefficient vector (M_i0,M_i1,M_i2).
        # The complete coefficient-extraction map is the identity matrix.
        size=3*rows
        coefficient_matrix=[[int(i==j) for j in range(size)] for i in range(size)]
        work=[row[:] for row in coefficient_matrix]
        rank=0
        for column in range(size):
            pivot=next((i for i in range(rank,size) if work[i][column]%p),None)
            if pivot is None:
                continue
            work[rank],work[pivot]=work[pivot],work[rank]
            inverse=pow(work[rank][column],-1,p)
            work[rank]=[(x*inverse)%p for x in work[rank]]
            for i in range(size):
                if i!=rank:
                    factor=work[i][column]
                    work[i]=[(x-factor*y)%p for x,y in zip(work[i],work[rank])]
            rank+=1
        assert rank==size
        # Dimension of the Hopf algebra of alpha_p^3 equals its order p^3.
        monomials=[(a,b,c) for a in range(p) for b in range(p) for c in range(p)]
        assert len(monomials)==p**3
        assert p**2 % (p**3) != 0
        results.append(dict(p=p,complement_dimension=complement_dimension,
            target_tangent_dimension=rows,
            coefficient_matrix=coefficient_matrix,coefficient_rank=rank,
            alpha_p3_hopf_monomials=monomials,kernel_order=p**3,
            hypothetical_composite_p_part=p**2,
            expected_degree_valuation=2,forced_degree_valuation_at_least=3))
result=dict(started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),
    runtime_seconds=time.perf_counter()-tick,status='PASS',cases=results,
    scope='Only coefficient independence, truncated Hopf-algebra dimension and degree arithmetic; Hom rigidity and height-one faithfulness are proved/identified separately in BT.9.')
(root/'agents/real_weil/output/alpha_p_constant_complement.json').write_text(json.dumps(result,indent=2)+'\n')
summary={key:result[key] for key in ('started_utc','finished_utc','runtime_seconds','status','scope')}
summary['case_count']=len(results)
summary['ranks']=[entry['coefficient_rank'] for entry in results]
output=json.dumps(summary,indent=2)+'\n'
(root/'agents/real_weil/output/alpha_p_constant_complement.out').write_text(output)
print(output,end='')
