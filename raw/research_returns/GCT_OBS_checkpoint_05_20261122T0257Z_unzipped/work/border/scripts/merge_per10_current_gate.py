#!/usr/bin/env python3
"""Union of reviewed BR-011 exclusions and the two BR-012 cases.

This checks the completed certificates and preserves all other cases.
It does not rerun the ranks or imply that a PARTIAL search is complete.
"""
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent
    source = root/'certificates/per10_projective_gate.json'
    source_bytes = source.read_bytes()
    previous = json.loads(source_bytes)
    assert previous['status'] == 'PASS' and previous['claim'] == 'BR-011'
    coupled_path = root/'certificates/per10_unique_coupled.json'
    coupled_bytes = coupled_path.read_bytes()
    coupled = json.loads(coupled_bytes)
    assert coupled['status'] == 'PASS' and coupled['claim'] == 'BR-012'
    assert coupled['new_coupled_ranks_recomputed'] and not coupled['optimization_solver_used']
    assert {r['mask'] for r in coupled['results']} == {13119, 13503}
    masks = set()
    for row in coupled['results']:
        assert row['status'] == 'EXCLUDED'
        assert row['V_dimension'] == 27 and row['R_dimension'] == 36 and row['U_dimension'] == 10
        assert Fraction(row['exact_dual_certificate']['weighted_right_bound']) == Fraction(65, 4) < 17
        prior = root/'certificates/per10_flags'/f"{row['mask']}.json"
        assert hashlib.sha256(prior.read_bytes()).hexdigest() == row['prior_flag_file_sha256']
        masks.add(row['mask'])
    remaining = [r for r in previous['remaining'] if r['mask'] not in masks]
    out = {'status': 'PASS', 'claims': ['BR-010', 'BR-011', 'BR-012'],
           'scope': 'Conservative characteristic-zero permanent tenth-minimum gate',
           'checked_utc': datetime.now(timezone.utc).isoformat(),
           'projective_phase_status': previous['phase_status'],
           'projective_processed': previous['processed'], 'projective_total': previous['baseline_count'],
           'projective_new_exclusions': previous['new_excluded_count'],
           'coupled_exclusions': sorted(masks),
           'remaining_count': len(remaining),
           'remaining_coordinate_subsets': sum(r['orbit_size'] for r in remaining),
           'remaining': remaining, 'ranks_recomputed_in_merge': False,
           'input_sha256': {'certificates/per10_projective_gate.json': hashlib.sha256(source_bytes).hexdigest(),
                            'certificates/per10_unique_coupled.json': hashlib.sha256(coupled_bytes).hexdigest()}}
    path = root/'certificates/per10_current_gate.json'
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out, indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k: v for k, v in out.items() if k not in ('remaining', 'input_sha256')}), flush=True)


if __name__ == '__main__':
    main()
