"""T065: independent-side endpoint traces and literal positive cells."""
from pathlib import Path
import json
from check_fixed_order_hook import partitions, direct_jet, actual_module, witnesses
import endpoint_hook_positive as P

HERE=Path(__file__).resolve().parent


def main():
    receipt={'statement':'T-065','coefficient_parity_comparisons':0,
             'removed_point_cases':0,'removed_points':0,
             'literal_polytope_cases':0,'literal_polytopes':0,
             'original_witnesses':0,'retained_witnesses':0}
    for m in range(4,10):
        for k in range(1,6):
            for r in range(min(m-2,(m-4)*k)+1):
                for nu in partitions(m):
                    wanted=direct_jet(m,k,r,nu)
                    expected=actual_module(m,2*k,r,nu)-wanted
                    assert P.coefficient(m,k,r,0,nu)==expected
                    assert P.coefficient(m,k,r,1,P.stable.transpose(nu))==expected
                    receipt['coefficient_parity_comparisons']+=2
                    if wanted:
                        points=P.fixed.base_points(m,k,2*k,r,nu)
                        base=P.stable.module_polytope(m,2*k,r,nu)
                        assert len(points)==wanted
                        assert len({tuple(p[v] for v in base['variables']) for p in points})==wanted
                        assert all(P.stable.valid_witness(base,p) for p in points)
                        receipt['removed_point_cases']+=1
                        receipt['removed_points']+=len(points)
        print('endpoint traces and points',m,'PASS',flush=True)
    for m,k in ((4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(6,2)):
        for r in range(min(m-2,(m-4)*k)+1):
            for nu in partitions(m):
                data=P.polytopes(m,k,r,0,nu);retained=0
                receipt['literal_polytope_cases']+=1
                receipt['literal_polytopes']+=len(data['polytopes'])
                for point in witnesses(m,2*k,r,nu):
                    receipt['original_witnesses']+=1
                    matches=sum(P.stable.valid_witness(cell,point) for cell in data['polytopes'])
                    assert matches==int(point not in data['removed_points'])
                    retained+=matches
                assert retained==P.coefficient(m,k,r,0,nu)
                receipt['retained_witnesses']+=retained
        print('endpoint literal cells',m,k,'PASS',flush=True)
    receipt['comparison']='original standard-hook cycle traces and fixed-point permutation-symmetric-power jets; no endpoint coefficient or LR correction on the comparison side'
    receipt['outcome']='PASS'
    (HERE/'ENDPOINT_HOOK_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)


if __name__=='__main__':main()
