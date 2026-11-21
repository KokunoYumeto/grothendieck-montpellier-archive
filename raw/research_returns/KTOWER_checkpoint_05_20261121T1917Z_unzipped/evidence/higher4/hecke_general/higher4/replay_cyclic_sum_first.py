"""Full frozen-model replay with exact sum-first neighbor evaluation.

Every neighbor's complete orbit vector is evaluated, summed, and then
projected onto the same harmonic basis once. All original entry checks
remain. A full modular Krylov witness and exact integer Horner identity
certify the whole characteristic polynomial. Inputs and executed source
snapshots are hashed before and after the run; publication is atomic.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import argparse
import json
import sys
import time
import flint

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'harmonic_hecke_certificate.py'
DRIVER = HERE / 'replay_integral_faddeev.py'
CERTIFICATE = HERE / 'cyclic_charpoly_certificate.py'


def digest(content):
    return sha256(content).hexdigest()


def replace_once(source, old, new):
    assert source.count(old) == 1
    return source.replace(old, new)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--neighbors', type=Path,
                        default=SOURCE.parent.parent / 'hecke_level_one/u3_weight5_exact_exploration.json')
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    sources = {'wrapper': Path(__file__).resolve(), 'frozen_verifier': SOURCE,
               'integral_driver': DRIVER, 'cyclic_module': CERTIFICATE}
    snapshots = {name: path.read_bytes() for name, path in sources.items()}
    start_hashes = {name: digest(content) for name, content in snapshots.items()}
    inputs = {'data': args.data.resolve(), 'neighbors': args.neighbors.resolve()}
    input_start = {name: digest(path.read_bytes()) for name, path in inputs.items()}
    output = args.report.resolve()
    assert output not in set(sources.values()) | set(inputs.values())
    pending = output.with_name(output.stem + '.pending.json')
    temporary = output.with_name(output.stem + '.tmp.json')

    certificate_namespace = {'__file__': str(CERTIFICATE), '__name__': 'frozen_cyclic_module'}
    exec(compile(snapshots['cyclic_module'], str(CERTIFICATE), 'exec'), certificate_namespace)
    driver = snapshots['integral_driver'].decode()
    cut = driver.rindex("exec(compile(source,str(SOURCE),'exec')")
    setup = replace_once(driver[:cut], 'source = SOURCE.read_text()',
                         'source = _frozen_source_text')
    namespace = {'__file__': str(DRIVER), '__name__': 'sum_first_setup',
                 '_frozen_source_text': snapshots['frozen_verifier'].decode()}
    exec(compile(setup, str(DRIVER), 'exec'), namespace)
    source = namespace['source']
    source = replace_once(source, namespace['new_faddeev'], '''_cyclic_certificates = []

def characteristic_polynomial(a, claimed, e, p):
    coefficients, certificate = certify_characteristic_polynomial(a, claimed)
    certificate.update({'e':e, 'p':p})
    _cyclic_certificates.append(certificate)
    return coefficients
''')
    source = replace_once(source,
        '        poly = characteristic_polynomial(rational)\n',
        "        poly = characteristic_polynomial(rational, record['charpoly_coefficients'], e, p)\n")
    begin = source.index('def transform_sum(')
    end = source.index('\n\n_cyclic_certificates = []', begin)
    original_transform = source[begin:end]
    assert original_transform.count('def ') == 1
    new_transform = '''def transform_sum(expanded, k, H, point, neighbors):
    global _harmonic_sparse_cache
    if _harmonic_sparse_cache[0] is not H:
        columns = [tuple((i, H[i][j]) for i in range(len(H)) if H[i][j])
                   for j in range(len(H[0]))]
        _harmonic_sparse_cache = (H, columns)
    columns = _harmonic_sparse_cache[1]
    z, w = point
    zero, one = [0]*len(expanded), [0]*len(expanded)
    for neighbor in neighbors:
        zz, ww = [], []
        for column in neighbor['columns']:
            zz.append(tuple(sum(conjugate(column[i])[j]*z[i] for i in range(3)) for j in range(2)))
            ww.append(tuple(sum(column[i][j]*w[i] for i in range(3)) for j in range(2)))
        values = orbit_values(expanded, k, zz, ww)
        for i, (a, b) in enumerate(values):
            zero[i] += a
            one[i] += b
    return ([sum(c*zero[i] for i,c in column) for column in columns],
            [sum(c*one[i] for i,c in column) for column in columns])
'''
    source = replace_once(source, original_transform, new_transform)
    # Make the square-matrix assumptions of the frozen verifier explicit.
    source = replace_once(source, '    d = len(H[0])\n    assert integer_rank(lap)',
        '    d = len(H[0])\n'
        '    assert len(H) == len(source) and all(len(row) == d for row in H)\n'
        '    assert len(lap) == len(target) and all(len(row) == len(source) for row in lap)\n'
        '    assert integer_rank(lap)')
    source = replace_once(source, "    signs = degree['swap_signs']\n",
        "    signs = degree['swap_signs']\n"
        '    assert len(signs) == d and all(sign in (-1,1) for sign in signs)\n')
    source = replace_once(source, '    det = determinant(A)\n',
        '    assert len(points) == len(A) == d and all(len(row) == d for row in A)\n'
        '    assert all(len(point) == 2 and all(len(side) == 3 for side in point) for point in points)\n'
        '    det = determinant(A)\n')
    source = replace_once(source, '        assert matmul(A, M0) == B0 and matmul(A, M1) == B1\n',
        '        assert len(M0) == len(M1) == d and all(len(row) == d for row in M0+M1)\n'
        '        assert matmul(A, M0) == B0 and matmul(A, M1) == B1\n')

    run = {'__name__': '__main__', '__file__': str(SOURCE),
           'certify_characteristic_polynomial': certificate_namespace['certify_characteristic_polynomial']}
    saved_argv = sys.argv
    try:
        sys.argv = [str(SOURCE), '--data', str(inputs['data']), '--neighbors',
                    str(inputs['neighbors']), '--report', str(pending)]
        exec(compile(source, str(SOURCE), 'exec'), run)
    finally:
        sys.argv = saved_argv
    end_hashes = {name: digest(path.read_bytes()) for name, path in sources.items()}
    input_end = {name: digest(path.read_bytes()) for name, path in inputs.items()}
    assert start_hashes == end_hashes, 'source changed during full replay'
    assert input_start == input_end, 'input changed during full replay'
    report = json.loads(pending.read_text())
    assert report['data_sha256'] == input_start['data']
    assert report['neighbor_sha256'] == input_start['neighbors']
    report['cyclic_characteristic_polynomial_certificates'] = run['_cyclic_certificates']
    report['replay_implementation'] = {
        'method': 'sum every complete neighbor orbit vector before harmonic projection',
        'source_sha256_start': start_hashes, 'source_sha256_end': end_hashes,
        'input_sha256_start': input_start, 'input_sha256_end': input_end,
        'effective_verifier_sha256': digest(source.encode()),
        'removed_transform_sha256': digest(original_transform.encode()),
        'native_backend': 'python-flint '+flint.__version__,
        'native_operations': 'integer matrix-vector multiplication and prime-field Krylov determinant only',
        'all_original_model_checks_retained': True, 'explicit_shape_checks_added': True,
        'completed_utc': datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds': time.monotonic()-start,
    }
    temporary.write_text(json.dumps(report, indent=2)+'\n')
    temporary.replace(output)
    pending.unlink()
    print(json.dumps({'complete_report': str(output), 'status': report['status'],
                      'elapsed_seconds': report['replay_implementation']['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
