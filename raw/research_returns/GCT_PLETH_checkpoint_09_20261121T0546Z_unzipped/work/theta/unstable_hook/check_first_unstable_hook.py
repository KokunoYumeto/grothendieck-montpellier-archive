"""T061 checks from original cycle traces and literal deleted-point matrices."""
from pathlib import Path
from fractions import Fraction
import sys
import json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'root'))
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import partitions,character,z
from check_stable_hook_positive import trace_data,actual_module,witnesses
import first_unstable_hook_positive as P


def induced_coefficient(m,r,nu):
    value=Fraction()
    for cyc in partitions(m):
        fixed=cyc.count(1)
        if not fixed:continue
        smaller=list(cyc);smaller.remove(1)
        _,ext=trace_data(tuple(smaller),r)
        value+=Fraction(character(nu,cyc)*fixed*ext[r],z(cyc))
    assert value.denominator==1
    return int(value)


def main():
    receipt={'statement':'T-061','cycle_character_cases':0,'canonical_points':0,
             'literal_polytope_cases':0,'literal_polytopes':0,'original_witnesses':0,
             'retained_witnesses':0,'zero_degree_polytope_cases':0}
    for m in range(4,9):
        for r in range(m-1):
            for nu in partitions(m):
                correction=induced_coefficient(m,r,nu)
                assert correction==int(nu in P.target_labels(m,r))
                for a in range(2,16):
                    if (m-2)*a<m+r:continue
                    expected=actual_module(m,a,r,nu)-correction
                    for t in (0,1):
                        mu=P.stable.transpose(nu) if t else nu
                        assert P.coefficient(m,a,r,t,mu)==expected,(m,a,r,t,mu)
                        receipt['cycle_character_cases']+=1
        print('cycle traces m',m,'PASS',flush=True)
    for m in range(4,21):
        for r in range(m-1):
            for a in (3,4,5,6,10,10**20+1):
                for nu in P.target_labels(m,r):
                    P.canonical_removed_point(m,a,r,nu)
                    receipt['canonical_points']+=1
    for m in (4,5):
        for r in range(m-1):
            for a in range(2,6):
                if (m-2)*a<m+r:continue
                for nu in partitions(m):
                    data=P.polytopes(m,a,r,0,nu)
                    if a==2:
                        assert len(data['polytopes'])==P.coefficient(m,a,r,0,nu)
                        receipt['zero_degree_polytope_cases']+=1
                        continue
                    receipt['literal_polytope_cases']+=1
                    receipt['literal_polytopes']+=len(data['polytopes'])
                    retained=0
                    for point in witnesses(m,a,r,nu):
                        receipt['original_witnesses']+=1
                        memberships=sum(P.stable.valid_witness(poly,point) for poly in data['polytopes'])
                        removed=point==data.get('removed_point')
                        assert memberships==int(not removed),(m,a,r,nu,point,memberships)
                        retained+=memberships
                    assert retained==P.coefficient(m,a,r,0,nu),(m,a,r,nu,retained)
                    receipt['retained_witnesses']+=retained
    receipt['comparison']='original standard-cycle hook Jacobi–Trudi and literal fixed-point induction; no content or correction-label formula on the comparison side'
    receipt['outcome']='PASS'
    (HERE/'FIRST_UNSTABLE_HOOK_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)


if __name__=='__main__':main()
