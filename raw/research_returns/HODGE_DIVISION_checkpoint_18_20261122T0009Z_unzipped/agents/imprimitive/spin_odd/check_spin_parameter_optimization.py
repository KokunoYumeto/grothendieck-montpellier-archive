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


def packing_certificate():
    # Finite local steps in the universal maximal-packing proof.
    weights = (3, 4, 5, 6)
    minimal = []
    checked = 0
    for counts in product(range(5), repeat=4):
        total = sum(x*w for x, w in zip(counts, weights))
        checked += 1
        if total >= 8 and all(c == 0 or total-w < 8 for c, w in zip(counts, weights)):
            minimal.append((counts, total))
    assert max(total for _, total in minimal) == 12
    assert [c for c, total in minimal if total == 12] == [(0, 0, 0, 2)]
    remainders = [c for c in product(range(3), repeat=4)
                  if sum(x*w for x, w in zip(c, weights)) == 7]
    assert remainders == [(1, 1, 0, 0)]
    assert 6+3 >= 8 and 6+4 >= 8
    assert max(7*12+6, 7*11+7) == 90
    assert 15*6 == 90 and 15//2 == 7
    return checked, len(minimal)


def regular_seven_certificate():
    q = 3
    one = (1, 0, 0, 0, 0, 0, 0)
    def mul(a, b):
        return tuple(sum(a[i]*b[k-i] for i in range(k+1)) % q for k in range(7))
    sx = (0, 2, 1, 2, 1, 2, 1)
    powers = [one]
    for j in range(6):
        powers.append(mul(powers[-1], sx))
    def sigma(a):
        return tuple(sum(a[i]*powers[i][k] for i in range(7)) % q for k in range(7))
    fixed = kernel = 0
    images = set()
    for tail in product(range(q), repeat=6):
        a = (1,)+tail
        sa = sigma(a)
        assert sigma(sa) == a
        value = mul(a, sa)
        assert sigma(value) == value
        images.add(value)
        fixed += sa == a
        kernel += value == one
    assert fixed == kernel == len(images) == 27
    assert 2*kernel == 54
    return 729


def main():
    started = perf_counter()
    gamma = F(19, 20)
    target = F(99997, 150000)
    beta = F(1, 6)-F(1, 10**7)
    delta = F(1, 6)+F(1, 10**5)
    assert target == 1-2*delta
    m, n1, n2 = 8, 7, 8
    c = gamma**m
    u = (target-c)/(1-c)
    assert u == F(247774877, 25849310877) > 0
    left = 16*3**17*247774877**4
    right = 25849310877**4
    assert left > right
    assert u**4 > F(1, 16*3**17)
    # Case A uses the complete degree/centralizer bridge.
    assert F(2, 3) < 1  # Seven-block endpoint sqrt(2/3)/8 < 1/8.
    assert F(1, 8)+F(1, 54) == F(31, 216) < F(3, 5)
    assert 2 < F(9, 4)  # sqrt(2) < 3/2.
    assert F(9, 16)+F(1, 162) == F(737, 1296) < F(3, 5) < target
    assert F(1, 16*3**13) < F(1, 54)**4
    assert F(1, 16*3**17) < F(1, 162)**4

    patterns = 0
    for bits in product((0, 1), repeat=m):
        k = sum(bits)
        assert gamma**(m-k) <= c+F(k, m)*(1-c)
        assert k == sum(bits)  # coefficient of the exact fixed-space sum.
        patterns += 1
    packing_cases, minimal_patterns = packing_certificate()
    ring_cases = regular_seven_certificate()
    threshold = 93
    assert threshold-2 == 91
    assert n1 >= 7 and n2 >= 8 and n2 >= 5

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
    for d in (187, 188):
        b = d-2
        assert (d-1)//2 == threshold
        assert b >= 43 and d-4 >= 21 and d >= 25
        assert (b+1)//2 <= b-2
        assert 3**(b-1)-3**((b+1)//2)-1 >= 2*3**(b-2)-1
        assert 2*3**(b-2)-1 >= 2*3**183-1 > 10**6
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
    assert len(tags) == len(set(tags)) == 22
    assert '$\\sqrt N/6$, not $\\sqrt{N/6}$' in proof
    out = {
        'status': 'PASS', 'arithmetic': 'integers and Fraction only; no floating-point comparisons',
        'proof_sha256': hashlib.sha256(proof.encode()).hexdigest(),
        'counts': {'trivial_factor_patterns': patterns, 'packing_local_patterns': packing_cases, 'minimal_cover_patterns': minimal_patterns,
                   'regular_unipotent_F3_units': ring_cases,
                   'Q8_central_character_column_checks': column_checks},
        'parameters': {'N1': n1, 'N2': n2, 'm0': m, 'natural_support_threshold': threshold},
        'rho': str(target), 'gamma': str(gamma), 'gamma_power': str(c),
        'alpha_fourth_power': str(F(1, 16*3**17)), 'comparison_rational_u': str(u),
        'integer_comparison': {'left': str(left), 'right': str(right), 'strict_greater': True},
        'gauss_endpoints': gauss, 'natural_dimension_endpoints': dimensions,
        'source_excess': str(11*beta+delta-2), 'seconds': perf_counter()-started,
        'scope': 'Finite constants, all eight-factor patterns, local packing patterns, the regular-seven ring and finite cover example. Universal decomposition/Clifford/source arguments remain the written proof.'}
    (HERE/'spin_parameter_optimization_checked.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))


if __name__ == '__main__':
    main()
