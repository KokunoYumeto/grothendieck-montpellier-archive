#!/usr/bin/env python3
"""Exact B98 supplement; no field or BT realization is inferred."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
import json, time, traceback
import sympy as s

OUT = Path(__file__).with_suffix('.output.json')
assert not OUT.exists(), 'Preserve prior executed output before rerunning'
started = time.perf_counter()
counts = {}

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**.5)+1))

def rank_mod(rows, p):
    a = [list(x) for x in rows]
    r = 0
    for j in range(len(a[0]) if a else 0):
        i = next((i for i in range(r, len(a)) if a[i][j] % p), None)
        if i is None:
            continue
        a[r], a[i] = a[i], a[r]
        inv = pow(a[r][j] % p, -1, p)
        a[r] = [(v*inv) % p for v in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][j] % p
                a[i] = [(u-c*v) % p for u, v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r

def run():
    p, x, y = s.symbols('p x y')
    q = p**2
    N = q-1
    c1 = N*(p-1)
    c2 = (q*q-1)*(p-1)
    lower = p*p*(p-1)**2+p-1
    delta2_min = p*p-p-2+1/p
    checks = [
        ((p*p-p)*p+(p-1)*p*p, 2*p*p*(p-1), 'cyclotomic_displacement_sum'),
        ((p-1)+p*2*p*p*(p-1)-p*p*N, lower, 'two_actual_towers_lower_bound'),
        (lower/(p-1)-(p+1), p*(p*p-p-1), 'different_to_upper_sum'),
        ((p*(p*p-p-1)-(p-1))/p, delta2_min, 'second_upper_break_bound'),
        ((p*p-1)*(x+1)+(p-1)*(p*y-(p-1)*x-x),
         (p-1)*(x+p*y+p+1), 'cyclic_order_p_squared_different'),
        (q*(N*delta2_min-c1)-c2, N*(p**4-3*p**3+1), 'strict_terminal_conductor_gap'),
        (N*delta2_min-c1, N*(p*p-2*p-1+1/p), 'second_above_first_break'),
        (p**4-3*p**3+1, p**3*(p-3)+1, 'uniform_positive_factor'),
        (p**3*(N*N-c1)-p*c2, p*N*(p-1)*(p**3-p*p-1), 'prior_traceless_gap')
    ]
    symbolic = []
    for a, b, name in checks:
        assert s.cancel(a-b) == 0, name
        symbolic.append(name)
    counts['symbolic_identities'] = len(symbolic)

    primes = [n for n in range(5, 32) if prime(n)]
    rows = []
    derivative_terms = derivative_profiles = cyclotomic_elements = 0
    rational_delta_rows = terminal_inequalities = 0
    for pp in primes:
        qq = pp*pp
        nn = qq-1
        ee = pp*(pp-1)
        cc1 = nn*(pp-1)
        cc2 = (qq*qq-1)*(pp-1)
        # All derivative monomials with coefficient valuation 1..p+2.
        # Different i have different residues, including the leading one.
        residues = {nn % pp}
        for i in range(1, pp):
            assert (i-1) not in residues
            residues.add(i-1)
            for va in range(1, pp+3):
                v = pp*va+i-1
                assert v % pp == i-1
                derivative_terms += 1
        assert residues == set(range(pp))
        # One non-leading coefficient at a time and explicit all-term profiles.
        profiles = [[pp*va+i-1 for i in range(1, pp)] for va in range(1, pp+3)]
        profiles += [[pp*(1+(i*j % (pp+2)))+i-1 for i in range(1, pp)]
                     for j in range(pp+2)]
        for v in profiles:
            vals = [nn]+v
            assert len(set(vals)) == len(vals)
            assert min(vals) <= nn and min(vals) >= pp-1
            derivative_profiles += 1

        # Literal cyclotomic exponent census over the cyclic p^2 group.
        ramification_sum = 0
        nonterminal = terminal = 0
        for a in range(1, pp*pp):
            exponent = 1+pp*a
            valuation = pp if a % pp else pp*pp
            assert exponent % pp == 1
            ramification_sum += valuation
            nonterminal += int(a % pp != 0)
            terminal += int(a % pp == 0)
            cyclotomic_elements += 1
        assert nonterminal == pp*pp-pp and terminal == pp-1
        assert ramification_sum == 2*pp*pp*(pp-1)
        lb = pp*pp*(pp-1)**2+pp-1
        assert lb == (pp-1)+pp*ramification_sum-pp*pp*nn

        # Rational break tests supplement the symbolic monotonic endpoint;
        # no Hasse--Arf/integer-break assumption is made.
        minimum_gap = None
        for den in (1, pp, pp*pp):
            for num in range(1, (pp-1)*den+1):
                d1 = F(num, den)
                d2 = (pp*(pp*pp-pp-1)-d1)/pp
                lo2 = pp*d2-(pp-1)*d1
                assert d2 > d1 and lo2 > d1
                df = (pp*pp-1)*(d1+1)+(pp-1)*(lo2-d1)
                assert df == lb
                assert d2 >= F(pp*pp-pp-2)+F(1, pp)
                dt = nn*d2
                assert dt > cc1
                gap = qq*(dt-cc1)-cc2
                assert gap >= nn*(pp**4-3*pp**3+1) > 0
                minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
                for rr in (3, 4):
                    assert pp**rr*(dt-cc1) > pp**(rr-2)*cc2
                    terminal_inequalities += 1
                rational_delta_rows += 1
        rows.append({'p':pp, 'absolute_index':ee, 'first_point_conductor':cc1,
            'second_point_conductor':cc2, 'different_lower_bound':lb,
            'second_cyclotomic_upper_bound_lower':str(F(pp*pp-pp-2)+F(1,pp)),
            'normalized_strict_gap':str(minimum_gap)})
    counts.update({'primes':len(primes), 'derivative_monomials':derivative_terms,
        'derivative_profiles':derivative_profiles, 'cyclotomic_nonidentity_elements':cyclotomic_elements,
        'rational_upper_break_pairs':rational_delta_rows,
        'terminal_conductor_comparisons':terminal_inequalities})

    # Actual terminal columns determine the matrix. Enumerate both full M2
    # and its traceless subspace; use all ordered bases for p=5,7,11 to
    # verify that the dual column maps span the complete terminal dual.
    matrices = bases = column_dual_checks = determinant_checks = 0
    for pp in (5,7,11):
        for a,b,c,d in product(range(pp), repeat=4):
            col1, col2 = (a,c), (b,d)
            assert (col1==(0,0) and col2==(0,0)) == (a==b==c==d==0)
            M = (1+pp*pp*a,pp*pp*b,pp*pp*c,1+pp*pp*d)
            assert (M[0]*M[3]-M[1]*M[2]) % pp**3 == (1+pp*pp*(a+d)) % pp**3
            matrices += 1
            determinant_checks += 1
        for u0,u1,v0,v1 in product(range(pp), repeat=4):
            if (u0*v1-u1*v0) % pp == 0:
                continue
            full = [(u0,u1,0,0),(0,0,u0,u1),(v0,v1,0,0),(0,0,v0,v1)]
            assert rank_mod(full,pp) == 4
            # Restrict d=-a: the four evaluation functionals span all
            # three dual coordinates on sl2 as well.
            restricted = [(u0,u1,0),(-u1,0,u0),(v0,v1,0),(-v1,0,v0)]
            assert rank_mod(restricted,pp) == 3
            bases += 1
            column_dual_checks += 2
    counts.update({'terminal_matrices':matrices,'basis_pairs':bases,
        'column_dual_spanning_checks':column_dual_checks,
        'terminal_determinant_checks':determinant_checks})
    return {'symbolic_identities':symbolic, 'prime_rows':rows,
        'scope_exclusions':['No finite coefficient profile is asserted exhaustive for fields.',
          'No existence of a BT comparison follows from the matrix census.',
          'All actual-field intersections and ramification functoriality use the full written proof.',
          'The exact full least-index conclusion is restricted to (p,e,h)=(5,20,2).']}

try:
    data=run(); status='PASS'; error=None
except Exception:
    data={}; status='FAIL'; error=traceback.format_exc()
record={'status':status, 'actual_utc':datetime.now(timezone.utc).isoformat(),
    'runtime_seconds':time.perf_counter()-started, 'counts':counts,
    'data':data, 'error':error,
    'scope':'Standalone symbolic and exact finite supplement to B98. Rational upper breaks are retained. Actual field theory and all-prime recovery require the full proof.'}
OUT.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='data'},indent=2))
if status!='PASS':
    raise SystemExit(1)
