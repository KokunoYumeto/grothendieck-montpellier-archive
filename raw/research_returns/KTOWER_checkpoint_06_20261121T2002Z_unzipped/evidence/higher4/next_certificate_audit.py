"""Reconcile next-weight support and completed reports without promoting pending rows.

The initial-field unitary full replay, full alternate-field unitary units,
and fresh complete classical replays are separate required gates.
This script recomputes the exact comparison-support arithmetic and checks
all report hashes. It does not rerun the large unitary models.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from math import gcd, isqrt, prod
import contextlib
import importlib.util
import io
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
INITIAL = HERE/'hecke_general/higher4'
ALTERNATE = HERE/'hecke_minus7/higher4'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def evaluate(coefficients, point):
    result = 0
    for coefficient in coefficients:
        result = result*point+coefficient
    return result


def main():
    native_path = HERE/'native_full_higher_completion_snapshot.py'
    spec = importlib.util.spec_from_file_location('native_report_reconciliation', native_path)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    with contextlib.redirect_stdout(io.StringIO()):
        native.main()
    native_snapshot = json.loads(native_path.with_suffix('.json').read_text())
    native_rows = {r['case']: r for r in native_snapshot['cases']}
    classical_path = HERE/'verify_next_classical.json'
    classical = json.loads(classical_path.read_text()) if classical_path.exists() else None
    if classical:
        assert classical['status'] == 'PASS all nine complete classical model replays'
        assert classical['replay_script_sha256'] == digest(classical_path.with_suffix('.py'))
        assert len(classical['results']) == 9
    initial_classical_path = HERE.parent/'gl2_next_weights.json'
    initial_classical = {r['e']: r for r in json.loads(initial_classical_path.read_text())['degrees']}
    neighbor_path = HERE/'hecke_level_one/u3_weight5_exact_exploration.json'
    results = []
    for e in (32, 34, 36):
        support_path = INITIAL/f'residual_support_e{e}.json'
        support_report = json.loads(support_path.read_text())
        support = support_report['degrees'][0]
        assert support['e'] == e and support['large_primality_assumed'] is False
        assert support_report['classical_data_sha256'] == digest(initial_classical_path)
        data_path = INITIAL/f'harmonic_hecke_e{e}_exact_data.json'
        data = json.loads(data_path.read_text())
        discovery_path = INITIAL/'fast_native'/f'harmonic_k{e-1}_exact_exploration.json'
        discovery = json.loads(discovery_path.read_text())
        assert data['degrees'] == [discovery]
        assert support['discovery_data_sha256'] == digest(discovery_path)
        assert discovery['e'] == e and discovery['k'] == e-1
        unitary = {r['p']: r for r in discovery['results']}
        gl2 = {r['p']: r for r in initial_classical[e]['results']}
        assert set(unitary) == set(gl2) == {7, 13}
        comparisons = []
        for p in (7, 13):
            uv = evaluate(unitary[p]['charpoly_coefficients'], 1+p**e+p**(2*e))
            gv = evaluate(gl2[p]['charpoly_coefficients'], 1+p**(2*e))
            assert uv == unitary[p]['comparison_value'] != 0
            assert gv == gl2[p]['comparison_value'] != 0
            item = next(r for r in support['results'] if r['p'] == p)
            assert (item['unitary_value'], item['classical_value'], item['combined_value']) == (uv, gv, uv*gv)
            comparisons.append(uv*gv)
        common = gcd(*comparisons)
        assert common == support['combined_gcd']
        small = {int(q): a for q, a in support['proved_small_prime_factors'].items()}
        for q, exponent in small.items():
            assert 2 <= q <= support['small_prime_bound'] < 2**31 and exponent > 0
            assert all(q % t for t in range(2, isqrt(q)+1))
        remainder = common//prod(q**a for q, a in small.items())
        assert common == remainder*prod(q**a for q, a in small.items())
        assert remainder == support['exact_remainder_after_small_prime_sieve']
        for factor in support['removed_bounded_integer_factors']:
            assert 1 < factor < 2**31 and remainder % factor == 0
            remainder //= factor
        assert remainder == support['exact_remaining_integer']
        moduli = support['residual_support_moduli']
        assert len(moduli) == 2 and all(m >= 2**31 for m in moduli)
        assert gcd(*moduli) == 1
        for factor in support['residual_support_divisions']:
            assert factor == gcd(remainder, prod(moduli)) > 1
            remainder //= factor
        assert remainder == 1

        replays = []
        for method in ('sum_first', 'cyclic', 'native'):
            report_path = INITIAL/f'ktower_full_{method}_replay_e{e}.json'
            if not report_path.exists():
                continue
            try:
                replay = json.loads(report_path.read_text())
            except json.JSONDecodeError:
                continue
            if 'replay_implementation' not in replay:
                continue
            assert replay['status'] == 'PASS exact full invariant-harmonic linear algebra and Hecke data'
            assert replay['data_sha256'] == digest(data_path)
            assert replay['neighbor_sha256'] == digest(neighbor_path)
            assert len(replay['results']) == 1
            rr = replay['results'][0]
            assert rr['e'] == e and rr['k'] == e-1
            assert rr['harmonic_dimension'] == support['unitary_dimension']
            assert rr['invariant_source_dimension'] == support['source_dimension']
            assert rr['invariant_target_dimension'] == support['target_dimension']
            assert rr['all_neighbor_evaluations'] and rr['exact_characteristic_polynomials']
            assert rr['two_extra_points_each_prime']
            assert rr['comparison_gcd'] == gcd(*(r['comparison_value'] for r in unitary.values()))
            implementation = replay['replay_implementation']
            if method == 'sum_first':
                assert implementation['source_sha256_start'] == implementation['source_sha256_end']
                assert implementation['input_sha256_start'] == implementation['input_sha256_end']
                assert implementation['source_sha256_start'] == {
                    'wrapper': digest(INITIAL/'replay_cyclic_sum_first.py'),
                    'frozen_verifier': digest(INITIAL.parent/'harmonic_hecke_certificate.py'),
                    'integral_driver': digest(INITIAL/'replay_integral_faddeev.py'),
                    'cyclic_module': digest(INITIAL/'cyclic_charpoly_certificate.py')}
                assert implementation['input_sha256_start'] == {'data': digest(data_path), 'neighbors': digest(neighbor_path)}
                assert implementation['all_original_model_checks_retained'] and implementation['explicit_shape_checks_added']
            else:
                assert implementation['other_full_checks_unchanged']
                filename = 'replay_cyclic_charpoly.py' if method == 'cyclic' else 'replay_native_faddeev.py'
                assert implementation['wrapper_sha256'] == digest(INITIAL/filename)
                assert implementation['frozen_verifier_sha256'] == digest(INITIAL.parent/'harmonic_hecke_certificate.py')
                assert implementation['integral_driver_sha256'] == digest(INITIAL/'replay_integral_faddeev.py')
                if method == 'cyclic':
                    assert implementation['certificate_module_sha256'] == digest(INITIAL/'cyclic_charpoly_certificate.py')
            if method != 'native':
                certificates = replay['cyclic_characteristic_polynomial_certificates']
                assert {r['p'] for r in certificates} == {7, 13} and len(certificates) == 2
                assert all(r['e'] == e and r['dimension'] == support['unitary_dimension'] and
                           r['exact_integer_horner_zero'] and r['krylov_determinant_mod_prime'] != 0
                           for r in certificates)
            replays.append({'method': method, 'path': str(report_path.relative_to(HERE)),
                            'sha256': digest(report_path)})

        alt_classical_path = ALTERNATE/f'gl2_e{e}_candidate_certificate.json'
        alt_classical = json.loads(alt_classical_path.read_text())
        assert alt_classical['candidate_moduli'] == moduli and alt_classical['all_units']
        assert alt_classical['source_sha256'] == digest(ALTERNATE/'gl2_twist_residual_certificate.py')
        assert alt_classical['driver_sha256'] == digest(ALTERNATE/'gl2_next_moduli.py')
        cases = []
        for m in moduli:
            r = next(r for r in alt_classical['cases'] if r['modulus'] == m)
            assert r['e'] == e and r['weight'] == 2*e+1 and r['dimension'] == 4*e-3
            assert r['comparison_point'] == 1+2**(2*e)
            assert r['unit'] and r['unresolved_pivot_obstruction'] is None
            assert gcd(r['cubic_determinant'], m) == r['determinant_gcd'] == 1
            assert all(gcd(v, m) == 1 for v in r['all_determinant_pivots'])
            native_row = native_rows[f'e{e}_m{m}']
            complete = native_row['status'].startswith('PASS:')
            cases.append({'modulus': m, 'unitary_complete': complete,
                          'classical_determinant': r['cubic_determinant'],
                          'native_report': native_row})
        classical_complete = classical is not None
        if classical_complete:
            cr = [r for r in classical['results'] if r['e'] == e]
            assert len(cr) == 3 and all(r['entire_numerical_object_equal'] for r in cr)
            assert [r['field'] for r in cr].count(-3) == 1
            assert [r['field'] for r in cr].count(-7) == 2
            for r in cr:
                expected = initial_classical_path if r['field'] == -3 else alt_classical_path
                assert r['data_sha256'] == digest(expected)
                expected_source = HERE.parent/'gl2_uniform.py' if r['field'] == -3 else ALTERNATE/'gl2_twist_residual_certificate.py'
                assert r['source_sha256'] == digest(expected_source)
            assert {r['modulus'] for r in cr if r['field'] == -7} == set(moduli)
        complete = bool(replays) and all(r['unitary_complete'] for r in cases) and classical_complete
        results.append({'e': e, 'K_degree': 2*e, 'all_finite_certificates_complete': complete,
                        'exhaustive_initial_support_checked': True,
                        'support_sha256': digest(support_path), 'initial_data_sha256': digest(data_path),
                        'unitary_dimension': support['unitary_dimension'],
                        'classical_dimension': initial_classical[e]['dimension'],
                        'moduli': moduli, 'initial_full_replays': replays,
                        'all_classical_replayed': classical_complete, 'alternate_cases': cases})
    report = {'checked_utc': datetime.now(timezone.utc).isoformat(),
              'audit_sha256': digest(Path(__file__)),
              'scope': 'Exact support and completed-report reconciliation, not a new large unitary replay; arithmetic conclusion requires the separate checked proof.',
              'classical_replay_sha256': digest(classical_path) if classical else None,
              'native_reconciliation_sha256': digest(native_path.with_suffix('.json')),
              'results': results}
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'complete_degrees': [r['e'] for r in results if r['all_finite_certificates_complete']],
                      'pending_degrees': [r['e'] for r in results if not r['all_finite_certificates_complete']]}), flush=True)


if __name__ == '__main__':
    main()
