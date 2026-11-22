#!/usr/bin/env python3
"""Exact solvable-flag refinements; every timeout/unhandled case stays OPEN."""
import argparse
from collections import Counter
from fractions import Fraction
from multiprocessing import Pool
from pathlib import Path
import contextlib
import json
import signal
import time
import sympy as sp

from permanent_solvable import per_module
from borel_quiver import extension_vectors, linear_combination
from probe_gate_pencils import analyze, decode_flag
from projected_pencils import stratify_projected
import check_det10_gate as gate
import continue_finite_flags as cf


def expired(signum, frame):
    raise TimeoutError('Per-case wall-time limit; original case retained OPEN')


def check_case(job):
    record, limit = job
    mask, subset = record['mask'], record['subset']
    started = time.time()
    signal.signal(signal.SIGALRM, expired)
    signal.alarm(limit)
    result = {'mask': mask, 'subset': subset, 'status': 'OPEN'}
    path = Path('certificates/per10_flags') / (str(mask) + '.json')
    try:
        gate.ab_module = per_module
        cf.ab_module = per_module
        M = per_module(subset)
        result['roots'] = M['roots']
        with open('/dev/null', 'w') as quiet, contextlib.redirect_stdout(quiet):
            initial = gate.run(subset)
            result['initial'] = initial
            surviving, families = [], []
            rigid_tests = []
            for encoded in initial['surviving_flags']:
                flag = decode_flag(encoded, M)
                E = M['U'] + extension_vectors(M, flag)
                failure = cf.test(E, M)
                rigid_tests.append({'flag': encoded, 'failure': failure})
                if failure is None:
                    surviving.append(encoded)
            result['rigid_tests'] = rigid_tests
            refinements = []
            for index, family in enumerate(initial['parameter_branches']):
                if family['projective_dimension'] != 1:
                    families.append({'index': index, 'reason': 'higher-dimensional projective kernel'})
                    continue
                test = analyze(M, family)
                test['index'] = index
                if test['status'] == 'OPEN':
                    F = decode_flag(family['flag_before'], M)
                    E0 = M['U'] + extension_vectors(M, F)
                    K = [{i: Fraction(x) for i, x in vector}
                         for vector in family['kernel_basis']]
                    X, Y = [linear_combination(M['blocks'][family['weight_block']][1], v)
                            for v in K]
                    projected = stratify_projected(E0, X, Y, M)
                    test['projected'] = projected
                    if projected['status'] != 'OPEN':
                        test['status'] = projected['status']
                        test['allowed'] = projected['allowed']
                if test['status'] == 'FINITE':
                    t = sp.Symbol('t')
                    rational = all(point == 'infinity' or sp.Poly(sp.sympify(point), t).degree() == 1
                                   for point in test['allowed'])
                    if rational:
                        continuation = cf.run(initial, family, index, test['allowed'], extra_projected=True)
                        test['continuation'] = continuation
                        if not continuation['survivors'] and not continuation['open_families']:
                            test['status'] = 'EXCLUDED'
                    else:
                        test['unhandled_reason'] = 'nonrational finite flag continuation'
                if test['status'] != 'EXCLUDED':
                    families.append({'index': index, 'reason': test['status']})
                refinements.append(test)
            result['refinements'] = refinements
            result['unhandled_families'] = families
            result['surviving_flags'] = surviving
            if not families and not surviving:
                result['status'] = 'EXCLUDED'
    except Exception as error:
        # A failed or timed-out calculation never eliminates its starting case.
        result['status'] = 'OPEN'
        result['unhandled_error'] = type(error).__name__ + ': ' + str(error)
    finally:
        signal.alarm(0)
    result['seconds'] = time.time() - started
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(path)
    return {key: value for key, value in result.items()
            if key in ('mask', 'subset', 'status', 'seconds', 'unhandled_error', 'roots')}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=6)
    parser.add_argument('--seconds-per-case', type=int, default=60)
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    source = json.loads(Path('certificates/per10_global_gate.json').read_text())
    assert source['status'] == 'COMPLETE'
    records = source['remaining']
    def support_size(record):
        from br_linear import RECTS
        return len({4*r+c for q in record['subset'] for r in RECTS[q][0] for c in RECTS[q][1]})
    records.sort(key=lambda record: (-support_size(record), record['mask']))
    Path('certificates/per10_flags').mkdir(exist_ok=True)
    result, counts = [], Counter()
    earlier_seconds = 0
    if args.resume:
        previous = json.loads(Path('certificates/per10_global_refined.json').read_text())
        result = previous['results']
        assert len({row['mask'] for row in result}) == len(result)
        assert {row['mask'] for row in result} <= {row['mask'] for row in records}
        counts.update(row['status'] for row in result)
        earlier_seconds = previous['seconds']
    completed = {row['mask'] for row in result}
    jobs = [(record, args.seconds_per_case) for record in records if record['mask'] not in completed]
    started = time.time()
    with Pool(args.workers) as pool:
        for row in pool.imap_unordered(check_case, jobs, chunksize=1):
            result.append(row)
            counts[row['status']] += 1
            out = {'scope': 'Refinement of the 596 permanent ten-plane orbit gate',
                   'status': 'COMPLETE_GATE' if len(result) == len(records) else 'PARTIAL',
                   'processed': len(result), 'total': len(records), 'counts': dict(counts),
                   'results': sorted(result, key=lambda row: row['mask']),
                   'seconds': earlier_seconds + time.time() - started}
            destination = Path('certificates/per10_global_refined.json')
            temporary = destination.with_suffix('.json.tmp')
            temporary.write_text(json.dumps(out, indent=2) + '\n')
            temporary.replace(destination)
            print('PERFLAG', len(result), len(records), dict(counts),
                  row['mask'], row['status'], row['seconds'], time.time() - started, flush=True)


if __name__ == '__main__':
    main()
