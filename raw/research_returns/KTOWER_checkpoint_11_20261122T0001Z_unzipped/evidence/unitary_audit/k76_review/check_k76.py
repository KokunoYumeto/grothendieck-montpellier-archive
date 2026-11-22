"""Independent integer and completed-report reconciliation for K76.

This does not execute the large unitary models.  It independently evaluates
the saved exact polynomials and recomputes both 149-dimensional classical
cubic determinants over the composite residue rings, using only Python.
"""
from pathlib import Path
from hashlib import sha256
from math import factorial, gcd, isqrt, prod
from datetime import datetime, timezone
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parents[1]
H = EVIDENCE / 'higher4'
M1 = 35578577811063982960672862780147
M2 = 15251674497332588499311578723828894246360050688455945759751526497655448146123593
MODULI = [M1, M2]
EXPECTED = {
 'further_vanishing_e38.tex': '2eed82b4947c8ea66d37b20024530494c91b2aa5d9fe3dda17bd62eebdc0c02f',
 'further_certificate_snapshot_e38.json': '0d036f4bb18ead1388dfb6e683e3a49be07a1785ba98bb0e44921a182cd5edd5',
 'further_certificate_lean_snapshot_e38.json': '0d036f4bb18ead1388dfb6e683e3a49be07a1785ba98bb0e44921a182cd5edd5',
 'hecke_general/higher4/harmonic_hecke_e38_exact_data.json': '80ef1296f3baea6292a9decb7bc274d9c2954852d4d4f1645722543e39b06bd7',
 'hecke_general/higher4/residual_support_e38.json': '33d58cbd24beff9e24850be3f0b5c46a83bdb176858f6fe064a8d0b4a6b0185d',
 'hecke_general/higher4/ktower_full_sum_first_replay_e38.json': '4e4519817db13b7661618f31428b0db521637c6c7b7200f9e1b0cfee152395dc',
 'verify_further_classical_e38.json': 'fd8d0a6492118bcf276e09733c98e62f7d6aeaac956c02ab370e34581e44c8da',
}

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def read(path):
    return json.loads(path.read_text())

def horner(coefficients, x):
    value = 0
    for a in coefficients:
        value = value*x + int(a)
    return value

def prime_by_trial(n):
    return n >= 2 and all(n%d for d in range(2, isqrt(n)+1))

def mul(A, B, modulus):
    columns = list(zip(*B))
    return [[sum(x*y for x, y in zip(row, col)) % modulus
             for col in columns] for row in A]

def unit_det(A, modulus):
    A = [row[:] for row in A]
    determinant = 1
    for j in range(len(A)):
        row = next((i for i in range(j, len(A))
                    if gcd(A[i][j], modulus) == 1), None)
        assert row is not None, ('nonunit pivot obstruction', j)
        if row != j:
            A[row], A[j] = A[j], A[row]
            determinant = -determinant
        pivot = A[j][j] % modulus
        determinant = determinant*pivot % modulus
        inverse = pow(pivot, -1, modulus)
        for i in range(j+1, len(A)):
            scale = A[i][j]*inverse % modulus
            if scale:
                for k in range(j+1, len(A)):
                    A[i][k] = (A[i][k]-scale*A[j][k]) % modulus
            A[i][j] = 0
    return determinant % modulus

def main():
    started = datetime.now(timezone.utc).isoformat()
    hashes = {name: digest(H/name) for name in EXPECTED}
    assert hashes == EXPECTED
    snap = read(H/'further_certificate_snapshot_e38.json')
    s38 = next(r for r in snap['results'] if r['e'] == 38)
    s40 = next(r for r in snap['results'] if r['e'] == 40)
    assert s38['all_finite_certificates_complete']
    assert not s40['all_finite_certificates_complete']
    assert not s40['initial_full_replays']
    assert s38['moduli'] == MODULI
    support_top = read(H/'hecke_general/higher4/residual_support_e38.json')
    support = support_top['degrees'][0]
    classical_path = EVIDENCE/'gl2_further_weights.json'
    assert digest(classical_path) == support_top['classical_data_sha256']
    classical = next(r for r in read(classical_path)['degrees'] if r['e'] == 38)
    unitary = read(H/'hecke_general/higher4/harmonic_hecke_e38_exact_data.json')['degrees'][0]
    assert classical['dimension'] == 24
    values = []
    for p in (7, 13):
        u = next(r for r in unitary['results'] if r['p'] == p)
        c = next(r for r in classical['results'] if r['p'] == p)
        s = next(r for r in support['results'] if r['p'] == p)
        assert len(u['charpoly_coefficients']) == 259
        assert len(c['charpoly_coefficients']) == 25
        assert u['charpoly_coefficients'][0] == c['charpoly_coefficients'][0] == 1
        assert int(u['comparison_point']) == 1+p**38+p**76
        assert int(c['comparison_point']) == 1+p**76
        uv = horner(u['charpoly_coefficients'], 1+p**38+p**76)
        cv = horner(c['charpoly_coefficients'], 1+p**76)
        assert uv == int(u['comparison_value']) == int(s['unitary_value'])
        assert cv == int(c['comparison_value']) == int(s['classical_value'])
        assert uv*cv == int(s['combined_value']) != 0
        values.append(uv*cv)
    factors = {2:1262, 3:1392, 5:127, 11:4, 23:1, 31:1, 2557:3, 15901:3}
    assert all(prime_by_trial(p) and p < 2**31 for p in factors)
    exact_gcd = gcd(*values)
    assert exact_gcd == prod(p**a for p,a in factors.items())*M1*M2**3
    assert exact_gcd == int(support['combined_gcd'])
    assert support['residual_support_moduli'] == MODULI
    assert support['large_primality_assumed'] is False
    replay = read(H/'hecke_general/higher4/ktower_full_sum_first_replay_e38.json')
    r = replay['results'][0]
    assert (r['invariant_source_dimension'],r['invariant_target_dimension'],r['harmonic_dimension']) == (2632,2374,258)
    assert all(r[x] for x in ('all_neighbor_evaluations','exact_characteristic_polynomials','two_extra_points_each_prime'))
    imp = replay['replay_implementation']
    assert imp['source_sha256_start'] == imp['source_sha256_end']
    assert imp['input_sha256_start'] == imp['input_sha256_end']
    assert imp['all_original_model_checks_retained'] and imp['explicit_shape_checks_added']
    assert prime_by_trial(1000003)
    for c in replay['cyclic_characteristic_polynomial_certificates']:
        assert c['dimension'] == 258 and c['prime'] == 1000003
        assert c['krylov_determinant_mod_prime'] == {7:418843,13:575934}[c['p']]
        assert c['exact_integer_horner_zero'] and c['monic_degree_equals_dimension']
    gl = read(H/'hecke_minus7/higher4/gl2_e38_candidate_certificate.json')
    cr = read(H/'verify_further_classical_e38.json')
    assert cr['start_sha256'] == cr['end_sha256']
    assert len(cr['results']) == 3
    assert all(r['entire_numerical_object_equal'] for r in cr['results'])
    assert cr['start_sha256']['candidate_data'] == digest(H/'hecke_minus7/higher4/gl2_e38_candidate_certificate.json')
    residue_rows = []
    for modulus, sn in zip(MODULI, s38['alternate_cases']):
        folder = H/'hecke_minus7/higher4'/f'e38_m{modulus}'
        n = read(folder/'ktower_complete_native_ring.json')
        assert digest(folder/'ktower_complete_native_ring.json') == sn['native_report']['report_sha256']
        for name, expected in n['sha256'].items():
            assert digest(folder/name) == expected
        assert (n['source_dimension'],n['target_dimension'],n['dimension']) == (23014,20728,2286)
        assert n['all_recomputed_evaluation_rows'] == 2286
        assert all(n[k] for k in ('all_thirteen_frames_per_row','entire_harmonic_kernel_verified','complete_model_text_verified','unit','no_primality_assumption'))
        assert n['frame_counts']['2'][2] + n['frame_counts']['4'][2] == 13
        residues = [n[key] for key in ('det_evaluation','det_schur_evaluations','det_schur_operator')]
        assert all(x[1] == 0 for x in residues)
        A,S,D = [x[0] for x in residues]
        assert A*D % modulus == S
        assert all(gcd(x*x, modulus) == 1 for x in (A,S,D))
        assert gcd(modulus,336*factorial(75)) == 1
        assert gcd(modulus,1+2**38+2**76) == 1
        g = next(r for r in gl['cases'] if r['modulus'] == modulus)
        assert g['dimension'] == 149 and g['weight'] == 77
        assert g['comparison_point'] == 1+2**76
        assert all(gcd(pivot,modulus) == 1 for pivot in g['all_determinant_pivots'])
        assert len(g['all_determinant_pivots']) == 149
        T = g['hecke_matrix']
        T3 = mul(mul(T,T,modulus),T,modulus)
        scalar = pow(1+2**76,3,modulus)
        C = [[((scalar if i == j else 0)-T3[i][j]) % modulus
              for j in range(149)] for i in range(149)]
        fresh = unit_det(C,modulus)
        assert fresh == g['cubic_determinant'] == sn['classical_determinant']
        assert gcd(fresh,modulus) == 1
        residue_rows.append({'modulus':modulus,'det_A':A,'det_S':S,'det_D':D,
                             'fresh_classical_cubic_determinant':fresh,
                             'all_unit_checks':True})
    assert {name:digest(H/name) for name in EXPECTED} == hashes
    result = {'status':'PASS independent integer reconciliation and both classical matrix determinants',
              'started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),
              'script_sha256':digest(Path(__file__)),'input_hashes':hashes,
              'polynomial_evaluations_exact':True,'combined_gcd_identity_exact':True,
              'small_prime_factors':factors,'residual_moduli':MODULI,
              'alternate_residues':residue_rows,'large_unitary_replay_performed_here':False,
              'completed_large_reports_reconciled':True,'K80_claimed':False,
              'scope':'Exact arithmetic and report reconciliation; the theorem additionally uses the separately whole-read carried comparison criteria.'}
    (HERE/'check_k76.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])
    print('report_sha256',digest(HERE/'check_k76.json'))

if __name__ == '__main__':
    main()
