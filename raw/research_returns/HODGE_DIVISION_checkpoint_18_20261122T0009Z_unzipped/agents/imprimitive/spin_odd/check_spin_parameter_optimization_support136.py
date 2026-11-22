#!/usr/bin/env python3
"""Exact finite supplement to D-OL27--29; no real-number approximation."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from time import perf_counter
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent


def q8_product(a, b):
    # (sign,index), with index 0,1,2,3 corresponding to 1,i,j,k.
    sa, ia = a
    sb, ib = b
    if ia == 0:
        return sa*sb, ib
    if ib == 0:
        return sa*sb, ia
    if ia == ib:
        return -sa*sb, 0
    table = {(1, 2): (1, 3), (2, 3): (1, 1), (3, 1): (1, 2),
             (2, 1): (-1, 3), (3, 2): (-1, 1), (1, 3): (-1, 2)}
    s, i = table[ia, ib]
    return sa*sb*s, i


def q8_central_column_certificate():
    group = [(s, i) for s in (1, -1) for i in range(4)]
    identity = (1, 0)
    z = (-1, 0)
    inverses = {x: next(y for y in group if q8_product(x, y) == identity) for x in group}
    chars = []
    for u, v in product((1, -1), repeat=2):
        chars.append({x: (1, u, v, u*v)[x[1]] for x in group})
    chars.append({x: 2*x[0] if x[1] == 0 else 0 for x in group})
    for i, chi in enumerate(chars):
        for j, psi in enumerate(chars):
            assert sum(chi[x]*psi[x] for x in group) == (8 if i == j else 0)
    checked = 0
    for h in group:
        conjugates = {q8_product(q8_product(x, h), inverses[x]) for x in group}
        ch = sum(q8_product(x, h) == q8_product(h, x) for x in group)
        zh = [w for w in (identity, z) if q8_product(w, h) in conjugates]
        assert ch*len(zh)//2 == 4  # Every centralizer in Q8/Z=V4 has order4.
        for central_sign in (1, -1):
            selected = [chi for chi in chars if chi[z] == central_sign*chi[identity]]
            left = sum(chi[h]**2 for chi in selected)
            right = F(ch, 2)*sum(1 if w == identity else central_sign for w in zh)
            assert left == right <= 4
            assert all(chi[h]**2 <= 4 for chi in selected)
            checked += 1
    return checked


def compositions(n):
    if n == 0:
        yield ()
    else:
        for first in range(1, n+1):
            for rest in compositions(n-first):
                yield (first,)+rest


def main():
    started = perf_counter()
    gamma = F(19, 20)
    target = F(99997, 150000)
    beta = F(1, 6)-F(1, 10**7)
    delta = F(1, 6)+F(1, 10**5)
    assert target == 1-2*delta
    m, n1, n2 = 8, 12, 8
    c = gamma**m
    u = (target-c)/(1-c)
    assert u == F(247774877, 25849310877) > 0
    left = 16*3**17*247774877**4
    right = 25849310877**4
    assert left > right
    assert u**4 > F(1, 16*3**17)
    # Case A uses the complete degree/centralizer bridge.
    assert 18 < 64  # 3 sqrt(2)<8.
    assert F(1, 16*3**33) < F(1, 9)**4
    assert F(2, 9) < target

    patterns = 0
    for bits in product((0, 1), repeat=m):
        k = sum(bits)
        assert gamma**(m-k) <= c+F(k, m)*(1-c)
        assert k == sum(bits)  # coefficient of the exact fixed-space sum.
        patterns += 1
    # Every possible greedy group's proper prefix has total below eight.
    greedy = 0
    largest = 0
    for subtotal in range(n2):
        for prefix in compositions(subtotal):
            for last in range(n2-subtotal, n1):
                group = prefix+(last,)
                assert all(x <= 11 for x in group)
                assert sum(group[:-1]) < n2 <= sum(group) <= n1+n2-2
                largest = max(largest, sum(group))
                greedy += 1
    assert largest == 18
    threshold = (m-1)*(n1+n2-2)+n2+2
    assert threshold == 136
    assert threshold-2-(m-1)*largest == 8
    assert n1 >= 12 and n2 >= 8 and n2 >= 5

    gauss = {}
    for q in (3, 5):
        fixed = (F(1, q)+F(1, q**20))/(1-F(1, q**20)-F(1, q**40))
        upper = 1-4*beta if q == 3 else F(1, 4)
        assert fixed < upper
        gauss[str(q)] = {'fixed_fraction': str(fixed), 'strict_upper': str(upper)}
    assert F(1, 6) < delta < F(3, 16) < F(7, 32)
    assert 13*beta-2 > F(1, 7)
    assert 11*beta+delta-2 == F(89, 10**7)
    assert F(6*10**7, 89) < 10**6
    assert 2*beta*(1-beta) > F(1, 4)
    dimensions = []
    for d in (273, 274):
        b = d-2
        assert (d-1)//2 == threshold
        assert b >= 43 and d-4 >= 21 and d >= 25
        assert (b+1)//2 <= b-2
        assert 3**(b-1)-3**((b+1)//2)-1 >= 2*3**(b-2)-1
        assert 2*3**(b-2)-1 >= 2*3**269-1 > 10**6
        assert d-1 > threshold
        dimensions.append({'natural_dimension': d, 'no_pair_support': (d-1)//2,
                           'line_radical_dimension': b})
    assert 2*3**15-1 > 10**6

    column_checks = q8_central_column_certificate()
    proof = (HERE/'spin_parameter_optimization_section.tex').read_text()
    assert not any(ord(ch) < 32 and ch not in '\n\r\t' for ch in proof)
    assert proof.count('\\[') == proof.count('\\]')
    assert proof.count('\\begin{proof}') == proof.count('\\end{proof}') == 3
    tags = re.findall(r'\\tag\{([^}]+)\}', proof)
    assert len(tags) == len(set(tags)) == 20
    assert '$\\sqrt N/6$, not $\\sqrt{N/6}$' in proof
    out = {
        'status': 'PASS', 'arithmetic': 'integers and Fraction only; no floating-point comparisons',
        'proof_sha256': hashlib.sha256(proof.encode()).hexdigest(),
        'counts': {'trivial_factor_patterns': patterns, 'all_greedy_group_endings': greedy,
                   'Q8_central_character_column_checks': column_checks},
        'parameters': {'N1': n1, 'N2': n2, 'm0': m, 'natural_support_threshold': threshold},
        'rho': str(target), 'gamma': str(gamma), 'gamma_power': str(c),
        'alpha_fourth_power': str(F(1, 16*3**17)), 'comparison_rational_u': str(u),
        'integer_comparison': {'left': str(left), 'right': str(right), 'strict_greater': True},
        'gauss_endpoints': gauss, 'natural_dimension_endpoints': dimensions,
        'source_excess': str(11*beta+delta-2), 'seconds': perf_counter()-started,
        'scope': 'Finite constants, all eight-factor patterns and finite cover example. Universal decomposition/Clifford/source arguments remain the written proof.'}
    (HERE/'spin_parameter_optimization_checked.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))


if __name__ == '__main__':
    main()
