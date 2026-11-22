"""Retain the complete B96 independent audit and unchanged isolated rerun."""
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
source = author / 'B_full_Iwahori_selected_point_candidate.tex'
program = author / 'code/verify_full_Iwahori_selected_point.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: 'a56221d040b93f4550b5dcd1cd78fe0ad8dcd833aba3020ed04299da5157778e',
    program: '37f77e0e5eb715602a7c9e63b5ce10f294d974a9b7de21d944a1fc25647f4da5',
    author_output: '7f100c57ea15a459f73de7fa1d06278aa660d4d6e6738845ecd541438fb721ea',
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for p, h in expected.items():
    assert sha(p) == h, str(p)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 6
isolated = own / 'outputs/B96_independent_run'
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
    'status': 'FULL PASS', 'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source], 'labels': labels,
    'proof_read_scope': (
        'Entire final six-label candidate and entire standalone checker read and independently rederived. '
        'Fresh bounded complete reads of B60 lower-break proof, B49 point/coefficient proof and tame-good-field lemma, '
        'B69 rules through the fixed-coefficient proof and the entire actual-quotient lemma, B87 coefficient lemma, '
        'and B94 common-high numerical proof. The entire B94/B95 actual-field and final-layer proofs were already '
        'read in this auditor\'s complete preceding B94 and B95 audits. The final B96 total-ramification scope is explicit.'),
    'checks': [
        'B91--B95 reduce the nontrivial residual-wild case to an actual image contained in the displayed Iwahori group with order5^9. Equality of orders gives the full group; no determinant relation is silently imposed on its nine digits. The finite special-character normalization and common high lines remain the earlier proved hypotheses.',
        'For the original selected point e1/125, direct vector stabilizers are a=w=0, and for e1/25 they are a0=w0=0. Adjoining the residual v0-field yields S fixed by v0=w0=a0=0 and T by these plus a1=w1=0. Multiplication on the S subgroup makes a1,w1 independent additive characters. Thus the relative group is actually F5^2, not merely a quotient of the correct orbit size.',
        'For the opposite orientation, q(e2/125) belongs to the available actual image M[125]/H of type125+25, has exact order125, and its25-multiple is the canonical quotient high point. In the reordered quotient lattice(e2,e1/5), only the first column of [[1+5d,w],[5v,1+5a]] modulo125 is used. That column is determined by the original125 matrix, although the whole quotient125 matrix need not be. The exact stabilizers v0=v1=d0=d1=0 and v0=d0=0 are therefore legitimate.',
        'The quotient residual field is w0. Its S subgroup has w0=v0=d0=0, with independent additive coordinates(d1,v1) and high line v1=0. Thus both orientations give Eh/L25, S/L125, T/L3125 and an actual Galois T/S25. The entire quotient25 module is also supplied by M[125]/H; no whole quotient125 comparison or extra torsion level is introduced.',
        'The coefficient bound underlying B49 is valid without its later prime-index rational-point hypothesis. At B=5b>20, the degree5 coefficient has valuation20b, strictly above the first inverse degree25 chord because20b>4(24-b); it is also above the next inverse chord. Other vertices are controlled by the full coefficient ideals. Thus successive high inverse values are(24-b)/5 and(24-b)/125. Actual field degrees give A=25(24-b), low/high displacements3125b and15625(24-b), and absolute index1500000. Formal-coordinate translation changes are torsion coordinates times units.',
        'Both actual opposite low25 fields have degree125 overL and elementary group25 over their residual field. Their rows are A=5m,D0=125m,D1=15000-625m, cutoff60000. Distinct trivial/off-diagonal tame characters force two breaks, by the injective ramification leading-coefficient map. For two prime parameters, a non-high last line contradicts the full B87 identity, which would give the same largest cyclic quotient conductor24m for both.',
        'For opposite pair(15,19), the prime row forces u+4t=2280 if the high line is not last. The divisible row has leading exponent75 of five-adic order2 and possible first-change slopes25,5,1. All possible minimal ties at t, including missing coefficients and a three-way tie, contradict its low displacement1875 at u. This is a full coefficient argument below60000, not an extrapolation from the finite t test.',
        'After that last-high result, the entire B94 common-high numerical proof applies using exactly the displayed point-coordinate data and no tracefree relation. It gives the four prime-row t values and C values, and for(15,19) gives0<t<360 with C606. Tame invariance of its diagonal quotient and degree25=1 modulo24 imply24 divides t, giving the exact interval24..336.',
        'Over the actual opposite residual w0-field, v0,a0,w1 are independent additive characters. Conjugation by the lower residual unipotent changes a0 by a scalar multiple of v0, giving cond(v0)<=cond(a0); equality is ruled out by their distinct tame weights. Hence0<sigma<tprime<Cprime. The opposite orientation uses the equally actual characters w0,d0,v1 and gives the same strict order.',
        'The actual compositum SZ over the opposite residual field has these three independent characters. Its S quotient uses the first two and its remaining cyclic field is S(w1), or S(v1) in the quotient orientation, inside the selected T. Exact Herbrand transitivity gives z=psi_S/Rstar(Cprime)=25Cprime-20tprime-4sigma. Its kernel in T/S is exactly the high translation line. No disjoint auxiliary extension or wrong base field is substituted.',
        'For the general totally ramified gap lemma, fixed residue representatives lie in the base. Below v_T(5), every five-divisible exponent changes no earlier than A+5h, while the first ordinary exponent J has unique nonzero leading change J+h. This remains true when v5(A)>1. In the single-break case the second bound forces an ordinary term with equal displacement on every nonidentity element, contradicting the high line.',
        'With two breaks t<u and last line different from H, the least-Delta coordinate gives u<=Delta by B60. If t>Delta/5 its ordinary term is uniquely too early on H. Thus t<=Delta/5 and the exact quotient average yields z=(u+4t)/5<=9Delta/25, contradicting the first bound. Hence the last line is H and t=z. The second bound then forces J+t=D0 for every coordinate, and at u all divisible terms grow faster, so D1=J+u below the cutoff. Every displacement gap is therefore u-t.',
        'All five strict conductor bounds exceed both thresholds, using Delta=3150b-600. The necessary finite-character census contains exactly ten pairs; taking their sorted opposite pairs gives precisely the five available orientations. The resulting equality of gaps contradicts D1-D0=375000-18750b for unequal b. This excludes every residual-wild comparison within the stated whole potentially supersingular setting.',
        'The checker is a literal finite supplement. It enumerates all5^9 matrices and fifteen digit field-image maps, separately verifies eight direct vector stabilizers per matrix, and checks all S-subgroup elements times six elementary digit generators in each orientation. This is187500 literal products, not a claim to enumerate all pairs; written multiplication proves the full additive homomorphisms. The remaining conjugation, binomial, mixed-tie, Herbrand and character checks have exactly their stated finite scopes.',
    ],
    'primary_source_scope': {
        'new_external_source_openings': [],
        'fresh_retained_original_read': 'agents/reduction_descent/sources/colmez_corps_locaux.txt: complete Proposition3.7 proof, Lemma3.8, Corollary3.9, Theorem3.10 proof, Definition3.11 and Proposition3.13 proof, printed pp14--16.',
        'retained_original_sha256': sha(author / 'sources/colmez_corps_locaux.txt'),
        'internal_dependencies': ['B_tame_reducible_newton.tex', 'B_tame_minimal_height_two.tex',
                                  'B_one_slope_quotient.tex', 'B_p5_tame_full_first_layer.tex',
                                  'B_both_large_tracefree_rows.tex', 'B_remaining_tracefree_rows.tex'],
        'prior_full_dependency_audits': ['agents/obstructions_crystals/B94_independent_audit.json',
                                         'agents/obstructions_crystals/B95_independent_audit.json'],
        'precise_limits': 'No fresh Hopkins--Gross or Stacks opening and no PDF/image inspection are claimed. The full original coefficient-source statements are supplied by the previously audited B49 chain; only its explicit universal coefficient proof was freshly read here. One guessed dependency filename was absent and was corrected by rg before reading the actual B49 file; no proof claim rests on that failed lookup.'
    },
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'independent_result_utc': result['actual_utc'],
    'program_sha256': sha(copied), 'independent_output_sha256': sha(copied.with_suffix('.output.json')),
    'all_mathematical_output_identical': True, 'author_bytes_unchanged': True,
    'exact_certificate_counts': result['counts'],
    'threshold_rows': result['data']['threshold_rows'],
    'scope': 'Complete six-assertion proof/source/code PASS. The remaining residual-wild branch at p5,e20 is excluded. The irreducible residual cases with wild image orders5^5 through5^8 remain, and the unrestricted least-index alternative{2,3} is not resolved. No remaining-case realization is inferred.'
}
audit = own / 'B96_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_source_code_audit',
                           str(source.relative_to(root)),
                           'Full selected-image torsion, exact actual fields, coefficient/conductor proof; retained Colmez original proofs; unchanged isolated checker',
                           'PASS', str(audit.relative_to(root))]) + '\n')
print(json.dumps({'status': 'FULL PASS', 'actual_utc': now,
                  'record': str(audit.relative_to(root)),
                  'candidate_sha256': expected[source], 'labels': labels,
                  'independent_runtime_seconds': result['runtime_seconds'],
                  'all_mathematical_output_identical': True, 'author_bytes_unchanged': True,
                  'counts': result['counts']}))
