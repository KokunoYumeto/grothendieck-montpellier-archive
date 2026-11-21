"""Complete minus-seven verification with a new exact GMP row evaluator.

The original verifier prefix is executed without editing its source: it
independently reconstructs all13 neighbor frames, the entire invariant
harmonic kernel, its identity minor, and every integer of model.txt.
Native code then evaluates every identifying row and both determinants.
This is a complete new computation unless a pre-existing report is matched;
the exact comparison scope is recorded, never inferred from a filename.
"""
from pathlib import Path
from hashlib import sha256
from math import gcd
import argparse
import json
import subprocess
import sys
import time

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
VERIFIER = HERE / 'hecke_minus7/higher4/verify_ring_schur_parallel.py'
NATIVE_SOURCE = HERE / 'ring_full_evaluator.cpp'
NATIVE = HERE / 'ring_full_evaluator'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('case', type=Path)
    parser.add_argument('--threads', type=int, default=1)
    parser.add_argument('--python-sample-checks', action='store_true',
                        help='Compare first/middle/last identifying rows and both extra rows to original Python formulas.')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    assert 1 <= args.threads <= 4
    case = args.case.resolve()
    output = (args.output or case / 'ktower_complete_native_ring.json').resolve()
    start = time.monotonic()
    wrapper_hash = digest(Path(__file__))
    hashes = {name: digest(case / name) for name in ['model.json', 'model.txt']}
    verifier_bytes = VERIFIER.read_bytes()
    verifier_source = verifier_bytes.decode()
    split = verifier_source.index('\n\ndef evaluate(z, w):')
    prefix = verifier_source[:split]
    namespace = {'__file__': str(VERIFIER), '__name__': 'archived_structural_prefix'}
    saved_argv = sys.argv
    try:
        sys.argv = [str(VERIFIER), str(case), str(args.threads)]
        exec(compile(prefix, str(VERIFIER), 'exec'), namespace)
    finally:
        sys.argv = saved_argv
    model = namespace['model']
    q, k, d = model['q'], model['k'], model['dimension']
    e = (1 + 2**(k+1) + 2**(2*k+2)) % q
    assert gcd(e, q) == 1
    command = [str(NATIVE), str(case / 'model.txt'), '--threads', str(args.threads)]
    samples_path = output.with_suffix('.samples.json')
    sample_indices = sorted({0, d//2, d-1, d, d+1}) if args.python_sample_checks else []
    if sample_indices:
        command += ['--sample-rows', ','.join(map(str, sample_indices)),
                    '--sample-output', str(samples_path)]
    native_hashes = {'source': digest(NATIVE_SOURCE), 'executable': digest(NATIVE)}
    proc = subprocess.run(command, text=True, stdout=subprocess.PIPE, check=False)
    native = json.loads(proc.stdout)
    if proc.returncode or native['status'] != 'PASS_NATIVE_COMPLETE':
        failure = {'status': 'NOT_A_COMPLETE_UNIT_CERTIFICATE', 'native': native,
                   'returncode': proc.returncode, 'sha256': hashes,
                   'native_sha256': native_hashes}
        output.with_suffix('.failure.json').write_text(json.dumps(failure, indent=2)+'\n')
        raise RuntimeError('Native calculation did not give a complete unit certificate')
    assert native['modulus'] == q and native['k'] == k
    assert native['dimension'] == d and native['source_dimension'] == len(namespace['source'])
    assert native['comparison_point_modulus'] == e
    assert native['all_recomputed_evaluation_rows'] == d and native['frame_counts'] == [6, 7]
    assert native['unit_pivots_per_determinant'] == d-1
    assert native['native_threads'] == args.threads
    for key in ['det_evaluation', 'det_schur_evaluations', 'det_schur_operator']:
        assert len(native[key]) == 2 and all(0 <= x < q for x in native[key])
    mul, inverse = namespace['mul'], namespace['inverse']
    norm = lambda x: (x[0]*x[0]+x[0]*x[1]+2*x[1]*x[1]) % q
    assert gcd(norm(native['det_evaluation']), q) == 1
    assert tuple(native['det_schur_operator']) == mul(native['det_schur_evaluations'], inverse(native['det_evaluation']))
    assert native['gcd_norm_determinant_modulus'] == gcd(norm(native['det_schur_operator']), q) == 1
    if sample_indices:
        functions_end = verifier_source.index('\n\nd = len(basis)', split)
        exec(compile(verifier_source[split:functions_end], str(VERIFIER), 'exec'), namespace)
        samples = json.loads(samples_path.read_text())
        assert (samples['modulus'], samples['k'], samples['dimension']) == (q, k, d)
        assert [r['index'] for r in samples['rows']] == sample_indices
        for row in samples['rows']:
            point = model['identifying_and_extra_points'][row['index']]
            z, w = [[(x, 0) for x in side] for side in point]
            a = namespace['evaluate'](z, w)
            b2 = namespace['transformed'](z, w, namespace['frames'][2])
            b4 = namespace['transformed'](z, w, namespace['frames'][4])
            s = [namespace['sub'](namespace['sub'](namespace['scale'](x, e*e),
                 namespace['scale'](y, e)), zz) for x, y, zz in zip(a, b2, b4)]
            assert a == list(map(tuple, row['evaluation']))
            assert s == list(map(tuple, row['schur']))
            print('Original Python row comparison PASS', row['index'], flush=True)
    comparisons = []
    for name in ['schur.json', 'verify_ring_schur.json', 'verify_ring_schur_parallel.json', 'ktower_complete_ring.json']:
        path = case / name
        if not path.exists():
            continue
        prior = json.loads(path.read_text())
        assert prior['modulus'] == q and prior['k'] == k and prior['dimension'] == d
        assert prior.get('comparison_point_modulus', prior.get('comparison_point')) == e
        for key in ['det_evaluation', 'det_schur_evaluations', 'det_schur_operator']:
            assert native[key] == prior[key]
        assert prior['gcd_norm_determinant_modulus'] == 1
        if 'all_recomputed_evaluation_rows' in prior:
            assert prior['all_recomputed_evaluation_rows'] == d and prior['unit'] is True
            assert prior['sha256']['model.json'] == hashes['model.json']
            assert prior['sha256']['model.txt'] == hashes['model.txt']
        comparisons.append({'file': name, 'sha256': digest(path),
                            'scope': 'All determinant residues and reported dimensions/parameters match.'})
    assert hashes == {name: digest(case / name) for name in hashes}
    assert native_hashes == {'source': digest(NATIVE_SOURCE), 'executable': digest(NATIVE)}
    report = {
        'status': 'PASS: complete exact native quadratic-algebra unit certificate',
        'modulus': q, 'k': k, 'e': k+1, 'dimension': d,
        'source_dimension': len(namespace['source']), 'target_dimension': len(namespace['target']),
        'comparison_point_modulus': e, 'frame_counts': namespace['frame_counts'],
        'all_recomputed_evaluation_rows': d, 'all_thirteen_frames_per_row': True,
        'entire_harmonic_kernel_verified': True, 'complete_model_text_verified': True,
        'evaluation_method': 'New GMP evaluator; all frame sums combined on orbit coefficients before two sparse projections.',
        'determinant_method': 'Exact scalar elimination for A; quadratic-algebra elimination for S; all inverted pivots are units.',
        'native_threads': args.threads,
        'det_evaluation': native['det_evaluation'],
        'det_schur_evaluations': native['det_schur_evaluations'],
        'det_schur_operator': native['det_schur_operator'],
        'gcd_norm_determinant_modulus': 1, 'unit': True, 'no_primality_assumption': True,
        'python_row_comparison_indices': sample_indices,
        'extra_rows_are_pointwise_comparisons_not_operator_identity_tests': bool(sample_indices),
        'preexisting_report_comparisons': comparisons,
        'numerical_scope': ('New complete computation, with explicitly listed prior determinant comparisons. '
                            'Full independent Python-row replay is separate unless a corresponding completed report is listed.'),
        'sha256': hashes,
        'verifier_sha256': wrapper_hash,
        'archived_verifier_sha256': sha256(verifier_bytes).hexdigest(),
        'unmodified_prefix_sha256': sha256(prefix.encode()).hexdigest(),
        'native_source_sha256': native_hashes['source'],
        'native_executable_sha256': native_hashes['executable'],
        'frame_sha256': digest(VERIFIER.parent.parent / 'neighbor_frames.json'),
        'native_elapsed_seconds': native['elapsed_seconds'],
        'elapsed_seconds': time.monotonic()-start,
    }
    if sample_indices:
        report['sample_output_sha256'] = digest(samples_path)
    temporary = output.with_suffix('.tmp')
    temporary.write_text(json.dumps(report, indent=2)+'\n')
    temporary.replace(output)
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
