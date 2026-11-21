"""T066: literal fixed-pair induction and exported-cell verification."""
from pathlib import Path
from fractions import Fraction
from math import comb
import json
from check_fixed_order_hook import partitions,character,z,trace_data,direct_jet,actual_module,witnesses
import pair_boundary_hook_positive as P

HERE=Path(__file__).resolve().parent


def direct_pair(m,r,nu):
    if r==0:return 0
    answer=Fraction()
    for cyc in partitions(m):
        trace=0;ones=cyc.count(1);twos=cyc.count(2)
        if ones>=2:
            rest=list(cyc);rest.remove(1);rest.remove(1)
            _,exterior=trace_data(tuple(rest),r-1)
            trace+=comb(ones,2)*exterior[r-1]
        if twos:
            rest=list(cyc);rest.remove(2)
            _,exterior=trace_data(tuple(rest),r-1)
            trace+=twos*exterior[r-1]
        answer+=Fraction(character(nu,cyc)*trace,z(cyc))
    assert answer.denominator==1
    return int(answer)


def main():
    receipt={'statement':'T-066','pair_multiplicity_comparisons':0,
             'coefficient_parity_comparisons':0,'selected_point_cases':0,
             'selected_points':0,'literal_polytope_cases':0,
             'literal_polytopes':0,'original_witnesses':0,'retained_witnesses':0}
    for m in range(5,11):
        for k in range(2,6):
            for r in range(min(m-2,(m-4)*k-(m-2))+1):
                for nu in partitions(m):
                    pair=direct_pair(m,r,nu)
                    assert P.pair_multiplicity(m,r,nu)==pair
                    receipt['pair_multiplicity_comparisons']+=1
                    expected=actual_module(m,2*k-1,r,nu)-direct_jet(m,k,r,nu)+pair
                    assert P.coefficient(m,k,r,0,nu)==expected
                    assert P.coefficient(m,k,r,1,P.stable.transpose(nu))==expected
                    receipt['coefficient_parity_comparisons']+=2
                    points=P.removed_points(m,k,r,nu)
                    if points:
                        base=P.stable.module_polytope(m,2*k-1,r,nu)
                        assert len({tuple(p[v] for v in base['variables']) for p in points})==len(points)
                        assert all(P.stable.valid_witness(base,p) for p in points)
                        receipt['selected_point_cases']+=1
                        receipt['selected_points']+=len(points)
        print('pair-boundary original traces',m,'PASS',flush=True)
    for m,k in ((5,3),(5,4),(5,5),(6,3),(7,2)):
        for r in range(min(m-2,(m-4)*k-(m-2))+1):
            for nu in partitions(m):
                data=P.polytopes(m,k,r,0,nu);retained=0
                receipt['literal_polytope_cases']+=1
                receipt['literal_polytopes']+=len(data['polytopes'])
                for point in witnesses(m,2*k-1,r,nu):
                    receipt['original_witnesses']+=1
                    matches=sum(P.stable.valid_witness(cell,point) for cell in data['polytopes'])
                    assert matches==int(point not in data['removed_points'])
                    retained+=matches
                assert retained==P.coefficient(m,k,r,0,nu)
                receipt['retained_witnesses']+=retained
        print('pair-boundary literal cells',m,k,'PASS',flush=True)
    receipt['comparison']='original standard-hook cycle traces minus literal fixed-point jets plus literal cycle-stable unordered-pair induction, with no proposed LR or Pieri correction labels'
    receipt['outcome']='PASS'
    (HERE/'PAIR_BOUNDARY_HOOK_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)


if __name__=='__main__':main()
