"""Focused independent replay of the native producer's carried k=13 control.

This is a producer-equivalence check, not the separate standard-library
full-model certificate for any new high weight. It writes only here.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import contextlib
import hashlib
import importlib.util
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
DRIVER = WORK / 'evidence/higher4/hecke_general/higher4/compute_higher_native.py'
BASELINE = WORK.parent / ('input/RETURN_K17_checkpoint_08_20261121T0616Z/'
                         'evidence/work/hecke_general/higher2/'
                         'harmonic_k13_exact_exploration.json')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def same_matrix(a, b):
    return [[Fraction(x) for x in r] for r in a] == [
        [Fraction(x) for x in r] for r in b]


def main():
    spec = importlib.util.spec_from_file_location('audited_native_driver', DRIVER)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    native.OUT = HERE / 'native_producer_replay'
    native.OUT.mkdir(exist_ok=True)
    with (HERE / 'native_producer_replay.log').open('w') as log:
        with contextlib.redirect_stdout(log):
            native.calculate(13, [7, 13])
    replay_path = native.OUT / 'harmonic_k13_exact_exploration.json'
    fresh = json.loads(replay_path.read_text())
    carried = json.loads(BASELINE.read_text())
    top_keys = ['k', 'e', 'highest_weight', 'source_orbits', 'target_orbits',
                'laplacian', 'harmonic_basis_columns', 'swap_signs',
                'evaluation_points', 'evaluation_matrix',
                'evaluation_determinant', 'neighbors_sha256']
    for key in top_keys:
        assert fresh[key] == carried[key], key
    rows = []
    for current, old in zip(fresh['results'], carried['results'], strict=True):
        for key in ['p', 'dimension', 'cosets', 'scaled_operator',
                    'charpoly_coefficients', 'comparison_point',
                    'comparison_value', 'two_extra_evaluation_checks',
                    'conjugation_similarity_checked']:
            assert current[key] == old[key], (current['p'], key)
        for key in ['transformed_evaluations_0',
                    'transformed_evaluations_omega', 'operator_0',
                    'operator_omega', 'rational_real_form_operator']:
            assert same_matrix(current[key], old[key]), (current['p'], key)
        factors = lambda row: sorted(
            (tuple(x['coefficients']), x['multiplicity'])
            for x in row['charpoly_factors'])
        assert factors(current) == factors(old)
        rows.append({'p': current['p'], 'dimension': current['dimension'],
                     'all_exact_fields_match': True})
    assert [x['p'] for x in rows] == [7, 13]
    output = {
        'status': 'PASS', 'date_utc': datetime.now(timezone.utc).isoformat(),
        'scope': ('Fresh k13 producer run compared against carried complete '
                  'model, all exact structural/matrix/polynomial fields; '
                  'does not certify new high-weight arithmetic outputs.'),
        'driver_sha256': digest(DRIVER),
        'basis_driver_sha256': digest(native.SOURCE),
        'original_model_sha256': digest(native.basis.SOURCE),
        'baseline_path': str(BASELINE), 'baseline_sha256': digest(BASELINE),
        'replay_sha256': digest(replay_path), 'rows': rows,
    }
    (HERE / 'native_producer_audit.json').write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
