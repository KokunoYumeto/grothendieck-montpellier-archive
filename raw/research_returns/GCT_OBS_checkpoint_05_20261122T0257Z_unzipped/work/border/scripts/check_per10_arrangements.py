#!/usr/bin/env python3
"""Refine complete OPEN flag certificates using exact first-wedge arrangements.

Only an empty allowed arrangement excludes an unresolved family here.
All nonempty subspaces remain OPEN, irrespective of their dimension.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json
import signal
import time
from permanent_solvable import per_module
from probe_gate_pencils import decode_flag
from first_wedge_arrangement import allowed_subspaces


def expired(signum, frame):
    raise TimeoutError('Original OPEN case retained')


def main():
    signal.signal(signal.SIGALRM, expired)
    source = json.loads(Path('certificates/per10_global_refined.json').read_text())
    results = []
    started = time.time()
    for original in source['results']:
        if original['status'] != 'OPEN':
            continue
        record = json.loads(Path('certificates/per10_flags', str(original['mask']) + '.json').read_text())
        if 'initial' not in record:
            continue
        initial = record['initial']
        if len(record.get('rigid_tests', [])) != len(initial['surviving_flags']):
            continue
        if any(test['failure'] is None for test in record.get('rigid_tests', [])):
            continue
        result = {'mask': original['mask'], 'subset': original['subset'], 'status': 'OPEN', 'tests': []}
        signal.alarm(5)
        try:
            M = per_module(original['subset'])
            previous = {test['index']: test for test in record.get('refinements', [])}
            for index, family in enumerate(initial['parameter_branches']):
                if index in previous and previous[index]['status'] == 'EXCLUDED':
                    result['tests'].append({'index': index, 'status': 'EXCLUDED', 'source': 'previous complete pencil'})
                    continue
                F = decode_flag(family['flag_before'], M)
                K = [{i: Fraction(value) for i, value in vector} for vector in family['kernel_basis']]
                allowed, metadata = allowed_subspaces(M, F, family['weight_block'], K)
                test = {'index': index, 'status': 'OPEN' if allowed else 'EXCLUDED', **metadata}
                result['tests'].append(test)
                if allowed:
                    break
            if (len(result['tests']) == len(initial['parameter_branches'])
                    and all(test['status'] == 'EXCLUDED' for test in result['tests'])):
                result['status'] = 'EXCLUDED'
        except Exception as error:
            result['status'] = 'OPEN'
            result['unhandled'] = type(error).__name__ + ': ' + str(error)
        finally:
            signal.alarm(0)
        results.append(result)
        output = {'scope': 'Exact first-wedge arrangement refinements of completed flag covers',
                  'status': 'COMPLETE_SNAPSHOT', 'flag_processed_at_input': source['processed'],
                  'results': results, 'counts': dict(Counter(row['status'] for row in results)),
                  'seconds': time.time() - started}
        path = Path('certificates/per10_arrangement_refinement.json')
        temporary = path.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(output, indent=2) + '\n')
        temporary.replace(path)
    print(json.dumps({key: value for key, value in output.items() if key != 'results'}), flush=True)


if __name__ == '__main__':
    main()
