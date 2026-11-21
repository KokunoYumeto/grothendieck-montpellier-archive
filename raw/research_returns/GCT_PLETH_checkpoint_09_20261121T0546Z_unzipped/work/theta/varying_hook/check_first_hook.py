"""T060: cycle-character, support, matrix and large-index checks.

The comparison side imports only the previously independently written
Murnaghan--Nakayama character primitive. It does not use fake degrees.
"""
from pathlib import Path
import sys
import json
from math import factorial, comb

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE.parent.parent/'rectangular'))
from verify_rectangular import partitions, character, z
import first_hook_positive as target


def standard_series(cyc, cap):
    out = [1]+[0]*cap
    for ell in cyc:
        for i in range(ell, cap+1):
            out[i] += out[i-ell]
    return [out[i]-(out[i-1] if i else 0) for i in range(cap+1)]


def expected_values(m, mu, cap):
    out = [0]*(cap+1)
    for cyc in partitions(m):
        h = standard_series(cyc, cap+1)
        weight = factorial(m)//z(cyc)*character(mu,cyc)
        e = cyc.count(1)-1
        for a in range(1,cap+1):
            out[a] += weight*(e*h[a]-h[a+1])
    if any(v%factorial(m) for v in out):
        raise ArithmeticError('nonintegral cycle inner product')
    return [v//factorial(m) for v in out]


def literal_points(piece):
    weights = piece['equalities'][0]
    rhs = piece['equality_bounds'][0]
    selector = bool(piece['variables'] and piece['variables'][-1]=='y')
    coinweights = weights[:-1] if selector else weights
    coefficient = piece['inequality_bounds'][-1]+1 if selector else 1
    point = []
    def rec(j, remaining):
        if j == len(coinweights):
            if remaining:
                return
            for y in range(coefficient):
                p = point+([y] if selector else [])
                assert all(sum(a*b for a,b in zip(row,p))<=bound
                           for row,bound in zip(piece['inequalities'],piece['inequality_bounds']))
                assert sum(a*b for a,b in zip(weights,p))==rhs
                yield tuple(p)
            return
        w=coinweights[j]
        for value in range(remaining//w+1):
            point.append(value)
            yield from rec(j+1,remaining-w*value)
            point.pop()
    yield from rec(0,rhs)


def main():
    coefficient_cases=support_cases=matrices=witnesses=0
    for m in range(4,11):
        for mu in partitions(m):
            expected=expected_values(m,mu,60)
            for a in range(1,61):
                got=target.coefficient(m,a,0,a,mu)
                assert got==expected[a],(m,mu,a,got,expected[a])
                assert target.support(m,a,0,a,mu)['positive']==bool(got)
                coefficient_cases+=1;support_cases+=1
            if m<=6:
                for t in (0,1):
                    nu=target.transpose(mu) if t else mu
                    ex=expected_values(m,nu,10)
                    for a in range(1,11):
                        formula=target.polytopes(m,a,t,a+t,mu)
                        total=0
                        for piece in formula['polytopes']:
                            points=list(literal_points(piece))
                            assert len(points)==len(set(points))
                            total+=len(points);witnesses+=len(points);matrices+=1
                        assert total==ex[a]
                        coefficient_cases+=1
        print('passed m',m,flush=True)
    # For m=4, every degree>=1 sequence is a period-12 quasipolynomial
    # of degree<=2: the exact denominator has root orders2,3,4 and
    # multiplicities at most3. Three small original cycle values fix it.
    large_cases=0
    for mu in partitions(4):
        expected=expected_values(4,mu,48)
        for residue in range(12):
            base=12+residue
            values=[expected[base+12*j-1] for j in range(3)]
            differences=(values[0],values[1]-values[0],values[2]-2*values[1]+values[0])
            q=10**30+17
            wanted=sum(differences[j]*comb(q,j) for j in range(3))
            degree=base+12*q
            assert target.coefficient(4,degree-1,0,degree-1,mu)==wanted
            large_cases+=1
    # The explicit m4 invariant Hilbert numerator witnesses the failed
    # all-label graded-freeness candidate.
    q=target.denominator(2,4)
    coefficients=[0]+[target.coefficient(4,d-1,0,d-1,(4,)) if d>=2 else 0 for d in range(1,15)]
    product=target.multiply(coefficients,q)
    assert product[:10]==[0,0,0,0,0,1,1,1,0,-1]
    receipt={'statement':'T-060','cycle_character_and_parity_cases':coefficient_cases,
             'support_checks':support_cases,'literal_polytope_matrices':matrices,
             'literal_integer_witnesses':witnesses,'large_binary_index_cases':large_cases,
             'm4_invariant_numerator':'q^5+q^6+q^7-q^9',
             'comparison':'cycle-index standard traces and independent MN primitive; no fake degrees on comparison side',
             'outcome':'PASS'}
    (HERE/'FIRST_HOOK_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2),flush=True)


if __name__=='__main__':main()
