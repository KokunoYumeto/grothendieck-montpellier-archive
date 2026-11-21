"""Continuation, branch and literal-witness tests of T050 evaluator."""
from pathlib import Path
from itertools import product,combinations
from math import prod,comb
import json
from two_below_all_positive import (BRANCHES,LABELS,transpose,fixed_value,
    polytope_tags,coefficient,constraints)
from two_row_positive import coefficient as old_coefficient

HERE=Path(__file__).resolve().parent


def main():
    checks=0;witnesses=0;matrices=0
    for name,(k,x0,b0,variable) in BRANCHES.items():
        samples=(0,1,59,60,61,123)
        for X in product(samples,repeat=2 if variable else 1):
            x=x0+X[0];b=b0+X[1] if variable else b0
            for mu in LABELS:
                for d in (0,1):
                    effective=transpose(mu) if (d+b+x)%2 else mu
                    expected=fixed_value(name,effective,X)
                    assert coefficient(x,b,k,d,mu)==expected,(name,X,d,mu)
                    checks+=1
    for k,x,b in [(5,1,0),(5,0,1),(6,0,0),(8,2,1)]:
        for mu in LABELS:
            assert coefficient(x,b,k,0,mu)==old_coefficient('line',x,b,k,0,mu)
            checks+=1
    for x,b,k in [(4,0,2),(2,1,2),(0,2,2),(3,0,3),(1,1,3),(0,1,4),(2,0,4)]:
        for mu in LABELS:
            tags=polytope_tags(x,b,k,0,mu);count=0
            for tag in tags:
                if tag['constant']>100:continue
                chains=[tuple(combinations(range(q),i)) for q,i in zip(tag['quotient'],tag['order'])]
                M=constraints(tag);local=0
                for y in range(tag['constant']):
                    for chosen in product(*chains):
                        z=tuple(tag['quotient'])+(y,)+tuple(v for chain in chosen for v in chain)
                        assert all(sum(a*v for a,v in zip(row,z))==rhs for row,rhs in zip(M['A_eq'],M['b_eq']))
                        assert all(sum(a*v for a,v in zip(row,z))<=rhs for row,rhs in zip(M['A_ub'],M['b_ub']))
                        local+=1;witnesses+=1
                expected=tag['constant']*prod(comb(q,i) if q>=i else 0 for q,i in zip(tag['quotient'],tag['order']))
                assert local==expected;matrices+=1;count+=local
            assert count==coefficient(x,b,k,0,mu)
    receipt=dict(statement='T-050',status='PASS',continuation_and_branch_checks=checks,
                 literal_polytope_checks=matrices,literal_witnesses=witnesses)
    (HERE/'TWO_BELOW_ALL_EVALUATOR_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
