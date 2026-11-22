"""Independent integer and completed-report reconciliation for K80.

This does not execute the large unitary models.  It independently evaluates
the saved exact polynomials and recomputes both 157-dimensional classical
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
M1 = 97006879910137295142114566339844001
M2 = 7108763171297761022563973098474159328699317449544482052462302898913655347936016491916627179
MODULI = [M1, M2]
EXPECTED = {
 'further_vanishing_e40.tex': 'c83012f830cd23921875edfc9a23a4200345b4f679cea1d35898d8076a7709d0',
 'further_certificate_lean_snapshot_e40.json': 'e361ae1f564b607dd6abe5b12f84abaf8038eccd99ebab625018198c23492200',
 'hecke_general/higher4/harmonic_hecke_e40_exact_data.json': '15e9d86e9489fabdf6823b4c069a76e86e14b4e769f0f2240ef61f1b4297d764',
 'hecke_general/higher4/residual_support_e40.json': 'bfc4fdcd5276394b20b3b84e7a06c8f7e4fa101fead4a0b5a527b5352a0e2686',
 'hecke_general/higher4/ktower_full_sum_first_replay_e40.json': 'd90be25e89d8b416da3ab3e701ee75a39b9cd97c3807ef23852f6756b0d81214',
 'verify_further_classical_e40.json': '5349dd81a15907e1f253a7bcaa74bbfc2eefcec5e9b3c932a94ac46eaa308717',
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
    snap = read(H/'further_certificate_lean_snapshot_e40.json')
    se = next(r for r in snap['results'] if r['e'] == 40)
    assert se['all_finite_certificates_complete']
    assert se['exhaustive_initial_support_checked']
    assert len(se['initial_full_replays']) == 1
    assert se['moduli'] == MODULI
    support_top = read(H/'hecke_general/higher4/residual_support_e40.json')
    support = support_top['degrees'][0]
    classical_path = EVIDENCE/'gl2_further_weights.json'
    assert digest(classical_path) == support_top['classical_data_sha256']
    classical = next(r for r in read(classical_path)['degrees'] if r['e'] == 40)
    unitary = read(H/'hecke_general/higher4/harmonic_hecke_e40_exact_data.json')['degrees'][0]
    assert classical['dimension'] == 26
    values = []
    for p in (7, 13):
        u = next(r for r in unitary['results'] if r['p'] == p)
        c = next(r for r in classical['results'] if r['p'] == p)
        s = next(r for r in support['results'] if r['p'] == p)
        assert len(u['charpoly_coefficients']) == 302
        assert len(c['charpoly_coefficients']) == 27
        assert u['charpoly_coefficients'][0] == c['charpoly_coefficients'][0] == 1
        assert int(u['comparison_point']) == 1+p**40+p**80
        assert int(c['comparison_point']) == 1+p**80
        uv = horner(u['charpoly_coefficients'], 1+p**40+p**80)
        cv = horner(c['charpoly_coefficients'], 1+p**80)
        assert uv == int(u['comparison_value']) == int(s['unitary_value'])
        assert cv == int(c['comparison_value']) == int(s['classical_value'])
        assert uv*cv == int(s['combined_value']) != 0
        values.append(uv*cv)
    factors = {2:1237, 3:1481, 5:30, 17:1, 19:3, 23:1, 53:3, 61:2, 263:3}
    assert all(prime_by_trial(p) and p < 2**31 for p in factors)
    exact_gcd = gcd(*values)
    assert exact_gcd == prod(p**a for p,a in factors.items())*M1*M2**3
    assert exact_gcd == int(support['combined_gcd'])
    assert support['residual_support_moduli'] == MODULI
    assert support['large_primality_assumed'] is False
    replay = read(H/'hecke_general/higher4/ktower_full_sum_first_replay_e40.json')
    r = replay['results'][0]
    assert (r['invariant_source_dimension'],r['invariant_target_dimension'],r['harmonic_dimension']) == (3216,2915,301)
    assert all(r[x] for x in ('all_neighbor_evaluations','exact_characteristic_polynomials','two_extra_points_each_prime'))
    imp = replay['replay_implementation']
    assert imp['source_sha256_start'] == imp['source_sha256_end']
    assert imp['input_sha256_start'] == imp['input_sha256_end']
    assert imp['all_original_model_checks_retained'] and imp['explicit_shape_checks_added']
    assert prime_by_trial(1000003)
    for c in replay['cyclic_characteristic_polynomial_certificates']:
        assert c['dimension'] == 301 and c['prime'] == 1000003
        assert c['krylov_determinant_mod_prime'] == {7:186012,13:203153}[c['p']]
        assert c['exact_integer_horner_zero'] and c['monic_degree_equals_dimension']
    gl = read(H/'hecke_minus7/higher4/gl2_e40_candidate_certificate.json')
    cr = read(H/'verify_further_classical_e40.json')
    assert cr['start_sha256'] == cr['end_sha256']
    assert len(cr['results']) == 3
    assert all(r['entire_numerical_object_equal'] for r in cr['results'])
    assert cr['start_sha256']['candidate_data'] == digest(H/'hecke_minus7/higher4/gl2_e40_candidate_certificate.json')
    residue_rows = []
    for modulus, sn in zip(MODULI, se['alternate_cases']):
        folder = H/'hecke_minus7/higher4'/f'e40_m{modulus}'
        n = read(folder/'ktower_complete_native_ring.json')
        assert digest(folder/'ktower_complete_native_ring.json') == sn['native_report']['report_sha256']
        for name, expected in n['sha256'].items():
            assert digest(folder/name) == expected
        assert (n['source_dimension'],n['target_dimension'],n['dimension']) == (28167,25500,2667)
        assert n['all_recomputed_evaluation_rows'] == 2667
        assert all(n[k] for k in ('all_thirteen_frames_per_row','entire_harmonic_kernel_verified','complete_model_text_verified','unit','no_primality_assumption'))
        assert n['frame_counts']['2'][2] + n['frame_counts']['4'][2] == 13
        residues = [n[key] for key in ('det_evaluation','det_schur_evaluations','det_schur_operator')]
        assert all(x[1] == 0 for x in residues)
        A,S,D = [x[0] for x in residues]
        assert A*D % modulus == S
        assert all(gcd(x*x, modulus) == 1 for x in (A,S,D))
        assert gcd(modulus,336*factorial(79)) == 1
        assert gcd(modulus,1+2**40+2**80) == 1
        g = next(r for r in gl['cases'] if r['modulus'] == modulus)
        assert g['dimension'] == 157 and g['weight'] == 81
        assert g['comparison_point'] == 1+2**80
        assert all(gcd(pivot,modulus) == 1 for pivot in g['all_determinant_pivots'])
        assert len(g['all_determinant_pivots']) == 157
        T = g['hecke_matrix']
        T3 = mul(mul(T,T,modulus),T,modulus)
        scalar = pow(1+2**80,3,modulus)
        C = [[((scalar if i == j else 0)-T3[i][j]) % modulus
              for j in range(157)] for i in range(157)]
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
              'completed_large_reports_reconciled':True,'higher_degree_claimed':False,
              'scope':'Exact arithmetic and report reconciliation; the theorem additionally uses the separately whole-read carried comparison criteria.'}
    (HERE/'check_k80.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])
    print('report_sha256',digest(HERE/'check_k80.json'))

if __name__ == '__main__':
    main()
