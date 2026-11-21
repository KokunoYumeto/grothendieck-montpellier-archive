"""T051 standalone continuation and literal-matrix checks."""
from pathlib import Path
from itertools import product,combinations
from math import prod,comb
import json
from three_below_all_positive import BRANCHES,LABELS,transpose,fixed_value,polytope_tags,coefficient,constraints
from two_row_positive import coefficient as old_coefficient

HERE=Path(__file__).resolve().parent


def main():
    checks=0;matrices=0;witnesses=0
    for name,(k,x0,b0,variable) in BRANCHES.items():
        for X in product((0,1,59,60,61,123),repeat=2 if variable else 1):
            x=x0+X[0];b=b0+X[1] if variable else b0
            for mu in LABELS:
                for d in (0,1):
                    label=transpose(mu) if (d+b+x)%2 else mu
                    assert coefficient(x,b,k,d,mu)==fixed_value(name,label,X)
                    checks+=1
    for x,b,k in [(1,0,8),(0,1,8),(0,0,9),(2,2,10)]:
        for mu in LABELS:
            assert coefficient(x,b,k,0,mu)==old_coefficient('three',x,b,k,0,mu)
            checks+=1
    for name,(k,x0,b0,variable) in BRANCHES.items():
        for mu in LABELS:
            tags=polytope_tags(x0,b0,k,0,mu);total=0
            for tag in tags:
                if tag['constant']>200:continue
                M=constraints(tag);choices=[tuple(combinations(range(q),i)) for q,i in zip(tag['quotient'],tag['order'])]
                local=0
                for y in range(tag['constant']):
                    for chosen in product(*choices):
                        z=tuple(tag['quotient'])+(y,)+tuple(v for chain in chosen for v in chain)
                        assert all(sum(a*v for a,v in zip(row,z))==rhs for row,rhs in zip(M['A_eq'],M['b_eq']))
                        assert all(sum(a*v for a,v in zip(row,z))<=rhs for row,rhs in zip(M['A_ub'],M['b_ub']))
                        local+=1;witnesses+=1
                assert local==tag['constant']*prod(comb(q,i) if q>=i else 0 for q,i in zip(tag['quotient'],tag['order']))
                total+=local;matrices+=1
            assert total==coefficient(x0,b0,k,0,mu)
    receipt=dict(statement='T-051',status='PASS',continuation_and_branch_checks=checks,
                 literal_polytope_checks=matrices,literal_witnesses=witnesses)
    (HERE/'THREE_BELOW_ALL_EVALUATOR_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
