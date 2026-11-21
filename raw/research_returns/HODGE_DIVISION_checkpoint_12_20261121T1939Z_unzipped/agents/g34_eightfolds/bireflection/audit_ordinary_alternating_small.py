#!/usr/bin/env python3
"""Independent Ramanujan reconstruction for root HD-ALT02.

Imports only this reviewer's earlier arithmetic. No GAP eigenvalue routine,
root/sibling arithmetic, selected-row list or precomputed spectrum is used.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, lcm
from collections import Counter
from functools import lru_cache
import hashlib
import json
import time
from audit_sporadic_input import encode, reduce_poly, abs_square, rational_mean_abs_square
from check_a1_spectra import spectrum

BASE = Path(__file__).resolve().parent
RESEARCH = BASE.parents[2] / 'research'


@lru_cache(None)
def real(z):
    if isinstance(z, int):
        return True
    n, cs = z
    diff = [0] * n
    for k, a in enumerate(cs):
        diff[k] += a
        diff[-k % n] -= a
    return reduce_poly(diff, n) == (0,)


def main():
    start = time.monotonic()
    raw = (RESEARCH / 'alternating_small_inputs.json').read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == 'f406cf1ad89801369196f36422c4dc2608e5cf96c763e5fab53b8a2ecfa1939c'
    data = json.loads(raw)
    tables = {t['name']: t for t in data['tables']}
    assert set(tables) == {f'{kind}({n})' for n in range(8, 15) for kind in ('Alt', 'Sym')}
    chars = {name: [[encode(z) for z in c] for c in t['characters']] for name, t in tables.items()}
    counts = [0, 0]
    records, small, nonreal = [], [], []
    for name, t in tables.items():
        n = t['n']; cc = chars[name]; alt = name.startswith('Alt')
        assert len(cc) == len(t['orders']) == len(t['sizes'])
        assert all(len(c) == len(cc) for c in cc)
        assert sum(c[0] ** 2 for c in cc) == sum(t['sizes']) == t['order']
        assert t['order'] == factorial(n) // (2 if alt else 1)
        assert t['information'] == 'computed using generic character table for ' + ('alternating' if alt else 'symmetric') + ' groups'
        if not alt:
            assert all(real(z) for c in cc for z in c)
        if 'core' in t:
            u = tables[t['core']]; fus = t['fusion']
            assert t['order'] == 2 * u['order']
            assert len(fus) == len(u['orders'])
            assert [i for i, j in enumerate(fus) if j == 1] == [0]
            assert all(o == t['orders'][j - 1] for o, j in zip(u['orders'], fus))
            for j in set(fus):
                assert sum(s for s, k in zip(u['sizes'], fus) if k == j) == t['sizes'][j - 1]
            powers = {p['prime']: p['map'] for p in t['power_maps']}
            for p in u['power_maps']:
                assert all(fus[k - 1] == powers[p['prime']][j - 1] for j, k in zip(fus, p['map']))
        selected = []
        for i, c in enumerate(cc):
            if c[0] <= 1:
                continue
            if 'core' in t:
                norm = sum(s * rational_mean_abs_square(c[j - 1]) for s, j in zip(u['sizes'], fus)) / u['order']
                assert norm.denominator == 1
                if norm != 1:
                    continue
                restriction = [c[j - 1] for j in fus]
                assert sum(restriction == x for x in chars[t['core']]) == 1
            selected.append(i)
        row_records = []
        for i in selected:
            c = cc[i]; a = c[0]; minima = []
            standard = a == n - 1
            for j, z in enumerate(c):
                if abs_square(z)[1] == (a * a,):
                    continue
                ms = spectrum(t, c, j)
                minima.append((F(a - max(ms), a), j, ms))
                counts[1] += 1
            minimum = min(x[0] for x in minima)
            worst = [{'class': j + 1, 'multiplicities_zero_first': ms} for q, j, ms in minima if q == minimum]
            if not standard:
                assert a >= 14
                assert minimum >= (F(1, 5) if alt else F(1, 7))
            if a <= 15:
                small.append({'table': name, 'row': i + 1, 'degree': a, 'standard': standard})
            if not standard and a == 14:
                assert n == 8 and minimum >= F(1, 4)
                assert t['character_parameters'][i][1] in ([4, 4], [2, 2, 2, 2])
            if alt and not all(real(z) for z in c):
                assert a > 15
                nonreal.append({'table': name, 'row': i + 1, 'degree': a})
            if standard:
                assert minimum >= F(1, n - 1)
            row_records.append({'row': i + 1, 'degree': a, 'standard': standard, 'minimum_ratio': str(minimum), 'worst': worst})
            counts[0] += 1
        records.append({'table': name, 'selected_rows': len(selected), 'rows': row_records})
    assert counts == [682, 49650]
    assert [(r['table'], r['degree']) for r in small if not r['standard']] == [('Alt(8)', 14), ('Sym(8)', 14), ('Sym(8)', 14)]
    assert [r['selected_rows'] for r in records if r['table'].startswith('Alt')] == [13, 17, 23, 30, 42, 54, 71]
    assert [r['selected_rows'] for r in records if r['table'].startswith('Sym')] == [18, 26, 38, 52, 72, 96, 130]
    # Only after independently reconstructing every spectrum, compare all
    # minimizing spectra with the separately retained GAP scan.
    prior = {t['name']: t for t in json.loads((RESEARCH / 'alternating_small_scan.json').read_text())['tables']}
    for t in records:
        old = {r['row']: r for r in prior[t['table']]['rows']}
        assert set(old) == {r['row'] for r in t['rows']}
        for r in t['rows']:
            o = old[r['row']]
            assert o['min_ratio'] == r['minimum_ratio']
            a = {w['class']: w['multiplicities'][-1:] + w['multiplicities'][:-1] for w in o['worst']}
            assert a == {w['class']: list(w['multiplicities_zero_first']) for w in r['worst']}
    tensor = [{'n': n, 'upper': str(F(6 * (n - 1), 11 - n)), 'lower': (n - 1) ** 2} for n in (8, 9, 10)]
    assert all(F(x['upper']) < x['lower'] for x in tensor)
    proof = RESEARCH / 'ordinary_alternating_small_obstruction.tex'
    out = {'status': 'PASS', 'input_sha256': sha, 'proof_sha256': hashlib.sha256(proof.read_bytes()).hexdigest(),
           'method': 'independent rational-trace selection and Ramanujan Fourier; complete minimizing spectra matched only afterward',
           'tables': 14, 'normal_fusions': 7, 'rows': counts[0], 'nonscalar_spectra': counts[1],
           'small_rows': small, 'nonreal_rows': nonreal, 'standard_tensor_bounds': tensor,
           'complete_rows': records, 'seconds': round(time.monotonic() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('complete_rows', 'small_rows', 'nonreal_rows')}))


if __name__ == '__main__':
    main()
