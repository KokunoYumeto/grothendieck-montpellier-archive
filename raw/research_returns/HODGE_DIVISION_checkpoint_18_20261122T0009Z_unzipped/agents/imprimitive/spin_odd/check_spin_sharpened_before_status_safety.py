#!/usr/bin/env python3
"""Exact integer/rational constant certificate for D-OL25--26."""
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent


def main():
    started = perf_counter()
    beta = F(1, 6) - F(1, 10**7)
    delta = F(1, 6) + F(1, 10**5)
    exponent = F(419, 53)
    assert beta == F(4999997, 30000000)
    assert delta == F(50003, 300000)
    assert exponent**2 == F(175561, 2809) < F(375, 6)
    assert 125*2809 - 2*175561 == 3
    assert 375 >= 144
    left = 19**419 * 150000**53
    right = 20**419 * 99997**53
    assert left < right
    assert left.bit_length() == right.bit_length() == 2692
    assert F(99997, 150000) == 1-2*delta
    margin = right-left

    endpoint = {}
    for q in (3, 5):
        c = (F(1, q)+F(1, q**20))/(1-F(1, q**20)-F(1, q**40))
        target = 1-4*beta if q == 3 else F(1, 4)
        assert 0 < c < target
        endpoint[str(q)] = {'fixed_fraction': str(c), 'strict_upper_bound': str(target),
                            'positive_margin': str(target-c)}
    assert F(1, 6) < delta < F(3, 16) < F(7, 32)
    assert 13*beta-2 > F(1, 7)
    assert 11*beta+delta-2 == F(89, 10**7)
    assert F(6*10**7, 89) < 10**6
    assert 2*beta*(1-beta) > F(1, 4)
    assert 0 < beta < F(1, 6)

    # The minimum support/dimension cases used in the universal proof.
    minimum_cases = []
    for dimension in (751, 752):
        m = dimension-2
        support = (dimension-2+1)//2
        assert support == 375
        assert m >= 43
        assert dimension-4 >= 21
        assert dimension >= 25 and dimension >= 22
        assert dimension-1 >= 375
        assert (m+1)//2 <= m-2
        assert 3**(m-1)-3**((m+1)//2)-1 >= 2*3**(m-2)-1
        assert 2*3**(m-2)-1 >= 2*3**747-1 > 10**6
        minimum_cases.append({'dimension': dimension, 'minimum_no_pair_support': support,
                              'line_radical_dimension': m})
    assert 2*3**15-1 == 28697813 > 10**6
    # Half-exponents in (SSP.9), checked after multiplication by two.
    assert -(43-1) <= -42 <= -40
    assert 2-43 <= -40
    assert 2*(1-43) <= -80

    proof = (HERE/'spin_sharpened_section.tex').read_text()
    assert not any(ord(c) < 32 and c not in '\n\r\t' for c in proof)
    assert proof.count('\\[') == proof.count('\\]')
    assert proof.count('\\begin{proof}') == proof.count('\\end{proof}') == 2
    tags = re.findall(r'\\tag\{([^}]+)\}', proof)
    assert len(tags) == len(set(tags)) == 12

    result = {
        'status': 'PASS',
        'arithmetic': 'Python integers and fractions.Fraction; no floating-point comparisons',
        'proof_sha256': hashlib.sha256(proof.encode()).hexdigest(),
        'beta': str(beta), 'delta': str(delta), 'rational_exponent': str(exponent),
        'rational_exponent_square': str(exponent**2),
        'power_comparison': {
            'left': '19**419 * 150000**53', 'right': '20**419 * 99997**53',
            'strict_less': True, 'both_operand_bit_lengths': 2692,
            'positive_difference_bit_length': margin.bit_length(),
            'positive_difference_sha256': hashlib.sha256(
                margin.to_bytes((margin.bit_length()+7)//8, 'big')).hexdigest()},
        'gauss_endpoints': endpoint,
        'minimum_dimension_cases': minimum_cases,
        'one_good_mark_excess': str(11*beta+delta-2),
        'maximum_degree_if_one_good_mark': str(F(6*10**7, 89)),
        'thirteen_mark_excess': str(13*beta-2),
        'two_bad_factor_support': str(2*beta*(1-beta)),
        'small_proxy_degree_floor': 2*3**15-1,
        'seconds': perf_counter()-started,
        'scope': 'Exact finite constants and minimal endpoints; the written Gauss and monotonicity arguments prove all dimensions and fields.'}
    (HERE/'spin_sharpened_checked.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__ == '__main__':
    main()
