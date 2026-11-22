#!/usr/bin/env python3
"""Sound all-coordinate-endpoints border-substitution tests, stdlib only.

Every successful test checks ALL coordinate endpoints of the stated
retained dimension.  A single strong restriction is never sufficient.
The stabilizing torus has distinct weights in A and B, so a minimum on
the corresponding Grassmannian is attained at a coordinate endpoint.
"""
import argparse
from itertools import combinations
from multiprocessing import Pool
from pathlib import Path
from collections import Counter
import json
import signal
import time
from br_linear import tensor
from check_koszul import koszul as direct_koszul
from probe_extension_koszul import koszul as general_koszul


def timeout(signum, frame):
    raise TimeoutError('Starting case retained OPEN')


def test_case(record):
    started = time.time()
    result = {'mask': record['mask'], 'subset': record['subset'], 'status': 'OPEN', 'attempts': []}
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(20)
    S = record['subset']
    support, U, aw, bw, _ = tensor(S, 1)
    try:
        for factor, deletion in [('A', 1), ('B', 1), ('A', 2), ('B', 2), ('A', 3)]:
            dimension = 10 if factor == 'A' else len(support)
            threshold = 17 - deletion
            witnesses, failure = [], None
            for removed in combinations(range(dimension), deletion):
                if factor == 'A':
                    chosen = [q for i, q in enumerate(S) if i not in removed]
                    support1, _, _, _, _ = tensor(chosen, 1)
                    if len(support1) > threshold:
                        witnesses.append({'removed': removed, 'test': 'flattening', 'rank': len(support1)})
                        continue
                else:
                    kept = [i for i in range(dimension) if i not in removed]
                    positions = {i: j for j, i in enumerate(kept)}
                    E = [{(a, positions[b]): value for (a, b), value in column.items() if b in positions}
                         for column in U]
                    E = [e for e in E if e]
                    M = {'subset': S, 'support': [support[i] for i in kept],
                         'aw': aw, 'bw': [bw[i] for i in kept]}
                    if len(E) > threshold:
                        witnesses.append({'removed': removed, 'test': 'flattening', 'rank': len(E)})
                        continue
                success = None
                for along, degree in [('A', 1), ('A', 2), ('A', 3), ('A', 4),
                                      ('B', 2), ('B', 3), ('B', 4)]:
                    if factor == 'A':
                        rank, _, cost = direct_koszul(chosen, 1, along, degree, 1000003)
                    else:
                        rank_test = general_koszul(E, M, 1 if along == 'A' else 2, 0, degree)
                        rank, cost = rank_test['rank'], rank_test['cost']
                    if rank > threshold * cost:
                        success = {'removed': removed, 'test': 'Koszul', 'factor': along,
                                   'p': degree, 'rank': rank, 'cost': cost}
                        break
                if success is None:
                    failure = {'removed': removed, 'reason': 'No sufficient direct rank witness'}
                    break
                witnesses.append(success)
            result['attempts'].append({'factor': factor, 'deletion': deletion,
                                       'witnesses': witnesses, 'failure': failure})
            if failure is None:
                result['status'] = 'EXCLUDED'
                result['successful_factor'] = factor
                result['successful_deletion'] = deletion
                break
    except Exception as error:
        result['status'] = 'OPEN'
        result['unhandled'] = type(error).__name__ + ': ' + str(error)
    finally:
        signal.alarm(0)
    result['seconds'] = time.time() - started
    path = Path('certificates/per10_substitution') / (str(record['mask']) + '.json')
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(path)
    return {key: value for key, value in result.items() if key != 'attempts'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=3)
    args = parser.parse_args()
    source = json.loads(Path('certificates/per10_global_gate.json').read_text())
    assert source['status'] == 'COMPLETE'
    Path('certificates/per10_substitution').mkdir(exist_ok=True)
    results, counts = [], Counter()
    start = time.time()
    with Pool(args.workers) as pool:
        for result in pool.imap_unordered(test_case, source['remaining'], chunksize=1):
            results.append(result)
            counts[result['status']] += 1
            out = {'scope': 'All-endpoint substitution refinement of the 596 permanent orbits',
                   'status': 'COMPLETE_GATE' if len(results) == len(source['remaining']) else 'PARTIAL',
                   'processed': len(results), 'total': len(source['remaining']),
                   'counts': dict(counts), 'results': sorted(results, key=lambda r: r['mask']),
                   'seconds': time.time() - start}
            path = Path('certificates/per10_substitution_summary.json')
            temporary = path.with_suffix('.json.tmp')
            temporary.write_text(json.dumps(out, indent=2) + '\n')
            temporary.replace(path)
            print('SUBSTITUTION', len(results), len(source['remaining']), dict(counts),
                  result['mask'], result['status'], time.time() - start, flush=True)


if __name__ == '__main__':
    main()
