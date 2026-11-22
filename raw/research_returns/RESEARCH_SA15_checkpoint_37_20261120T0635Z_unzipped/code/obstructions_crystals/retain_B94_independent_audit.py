"""Complete B94 proof/source audit with literal isolated author-preserving run."""
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
source = author / 'B_both_large_tracefree_rows_candidate.tex'
program = author / 'code/verify_both_large_tracefree_rows.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: '756e9cfc2b38369c603ff21f98dac6210bfc5f2d8bc1c3804f1b273eee2bc44f',
    program: '591eacd022e0ef5347029edf30d1c213b82f3f426297551bea8a175d141a548d',
    author_output: '3cc008f3222d0297bff1e105998503876079e05b3e4cb36c147b2e7b908dc0fc',
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for p, h in expected.items():
    assert sha(p) == h, str(p)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 7
isolated = own / 'outputs/B94_independent_run'
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
        'Entire final seven-label candidate and complete standalone checker read. '
        'The exact typesetting-only four-backslash delta was separately read. '
        'Complete B60 lower-break proof, B49 coefficient/Newton proof and tame-good-field proof, '
        'B69 comparison/actual quotient/Newton proofs, B86 cyclotomic proof, complete B91 layer '
        'reduction and B92 common-high proof, B87 fixed-coefficient and tame-conductor proofs, '
        'and the B93 actual point-field/conductor comparison were freshly reread in their retained '
        'canonical forms. All newly invoked fields, maps and inequalities independently rederived.'),
    'checks': [
        'B91 gives the actual congruence layers sl2 and M2. The determinant modulo25 vanishes on the congruence subgroup, and its factor through the original residual unipotent group vanishes by its nontrivial tame weight. The containing determinant-one-mod25 Iwahori has exactly5^8 elements, so actual-image equality follows from the known order. No abstract group is substituted for an actual field image.',
        'The high quotient has the exact lattice (e1/5,e2), with matrix upper entry5v and lower entryw. The original and quotient mod25 maps have free coordinate sets(v0,w0,a0,v1) and(v0,w0,a0,w1). Their compositum has degree5^5 and terminal kernel1+25 upper triangular. The two additive residual characters v0,w0 are independent.',
        'Determinant triviality modulo25 overL forces mu25 inL, hence inK since L/K is tame. The full B86 Cohen-ring argument identifies K with K0(mu25). Its next cyclotomic extension has break24 overK and576 overL. The finite determinant factor is killed on the good field.',
        'Residual unipotent conjugation on sl2 gives a -> a+t*w and v -> v-2t*a-t^2*w. Conductors of conjugate characters imply rho<=x<=C. Distinct F5-valued tame weights make equality impossible: a hypothetical equal-conductor two-character compositum has a one-break graded group on which the leading coefficient map gives a single tame scalar. The opposite group gives sigma<y<Cprime.',
        'The actual low25 point stabilizer gives a Galois degree25 field over the residual field, whose translation characters are the high upper entry and the diagonal character. The strict order puts the last ramification line at the common high line. For x>r, the maximum-break lift in a residual coset has r=phi_H(M). A lower-root element has commutator with nonzero diagonal and breakD, contradicting b([g,h])>=b(g)+b(h)>D if M>=D. This follows directly from the fixed-representative lower-break bound, with no arbitrary-lift break assignment.',
        'Over the actual shared residual compositum RRprime, the two diagonal characters agree up to sign. Their restricted conductors5x-4rho and5y-4sigma agree, while rho-sigma=5(rprime-r); hence y=x+4(r-rprime). The tame eigenvalue ratio is zeta^(-6b), yielding the displayed opposite congruences. The divisible-coordinate strict B60 bound gives r<600-30b and its quotient analogue. All bases and valuations are indicated.',
        'Both-prime common-high coordinates reproduce the exact strict/boundary first-term table and force t=24m1. For the four mixed rows, A1 is divisible by25. Below v(5)=60000, all terms with p-divisible binomial coefficient are later. The cases t>=24m2 are excluded by the forced ordinary exponents; for t<24m2 the two explicit inequalities force the high change to come from an ordinary exponent and then t<24m1. The leading degreeA1 cannot attain the degree-five equality because v5(A1)=2. Thus the diagonal conductor is a positive multiple24 and the other conductor is3000-126m2.',
        'For(5,13)/(5,17), the shared-diagonal relation leaves(r,x)=(66,24)/(42,24), contradicted by sigma<y. Reversing the original and actual quotient25 groups excludes the two mirror rows without asserting quotient125 torsion. For(5,9)/(15,19), all necessary bounds leave exactly nine(R0,X) profiles each.',
        'The upper filtration of the actual compositum is the stated union of the original and quotient lists. At the largest break the v1 kernel alone survives; just below126 both independent kernel lines survive. At earlier breaks these two kernel lines together with the common degree5^3 quotient determine every order, preventing hidden drops. Integrating the indices1,5,25,125,625 gives all five displayed lower breaks.',
        'Since576 exceeds every last upper break ofE/L, the actual cyclotomic terminal subgroup survives restriction. Its exact conductor is psi_E/L(576), namely803976-20X-2100R0. This is the same determinant character later bounded on Gal(F/E).',
        'Literal first/second column stabilizers give all actual primitive point-field degrees. The quotients overS_h andE_low are normal elementary abelian25 with coordinates(a1,w1) and(v2,d1). E/S_h has the two root-coordinate lower breaks l4,l5; E/E_low is the actual cyclic25 lower-root subgroup, with the two stated lower-break pairs. The intersections T_h capE=S_h(w1) and E_low_plus capE=E_low are accounted for, and no disjointness is imposed.',
        'The high inverse Newton polygons are single segments because B>20: the degree5 coefficient valuation20b lies strictly above both chords, and B49 supplies all intermediate coefficient bounds. High125 coordinates have v_L=j/125, hence value25j inT_h; high translation displacement15625j gives lower bound<=15600j. The one-/two-break analysis bounds a1 by(15600jmin+4z_h)/5 before restriction. Low125 coordinates have value5b in their degree3125 point fields, and every d1-nonzero translation has displacement3125b; quotient averaging bounds d1 by3120bmin. Applying the actual subgroup Herbrand functions produces all four terminal bounds.',
        'On the same terminal group the determinant is1+25(a1+d1). Every one of its18 possible profiles has exact cyclotomic conductor strictly greater than both terminal diagonal bounds. Four immediate rows and these two rows are excluded; the remaining(3,4) pairs are(7,15),(9,13),(9,17),(11,15). Every(4,4) pair and the irreducible-residual sector remain outside the conclusion; no realization or least-index equality is inferred.'
    ],
    'primary_source_scope': {
        'fresh_retained_original_read': 'Pierre Colmez, Corps locaux, Proposition3.7 with full proof, Lemma3.8, Corollary3.9, Theorem3.10 with full proof, and Proposition3.13 with full proof, printed pp14-16.',
        'retained_text': 'agents/reduction_descent/sources/colmez_corps_locaux.txt',
        'retained_text_sha256': sha(author / 'sources/colmez_corps_locaux.txt'),
        'no_inflation': 'No fresh external web opening, new PDF image inspection, or fresh full Hopkins-Gross/Stacks source read is claimed here. Their exact already-audited coefficient/Cohen arguments were reread in the canonical B49/B86 dependencies; the earlier B93 independent source record retains the actual external reading scope.'
    },
    'typography_delta': {
        'prior_candidate_sha256': 'f4ef1b2ae77a8bc2c6fc9bacac0f057df1bc1394a20c77da12f48629a86da7f0',
        'diff': 'agents/reduction_descent/notes/B94_quad_typography_repair/exact.diff',
        'scope': 'Four missing backslashes on quad in equationB-RD94.16 only; no mathematical or checker/output change.'
    },
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'independent_result_utc': result['actual_utc'],
    'program_sha256': sha(copied),
    'all_mathematical_output_identical': True,
    'author_bytes_unchanged': True,
    'exact_certificate_counts': result['counts'],
    'remaining_3_4_pairs': result['remaining_3_4_pairs'],
    'scope': 'Complete seven-assertion proof/source/code audit. Six both-large tracefree-first-layer rows excluded; no full remaining-branch or unrestricted least-index conclusion.'
}
audit = own / 'B94_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([
            now, label, 'independent_full_proof_source_code_audit', str(source.relative_to(root)),
            'Entire actual group/field/conductor proof; invoked dependency steps and full original Herbrand proofs; unchanged isolated checker',
            'PASS', str(audit.relative_to(root)),
        ]) + '\n')
print(json.dumps({
    'status': 'FULL PASS', 'actual_utc': now, 'record': str(audit.relative_to(root)),
    'candidate_sha256': expected[source], 'labels': labels,
    'independent_runtime_seconds': result['runtime_seconds'],
    'all_mathematical_output_identical': True, 'author_bytes_unchanged': True,
}))
