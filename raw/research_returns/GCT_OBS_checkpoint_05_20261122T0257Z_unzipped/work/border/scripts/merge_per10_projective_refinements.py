#!/usr/bin/env python3
"""Conservative structural/hash check of completed BR-011 records.

The exact ranks and polynomial minors are produced by the independently
reviewed search driver.  This merger does not rerun them.  It checks case
identity, complete rigid counts, absence of unhandled projective branches,
and every asserted scalar rank inequality before forming the new gate.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


def validate(row):
    assert row['status'] == 'EXCLUDED' and row['search_complete']
    assert not row.get('unhandled_error')
    assert not row['open_families'] and not row['surviving_flags']
    history = row['history']
    assert history and history[-1]['retained'] == 0
    assert [h['level'] for h in history] == list(range(1, len(history)+1))
    assert len(history) <= 17-len(row['support'])
    failures = Counter(e['level'] for e in row['exclusions'])
    keys = [(e['level'], json.dumps(e['flag'], sort_keys=True)) for e in row['exclusions']]
    assert len(keys) == len(set(keys))
    for h in history:
        assert h['generated']-h['retained'] == failures[h['level']]
        assert h['open_families_so_far'] == 0
    a, b = len(row['subset']), len(row['support'])
    for e in row['exclusions']:
        f = e['failure']
        if f['test'] == 'wedge':
            assert f['ranks']['A'] > 17*(a-1) or f['ranks']['B'] > 17*(b-1)
        elif f['test'] == 'higher_koszul':
            assert f['lower'] > 17
            assert f['rank'] > 17*f['cost']
        elif f['test'] == 'projected_B7':
            assert f['cost'] == 20 and f['rank'] > 340
        elif f['test'] == 'P22':
            assert e['level'] == 17-b and f['P22_dimension'] < 17
        else:
            raise AssertionError('unknown rank test')
    for e in row['arrangements']:
        assert e['test']['allowed_dimensions'] == [len(K) for K in e['cover']]
    for e in row['hypersurface_covers']:
        assert not e['nonlinear_remainder']
        proof = e['evidence']
        assert proof['status'] == 'COMPLETE_LINEAR_COVER'
        witness = proof['attempts'][proof['selected_attempt']]
        assert witness['status'] == 'COVER'
        assert witness['generic_rank_lower'] > witness['threshold']
        assert witness['threshold'] == 17*witness['pure_cost']
        assert not witness['nonlinear_factors']
        assert len(witness['linear_factors']) == len(e['linear_cover'])
        d = len(e['family']['kernel_basis'])
        assert all(len(K) == d-1 for K in e['linear_cover'])
        assert witness['base_rank']+sum(m['rank_lower'] for m in witness['selected_minors']) == witness['generic_rank_lower']
    for e in row['pencils']:
        assert e['result']['status'] in ('EXCLUDED', 'FINITE')


def main():
    root = Path(__file__).resolve().parent.parent
    baseline_path = root/'certificates/per10_combined_gate.json'
    baseline_bytes = baseline_path.read_bytes()
    baseline = json.loads(baseline_bytes)
    assert baseline['status'] == 'PASS' and baseline['remaining_count'] == 381
    records = {r['mask']: r for r in baseline['remaining']}
    assert len(records) == 381
    processed, excluded, hashes = [], [], {}
    for path in sorted((root/'certificates/per10_arranged_flags').glob('*.json')):
        data = path.read_bytes()
        row = json.loads(data)
        mask = row['mask']
        assert mask in records and row['subset'] == records[mask]['subset']
        assert path.stem == str(mask)
        processed.append(mask)
        if row['status'] == 'EXCLUDED':
            validate(row)
            excluded.append(mask)
            hashes[str(path.relative_to(root))] = hashlib.sha256(data).hexdigest()
        else:
            assert row['status'] == 'OPEN'
    assert len(processed) == len(set(processed))
    remaining = [r for m, r in sorted(records.items()) if m not in excluded]
    for relative in ('scripts/refine_per10_arranged_flags.py',
                     'scripts/projective_koszul_cover.py',
                     'scripts/merge_per10_projective_refinements.py'):
        hashes[relative] = hashlib.sha256((root/relative).read_bytes()).hexdigest()
    hashes['certificates/per10_combined_gate.json'] = hashlib.sha256(baseline_bytes).hexdigest()
    out = {'claim': 'BR-011', 'status': 'PASS',
           'scope': 'Conservative characteristic-zero permanent tenth-minimum gate',
           'checked_utc': datetime.now(timezone.utc).isoformat(),
           'phase_status': 'COMPLETE_GATE' if len(processed) == 381 else 'PARTIAL',
           'processed': len(processed), 'baseline_count': 381,
           'new_excluded_count': len(excluded), 'new_excluded_masks': sorted(excluded),
           'remaining_count': len(remaining),
           'remaining_coordinate_subsets': sum(r['orbit_size'] for r in remaining),
           'remaining': remaining, 'ranks_recomputed_in_merge': False,
           'source_and_completed_exclusion_sha256': hashes}
    path = root/'certificates/per10_projective_gate.json'
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out, indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ('remaining', 'source_and_completed_exclusion_sha256')}), flush=True)


if __name__ == '__main__':
    main()
