#!/usr/bin/env python3
"""Validate complete-case coverage and merge conservative permanent gates.

This verifies structural completeness of every claimed refinement,
including every substitution endpoint; rank computations were performed
by the cited source checkers and are not reexecuted here.
"""
from itertools import combinations
from math import comb
from pathlib import Path
import json
from br_linear import tensor


def main():
    base = json.loads(Path('certificates/per10_global_gate.json').read_text())
    assert base['status'] == 'COMPLETE' and len(base['remaining']) == 596
    originals = {row['mask']: row for row in base['remaining']}
    flags = json.loads(Path('certificates/per10_global_refined.json').read_text())
    substitutions = json.loads(Path('certificates/per10_substitution_summary.json').read_text())
    flag_excluded, sub_excluded = set(), set()
    for row in flags['results']:
        if row['status'] != 'EXCLUDED':
            continue
        mask = row['mask']
        record = json.loads(Path('certificates/per10_flags', str(mask) + '.json').read_text())
        assert record['mask'] == mask and record['subset'] == originals[mask]['subset']
        assert record['status'] == 'EXCLUDED' and 'unhandled_error' not in record
        assert record['unhandled_families'] == [] and record['surviving_flags'] == []
        initial = record['initial']
        assert len(record['rigid_tests']) == len(initial['surviving_flags'])
        assert [test['flag'] for test in record['rigid_tests']] == initial['surviving_flags']
        assert all(test['failure'] is not None for test in record['rigid_tests'])
        assert [test['index'] for test in record['refinements']] == list(range(len(initial['parameter_branches'])))
        assert all(test['status'] == 'EXCLUDED' for test in record['refinements'])
        for test in record['refinements']:
            if 'continuation' in test:
                continuation = test['continuation']
                assert not continuation['survivors'] and not continuation['open_families']
        flag_excluded.add(mask)
    for row in substitutions['results']:
        if row['status'] != 'EXCLUDED':
            continue
        mask = row['mask']
        record = json.loads(Path('certificates/per10_substitution', str(mask) + '.json').read_text())
        assert record['mask'] == mask and record['subset'] == originals[mask]['subset']
        assert record['status'] == 'EXCLUDED' and 'unhandled' not in record
        attempt = record['attempts'][-1]
        assert attempt['failure'] is None
        factor, deletion = attempt['factor'], attempt['deletion']
        support, U, _, _, _ = tensor(record['subset'], 1)
        dimension = 10 if factor == 'A' else len(support)
        witnesses = attempt['witnesses']
        assert [tuple(w['removed']) for w in witnesses] == list(combinations(range(dimension), deletion))
        threshold = 17 - deletion
        for witness in witnesses:
            removed = witness['removed']
            if factor == 'A':
                chosen = [q for i, q in enumerate(record['subset']) if i not in removed]
                support1 = tensor(chosen, 1)[0]
                a, b = len(chosen), len(support1)
                flattening = b
            else:
                a, b = 10, dimension - deletion
                flattening = sum(any(j not in removed for h, j in column) for column in U)
            if witness['test'] == 'flattening':
                assert witness['rank'] == flattening and flattening > threshold
            else:
                d = a if witness['factor'] == 'A' else b
                assert witness['cost'] == comb(d - 1, witness['p'])
                assert witness['rank'] > threshold * witness['cost']
        sub_excluded.add(mask)
    assert 2015 in originals
    arrangement_excluded = set()
    arrangement_path = Path('certificates/per10_arrangement_refinement.json')
    if arrangement_path.exists():
        arrangement_data = json.loads(arrangement_path.read_text())
        for row in arrangement_data['results']:
            if row['status'] != 'EXCLUDED':
                continue
            mask = row['mask']
            original = json.loads(Path('certificates/per10_flags', str(mask) + '.json').read_text())
            assert row['subset'] == originals[mask]['subset'] and 'unhandled' not in row
            initial = original['initial']
            assert len(original.get('rigid_tests', [])) == len(initial['surviving_flags'])
            assert all(test['failure'] is not None for test in original.get('rigid_tests', []))
            assert [test['index'] for test in row['tests']] == list(range(len(initial['parameter_branches'])))
            previous = {test['index']: test for test in original.get('refinements', [])}
            for test in row['tests']:
                assert test['status'] == 'EXCLUDED'
                if test.get('source') == 'previous complete pencil':
                    assert previous[test['index']]['status'] == 'EXCLUDED'
                else:
                    assert test['allowed_dimensions'] == []
            arrangement_excluded.add(mask)
    excluded = flag_excluded | sub_excluded | arrangement_excluded | {2015}
    remaining = [row for mask, row in sorted(originals.items()) if mask not in excluded]
    assert len(excluded) + len(remaining) == 596
    result = {'claim': 'BR-010', 'scope': 'Characteristic-zero permanent tenth-minimum finite gate',
              'status': 'PASS', 'flag_phase_status': flags['status'],
              'substitution_phase_status': substitutions['status'],
              'flag_processed': flags['processed'], 'substitution_processed': substitutions['processed'],
              'flag_excluded': sorted(flag_excluded), 'substitution_excluded': sorted(sub_excluded),
              'arrangement_excluded': sorted(arrangement_excluded),
              'P20_excluded': 2015, 'union_excluded_count': len(excluded),
              'remaining_count': len(remaining), 'remaining': remaining,
              'ranks_recomputed_in_merge': False}
    path = Path('certificates/per10_combined_gate.json')
    temporary = path.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(path)
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ('remaining', 'flag_excluded', 'substitution_excluded')}), flush=True)


if __name__ == '__main__':
    main()
