"""Record completed post-checkpoint10 audits and prepare, but do not run, review06."""
from pathlib import Path
import csv
import hashlib
import json

BASE = Path(__file__).resolve().parent.parent
OUT = BASE / 'output' / 'RESEARCH_SA07'
WORK = BASE / 'work'

prior = json.loads((OUT / 'PROGRESS_REVIEW_STATE.json').read_text())
assert prior['review_number'] == 5
gates = dict(prior['main_gates'])
gates['F.3'] = (
    'The full profinite LM6 A.22 normalizer obligation is now proved by F.3.32, '
    'composed with the actual full-class witness map of F.3.31. The exact '
    'all-genus identity N0(s)M7(s)=9(2s+3)(4s^2+6s-1)LK(s), with nonzero scalar '
    'for every integer s>=3, proves the remaining kernel inclusion over every '
    'Q_l. F.3.33 proves the cuspidality classification for every smooth '
    'geometrically connected affine hyperbolic curve over a number field and '
    'the trivial intersection of cusp inertia with the common kernel of the '
    'maximal pro-prime quotients. F.3.34 independently reconstructs the needed '
    'R-vanishing from six literal Johnson brackets, determinant -203784, the '
    'opened published MSS2015 standard-H multiplicity bound and explicit '
    'stabilization maps. It retains the 2026 formula attribution without '
    'requiring the omitted finite generator checks in that preprint. '
    'Historical documentary obligations, including identification of the '
    'particular manuscript M_alpha and its integral forms, remain individually '
    'recorded; the original ambiguous LM6 reading remains a reading row.'
)
gates['A.4c / H1'] += (
    ' The actual symmetric-square and conjugate-extension maps, the ordinary '
    'etale-integral tangent calculation, and the original Waldschmidt graph '
    'inequality have now also been checked. The integral tangent line has not '
    'been identified with the actual complex Hodge line; the graph has no '
    'constructed third independent algebraic point. These retain the same '
    'nonzero algebraic-h gate.'
)
gates['E.2 separation'] += (
    ' E.2.27 constructs an actual profinite loop outside every profinite '
    'conjugate of the discrete free group whose every lifted power has '
    'integral homology on every finite cover; it constructs no Galois '
    'automorphism. The independently audited affine-completion proof '
    'identifies all affine integral-lattice-preserving automorphisms with '
    'Inn(G) times the stabilizer of H_int, using surjective normalizer '
    'transition maps and one actual global conjugator. The actual boundary '
    'extension block and the Galois/peripheral intersection remain to be '
    'determined. The integral A5-cover counterexample has an actual IA '
    'profinite lift and moves a boundary class into nonzero proper homology; '
    'it supplies no element of the simultaneous Galois transporter.'
)
assessment = {
    'previous_review_number': 5,
    'expected_status_changes': [],
    'movement': True,
    'main_gates': gates,
    'reasoning': (
        'Qualifying movement is the completed proof of the full profinite '
        'normalizer gate, F.3.32-F.3.33, after actualreview05. The former '
        'remaining polynomial-matrix inclusion has now been proved by all36 '
        'exact coefficient identities and the displayed nonvanishing scalar, '
        'and the actual witness map returns the conclusion to every original '
        'subgroup candidate. The general affine-curve result includes the '
        'cuspidal converse and common-kernel assertion. F.3.34 also gives a '
        'complete reconstruction of the source R-vanishing input using the '
        'published multiplicity bound and six checked actual brackets. All307 '
        'canonical statuses and all67 OPEN, READING and DOCUMENTARY-GAP '
        'obligations have been compared; their historical statuses are '
        'unchanged, while their current scope records point to the completed '
        'normalizer result. The credited movement is the closure of this main '
        'gate. The nondiscrete loop, affine-completion characterization, '
        'one-cover IA lift, further H1 source routes, source audits, '
        'computations and typesetting are not separately counted as '
        'qualifying movement. A.2, A.3, H1, the full integral transporter and '
        'the general essential-image questions retain their stated gates. '
        'The two-consecutive-no-movement stopping rule has not been met; '
        'continue the unresolved work.'
    )
}
(WORK / 'timed_review06_assessment.json').write_text(
    json.dumps(assessment, indent=2) + '\n')

events = [
    ('F.3.34', 'independent re-proof',
     'Read the complete six-generator reconstruction, actual H-isotypic map, determinant -203784, published MSS2015 standard-H multiplicity bound and boundary stabilization. Original pp16-17 and29-30 were rechecked, with p30 visually read. The 2026 R formula attribution is retained.'),
    ('E.2.27', 'independent re-proof',
     'Read the full nested-coset loop construction, trace separation of every discrete profinite conjugacy class, normal commutator tails, all integer powers and all conjugate lifted loops. Checked the actual basepoint path and compactification quotient. No automorphism or full transporter follows from this element construction.'),
    ('E.2.28', 'independent re-proof',
     'Read AF1-AF8 in full: virtual-abelian residual finiteness, exact embedded completion, every cover lattice, Q-vector complement conjugacy, Smith-normal-form normalizer, invariant edge sums, surjective solution transitions, one global conjugator and finite-generator characterization. Retained the boundary-extension obstruction and actual Galois scope.'),
    ('E.2.29', 'targeted proof check',
     'Read the complete actual A5 cover construction, saturated boundary sequence, averaged integral nilpotent and qNb=19440. Checked the extension cocycle sign delta eta=(gamma-I)c and inverse, BCL lifting map and exact one-cover limitation. Independent matrix/rerun audit is separately attributed to period_generation.'),
    ('H1-work-47', 'targeted proof check',
     'Read the actual base-change tangent and binomial derivative argument, the p5 coefficients H=3 K=2, and the required a=1 congruence. Algebraicity of the actual complex h has not supplied the needed integral tangent lift.'),
    ('H1-work-48', 'used and rechecked in this run',
     'Opened the original Waldschmidt1988 scan and visually read Theorem4.1 on pp385-386. Checked lambda after exponentiation, kappa=2, G=E-dagger times conjugate E, the exact graph subspace and subgroup classification. Two periods give 6<=8; the graph rank bound supplies no third independent algebraic point.'),
    ('PDF-postcheckpoint10', 'targeted proof check',
     'The 253-page build has no overfull boxes, undefined references/citations, missing characters, fatal errors or LaTeX warnings. Root visually inspected pages147-150,227-229 and253; the new E2.27 and F3.34 displays and tables fit.'),
]
with (WORK / 'root_postcheckpoint10_CHECK_EVENTS.tsv').open('w', newline='') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    writer.writerow(['claim_id','date','who','check','details'])
    for claim, kind, detail in events:
        writer.writerow([claim, '2026-11-19', 'OpenAI GPT-6 Astra /root', kind, detail])

rows = list(csv.DictReader((OUT / 'COMPUTATION_RECORD.tsv').open(), delimiter='\t'))
failures = []
for row in rows:
    for field, expected in [('script', 'script_sha256'), ('output', 'output_sha256')]:
        path = OUT / ('code/' + row[field] if field == 'script' else row[field])
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != row[expected]:
            failures.append({'script': row['script'], 'field': field, 'actual': actual})
    if row['exit_code'] != '0':
        failures.append({'script': row['script'], 'exit_code': row['exit_code']})
assert not failures, failures

report = OUT / 'RESEARCH_SA07_report.md'
heading = '## Audited developments after checkpoint10'
text = report.read_text()
if heading not in text:
    text += '''

## Audited developments after checkpoint10

F.3.34 completes an independent reconstruction of the R-vanishing used in F.3.29-F.3.32. The six actual left-nested Johnson brackets have a six-by-six H-valued contraction minor of determinant -203784 and all six R values zero. The opened published MSS2015 Theorem7.5(iv), including its pp29-30 proof and Proposition3.5(ii), bounds the relevant standard-H multiplicity by six. The actual isotypic projector and the boundary-surface stabilization map then prove vanishing on the full required image in every genus and over every Q_l. The five-term formula remains attributed to MSS2026 Proposition4.1; its omitted finite checks are no longer an unfilled proof step. Root and both independent arithmetic reviewers audited this reconstruction. The registered reconstruction program passes in4.377495seconds, with its exact source/output hashes retained.

E.2.27 constructs a specified element of the actual free profinite group outside every profinite conjugate of a discrete word, while every lifted integer power on every actual finite cover has integral homology. The proof retains the finite trace quotient excluding each word, the nested compact cosets, normal commutator tails, and the change-of-basepoint map. The registered96-stage certificate passes in0.838486seconds; the quantified infinite assertion is proved separately. This loop does not construct a Galois automorphism or a simultaneous motivic transporter.

The253-page build containing these two results has175 numbered statements and47 registered mathematical programs. All47 recorded runs pass, and root checked every retained script/output hash pair with no mismatch. The build has zero overfull boxes, undefined references/citations, missing characters, fatal errors and LaTeX warnings. Root visually inspected pages147-150,227-229 and253. The matrices, cusp-lift maps, polynomial identities and contraction table fit their margins. This is a completed typesetting check, not an hourly movement review.

Further work notes give the actual affine-completion characterization (AF1-AF8), its independent proof audit, an A5 cover with a concrete integral IA lift moving boundary into proper homology, and the simpler cyclic-cover Bass-unit lift. Each retains the exact Galois, peripheral and all-cover maps still required. The original Waldschmidt1988 Theorem4.1 has been read from the scanned pp385-386; its rank counts exponentiated points, and the actual two-period input satisfies its inequality6<=8. The ordinary etale-integral tangent route similarly retains the missing identification of that integral line with the actual complex Hodge line. The main nonzero algebraic-h and full integral-transporter gates remain unchanged by these work results.
'''
    report.write_text(text)
print(json.dumps({'prepared_review': 6, 'review_executed': False,
                  'registered_hash_pairs_verified': len(rows),
                  'root_check_events': len(events)}))
