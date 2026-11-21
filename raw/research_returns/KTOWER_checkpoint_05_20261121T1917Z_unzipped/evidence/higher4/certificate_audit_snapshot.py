#!/usr/bin/env python3
"""Read-only reconciliation of completed reports; writes this audit's snapshot.

No full polynomial/model calculation is rerun. Missing reports are kept pending.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from math import factorial, gcd, prod
import ast
import json
import sys
sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
U = HERE/'hecke_minus7/higher4'
G = HERE/'hecke_general/higher4'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def norm(v, m):
    a, b = v
    return (a*a+a*b+2*b*b) % m


def mul(x, y, m):
    a, b = x
    c, d = y
    return ((a*c-2*b*d) % m, (a*d+b*c+b*d) % m)


old = (U/'verify_ring_schur_parallel.py').read_text()
old_functions = {n.name: ast.dump(n, include_attributes=False)
                 for n in ast.parse(old).body if isinstance(n, ast.FunctionDef)}
generated_checks = []
for p in sorted(U.glob('ktower_ring_verifier_*.py')):
    text = p.read_text()
    functions = {n.name: ast.dump(n, include_attributes=False)
                 for n in ast.parse(text).body if isinstance(n, ast.FunctionDef)}
    names = sorted(set(old_functions)-{'determinant'})
    assert all(old_functions[n] == functions[n] for n in names)
    # Every pre-determinant top-level validation is also byte-identical.
    assert old[old.index('from collections'):old.index('def determinant(matrix):')] == \
           text[text.index('from collections'):text.index('def determinant(matrix):')]
    generated_checks.append({'file': p.name, 'sha256': digest(p),
                             'unchanged_functions': names,
                             'all_pre_determinant_checks_identical': True})

rows = []
for e in (26, 28, 30):
    support_file = G/f'residual_support_e{e}.json'
    support = json.loads(support_file.read_text())['degrees'][0]
    assert support['e'] == e
    moduli = support['residual_support_moduli']
    gl2file = U/f'gl2_e{e}_residual_certificate.json'
    gl2data = json.loads(gl2file.read_text())
    assert gl2data['complete_support_moduli'] == moduli
    assert gl2data['support_data_sha256'] == digest(support_file)
    gl2 = {r['modulus']: r for r in gl2data['cases']}
    assert set(gl2) == set(moduli)
    for m in moduli:
        r = gl2[m]
        assert r['e'] == e and r['dimension'] == 4*e-3
        assert r['comparison_point'] == 1+2**(2*e)
        assert gcd(r['cubic_determinant'], m) == r['determinant_gcd'] == 1
        assert r['unit'] and r['unresolved_pivot_obstruction'] is None
        assert all(gcd(x, m) == 1 for x in r['all_determinant_pivots'])
        case = U/f'e{e}_m{m}'
        candidates = [case/'verify_ring_schur.json',
                      case/'verify_ring_schur_parallel.json',
                      case/'ktower_complete_ring.json']
        present = [p for p in candidates if p.exists()]
        row = {'e': e, 'modulus': m,
               'gl2_dimension': r['dimension'],
               'gl2_determinant': r['cubic_determinant'],
               'gl2_norm_gcd': 1, 'gl2_report_sha256': digest(gl2file),
               'unitary_status': 'pending: no complete report present'}
        if present:
            reports = []
            for p in present:
                v = json.loads(p.read_text())
                assert v['modulus'] == m and v['e'] == e and v['k'] == e-1
                assert v['dimension'] == v['source_dimension']-v['target_dimension']
                assert v['all_recomputed_evaluation_rows'] == v['dimension']
                assert v['comparison_point_modulus'] == (1+2**e+2**(2*e)) % m
                assert gcd(m, 336*factorial(2*e-1)) == 1
                assert gcd(m, 1+2**e+2**(2*e)) == 1
                assert gcd(norm(v['det_evaluation'], m), m) == 1
                assert gcd(norm(v['det_schur_evaluations'], m), m) == 1
                assert gcd(norm(v['det_schur_operator'], m), m) == 1
                assert mul(v['det_schur_operator'], v['det_evaluation'], m) == \
                       tuple(v['det_schur_evaluations'])
                assert v['unit'] and v['gcd_norm_determinant_modulus'] == 1
                assert v['frame_sha256'] == digest(U.parent/'neighbor_frames.json')
                for name, h in v['sha256'].items():
                    assert digest(case/name) == h
                if 'native_source_sha256' in v:
                    assert v['native_source_sha256'] == digest(HERE/'ring_determinant.cpp')
                    assert v['native_executable_sha256'] == digest(HERE/'ring_determinant')
                reports.append({'report': str(p.relative_to(HERE)),
                                'sha256': digest(p),
                                'reported_status': v['status'],
                                'archived_producer_matched': v.get('archived_producer_matched'),
                                'det_evaluation': v['det_evaluation'],
                                'det_schur_operator': v['det_schur_operator'],
                                'dimension': v['dimension']})
            assert all(r['det_schur_operator'] == reports[0]['det_schur_operator']
                       for r in reports)
            row.update(unitary_status='complete report reconciled', reports=reports)
        rows.append(row)

e3 = []
for e in (26, 28, 30):
    path = G/f'harmonic_hecke_e{e}_exact_data.json'
    data = json.loads(path.read_text())
    discovery = json.loads((G/'fast'/f'harmonic_k{e-1}_exact_exploration.json').read_text())
    assert data['degrees'] == [discovery]
    checked = []
    reports = list(G.glob(f'harmonic_hecke_e{e}*certificate.json'))
    full_replay = G/f'ktower_full_replay_e{e}.json'
    if full_replay.exists():
        reports.append(full_replay)
    for p in sorted(reports):
        r = json.loads(p.read_text())
        assert r['data_sha256'] == digest(path)
        assert r['neighbor_sha256'] == digest(HERE/'hecke_level_one/u3_weight5_exact_exploration.json')
        assert len(r['results']) == 1 and r['results'][0]['e'] == e
        x = r['results'][0]
        assert x['all_neighbor_evaluations'] and x['exact_characteristic_polynomials']
        assert x['two_extra_points_each_prime']
        checked.append({'report': p.name, 'sha256': digest(p), 'status': r['status']})
    e3.append({'e': e, 'exact_data_sha256': digest(path),
               'reports': checked,
               'status': 'complete report reconciled' if checked else 'pending: no complete report present'})

out = {'date_utc': datetime.now(timezone.utc).isoformat(),
       'type': 'report reconciliation and exact small checks, not large-model replay',
       'generated_code_checks': generated_checks,
       'source_hashes': {str(p.relative_to(HERE)): digest(p)
                         for p in [HERE/'ring_determinant.cpp', HERE/'ring_determinant',
                                   U/'ktower_complete_ring.py', U/'verify_ring_schur_parallel.py']},
       'alternate_field_cases': rows, 'initial_field_full_replays': e3}
(HERE/'certificate_audit_snapshot.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': 'PASS for present reports',
                  'unitary_complete': [(r['e'],r['modulus']) for r in rows
                                       if r['unitary_status']=='complete report reconciled'],
                  'initial_field_complete': [r['e'] for r in e3 if r['reports']],
                  'generated_scripts_checked': len(generated_checks)}, indent=2))
