"""T067: degree-one identity, previous exact endpoints, literal positive cells.

--full-scan also reproduces the initial 42,624-case consistency sweep.
"""
from pathlib import Path
import argparse,json
from check_fixed_order_hook import witnesses
import all_fixed_order_hook_positive as P
import pair_boundary_hook_positive as boundary

HERE=Path(__file__).resolve().parent


def full_scan():
    count=identity=0
    for k in range(1,5):
        for m in range(4,14):
            for a in range(k+1,2*k+2):
                for r in range(m-1):
                    if (m-2)*a<m*k+r:continue
                    for nu in P.fixed.partitions(m):
                        answer=P.coefficient(m,k,a,r,0,nu)
                        if a==k+1:
                            lam=P.parameters(m,k,a,r,0,nu)[0]
                            assert answer==int(nu==tuple(x for x in lam if x))
                            identity+=1
                        count+=1
        print('full exact-complex scan',k,count,'PASS',flush=True)
    return {'consistency_cases':count,'degree_one_identity_cases':identity}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full-scan',action='store_true')
    args=parser.parse_args()
    receipt={'statement':'T-067','degree_one_identity_comparisons':0,
             'previous_endpoint_comparisons':0,'selected_point_cases':0,
             'literal_polytope_cases':0,'literal_polytopes':0,
             'original_witnesses':0,'retained_witnesses':0,'largest_selected_subset_seen':0}
    if args.full_scan:receipt['reproduced_full_scan']=full_scan()
    # The plethysm at inner degree one is literally S_mu(V).
    for m,k,r in ((8,3,0),(9,3,0),(9,3,1),(10,3,2),(13,4,3),(16,5,4)):
        a=k+1;lam=P.parameters(m,k,a,r,0,(m,))[0];lam=tuple(x for x in lam if x)
        for nu in P.fixed.partitions(m):
            expected=int(nu==lam)
            assert P.coefficient(m,k,a,r,0,nu)==expected
            assert P.coefficient(m,k,a,r,1,P.stable.transpose(nu))==expected
            receipt['degree_one_identity_comparisons']+=2
            terms=P.complex_multiplicities(m,k,a,r,nu)
            for q,value in enumerate(terms,1):
                if value:receipt['largest_selected_subset_seen']=max(receipt['largest_selected_subset_seen'],q)
        print('literal degree-one identity',m,k,r,'PASS',flush=True)
    for m in range(4,9):
        for k in range(1,4):
            for a in range(max(2,2*k-1),2*k+3):
                for r in range(m-1):
                    if (m-2)*a<m*k+r:continue
                    for nu in P.fixed.partitions(m):
                        expected=boundary.full_coefficient(m,k,a,r,0,nu)
                        assert P.coefficient(m,k,a,r,0,nu)==expected
                        receipt['previous_endpoint_comparisons']+=1
        print('previous actual endpoint formulas',m,'PASS',flush=True)
    selected=[]
    for m,k,a,r in ((8,3,4,0),(10,3,4,2),(13,4,5,3)):
        choices=[]
        for nu in P.fixed.partitions(m):
            terms=P.complex_multiplicities(m,k,a,r,nu)
            if P.correction(m,k,a,r,nu) and (len(terms)<3 or any(terms[2:])):
                choices.append(nu)
        if not choices:
            choices=[nu for nu in P.fixed.partitions(m) if P.correction(m,k,a,r,nu)]
        selected.extend((m,k,a,r,nu) for nu in choices[:3])
        lam=tuple(x for x in P.parameters(m,k,a,r,0,(m,))[0] if x)
        selected.append((m,k,a,r,lam))
    for m,k,a,r,nu in selected:
        data=P.polytopes(m,k,a,r,0,nu);retained=0
        receipt['selected_point_cases']+=1
        receipt['literal_polytope_cases']+=1
        receipt['literal_polytopes']+=len(data['polytopes'])
        for point in witnesses(m,a,r,nu):
            receipt['original_witnesses']+=1
            matches=sum(P.stable.valid_witness(cell,point) for cell in data['polytopes'])
            assert matches==int(point not in data['removed_points'])
            retained+=matches
        assert retained==P.coefficient(m,k,a,r,0,nu)
        receipt['retained_witnesses']+=retained
        print('new-range literal positive cells',m,k,a,r,nu,'PASS',flush=True)
    receipt['comparisons']='literal inner-degree-one identity (including five selected blocks), previously proved endpoint formulas, and direct lattice witnesses in the original stable matrices'
    receipt['outcome']='PASS'
    (HERE/'ALL_FIXED_ORDER_HOOK_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)


if __name__=='__main__':main()
