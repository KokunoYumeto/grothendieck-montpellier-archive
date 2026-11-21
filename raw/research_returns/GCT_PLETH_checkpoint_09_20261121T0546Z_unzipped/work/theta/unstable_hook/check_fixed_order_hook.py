"""T064 independent-side cycle traces and literal general-order cells."""
from pathlib import Path
from fractions import Fraction
import sys,json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'root'))
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import partitions,character,z
from check_stable_hook_positive import trace_data,actual_module,witnesses
import fixed_order_hook_positive as P


def direct_jet(m,k,r,nu):
    answer=Fraction()
    for cyc in partitions(m):
        fixed=cyc.count(1)
        if not fixed:continue
        rest=list(cyc);rest.remove(1)
        sym=[1]+[0]*(k-1)
        for ell in rest:
            for h in range(ell,k):sym[h]+=sym[h-ell]
        _,exterior=trace_data(tuple(rest),r)
        answer+=Fraction(character(nu,cyc)*fixed*sym[-1]*exterior[r],z(cyc))
    assert answer.denominator==1
    return int(answer)


def main():
    receipt={'statement':'T-064','jet_multiplicity_comparisons':0,
             'coefficient_comparisons':0,'removed_point_cases':0,'literal_polytope_cases':0,
             'literal_polytopes':0,'original_witnesses':0,'retained_witnesses':0,
             'max_actual_correction':{},'uniform_bounds':{k:P.correction_bound(k) for k in range(1,6)}}
    for m in range(4,10):
        for k in range(1,6):
            maximum=0
            for r in range(m-1):
                for nu in partitions(m):
                    expected=direct_jet(m,k,r,nu)
                    got=P.jet_multiplicity(m,k,r,nu)
                    assert got==expected,(m,k,r,nu,got,expected)
                    assert got<=P.correction_bound(k)
                    maximum=max(maximum,got)
                    receipt['jet_multiplicity_comparisons']+=1
                    for a in (2*k+1,2*k+2):
                        expected_value=actual_module(m,a,r,nu)-expected
                        assert P.coefficient(m,k,a,r,0,nu)==expected_value
                        assert P.coefficient(m,k,a,r,1,P.stable.transpose(nu))==expected_value
                        receipt['coefficient_comparisons']+=2
                        if got and k<=4:
                            P.removed_points(m,k,a,r,nu)
                            receipt['removed_point_cases']+=1
                    if got and k<=4:
                        P.removed_points(m,k,10**20+1,r,nu)
                        receipt['removed_point_cases']+=1
            receipt['max_actual_correction'][f'm{m}_k{k}']=maximum
        print('all fixed-order cycle traces',m,'PASS',flush=True)
    for m,k,a in ((4,3,7),(5,3,7),(4,4,9)):
        for r in range(m-1):
            for nu in partitions(m):
                data=P.polytopes(m,k,a,r,0,nu);retained=0
                receipt['literal_polytope_cases']+=1
                receipt['literal_polytopes']+=len(data['polytopes'])
                for point in witnesses(m,a,r,nu):
                    receipt['original_witnesses']+=1
                    matches=sum(P.stable.valid_witness(cell,point) for cell in data['polytopes'])
                    assert matches==int(point not in data['removed_points']),(m,k,a,r,nu,point,matches)
                    retained+=matches
                assert retained==P.coefficient(m,k,a,r,0,nu)
                receipt['retained_witnesses']+=retained
        print('literal general-order cells',m,k,a,'PASS',flush=True)
    receipt['comparison']='original standard hook cycle traces and permutation-symmetric-power fixed-point jets; no monomial-orbit/exterior/LR formula on comparison side'
    receipt['outcome']='PASS'
    (HERE/'FIXED_ORDER_HOOK_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)


if __name__=='__main__':main()

