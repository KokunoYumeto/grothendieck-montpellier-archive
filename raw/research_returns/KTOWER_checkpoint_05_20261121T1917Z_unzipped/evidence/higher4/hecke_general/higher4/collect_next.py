"""Exact next-degree residual support, without large factorization or primality.

Incomplete discovery files are skipped. Each available complete model gets
an individual replay input. The aggregate replay input is written only when
all three degrees are complete. Pairwise gcd refinement preserves complete
prime support and does not assume the saved polynomial factors irreducible.
"""
from pathlib import Path
from math import gcd, prod, isqrt
from hashlib import sha256
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ES = (32, 34, 36)
SMALL_LIMIT = 100000


def primes_through(n):
    flags = bytearray(b'\x01')*(n+1)
    flags[:2] = b'\x00\x00'
    for q in range(2, isqrt(n)+1):
        if flags[q]:
            flags[q*q:n+1:q] = b'\x00'*(((n-q*q)//q)+1)
    return [q for q in range(2, n+1) if flags[q]]


def evaluate(poly, point):
    value = 0
    for coefficient in poly:
        value = value*point+coefficient
    return value


def multiply_polynomials(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def nth_root(n, degree):
    x = 1 << ((n.bit_length()+degree-1)//degree)
    while True:
        y = ((degree-1)*x+n//x**(degree-1))//degree
        if y >= x:
            return x
        x = y


def remove_exact_powers(n):
    changed = True
    while changed:
        changed = False
        for d in (2, 3, 5, 7):
            r = nth_root(n, d)
            if r > 1 and r**d == n:
                n, changed = r, True
                break
    return n


def coprime_support_basis(values):
    """Only gcds, exact division, and verified exact-power removal."""
    values = sorted(set(remove_exact_powers(abs(v)) for v in values if abs(v)>1))
    while True:
        split = None
        for i, a in enumerate(values):
            for j in range(i+1, len(values)):
                b = values[j]
                g = gcd(a, b)
                if g > 1:
                    split = (i, j, a, b, g)
                    break
            if split:
                break
        if split is None:
            return values
        i, j, a, b, g = split
        retained = [v for t, v in enumerate(values) if t not in (i, j)]
        retained.extend((g, a//g, b//g))
        values = sorted(set(remove_exact_powers(v) for v in retained if v>1))


small_primes = primes_through(SMALL_LIMIT)
classical_path = HERE.parents[2]/'gl2_next_weights.json'
classical = {r['e']:r for r in json.loads(classical_path.read_text())['degrees']}
rows, degrees = [], []
for e in ES:
    path = HERE/'fast_native'/f'harmonic_k{e-1}_exact_exploration.json'
    if not path.exists():
        print(json.dumps({'e':e, 'status':'discovery file not yet present'}), flush=True)
        continue
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        print(json.dumps({'e':e, 'status':'discovery file not yet complete'}), flush=True)
        continue
    us = {r['p']:r for r in data['results']}
    gs = {r['p']:r for r in classical[e]['results']}
    if set(us) != {7, 13}:
        print(json.dumps({'e':e, 'status':'second auxiliary prime pending',
                          'available_primes':sorted(us)}), flush=True)
        continue
    if 'elapsed_seconds' not in data:
        print(json.dumps({'e':e, 'status':'final discovery write pending'}), flush=True)
        continue
    assert set(gs) == {7, 13}
    assert data['e'] == e and data['k'] == e-1
    degrees.append(data)
    by_prime, values, details = {}, [], []
    for p in (7, 13):
        ue, ge = 1+p**e+p**(2*e), 1+p**(2*e)
        up, gp = us[p]['charpoly_coefficients'], gs[p]['charpoly_coefficients']
        assert up[0] == gp[0] == 1 and all(isinstance(x,int) for x in up+gp)
        uv, gv = evaluate(up, ue), evaluate(gp, ge)
        assert uv == us[p]['comparison_value'] != 0
        assert gv == gs[p]['comparison_value'] != 0
        assert ue == us[p]['comparison_point'] and ge == gs[p]['comparison_point']
        factors, expanded = [], [1]
        for factor in us[p]['charpoly_factors']:
            poly, count = factor['coefficients'], factor['multiplicity']
            assert count > 0 and poly[0] == 1
            value = evaluate(poly, ue)
            assert value != 0
            for _ in range(count):
                expanded = multiply_polynomials(expanded, poly)
                factors.append(value)
        assert expanded == up and prod(factors) == uv
        factors.append(gv)
        by_prime[p] = factors
        values.append(uv*gv)
        details.append({'p':p, 'unitary_value':uv, 'classical_value':gv,
                        'combined_value':uv*gv,
                        'verified_factor_values':factors})
    common = gcd(*values)
    remaining, small = common, {}
    for q in small_primes:
        if remaining % q == 0:
            exponent = 0
            while remaining % q == 0:
                remaining //= q
                exponent += 1
            small[q] = exponent
    assert common == prod(q**a for q,a in small.items())*remaining
    cross_gcds = []
    for a in by_prime[7]:
        for b in by_prime[13]:
            g = gcd(a, b)
            for q in small:
                while g % q == 0:
                    g //= q
            if g > 1:
                cross_gcds.append(g)
    blocks = coprime_support_basis(cross_gcds)
    assert all(common % m == 0 for m in blocks)
    assert all(gcd(a,b)==1 for i,a in enumerate(blocks) for b in blocks[i+1:])
    sieve_remainder = remaining
    bounded_support = [m for m in blocks if m < 2**31]
    bounded_factors = []
    for m in bounded_support:
        while True:
            g = gcd(remaining, m)
            if g == 1:
                break
            assert 1 < g <= m < 2**31
            bounded_factors.append(g)
            remaining //= g
    # Every prime of each removed integer is below the verified Vandiver bound;
    # the integer itself need not be prime.
    assert common == prod(q**a for q,a in small.items())*prod(bounded_factors)*remaining
    blocks = [m for m in blocks if m >= 2**31]
    support_product = prod(blocks)
    residue, support_divisions = remaining, []
    while residue > 1:
        g = gcd(residue, support_product)
        assert g > 1
        support_divisions.append(g)
        residue //= g
    # Thus every prime of the exact remainder occurs in the listed moduli.
    row = {
        'e':e, 'unitary_dimension':len(up)-1,
        'classical_dimension':classical[e]['dimension'],
        'source_dimension':len(data['source_orbits']),
        'target_dimension':len(data['target_orbits']),
        'swap_plus':data['swap_signs'].count(1),
        'swap_minus':data['swap_signs'].count(-1),
        'results':details, 'combined_gcd':common,
        'proved_small_prime_factors':small, 'small_prime_bound':SMALL_LIMIT,
        'exact_remainder_after_small_prime_sieve':sieve_remainder,
        'removed_bounded_support_moduli':bounded_support,
        'removed_bounded_integer_factors':bounded_factors,
        'exact_remaining_integer':remaining,
        'residual_support_moduli':blocks,
        'residual_support_divisions':support_divisions,
        'large_primality_assumed':False,
        'discovery_data_sha256':sha256(path.read_bytes()).hexdigest(),
    }
    rows.append(row)
    (HERE/f'residual_support_e{e}.json').write_text(json.dumps({
        'status':'Exact comparison support; full model replay remains separate',
        'degrees':[row],
        'classical_data_sha256':sha256(classical_path.read_bytes()).hexdigest(),
    },indent=2)+'\n')
    individual = {'status':'Full individual higher4 model; replay pending',
                  'degrees':[data], 'comparison_gcds':[]}
    (HERE/f'harmonic_hecke_e{e}_exact_data.json').write_text(
        json.dumps(individual,indent=2)+'\n')
    print(json.dumps({k:row[k] for k in
                      ('e','unitary_dimension','classical_dimension',
                       'proved_small_prime_factors','removed_bounded_support_moduli',
                       'residual_support_moduli')}),
          flush=True)
    (HERE/'combined_next_residuals.json').write_text(json.dumps({
        'status':'Exact comparison supports; full model replay remains separate',
        'degrees':rows, 'all_three_degrees_present':len(rows)==len(ES),
        'classical_data_sha256':sha256(classical_path.read_bytes()).hexdigest(),
        'collector_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    },indent=2)+'\n')

if len(degrees) == len(ES):
    aggregate = {'status':'Full higher4 models; independent replay pending',
                 'degrees':degrees, 'comparison_gcds':[]}
    (HERE/'harmonic_hecke_next_exact_data.json').write_text(
        json.dumps(aggregate,indent=2)+'\n')
