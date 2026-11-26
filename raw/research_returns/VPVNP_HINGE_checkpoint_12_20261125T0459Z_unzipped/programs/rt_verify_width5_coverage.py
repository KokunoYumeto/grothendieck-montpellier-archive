#!/usr/bin/env python3
"""Verify all selected width-five certificates and complete case coverage.

The analytic exclusions A>=3, D=2..4, and D>=15 are separately proved
in SH-27 and SH-28a. This program checks every remaining minimum branch.
It imports only the independent exact verifiers, never the generators.
"""
import json
import sys
from pathlib import Path

import rt_verify_rank_profile_certificates as radial
import rt_verify_two_minimum_certificates as paired


if __name__ == '__main__':
    cfg = json.loads(Path(sys.argv[1]).read_text())
    singles = [radial.check(Path(p)) for p in cfg['single_certificates']]
    doubles = [paired.check_manifest(Path(p)) for p in cfg['two_minimum_manifests']]
    covered = {}
    for r in singles:
        assert r['width'] == 5 and r['low_value'] is not None
        covered.setdefault((r['dimension'], r['low_value']), []).append(r['file'])
    for r in doubles:
        assert r['width'] == 5 and r['complete_branch_coverage']
        for t in r['first_minima']:
            covered.setdefault((r['dimension'], t), []).append(r['manifest'])
    cases = []
    for D in range(5, 15):
        for t in range(3 * D):
            assert (D, t) in covered, (D, t)
            cases.append({'D': D, 'minimum': t, 'evidence': covered[D, t]})
    out = {
        'result': 'PASS',
        'scope': 'All remaining A=2,m=5 minimum branches for dimensions5..14',
        'analytic_cases_used': 'SH-27: A>=3,D2,D3,D>=15; SH-28a: D4',
        'single_certificates_verified': len(singles),
        'two_minimum_certificates_verified': sum(len(r['checks']) for r in doubles),
        'minimum_branches_covered': len(cases),
        'all_rational_checks_exact': True,
        'all_orbit_sizes_and_pair_distances_independently_checked': True,
        'solver_used_by_verifier': False,
        'coverage': cases,
        'single_checks': singles,
        'two_minimum_checks': doubles,
    }
    Path(sys.argv[2]).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ('coverage', 'single_checks', 'two_minimum_checks')}, indent=2))
