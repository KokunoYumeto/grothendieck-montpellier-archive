"""Retain the full B95 proof audit and literal unchanged isolated certificate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_remaining_tracefree_rows_candidate.tex'
program = author / 'code/verify_remaining_tracefree_rows.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: '7967d6fbaffaef6eb32fa250ae9e24d403fd0424ff013bdfd79fbca9e1461a86',
    program: 'e229c00b9a5f8071f07a8ce9335844cd42de1c96471f383e399e627437d724bd',
    author_output: 'b30398a4d20e31630bc39fdff7527b2fab68890f439bcf3dd21217183542fd5e',
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for p, h in expected.items():
    assert sha(p) == h, str(p)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 4
isolated = own / 'outputs/B95_independent_run'
isolated.mkdir(exist_ok=False)
copied = isolated / program.name
copied.write_bytes(program.read_bytes())
assert sha(copied) == expected[program]
run = subprocess.run([sys.executable, str(copied)], cwd=isolated,
                     capture_output=True, text=True)
(isolated / 'stdout.txt').write_text(run.stdout)
(isolated / 'stderr.txt').write_text(run.stderr)
preserved = {str(p.relative_to(root)): {'before': h, 'after': sha(p)}
             for p, h in expected.items()}
(isolated / 'author_hashes.json').write_text(json.dumps(preserved, indent=2) + '\n')
assert all(v['before'] == v['after'] for v in preserved.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
original = json.loads(author_output.read_text())
mathematical = lambda d: {k: v for k, v in d.items()
                        if k not in ('actual_utc', 'runtime_seconds')}
assert result['status'] == 'PASS'
assert mathematical(result) == mathematical(original)
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PASS',
    'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source],
    'labels': labels,
    'proof_read_scope': (
        'Entire final four-label proof and entire literal standalone checker read. '
        'The exact repaired filtration paragraph was read separately against its retained prior. '
        'The B94 actual primitive125 point-field lemma was freshly reread in full, and its '
        'complete group, field, coefficient, normality and conductor proof had just received '
        'this auditor\'s full independent B94 audit. All B95 critical coefficient, orientation, '
        'conductor and final image-order steps were independently rederived.'),
    'checks': [
        'The original25 field and the actual high-quotient25 field are both supplied by the original125 comparison. Orienting these two existing fields to the critical pair(a,15), a=7 or11, does not supply125 torsion of the high quotients. The mirrored terminal estimates are always supplied by the original module in that orientation.',
        'For the critical actual degree25 point field the coordinate rows are (5a,125a,15000-625a) and(75,1875,5625), with absolute index60000. B94 places the last ramification line at the high translation line. Both strict prime-parameter branches t<24a and t>24a force z>15000-726a>5550, contrary to the strict lower-break inequality for the coordinate of value75. Hence t=24a.',
        'If z>1110, the degree75 term first changes at75+25z>5625, and all other five-divisible terms have exponent at least80 and first change at least80+5z>5625. Terms involving mixed-characteristic binomial coefficients lie beyond the absolute-index cutoff. Thus an ordinary exponent J=5625-z is forced. At t=24a its first change cannot precede80+5t<1875: it would be uniquely first, since the leading75 term and all higher ordinary/divisible terms are later. Therefore C=(z+4t)/5<=1109. If z<=1110 the bound is immediate. No critical ordinary coefficient is assumed nonzero.',
        'The actual off-diagonal cyclic character has weight zeta^6. Its degree25 field overL has tame uniformizer eigenvalue zeta because25=1 modulo24. The ramification leading map gives C=6 modulo24, so the bound sharpens to1086. Strict normality gives C>24a. This is a necessary interval, not a realization assertion.',
        'The opposite prime pair(9,24-a) has diagonal conductor216 and off-diagonal conductor858 or1362. Equality of the actual shared diagonal characters gives216=24a+4(r-rprime). The opposite congruences and strict residual bounds give exactly r=30,54,78 for a7 and r=6,30,54,78,102,126 for a11. The first three actual compositum upper breaks and the two last root breaks then follow from B94\'s subgroup and quotient maps.',
        'The two last upper breaks are distinct: their equality would require C810 when a7, contrary to C=6 modulo24, or C1410 when a11, beyond1086. Between these last breaks only the larger-break kernel line remains; above both the group is trivial. Below both independent kernel lines survive, and the common degree5^3 quotient fixes the earlier group orders. The repaired wording is now consistent with this exact union filtration.',
        'Independent integration with indices1,5,25,125,625 gives the displayed first three lower breaks and all three closed formulas for V,W,T. Every last upper break is below576. Thus the actual cyclotomic terminal character survives restriction, with exact conductor T=psi_E/L(576). This is the same determinant character bounded below, not a substitute cyclic extension.',
        'The B94 literal column stabilizers supply the actual primitive125 fields and additive characters(a1,w1) overS_h and(v2,d1) overE_low, as well as the exact subgroup extensions E/S_h and E/E_low. In the critical original orientation bmin=a,jmin9 and the root/residual breaks are V,W,Rprime; in the mirrored original orientation bmin9,jmin=a and they are W,V,R. The field intersections and restriction maps remain the actual ones.',
        'For E/S_h, with lower breaks Vo,Wo in either order, the lower-root quotient conductor is Wo when Wo<Vo and(Wo+4Vo)/5 otherwise. Above the final upper break, psi applied to(15600*jmin+4*z_h)/5 is exactly78000*jmin-4*Vo in both cases. For the actual cyclic25 E/E_low with lower breaks Ro,Wo, psi(3120*bmin)=78000*bmin-4*Wo-20*Ro. No disjointness is imposed.',
        'The four high/low threshold maxima follow directly by endpoint evaluation of the displayed affine formulas, splitting a7 at C810. All are strictly below the required primitive-coordinate bounds. In particular for a11 the high threshold is29730-4r<=29706 in one orientation and Wo<=143706 in the other. Thus every restriction argument used lies above its last upper break.',
        'Subtraction produces all eight displayed affine gap formulas. For a7 both sides of C810 give the same differences. Using r<=78 or126 and C<=1086 makes every gap strictly positive, with minimum a1 margin47880 and d1 margin50400. Hence the conductor of the actual sum a1+d1 cannot equal the cyclotomic conductor T, excluding all four remaining(3,4) rows.',
        'The complete B91/B93 reductions leave only residual-wild layer shape(4,4). Its actual image is contained in the stated Iwahori group of order5^9, and its known layer order is5^(1+4+4), so equality follows. This is only a necessary full-image condition. The full Iwahori case, irreducible residual cases, and unrestricted least-index alternative{2,3} remain unresolved.'
    ],
    'primary_source_scope': {
        'new_external_source_openings': [],
        'dependency_audit': 'agents/obstructions_crystals/B94_independent_audit.json',
        'precise_scope': 'No new external-source opening or new PDF inspection is claimed for B95. The complete actual-field and Herbrand dependencies were reread and sourced in the immediately preceding full B94 audit, including the full retained Colmez3.7,3.10,3.13 proofs. The actual B94 primitive125-field lemma was freshly reread for this B95 check.'
    },
    'filtration_wording_delta': {
        'prior_candidate_sha256': '142dc84d07d48613f64e678bc090082c274da76bef4df50f0e715850d1a69498',
        'diff': 'agents/reduction_descent/notes/B95_filtration_wording_repair/exact.diff',
        'scope': 'Replaces the incorrect temporal wording about disappearance of the larger break by the correct between-break survival and triviality above both. Displayed formulas and checker/output are unchanged.'
    },
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'independent_result_utc': result['actual_utc'],
    'program_sha256': sha(copied),
    'all_mathematical_output_identical': True,
    'author_bytes_unchanged': True,
    'exact_certificate_counts': {k: result[k] for k in ('profiles', 'critical_bound_checks', 'binomial_checks')},
    'relative_field_thresholds': result['relative_field_thresholds'],
    'minimum_a_gap': result['minimum_a_gap'],
    'minimum_d_gap': result['minimum_d_gap'],
    'scope': 'Complete four-assertion proof/code audit. All remaining residual-wild tracefree-first-layer rows are excluded; no full-Iwahori exclusion, realization, or unrestricted least-index equality is inferred.'
}
audit = own / 'B95_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([
            now, label, 'independent_full_proof_code_audit', str(source.relative_to(root)),
            'Entire critical coefficient and actual-field conductor proof; B94 dependencies; unchanged isolated checker; exact corrected filtration paragraph',
            'PASS', str(audit.relative_to(root)),
        ]) + '\n')
print(json.dumps({
    'status': 'FULL PASS', 'actual_utc': now, 'record': str(audit.relative_to(root)),
    'candidate_sha256': expected[source], 'labels': labels,
    'independent_runtime_seconds': result['runtime_seconds'],
    'all_mathematical_output_identical': True, 'author_bytes_unchanged': True,
    'profiles': result['profiles'], 'critical_bound_checks': result['critical_bound_checks'],
    'binomial_checks': result['binomial_checks'],
}))
