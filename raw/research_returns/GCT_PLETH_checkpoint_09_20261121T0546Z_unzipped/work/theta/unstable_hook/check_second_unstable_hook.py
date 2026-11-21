"""T063: original cycle traces and literal multiple-point polytope checks."""
from pathlib import Path
from fractions import Fraction
import sys,json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'root'))
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import partitions,character,z
from check_stable_hook_positive import trace_data,actual_module,witnesses
import second_unstable_hook_positive as P


def induced_twojet(m,r,nu):
    value=Fraction()
    for cyc in partitions(m):
        fixed=cyc.count(1)
        if not fixed:continue
        rest=list(cyc);rest.remove(1)
        _,ext=trace_data(tuple(rest),r)
        value+=Fraction(character(nu,cyc)*fixed*rest.count(1)*ext[r],z(cyc))
    assert value.denominator==1
    return int(value)


def main():
    receipt={'statement':'T-063','cycle_character_cases':0,'branching_multiplicities':0,
             'removed_point_cases':0,'literal_polytope_cases':0,'literal_polytopes':0,
             'original_witnesses':0,'retained_witnesses':0,'max_correction':0}
    for m in range(4,9):
        for r in range(m-1):
            targets=P.target_multiplicities(m,r)
            for nu in partitions(m):
                correction=induced_twojet(m,r,nu)
                assert correction==targets.get(nu,0)
                receipt['branching_multiplicities']+=1
                receipt['max_correction']=max(receipt['max_correction'],correction)
                for a in range(5,15):
                    expected=actual_module(m,a,r,nu)-correction
                    for t in (0,1):
                        mu=P.stable.transpose(nu) if t else nu
                        assert P.coefficient(m,a,r,t,mu)==expected,(m,a,r,t,nu)
                        receipt['cycle_character_cases']+=1
        print('cycle traces',m,'PASS',flush=True)
    for m in range(4,16):
        for r in range(m-1):
            for nu in P.target_multiplicities(m,r):
                for a in (5,6,7,8,10**20+1):
                    P.removed_points(m,a,r,nu)
                    receipt['removed_point_cases']+=1
    for m in (4,5):
        for r in range(m-1):
            for nu in partitions(m):
                for a in (5,6):
                    data=P.polytopes(m,a,r,0,nu)
                    receipt['literal_polytope_cases']+=1
                    receipt['literal_polytopes']+=len(data['polytopes'])
                    retained=0
                    for point in witnesses(m,a,r,nu):
                        receipt['original_witnesses']+=1
                        memberships=sum(P.stable.valid_witness(poly,point)
                                        for poly in data['polytopes'])
                        removed=point in data['removed_points']
                        assert memberships==int(not removed),(m,a,r,nu,point,memberships)
                        retained+=memberships
                    assert retained==P.coefficient(m,a,r,0,nu)
                    receipt['retained_witnesses']+=retained
    receipt['comparison']='original hook Jacobi–Trudi cycle traces and literal fixed-point first-jet induction, no small-label formula on comparison side'
    receipt['outcome']='PASS'
    (HERE/'SECOND_UNSTABLE_HOOK_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)


if __name__=='__main__':main()

